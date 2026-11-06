import React, { useState, useEffect, useCallback, useMemo } from 'react';
import confetti from 'canvas-confetti';
import { 
  Zap, 
  Clock, 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  Home, 
  Award, 
  Brain,
  Volume2,
  VolumeX,
  Sparkles,
  Flame,
  HelpCircle,
  Star,
  RefreshCw,
  TrendingUp,
  ShieldAlert,
  ChevronRight,
  LogOut
} from 'lucide-react';
import { Question, DrillConfig, TestResult } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { StorageService, UserProfile } from '../../storage/db';
import { soundFx } from '../../utils/soundEffects';

interface InstantDrillRunnerProps {
  config: DrillConfig;
  questions: Question[];
  userProfile?: UserProfile;
  onFinishDrill?: (result: TestResult) => void;
  onAbortDrill: () => void;
  onOpenSpacedRepetition?: () => void;
}

export const InstantDrillRunner: React.FC<InstantDrillRunnerProps> = ({
  config,
  questions,
  userProfile: _userProfile,
  onFinishDrill,
  onAbortDrill,
  onOpenSpacedRepetition
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState(false);
  
  // Game & Scoring state
  const [correctCount, setCorrectCount] = useState(0);
  const [incorrectCount, setIncorrectCount] = useState(0);
  const [currentStreak, setCurrentStreak] = useState(0);
  const [bestStreak, setBestStreak] = useState(0);
  const [missedQuestionIds, setMissedQuestionIds] = useState<string[]>([]);
  const [isDrillCompleted, setIsDrillCompleted] = useState(false);

  // Lifelines: 50:50
  const [eliminatedOptions, setEliminatedOptions] = useState<number[]>([]);
  const [hasUsedFiftyFiftyOnCurrent, setHasUsedFiftyFiftyOnCurrent] = useState(false);
  const [fiftyFiftyRemaining, setFiftyFiftyRemaining] = useState(Math.max(1, Math.min(3, Math.ceil(questions.length / 10))));

  // Floating score feedback animation (+4 / -1)
  const [scoreBadge, setScoreBadge] = useState<{ text: string; isPositive: boolean; key: number } | null>(null);

  // Bookmarking / SRS save
  const [isCurrentBookmarked, setIsCurrentBookmarked] = useState(false);

  // Sound toggle
  const [soundEnabled, setSoundEnabled] = useState(soundFx.isEnabled());

  // Time tracking
  const [timeRemainingSeconds, setTimeRemainingSeconds] = useState(
    config.durationMinutes > 0 ? config.durationMinutes * 60 : 0
  );
  const [totalTimeSpentSeconds, setTotalTimeSpentSeconds] = useState(0);

  const currentQ = questions[currentIndex];

  // Check if current question is already in SRS
  useEffect(() => {
    if (!currentQ) return;
    const records = StorageService.getSRSRecords();
    setIsCurrentBookmarked(!!records[currentQ.id]);
    setEliminatedOptions([]);
    setHasUsedFiftyFiftyOnCurrent(false);
  }, [currentIndex, currentQ]);

  const handleToggleSound = () => {
    const newState = soundFx.toggle();
    setSoundEnabled(newState);
  };

  const handleCompleteDrill = useCallback(() => {
    setIsDrillCompleted(true);
    soundFx.playVictory();
    
    // Auto enroll missed questions into SRS
    if (missedQuestionIds.length > 0) {
      StorageService.autoEnrollMissedQuestions(missedQuestionIds);
    }

    // Record questions solved into daily progress
    const totalAttempted = correctCount + incorrectCount + (isAnswerSubmitted ? 1 : 0);
    StorageService.recordQuestionsAttempted(totalAttempted);

    // Build TestResult for persistence
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
    if (onFinishDrill) {
      onFinishDrill(result);
    }

    try {
      confetti({
        particleCount: 120,
        spread: 90,
        origin: { y: 0.55 },
        colors: ['#10b981', '#f59e0b', '#6366f1', '#ec4899', '#06b6d4']
      });
    } catch {}
  }, [
    config, 
    correctCount, 
    incorrectCount, 
    isAnswerSubmitted, 
    missedQuestionIds, 
    onFinishDrill, 
    questions, 
    totalTimeSpentSeconds
  ]);

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
  }, [isDrillCompleted, config.durationMinutes, handleCompleteDrill]);

  // Handle 50:50 Lifeline
  const handleUseFiftyFifty = () => {
    if (!currentQ || hasUsedFiftyFiftyOnCurrent || fiftyFiftyRemaining <= 0 || isAnswerSubmitted) return;

    soundFx.playLifeline();
    const wrongIndices = [0, 1, 2, 3].filter(idx => idx !== currentQ.correctOptionIndex);
    // Shuffle and pick 2
    const shuffledWrong = [...wrongIndices].sort(() => Math.random() - 0.5).slice(0, 2);
    setEliminatedOptions(shuffledWrong);
    setHasUsedFiftyFiftyOnCurrent(true);
    setFiftyFiftyRemaining(prev => Math.max(0, prev - 1));

    // If user currently selected one of the eliminated, deselect it
    if (selectedOption !== null && shuffledWrong.includes(selectedOption)) {
      setSelectedOption(null);
    }
  };

  // Toggle bookmark in SRS
  const handleToggleBookmark = () => {
    if (!currentQ) return;
    soundFx.playPop();
    const records = StorageService.getSRSRecords();
    if (records[currentQ.id]) {
      // Remove or mark unreviewed
      delete records[currentQ.id];
      try {
        localStorage.setItem('icar_pg_srs_records_v1', JSON.stringify(records));
      } catch {}
      setIsCurrentBookmarked(false);
    } else {
      // Enroll
      StorageService.autoEnrollMissedQuestions([currentQ.id]);
      setIsCurrentBookmarked(true);
    }
  };

  const handleSelectOption = (idx: number) => {
    if (isAnswerSubmitted) return;
    if (eliminatedOptions.includes(idx)) return;
    soundFx.playPop();
    setSelectedOption(idx);
  };

  const handleSubmitAnswer = useCallback(() => {
    if (selectedOption === null || !currentQ || isAnswerSubmitted) return;

    const isCorrect = selectedOption === currentQ.correctOptionIndex;
    setIsAnswerSubmitted(true);

    if (isCorrect) {
      soundFx.playCorrect();
      setCorrectCount(prev => prev + 1);
      const newStreak = currentStreak + 1;
      setCurrentStreak(newStreak);
      setBestStreak(prev => Math.max(prev, newStreak));

      // Trigger streak audio / confetti on 3+ streaks
      if (newStreak >= 3) {
        soundFx.playStreak();
        try {
          confetti({
            particleCount: 40,
            spread: 60,
            origin: { y: 0.65 },
            colors: ['#f59e0b', '#10b981', '#3b82f6']
          });
        } catch {}
      }

      setScoreBadge({ text: '+4 Marks!', isPositive: true, key: Date.now() });
    } else {
      soundFx.playIncorrect();
      setIncorrectCount(prev => prev + 1);
      setCurrentStreak(0);
      setMissedQuestionIds(prev => [...prev, currentQ.id]);
      setScoreBadge({ text: '-1 Penalty', isPositive: false, key: Date.now() });
    }
  }, [currentQ, currentStreak, isAnswerSubmitted, selectedOption]);

  const handleNextQuestion = useCallback(() => {
    if (currentIndex + 1 < questions.length) {
      soundFx.playPop();
      setCurrentIndex(prev => prev + 1);
      setSelectedOption(null);
      setIsAnswerSubmitted(false);
      setScoreBadge(null);
    } else {
      handleCompleteDrill();
    }
  }, [currentIndex, handleCompleteDrill, questions.length]);

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
        if ((e.key === '1' || e.key === 'a' || e.key === 'A') && !eliminatedOptions.includes(0)) handleSelectOption(0);
        if ((e.key === '2' || e.key === 'b' || e.key === 'B') && !eliminatedOptions.includes(1)) handleSelectOption(1);
        if ((e.key === '3' || e.key === 'c' || e.key === 'C') && !eliminatedOptions.includes(2)) handleSelectOption(2);
        if ((e.key === '4' || e.key === 'd' || e.key === 'D') && !eliminatedOptions.includes(3)) handleSelectOption(3);
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
  }, [isAnswerSubmitted, selectedOption, isDrillCompleted, eliminatedOptions, handleSubmitAnswer, handleNextQuestion]);

  const currentScore = (correctCount * 4) - (incorrectCount * 1);
  const progressPercent = Math.round(((currentIndex + (isAnswerSubmitted ? 1 : 0)) / questions.length) * 100);

  // Subject info
  const subjectMeta = useMemo(() => {
    if (!currentQ) return null;
    return SUBJECT_LIST.find(s => s.id === currentQ.subjectId);
  }, [currentQ]);

  // Option styling palettes (A: Blue, B: Violet, C: Amber, D: Teal)
  const optionThemes = [
    { bg: 'bg-blue-500', text: 'text-blue-700', border: 'border-blue-200', lightBg: 'bg-blue-50/60' },
    { bg: 'bg-purple-500', text: 'text-purple-700', border: 'border-purple-200', lightBg: 'bg-purple-50/60' },
    { bg: 'bg-amber-500', text: 'text-amber-700', border: 'border-amber-200', lightBg: 'bg-amber-50/60' },
    { bg: 'bg-emerald-500', text: 'text-emerald-700', border: 'border-emerald-200', lightBg: 'bg-emerald-50/60' }
  ];

  return (
    <div className="w-full max-w-4xl mx-auto px-2.5 sm:px-6 pt-safe pb-safe min-h-screen flex flex-col justify-between space-y-3 sm:space-y-4">
      
      {/* 1. PLAYFUL GAMIFIED TOP HUD */}
      <div className="bg-white/95 backdrop-blur-md border border-slate-200/90 rounded-2xl p-3 sm:p-4 shadow-sm shrink-0 space-y-3">
        <div className="flex items-center justify-between gap-2">
          
          {/* Mode Title & Mascot Badge */}
          <div className="flex items-center space-x-2.5 min-w-0">
            <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-tr from-amber-500 via-orange-500 to-amber-400 text-white flex items-center justify-center font-black shadow-sm shrink-0 animate-pop-in">
              <Zap className="w-5 h-5 fill-current" />
            </div>
            <div className="min-w-0">
              <div className="flex items-center space-x-1.5">
                <h2 className="font-extrabold text-slate-900 text-xs sm:text-base leading-tight truncate">
                  {config.title}
                </h2>
                <span className="hidden xs:inline-block bg-amber-100 text-amber-900 text-[10px] font-extrabold px-1.5 py-0.5 rounded-full border border-amber-300">
                  QUIZ
                </span>
              </div>
              <p className="text-[10px] sm:text-[11px] text-slate-500 font-medium truncate">
                Interactive Learning Arcade &bull; +4 / -1 ICAR PG
              </p>
            </div>
          </div>

          {/* Quick HUD Counters: Streak, Score, Sound, Exit */}
          <div className="flex items-center space-x-1.5 sm:space-x-2.5 shrink-0">
            
            {/* Streak Counter Pill */}
            {currentStreak > 0 && (
              <div className="flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-full bg-gradient-to-r from-orange-500 to-amber-500 text-white font-extrabold text-[11px] sm:text-xs shadow-xs animate-pop-in">
                <Flame className="w-3.5 h-3.5 fill-current animate-bounce" />
                <span>{currentStreak} Streak!</span>
              </div>
            )}

            {/* Live Score Pill */}
            <div className="relative flex items-center space-x-1 px-2.5 py-1 rounded-xl bg-slate-900 text-white font-black text-xs sm:text-sm shadow-xs font-mono">
              <span className="text-[10px] text-amber-300 font-bold hidden sm:inline">PTS:</span>
              <span className={currentScore >= 0 ? 'text-emerald-400' : 'text-rose-400'}>
                {currentScore > 0 ? `+${currentScore}` : currentScore}
              </span>

              {/* Floating score animation badge */}
              {scoreBadge && (
                <div 
                  key={scoreBadge.key}
                  className={`absolute -bottom-6 left-1/2 -translate-x-1/2 whitespace-nowrap text-[11px] font-black px-2 py-0.5 rounded-full shadow-md animate-pop-in ${
                    scoreBadge.isPositive ? 'bg-emerald-500 text-white' : 'bg-rose-500 text-white'
                  }`}
                >
                  {scoreBadge.text}
                </div>
              )}
            </div>

            {/* Countdown Timer */}
            {config.durationMinutes > 0 && (
              <div className={`flex items-center space-x-1 px-2 sm:px-2.5 py-1 rounded-xl font-mono text-[11px] sm:text-xs font-bold border transition-colors ${
                timeRemainingSeconds < 60 
                  ? 'bg-rose-50 text-rose-700 border-rose-300 animate-pulse' 
                  : 'bg-slate-100 text-slate-700 border-slate-200'
              }`}>
                <Clock className="w-3.5 h-3.5" />
                <span>{formatTime(timeRemainingSeconds)}</span>
              </div>
            )}

            {/* Audio Toggle */}
            <button
              onClick={handleToggleSound}
              className={`p-1.5 rounded-xl border transition-colors cursor-pointer touch-manipulation ${
                soundEnabled 
                  ? 'bg-amber-50 border-amber-200 text-amber-700 hover:bg-amber-100' 
                  : 'bg-slate-100 border-slate-200 text-slate-400 hover:bg-slate-200'
              }`}
              title={soundEnabled ? 'Mute sound effects' : 'Unmute sound effects'}
            >
              {soundEnabled ? <Volume2 className="w-4 h-4" /> : <VolumeX className="w-4 h-4" />}
            </button>

            {/* Exit Drill */}
            <button
              onClick={() => {
                if (window.confirm('Do you want to leave this quiz? Your current score will be saved.')) {
                  onAbortDrill();
                }
              }}
              className="p-1.5 rounded-xl bg-slate-100 hover:bg-rose-50 text-slate-500 hover:text-rose-600 border border-slate-200 transition-colors cursor-pointer"
              title="Exit Quiz"
            >
              <LogOut className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Playful Animated Progress Bar with Rocket 🚀 */}
        <div className="space-y-1">
          <div className="flex items-center justify-between text-[11px] font-bold text-slate-500 px-0.5">
            <span className="flex items-center space-x-1 text-slate-700">
              <span className="font-mono text-xs text-indigo-600 font-extrabold">Q{currentIndex + 1}</span>
              <span>of {questions.length} Questions</span>
            </span>
            <span className="font-mono text-emerald-700 font-extrabold">{progressPercent}% Conquered</span>
          </div>
          
          <div className="bg-slate-100 h-3 rounded-full w-full relative overflow-visible p-0.5 border border-slate-200/80">
            <div 
              className="bg-gradient-to-r from-indigo-500 via-amber-500 to-emerald-500 h-full rounded-full transition-all duration-300 relative"
              style={{ width: `${Math.max(3, progressPercent)}%` }}
            >
              <div className="absolute inset-0 shimmer-bar rounded-full" />
              {/* Cute Rocket Thumb at head of progress */}
              <span className="absolute -right-2.5 -top-1.5 text-xs select-none filter drop-shadow animate-bounce">
                🚀
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* 2. COMPLETION CEREMONY SCREEN */}
      {isDrillCompleted ? (
        <div className="bg-white border-2 border-emerald-300 rounded-3xl p-5 sm:p-8 text-center space-y-6 shadow-xl my-auto animate-pop-in">
          
          {/* Trophy Header */}
          <div className="space-y-3">
            <div className="w-20 h-20 sm:w-24 sm:h-24 bg-gradient-to-tr from-amber-400 via-yellow-400 to-amber-300 text-amber-950 rounded-full flex items-center justify-center mx-auto shadow-lg animate-pulse-glow">
              <Award className="w-10 h-10 sm:w-12 sm:h-12" />
            </div>

            <div>
              <span className="bg-emerald-100 text-emerald-900 text-xs font-black px-3 py-1 rounded-full uppercase tracking-wider border border-emerald-300">
                Quiz Conquered! 🎉
              </span>
              <h2 className="text-2xl sm:text-4xl font-black text-slate-900 mt-2 tracking-tight">
                Outstanding Effort!
              </h2>
              <p className="text-xs sm:text-sm text-slate-600 max-w-md mx-auto mt-1">
                Evaluated with official ICAR PG scoring (+4 correct, -1 incorrect).
              </p>
            </div>
          </div>

          {/* 4 Big Colorful Stat Cards */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-2xl mx-auto">
            
            {/* Final Score */}
            <div className="bg-gradient-to-br from-indigo-50 to-indigo-100/50 p-4 rounded-2xl border-2 border-indigo-200 shadow-xs">
              <span className="text-[10px] uppercase font-black text-indigo-700 block">Total Marks</span>
              <span className="text-2xl font-black text-indigo-950 block mt-0.5 font-mono">
                {currentScore}
              </span>
              <span className="text-[10px] text-indigo-600 font-bold block">
                out of {questions.length * 4}
              </span>
            </div>

            {/* Accuracy */}
            <div className="bg-gradient-to-br from-emerald-50 to-emerald-100/50 p-4 rounded-2xl border-2 border-emerald-300 shadow-xs">
              <span className="text-[10px] uppercase font-black text-emerald-700 block">Accuracy</span>
              <span className="text-2xl font-black text-emerald-950 block mt-0.5 font-mono">
                {correctCount + incorrectCount > 0 
                  ? Math.round((correctCount / (correctCount + incorrectCount)) * 100) 
                  : 0}%
              </span>
              <span className="text-[10px] text-emerald-700 font-bold block">
                {correctCount} Right &bull; {incorrectCount} Wrong
              </span>
            </div>

            {/* Longest Streak */}
            <div className="bg-gradient-to-br from-amber-50 to-amber-100/50 p-4 rounded-2xl border-2 border-amber-300 shadow-xs">
              <span className="text-[10px] uppercase font-black text-amber-700 block">Best Streak</span>
              <span className="text-2xl font-black text-amber-950 block mt-0.5 font-mono">
                🔥 {bestStreak}
              </span>
              <span className="text-[10px] text-amber-700 font-bold block">
                in a row!
              </span>
            </div>

            {/* Avg Speed */}
            <div className="bg-gradient-to-br from-cyan-50 to-cyan-100/50 p-4 rounded-2xl border-2 border-cyan-200 shadow-xs">
              <span className="text-[10px] uppercase font-black text-cyan-700 block">Avg Speed</span>
              <span className="text-2xl font-black text-cyan-950 block mt-0.5 font-mono">
                {Math.round(totalTimeSpentSeconds / Math.max(1, questions.length))}s
              </span>
              <span className="text-[10px] text-cyan-700 font-bold block">
                per question
              </span>
            </div>

          </div>

          {/* Auto-enrolled in SRS Notice */}
          {missedQuestionIds.length > 0 && (
            <div className="bg-indigo-50 border-2 border-indigo-200 rounded-2xl p-4 max-w-xl mx-auto flex items-center justify-between gap-3 text-left shadow-xs">
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-bold shrink-0 shadow-sm">
                  <Brain className="w-5 h-5" />
                </div>
                <div>
                  <p className="text-xs sm:text-sm font-black text-indigo-950">
                    {missedQuestionIds.length} Mistake{missedQuestionIds.length > 1 ? 's' : ''} Saved to Flashcards!
                  </p>
                  <p className="text-[11px] text-indigo-700 leading-tight">
                    Queued in Spaced Repetition so you master them and never lose marks again.
                  </p>
                </div>
              </div>

              {onOpenSpacedRepetition && (
                <button
                  onClick={onOpenSpacedRepetition}
                  className="px-3.5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-black shrink-0 shadow-sm transition-transform active:scale-95 cursor-pointer"
                >
                  Review
                </button>
              )}
            </div>
          )}

          {/* Action Buttons */}
          <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
            <button
              onClick={onAbortDrill}
              className="px-6 py-3 bg-slate-900 hover:bg-slate-800 text-white font-black text-xs sm:text-sm rounded-xl shadow-md flex items-center space-x-2 transition-transform active:scale-95 cursor-pointer"
            >
              <Home className="w-4 h-4" />
              <span>Back to Dashboard</span>
            </button>
          </div>
        </div>
      ) : currentQ ? (
        
        /* 3. ACTIVE PLAYFUL QUESTION VIEWPORT */
        <div className="bg-white border-2 border-slate-200/90 rounded-3xl shadow-sm flex flex-col flex-1 overflow-hidden transition-all">
          
          {/* Question Meta Bar (Subject, Topic, Lifeline & Star) */}
          <div className="p-3 sm:p-4 border-b border-slate-100 flex items-center justify-between gap-2 bg-slate-50/80 shrink-0">
            
            {/* Subject & Chapter Badges */}
            <div className="flex flex-wrap items-center gap-1.5 sm:gap-2 min-w-0">
              <span className="bg-gradient-to-r from-slate-900 to-slate-800 text-white text-[11px] font-black px-2.5 py-1 rounded-lg font-mono shadow-2xs">
                Q{currentIndex + 1}
              </span>
              
              <span className="bg-indigo-50 border border-indigo-200 text-indigo-800 text-xs font-black px-2.5 py-0.5 rounded-full truncate">
                {subjectMeta?.name || 'Veterinary Science'}
              </span>

              {currentQ.topic && (
                <span className="hidden sm:inline-block bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px] font-bold px-2 py-0.5 rounded-full truncate max-w-xs">
                  {currentQ.topic}
                </span>
              )}

              {currentQ.isPYQ && (
                <span className="bg-amber-100 text-amber-900 border border-amber-300 text-[10px] font-black px-2 py-0.5 rounded-full uppercase">
                  ⭐ ICAR PYQ
                </span>
              )}
            </div>

            {/* Lifeline: 50:50 and Flashcard Star Bookmark */}
            <div className="flex items-center space-x-2 shrink-0">
              
              {/* 50:50 Lifeline Button */}
              {!isAnswerSubmitted && fiftyFiftyRemaining > 0 && !hasUsedFiftyFiftyOnCurrent && (
                <button
                  type="button"
                  onClick={handleUseFiftyFifty}
                  className="px-2.5 py-1 rounded-xl bg-amber-400 hover:bg-amber-500 text-slate-950 font-black text-xs flex items-center space-x-1 shadow-2xs transition-transform active:scale-95 cursor-pointer touch-manipulation"
                  title="Eliminate 2 wrong answers!"
                >
                  <Sparkles className="w-3.5 h-3.5 fill-current" />
                  <span>50:50 ({fiftyFiftyRemaining})</span>
                </button>
              )}

              {/* Bookmark to Flashcards Button */}
              <button
                type="button"
                onClick={handleToggleBookmark}
                className={`p-1.5 rounded-xl border transition-all cursor-pointer touch-manipulation active:scale-95 ${
                  isCurrentBookmarked 
                    ? 'bg-amber-100 border-amber-300 text-amber-700 shadow-2xs' 
                    : 'bg-white border-slate-200 text-slate-400 hover:text-amber-500 hover:bg-amber-50'
                }`}
                title={isCurrentBookmarked ? 'Saved in Spaced Repetition!' : 'Save to Spaced Repetition Flashcards'}
              >
                <Star className={`w-4 h-4 ${isCurrentBookmarked ? 'fill-current' : ''}`} />
              </button>
            </div>
          </div>

          {/* Question Body & Colorful Options */}
          <div key={currentQ.id} className="p-4 sm:p-7 space-y-5 flex-1 overflow-y-auto animate-fade-in-up">
            
            {/* Question Stem */}
            <div className="space-y-1">
              <span className="text-[10px] font-black uppercase tracking-wider text-slate-400 block">
                Official MCQ Stem
              </span>
              <h3 className="text-base sm:text-xl font-bold text-slate-900 leading-relaxed select-text">
                {currentQ.questionText}
              </h3>
            </div>

            {/* 4 Tactile Colorful Options */}
            <div className="space-y-3">
              {currentQ.options.map((opt, idx) => {
                const isSelected = selectedOption === idx;
                const isCorrect = idx === currentQ.correctOptionIndex;
                const isEliminated = eliminatedOptions.includes(idx);
                const theme = optionThemes[idx % 4];

                let cardStyle = 'border-slate-200 hover:border-slate-300 bg-white hover:bg-slate-50/80 text-slate-800 shadow-2xs';

                if (isEliminated) {
                  cardStyle = 'border-dashed border-slate-200 bg-slate-50 text-slate-300 opacity-40 cursor-not-allowed line-through';
                } else if (isAnswerSubmitted) {
                  if (isCorrect) {
                    cardStyle = 'border-2 border-emerald-500 bg-emerald-50 text-emerald-950 font-bold ring-4 ring-emerald-500/20 shadow-md animate-pop-in';
                  } else if (isSelected) {
                    cardStyle = 'border-2 border-rose-500 bg-rose-50 text-rose-950 font-medium ring-2 ring-rose-400/20 line-through';
                  } else {
                    cardStyle = 'border-slate-200 opacity-40 text-slate-400 bg-slate-50';
                  }
                } else if (isSelected) {
                  cardStyle = 'border-2 border-indigo-600 bg-indigo-50/70 text-indigo-950 font-bold ring-4 ring-indigo-500/20 shadow-sm scale-[1.01]';
                }

                return (
                  <div
                    key={idx}
                    onClick={() => handleSelectOption(idx)}
                    className={`option-card-interactive p-4 sm:p-4.5 rounded-2xl border-2 text-xs sm:text-base flex items-center justify-between cursor-pointer min-h-[58px] select-none transition-all ${cardStyle}`}
                  >
                    <div className="flex items-center space-x-3.5 flex-1 min-w-0 pr-2">
                      
                      {/* Playful Colorful Letter Badge */}
                      <span className={`w-7 h-7 sm:w-8 sm:h-8 rounded-xl flex items-center justify-center font-black text-xs sm:text-sm shrink-0 transition-transform ${
                        isAnswerSubmitted && isCorrect
                          ? 'bg-emerald-600 text-white shadow-xs'
                          : isAnswerSubmitted && isSelected && !isCorrect
                          ? 'bg-rose-500 text-white'
                          : isSelected
                          ? 'bg-indigo-600 text-white shadow-xs'
                          : `${theme.bg} text-white shadow-2xs`
                      }`}>
                        {String.fromCharCode(65 + idx)}
                      </span>

                      <span className="leading-snug font-medium select-text">{opt}</span>
                    </div>

                    {/* Result Icons */}
                    {isEliminated && (
                      <span className="text-[10px] font-bold text-slate-400 bg-slate-200/60 px-2 py-0.5 rounded-full shrink-0">
                        Eliminated
                      </span>
                    )}
                    {isAnswerSubmitted && isCorrect && (
                      <div className="flex items-center space-x-1 text-emerald-600 font-black text-xs bg-emerald-100/80 px-2 py-1 rounded-lg shrink-0 animate-scale-in">
                        <CheckCircle2 className="w-5 h-5 fill-emerald-100" />
                        <span className="hidden sm:inline">CORRECT</span>
                      </div>
                    )}
                    {isAnswerSubmitted && isSelected && !isCorrect && (
                      <div className="flex items-center space-x-1 text-rose-600 font-black text-xs bg-rose-100/80 px-2 py-1 rounded-lg shrink-0 animate-scale-in">
                        <XCircle className="w-5 h-5 fill-rose-100" />
                        <span className="hidden sm:inline">WRONG (-1)</span>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            {/* 4. INSTANT CELEBRATION / LEARNING FEEDBACK CARD */}
            {isAnswerSubmitted && (
              <div className={`p-4 sm:p-5 rounded-2xl border-2 animate-scale-in space-y-2.5 shadow-sm ${
                selectedOption === currentQ.correctOptionIndex
                  ? 'bg-gradient-to-r from-emerald-50 via-teal-50/50 to-emerald-50 border-emerald-300 text-emerald-950'
                  : 'bg-gradient-to-r from-rose-50 via-red-50/50 to-rose-50 border-rose-300 text-rose-950'
              }`}>
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    {selectedOption === currentQ.correctOptionIndex ? (
                      <span className="bg-emerald-600 text-white text-[11px] font-black px-2.5 py-1 rounded-lg uppercase shadow-2xs flex items-center space-x-1">
                        <span>🎉 Nailed It! (+4 Marks)</span>
                      </span>
                    ) : (
                      <span className="bg-rose-600 text-white text-[11px] font-black px-2.5 py-1 rounded-lg uppercase shadow-2xs flex items-center space-x-1">
                        <span>💡 Concept Note (-1 Mark)</span>
                      </span>
                    )}
                    
                    {currentStreak >= 3 && selectedOption === currentQ.correctOptionIndex && (
                      <span className="bg-amber-400 text-slate-950 text-[10px] font-black px-2 py-0.5 rounded-full flex items-center space-x-1 animate-bounce">
                        <Flame className="w-3 h-3 fill-current" />
                        <span>Streak x{currentStreak}!</span>
                      </span>
                    )}
                  </div>

                  <span className="text-[11px] font-extrabold opacity-75">
                    Official Reference
                  </span>
                </div>

                <p className="text-xs sm:text-sm leading-relaxed font-medium pt-1 select-text">
                  {currentQ.explanation}
                </p>
              </div>
            )}
          </div>

          {/* 5. THUMB-FRIENDLY BIG CONSOLIDATED ACTION BAR */}
          <div className="sticky bottom-0 z-30 bg-white/95 backdrop-blur-md border-t border-slate-200 p-3 sm:p-4 pb-[max(0.75rem,env(safe-area-inset-bottom,0px))] shadow-[0_-4px_16px_rgba(0,0,0,0.06)] flex items-center justify-between gap-3">
            
            <div className="hidden sm:flex items-center space-x-2 text-xs text-slate-500 font-medium">
              {!isAnswerSubmitted ? (
                <span>Press <kbd className="px-1.5 py-0.5 bg-slate-100 border rounded font-mono font-bold text-slate-700">A-D</kbd> then <kbd className="px-1.5 py-0.5 bg-slate-100 border rounded font-mono font-bold text-slate-700">Enter</kbd></span>
              ) : (
                <span>Press <kbd className="px-1.5 py-0.5 bg-slate-100 border rounded font-mono font-bold text-slate-700">Space</kbd> or <kbd className="px-1.5 py-0.5 bg-slate-100 border rounded font-mono font-bold text-slate-700">Enter</kbd> to continue</span>
              )}
            </div>

            <div className="flex items-center justify-between sm:justify-end w-full sm:w-auto gap-3">
              <span className="text-xs font-mono font-bold text-slate-500 sm:hidden">
                Q{currentIndex + 1} / {questions.length}
              </span>

              {!isAnswerSubmitted ? (
                <button
                  onClick={handleSubmitAnswer}
                  disabled={selectedOption === null}
                  className="flex-1 sm:flex-initial px-8 py-3.5 bg-gradient-to-r from-amber-400 via-orange-400 to-amber-500 hover:from-amber-500 hover:to-orange-500 disabled:opacity-40 text-slate-950 font-black text-sm sm:text-base rounded-2xl shadow-md transition-all active:scale-95 cursor-pointer touch-manipulation disabled:pointer-events-none flex items-center justify-center space-x-2"
                >
                  <span>{selectedOption === null ? 'Select an Option Above 👆' : 'Check Answer ⚡'}</span>
                </button>
              ) : (
                <button
                  onClick={handleNextQuestion}
                  className="flex-1 sm:flex-initial px-8 py-3.5 bg-slate-900 hover:bg-slate-800 text-white font-black text-sm sm:text-base rounded-2xl shadow-lg flex items-center justify-center space-x-2 transition-all active:scale-95 cursor-pointer touch-manipulation"
                >
                  <span>{currentIndex + 1 < questions.length ? 'Next Question' : 'View Final Score 🏆'}</span>
                  <ArrowRight className="w-5 h-5" />
                </button>
              )}
            </div>

          </div>

        </div>
      ) : null}

    </div>
  );
};
