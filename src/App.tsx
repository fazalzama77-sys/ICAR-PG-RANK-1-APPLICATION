import React, { useState, useEffect } from 'react';
import { TopNav } from './components/navbar/TopNav';
import { Dashboard } from './components/dashboard/Dashboard';
import { TestConfigModal } from './components/config/TestConfigModal';
import { CBTExamContainer } from './components/cbt/CBTExamContainer';
import { QuestionBankView } from './components/questionBank/QuestionBankView';
import { TestSummaryView } from './components/analytics/TestSummaryView';
import { AnalyticsView } from './components/analytics/AnalyticsView';
import { SpacedRepetitionView } from './components/spacedRepetition/SpacedRepetitionView';
import { DrillTestLauncher } from './components/drill/DrillTestLauncher';
import { InstantDrillRunner } from './components/drill/InstantDrillRunner';
import { Question, TestResult, TestConfig, NavigationTab, DrillConfig, DrillPreset } from './types';
import { StorageService, UserProfile } from './storage/db';

export function App() {
  const [activeTab, setActiveTab] = useState<NavigationTab>('dashboard');
  
  // Data states
  const [questions, setQuestions] = useState<Question[]>([]);
  const [testResults, setTestResults] = useState<TestResult[]>([]);
  const [userProfile, setUserProfile] = useState<UserProfile>(StorageService.getUserProfile());

  // Active Exam state (CBT)
  const [isExamActive, setIsExamActive] = useState(false);
  const [activeExamConfig, setActiveExamConfig] = useState<TestConfig | null>(null);
  const [activeExamQuestions, setActiveExamQuestions] = useState<Question[]>([]);

  // Active Instant Drill state
  const [isInstantDrillActive, setIsInstantDrillActive] = useState(false);
  const [activeDrillConfig, setActiveDrillConfig] = useState<DrillConfig | null>(null);
  const [activeDrillQuestions, setActiveDrillQuestions] = useState<Question[]>([]);

  // Selected result for summary review
  const [selectedResult, setSelectedResult] = useState<TestResult | null>(null);

  // Preselected questions for custom config drill
  const [preSelectedQuestions, setPreSelectedQuestions] = useState<Question[] | null>(null);

  // Filter for Spaced Repetition launched from a specific subject
  const [srsSubjectFilter, setSrsSubjectFilter] = useState<string | null>(null);

  const refreshData = () => {
    setQuestions(StorageService.getQuestions());
    setTestResults(StorageService.getTestResults());
    setUserProfile(StorageService.getUserProfile());
  };

  // Load questions and results on mount
  useEffect(() => {
    refreshData();
  }, []);

  // Launch a CBT Exam
  const handleStartExam = (config: TestConfig, examQuestions: Question[]) => {
    setActiveExamConfig(config);
    setActiveExamQuestions(examQuestions);
    setIsExamActive(true);
    setIsInstantDrillActive(false);
  };

  // Launch Instant Interactive Drill
  const handleStartInstantDrill = (config: DrillConfig, drillQuestions: Question[]) => {
    setActiveDrillConfig(config);
    setActiveDrillQuestions(drillQuestions);
    setIsInstantDrillActive(true);
    setIsExamActive(false);
  };

  // Launch preset drill from dashboard directly
  const handleLaunchPresetDrill = (preset: DrillPreset) => {
    let pool = [...questions];
    let title = '🎯 Daily 20-Q Exam Standard Drill';
    let qCount = 20;
    let duration = 15;

    if (preset === 'lightning_10') {
      title = '⚡ Lightning 10-Q Fire Drill';
      qCount = 10;
      duration = 7;
    } else if (preset === 'clinical_blitz') {
      title = '🔬 Paraclinical Core Blitz';
      pool = questions.filter(q => ['vpp', 'vmc', 'vpa'].includes(q.subjectId));
      qCount = 20;
      duration = 15;
    } else if (preset === 'animal_blitz') {
      title = '🐄 Animal Science Core Blitz';
      pool = questions.filter(q => ['lpm', 'agb', 'ann'].includes(q.subjectId));
      qCount = 20;
      duration = 15;
    } else if (preset === 'weak_blitz') {
      title = '🛡️ Weak Areas Blitz Drill';
      const missedIds = new Set<string>();
      testResults.forEach(res => {
        res.questionRecords.forEach(r => {
          if (!r.isCorrect) missedIds.add(r.question.id);
        });
      });
      const missedPool = questions.filter(q => missedIds.has(q.id));
      pool = missedPool.length >= 5 ? missedPool : questions.filter(q => ['vpp', 'vmc', 'vpa'].includes(q.subjectId));
      qCount = Math.min(20, pool.length);
      duration = 15;
    }

    if (pool.length === 0) {
      alert('No questions in your bank match this drill. Please add questions first!');
      return;
    }

    const shuffled = [...pool].sort(() => Math.random() - 0.5).slice(0, Math.min(qCount, pool.length));
    const config: DrillConfig = {
      preset,
      title,
      totalQuestions: shuffled.length,
      durationMinutes: duration,
      feedbackMode: 'instant'
    };

    handleStartInstantDrill(config, shuffled);
  };

  // Exam / Drill finished -> Save result & show summary
  const handleFinishExam = (result: TestResult) => {
    StorageService.saveTestResult(result);
    refreshData();
    setIsExamActive(false);
    setIsInstantDrillActive(false);
    setSelectedResult(result);
    setActiveTab('summary');
  };

  // Exam aborted
  const handleAbortExam = () => {
    if (window.confirm('Are you sure you want to exit the exam? Your current progress will not be evaluated.')) {
      setIsExamActive(false);
      setActiveTab('dashboard');
    }
  };

  // Drill aborted
  const handleAbortDrill = () => {
    setIsInstantDrillActive(false);
    refreshData();
    setActiveTab('dashboard');
  };

  // Retake exam with same questions
  const handleRetakeExam = () => {
    if (selectedResult) {
      handleStartExam(selectedResult.config, selectedResult.config.shuffleQuestions 
        ? [...selectedResult.questionRecords.map(r => r.question)].sort(() => Math.random() - 0.5)
        : selectedResult.questionRecords.map(r => r.question)
      );
    }
  };

  // Launch single subject practice from dashboard
  const handleLaunchSubjectPractice = (subjectId: string) => {
    const subjectQuestions = questions.filter(q => q.subjectId === subjectId);
    if (subjectQuestions.length === 0) {
      alert('No questions in your bank for this subject yet. Add some questions in the Question Bank first!');
      setActiveTab('question_bank');
      return;
    }

    setPreSelectedQuestions(subjectQuestions);
    setActiveTab('cbt_config');
  };

  // Launch Spaced Repetition for single subject
  const handleLaunchSubjectSRS = (subjectId: string) => {
    setSrsSubjectFilter(subjectId);
    setActiveTab('spaced_repetition');
  };

  // Launch practice with filtered questions from Question Bank
  const handleLaunchPracticeWithFiltered = (filtered: Question[]) => {
    setPreSelectedQuestions(filtered);
    setActiveTab('cbt_config');
  };

  // View a specific past result
  const handleViewResult = (result: TestResult) => {
    setSelectedResult(result);
    setActiveTab('summary');
  };

  const srsMetrics = StorageService.getSRSMetrics(questions);

  return (
    <div className="min-h-screen bg-[#f8fafc] text-slate-900 flex flex-col font-sans">
      {/* 1. Top Navigation Bar (Hidden during active examination or instant drill) */}
      <TopNav
        activeTab={activeTab === 'summary' ? 'analytics' : activeTab}
        setActiveTab={(tab) => {
          setPreSelectedQuestions(null);
          setSrsSubjectFilter(null);
          setActiveTab(tab);
        }}
        userProfile={userProfile}
        onProfileUpdate={setUserProfile}
        isExamInProgress={isExamActive || isInstantDrillActive}
        srsDueCount={srsMetrics.dueToday}
      />

      {/* 2. Main Viewport */}
      <main className="flex-1">
        {/* Full CBT Mock Exam Engine */}
        {isExamActive && activeExamConfig && (
          <CBTExamContainer
            config={activeExamConfig}
            questions={activeExamQuestions}
            userProfile={userProfile}
            onFinishExam={handleFinishExam}
            onAbortExam={handleAbortExam}
          />
        )}

        {/* Instant Rapid Drill Runner */}
        {isInstantDrillActive && activeDrillConfig && (
          <InstantDrillRunner
            config={activeDrillConfig}
            questions={activeDrillQuestions}
            userProfile={userProfile}
            onFinishDrill={handleFinishExam}
            onAbortDrill={handleAbortDrill}
            onOpenSpacedRepetition={() => {
              setIsInstantDrillActive(false);
              setActiveTab('spaced_repetition');
            }}
          />
        )}

        {/* Dashboard */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'dashboard' && (
          <Dashboard
            questions={questions}
            testResults={testResults}
            userProfile={userProfile}
            onLaunchCBT={() => {
              setPreSelectedQuestions(null);
              setActiveTab('cbt_config');
            }}
            onLaunchSubjectPractice={handleLaunchSubjectPractice}
            onLaunchSubjectSRS={handleLaunchSubjectSRS}
            onLaunchPresetDrill={handleLaunchPresetDrill}
            onOpenSpacedRepetition={() => {
              setSrsSubjectFilter(null);
              setActiveTab('spaced_repetition');
            }}
            onOpenDrillLauncher={() => setActiveTab('drill_test')}
            onViewResult={handleViewResult}
            onNavigateToBank={() => setActiveTab('question_bank')}
          />
        )}

        {/* Rapid Drill Test Launcher */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'drill_test' && (
          <DrillTestLauncher
            questions={questions}
            onLaunchInstantDrill={handleStartInstantDrill}
            onLaunchCbtExam={handleStartExam}
            onBackToDashboard={() => setActiveTab('dashboard')}
          />
        )}

        {/* Spaced Repetition (Active Recall Flashcards) */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'spaced_repetition' && (
          <SpacedRepetitionView
            questions={questions}
            onBackToDashboard={() => setActiveTab('dashboard')}
            onRefreshData={refreshData}
            initialSubjectFilter={srsSubjectFilter}
          />
        )}

        {/* Take CBT Exam Config Modal */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'cbt_config' && (
          <TestConfigModal
            questions={questions}
            onStartExam={handleStartExam}
            onNavigateToBank={() => setActiveTab('question_bank')}
            preSelectedQuestions={preSelectedQuestions}
          />
        )}

        {/* Question Bank */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'question_bank' && (
          <QuestionBankView
            questions={questions}
            onRefreshQuestions={refreshData}
            onLaunchPracticeWithFiltered={handleLaunchPracticeWithFiltered}
          />
        )}

        {/* Analytics & History */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'analytics' && (
          <AnalyticsView
            testResults={testResults}
            onSelectResult={handleViewResult}
            onRefreshResults={refreshData}
          />
        )}

        {/* Summary & Scorecard */}
        {!isExamActive && !isInstantDrillActive && activeTab === 'summary' && selectedResult && (
          <TestSummaryView
            result={selectedResult}
            onRetakeTest={handleRetakeExam}
            onBackToDashboard={() => setActiveTab('dashboard')}
          />
        )}
      </main>
    </div>
  );
}

export default App;

