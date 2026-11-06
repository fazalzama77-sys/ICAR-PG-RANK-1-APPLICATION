import React, { useState } from 'react';
import { 
  Target, 
  BookOpen, 
  ChevronRight, 
  ChevronDown,
  ChevronUp,
  Play, 
  Layers, 
  ShieldCheck, 
  TrendingUp,
  Brain,
  Zap,
  Flame,
  AlertTriangle,
  Award,
  Sparkles,
  ArrowRight,
  CheckCircle2,
  Clock,
  Compass
} from 'lucide-react';
import { Question, TestResult, DrillPreset } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { UserProfile, StorageService } from '../../storage/db';
import { soundFx } from '../../utils/soundEffects';

interface DashboardProps {
  questions: Question[];
  testResults: TestResult[];
  userProfile: UserProfile;
  onLaunchCBT: () => void;
  onLaunchSubjectPractice: (subjectId: string) => void;
  onLaunchTopicDrill?: (subjectId: string, topic: string, mode: 'instant' | 'cbt') => void;
  onLaunchSubjectSRS?: (subjectId: string) => void;
  onLaunchPresetDrill: (preset: DrillPreset) => void;
  onOpenSpacedRepetition: () => void;
  onOpenDrillLauncher: () => void;
  onViewResult: (result: TestResult) => void;
  onNavigateToBank: () => void;
  onOpenSettings?: (tab?: 'profile' | 'cache' | 'data') => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  questions,
  testResults,
  userProfile,
  onLaunchCBT,
  onLaunchSubjectPractice,
  onLaunchTopicDrill,
  onLaunchSubjectSRS,
  onLaunchPresetDrill,
  onOpenSpacedRepetition,
  onOpenDrillLauncher,
  onViewResult,
  onNavigateToBank: _onNavigateToBank,
  onOpenSettings: _onOpenSettings
}) => {
  const [subjectFilter, setSubjectFilter] = useState<'all' | '1st_year' | '2nd_year' | 'veterinary_science' | 'animal_science'>('all');
  
  // Keep chapters collapsed by default for an ultra-clean, scannable overview
  const [expandedSubjects, setExpandedSubjects] = useState<Record<string, boolean>>({});

  const toggleExpandSubject = (subjectId: string) => {
    soundFx.playPop();
    setExpandedSubjects(prev => ({ ...prev, [subjectId]: !prev[subjectId] }));
  };

  // Daily Progress & Streak
  const dailyProgress = StorageService.getDailyProgress();
  const srsMetrics = StorageService.getSRSMetrics(questions);

  // Aggregate stats
  const totalTests = testResults.length;
  const avgAccuracy = totalTests > 0
    ? Math.round(testResults.reduce((acc, r) => acc + r.accuracy, 0) / totalTests)
    : 0;

  // Total questions attempted across tests
  const totalAttempted = testResults.reduce((acc, r) => acc + r.attemptedCount, 0);

  // Subject-wise accuracy calculation
  const subjectStats: Record<string, { total: number; correct: number; accuracy: number }> = {};
  SUBJECT_LIST.forEach(s => {
    subjectStats[s.id] = { total: 0, correct: 0, accuracy: -1 };
  });

  testResults.forEach(r => {
    Object.values(r.subjectPerformance).forEach(sp => {
      if (subjectStats[sp.subjectId]) {
        subjectStats[sp.subjectId].total += sp.attempted;
        subjectStats[sp.subjectId].correct += sp.correct;
      }
    });
  });

  Object.keys(subjectStats).forEach(sId => {
    const s = subjectStats[sId];
    if (s.total > 0) {
      s.accuracy = Math.round((s.correct / s.total) * 100);
    }
  });

  // Filtered subjects
  const displayedSubjects = SUBJECT_LIST.filter(s => {
    if (subjectFilter === '1st_year') return s.year === '1st_year';
    if (subjectFilter === '2nd_year') return s.year === '2nd_year';
    if (subjectFilter === 'veterinary_science') return s.domain === 'veterinary_science';
    if (subjectFilter === 'animal_science') return s.domain === 'animal_science';
    return true;
  });

  // Subject color mappings and playful icons
  const subjectStyles: Record<string, { gradient: string; text: string; bg: string; icon: string; border: string }> = {
    vpp: { gradient: 'from-rose-500 to-red-600', text: 'text-rose-600', bg: 'bg-rose-50', icon: '🔬', border: 'border-rose-200 hover:border-rose-300' },
    vmc: { gradient: 'from-emerald-500 to-teal-600', text: 'text-emerald-600', bg: 'bg-emerald-50', icon: '🧫', border: 'border-emerald-200 hover:border-emerald-300' },
    van: { gradient: 'from-indigo-500 to-blue-600', text: 'text-indigo-600', bg: 'bg-indigo-50', icon: '🦴', border: 'border-indigo-200 hover:border-indigo-300' },
    vpa: { gradient: 'from-amber-500 to-orange-600', text: 'text-amber-600', bg: 'bg-amber-50', icon: '🐛', border: 'border-amber-200 hover:border-amber-300' },
    agb: { gradient: 'from-cyan-500 to-blue-600', text: 'text-cyan-600', bg: 'bg-cyan-50', icon: '🧬', border: 'border-cyan-200 hover:border-cyan-300' },
    ann: { gradient: 'from-orange-500 to-amber-600', text: 'text-orange-600', bg: 'bg-orange-50', icon: '🌾', border: 'border-orange-200 hover:border-orange-300' },
    vpy: { gradient: 'from-sky-500 to-indigo-600', text: 'text-sky-600', bg: 'bg-sky-50', icon: '💓', border: 'border-sky-200 hover:border-sky-300' },
    vbc: { gradient: 'from-purple-500 to-fuchsia-600', text: 'text-purple-600', bg: 'bg-purple-50', icon: '🧪', border: 'border-purple-200 hover:border-purple-300' },
    lpm: { gradient: 'from-lime-600 to-emerald-600', text: 'text-lime-700', bg: 'bg-lime-50', icon: '🐄', border: 'border-lime-200 hover:border-lime-300' }
  };

  const dailyPercentage = Math.min(100, Math.round((dailyProgress.questionsSolvedToday / dailyProgress.dailyTarget) * 100));

  return (
    <div className="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 py-5 sm:py-8 space-y-6 sm:space-y-8 pb-24 md:pb-12">
      
      {/* 1. HERO CARD: TODAY'S QUEST & STREAK (Dead simple to understand) */}
      <div className="bg-gradient-to-br from-[#122840] via-[#1a3d60] to-[#245279] rounded-3xl p-5 sm:p-8 text-white shadow-xl border border-white/10 relative overflow-hidden animate-fade-in-up">
        <div className="absolute -top-24 -right-24 w-64 h-64 rounded-full bg-emerald-400/15 blur-3xl pointer-events-none" />
        <div className="absolute -bottom-24 -left-24 w-64 h-64 rounded-full bg-amber-400/15 blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          
          {/* Welcome Text & Simple Goal */}
          <div className="space-y-3 max-w-2xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-amber-400 text-slate-950 font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider shadow-2xs">
                Target: All India Rank 1 🏆
              </span>
              
              <span className="bg-orange-500/30 text-amber-300 border border-amber-400/40 text-xs font-bold px-3 py-0.5 rounded-full flex items-center space-x-1.5 shadow-2xs">
                <Flame className="w-4 h-4 text-amber-400 fill-amber-400 animate-bounce" />
                <span>{dailyProgress.streakDays} Day Streak!</span>
              </span>
            </div>

            <h1 className="text-2xl sm:text-4xl font-black tracking-tight leading-tight">
              Hello, {userProfile.name}! 👋
            </h1>

            <p className="text-xs sm:text-base text-slate-200 leading-relaxed font-medium">
              Ready to practice today? Complete your daily 20 questions to boost your speed and master tricky ICAR PG questions!
            </p>

            {/* Daily Goal Visual Progress Bar */}
            <div className="bg-white/10 backdrop-blur-md rounded-2xl p-4 max-w-lg border border-white/15 space-y-2">
              <div className="flex items-center justify-between text-xs sm:text-sm">
                <span className="font-extrabold text-amber-300 flex items-center space-x-1.5">
                  <Target className="w-4 h-4 text-amber-400 shrink-0" />
                  <span>Today's Goal: {dailyProgress.questionsSolvedToday} / {dailyProgress.dailyTarget} Questions</span>
                </span>
                <span className="font-mono text-white font-black">{dailyPercentage}%</span>
              </div>
              
              <div className="bg-white/20 h-3 rounded-full overflow-hidden p-0.5">
                <div 
                  className="bg-gradient-to-r from-amber-400 via-orange-400 to-emerald-400 h-full rounded-full transition-all duration-700 relative overflow-hidden"
                  style={{ width: `${Math.max(5, dailyPercentage)}%` }}
                >
                  <div className="absolute inset-0 shimmer-bar" />
                </div>
              </div>

              <p className="text-[11px] text-slate-300 font-medium">
                {dailyProgress.questionsSolvedToday >= dailyProgress.dailyTarget
                  ? '🎉 Daily goal achieved! Keep drilling for extra rank points!'
                  : `Only ${dailyProgress.dailyTarget - dailyProgress.questionsSolvedToday} more questions to finish today's mission! 🚀`}
              </p>
            </div>

            {/* Big 1-Click Action Buttons */}
            <div className="flex flex-wrap items-center gap-3 pt-2">
              <button
                onClick={() => onLaunchPresetDrill('standard_20')}
                className="px-6 py-3.5 bg-gradient-to-r from-amber-400 via-orange-400 to-amber-500 hover:from-amber-500 hover:to-orange-500 text-slate-950 font-black text-xs sm:text-sm rounded-2xl shadow-lg flex items-center space-x-2 transition-transform active:scale-95 cursor-pointer touch-manipulation"
              >
                <Zap className="w-4 h-4 fill-current shrink-0" />
                <span>Start Daily 20-Q Quiz ⚡</span>
              </button>

              <button
                onClick={onOpenSpacedRepetition}
                className="px-5 py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs sm:text-sm rounded-2xl shadow-md flex items-center space-x-2 transition-transform active:scale-95 cursor-pointer touch-manipulation"
              >
                <Brain className="w-4 h-4 shrink-0" />
                <span>Flashcards ({srsMetrics.dueToday} Due)</span>
              </button>

              <button
                onClick={onLaunchCBT}
                className="px-5 py-3.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs sm:text-sm rounded-2xl shadow-md flex items-center space-x-2 transition-transform active:scale-95 cursor-pointer touch-manipulation"
              >
                <Play className="w-4 h-4 fill-current shrink-0" />
                <span>Full CBT Mock Exam</span>
              </button>
            </div>
          </div>

          {/* Quick Roll & Status Pill Card */}
          <div className="bg-white/10 backdrop-blur-md p-5 rounded-3xl border border-white/15 shrink-0 flex flex-col justify-between text-center min-w-[200px] space-y-4">
            <div>
              <p className="text-[10px] text-amber-200 uppercase font-black tracking-wider">Candidate Roll</p>
              <p className="text-xs font-mono font-bold text-white mt-0.5">{userProfile.rollNumber}</p>
            </div>

            <div className="border-t border-white/15 pt-3">
              <p className="text-[10px] text-amber-200 uppercase font-black tracking-wider">Accuracy Level</p>
              <p className="text-3xl font-black text-amber-300 font-mono mt-0.5">
                {totalTests > 0 ? `${avgAccuracy}%` : 'New'}
              </p>
              <span className="text-[10px] text-emerald-300 font-bold block mt-1">
                {totalTests > 0 ? `${totalAttempted} Questions Practiced` : 'Ready for First Quiz'}
              </span>
            </div>
          </div>

        </div>
      </div>

      {/* 2. THREE BIG COLORFUL STAT CARDS (Simple enough for a 13-year-old) */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        
        {/* Stat 1: Accuracy */}
        <div className="bg-gradient-to-br from-emerald-50 via-teal-50/40 to-emerald-50 border-2 border-emerald-200 p-5 rounded-3xl shadow-xs space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-black uppercase text-emerald-800 tracking-wide">Your Accuracy</span>
            <span className="text-2xl p-2 rounded-2xl bg-emerald-100 text-emerald-800">🎯</span>
          </div>
          <div className="space-y-0.5">
            <span className="text-3xl sm:text-4xl font-black text-emerald-950 font-mono">
              {totalTests > 0 ? `${avgAccuracy}%` : '100%'}
            </span>
            <p className="text-xs text-emerald-800 font-semibold">
              {totalTests > 0 
                ? `${Math.round(avgAccuracy / 10)} out of every 10 answers correct!` 
                : 'Take your first quiz to calculate accuracy!'}
            </p>
          </div>
        </div>

        {/* Stat 2: Total Questions Available */}
        <div className="bg-gradient-to-br from-blue-50 via-indigo-50/40 to-blue-50 border-2 border-blue-200 p-5 rounded-3xl shadow-xs space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-black uppercase text-blue-800 tracking-wide">Question Bank</span>
            <span className="text-2xl p-2 rounded-2xl bg-blue-100 text-blue-800">📚</span>
          </div>
          <div className="space-y-0.5">
            <span className="text-3xl sm:text-4xl font-black text-blue-950 font-mono">
              {questions.length}
            </span>
            <p className="text-xs text-blue-800 font-semibold">
              Authentic textbook questions across 54 chapters!
            </p>
          </div>
        </div>

        {/* Stat 3: Flashcard Memory */}
        <div 
          onClick={onOpenSpacedRepetition}
          className="bg-gradient-to-br from-purple-50 via-violet-50/40 to-purple-50 border-2 border-purple-200 p-5 rounded-3xl shadow-xs space-y-2 cursor-pointer hover:border-purple-300 transition-all active:scale-98"
        >
          <div className="flex items-center justify-between">
            <span className="text-xs font-black uppercase text-purple-800 tracking-wide">Memory Flashcards</span>
            <span className="text-2xl p-2 rounded-2xl bg-purple-100 text-purple-800">🧠</span>
          </div>
          <div className="space-y-0.5">
            <span className="text-3xl sm:text-4xl font-black text-purple-950 font-mono">
              {srsMetrics.dueToday} Due
            </span>
            <p className="text-xs text-purple-800 font-semibold flex items-center justify-between">
              <span>{srsMetrics.totalEnrolled} cards in your memory box</span>
              <span className="underline font-bold">Review ➔</span>
            </p>
          </div>
        </div>

      </div>

      {/* 3. QUICK PLAY ARCADE MODES (Inviting, colorful game-style cards) */}
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base sm:text-lg font-black text-slate-900 flex items-center space-x-2">
              <span>🎮 Quick Play Quizzes</span>
            </h3>
            <p className="text-xs text-slate-500 font-medium">
              Pick a quick mode below to test your knowledge in minutes!
            </p>
          </div>

          <button
            onClick={onOpenDrillLauncher}
            className="text-xs font-black text-indigo-600 hover:text-indigo-700 bg-indigo-50 border border-indigo-200 px-3 py-1.5 rounded-xl transition-colors cursor-pointer"
          >
            All Drill Modes ➔
          </button>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
          
          {/* Mode 1: 5-Min Lightning */}
          <div
            onClick={() => onLaunchPresetDrill('lightning_10')}
            className="p-4 rounded-3xl border-2 border-amber-200 bg-gradient-to-br from-amber-50 to-orange-50/40 hover:border-amber-400 transition-all cursor-pointer shadow-xs active:scale-95 space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="text-3xl p-2 rounded-2xl bg-white shadow-2xs">⚡</span>
              <span className="text-[10px] font-black px-2 py-0.5 rounded-full bg-amber-200 text-amber-900">
                5 MINS
              </span>
            </div>
            <div>
              <h4 className="font-black text-slate-900 text-base">Lightning Quiz</h4>
              <p className="text-xs text-slate-500 mt-0.5">10 questions. Quick speed boost!</p>
            </div>
            <div className="pt-2 border-t border-amber-200/60 flex items-center justify-between text-xs font-black text-amber-800">
              <span>Play Now</span>
              <ArrowRight className="w-4 h-4" />
            </div>
          </div>

          {/* Mode 2: Daily Standard */}
          <div
            onClick={() => onLaunchPresetDrill('standard_20')}
            className="p-4 rounded-3xl border-2 border-emerald-200 bg-gradient-to-br from-emerald-50 to-teal-50/40 hover:border-emerald-400 transition-all cursor-pointer shadow-xs active:scale-95 space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="text-3xl p-2 rounded-2xl bg-white shadow-2xs">🎯</span>
              <span className="text-[10px] font-black px-2 py-0.5 rounded-full bg-emerald-200 text-emerald-900">
                15 MINS
              </span>
            </div>
            <div>
              <h4 className="font-black text-slate-900 text-base">Daily Champion</h4>
              <p className="text-xs text-slate-500 mt-0.5">20 questions. The official standard.</p>
            </div>
            <div className="pt-2 border-t border-emerald-200/60 flex items-center justify-between text-xs font-black text-emerald-800">
              <span>Play Now</span>
              <ArrowRight className="w-4 h-4" />
            </div>
          </div>

          {/* Mode 3: Mistake Buster */}
          <div
            onClick={() => onLaunchPresetDrill('weak_blitz')}
            className="p-4 rounded-3xl border-2 border-rose-200 bg-gradient-to-br from-rose-50 to-pink-50/40 hover:border-rose-400 transition-all cursor-pointer shadow-xs active:scale-95 space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="text-3xl p-2 rounded-2xl bg-white shadow-2xs">🛡️</span>
              <span className="text-[10px] font-black px-2 py-0.5 rounded-full bg-rose-200 text-rose-900">
                SMART
              </span>
            </div>
            <div>
              <h4 className="font-black text-slate-900 text-base">Mistake Buster</h4>
              <p className="text-xs text-slate-500 mt-0.5">Practice questions you got wrong!</p>
            </div>
            <div className="pt-2 border-t border-rose-200/60 flex items-center justify-between text-xs font-black text-rose-800">
              <span>Fix Mistakes</span>
              <ArrowRight className="w-4 h-4" />
            </div>
          </div>

          {/* Mode 4: Full NTA CBT Mock */}
          <div
            onClick={onLaunchCBT}
            className="p-4 rounded-3xl border-2 border-indigo-200 bg-gradient-to-br from-indigo-50 to-purple-50/40 hover:border-indigo-400 transition-all cursor-pointer shadow-xs active:scale-95 space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="text-3xl p-2 rounded-2xl bg-white shadow-2xs">🏆</span>
              <span className="text-[10px] font-black px-2 py-0.5 rounded-full bg-indigo-200 text-indigo-900">
                120 QS
              </span>
            </div>
            <div>
              <h4 className="font-black text-slate-900 text-base">Official CBT Mock</h4>
              <p className="text-xs text-slate-500 mt-0.5">Full exam interface with NTA palette.</p>
            </div>
            <div className="pt-2 border-t border-indigo-200/60 flex items-center justify-between text-xs font-black text-indigo-800">
              <span>Start Mock</span>
              <ArrowRight className="w-4 h-4" />
            </div>
          </div>

        </div>
      </div>

      {/* 4. SUBJECT MASTERY MAP (Clean, Colorful & Neatly Foldable) */}
      <div className="space-y-4">
        
        {/* Header & Filter Pills */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h3 className="text-base sm:text-lg font-black text-slate-900 flex items-center space-x-2">
              <Compass className="w-5 h-5 text-emerald-600" />
              <span>Subject Explorer &amp; Chapters</span>
            </h3>
            <p className="text-xs text-slate-500 font-medium">
              Pick any subject to start a focused quiz or view its 6 chapters.
            </p>
          </div>

          {/* Clean Filter Tabs */}
          <div className="flex items-center gap-1.5 text-xs overflow-x-auto no-scrollbar pb-1 sm:pb-0 flex-nowrap sm:flex-wrap">
            <button
              onClick={() => {
                soundFx.playPop();
                setSubjectFilter('all');
              }}
              className={`px-3.5 py-1.5 rounded-xl font-bold transition-all cursor-pointer active:scale-95 ${
                subjectFilter === 'all' 
                  ? 'bg-slate-900 text-white shadow-xs' 
                  : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              All Subjects (9)
            </button>
            
            <button
              onClick={() => {
                soundFx.playPop();
                setSubjectFilter('1st_year');
              }}
              className={`px-3.5 py-1.5 rounded-xl font-bold transition-all cursor-pointer active:scale-95 ${
                subjectFilter === '1st_year' 
                  ? 'bg-indigo-600 text-white shadow-xs' 
                  : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              1st Year (4)
            </button>

            <button
              onClick={() => {
                soundFx.playPop();
                setSubjectFilter('2nd_year');
              }}
              className={`px-3.5 py-1.5 rounded-xl font-bold transition-all cursor-pointer active:scale-95 ${
                subjectFilter === '2nd_year' 
                  ? 'bg-purple-600 text-white shadow-xs' 
                  : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              2nd Year (5)
            </button>

            <button
              onClick={() => {
                soundFx.playPop();
                setSubjectFilter('veterinary_science');
              }}
              className={`px-3.5 py-1.5 rounded-xl font-bold transition-all cursor-pointer active:scale-95 ${
                subjectFilter === 'veterinary_science' 
                  ? 'bg-blue-600 text-white shadow-xs' 
                  : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              Vet Science
            </button>

            <button
              onClick={() => {
                soundFx.playPop();
                setSubjectFilter('animal_science');
              }}
              className={`px-3.5 py-1.5 rounded-xl font-bold transition-all cursor-pointer active:scale-95 ${
                subjectFilter === 'animal_science' 
                  ? 'bg-teal-600 text-white shadow-xs' 
                  : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              Animal Science
            </button>
          </div>
        </div>

        {/* 9 Colorful Subject Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {displayedSubjects.map(sub => {
            const subQuestions = questions.filter(q => q.subjectId === sub.id);
            const stats = subjectStats[sub.id];
            const hasData = stats && stats.total > 0;
            const accuracy = hasData ? stats.accuracy : null;
            const isExpanded = !!expandedSubjects[sub.id];
            const theme = subjectStyles[sub.id] || {
              gradient: 'from-slate-500 to-slate-700',
              text: 'text-slate-700',
              bg: 'bg-slate-50',
              icon: '📖',
              border: 'border-slate-200 hover:border-slate-300'
            };

            return (
              <div
                key={sub.id}
                className={`bg-white rounded-3xl border-2 p-5 shadow-xs flex flex-col justify-between space-y-4 transition-all ${theme.border}`}
              >
                <div>
                  
                  {/* Card Header: Icon, Name, Code, Accuracy */}
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex items-center space-x-3">
                      <div className="w-12 h-12 rounded-2xl bg-slate-50 border border-slate-100 flex items-center justify-center text-2xl shadow-2xs shrink-0">
                        {theme.icon}
                      </div>

                      <div>
                        <div className="flex items-center space-x-1.5">
                          <h4 className="font-black text-slate-900 text-base leading-snug">
                            {sub.name}
                          </h4>
                        </div>

                        <div className="flex items-center space-x-1.5 mt-0.5">
                          <span className="font-mono text-[10px] font-black bg-slate-100 text-slate-700 px-2 py-0.5 rounded-md">
                            {sub.code}
                          </span>
                          <span className="text-[11px] text-slate-400 font-bold">
                            &bull; {sub.domain === 'veterinary_science' ? 'Vet Science' : 'Animal Science'}
                          </span>
                        </div>
                      </div>
                    </div>

                    {/* Accuracy Badge */}
                    {hasData ? (
                      <span className={`text-xs font-black px-2.5 py-1 rounded-full border shadow-2xs shrink-0 ${
                        accuracy! >= 75
                          ? 'bg-emerald-50 text-emerald-800 border-emerald-300'
                          : accuracy! >= 60
                          ? 'bg-amber-50 text-amber-800 border-amber-300'
                          : 'bg-rose-50 text-rose-800 border-rose-300'
                      }`}>
                        {accuracy}% Right
                      </span>
                    ) : (
                      <span className="text-[10px] bg-slate-100 text-slate-500 font-bold px-2 py-0.5 rounded-full shrink-0">
                        Untested
                      </span>
                    )}
                  </div>

                  {/* Subtitle / MCQ count */}
                  <div className="mt-3 flex items-center justify-between text-xs font-bold text-slate-500">
                    <span>{subQuestions.length} Total MCQs</span>
                    <span>{sub.topics.length} Chapters</span>
                  </div>
                </div>

                {/* Collapsible Chapters Drawer */}
                {sub.topics && sub.topics.length > 0 && (
                  <div className="pt-1">
                    <button
                      type="button"
                      onClick={() => toggleExpandSubject(sub.id)}
                      className="w-full flex items-center justify-between px-3.5 py-2.5 rounded-2xl bg-slate-50 hover:bg-slate-100 border border-slate-200 text-xs font-bold text-slate-700 transition-all active:scale-[0.99] cursor-pointer"
                    >
                      <span className="flex items-center space-x-2">
                        <Layers className="w-3.5 h-3.5 text-slate-500" />
                        <span>View All {sub.topics.length} Chapters</span>
                      </span>
                      {isExpanded ? (
                        <ChevronUp className="w-4 h-4 text-slate-500" />
                      ) : (
                        <ChevronDown className="w-4 h-4 text-slate-500" />
                      )}
                    </button>

                    {isExpanded && (
                      <div className="mt-2 space-y-1.5 max-h-64 overflow-y-auto pr-1 animate-scale-in">
                        {sub.topics.map((unitName, uIdx) => {
                          const unitQuestions = subQuestions.filter(q => q.topic === unitName);
                          return (
                            <div
                              key={unitName}
                              className="p-2.5 rounded-xl bg-slate-50 border border-slate-200/90 hover:border-slate-300 transition-all flex items-center justify-between gap-2"
                            >
                              <div className="min-w-0 flex-1">
                                <div className="flex items-center space-x-1.5">
                                  <span className="text-[9px] font-black uppercase px-1.5 py-0.2 rounded bg-indigo-100 text-indigo-900 shrink-0">
                                    CH {uIdx + 1}
                                  </span>
                                  <span className="text-[10px] font-mono font-bold text-slate-500 shrink-0">
                                    {unitQuestions.length} Qs
                                  </span>
                                </div>
                                <p className="text-xs font-bold text-slate-800 leading-snug mt-0.5 truncate">
                                  {unitName}
                                </p>
                              </div>

                              {onLaunchTopicDrill && unitQuestions.length > 0 && (
                                <button
                                  type="button"
                                  onClick={() => onLaunchTopicDrill(sub.id, unitName, 'instant')}
                                  className="px-2.5 py-1 rounded-lg bg-amber-400 hover:bg-amber-500 text-slate-950 font-black text-[10px] shadow-2xs transition-transform active:scale-95 cursor-pointer shrink-0"
                                >
                                  Play
                                </button>
                              )}
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </div>
                )}

                {/* 2 Big Action Buttons */}
                <div className="pt-2 border-t border-slate-100 flex items-center gap-2">
                  <button
                    onClick={() => onLaunchSubjectPractice(sub.id)}
                    className="flex-1 py-2.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl transition-all font-black text-xs flex items-center justify-center space-x-1.5 shadow-sm active:scale-95 cursor-pointer"
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span>Play Subject Quiz</span>
                  </button>

                  {onLaunchSubjectSRS && (
                    <button
                      onClick={() => onLaunchSubjectSRS(sub.id)}
                      className="p-2.5 bg-indigo-50 hover:bg-indigo-600 text-indigo-700 hover:text-white rounded-xl border border-indigo-200 transition-colors cursor-pointer"
                      title="Review Flashcards for this subject"
                    >
                      <Brain className="w-4 h-4" />
                    </button>
                  )}
                </div>

              </div>
            );
          })}
        </div>
      </div>

      {/* 5. RECENT ACTIVITY (Simple & Clean) */}
      <div className="bg-white border-2 border-slate-200/90 rounded-3xl p-6 shadow-sm space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-black text-slate-900 flex items-center space-x-2">
              <TrendingUp className="w-5 h-5 text-emerald-600" />
              <span>Recent Quizzes Taken</span>
            </h3>
            <p className="text-xs text-slate-500 font-medium">
              Check your scores and review questions you missed.
            </p>
          </div>
        </div>

        {testResults.length === 0 ? (
          <div className="p-8 text-center border-2 border-dashed border-slate-200 rounded-2xl space-y-3">
            <span className="text-4xl">🚀</span>
            <p className="text-sm font-black text-slate-800">No quizzes played yet!</p>
            <p className="text-xs text-slate-500 max-w-sm mx-auto">
              Start with the Daily 20-Q Quiz above or choose any subject to begin your journey to All India Rank 1.
            </p>
            <button
              onClick={() => onLaunchPresetDrill('standard_20')}
              className="px-6 py-2.5 bg-gradient-to-r from-amber-400 to-orange-400 text-slate-950 rounded-xl text-xs font-black shadow-md transition-transform active:scale-95 cursor-pointer"
            >
              Play Your First Quiz ⚡
            </button>
          </div>
        ) : (
          <div className="space-y-2.5">
            {testResults.slice(0, 5).map(res => (
              <div
                key={res.id}
                onClick={() => onViewResult(res)}
                className="p-4 rounded-2xl border border-slate-200 hover:border-indigo-300 bg-slate-50/50 hover:bg-indigo-50/20 flex flex-wrap items-center justify-between gap-3 transition-all cursor-pointer shadow-2xs"
              >
                <div>
                  <h4 className="font-black text-sm text-slate-900">{res.title}</h4>
                  <div className="flex items-center space-x-2 text-[11px] text-slate-500 font-medium mt-0.5">
                    <span>{res.dateString}</span>
                    <span>&bull;</span>
                    <span>{res.totalQuestions} Questions</span>
                    <span>&bull;</span>
                    <span className="font-mono text-emerald-700 font-bold">{res.accuracy}% Accuracy</span>
                  </div>
                </div>

                <div className="flex items-center space-x-3">
                  <div className="text-right">
                    <span className="text-sm font-black text-slate-900 block font-mono">
                      {res.totalScore} / {res.maxPossibleScore}
                    </span>
                    <span className="text-[10px] text-slate-400 font-bold">Marks</span>
                  </div>

                  <span className="p-2 rounded-xl bg-white border border-slate-200 text-slate-700">
                    <ChevronRight className="w-4 h-4" />
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  );
};
