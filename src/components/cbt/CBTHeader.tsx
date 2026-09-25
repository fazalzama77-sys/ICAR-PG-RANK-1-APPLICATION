import React from 'react';
import { Clock, Maximize2, Minimize2, User, ShieldCheck, LayoutGrid } from 'lucide-react';
import { UserProfile } from '../../storage/db';
import { Domain } from '../../types';
import { usePwa } from '../../hooks/usePwa';

interface CBTHeaderProps {
  examTitle: string;
  userProfile: UserProfile;
  timeRemainingSeconds: number;
  currentSection: Domain;
  onSectionChange: (section: Domain) => void;
  sectionCounts: {
    veterinary_science: number;
    animal_science: number;
  };
  isFullscreen: boolean;
  onToggleFullscreen: () => void;
  onOpenMobilePalette?: () => void;
  currentQuestionIndex?: number;
  totalQuestions?: number;
}

export const CBTHeader: React.FC<CBTHeaderProps> = ({
  examTitle,
  userProfile,
  timeRemainingSeconds,
  currentSection,
  onSectionChange,
  sectionCounts,
  isFullscreen,
  onToggleFullscreen,
  onOpenMobilePalette,
  currentQuestionIndex = 0,
  totalQuestions
}) => {
  const { isOnline } = usePwa();

  // Format seconds into HH:MM:SS
  const formatTime = (secs: number) => {
    const hours = Math.floor(secs / 3600);
    const minutes = Math.floor((secs % 3600) / 60);
    const seconds = secs % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  };

  const isLowTime = timeRemainingSeconds <= 600 && timeRemainingSeconds > 0; // <= 10 mins

  return (
    <div className="bg-[#2b547e] text-white border-b-2 border-[#1e3c59] select-none shadow-md pt-safe">
      {/* Upper Bar: Official NTA Header */}
      <div className="px-2.5 sm:px-6 py-2 sm:py-2.5 flex items-center justify-between gap-2 border-b border-[#3b6b9d]">
        <div className="flex items-center space-x-2 sm:space-x-3 min-w-0">
          <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-sm bg-white/10 flex items-center justify-center font-bold text-xs border border-white/20 shrink-0">
            NTA
          </div>
          <div className="min-w-0">
            <h1 className="font-bold text-xs sm:text-base leading-tight tracking-wide text-amber-300 uppercase truncate">
              {examTitle}
            </h1>
            <p className="text-[10px] sm:text-xs text-slate-200 truncate">
              Computer Based Test (CBT) &bull; Vet & Animal Sci
            </p>
          </div>
        </div>

        {/* Candidate Badge & System Info & Mobile Palette Trigger */}
        <div className="flex items-center space-x-1.5 sm:space-x-3 shrink-0">
          {/* Mobile Palette Button */}
          {onOpenMobilePalette && (
            <button
              onClick={onOpenMobilePalette}
              className="lg:hidden flex items-center space-x-1 px-2.5 py-1 rounded bg-amber-400 hover:bg-amber-300 text-slate-950 font-bold text-xs shadow-xs transition-colors cursor-pointer active:scale-95"
              title="Open Question Palette"
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span>Palette</span>
              <span className="bg-slate-900 text-amber-300 text-[10px] px-1 py-0.2 rounded font-mono leading-none">
                {currentQuestionIndex + 1}/{totalQuestions || 120}
              </span>
            </button>
          )}

          {/* Offline Security Badge */}
          <div
            className="hidden md:flex items-center space-x-1.5 px-2.5 py-1 rounded bg-black/20 border border-white/15 text-[11px] text-slate-200"
            title="100% Offline Exam: Questions and responses are securely stored locally."
          >
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
            <span>{isOnline ? 'Offline Ready' : '100% Offline'}</span>
          </div>

          {/* Candidate Card in Official NTA style */}
          <div className="hidden sm:flex items-center space-x-2 bg-white/10 px-2.5 sm:px-3 py-1 rounded border border-white/15">
            <div className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-200 text-slate-700 flex items-center justify-center font-bold text-xs shadow-inner">
              <User className="w-4 h-4 text-slate-600" />
            </div>
            <div className="text-right">
              <p className="text-xs font-bold leading-tight text-white truncate max-w-[100px]">{userProfile.name}</p>
              <p className="text-[10px] text-amber-200 font-mono hidden md:block">Roll: {userProfile.rollNumber}</p>
            </div>
          </div>

          {/* Fullscreen Button */}
          <button
            onClick={onToggleFullscreen}
            className="p-1.5 rounded bg-white/10 hover:bg-white/20 text-slate-200 hover:text-white transition-colors text-xs flex items-center space-x-1"
            title={isFullscreen ? 'Exit Fullscreen' : 'Enter Fullscreen'}
          >
            {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Lower Bar: Section Tabs & Countdown Timer */}
      <div className="px-2.5 sm:px-6 py-1.5 bg-[#1f3f60] flex items-center justify-between gap-2 overflow-x-auto">
        {/* Section Navigation Tabs */}
        <div className="flex items-center space-x-1.5 sm:space-x-2">
          <span className="text-xs font-semibold text-slate-300 uppercase tracking-wider mr-1 hidden lg:inline">
            Sections:
          </span>

          <button
            onClick={() => onSectionChange('veterinary_science')}
            className={`px-2 sm:px-3 py-1 sm:py-1.5 rounded-t text-xs font-bold transition-colors flex items-center space-x-1.5 shrink-0 ${
              currentSection === 'veterinary_science'
                ? 'bg-white text-[#1f3f60] shadow-sm'
                : 'bg-white/10 text-slate-200 hover:bg-white/20'
            }`}
          >
            <span className="hidden sm:inline">Veterinary Science (Code 13)</span>
            <span className="sm:hidden">Vet Sci</span>
            <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
              currentSection === 'veterinary_science' ? 'bg-[#1f3f60] text-white' : 'bg-white/20 text-white'
            }`}>
              {sectionCounts.veterinary_science}
            </span>
          </button>

          <button
            onClick={() => onSectionChange('animal_science')}
            className={`px-2 sm:px-3 py-1 sm:py-1.5 rounded-t text-xs font-bold transition-colors flex items-center space-x-1.5 shrink-0 ${
              currentSection === 'animal_science'
                ? 'bg-white text-[#1f3f60] shadow-sm'
                : 'bg-white/10 text-slate-200 hover:bg-white/20'
            }`}
          >
            <span className="hidden sm:inline">Animal Sciences (Code 14)</span>
            <span className="sm:hidden">Animal Sci</span>
            <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
              currentSection === 'animal_science' ? 'bg-[#1f3f60] text-white' : 'bg-white/20 text-white'
            }`}>
              {sectionCounts.animal_science}
            </span>
          </button>
        </div>

        {/* Real-time Countdown Timer */}
        <div className="flex items-center space-x-2">
          <div
            className={`flex items-center space-x-2 px-3 py-1 rounded font-mono font-bold text-sm tracking-wider shadow-inner transition-colors ${
              isLowTime
                ? 'bg-red-600 text-white animate-pulse'
                : 'bg-amber-400 text-slate-900'
            }`}
          >
            <Clock className="w-4 h-4" />
            <span>Time Left: {formatTime(timeRemainingSeconds)}</span>
          </div>
        </div>
      </div>
    </div>
  );
};
