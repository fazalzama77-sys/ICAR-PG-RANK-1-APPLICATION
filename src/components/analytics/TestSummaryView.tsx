import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { Award, CheckCircle, XCircle, AlertCircle, Clock, BookOpen, RotateCcw, ArrowLeft, BarChart2 } from 'lucide-react';
import { TestResult } from '../../types';
import { QuestionReviewModal } from './QuestionReviewModal';

interface TestSummaryViewProps {
  result: TestResult;
  onRetakeTest: () => void;
  onBackToDashboard: () => void;
}

export const TestSummaryView: React.FC<TestSummaryViewProps> = ({
  result,
  onRetakeTest,
  onBackToDashboard
}) => {
  const [showReviewModal, setShowReviewModal] = useState(false);

  // Trigger celebration confetti if high score
  useEffect(() => {
    if (result.percentage >= 75) {
      try {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 }
        });
      } catch (e) {}
    }
  }, [result.percentage]);

  const formatSeconds = (totalSecs: number) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${mins}m ${secs}s`;
  };

  const avgSecondsPerQ = result.attemptedCount > 0
    ? Math.round(result.timeSpentSeconds / result.attemptedCount)
    : 0;

  // AIR 1 Feedback Generator
  const getAir1Message = () => {
    if (result.percentage >= 85) {
      return {
        badge: 'All India Rank 1 Potential',
        color: 'text-emerald-700 bg-emerald-100 border-emerald-300',
        message: 'Exceptional mastery across veterinary and animal science domains. Your negative marking control is outstanding!'
      };
    } else if (result.percentage >= 70) {
      return {
        badge: 'Top 10 Rank Contender',
        color: 'text-blue-700 bg-blue-100 border-blue-300',
        message: 'Very solid preparation! Focus on reviewing the incorrect questions below to eliminate negative marking penalty.'
      };
    } else {
      return {
        badge: 'Concept Consolidation Phase',
        color: 'text-amber-700 bg-amber-100 border-amber-300',
        message: 'Good attempt. Focus your revision on 1st & 2nd year textbook chapters in the subjects flagged with lower accuracy below.'
      };
    }
  };

  const feedback = getAir1Message();
  const negativeMarkPenalty = result.incorrectCount * result.config.negativeMarks;

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Top Navigation */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBackToDashboard}
          className="flex items-center space-x-1 text-xs font-semibold text-slate-600 hover:text-slate-900 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Dashboard</span>
        </button>

        <span className="text-xs text-slate-400 font-medium">
          Exam Date: {result.dateString}
        </span>
      </div>

      {/* Main Scorecard Banner */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm relative overflow-hidden">
        <div className="flex flex-col lg:flex-row items-center justify-between gap-6">
          {/* Left: Score Overview */}
          <div className="text-center lg:text-left space-y-2">
            <div className="flex flex-wrap items-center justify-center lg:justify-start gap-2">
              <span className={`text-xs font-extrabold px-3 py-1 rounded-full border ${feedback.color}`}>
                {feedback.badge}
              </span>
              <span className="text-xs font-bold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">
                {result.title}
              </span>
            </div>

            <div className="flex items-baseline justify-center lg:justify-start space-x-3 pt-2">
              <span className="text-4xl sm:text-6xl font-black text-slate-900 tracking-tight">
                {result.totalScore}
              </span>
              <span className="text-xl sm:text-2xl font-bold text-slate-400">
                / {result.maxPossibleScore} Marks
              </span>
              <span className="text-lg sm:text-xl font-extrabold text-emerald-600 bg-emerald-50 px-2.5 py-0.5 rounded-lg border border-emerald-200 ml-2">
                {result.percentage}%
              </span>
            </div>

            <p className="text-xs sm:text-sm text-slate-600 max-w-xl leading-relaxed pt-1">
              {feedback.message}
            </p>
          </div>

          {/* Right: Quick Action Buttons */}
          <div className="flex flex-col sm:flex-row gap-3 shrink-0">
            <button
              onClick={() => setShowReviewModal(true)}
              className="px-5 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs sm:text-sm shadow-md flex items-center justify-center space-x-2 transition-transform transform active:scale-98"
            >
              <BookOpen className="w-4 h-4" />
              <span>Review All Solutions</span>
            </button>

            <button
              onClick={onRetakeTest}
              className="px-5 py-3 rounded-xl bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-bold text-xs sm:text-sm shadow-2xs flex items-center justify-center space-x-2 transition-colors"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Retake Test</span>
            </button>
          </div>
        </div>

        {/* 5 Performance Stat Cards */}
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 sm:gap-4 mt-8 pt-6 border-t border-slate-100 text-center">
          <div className="bg-slate-50 p-3 rounded-xl border border-slate-200">
            <p className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">Attempted</p>
            <p className="text-lg sm:text-xl font-black text-slate-800 mt-1">
              {result.attemptedCount} / {result.totalQuestions}
            </p>
          </div>

          <div className="bg-emerald-50/70 p-3 rounded-xl border border-emerald-200">
            <p className="text-[11px] font-bold text-emerald-700 uppercase tracking-wider">Correct</p>
            <p className="text-lg sm:text-xl font-black text-emerald-800 mt-1">
              {result.correctCount} <span className="text-xs font-medium text-emerald-600">(+{result.correctCount * result.config.positiveMarks})</span>
            </p>
          </div>

          <div className="bg-red-50/70 p-3 rounded-xl border border-red-200">
            <p className="text-[11px] font-bold text-red-700 uppercase tracking-wider">Incorrect</p>
            <p className="text-lg sm:text-xl font-black text-red-800 mt-1">
              {result.incorrectCount} <span className="text-xs font-medium text-red-600">(-{negativeMarkPenalty})</span>
            </p>
          </div>

          <div className="bg-blue-50/70 p-3 rounded-xl border border-blue-200">
            <p className="text-[11px] font-bold text-blue-700 uppercase tracking-wider">Accuracy</p>
            <p className="text-lg sm:text-xl font-black text-blue-800 mt-1">
              {result.accuracy}%
            </p>
          </div>

          <div className="bg-amber-50/70 p-3 rounded-xl border border-amber-200 col-span-2 sm:col-span-1">
            <p className="text-[11px] font-bold text-amber-700 uppercase tracking-wider">Time Taken</p>
            <p className="text-lg sm:text-xl font-black text-amber-900 mt-1">
              {formatSeconds(result.timeSpentSeconds)}
            </p>
          </div>
        </div>
      </div>

      {/* Two Domain Comparison Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Veterinary Science Domain */}
        {result.domainPerformance.veterinary_science && (
          <div className="bg-white rounded-xl border border-blue-200 p-5 shadow-2xs space-y-4">
            <div className="flex items-center justify-between border-b border-blue-100 pb-3">
              <div>
                <span className="text-xs font-extrabold uppercase tracking-wider text-blue-800">
                  Domain 1
                </span>
                <h4 className="font-extrabold text-base text-slate-900">Veterinary Science Subjects</h4>
              </div>
              <span className="text-sm font-black text-blue-700 bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
                {result.domainPerformance.veterinary_science.score} / {result.domainPerformance.veterinary_science.maxScore}
              </span>
            </div>

            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="bg-slate-50 p-2 rounded">
                <span className="text-slate-500 block">Questions</span>
                <span className="font-bold text-slate-800 font-mono">
                  {result.domainPerformance.veterinary_science.totalQuestions}
                </span>
              </div>
              <div className="bg-emerald-50 p-2 rounded">
                <span className="text-emerald-700 block">Correct</span>
                <span className="font-bold text-emerald-800 font-mono">
                  {result.domainPerformance.veterinary_science.correct}
                </span>
              </div>
              <div className="bg-blue-50 p-2 rounded">
                <span className="text-blue-700 block">Accuracy</span>
                <span className="font-bold text-blue-800 font-mono">
                  {result.domainPerformance.veterinary_science.accuracy}%
                </span>
              </div>
            </div>
          </div>
        )}

        {/* Animal Science Domain */}
        {result.domainPerformance.animal_science && (
          <div className="bg-white rounded-xl border border-teal-200 p-5 shadow-2xs space-y-4">
            <div className="flex items-center justify-between border-b border-teal-100 pb-3">
              <div>
                <span className="text-xs font-extrabold uppercase tracking-wider text-teal-800">
                  Domain 2
                </span>
                <h4 className="font-extrabold text-base text-slate-900">Animal Science Subjects</h4>
              </div>
              <span className="text-sm font-black text-teal-700 bg-teal-50 px-3 py-1 rounded-full border border-teal-200">
                {result.domainPerformance.animal_science.score} / {result.domainPerformance.animal_science.maxScore}
              </span>
            </div>

            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="bg-slate-50 p-2 rounded">
                <span className="text-slate-500 block">Questions</span>
                <span className="font-bold text-slate-800 font-mono">
                  {result.domainPerformance.animal_science.totalQuestions}
                </span>
              </div>
              <div className="bg-emerald-50 p-2 rounded">
                <span className="text-emerald-700 block">Correct</span>
                <span className="font-bold text-emerald-800 font-mono">
                  {result.domainPerformance.animal_science.correct}
                </span>
              </div>
              <div className="bg-teal-50 p-2 rounded">
                <span className="text-teal-700 block">Accuracy</span>
                <span className="font-bold text-teal-800 font-mono">
                  {result.domainPerformance.animal_science.accuracy}%
                </span>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Subject-wise Diagnostic Breakdown Table */}
      <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h4 className="font-extrabold text-slate-900 text-base flex items-center space-x-2">
              <BarChart2 className="w-5 h-5 text-emerald-600" />
              <span>Subject-Wise Precision Breakdown</span>
            </h4>
            <p className="text-xs text-slate-500">
              Pinpoint which 1st &amp; 2nd year subjects need more revision.
            </p>
          </div>
        </div>

        <div className="overflow-x-auto border border-slate-200 rounded-lg">
          <table className="w-full text-xs text-left border-collapse">
            <thead>
              <tr className="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                <th className="py-2.5 px-4">Subject</th>
                <th className="py-2.5 px-3">Domain</th>
                <th className="py-2.5 px-3 text-center">Total Qs</th>
                <th className="py-2.5 px-3 text-center">Attempted</th>
                <th className="py-2.5 px-3 text-center text-emerald-700">Correct</th>
                <th className="py-2.5 px-3 text-center text-red-600">Incorrect</th>
                <th className="py-2.5 px-3 text-center">Score</th>
                <th className="py-2.5 px-3 text-center">Accuracy</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 font-medium">
              {Object.values(result.subjectPerformance).map(sub => {
                const isWeak = sub.accuracy < 60 && sub.attempted > 0;

                return (
                  <tr key={sub.subjectId} className="hover:bg-slate-50">
                    <td className="py-2.5 px-4 font-semibold text-slate-900">
                      {sub.subjectName}
                    </td>
                    <td className="py-2.5 px-3">
                      <span className={`px-2 py-0.5 rounded text-[10px] font-semibold ${
                        sub.domain === 'veterinary_science' ? 'bg-blue-100 text-blue-800' : 'bg-teal-100 text-teal-800'
                      }`}>
                        {sub.domain === 'veterinary_science' ? 'Vet Sci' : 'Animal Sci'}
                      </span>
                    </td>
                    <td className="py-2.5 px-3 text-center font-mono">{sub.totalQuestions}</td>
                    <td className="py-2.5 px-3 text-center font-mono">{sub.attempted}</td>
                    <td className="py-2.5 px-3 text-center font-mono text-emerald-700 font-bold">{sub.correct}</td>
                    <td className="py-2.5 px-3 text-center font-mono text-red-600 font-bold">{sub.incorrect}</td>
                    <td className="py-2.5 px-3 text-center font-mono font-bold text-slate-800">
                      {sub.score} / {sub.maxScore}
                    </td>
                    <td className="py-2.5 px-3 text-center">
                      <span className={`px-2 py-0.5 rounded font-bold ${
                        isWeak ? 'bg-red-100 text-red-800' : 'bg-emerald-100 text-emerald-800'
                      }`}>
                        {sub.accuracy}%
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Review Modal */}
      {showReviewModal && (
        <QuestionReviewModal
          result={result}
          onClose={() => setShowReviewModal(false)}
        />
      )}
    </div>
  );
};
