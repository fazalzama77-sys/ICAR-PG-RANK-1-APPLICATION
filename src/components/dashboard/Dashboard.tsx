import React, { useState } from 'react';
import { 
  Award, 
  Target, 
  BookOpen, 
  Clock, 
  ChevronRight, 
  Play, 
  Sparkles, 
  Layers, 
  ShieldCheck, 
  TrendingUp,
  Brain,
  Zap,
  Flame,
  AlertTriangle,
  CheckCircle2,
  Filter,
  BarChart3
} from 'lucide-react';
import { Question, TestResult, DrillPreset, Domain } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { UserProfile, StorageService } from '../../storage/db';

interface DashboardProps {
  questions: Question[];
  testResults: TestResult[];
  userProfile: UserProfile;
  onLaunchCBT: () => void;
  onLaunchSubjectPractice: (subjectId: string) => void;
  onLaunchSubjectSRS?: (subjectId: string) => void;
  onLaunchPresetDrill: (preset: DrillPreset) => void;
  onOpenSpacedRepetition: () => void;
  onOpenDrillLauncher: () => void;
  onViewResult: (result: TestResult) => void;
  onNavigateToBank: () => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  questions,
  testResults,
  userProfile,
  onLaunchCBT,
  onLaunchSubjectPractice,
  onLaunchSubjectSRS,
  onLaunchPresetDrill,
  onOpenSpacedRepetition,
  onOpenDrillLauncher,
  onViewResult,
  onNavigateToBank
}) => {
  const [subjectFilter, setSubjectFilter] = useState<'all' | '1st_year' | '2nd_year' | 'veterinary_science' | 'animal_science'>('all');

  // Daily Progress & Streak
  const dailyProgress = StorageService.getDailyProgress();
  const srsMetrics = StorageService.getSRSMetrics(questions);

  // Aggregate stats
  const totalTests = testResults.length;
  const avgAccuracy = totalTests > 0
    ? Math.round(testResults.reduce((acc, r) => acc + r.accuracy, 0) / totalTests)
    : 0;
  const highestScore = totalTests > 0
    ? Math.max(...testResults.map(r => r.totalScore))
    : 0;

  // Negative marking penalty metrics
  const totalIncorrectAnswers = testResults.reduce((acc, r) => acc + r.incorrectCount, 0);
  const totalCorrectAnswers = testResults.reduce((acc, r) => acc + r.correctCount, 0);
  const totalAttempted = totalCorrectAnswers + totalIncorrectAnswers;
  
  // Discipline / Penalty Resistance Score: (Correct / Attempted) * 100
  const disciplineScore = totalAttempted > 0 
    ? Math.round((totalCorrectAnswers / totalAttempted) * 100) 
    : 100;

  // Subject-wise accuracy calculation from test results
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

  // Identify weakest subjects (< 70% accuracy and at least attempted)
  const weakSubjects = SUBJECT_LIST.filter(s => {
    const stat = subjectStats[s.id];
    return stat.total >= 5 && stat.accuracy < 70;
  });

  // Filtered subjects
  const displayedSubjects = SUBJECT_LIST.filter(s => {
    if (subjectFilter === '1st_year') return s.year === '1st_year';
    if (subjectFilter === '2nd_year') return s.year === '2nd_year';
    if (subjectFilter === 'veterinary_science') return s.domain === 'veterinary_science';
    if (subjectFilter === 'animal_science') return s.domain === 'animal_science';
    return true;
  });

  const dailyPercentage = Math.min(100, Math.round((dailyProgress.questionsSolvedToday / dailyProgress.dailyTarget) * 100));

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      
      {/* 1. AIR 1 Mission Command Hero */}
      <div className="bg-gradient-to-r from-[#172e48] via-[#1f3f60] to-[#28537d] rounded-2xl p-6 sm:p-8 text-white shadow-md relative overflow-hidden">
        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-amber-400 text-slate-900 font-extrabold text-[11px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
                Mission AIR 1
              </span>
              <span className="text-xs text-slate-200 font-medium">
                ICAR AIEEA PG (M.V.Sc.) Strategic Blueprint
              </span>
              <span className="bg-emerald-500/30 text-emerald-200 border border-emerald-400/40 text-[11px] font-bold px-2 py-0.5 rounded-full flex items-center space-x-1">
                <Flame className="w-3 h-3 text-amber-400 fill-amber-400" />
                <span>{dailyProgress.streakDays} Days Streak</span>
              </span>
            </div>

            <h1 className="text-2xl sm:text-3xl font-black tracking-tight leading-tight">
              Welcome, {userProfile.name}
            </h1>

            <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
              Targeted early preparation starting in 2nd year B.V.Sc. &amp; A.H. By mastering 1st-year (Anatomy, Physiology, Biochemistry, LPM) and 2nd-year (Pathology, Microbiology, Parasitology, AGB, Nutrition) MCQs through daily rapid drills and active spaced recall, you eliminate 5th-year internship pressure and secure All India Rank 1.
            </p>

            {/* Daily Target Progress Bar */}
            <div className="bg-white/10 rounded-xl p-3 max-w-lg border border-white/15 space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="font-bold text-amber-200 flex items-center space-x-1">
                  <Target className="w-3.5 h-3.5" />
                  <span>Daily Study Target: {dailyProgress.questionsSolvedToday} / {dailyProgress.dailyTarget} MCQs</span>
                </span>
                <span className="font-mono text-white font-bold">{dailyPercentage}%</span>
              </div>
              <div className="bg-white/20 h-2 rounded-full overflow-hidden">
                <div 
                  className="bg-amber-400 h-2 rounded-full transition-all duration-500"
                  style={{ width: `${dailyPercentage}%` }}
                />
              </div>
            </div>

            {/* Core Action CTAs */}
            <div className="flex flex-wrap items-center gap-3 pt-2">
              <button
                onClick={onOpenDrillLauncher}
                className="bg-amber-400 hover:bg-amber-500 text-slate-950 font-black text-xs sm:text-sm px-5 py-2.5 rounded-lg shadow-md flex items-center space-x-2 transition-transform transform active:scale-98 cursor-pointer"
              >
                <Zap className="w-4 h-4 fill-current" />
                <span>Rapid Daily Drill</span>
              </button>

              <button
                onClick={onOpenSpacedRepetition}
                className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold text-xs sm:text-sm px-4 py-2.5 rounded-lg shadow-md flex items-center space-x-2 transition-transform transform active:scale-98 cursor-pointer"
              >
                <Brain className="w-4 h-4" />
                <span>Spaced Repetition ({srsMetrics.dueToday} Due)</span>
              </button>

              <button
                onClick={onLaunchCBT}
                className="bg-emerald-500 hover:bg-emerald-600 text-white font-bold text-xs sm:text-sm px-4 py-2.5 rounded-lg shadow-md flex items-center space-x-2 transition-transform transform active:scale-98 cursor-pointer"
              >
                <Play className="w-4 h-4 fill-current" />
                <span>Full CBT Mock Exam</span>
              </button>
            </div>
          </div>

          {/* Quick Metrics Badge */}
          <div className="bg-white/10 backdrop-blur-xs p-5 rounded-xl border border-white/15 shrink-0 flex flex-col space-y-3 text-center min-w-[220px]">
            <div>
              <p className="text-[10px] text-amber-200 uppercase font-bold tracking-wider">Candidate Roll No.</p>
              <p className="text-xs font-mono font-bold text-white">{userProfile.rollNumber}</p>
            </div>
            <div className="border-t border-white/10 pt-2">
              <p className="text-[10px] text-amber-200 uppercase font-bold tracking-wider">Preparedness Index</p>
              <p className="text-2xl font-black text-amber-300">
                {totalTests > 0 ? `${avgAccuracy}%` : 'Ready to Start'}
              </p>
            </div>
            <div className="border-t border-white/10 pt-2 flex justify-around text-xs">
              <div>
                <span className="text-slate-300 block text-[10px]">CBTs Taken</span>
                <span className="font-bold text-white font-mono">{totalTests}</span>
              </div>
              <div className="border-l border-white/10 pl-3">
                <span className="text-slate-300 block text-[10px]">Top Score</span>
                <span className="font-bold text-white font-mono">{highestScore}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* 2. Top-Level Strategic Cards: Spaced Repetition Due & Rapid Drill Presets */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        {/* Spaced Repetition Due Deck Card */}
        <div className="bg-white rounded-xl border border-slate-200 p-5 shadow-2xs flex flex-col justify-between space-y-4">
          <div>
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <div className="p-2 rounded-lg bg-indigo-50 text-indigo-700">
                  <Brain className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-extrabold text-slate-900 text-base">Spaced Repetition Active Recall</h3>
                  <p className="text-xs text-slate-500">SuperMemo SM-2 memory consolidation engine</p>
                </div>
              </div>
              <span className="text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-full border border-indigo-200">
                {srsMetrics.dueToday} Due Today
              </span>
            </div>

            <p className="text-xs text-slate-600 mt-3 leading-relaxed">
              Active recall flashcards for anatomy bones, infectious etiologies, drug classes, and genetics ratios. Questions answered incorrectly in tests are automatically queued here.
            </p>

            <div className="grid grid-cols-3 gap-2 mt-4 pt-3 border-t border-slate-100 text-center">
              <div className="bg-slate-50 p-2 rounded-lg border border-slate-200">
                <span className="text-[10px] uppercase font-bold text-amber-600 block">Due Cards</span>
                <span className="text-lg font-black text-slate-900 font-mono">{srsMetrics.dueToday}</span>
              </div>
              <div className="bg-slate-50 p-2 rounded-lg border border-slate-200">
                <span className="text-[10px] uppercase font-bold text-blue-600 block">Learning</span>
                <span className="text-lg font-black text-slate-900 font-mono">{srsMetrics.learning}</span>
              </div>
              <div className="bg-slate-50 p-2 rounded-lg border border-slate-200">
                <span className="text-[10px] uppercase font-bold text-emerald-600 block">Mastered</span>
                <span className="text-lg font-black text-slate-900 font-mono">{srsMetrics.mastered}</span>
              </div>
            </div>
          </div>

          <button
            onClick={onOpenSpacedRepetition}
            className="w-full py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs sm:text-sm rounded-lg shadow-sm flex items-center justify-center space-x-2 transition-colors cursor-pointer"
          >
            <Brain className="w-4 h-4" />
            <span>Open Flashcards Deck ({srsMetrics.dueToday > 0 ? `${srsMetrics.dueToday} Due` : 'Review All'})</span>
          </button>
        </div>

        {/* Rapid Drill Launcher Widget */}
        <div className="bg-white rounded-xl border border-slate-200 p-5 shadow-2xs flex flex-col justify-between space-y-4">
          <div>
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <div className="p-2 rounded-lg bg-amber-50 text-amber-700">
                  <Zap className="w-5 h-5 fill-amber-500" />
                </div>
                <div>
                  <h3 className="font-extrabold text-slate-900 text-base">Rapid Daily Drill Launcher</h3>
                  <p className="text-xs text-slate-500">1-Click presets for speed and negative mark control</p>
                </div>
              </div>
              <button
                onClick={onOpenDrillLauncher}
                className="text-xs font-bold text-amber-700 hover:text-amber-800 underline"
              >
                Custom Drill &rarr;
              </button>
            </div>

            <p className="text-xs text-slate-600 mt-3 leading-relaxed">
              Start a high-yield drill immediately. Choose from instant feedback active learning or official timed test conditions:
            </p>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 mt-3 pt-2 border-t border-slate-100">
              <button
                onClick={() => onLaunchPresetDrill('standard_20')}
                className="p-2.5 rounded-lg border border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 text-left transition-all group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-800 group-hover:text-emerald-700">🎯 Daily 20-Q</span>
                </div>
                <span className="text-[10px] text-slate-500 block">15 Mins &bull; Standard</span>
              </button>

              <button
                onClick={() => onLaunchPresetDrill('lightning_10')}
                className="p-2.5 rounded-lg border border-slate-200 hover:border-amber-500 hover:bg-amber-50/40 text-left transition-all group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-800 group-hover:text-amber-700">⚡ Lightning 10</span>
                </div>
                <span className="text-[10px] text-slate-500 block">7 Mins &bull; Speed Fire</span>
              </button>

              <button
                onClick={() => onLaunchPresetDrill('clinical_blitz')}
                className="p-2.5 rounded-lg border border-slate-200 hover:border-purple-500 hover:bg-purple-50/40 text-left transition-all group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-800 group-hover:text-purple-700">🔬 Paraclinical</span>
                </div>
                <span className="text-[10px] text-slate-500 block">Path, Micro, Parasito</span>
              </button>

              <button
                onClick={() => onLaunchPresetDrill('animal_blitz')}
                className="p-2.5 rounded-lg border border-slate-200 hover:border-teal-500 hover:bg-teal-50/40 text-left transition-all group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-800 group-hover:text-teal-700">🐄 Animal Sci</span>
                </div>
                <span className="text-[10px] text-slate-500 block">LPM, AGB, Nutrition</span>
              </button>

              <button
                onClick={() => onLaunchPresetDrill('weak_blitz')}
                className="p-2.5 rounded-lg border border-slate-200 hover:border-red-500 hover:bg-red-50/40 text-left transition-all group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-800 group-hover:text-red-700">🛡️ Weak Blitz</span>
                </div>
                <span className="text-[10px] text-slate-500 block">Focus on Mistakes</span>
              </button>

              <button
                onClick={onOpenDrillLauncher}
                className="p-2.5 rounded-lg border border-dashed border-slate-300 hover:border-slate-400 text-left transition-all text-slate-600 hover:text-slate-900"
              >
                <span className="text-xs font-bold block">⚙️ More Drills</span>
                <span className="text-[10px] text-slate-400 block">Configure options</span>
              </button>
            </div>
          </div>

          <button
            onClick={() => onLaunchPresetDrill('standard_20')}
            className="w-full py-2.5 bg-amber-500 hover:bg-amber-600 text-slate-950 font-black text-xs sm:text-sm rounded-lg shadow-sm flex items-center justify-center space-x-2 transition-colors cursor-pointer"
          >
            <Play className="w-4 h-4 fill-current" />
            <span>Launch Today's Recommended 20-Q Drill</span>
          </button>
        </div>

      </div>

      {/* 3. AIR 1 Strategic Diagnostics: Discipline & Weak Areas Alert */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        
        {/* Negative Penalty Discipline Card */}
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-2xs space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-extrabold uppercase text-slate-500">Negative Penalty Resistance</span>
            <ShieldCheck className={`w-5 h-5 ${disciplineScore >= 80 ? 'text-emerald-600' : 'text-amber-600'}`} />
          </div>
          <div className="flex items-baseline space-x-2">
            <span className="text-2xl font-black text-slate-900">{disciplineScore}%</span>
            <span className="text-xs text-slate-500">Guessing Discipline</span>
          </div>
          <p className="text-[11px] text-slate-500 leading-normal">
            {disciplineScore >= 80
              ? 'Excellent restraint! You avoid reckless negative marks (-1), which is the #1 discriminator for AIR 1.'
              : 'Alert: High negative penalty bleed. Review questions carefully and avoid guessing uncertain options.'}
          </p>
        </div>

        {/* Total Questions Solved */}
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-2xs space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-extrabold uppercase text-slate-500">Lifetime Question Bank</span>
            <BookOpen className="w-5 h-5 text-blue-600" />
          </div>
          <div className="flex items-baseline space-x-2">
            <span className="text-2xl font-black text-slate-900">{questions.length}</span>
            <span className="text-xs text-slate-500">Verified MCQs</span>
          </div>
          <div className="flex items-center justify-between text-[11px] text-slate-500 pt-1">
            <span>Vet Sci: {questions.filter(q => q.domain === 'veterinary_science').length}</span>
            <span>Animal Sci: {questions.filter(q => q.domain === 'animal_science').length}</span>
            <button onClick={onNavigateToBank} className="text-blue-600 font-bold hover:underline">Manage</button>
          </div>
        </div>

        {/* Weak Areas Alert */}
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-2xs space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-extrabold uppercase text-slate-500">Weak Area Alerts</span>
            <AlertTriangle className={`w-5 h-5 ${weakSubjects.length > 0 ? 'text-amber-500' : 'text-emerald-500'}`} />
          </div>
          {weakSubjects.length > 0 ? (
            <div>
              <span className="text-sm font-bold text-amber-800 block">
                {weakSubjects.length} Subject{weakSubjects.length > 1 ? 's' : ''} Need Revision (&lt; 70%)
              </span>
              <div className="flex flex-wrap gap-1.5 mt-2">
                {weakSubjects.slice(0, 3).map(ws => (
                  <button
                    key={ws.id}
                    onClick={() => onLaunchSubjectPractice(ws.id)}
                    className="text-[10px] bg-amber-50 border border-amber-300 text-amber-900 font-bold px-2 py-0.5 rounded-full hover:bg-amber-100"
                  >
                    {ws.code} ({subjectStats[ws.id].accuracy}%) &rarr;
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div>
              <span className="text-sm font-bold text-emerald-800 block">
                No Critical Weak Subjects
              </span>
              <p className="text-[11px] text-slate-500 mt-1">
                All attempted subjects are maintaining solid accuracy &gt;= 70%. Keep up the consistency!
              </p>
            </div>
          )}
        </div>

      </div>

      {/* 4. Syllabus & Subject Precision Tracker */}
      <div className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h3 className="text-lg font-extrabold text-slate-900 tracking-tight flex items-center space-x-2">
              <Layers className="w-5 h-5 text-emerald-600" />
              <span>Syllabus &amp; Subject Precision Tracker</span>
            </h3>
            <p className="text-xs text-slate-500">
              Track your accuracy, available MCQs, and launch focused drills or active recall flashcards per subject.
            </p>
          </div>

          {/* Filter Chips */}
          <div className="flex flex-wrap gap-1.5 text-xs">
            <button
              onClick={() => setSubjectFilter('all')}
              className={`px-3 py-1 rounded-lg font-semibold transition-colors ${
                subjectFilter === 'all' ? 'bg-slate-900 text-white' : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              All (9)
            </button>
            <button
              onClick={() => setSubjectFilter('1st_year')}
              className={`px-3 py-1 rounded-lg font-semibold transition-colors ${
                subjectFilter === '1st_year' ? 'bg-indigo-600 text-white' : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              1st Year (4)
            </button>
            <button
              onClick={() => setSubjectFilter('2nd_year')}
              className={`px-3 py-1 rounded-lg font-semibold transition-colors ${
                subjectFilter === '2nd_year' ? 'bg-purple-600 text-white' : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              2nd Year (5)
            </button>
            <button
              onClick={() => setSubjectFilter('veterinary_science')}
              className={`px-3 py-1 rounded-lg font-semibold transition-colors ${
                subjectFilter === 'veterinary_science' ? 'bg-blue-600 text-white' : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              Vet Science
            </button>
            <button
              onClick={() => setSubjectFilter('animal_science')}
              className={`px-3 py-1 rounded-lg font-semibold transition-colors ${
                subjectFilter === 'animal_science' ? 'bg-teal-600 text-white' : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              Animal Science
            </button>
          </div>
        </div>

        {/* Subjects Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {displayedSubjects.map(sub => {
            const subQuestions = questions.filter(q => q.subjectId === sub.id);
            const stats = subjectStats[sub.id];
            const hasData = stats && stats.total > 0;
            const accuracy = hasData ? stats.accuracy : null;

            return (
              <div
                key={sub.id}
                className="bg-white rounded-xl border border-slate-200 hover:border-slate-300 p-4 shadow-2xs flex flex-col justify-between space-y-3 transition-all"
              >
                <div>
                  <div className="flex items-start justify-between gap-2">
                    <div>
                      <div className="flex items-center space-x-2">
                        <span className="font-extrabold text-xs sm:text-sm text-slate-900">{sub.name}</span>
                        <span className="font-mono text-[10px] bg-slate-100 text-slate-700 px-1.5 py-0.5 rounded font-bold">
                          {sub.code}
                        </span>
                      </div>
                      <span className="text-[10px] text-slate-400 capitalize block mt-0.5">
                        {sub.year === '1st_year' ? '1st Professional Year' : '2nd Professional Year'} &bull; {sub.domain === 'veterinary_science' ? 'Vet Sci' : 'Animal Sci'}
                      </span>
                    </div>

                    {/* Accuracy Badge */}
                    {hasData ? (
                      <span className={`text-xs font-extrabold px-2 py-0.5 rounded-full border ${
                        accuracy! >= 75
                          ? 'bg-emerald-50 text-emerald-700 border-emerald-300'
                          : accuracy! >= 60
                          ? 'bg-amber-50 text-amber-700 border-amber-300'
                          : 'bg-red-50 text-red-700 border-red-300'
                      }`}>
                        {accuracy}%
                      </span>
                    ) : (
                      <span className="text-[10px] bg-slate-100 text-slate-500 font-medium px-2 py-0.5 rounded-full">
                        Untested
                      </span>
                    )}
                  </div>

                  <p className="text-[11px] text-slate-500 line-clamp-2 mt-2 leading-relaxed">
                    {sub.description}
                  </p>
                </div>

                <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                  <span className="font-mono font-semibold text-slate-500 text-[11px]">
                    {subQuestions.length} MCQs in Bank
                  </span>

                  <div className="flex items-center space-x-2">
                    {onLaunchSubjectSRS && (
                      <button
                        onClick={() => onLaunchSubjectSRS(sub.id)}
                        className="p-1.5 bg-indigo-50 hover:bg-indigo-600 text-indigo-700 hover:text-white rounded-lg transition-colors"
                        title="Review Flashcards for this subject"
                      >
                        <Brain className="w-3.5 h-3.5" />
                      </button>
                    )}

                    <button
                      onClick={() => onLaunchSubjectPractice(sub.id)}
                      className="px-2.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg transition-colors font-bold text-xs flex items-center space-x-1 shadow-2xs"
                      title="Practice this subject"
                    >
                      <Play className="w-3 h-3 fill-current" />
                      <span>Drill</span>
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* 5. Recent CBT Test & Drill History */}
      <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-extrabold text-slate-900 tracking-tight flex items-center space-x-2">
              <TrendingUp className="w-5 h-5 text-emerald-600" />
              <span>Recent CBT Test &amp; Rapid Drill History</span>
            </h3>
            <p className="text-xs text-slate-500">
              Review your negative marking penalties and scorecards.
            </p>
          </div>
        </div>

        {testResults.length === 0 ? (
          <div className="p-8 text-center border border-dashed border-slate-200 rounded-lg space-y-2">
            <ShieldCheck className="w-10 h-10 text-slate-300 mx-auto" />
            <p className="text-xs font-bold text-slate-700">No tests or drills recorded yet</p>
            <p className="text-[11px] text-slate-500">
              Start with a rapid 10-Q or 20-Q drill or take the full 120-question CBT mock exam.
            </p>
            <div className="flex justify-center gap-3 pt-2">
              <button
                onClick={() => onLaunchPresetDrill('standard_20')}
                className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-slate-950 rounded-lg text-xs font-black transition-colors"
              >
                Launch First 20-Q Drill
              </button>
              <button
                onClick={onLaunchCBT}
                className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold transition-colors"
              >
                Take Full 120-Q Mock
              </button>
            </div>
          </div>
        ) : (
          <div className="space-y-3">
            {testResults.slice(0, 5).map(res => (
              <div
                key={res.id}
                className="p-4 rounded-lg border border-slate-200 hover:border-slate-300 bg-slate-50/50 flex flex-wrap items-center justify-between gap-4 transition-colors"
              >
                <div>
                  <h4 className="font-bold text-xs sm:text-sm text-slate-900">{res.title}</h4>
                  <div className="flex flex-wrap items-center gap-2 text-[11px] text-slate-500 mt-1">
                    <span>{res.dateString}</span>
                    <span>&bull;</span>
                    <span>{res.totalQuestions} Questions</span>
                    <span>&bull;</span>
                    <span className="text-red-600 font-medium">
                      -{res.incorrectCount * (res.config?.negativeMarks || 1)} Negative Penalty
                    </span>
                  </div>
                </div>

                <div className="flex items-center space-x-4">
                  <div className="text-right">
                    <div className="font-extrabold text-sm sm:text-base text-slate-900">
                      {res.totalScore} <span className="text-xs text-slate-400">/ {res.maxPossibleScore}</span>
                    </div>
                    <span className="text-[11px] font-bold text-emerald-600">
                      {res.accuracy}% Accuracy
                    </span>
                  </div>

                  <button
                    onClick={() => onViewResult(res)}
                    className="px-3 py-1.5 rounded-lg bg-white hover:bg-slate-100 border border-slate-300 text-xs font-semibold text-slate-700 flex items-center space-x-1"
                  >
                    <span>View Scorecard</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  );
};
