import React from 'react';
import { User } from 'lucide-react';
import { Question, QuestionState, UserResponseState, Domain } from '../../types';
import { UserProfile } from '../../storage/db';

interface CBTPaletteProps {
  questions: Question[];
  userResponses: Record<string, UserResponseState>;
  currentQuestionIndex: number;
  onSelectQuestion: (index: number) => void;
  onSubmitExam: () => void;
  userProfile: UserProfile;
  currentSection: Domain;
}

export const CBTPalette: React.FC<CBTPaletteProps> = ({
  questions,
  userResponses,
  currentQuestionIndex,
  onSelectQuestion,
  onSubmitExam,
  userProfile,
  currentSection
}) => {
  // Compute counts for all 5 NTA states
  const stateCounts = {
    ANSWERED: 0,
    NOT_ANSWERED: 0,
    NOT_VISITED: 0,
    MARKED_FOR_REVIEW: 0,
    ANSWERED_AND_MARKED_FOR_REVIEW: 0
  };

  questions.forEach(q => {
    const resp = userResponses[q.id];
    const state: QuestionState = resp ? resp.state : 'NOT_VISITED';
    stateCounts[state]++;
  });

  // Filter questions that belong to the currently viewed section for the grid
  const sectionQuestionsWithOriginalIndex = questions
    .map((q, idx) => ({ question: q, originalIndex: idx }))
    .filter(item => item.question.domain === currentSection);

  // Helper function to return authentic NTA palette button styles
  const getPaletteButtonClass = (state: QuestionState, isActive: boolean) => {
    let baseClass = 'w-9 h-9 sm:w-10 sm:h-10 text-xs font-bold flex items-center justify-center transition-all cursor-pointer select-none ';
    
    if (isActive) {
      baseClass += 'ring-2 ring-blue-600 ring-offset-2 scale-105 z-10 ';
    }

    switch (state) {
      case 'ANSWERED':
        return baseClass + 'nta-answered shadow-xs';
      case 'NOT_ANSWERED':
        return baseClass + 'nta-not-answered shadow-xs';
      case 'MARKED_FOR_REVIEW':
        return baseClass + 'nta-marked-review shadow-xs';
      case 'ANSWERED_AND_MARKED_FOR_REVIEW':
        return baseClass + 'nta-answered-marked shadow-xs';
      case 'NOT_VISITED':
      default:
        return baseClass + 'nta-not-visited hover:bg-slate-100 shadow-2xs';
    }
  };

  return (
    <div className="w-full lg:w-80 bg-white border-l border-slate-300 flex flex-col h-full overflow-hidden select-none">
      {/* Candidate Profile Box in Palette */}
      <div className="p-3 bg-[#e9eef4] border-b border-slate-300 flex items-center space-x-3">
        <div className="w-10 h-10 rounded bg-slate-300 border border-slate-400 flex items-center justify-center text-slate-700">
          <User className="w-6 h-6 text-slate-600" />
        </div>
        <div className="overflow-hidden">
          <h4 className="text-xs font-bold text-slate-900 truncate">{userProfile.name}</h4>
          <p className="text-[11px] text-slate-600 font-mono">Roll: {userProfile.rollNumber}</p>
        </div>
      </div>

      {/* Official 5-Color NTA Legend Box */}
      <div className="p-3 bg-slate-50 border-b border-slate-300">
        <div className="text-[11px] font-bold uppercase tracking-wider text-slate-700 mb-2 border-b border-slate-200 pb-1">
          Legend & Question Status
        </div>

        <div className="grid grid-cols-2 gap-2 text-[11px]">
          {/* Answered */}
          <div className="flex items-center space-x-2">
            <div className="w-5 h-5 nta-answered flex items-center justify-center text-[10px] font-bold shrink-0">
              {stateCounts.ANSWERED}
            </div>
            <span className="text-slate-700 leading-tight">Answered</span>
          </div>

          {/* Not Answered */}
          <div className="flex items-center space-x-2">
            <div className="w-5 h-5 nta-not-answered flex items-center justify-center text-[10px] font-bold shrink-0">
              {stateCounts.NOT_ANSWERED}
            </div>
            <span className="text-slate-700 leading-tight">Not Answered</span>
          </div>

          {/* Not Visited */}
          <div className="flex items-center space-x-2">
            <div className="w-5 h-5 nta-not-visited flex items-center justify-center text-[10px] font-bold shrink-0">
              {stateCounts.NOT_VISITED}
            </div>
            <span className="text-slate-700 leading-tight">Not Visited</span>
          </div>

          {/* Marked for Review */}
          <div className="flex items-center space-x-2">
            <div className="w-5 h-5 nta-marked-review flex items-center justify-center text-[10px] font-bold shrink-0">
              {stateCounts.MARKED_FOR_REVIEW}
            </div>
            <span className="text-slate-700 leading-tight">Marked for Review</span>
          </div>
        </div>

        {/* 5th NTA Status: Answered & Marked for Review */}
        <div className="mt-2.5 pt-2 border-t border-slate-200 flex items-start space-x-2">
          <div className="w-5 h-5 nta-answered-marked flex items-center justify-center text-[10px] font-bold shrink-0 mt-0.5">
            {stateCounts.ANSWERED_AND_MARKED_FOR_REVIEW}
          </div>
          <span className="text-[10px] text-slate-600 leading-tight">
            Answered & Marked for Review (<span className="text-emerald-700 font-semibold">evaluated</span>)
          </span>
        </div>
      </div>

      {/* Palette Title */}
      <div className="px-3 py-2 bg-[#2b547e] text-white flex items-center justify-between">
        <span className="text-xs font-bold uppercase tracking-wide">
          {currentSection === 'veterinary_science' ? 'Veterinary Science Grid' : 'Animal Science Grid'}
        </span>
        <span className="text-[11px] bg-white/20 px-2 py-0.5 rounded font-mono">
          {sectionQuestionsWithOriginalIndex.length} Questions
        </span>
      </div>

      {/* Question Number Palette Grid */}
      <div className="flex-1 p-3 overflow-y-auto bg-slate-100/60">
        <div className="grid grid-cols-5 sm:grid-cols-5 gap-2 justify-items-center">
          {sectionQuestionsWithOriginalIndex.map(item => {
            const resp = userResponses[item.question.id];
            const state: QuestionState = resp ? resp.state : 'NOT_VISITED';
            const isActive = currentQuestionIndex === item.originalIndex;

            return (
              <button
                key={item.question.id}
                onClick={() => onSelectQuestion(item.originalIndex)}
                className={getPaletteButtonClass(state, isActive)}
                title={`Question ${item.originalIndex + 1} (${state.replace(/_/g, ' ')})`}
              >
                {item.originalIndex + 1}
              </button>
            );
          })}
        </div>
      </div>

      {/* Submit Exam Button in Palette Bottom */}
      <div className="p-3 bg-white border-t border-slate-300 shadow-lg">
        <button
          onClick={onSubmitExam}
          className="w-full bg-[#16a34a] hover:bg-[#15803d] text-white py-2.5 px-4 rounded font-bold text-sm uppercase tracking-wider shadow-sm transition-all transform active:scale-98 flex items-center justify-center space-x-2"
        >
          <span>Submit Exam</span>
        </button>
      </div>
    </div>
  );
};
