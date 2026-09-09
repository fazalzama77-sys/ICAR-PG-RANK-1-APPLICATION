import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { 
  Zap, 
  Clock, 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  RotateCcw, 
  Home, 
  Award, 
  Sparkles,
  BookOpen,
  Brain
} from 'lucide-react';
import { Question, DrillConfig, TestResult } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { StorageService, UserProfile } from '../../storage/db';

interface InstantDrillRunnerProps {
  config: DrillConfig;
  questions: Question[];
  userProfile: UserProfile;
  onFinishDrill: (result: TestResult) => void;
  onAbortDrill: () => void;
  onOpenSpacedRepetition?: () => void;
}

export const InstantDrillRunner: React.FC<InstantDrillRunnerProps> = ({
  config,
  questions,
  userProfile,
  onFinishDrill,
  onAbortDrill,
  onOpenSpacedRepetition
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState(false);
  
  // Scoring state
  const [correctCount, setCorrectCount] = useState(0);
  const [incorrectCount, setIncorrectCount] = useState(0);
  const [missedQuestionIds, setMissedQuestionIds] = useState<string[]>([]);
  const [isDrillCompleted, setIsDrillCompleted] = useState(false);

  // Time tracking
  const [timeRemainingSeconds, setTimeRemainingSeconds] = useState(
    config.durationMinutes > 0 ? config.durationMinutes * 60 : 0
  );
  const [totalTimeSpentSeconds, setTotalTimeSpentSeconds] = useState(0);

  // Timer effect
  useEffect(() => {
    if (isDrillCompleted) return;

    const timer = setInterval(() => {
      setTotalTimeSpentSeconds(prev => prev + 1);
      if (config.durationMinutes > 0) {
        setTimeRemainingSeconds(prev => {
          if (prev <= 1) {
            clearInterval(timer);
            handleCompleteDrill();
            return 0;
          }
          return prev - 1;
        });
      }
    }, 1000);

    return () => clearInterval(timer);
  }, [isDrillCompleted, config.durationMinutes]);

  const currentQ = questions[currentIndex];

  const handleSubmitAnswer = () => {
    if (selectedOption === null || !currentQ) return;

    const isCorrect = selectedOption === currentQ.correctOptionIndex;
    setIsAnswerSubmitted(true);

    if (isCorrect) {
      setCorrectCount(prev => prev + 1);
    } else {
      setIncorrectCount(prev => prev + 1);
      setMissedQuestionIds(prev => [...prev, currentQ.id]);
    }
  };

  const handleNextQuestion = () => {
    if (currentIndex + 1 < questions.length) {
      setCurrentIndex(prev => prev + 1);
      setSelectedOption(null);
      setIsAnswerSubmitted(false);
    } else {
      handleCompleteDrill();
    }
  };

  const handleCompleteDrill = () => {
    setIsDrillCompleted(true);
    
    // Auto enroll missed questions into SRS
    if (missedQuestionIds.length > 0) {
      StorageService.autoEnrollMissedQuestions(missedQuestionIds);
    }

    // Build TestResult for persistence
    const totalAttempted = correctCount + incorrectCount + (isAnswerSubmitted ? 0 : 0);
    const score = (correctCount * 4) - (incorrectCount * 1);
    const maxScore = questions.length * 4;
    const accuracy = totalAttempted > 0 ? Math.round((correctCount / totalAttempted) * 100) : 0;

    const result: TestResult = {
      id: 'drill_' + Date.now(),
      title: config.title,
      timestamp: Date.now(),
      dateString: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }),
      config: {
        mode: 'custom_practice',
        title: config.title,
        totalQuestions: questions.length,
        durationMinutes: config.durationMinutes,
        selectedDomains: ['veterinary_science', 'animal_science'],
        selectedYears: ['1st_year', '2nd_year'],
        selectedSubjectIds: config.selectedSubjectIds || [],
        positiveMarks: 4,
        negativeMarks: 1,
        shuffleQuestions: true
      },
      totalQuestions: questions.length,
      attemptedCount: totalAttempted,
      correctCount,
      incorrectCount,
      unattemptedCount: questions.length - totalAttempted,
      markedForReviewCount: 0,
      totalScore: score,
      maxPossibleScore: maxScore,
      percentage: Math.round((score / maxScore) * 100),
      accuracy,
      timeSpentSeconds: totalTimeSpentSeconds,
      domainPerformance: {
        veterinary_science: {
          domain: 'veterinary_science',
          totalQuestions: questions.filter(q => q.domain === 'veterinary_science').length,
          attempted: 0,
          correct: 0,
          incorrect: 0,
          score: 0,
          maxScore: 0,
          accuracy: 0
        },
        animal_science: {
          domain: 'animal_science',
          totalQuestions: questions.filter(q => q.domain === 'animal_science').length,
          attempted: 0,
          correct: 0,
          incorrect: 0,
          score: 0,
          maxScore: 0,
          accuracy: 0
        }
      },
      subjectPerformance: {},
      questionRecords: []
    };

    StorageService.saveTestResult(result);

    if (accuracy >= 75) {
      try {
        confetti({ particleCount: 80, spread: 70, origin: { y: 0.6 } });
      } catch {}
    }
  };

  const formatTime = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  // Keyboard shortcut listener
  useEffect(() => {
    const handleKey = (e: KeyboardEvent) => {
      if (isDrillCompleted) return;

      if (!isAnswerSubmitted) {
        if (e.key === '1' || e.key === 'a' || e.key === 'A') setSelectedOption(0);
        if (e.key === '2' || e.key === 'b' || e.key === 'B') setSelectedOption(1);
        if (e.key === '3' || e.key === 'c' || e.key === 'C') setSelectedOption(2);
        if (e.key === '4' || e.key === 'd' || e.key === 'D') setSelectedOption(3);
        if (e.key === 'Enter' && selectedOption !== null) handleSubmitAnswer();
      } else {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          handleNextQuestion();
        }
      }
    };

    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, [isAnswerSubmitted, selectedOption, isDrillCompleted, currentIndex, questions.length]);

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 space-y-6">
      
      {/* Top Header Bar */}
      <div className="flex items-center justify-between bg-white border border-slate-200 rounded-xl p-4 shadow-xs">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 rounded-lg bg-amber-500 text-white flex items-center justify-center font-bold">
            <Zap className="w-5 h-5 fill-current" />
          </div>
          <div>
            <h2 className="font-extrabold text-slate-900 text-sm sm:text-base leading-tight">
              {config.title}
            </h2>
            <span className="text-[11px] text-slate-500 font-medium">
              Instant Feedback Mode &bull; ICAR PG High-Yield Drill
            </span>
          </div>
        </div>

        <div className="flex items-center space-x-4 text-xs font-bold">
          {config.durationMinutes > 0 && (
            <div className="flex items-center space-x-1.5 px-3 py-1 rounded-lg bg-slate-100 text-slate-700 font-mono">
              <Clock className="w-4 h-4 text-slate-500" />
              <span>{formatTime(timeRemainingSeconds)}</span>
            </div>
          )}

          <button
            onClick={onAbortDrill}
            className="text-slate-400 hover:text-red-600 transition-colors"
            title="Exit Drill"
          >
            Exit
          </button>
        </div>
      </div>

      {/* Completion View */}
      {isDrillCompleted ? (
        <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 text-center space-y-6 shadow-sm">
          <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto shadow-inner">
            <Award className="w-8 h-8" />
          </div>

          <div className="space-y-2">
            <h2 className="text-2xl sm:text-3xl font-black text-slate-900">Drill Completed!</h2>
            <p className="text-xs sm:text-sm text-slate-500 max-w-md mx-auto">
              Speed drill evaluated with official ICAR PG marking (+4 for correct, -1 for wrong).
            </p>
          </div>

          {/* Quick Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-xl mx-auto">
            <div className="bg-slate-50 p-3.5 rounded-xl border border-slate-200">
              <span className="text-[10px] uppercase font-bold text-slate-400 block">Total Score</span>
              <span className="text-xl font-black text-slate-900">
                {(correctCount * 4) - (incorrectCount * 1)}
                <span className="text-xs text-slate-400 font-normal"> / {questions.length * 4}</span>
              </span>
            </div>

            <div className="bg-slate-50 p-3.5 rounded-xl border border-emerald-200">
              <span className="text-[10px] uppercase font-bold text-emerald-600 block">Accuracy</span>
              <span className="text-xl font-black text-emerald-700">
                {correctCount + incorrectCount > 0 
                  ? Math.round((correctCount / (correctCount + incorrectCount)) * 100) 
                  : 0}%
              </span>
            </div>

            <div className="bg-slate-50 p-3.5 rounded-xl border border-emerald-200">
              <span className="text-[10px] uppercase font-bold text-emerald-600 block">Correct</span>
              <span className="text-xl font-black text-emerald-600">+{correctCount * 4}</span>
            </div>

            <div className="bg-slate-50 p-3.5 rounded-xl border border-red-200">
              <span className="text-[10px] uppercase font-bold text-red-600 block">Negative Marks</span>
              <span className="text-xl font-black text-red-600">-{incorrectCount * 1}</span>
            </div>
          </div>

          {/* Auto-enrolled in SRS Notice */}
          {missedQuestionIds.length > 0 && (
            <div className="bg-indigo-50 border border-indigo-200 rounded-xl p-4 max-w-xl mx-auto flex items-center justify-between gap-3 text-left">
              <div className="flex items-center space-x-2.5">
                <Brain className="w-5 h-5 text-indigo-600 shrink-0" />
                <div>
                  <p className="text-xs font-bold text-indigo-900">
                    {missedQuestionIds.length} Mistake{missedQuestionIds.length > 1 ? 's' : ''} Enrolled in Spaced Repetition
                  </p>
                  <p className="text-[11px] text-indigo-700">
                    These questions are queued for review in your active recall deck to prevent repeating mistakes.
                  </p>
                </div>
              </div>

              {onOpenSpacedRepetition && (
                <button
                  onClick={onOpenSpacedRepetition}
                  className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-xs font-bold shrink-0 shadow-2xs"
                >
                  Review Now
                </button>
              )}
            </div>
          )}

          {/* Actions */}
          <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
            <button
              onClick={onAbortDrill}
              className="px-5 py-2.5 bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs sm:text-sm rounded-xl shadow-md flex items-center space-x-2"
            >
              <Home className="w-4 h-4" />
              <span>Return to Dashboard</span>
            </button>
          </div>
        </div>
      ) : currentQ ? (
        <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
          
          {/* Progress bar */}
          <div className="bg-slate-100 h-1.5 w-full">
            <div 
              className="bg-amber-500 h-1.5 transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
            />
          </div>

          {/* Question Header */}
          <div className="p-4 sm:p-5 border-b border-slate-100 flex flex-wrap items-center justify-between gap-2 bg-slate-50/50">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-slate-800 text-white text-[11px] font-bold px-2 py-0.5 rounded font-mono">
                Q{currentIndex + 1}
              </span>
              <span className="text-xs font-bold text-slate-700">
                {SUBJECT_LIST.find(s => s.id === currentQ.subjectId)?.name || 'Subject'}
              </span>
              {currentQ.topic && (
                <span className="text-xs text-slate-400 font-medium">
                  &bull; {currentQ.topic}
                </span>
              )}
            </div>

            <div className="flex items-center space-x-3 text-xs font-semibold">
              <span className="text-emerald-700">✓ {correctCount}</span>
              <span className="text-red-600">✗ {incorrectCount}</span>
              <span className="font-mono text-slate-400">
                {currentIndex + 1} / {questions.length}
              </span>
            </div>
          </div>

          {/* Question Content */}
          <div className="p-6 sm:p-8 space-y-6">
            <h3 className="text-base sm:text-lg font-bold text-slate-900 leading-relaxed">
              {currentQ.questionText}
            </h3>

            {/* Options List */}
            <div className="space-y-2.5">
              {currentQ.options.map((opt, idx) => {
                const isSelected = selectedOption === idx;
                const isCorrect = idx === currentQ.correctOptionIndex;

                let style = 'border-slate-200 hover:border-slate-300 hover:bg-slate-50 text-slate-800';

                if (isAnswerSubmitted) {
                  if (isCorrect) {
                    style = 'border-emerald-500 bg-emerald-50 text-emerald-900 font-bold ring-2 ring-emerald-500';
                  } else if (isSelected) {
                    style = 'border-red-500 bg-red-50 text-red-900 font-medium line-through';
                  } else {
                    style = 'border-slate-200 opacity-50 text-slate-400';
                  }
                } else if (isSelected) {
                  style = 'border-amber-500 bg-amber-50 text-amber-900 font-semibold ring-2 ring-amber-500';
                }

                return (
                  <div
                    key={idx}
                    onClick={() => {
                      if (!isAnswerSubmitted) setSelectedOption(idx);
                    }}
                    className={`p-3.5 sm:p-4 rounded-xl border text-xs sm:text-sm flex items-center justify-between cursor-pointer transition-all ${style}`}
                  >
                    <div className="flex items-center space-x-3">
                      <span className="w-6 h-6 rounded-full border border-current flex items-center justify-center font-bold text-xs shrink-0">
                        {String.fromCharCode(65 + idx)}
                      </span>
                      <span>{opt}</span>
                    </div>

                    {isAnswerSubmitted && isCorrect && (
                      <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
                    )}
                    {isAnswerSubmitted && isSelected && !isCorrect && (
                      <XCircle className="w-5 h-5 text-red-500 shrink-0" />
                    )}
                  </div>
                );
              })}
            </div>

            {/* Instant Feedback Explanation Card */}
            {isAnswerSubmitted && (
              <div className={`p-4 sm:p-5 rounded-xl border animate-in fade-in duration-200 space-y-2 ${
                selectedOption === currentQ.correctOptionIndex
                  ? 'bg-emerald-50 border-emerald-200 text-emerald-900'
                  : 'bg-red-50 border-red-200 text-red-950'
              }`}>
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    {selectedOption === currentQ.correctOptionIndex ? (
                      <span className="bg-emerald-600 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                        Correct (+4 Marks)
                      </span>
                    ) : (
                      <span className="bg-red-600 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                        Incorrect (-1 Negative Mark)
                      </span>
                    )}
                  </div>
                  <span className="text-[11px] font-semibold opacity-75">
                    Official Reference Explanation
                  </span>
                </div>

                <p className="text-xs sm:text-sm leading-relaxed font-medium pt-1">
                  {currentQ.explanation}
                </p>
              </div>
            )}
          </div>

          {/* Bottom Actions */}
          <div className="bg-slate-50 border-t border-slate-200 p-4 sm:p-5 flex items-center justify-between">
            <span className="text-[11px] text-slate-400 hidden sm:inline">
              {!isAnswerSubmitted ? 'Press [A/B/C/D] to select, [Enter] to submit' : 'Press [Space] or [Enter] for next'}
            </span>

            <div className="flex items-center space-x-3 ml-auto">
              {!isAnswerSubmitted ? (
                <button
                  onClick={handleSubmitAnswer}
                  disabled={selectedOption === null}
                  className="px-6 py-2.5 bg-amber-500 hover:bg-amber-600 disabled:opacity-40 text-slate-950 font-black text-xs sm:text-sm rounded-xl shadow-md transition-all cursor-pointer"
                >
                  Submit Answer
                </button>
              ) : (
                <button
                  onClick={handleNextQuestion}
                  className="px-6 py-2.5 bg-slate-900 hover:bg-slate-800 text-white font-black text-xs sm:text-sm rounded-xl shadow-md flex items-center space-x-2 transition-all cursor-pointer"
                >
                  <span>{currentIndex + 1 < questions.length ? 'Next Question' : 'Complete Drill'}</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              )}
            </div>
          </div>

        </div>
      ) : null}

    </div>
  );
};
