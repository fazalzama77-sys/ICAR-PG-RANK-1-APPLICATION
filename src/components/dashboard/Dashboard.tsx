import React from 'react';
import { Award, Target, BookOpen, Clock, ChevronRight, Play, Sparkles, Layers, ShieldCheck, TrendingUp } from 'lucide-react';
import { Question, TestResult } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { UserProfile } from '../../storage/db';

interface DashboardProps {
  questions: Question[];
  testResults: TestResult[];
  userProfile: UserProfile;
  onLaunchCBT: () => void;
  onLaunchSubjectPractice: (subjectId: string) => void;
  onViewResult: (result: TestResult) => void;
  onNavigateToBank: () => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  questions,
  testResults,
  userProfile,
  onLaunchCBT,
  onLaunchSubjectPractice,
  onViewResult,
  onNavigateToBank
}) => {
  // Aggregate stats
  const totalTests = testResults.length;
  const avgAccuracy = totalTests > 0
    ? Math.round(testResults.reduce((acc, r) => acc + r.accuracy, 0) / totalTests)
    : 0;
  const highestScore = totalTests > 0
    ? Math.max(...testResults.map(r => r.totalScore))
    : 0;

  const firstYearSubjects = SUBJECT_LIST.filter(s => s.year === '1st_year');
  const secondYearSubjects = SUBJECT_LIST.filter(s => s.year === '2nd_year');

  const vetCount = questions.filter(q => q.domain === 'veterinary_science').length;
  const animalCount = questions.filter(q => q.domain === 'animal_science').length;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      
      {/* Welcome & AIR 1 Strategy Hero */}
      <div className="bg-gradient-to-r from-[#172e48] via-[#1f3f60] to-[#28537d] rounded-2xl p-6 sm:p-8 text-white shadow-md relative overflow-hidden">
        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-amber-400 text-slate-900 font-extrabold text-[11px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
                Mission AIR 1
              </span>
              <span className="text-xs text-slate-200 font-medium">
                ICAR AIEEA PG (M.V.Sc.) Entrance Exam
              </span>
            </div>

            <h1 className="text-2xl sm:text-3xl font-black tracking-tight leading-tight">
              Welcome, {userProfile.name}
            </h1>

            <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
              Targeted early preparation starting in 2nd year B.V.Sc. &amp; A.H. By mastering 1st-year (Anatomy, Physiology, Biochemistry, LPM) and 2nd-year (Pathology, Microbiology, Parasitology, AGB, Nutrition) MCQs systematically right now, you eliminate 5th-year internship pressure and secure All India Rank 1.
            </p>

            <div className="flex flex-wrap items-center gap-3 pt-2">
              <button
                onClick={onLaunchCBT}
                className="bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold text-xs sm:text-sm px-5 py-2.5 rounded-lg shadow-md flex items-center space-x-2 transition-transform transform active:scale-98"
              >
                <Play className="w-4 h-4 fill-current" />
                <span>Launch 120-Q CBT Mock Exam</span>
              </button>

              <button
                onClick={onNavigateToBank}
                className="bg-white/10 hover:bg-white/20 text-white font-semibold text-xs sm:text-sm px-4 py-2.5 rounded-lg border border-white/20 flex items-center space-x-2 transition-colors"
              >
                <BookOpen className="w-4 h-4" />
                <span>Manage Question Bank ({questions.length} MCQs)</span>
              </button>
            </div>
          </div>

          {/* Quick Metrics Badge */}
          <div className="bg-white/10 backdrop-blur-xs p-5 rounded-xl border border-white/15 shrink-0 flex flex-col space-y-3 text-center min-w-[200px]">
            <div>
              <p className="text-[11px] text-amber-200 uppercase font-bold tracking-wider">Target Exam</p>
              <p className="text-sm font-extrabold text-white">ICAR AIEEA PG</p>
            </div>
            <div className="border-t border-white/10 pt-2">
              <p className="text-[11px] text-amber-200 uppercase font-bold tracking-wider">Preparedness Index</p>
              <p className="text-2xl font-black text-amber-300">
                {totalTests > 0 ? `${avgAccuracy}%` : 'Ready to Start'}
              </p>
            </div>
            <div className="border-t border-white/10 pt-2 flex justify-around text-xs">
              <div>
                <span className="text-slate-300 block text-[10px]">Tests Taken</span>
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

      {/* 1st & 2nd Year Subject Master Grid */}
      <div className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <h3 className="text-lg font-extrabold text-slate-900 tracking-tight flex items-center space-x-2">
              <Layers className="w-5 h-5 text-emerald-600" />
              <span>Syllabus &amp; Subject Precision Tracker</span>
            </h3>
            <p className="text-xs text-slate-500">
              Practice individual subjects anytime or launch full CBT mock tests.
            </p>
          </div>

          <div className="flex items-center space-x-2 text-xs">
            <span className="bg-blue-100 text-blue-800 font-semibold px-2 py-0.5 rounded">
              Vet Science: {vetCount} Qs
            </span>
            <span className="bg-teal-100 text-teal-800 font-semibold px-2 py-0.5 rounded">
              Animal Science: {animalCount} Qs
            </span>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          {/* 1st Year (Completed Year Revision) */}
          <div className="bg-white rounded-xl border border-slate-200 p-5 shadow-2xs space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div>
                <span className="text-indigo-600 font-extrabold text-xs uppercase tracking-wider">
                  1st Professional Year
                </span>
                <h4 className="font-extrabold text-slate-900 text-base">Completed Year Revision</h4>
              </div>
              <span className="text-xs bg-indigo-50 text-indigo-700 font-bold px-2.5 py-1 rounded-full border border-indigo-200">
                4 Core Subjects
              </span>
            </div>

            <div className="space-y-2.5">
              {firstYearSubjects.map(sub => {
                const subQuestions = questions.filter(q => q.subjectId === sub.id);
                return (
                  <div
                    key={sub.id}
                    className="p-3 rounded-lg border border-slate-200 hover:border-indigo-300 hover:bg-indigo-50/20 transition-all flex items-center justify-between gap-2"
                  >
                    <div>
                      <div className="flex items-center space-x-2">
                        <span className="font-bold text-xs text-slate-800">{sub.name}</span>
                        <span className="font-mono text-[10px] bg-slate-100 text-slate-600 px-1.5 py-0.2 rounded">
                          {sub.code}
                        </span>
                      </div>
                      <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                        {sub.description}
                      </p>
                    </div>

                    <div className="flex items-center space-x-3 shrink-0">
                      <span className="text-xs font-mono font-semibold text-slate-600">
                        {subQuestions.length} Qs
                      </span>
                      <button
                        onClick={() => onLaunchSubjectPractice(sub.id)}
                        className="p-1.5 bg-slate-100 hover:bg-indigo-600 text-slate-600 hover:text-white rounded transition-colors text-xs flex items-center space-x-1"
                        title="Practice this subject"
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* 2nd Year (Current Year Mastery) */}
          <div className="bg-white rounded-xl border border-slate-200 p-5 shadow-2xs space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div>
                <span className="text-purple-600 font-extrabold text-xs uppercase tracking-wider">
                  2nd Professional Year
                </span>
                <h4 className="font-extrabold text-slate-900 text-base">Current Year Active Mastery</h4>
              </div>
              <span className="text-xs bg-purple-50 text-purple-700 font-bold px-2.5 py-1 rounded-full border border-purple-200">
                5 Core Subjects
              </span>
            </div>

            <div className="space-y-2.5">
              {secondYearSubjects.map(sub => {
                const subQuestions = questions.filter(q => q.subjectId === sub.id);
                return (
                  <div
                    key={sub.id}
                    className="p-3 rounded-lg border border-slate-200 hover:border-purple-300 hover:bg-purple-50/20 transition-all flex items-center justify-between gap-2"
                  >
                    <div>
                      <div className="flex items-center space-x-2">
                        <span className="font-bold text-xs text-slate-800">{sub.name}</span>
                        <span className="font-mono text-[10px] bg-slate-100 text-slate-600 px-1.5 py-0.2 rounded">
                          {sub.code}
                        </span>
                      </div>
                      <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                        {sub.description}
                      </p>
                    </div>

                    <div className="flex items-center space-x-3 shrink-0">
                      <span className="text-xs font-mono font-semibold text-slate-600">
                        {subQuestions.length} Qs
                      </span>
                      <button
                        onClick={() => onLaunchSubjectPractice(sub.id)}
                        className="p-1.5 bg-slate-100 hover:bg-purple-600 text-slate-600 hover:text-white rounded transition-colors text-xs flex items-center space-x-1"
                        title="Practice this subject"
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

        </div>
      </div>

      {/* Recent Test History */}
      <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-extrabold text-slate-900 tracking-tight flex items-center space-x-2">
              <TrendingUp className="w-5 h-5 text-emerald-600" />
              <span>Recent CBT Test History</span>
            </h3>
            <p className="text-xs text-slate-500">
              Track your scores, accuracy, and negative marking penalty progression over time.
            </p>
          </div>
        </div>

        {testResults.length === 0 ? (
          <div className="p-8 text-center border border-dashed border-slate-200 rounded-lg">
            <ShieldCheck className="w-10 h-10 text-slate-300 mx-auto mb-2" />
            <p className="text-xs font-bold text-slate-700">No tests taken yet</p>
            <p className="text-[11px] text-slate-500 mt-0.5 mb-3">
              Configure your first practice test or take a full 120-question mock exam.
            </p>
            <button
              onClick={onLaunchCBT}
              className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-xs font-bold transition-colors"
            >
              Take First CBT Test
            </button>
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
                      -{res.incorrectCount * res.config.negativeMarks} Negative Marks
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
                    className="px-3 py-1.5 rounded bg-white hover:bg-slate-100 border border-slate-300 text-xs font-semibold text-slate-700 flex items-center space-x-1"
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
