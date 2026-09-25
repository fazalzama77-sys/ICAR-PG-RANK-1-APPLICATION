import React from 'react';
import { ChevronLeft, ChevronRight, Check, Bookmark, RotateCcw, HelpCircle, LayoutGrid } from 'lucide-react';

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
  onOpenPalette?: () => void;
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
  hasSelectedOption,
  onOpenPalette
}) => {
  return (
    <div className="bg-[#f8fafc] border-t border-slate-300 p-2 sm:p-3 sm:px-6 select-none shadow-xs pb-[max(0.6rem,env(safe-area-inset-bottom,0px))]">
      {/* Mobile Layout (< lg) */}
      <div className="flex flex-col gap-2 lg:hidden">
        {/* Row 1: Secondary NTA Exam Actions */}
        <div className="grid grid-cols-3 gap-1.5">
          {/* Save & Mark for Review */}
          <button
            onClick={onSaveAndMarkForReview}
            disabled={!hasSelectedOption}
            className={`py-2 px-1.5 rounded text-[11px] font-bold flex items-center justify-center space-x-1 shadow-xs transition-colors truncate touch-manipulation active:scale-98 ${
              hasSelectedOption
                ? 'bg-[#d97706] hover:bg-[#b45309] text-white'
                : 'bg-slate-200 text-slate-400 cursor-not-allowed border border-slate-300'
            }`}
            title="Save answer and mark for review (Evaluated in NTA)"
          >
            <Bookmark className="w-3.5 h-3.5 shrink-0" />
            <span className="truncate">Save & Mark</span>
          </button>

          {/* Mark for Review & Next */}
          <button
            onClick={onMarkForReviewAndNext}
            className="bg-[#7c3aed] hover:bg-[#6d28d9] text-white py-2 px-1.5 rounded text-[11px] font-bold flex items-center justify-center space-x-1 shadow-xs transition-colors truncate touch-manipulation active:scale-98"
            title="Mark for review without answering and move to next question"
          >
            <HelpCircle className="w-3.5 h-3.5 shrink-0" />
            <span className="truncate">Mark & Next</span>
          </button>

          {/* Clear Response */}
          <button
            onClick={onClearResponse}
            disabled={!hasSelectedOption}
            className={`py-2 px-1.5 rounded text-[11px] font-bold flex items-center justify-center space-x-1 border transition-colors truncate touch-manipulation active:scale-98 ${
              hasSelectedOption
                ? 'bg-white hover:bg-slate-100 text-slate-700 border-slate-300 shadow-2xs'
                : 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed'
            }`}
            title="Clear currently selected answer choice"
          >
            <RotateCcw className="w-3.5 h-3.5 shrink-0" />
            <span className="truncate">Clear</span>
          </button>
        </div>

        {/* Row 2: Primary Navigation & Save & Next */}
        <div className="flex items-center gap-1.5">
          {/* Previous Question */}
          <button
            onClick={onPrevious}
            disabled={isFirstQuestion}
            className={`py-2.5 px-3 rounded text-xs font-bold flex items-center justify-center space-x-1 border transition-colors shrink-0 touch-manipulation active:scale-98 ${
              isFirstQuestion
                ? 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed'
                : 'bg-white hover:bg-slate-100 text-slate-800 border-slate-300 shadow-2xs'
            }`}
            title="Previous Question"
          >
            <ChevronLeft className="w-4 h-4" />
            <span className="hidden xs:inline">Prev</span>
          </button>

          {/* Save & Next (Prominent Primary Button) */}
          <button
            onClick={onSaveAndNext}
            className="flex-1 bg-[#2563eb] hover:bg-[#1d4ed8] text-white py-2.5 px-3 rounded text-xs font-black flex items-center justify-center space-x-1.5 shadow-md transition-colors touch-manipulation active:scale-98"
            title="Save your answer and proceed to the next question"
          >
            <Check className="w-4 h-4" />
            <span>Save & Next</span>
          </button>

          {/* Next Question */}
          <button
            onClick={onNext}
            disabled={isLastQuestion}
            className={`py-2.5 px-3 rounded text-xs font-bold flex items-center justify-center space-x-1 border transition-colors shrink-0 touch-manipulation active:scale-98 ${
              isLastQuestion
                ? 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed'
                : 'bg-white hover:bg-slate-100 text-slate-800 border-slate-300 shadow-2xs'
            }`}
            title="Next Question"
          >
            <span className="hidden xs:inline">Next</span>
            <ChevronRight className="w-4 h-4" />
          </button>

          {/* Mobile Palette Drawer Trigger */}
          {onOpenPalette && (
            <button
              onClick={onOpenPalette}
              className="py-2.5 px-2.5 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-bold flex items-center justify-center shadow-xs transition-colors shrink-0 touch-manipulation active:scale-98"
              title="Open Question Palette"
            >
              <LayoutGrid className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Desktop Layout (>= lg) - Authentic NTA Desktop Action Bar */}
      <div className="hidden lg:flex items-center justify-between gap-2.5">
        {/* Left side actions (Action Buttons) */}
        <div className="flex items-center gap-2">
          {/* 1. Save & Next */}
          <button
            onClick={onSaveAndNext}
            className="bg-[#2563eb] hover:bg-[#1d4ed8] text-white px-4 py-2 rounded text-sm font-semibold flex items-center space-x-1.5 shadow-xs transition-colors cursor-pointer"
            title="Save your answer and proceed to the next question"
          >
            <Check className="w-4 h-4" />
            <span>Save & Next</span>
          </button>

          {/* 2. Save & Mark for Review */}
          <button
            onClick={onSaveAndMarkForReview}
            disabled={!hasSelectedOption}
            className={`px-3.5 py-2 rounded text-sm font-semibold flex items-center space-x-1.5 shadow-xs transition-colors cursor-pointer ${
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
            className={`px-3.5 py-2 rounded text-sm font-semibold flex items-center space-x-1.5 border transition-colors cursor-pointer ${
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
            className="bg-[#7c3aed] hover:bg-[#6d28d9] text-white px-3.5 py-2 rounded text-sm font-semibold flex items-center space-x-1.5 shadow-xs transition-colors cursor-pointer"
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
            className={`px-3.5 py-2 rounded text-sm font-semibold flex items-center space-x-1 border transition-colors cursor-pointer ${
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
            className={`px-3.5 py-2 rounded text-sm font-semibold flex items-center space-x-1 border transition-colors cursor-pointer ${
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
    </div>
  );
};
