import React from 'react';
import { BarChart3, TrendingUp, Award, Calendar, Trash2, ChevronRight, BookOpen } from 'lucide-react';
import { TestResult, Domain } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { StorageService } from '../../storage/db';

interface AnalyticsViewProps {
  testResults: TestResult[];
  onSelectResult: (result: TestResult) => void;
  onRefreshResults: () => void;
}

export const AnalyticsView: React.FC<AnalyticsViewProps> = ({
  testResults,
  onSelectResult,
  onRefreshResults
}) => {
  const handleDeleteTest = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (window.confirm('Delete this test record from history?')) {
      StorageService.deleteTestResult(id);
      onRefreshResults();
    }
  };

  const handleClearHistory = () => {
    if (window.confirm('Clear all test history? This cannot be undone.')) {
      localStorage.removeItem('icar_pg_results_v1');
      onRefreshResults();
    }
  };

  // Cumulative computations
  const totalTests = testResults.length;
  const totalQuestionsAttempted = testResults.reduce((sum, r) => sum + r.attemptedCount, 0);
  const totalCorrect = testResults.reduce((sum, r) => sum + r.correctCount, 0);
  const cumulativeAccuracy = totalQuestionsAttempted > 0
    ? Math.round((totalCorrect / totalQuestionsAttempted) * 100)
    : 0;

  // Aggregate performance per subject across all tests
  const subjectAggregates: Record<string, { attempted: number; correct: number; total: number; name: string; domain: Domain }> = {};

  testResults.forEach(r => {
    Object.values(r.subjectPerformance).forEach(sub => {
      if (!subjectAggregates[sub.subjectId]) {
        subjectAggregates[sub.subjectId] = {
          attempted: 0,
          correct: 0,
          total: 0,
          name: sub.subjectName,
          domain: sub.domain
        };
      }
      subjectAggregates[sub.subjectId].attempted += sub.attempted;
      subjectAggregates[sub.subjectId].correct += sub.correct;
      subjectAggregates[sub.subjectId].total += sub.totalQuestions;
    });
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight flex items-center space-x-2.5">
            <BarChart3 className="w-6 h-6 text-emerald-600" />
            <span>Cumulative Performance &amp; History</span>
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
            Evaluate your progress toward All India Rank 1 with domain balance and subject-wise mastery.
          </p>
        </div>

        {totalTests > 0 && (
          <button
            onClick={handleClearHistory}
            className="text-xs text-red-600 hover:text-red-700 hover:bg-red-50 px-3 py-2 rounded-lg border border-red-200 font-medium transition-colors"
          >
            Clear All History
          </button>
        )}
      </div>

      {/* Top 4 Cumulative KPI Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
          <p className="text-xs font-semibold text-slate-500">Total CBTs Completed</p>
          <p className="text-2xl font-black text-slate-900 mt-1">{totalTests}</p>
        </div>

        <div className="bg-white p-4 rounded-xl border border-blue-200 shadow-2xs">
          <p className="text-xs font-semibold text-blue-700">Questions Solved</p>
          <p className="text-2xl font-black text-blue-900 mt-1">{totalQuestionsAttempted}</p>
        </div>

        <div className="bg-white p-4 rounded-xl border border-emerald-200 shadow-2xs">
          <p className="text-xs font-semibold text-emerald-700">Overall Accuracy</p>
          <p className="text-2xl font-black text-emerald-900 mt-1">{cumulativeAccuracy}%</p>
        </div>

        <div className="bg-white p-4 rounded-xl border border-amber-200 shadow-2xs">
          <p className="text-xs font-semibold text-amber-700">Target Trajectory</p>
          <p className="text-base font-extrabold text-amber-900 mt-2">
            {cumulativeAccuracy >= 80 ? 'AIR 1 Track' : cumulativeAccuracy >= 65 ? 'Top 10 Track' : 'Foundational'}
          </p>
        </div>
      </div>

      {/* Cumulative Subject Mastery Table */}
      {Object.keys(subjectAggregates).length > 0 && (
        <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
          <h3 className="font-extrabold text-slate-900 text-base flex items-center space-x-2">
            <TrendingUp className="w-5 h-5 text-emerald-600" />
            <span>Cumulative Subject Mastery</span>
          </h3>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
            {Object.entries(subjectAggregates).map(([subId, data]) => {
              const acc = data.attempted > 0 ? Math.round((data.correct / data.attempted) * 100) : 0;
              const isStrong = acc >= 75;

              return (
                <div
                  key={subId}
                  className="p-3.5 rounded-lg border border-slate-200 bg-slate-50/60 flex flex-col justify-between"
                >
                  <div className="flex items-start justify-between">
                    <div>
                      <span className="font-bold text-xs text-slate-900 block">{data.name}</span>
                      <span className="text-[10px] text-slate-500 uppercase">
                        {data.domain === 'veterinary_science' ? 'Veterinary Science' : 'Animal Science'}
                      </span>
                    </div>
                    <span className={`text-xs font-bold px-2 py-0.5 rounded ${
                      isStrong ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                    }`}>
                      {acc}%
                    </span>
                  </div>

                  <div className="mt-3 flex items-center justify-between text-[11px] text-slate-500 border-t border-slate-200 pt-2 font-mono">
                    <span>Attempted: {data.attempted}</span>
                    <span>Correct: {data.correct}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Test History List */}
      <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
        <h3 className="font-extrabold text-slate-900 text-base flex items-center space-x-2">
          <Calendar className="w-5 h-5 text-emerald-600" />
          <span>All Completed Examinations ({testResults.length})</span>
        </h3>

        {testResults.length === 0 ? (
          <div className="p-8 text-center text-slate-500 text-xs">
            No examinations taken yet. Your test history and scorecards will appear here.
          </div>
        ) : (
          <div className="space-y-3">
            {testResults.map(r => (
              <div
                key={r.id}
                onClick={() => onSelectResult(r)}
                className="p-4 rounded-xl border border-slate-200 hover:border-emerald-400 bg-slate-50/50 hover:bg-emerald-50/20 transition-all cursor-pointer flex flex-wrap items-center justify-between gap-4"
              >
                <div>
                  <h4 className="font-bold text-slate-900 text-sm">{r.title}</h4>
                  <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 mt-1">
                    <span>{r.dateString}</span>
                    <span>&bull;</span>
                    <span>{r.totalQuestions} Questions</span>
                    <span>&bull;</span>
                    <span className="text-emerald-700 font-semibold">{r.correctCount} Correct</span>
                    <span>&bull;</span>
                    <span className="text-red-600 font-semibold">{r.incorrectCount} Incorrect</span>
                  </div>
                </div>

                <div className="flex items-center space-x-4">
                  <div className="text-right">
                    <span className="font-black text-slate-900 text-base">
                      {r.totalScore} <span className="text-xs text-slate-400">/ {r.maxPossibleScore}</span>
                    </span>
                    <span className="block text-xs font-bold text-emerald-600">
                      {r.accuracy}% Accuracy
                    </span>
                  </div>

                  <button
                    onClick={(e) => handleDeleteTest(r.id, e)}
                    className="p-1.5 text-slate-400 hover:text-red-600 hover:bg-red-50 rounded"
                    title="Delete record"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>

                  <ChevronRight className="w-4 h-4 text-slate-400" />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  );
};
