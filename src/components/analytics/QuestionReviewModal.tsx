import React, { useState } from 'react';
import { X, CheckCircle2, XCircle, Clock, BookOpen, Filter } from 'lucide-react';
import { TestResult, Domain } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';

interface QuestionReviewModalProps {
  result: TestResult;
  onClose: () => void;
}

export const QuestionReviewModal: React.FC<QuestionReviewModalProps> = ({
  result,
  onClose
}) => {
  const [filter, setFilter] = useState<'all' | 'incorrect' | 'correct' | 'unattempted'>('all');
  const [selectedDomain, setSelectedDomain] = useState<string>('all');

  const filteredRecords = result.questionRecords.filter(rec => {
    if (selectedDomain !== 'all' && rec.question.domain !== selectedDomain) return false;

    const isAttempted = rec.response.selectedOptionIndex !== null &&
      (rec.response.state === 'ANSWERED' || rec.response.state === 'ANSWERED_AND_MARKED_FOR_REVIEW');

    if (filter === 'incorrect') {
      return isAttempted && !rec.isCorrect;
    }
    if (filter === 'correct') {
      return isAttempted && rec.isCorrect;
    }
    if (filter === 'unattempted') {
      return !isAttempted;
    }
    return true;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/70 backdrop-blur-xs p-3 sm:p-6 overflow-y-auto">
      <div className="bg-white rounded-xl shadow-2xl max-w-4xl w-full max-h-[92vh] flex flex-col border border-slate-300">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
          <div>
            <h3 className="font-extrabold text-slate-900 text-base sm:text-lg flex items-center space-x-2">
              <BookOpen className="w-5 h-5 text-emerald-600" />
              <span>Question-by-Question Solution &amp; Review</span>
            </h3>
            <p className="text-xs text-slate-500">
              {result.title} &bull; Score: <span className="font-bold text-emerald-700">{result.totalScore}/{result.maxPossibleScore}</span>
            </p>
          </div>

          <button
            onClick={onClose}
            className="p-1 rounded text-slate-400 hover:text-slate-700 hover:bg-slate-200 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Filter Bar */}
        <div className="p-4 bg-slate-100/70 border-b border-slate-200 flex flex-wrap items-center justify-between gap-3 text-xs">
          <div className="flex flex-wrap items-center gap-2">
            <button
              onClick={() => setFilter('all')}
              className={`px-3 py-1.5 rounded-md font-semibold transition-colors ${
                filter === 'all'
                  ? 'bg-slate-900 text-white'
                  : 'bg-white text-slate-700 hover:bg-slate-200 border border-slate-300'
              }`}
            >
              All Questions ({result.questionRecords.length})
            </button>

            <button
              onClick={() => setFilter('incorrect')}
              className={`px-3 py-1.5 rounded-md font-semibold transition-colors ${
                filter === 'incorrect'
                  ? 'bg-red-600 text-white'
                  : 'bg-white text-red-700 hover:bg-red-50 border border-red-200'
              }`}
            >
              Incorrect / Negative ({result.incorrectCount})
            </button>

            <button
              onClick={() => setFilter('correct')}
              className={`px-3 py-1.5 rounded-md font-semibold transition-colors ${
                filter === 'correct'
                  ? 'bg-emerald-600 text-white'
                  : 'bg-white text-emerald-700 hover:bg-emerald-50 border border-emerald-200'
              }`}
            >
              Correct ({result.correctCount})
            </button>

            <button
              onClick={() => setFilter('unattempted')}
              className={`px-3 py-1.5 rounded-md font-semibold transition-colors ${
                filter === 'unattempted'
                  ? 'bg-slate-600 text-white'
                  : 'bg-white text-slate-600 hover:bg-slate-200 border border-slate-300'
              }`}
            >
              Unattempted ({result.unattemptedCount})
            </button>
          </div>

          {/* Domain Filter */}
          <div className="flex items-center space-x-2">
            <Filter className="w-3.5 h-3.5 text-slate-500" />
            <select
              value={selectedDomain}
              onChange={e => setSelectedDomain(e.target.value)}
              className="text-xs bg-white border border-slate-300 rounded px-2.5 py-1 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden font-medium"
            >
              <option value="all">Both Domains</option>
              <option value="veterinary_science">Veterinary Science</option>
              <option value="animal_science">Animal Science</option>
            </select>
          </div>
        </div>

        {/* Question Solutions List */}
        <div className="flex-1 overflow-y-auto p-5 sm:p-6 space-y-6">
          {filteredRecords.length === 0 ? (
            <div className="text-center py-12 text-slate-500 text-xs">
              No questions found under this filter.
            </div>
          ) : (
            filteredRecords.map((record, index) => {
              const q = record.question;
              const resp = record.response;
              const subject = SUBJECT_LIST.find(s => s.id === q.subjectId);
              const isAttempted = resp.selectedOptionIndex !== null &&
                (resp.state === 'ANSWERED' || resp.state === 'ANSWERED_AND_MARKED_FOR_REVIEW');

              return (
                <div
                  key={q.id}
                  className={`p-5 rounded-xl border transition-all ${
                    !isAttempted
                      ? 'bg-slate-50/70 border-slate-200'
                      : record.isCorrect
                      ? 'bg-emerald-50/40 border-emerald-300'
                      : 'bg-red-50/40 border-red-300'
                  }`}
                >
                  {/* Top Bar: Question Number & Badges */}
                  <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <div className="flex flex-wrap items-center gap-2 text-xs">
                      <span className="font-mono font-bold bg-white text-slate-800 px-2.5 py-0.5 rounded border border-slate-300 shadow-2xs">
                        Q.{index + 1}
                      </span>
                      <span className={`font-semibold px-2 py-0.5 rounded ${
                        q.domain === 'veterinary_science' ? 'bg-blue-100 text-blue-800' : 'bg-teal-100 text-teal-800'
                      }`}>
                        {q.domain === 'veterinary_science' ? 'Veterinary Science' : 'Animal Science'}
                      </span>
                      {subject && (
                        <span className="bg-slate-200 text-slate-700 px-2 py-0.5 rounded font-medium">
                          {subject.name} ({subject.code})
                        </span>
                      )}
                      {q.topic && (
                        <span className="bg-amber-100 text-amber-900 px-2 py-0.5 rounded font-medium">
                          {q.topic}
                        </span>
                      )}
                    </div>

                    <div className="flex items-center space-x-3 text-xs font-semibold">
                      <span className="flex items-center space-x-1 text-slate-500 font-mono">
                        <Clock className="w-3.5 h-3.5" />
                        <span>{resp.timeSpentSeconds}s</span>
                      </span>

                      {/* Marks awarded badge */}
                      <span className={`px-2.5 py-0.5 rounded-full font-bold ${
                        !isAttempted
                          ? 'bg-slate-200 text-slate-700'
                          : record.isCorrect
                          ? 'bg-emerald-600 text-white'
                          : 'bg-red-600 text-white'
                      }`}>
                        {record.scoreAwarded > 0 ? `+${record.scoreAwarded}` : record.scoreAwarded} Marks
                      </span>
                    </div>
                  </div>

                  {/* Question Stem */}
                  <p className="text-sm font-semibold text-slate-900 mb-4 leading-relaxed whitespace-pre-wrap">
                    {q.questionText}
                  </p>

                  {/* 4 Options with User Selection and Correct Highlight */}
                  <div className="space-y-2 mb-4">
                    {q.options.map((optionText, optIdx) => {
                      const isCorrectAnswer = optIdx === q.correctOptionIndex;
                      const isUserChoice = optIdx === resp.selectedOptionIndex;
                      const letter = ['A', 'B', 'C', 'D'][optIdx];

                      let optionStyle = 'bg-white border-slate-200 text-slate-700';

                      if (isCorrectAnswer) {
                        optionStyle = 'bg-emerald-100/80 border-emerald-500 text-emerald-950 font-bold ring-1 ring-emerald-400';
                      } else if (isUserChoice && !record.isCorrect) {
                        optionStyle = 'bg-red-100/80 border-red-500 text-red-950 font-bold ring-1 ring-red-400';
                      }

                      return (
                        <div
                          key={optIdx}
                          className={`p-3 rounded-lg border text-xs flex items-start justify-between ${optionStyle}`}
                        >
                          <div className="flex items-start space-x-2">
                            <span className={`font-mono font-bold px-1.5 py-0.5 rounded text-[11px] ${
                              isCorrectAnswer ? 'bg-emerald-700 text-white' : isUserChoice ? 'bg-red-600 text-white' : 'bg-slate-200 text-slate-700'
                            }`}>
                              {letter}
                            </span>
                            <span className="leading-snug pt-0.5">{optionText}</span>
                          </div>

                          <div className="shrink-0 ml-3 flex items-center space-x-1.5 text-[11px]">
                            {isCorrectAnswer && (
                              <span className="text-emerald-800 font-bold flex items-center space-x-1">
                                <CheckCircle2 className="w-3.5 h-3.5" />
                                <span>Correct Answer</span>
                              </span>
                            )}
                            {isUserChoice && !isCorrectAnswer && (
                              <span className="text-red-700 font-bold flex items-center space-x-1">
                                <XCircle className="w-3.5 h-3.5" />
                                <span>Your Answer (Incorrect)</span>
                              </span>
                            )}
                            {isUserChoice && isCorrectAnswer && (
                              <span className="text-emerald-800 font-bold">
                                (Your Answer)
                              </span>
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  {/* High-Yield Note / Detailed Explanation */}
                  {q.explanation && (
                    <div className="p-3.5 bg-amber-50/80 border border-amber-200 rounded-lg text-xs leading-relaxed text-slate-800">
                      <span className="font-bold text-amber-900 block mb-1">
                        High-Yield Explanation &amp; Core Concept:
                      </span>
                      {q.explanation}
                    </div>
                  )}
                </div>
              );
            })
          )}
        </div>

        {/* Modal Footer */}
        <div className="px-6 py-3 border-t border-slate-200 bg-slate-50 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 bg-slate-800 hover:bg-slate-900 text-white text-xs font-bold rounded-lg transition-colors"
          >
            Close Review
          </button>
        </div>
      </div>
    </div>
  );
};
