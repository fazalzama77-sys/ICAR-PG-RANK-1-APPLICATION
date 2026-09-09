import React from 'react';
import { AlertTriangle, CheckCircle2 } from 'lucide-react';
import { Question, UserResponseState, QuestionState } from '../../types';

interface CBTSubmitModalProps {
  questions: Question[];
  userResponses: Record<string, UserResponseState>;
  onConfirmSubmit: () => void;
  onCancel: () => void;
  isTimeExpired?: boolean;
}

export const CBTSubmitModal: React.FC<CBTSubmitModalProps> = ({
  questions,
  userResponses,
  onConfirmSubmit,
  onCancel,
  isTimeExpired = false
}) => {
  // Aggregate stats by section
  const computeSectionStats = (domain?: 'veterinary_science' | 'animal_science') => {
    const subset = domain ? questions.filter(q => q.domain === domain) : questions;

    const stats = {
      total: subset.length,
      answered: 0,
      notAnswered: 0,
      markedForReview: 0,
      answeredAndMarked: 0,
      notVisited: 0
    };

    subset.forEach(q => {
      const resp = userResponses[q.id];
      const state: QuestionState = resp ? resp.state : 'NOT_VISITED';

      switch (state) {
        case 'ANSWERED':
          stats.answered++;
          break;
        case 'NOT_ANSWERED':
          stats.notAnswered++;
          break;
        case 'MARKED_FOR_REVIEW':
          stats.markedForReview++;
          break;
        case 'ANSWERED_AND_MARKED_FOR_REVIEW':
          stats.answeredAndMarked++;
          break;
        case 'NOT_VISITED':
        default:
          stats.notVisited++;
          break;
      }
    });

    return stats;
  };

  const vetStats = computeSectionStats('veterinary_science');
  const animalStats = computeSectionStats('animal_science');
  const totalStats = computeSectionStats();

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/75 backdrop-blur-xs p-4 select-none">
      <div className="bg-white rounded-lg shadow-2xl max-w-2xl w-full overflow-hidden border border-slate-300">
        
        {/* Modal Header */}
        <div className="bg-[#2b547e] text-white px-6 py-4 flex items-center justify-between">
          <div className="flex items-center space-x-2.5">
            {isTimeExpired ? (
              <AlertTriangle className="w-5 h-5 text-amber-300 animate-pulse" />
            ) : (
              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
            )}
            <h3 className="font-bold text-base tracking-wide">
              {isTimeExpired ? 'Time Expired - Final Exam Submission' : 'NTA Examination Summary'}
            </h3>
          </div>
        </div>

        {/* Modal Body */}
        <div className="p-6">
          {isTimeExpired ? (
            <div className="mb-4 bg-red-50 border-l-4 border-red-500 p-3 text-red-800 text-xs font-semibold">
              The allotted exam duration has ended. Your responses have been saved and are ready for evaluation.
            </div>
          ) : (
            <p className="text-xs sm:text-sm text-slate-600 mb-4 leading-relaxed">
              Please review your attempt status below across both domains before submitting your final examination.
            </p>
          )}

          {/* Official NTA Summary Table */}
          <div className="overflow-x-auto border border-slate-300 rounded mb-5">
            <table className="w-full text-xs text-left border-collapse">
              <thead>
                <tr className="bg-[#e9eef4] text-slate-800 font-bold border-b border-slate-300 text-center">
                  <th className="py-2.5 px-3 text-left">Section Name</th>
                  <th className="py-2.5 px-2">No. of Qs</th>
                  <th className="py-2.5 px-2 text-emerald-700">Answered</th>
                  <th className="py-2.5 px-2 text-red-600">Not Answered</th>
                  <th className="py-2.5 px-2 text-purple-700">Marked Review</th>
                  <th className="py-2.5 px-2 text-purple-800">Ans & Marked*</th>
                  <th className="py-2.5 px-2 text-slate-500">Not Visited</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 text-center font-medium">
                {/* Veterinary Science Row */}
                <tr className="hover:bg-slate-50">
                  <td className="py-2 px-3 text-left font-semibold text-slate-800">Veterinary Science</td>
                  <td className="py-2 px-2 font-mono">{vetStats.total}</td>
                  <td className="py-2 px-2 text-emerald-700 font-bold">{vetStats.answered}</td>
                  <td className="py-2 px-2 text-red-600 font-semibold">{vetStats.notAnswered}</td>
                  <td className="py-2 px-2 text-purple-700">{vetStats.markedForReview}</td>
                  <td className="py-2 px-2 text-purple-800 font-bold">{vetStats.answeredAndMarked}</td>
                  <td className="py-2 px-2 text-slate-500">{vetStats.notVisited}</td>
                </tr>

                {/* Animal Science Row */}
                <tr className="hover:bg-slate-50">
                  <td className="py-2 px-3 text-left font-semibold text-slate-800">Animal Science</td>
                  <td className="py-2 px-2 font-mono">{animalStats.total}</td>
                  <td className="py-2 px-2 text-emerald-700 font-bold">{animalStats.answered}</td>
                  <td className="py-2 px-2 text-red-600 font-semibold">{animalStats.notAnswered}</td>
                  <td className="py-2 px-2 text-purple-700">{animalStats.markedForReview}</td>
                  <td className="py-2 px-2 text-purple-800 font-bold">{animalStats.answeredAndMarked}</td>
                  <td className="py-2 px-2 text-slate-500">{animalStats.notVisited}</td>
                </tr>

                {/* Total Row */}
                <tr className="bg-slate-100 font-bold text-slate-900 border-t-2 border-slate-300">
                  <td className="py-2.5 px-3 text-left">Total</td>
                  <td className="py-2.5 px-2 font-mono">{totalStats.total}</td>
                  <td className="py-2.5 px-2 text-emerald-700">{totalStats.answered}</td>
                  <td className="py-2.5 px-2 text-red-600">{totalStats.notAnswered}</td>
                  <td className="py-2.5 px-2 text-purple-700">{totalStats.markedForReview}</td>
                  <td className="py-2.5 px-2 text-purple-800">{totalStats.answeredAndMarked}</td>
                  <td className="py-2.5 px-2 text-slate-600">{totalStats.notVisited}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p className="text-[11px] text-slate-500 italic mb-5 leading-tight">
            * Note: Questions flagged as &quot;Answered &amp; Marked for Review&quot; will be evaluated and scored as per NTA ICAR guidelines.
          </p>

          {!isTimeExpired && (
            <div className="text-xs text-slate-800 font-semibold bg-amber-50 border border-amber-200 rounded p-3 mb-5">
              Are you sure you want to submit the examination for final scoring? You will not be able to modify your answers afterwards.
            </div>
          )}

          {/* Action Buttons */}
          <div className="flex items-center justify-end space-x-3 pt-2">
            {!isTimeExpired && (
              <button
                type="button"
                onClick={onCancel}
                className="px-4 py-2 border border-slate-300 text-slate-700 hover:bg-slate-100 rounded text-xs font-semibold uppercase tracking-wider transition-colors"
              >
                No, Return to Test
              </button>
            )}

            <button
              type="button"
              onClick={onConfirmSubmit}
              className="px-5 py-2 bg-[#16a34a] hover:bg-[#15803d] text-white rounded text-xs font-bold uppercase tracking-wider shadow-sm transition-all"
            >
              Yes, Submit Final Exam
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
