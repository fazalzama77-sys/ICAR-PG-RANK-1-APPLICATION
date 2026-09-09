import React, { useState, useEffect } from 'react';
import { TopNav } from './components/navbar/TopNav';
import { Dashboard } from './components/dashboard/Dashboard';
import { TestConfigModal } from './components/config/TestConfigModal';
import { CBTExamContainer } from './components/cbt/CBTExamContainer';
import { QuestionBankView } from './components/questionBank/QuestionBankView';
import { TestSummaryView } from './components/analytics/TestSummaryView';
import { AnalyticsView } from './components/analytics/AnalyticsView';
import { Question, TestResult, TestConfig } from './types';
import { StorageService, UserProfile } from './storage/db';

export function App() {
  const [activeTab, setActiveTab] = useState<'dashboard' | 'cbt_config' | 'question_bank' | 'analytics' | 'summary'>('dashboard');
  
  // Data states
  const [questions, setQuestions] = useState<Question[]>([]);
  const [testResults, setTestResults] = useState<TestResult[]>([]);
  const [userProfile, setUserProfile] = useState<UserProfile>(StorageService.getUserProfile());

  // Active Exam state
  const [isExamActive, setIsExamActive] = useState(false);
  const [activeExamConfig, setActiveExamConfig] = useState<TestConfig | null>(null);
  const [activeExamQuestions, setActiveExamQuestions] = useState<Question[]>([]);

  // Selected result for summary review
  const [selectedResult, setSelectedResult] = useState<TestResult | null>(null);

  // Preselected questions for custom config drill
  const [preSelectedQuestions, setPreSelectedQuestions] = useState<Question[] | null>(null);

  // Load questions and results on mount
  useEffect(() => {
    refreshData();
  }, []);

  const refreshData = () => {
    setQuestions(StorageService.getQuestions());
    setTestResults(StorageService.getTestResults());
    setUserProfile(StorageService.getUserProfile());
  };

  // Launch a CBT Exam
  const handleStartExam = (config: TestConfig, examQuestions: Question[]) => {
    setActiveExamConfig(config);
    setActiveExamQuestions(examQuestions);
    setIsExamActive(true);
  };

  // Exam finished -> Save result & show summary
  const handleFinishExam = (result: TestResult) => {
    StorageService.saveTestResult(result);
    refreshData();
    setIsExamActive(false);
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

  return (
    <div className="min-h-screen bg-[#f8fafc] text-slate-900 flex flex-col font-sans">
      {/* 1. Top Navigation Bar (Hidden during active CBT examination) */}
      <TopNav
        activeTab={activeTab === 'summary' ? 'analytics' : activeTab}
        setActiveTab={(tab) => {
          setPreSelectedQuestions(null);
          setActiveTab(tab);
        }}
        userProfile={userProfile}
        onProfileUpdate={setUserProfile}
        isExamInProgress={isExamActive}
      />

      {/* 2. Main Viewport */}
      <main className="flex-1">
        {isExamActive && activeExamConfig && (
          <CBTExamContainer
            config={activeExamConfig}
            questions={activeExamQuestions}
            userProfile={userProfile}
            onFinishExam={handleFinishExam}
            onAbortExam={handleAbortExam}
          />
        )}

        {!isExamActive && activeTab === 'dashboard' && (
          <Dashboard
            questions={questions}
            testResults={testResults}
            userProfile={userProfile}
            onLaunchCBT={() => {
              setPreSelectedQuestions(null);
              setActiveTab('cbt_config');
            }}
            onLaunchSubjectPractice={handleLaunchSubjectPractice}
            onViewResult={handleViewResult}
            onNavigateToBank={() => setActiveTab('question_bank')}
          />
        )}

        {!isExamActive && activeTab === 'cbt_config' && (
          <TestConfigModal
            questions={questions}
            onStartExam={handleStartExam}
            onNavigateToBank={() => setActiveTab('question_bank')}
            preSelectedQuestions={preSelectedQuestions}
          />
        )}

        {!isExamActive && activeTab === 'question_bank' && (
          <QuestionBankView
            questions={questions}
            onRefreshQuestions={refreshData}
            onLaunchPracticeWithFiltered={handleLaunchPracticeWithFiltered}
          />
        )}

        {!isExamActive && activeTab === 'analytics' && (
          <AnalyticsView
            testResults={testResults}
            onSelectResult={handleViewResult}
            onRefreshResults={refreshData}
          />
        )}

        {!isExamActive && activeTab === 'summary' && selectedResult && (
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
