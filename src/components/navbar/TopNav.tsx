import React from 'react';
import { Award, BookOpen, Layers, BarChart3, Settings, ShieldCheck, Download, WifiOff, Zap, Brain } from 'lucide-react';
import { UserProfile } from '../../storage/db';
import { usePwa } from '../../hooks/usePwa';
import { PwaStatusBanner } from '../pwa/PwaStatusBanner';
import { NavigationTab } from '../../types';

interface TopNavProps {
  activeTab: NavigationTab;
  setActiveTab: (tab: NavigationTab) => void;
  userProfile: UserProfile;
  onOpenSettings: (tab?: 'profile' | 'cache' | 'data') => void;
  isExamInProgress: boolean;
  srsDueCount?: number;
}

export const TopNav: React.FC<TopNavProps> = ({
  activeTab,
  setActiveTab,
  userProfile,
  onOpenSettings,
  isExamInProgress,
  srsDueCount = 0
}) => {
  const { isOnline, canInstall, installPwa } = usePwa();

  // If exam is in progress, the global top nav is replaced by the authentic NTA CBT exam header
  if (isExamInProgress) {
    return null;
  }

  return (
    <>
      <PwaStatusBanner />
      <header className="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            
            {/* Branding */}
            <div className="flex items-center space-x-3 cursor-pointer" onClick={() => setActiveTab('dashboard')}>
              <div className="w-10 h-10 rounded-lg bg-gradient-to-tr from-emerald-600 to-teal-700 flex items-center justify-center text-white shadow-sm">
                <Award className="w-6 h-6" />
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <span className="font-bold text-slate-900 tracking-tight text-lg">ICAR AIEEA PG</span>
                  <span className="bg-amber-100 text-amber-800 text-xs font-semibold px-2 py-0.5 rounded-full border border-amber-300">
                    AIR 1 Mission
                  </span>
                </div>
                <p className="text-xs text-slate-500 font-medium">B.V.Sc. & A.H. 1st & 2nd Year CBT Prep Portal</p>
              </div>
            </div>

            {/* Navigation Tabs */}
            <nav className="hidden lg:flex space-x-1">
              <button
                onClick={() => setActiveTab('dashboard')}
                className={`flex items-center space-x-1.5 px-3 py-2 rounded-md text-xs sm:text-sm font-medium transition-colors ${
                  activeTab === 'dashboard'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <Layers className="w-4 h-4" />
                <span>Dashboard</span>
              </button>

              <button
                onClick={() => setActiveTab('drill_test')}
                className={`flex items-center space-x-1.5 px-3 py-2 rounded-md text-xs sm:text-sm font-medium transition-colors ${
                  activeTab === 'drill_test'
                    ? 'bg-amber-50 text-amber-800 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <Zap className="w-4 h-4 text-amber-500 fill-amber-500" />
                <span>Rapid Drill</span>
              </button>

              <button
                onClick={() => setActiveTab('spaced_repetition')}
                className={`flex items-center space-x-1.5 px-3 py-2 rounded-md text-xs sm:text-sm font-medium transition-colors relative ${
                  activeTab === 'spaced_repetition'
                    ? 'bg-indigo-50 text-indigo-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <Brain className="w-4 h-4 text-indigo-600" />
                <span>Spaced Repetition</span>
                {srsDueCount > 0 && (
                  <span className="bg-amber-400 text-slate-950 text-[10px] font-black px-1.5 py-0.2 rounded-full ml-1">
                    {srsDueCount}
                  </span>
                )}
              </button>

              <button
                onClick={() => setActiveTab('cbt_config')}
                className={`flex items-center space-x-1.5 px-3 py-2 rounded-md text-xs sm:text-sm font-medium transition-colors ${
                  activeTab === 'cbt_config'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <ShieldCheck className="w-4 h-4" />
                <span>Take CBT Mock</span>
              </button>

              <button
                onClick={() => setActiveTab('question_bank')}
                className={`flex items-center space-x-1.5 px-3 py-2 rounded-md text-xs sm:text-sm font-medium transition-colors ${
                  activeTab === 'question_bank'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <BookOpen className="w-4 h-4" />
                <span>Question Bank</span>
              </button>

              <button
                onClick={() => setActiveTab('analytics')}
                className={`flex items-center space-x-1.5 px-3 py-2 rounded-md text-xs sm:text-sm font-medium transition-colors ${
                  activeTab === 'analytics'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <BarChart3 className="w-4 h-4" />
                <span>Analytics</span>
              </button>
            </nav>

            {/* Right Action Items: PWA Status & Install + User Candidate Info */}
            <div className="flex items-center space-x-2.5">
              {/* PWA Install Button (visible when install prompt is available) */}
              {canInstall && (
                <button
                  onClick={installPwa}
                  className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold shadow-xs transition-colors"
                  title="Install ICAR AIEEA PG CBT App for offline desktop/tablet use"
                >
                  <Download className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Install App</span>
                </button>
              )}

              {/* Online / Offline Status Badge */}
              <div
                className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium border ${
                  isOnline
                    ? 'bg-emerald-50 text-emerald-700 border-emerald-200'
                    : 'bg-amber-50 text-amber-800 border-amber-300'
                }`}
                title={isOnline ? 'All mock questions & tests work 100% offline' : 'Working 100% offline'}
              >
                {isOnline ? (
                  <>
                    <span className="w-2 h-2 rounded-full bg-emerald-500" />
                    <span className="hidden md:inline">Offline Ready</span>
                  </>
                ) : (
                  <>
                    <WifiOff className="w-3 h-3 text-amber-600 animate-pulse" />
                    <span>Offline</span>
                  </>
                )}
              </div>

              {/* Dedicated Settings & Storage Action Button */}
              <button
                onClick={() => onOpenSettings('cache')}
                className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg border border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-700 hover:text-slate-900 transition-colors text-xs font-semibold cursor-pointer"
                title="Reset Cache Memory, Reset Data & Storage Settings"
              >
                <Settings className="w-3.5 h-3.5 text-slate-500" />
                <span className="hidden sm:inline">Settings</span>
              </button>

              {/* User Candidate Info Pill */}
              <button
                onClick={() => onOpenSettings('profile')}
                className="flex items-center space-x-2 text-left pl-3 pr-3.5 py-1.5 rounded-full border border-slate-200 bg-slate-50 hover:bg-slate-100 transition-colors text-xs cursor-pointer"
                title="Click to edit Candidate Profile & View App Settings"
              >
                <div className="w-6 h-6 rounded-full bg-emerald-700 text-white flex items-center justify-center font-bold text-[10px]">
                  {userProfile.name.charAt(0) || 'V'}
                </div>
                <div className="hidden sm:block">
                  <span className="font-semibold text-slate-800 block truncate max-w-[120px] leading-tight">
                    {userProfile.name}
                  </span>
                  <span className="text-[10px] text-emerald-700 font-mono">
                    {userProfile.rollNumber}
                  </span>
                </div>
              </button>
            </div>

          </div>
        </div>
      </header>
    </>
  );
};
