import React from 'react';
import { ChevronLeft, ChevronRight, Check, Bookmark, RotateCcw, HelpCircle } from 'lucide-react';

interface CBTBottomActionsProps {
  onSaveAndNext: () => void;
  onSaveAndMarkForReview: () => void;
  onClearResponse: () => void;
  onMarkForReviewAndNext: () => void;
  onPrevious: () => void;
  onNext: () => void;
  isFirstQuestion: boolean;
  isLastQuestion: boolean;
  hasSelectedOption: boolean;
}

export const CBTBottomActions: React.FC<CBTBottomActionsProps> = ({
  onSaveAndNext,
  onSaveAndMarkForReview,
  onClearResponse,
  onMarkForReviewAndNext,
  onPrevious,
  onNext,
  isFirstQuestion,
  isLastQuestion,
  hasSelectedOption
}) => {
  return (
    <div className="bg-[#f8fafc] border-t border-slate-300 p-3 sm:px-6 flex flex-wrap items-center justify-between gap-2.5 select-none shadow-xs">
      {/* Left side actions (Action Buttons) */}
      <div className="flex flex-wrap items-center gap-2">
        {/* 1. Save & Next */}
        <button
          onClick={onSaveAndNext}
          className="bg-[#2563eb] hover:bg-[#1d4ed8] text-white px-4 py-2 rounded text-xs sm:text-sm font-semibold flex items-center space-x-1.5 shadow-xs transition-colors"
          title="Save your answer and proceed to the next question"
        >
          <Check className="w-4 h-4" />
          <span>Save & Next</span>
        </button>

        {/* 2. Save & Mark for Review */}
        <button
          onClick={onSaveAndMarkForReview}
          disabled={!hasSelectedOption}
          className={`px-3.5 py-2 rounded text-xs sm:text-sm font-semibold flex items-center space-x-1.5 shadow-xs transition-colors ${
            hasSelectedOption
              ? 'bg-[#d97706] hover:bg-[#b45309] text-white'
              : 'bg-slate-200 text-slate-400 cursor-not-allowed border border-slate-300'
          }`}
          title="Save answer and mark for review (Evaluated in NTA)"
        >
          <Bookmark className="w-4 h-4" />
          <span>Save & Mark for Review</span>
        </button>

        {/* 3. Clear Response */}
        <button
          onClick={onClearResponse}
          disabled={!hasSelectedOption}
          className={`px-3.5 py-2 rounded text-xs sm:text-sm font-semibold flex items-center space-x-1.5 border transition-colors ${
            hasSelectedOption
              ? 'bg-white hover:bg-slate-100 text-slate-700 border-slate-300 shadow-2xs'
              : 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed'
          }`}
          title="Clear currently selected answer choice"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>Clear Response</span>
        </button>

        {/* 4. Mark for Review & Next */}
        <button
          onClick={onMarkForReviewAndNext}
          className="bg-[#7c3aed] hover:bg-[#6d28d9] text-white px-3.5 py-2 rounded text-xs sm:text-sm font-semibold flex items-center space-x-1.5 shadow-xs transition-colors"
          title="Mark for review without answering and move to next question"
        >
          <HelpCircle className="w-4 h-4" />
          <span>Mark for Review & Next</span>
        </button>
      </div>

      {/* Right side navigation: Previous / Next */}
      <div className="flex items-center space-x-2 ml-auto">
        <button
          onClick={onPrevious}
          disabled={isFirstQuestion}
          className={`px-3.5 py-2 rounded text-xs sm:text-sm font-semibold flex items-center space-x-1 border transition-colors ${
            isFirstQuestion
              ? 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed'
              : 'bg-white hover:bg-slate-100 text-slate-800 border-slate-300 shadow-2xs'
          }`}
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Previous</span>
        </button>

        <button
          onClick={onNext}
          disabled={isLastQuestion}
          className={`px-3.5 py-2 rounded text-xs sm:text-sm font-semibold flex items-center space-x-1 border transition-colors ${
            isLastQuestion
              ? 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed'
              : 'bg-white hover:bg-slate-100 text-slate-800 border-slate-300 shadow-2xs'
          }`}
        >
          <span>Next</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
