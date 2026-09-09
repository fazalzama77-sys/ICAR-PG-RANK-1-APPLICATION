import React, { useState, useEffect, useRef } from 'react';
import { Question, TestConfig, UserResponseState, TestResult, Domain, SubjectPerformance, DomainPerformance } from '../../types';
import { UserProfile } from '../../storage/db';
import { SUBJECT_LIST } from '../../data/subjects';
import { CBTHeader } from './CBTHeader';
import { CBTQuestionArea } from './CBTQuestionArea';
import { CBTPalette } from './CBTPalette';
import { CBTBottomActions } from './CBTBottomActions';
import { CBTSubmitModal } from './CBTSubmitModal';

interface CBTExamContainerProps {
  config: TestConfig;
  questions: Question[];
  userProfile: UserProfile;
  onFinishExam: (result: TestResult) => void;
  onAbortExam: () => void;
}

export const CBTExamContainer: React.FC<CBTExamContainerProps> = ({
  config,
  questions,
  userProfile,
  onFinishExam,
  onAbortExam
}) => {
  // Current question index in the overall test array
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);

  // Current active section tab
  const [currentSection, setCurrentSection] = useState<Domain>(
    questions.length > 0 ? questions[0].domain : 'veterinary_science'
  );

  // User responses dictionary: questionId -> UserResponseState
  const [userResponses, setUserResponses] = useState<Record<string, UserResponseState>>(() => {
    const initial: Record<string, UserResponseState> = {};
    questions.forEach((q, idx) => {
      initial[q.id] = {
        selectedOptionIndex: null,
        state: idx === 0 ? 'NOT_ANSWERED' : 'NOT_VISITED',
        timeSpentSeconds: 0,
        visited: idx === 0
      };
    });
    return initial;
  });

  // Timer states (in seconds)
  const initialDuration = config.durationMinutes > 0 ? config.durationMinutes * 60 : 120 * 60;
  const [timeRemaining, setTimeRemaining] = useState(initialDuration);
  const [timeSpentTotal, setTimeSpentTotal] = useState(0);
  const [isTimeExpired, setIsTimeExpired] = useState(false);

  // Submit confirmation modal toggle
  const [showSubmitModal, setShowSubmitModal] = useState(false);

  // Fullscreen state
  const [isFullscreen, setIsFullscreen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // Track time remaining with interval
  useEffect(() => {
    if (config.durationMinutes === 0) return; // Untimed practice mode

    const timer = setInterval(() => {
      setTimeRemaining(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          setIsTimeExpired(true);
          setShowSubmitModal(true);
          return 0;
        }
        return prev - 1;
      });

      setTimeSpentTotal(prev => prev + 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [config.durationMinutes]);

  // Track time spent per active question
  useEffect(() => {
    const activeQ = questions[currentQuestionIndex];
    if (!activeQ) return;

    const interval = setInterval(() => {
      setUserResponses(prev => {
        const existing = prev[activeQ.id];
        if (!existing) return prev;
        return {
          ...prev,
          [activeQ.id]: {
            ...existing,
            timeSpentSeconds: existing.timeSpentSeconds + 1
          }
        };
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [currentQuestionIndex, questions]);

  // Fullscreen toggle handler
  const handleToggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().then(() => setIsFullscreen(true)).catch(() => {});
    } else {
      document.exitFullscreen().then(() => setIsFullscreen(false)).catch(() => {});
    }
  };

  const activeQuestion = questions[currentQuestionIndex];
  const activeResponse = activeQuestion ? userResponses[activeQuestion.id] : null;
  const selectedOption = activeResponse ? activeResponse.selectedOptionIndex : null;

  // Question counts by section
  const sectionCounts = {
    veterinary_science: questions.filter(q => q.domain === 'veterinary_science').length,
    animal_science: questions.filter(q => q.domain === 'animal_science').length
  };

  // Switch question helper
  const navigateToQuestion = (newIndex: number) => {
    if (newIndex < 0 || newIndex >= questions.length) return;

    const targetQ = questions[newIndex];
    
    // Automatically switch section if target question belongs to the other section
    if (targetQ && targetQ.domain !== currentSection) {
      setCurrentSection(targetQ.domain);
    }

    // Update target question's status if it was NOT_VISITED to NOT_ANSWERED
    setUserResponses(prev => {
      const targetState = prev[targetQ.id];
      if (targetState && targetState.state === 'NOT_VISITED') {
        return {
          ...prev,
          [targetQ.id]: {
            ...targetState,
            state: 'NOT_ANSWERED',
            visited: true
          }
        };
      }
      return prev;
    });

    setCurrentQuestionIndex(newIndex);
  };

  // Section Tab Click: Jumps to the first question of that section
  const handleSectionTabChange = (newSection: Domain) => {
    setCurrentSection(newSection);
    const firstQIndex = questions.findIndex(q => q.domain === newSection);
    if (firstQIndex !== -1) {
      navigateToQuestion(firstQIndex);
    }
  };

  // Radio option selection
  const handleSelectOption = (optionIndex: number) => {
    if (!activeQuestion) return;
    setUserResponses(prev => ({
      ...prev,
      [activeQuestion.id]: {
        ...prev[activeQuestion.id],
        selectedOptionIndex: optionIndex
      }
    }));
  };

  // 1. Save & Next
  const handleSaveAndNext = () => {
    if (!activeQuestion) return;

    setUserResponses(prev => {
      const current = prev[activeQuestion.id];
      const hasOption = current.selectedOptionIndex !== null;
      return {
        ...prev,
        [activeQuestion.id]: {
          ...current,
          state: hasOption ? 'ANSWERED' : 'NOT_ANSWERED'
        }
      };
    });

    if (currentQuestionIndex < questions.length - 1) {
      navigateToQuestion(currentQuestionIndex + 1);
    }
  };

  // 2. Save & Mark for Review
  const handleSaveAndMarkForReview = () => {
    if (!activeQuestion) return;

    setUserResponses(prev => {
      const current = prev[activeQuestion.id];
      return {
        ...prev,
        [activeQuestion.id]: {
          ...current,
          state: 'ANSWERED_AND_MARKED_FOR_REVIEW'
        }
      };
    });

    if (currentQuestionIndex < questions.length - 1) {
      navigateToQuestion(currentQuestionIndex + 1);
    }
  };

  // 3. Clear Response
  const handleClearResponse = () => {
    if (!activeQuestion) return;

    setUserResponses(prev => ({
      ...prev,
      [activeQuestion.id]: {
        ...prev[activeQuestion.id],
        selectedOptionIndex: null,
        state: 'NOT_ANSWERED'
      }
    }));
  };

  // 4. Mark for Review & Next
  const handleMarkForReviewAndNext = () => {
    if (!activeQuestion) return;

    setUserResponses(prev => ({
      ...prev,
      [activeQuestion.id]: {
        ...prev[activeQuestion.id],
        state: 'MARKED_FOR_REVIEW'
      }
    }));

    if (currentQuestionIndex < questions.length - 1) {
      navigateToQuestion(currentQuestionIndex + 1);
    }
  };

  // Evaluate and compile final test result
  const handleFinalSubmit = () => {
    let attempted = 0;
    let correct = 0;
    let incorrect = 0;
    let unattempted = 0;
    let markedForReview = 0;
    let totalScore = 0;

    const subjectStatsMap: Record<string, SubjectPerformance> = {};
    const domainStatsMap: Record<Domain, DomainPerformance> = {
      veterinary_science: {
        domain: 'veterinary_science',
        totalQuestions: 0,
        attempted: 0,
        correct: 0,
        incorrect: 0,
        score: 0,
        maxScore: 0,
        accuracy: 0
      },
      animal_science: {
        domain: 'animal_science',
        totalQuestions: 0,
        attempted: 0,
        correct: 0,
        incorrect: 0,
        score: 0,
        maxScore: 0,
        accuracy: 0
      }
    };

    const questionRecords = questions.map(q => {
      const resp = userResponses[q.id] || {
        selectedOptionIndex: null,
        state: 'NOT_VISITED',
        timeSpentSeconds: 0,
        visited: false
      };

      // In NTA CBT, only ANSWERED and ANSWERED_AND_MARKED_FOR_REVIEW are evaluated for marks!
      const isEvaluated = resp.state === 'ANSWERED' || resp.state === 'ANSWERED_AND_MARKED_FOR_REVIEW';
      const isSelected = resp.selectedOptionIndex !== null;

      let isCorrect = false;
      let scoreAwarded = 0;

      if (isEvaluated && isSelected) {
        attempted++;
        if (resp.selectedOptionIndex === q.correctOptionIndex) {
          isCorrect = true;
          correct++;
          scoreAwarded = config.positiveMarks;
        } else {
          incorrect++;
          scoreAwarded = -config.negativeMarks;
        }
      } else {
        unattempted++;
        scoreAwarded = 0;
      }

      if (resp.state === 'MARKED_FOR_REVIEW') {
        markedForReview++;
      }

      totalScore += scoreAwarded;

      // Track domain stats
      const dom = q.domain;
      if (domainStatsMap[dom]) {
        domainStatsMap[dom].totalQuestions++;
        domainStatsMap[dom].maxScore += config.positiveMarks;
        domainStatsMap[dom].score += scoreAwarded;
        if (isEvaluated && isSelected) {
          domainStatsMap[dom].attempted++;
          if (isCorrect) domainStatsMap[dom].correct++;
          else domainStatsMap[dom].incorrect++;
        }
      }

      // Track subject stats
      if (!subjectStatsMap[q.subjectId]) {
        const subInfo = SUBJECT_LIST.find(s => s.id === q.subjectId);
        subjectStatsMap[q.subjectId] = {
          subjectId: q.subjectId,
          subjectName: subInfo ? subInfo.name : q.subjectId,
          domain: q.domain,
          totalQuestions: 0,
          attempted: 0,
          correct: 0,
          incorrect: 0,
          score: 0,
          maxScore: 0,
          accuracy: 0
        };
      }

      const subEntry = subjectStatsMap[q.subjectId];
      subEntry.totalQuestions++;
      subEntry.maxScore += config.positiveMarks;
      subEntry.score += scoreAwarded;
      if (isEvaluated && isSelected) {
        subEntry.attempted++;
        if (isCorrect) subEntry.correct++;
        else subEntry.incorrect++;
      }

      return {
        question: q,
        response: resp,
        isCorrect,
        scoreAwarded
      };
    });

    // Compute accuracies
    const overallAccuracy = attempted > 0 ? Math.round((correct / attempted) * 100) : 0;
    const maxPossible = questions.length * config.positiveMarks;
    const overallPercentage = maxPossible > 0 ? Math.round((Math.max(0, totalScore) / maxPossible) * 100) : 0;

    Object.keys(domainStatsMap).forEach(key => {
      const d = domainStatsMap[key as Domain];
      d.accuracy = d.attempted > 0 ? Math.round((d.correct / d.attempted) * 100) : 0;
    });

    Object.keys(subjectStatsMap).forEach(key => {
      const s = subjectStatsMap[key];
      s.accuracy = s.attempted > 0 ? Math.round((s.correct / s.attempted) * 100) : 0;
    });

    const result: TestResult = {
      id: 'result_' + Date.now(),
      title: config.title || 'ICAR AIEEA PG Mock Test',
      timestamp: Date.now(),
      dateString: new Date().toLocaleDateString('en-IN', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      }),
      config,
      totalQuestions: questions.length,
      attemptedCount: attempted,
      correctCount: correct,
      incorrectCount: incorrect,
      unattemptedCount: unattempted,
      markedForReviewCount: markedForReview,
      totalScore,
      maxPossibleScore: maxPossible,
      percentage: overallPercentage,
      accuracy: overallAccuracy,
      timeSpentSeconds: timeSpentTotal,
      domainPerformance: domainStatsMap,
      subjectPerformance: subjectStatsMap,
      questionRecords
    };

    setShowSubmitModal(false);
    onFinishExam(result);
  };

  if (!activeQuestion) {
    return (
      <div className="p-8 text-center bg-white border rounded">
        <p className="text-slate-600 mb-4">No questions available in this test.</p>
        <button onClick={onAbortExam} className="px-4 py-2 bg-slate-800 text-white rounded">
          Return to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div ref={containerRef} className="fixed inset-0 z-50 bg-[#eef2f6] flex flex-col overflow-hidden">
      {/* 1. Official NTA Exam Top Bar */}
      <CBTHeader
        examTitle={config.title}
        userProfile={userProfile}
        timeRemainingSeconds={timeRemaining}
        currentSection={currentSection}
        onSectionChange={handleSectionTabChange}
        sectionCounts={sectionCounts}
        isFullscreen={isFullscreen}
        onToggleFullscreen={handleToggleFullscreen}
      />

      {/* 2. Main CBT Body (Question Area + Question Palette) */}
      <div className="flex-1 flex flex-col lg:flex-row overflow-hidden p-2 sm:p-3 gap-2 sm:gap-3">
        {/* Left Side: Question Viewport and Bottom Action Bar */}
        <div className="flex-1 flex flex-col overflow-hidden">
          <CBTQuestionArea
            questionNumber={currentQuestionIndex + 1}
            totalQuestions={questions.length}
            question={activeQuestion}
            selectedOptionIndex={selectedOption}
            onSelectOption={handleSelectOption}
            positiveMarks={config.positiveMarks}
            negativeMarks={config.negativeMarks}
          />

          <CBTBottomActions
            onSaveAndNext={handleSaveAndNext}
            onSaveAndMarkForReview={handleSaveAndMarkForReview}
            onClearResponse={handleClearResponse}
            onMarkForReviewAndNext={handleMarkForReviewAndNext}
            onPrevious={() => navigateToQuestion(currentQuestionIndex - 1)}
            onNext={() => navigateToQuestion(currentQuestionIndex + 1)}
            isFirstQuestion={currentQuestionIndex === 0}
            isLastQuestion={currentQuestionIndex === questions.length - 1}
            hasSelectedOption={selectedOption !== null}
          />
        </div>

        {/* Right Side: NTA Question Palette */}
        <div className="w-full lg:w-80 h-72 lg:h-auto shrink-0 flex flex-col">
          <CBTPalette
            questions={questions}
            userResponses={userResponses}
            currentQuestionIndex={currentQuestionIndex}
            onSelectQuestion={navigateToQuestion}
            onSubmitExam={() => setShowSubmitModal(true)}
            userProfile={userProfile}
            currentSection={currentSection}
          />
        </div>
      </div>

      {/* 3. Official NTA Submit Summary Modal */}
      {showSubmitModal && (
        <CBTSubmitModal
          questions={questions}
          userResponses={userResponses}
          onConfirmSubmit={handleFinalSubmit}
          onCancel={() => setShowSubmitModal(false)}
          isTimeExpired={isTimeExpired}
        />
      )}
    </div>
  );
};
