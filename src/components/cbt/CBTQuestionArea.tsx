import React, { useState } from 'react';
import { Question } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';

interface CBTQuestionAreaProps {
  questionNumber: number;
  totalQuestions: number;
  question: Question;
  selectedOptionIndex: number | null;
  onSelectOption: (optionIndex: number) => void;
  positiveMarks: number;
  negativeMarks: number;
}

export const CBTQuestionArea: React.FC<CBTQuestionAreaProps> = ({
  questionNumber,
  totalQuestions,
  question,
  selectedOptionIndex,
  onSelectOption,
  positiveMarks,
  negativeMarks
}) => {
  // Font size multiplier for accessibility (standard NTA CBT feature)
  const [fontSizeLevel, setFontSizeLevel] = useState<'normal' | 'large' | 'xlarge'>('normal');

  const subject = SUBJECT_LIST.find(s => s.id === question.subjectId);

  const getFontSizeClass = () => {
    switch (fontSizeLevel) {
      case 'large':
        return 'text-base sm:text-lg';
      case 'xlarge':
        return 'text-lg sm:text-xl';
      default:
        return 'text-sm sm:text-base';
    }
  };

  return (
    <div className="flex-1 flex flex-col bg-white border border-slate-300 rounded-sm shadow-xs overflow-hidden h-full">
      {/* Top Question Info Bar */}
      <div className="bg-[#e9eef4] px-4 py-2 border-b border-slate-300 flex flex-wrap items-center justify-between gap-2 select-none">
        <div className="flex items-center space-x-3">
          <span className="font-bold text-slate-800 text-sm sm:text-base">
            Question No. {questionNumber} of {totalQuestions}
          </span>
          {subject && (
            <span className="bg-slate-200 text-slate-700 text-xs px-2 py-0.5 rounded font-medium border border-slate-300">
              {subject.name} ({subject.code})
            </span>
          )}
          {question.topic && (
            <span className="hidden sm:inline bg-blue-50 text-blue-800 text-xs px-2 py-0.5 rounded font-medium border border-blue-200">
              {question.topic}
            </span>
          )}
        </div>

        {/* Marking Scheme & Zoom Controls */}
        <div className="flex items-center space-x-4">
          <div className="text-xs text-slate-700 bg-white px-2.5 py-1 rounded border border-slate-300 shadow-2xs font-semibold">
            Marking: <span className="text-emerald-700 font-bold">+{positiveMarks}</span> &bull; <span className="text-red-600 font-bold">-{negativeMarks}</span>
          </div>

          {/* Text Resize Controls (Official NTA CBT Feature) */}
          <div className="flex items-center space-x-1 border border-slate-300 rounded bg-white px-1 py-0.5 text-xs">
            <button
              onClick={() => setFontSizeLevel('normal')}
              className={`px-1.5 py-0.5 rounded font-medium ${fontSizeLevel === 'normal' ? 'bg-slate-200 text-slate-800 font-bold' : 'text-slate-500 hover:text-slate-800'}`}
              title="Normal Font"
            >
              A
            </button>
            <button
              onClick={() => setFontSizeLevel('large')}
              className={`px-1.5 py-0.5 rounded font-medium ${fontSizeLevel === 'large' ? 'bg-slate-200 text-slate-800 font-bold' : 'text-slate-500 hover:text-slate-800'}`}
              title="Large Font"
            >
              A+
            </button>
            <button
              onClick={() => setFontSizeLevel('xlarge')}
              className={`px-1.5 py-0.5 rounded font-medium ${fontSizeLevel === 'xlarge' ? 'bg-slate-200 text-slate-800 font-bold' : 'text-slate-500 hover:text-slate-800'}`}
              title="Extra Large Font"
            >
              A++
            </button>
          </div>
        </div>
      </div>

      {/* Main Question Scrollable Body */}
      <div className="flex-1 p-5 sm:p-7 overflow-y-auto space-y-6">
        {/* Question Statement */}
        <div className={`text-slate-900 leading-relaxed font-normal whitespace-pre-wrap ${getFontSizeClass()}`}>
          {question.questionText}
        </div>

        <div className="border-t border-slate-200 pt-4">
          <div className="text-xs uppercase font-bold text-slate-500 tracking-wider mb-3">
            Select one of the following options:
          </div>

          {/* 4 Radio Option Cards */}
          <div className="space-y-3">
            {question.options.map((optionText, idx) => {
              const isSelected = selectedOptionIndex === idx;
              const optionLabel = ['A', 'B', 'C', 'D'][idx] || `(${idx + 1})`;

              return (
                <div
                  key={idx}
                  onClick={() => onSelectOption(idx)}
                  className={`flex items-start p-3.5 rounded border transition-all cursor-pointer select-none ${
                    isSelected
                      ? 'bg-blue-50/80 border-blue-600 ring-1 ring-blue-500 shadow-2xs'
                      : 'bg-slate-50/60 border-slate-300 hover:bg-slate-100 hover:border-slate-400'
                  }`}
                >
                  <div className="flex items-center h-5 mr-3 mt-0.5">
                    <input
                      type="radio"
                      name={`question_option_${question.id}`}
                      checked={isSelected}
                      onChange={() => onSelectOption(idx)}
                      className="w-4 h-4 text-blue-600 border-slate-400 focus:ring-blue-500 cursor-pointer"
                    />
                  </div>
                  <div className="flex-1 flex items-start">
                    <span className={`inline-block font-bold mr-2.5 text-xs px-2 py-0.5 rounded ${
                      isSelected ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-700'
                    }`}>
                      {optionLabel}
                    </span>
                    <span className={`leading-snug text-slate-800 ${getFontSizeClass()}`}>
                      {optionText}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};
