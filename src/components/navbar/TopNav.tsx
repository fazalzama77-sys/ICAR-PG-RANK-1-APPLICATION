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

  const navItems = [
    {
      id: 'dashboard' as NavigationTab,
      label: 'Dashboard',
      shortLabel: 'Dashboard',
      icon: Layers,
      color: 'emerald'
    },
    {
      id: 'drill_test' as NavigationTab,
      label: 'Rapid Drill',
      shortLabel: 'Drill',
      icon: Zap,
      iconClass: 'text-amber-500 fill-amber-500',
      color: 'amber'
    },
    {
      id: 'spaced_repetition' as NavigationTab,
      label: 'Spaced Repetition',
      shortLabel: 'Revision',
      icon: Brain,
      iconClass: 'text-indigo-600',
      badge: srsDueCount > 0 ? srsDueCount : undefined,
      color: 'indigo'
    },
    {
      id: 'cbt_config' as NavigationTab,
      label: 'CBT Mock',
      shortLabel: 'CBT Mock',
      icon: ShieldCheck,
      color: 'emerald'
    },
    {
      id: 'question_bank' as NavigationTab,
      label: 'Question Bank',
      shortLabel: 'Q-Bank',
      icon: BookOpen,
      color: 'emerald'
    },
    {
      id: 'analytics' as NavigationTab,
      label: 'Analytics',
      shortLabel: 'Analytics',
      icon: BarChart3,
      color: 'emerald'
    }
  ];

  return (
    <>
      <PwaStatusBanner />
      <header className="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs pt-[env(safe-area-inset-top,0px)]">
        <div className="w-full max-w-[1580px] mx-auto px-3 sm:px-4 lg:px-6">
          <div className="flex items-center justify-between h-16 gap-2">
            
            {/* Branding (Fixed height, perfectly centered, never clipped) */}
            <div 
              className="flex items-center space-x-2.5 cursor-pointer shrink-0 select-none py-1 group" 
              onClick={() => setActiveTab('dashboard')}
              title="Return to Dashboard"
            >
              <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-700 flex items-center justify-center text-white shadow-xs shrink-0 group-hover:scale-105 transition-transform">
                <Award className="w-5 h-5" />
              </div>
              <div className="flex flex-col justify-center min-w-0">
                <div className="flex items-center space-x-1.5">
                  <span className="font-extrabold text-slate-900 tracking-tight text-base sm:text-lg leading-none whitespace-nowrap">
                    ICAR AIEEA PG
                  </span>
                  <span className="bg-amber-100 text-amber-900 text-[10px] font-bold px-1.5 py-0.5 rounded-full border border-amber-300 shadow-2xs whitespace-nowrap leading-none">
                    AIR 1
                  </span>
                </div>
                <p className="text-[11px] text-slate-500 font-medium whitespace-nowrap leading-none mt-1 truncate hidden md:block">
                  B.V.Sc. &amp; A.H. CBT Prep Portal
                </p>
              </div>
            </div>

            {/* Desktop / Tablet Navigation Tabs */}
            <nav className="hidden md:flex items-center space-x-1 lg:space-x-1.5 shrink-0">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = activeTab === item.id;
                let activeClasses = 'bg-emerald-50 text-emerald-800 font-bold border border-emerald-200/80 shadow-2xs';
                if (item.color === 'amber') {
                  activeClasses = 'bg-amber-50 text-amber-900 font-bold border border-amber-200/80 shadow-2xs';
                } else if (item.color === 'indigo') {
                  activeClasses = 'bg-indigo-50 text-indigo-900 font-bold border border-indigo-200/80 shadow-2xs';
                }

                return (
                  <button
                    key={item.id}
                    onClick={() => setActiveTab(item.id)}
                    className={`flex items-center space-x-1.5 px-2.5 xl:px-3 py-1.5 rounded-lg text-xs xl:text-sm font-semibold transition-all whitespace-nowrap shrink-0 cursor-pointer ${
                      isActive
                        ? activeClasses
                        : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                    }`}
                  >
                    <Icon className={`w-4 h-4 shrink-0 ${item.iconClass || ''}`} />
                    <span className="hidden xl:inline">{item.label}</span>
                    <span className="xl:hidden">{item.shortLabel}</span>
                    {item.badge !== undefined && (
                      <span className="bg-amber-400 text-slate-950 text-[10px] font-black px-1.5 py-0.5 rounded-full leading-none ml-0.5 shadow-2xs">
                        {item.badge}
                      </span>
                    )}
                  </button>
                );
              })}
            </nav>

            {/* Right Action Items: PWA Status & Install + User Candidate Info */}
            <div className="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
              {/* PWA Install Button */}
              {canInstall && (
                <button
                  onClick={installPwa}
                  className="hidden 2xl:flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold shadow-xs transition-colors shrink-0 whitespace-nowrap cursor-pointer"
                  title="Install ICAR AIEEA PG CBT App for offline desktop/tablet use"
                >
                  <Download className="w-3.5 h-3.5" />
                  <span>Install App</span>
                </button>
              )}

              {/* Online / Offline Status Badge */}
              <div
                className={`flex items-center space-x-1.5 px-2 sm:px-2.5 py-1 rounded-full text-xs font-semibold border shrink-0 whitespace-nowrap ${
                  isOnline
                    ? 'bg-emerald-50 text-emerald-700 border-emerald-200'
                    : 'bg-amber-50 text-amber-800 border-amber-300'
                }`}
                title={isOnline ? 'All 1,665 mock questions work 100% offline' : 'Working 100% offline'}
              >
                {isOnline ? (
                  <>
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                    <span className="hidden 2xl:inline text-[11px]">Offline Ready</span>
                  </>
                ) : (
                  <>
                    <WifiOff className="w-3.5 h-3.5 text-amber-600 animate-pulse" />
                    <span className="text-[11px]">Offline</span>
                  </>
                )}
              </div>

              {/* Dedicated Settings & Storage Action Button */}
              <button
                onClick={() => onOpenSettings('cache')}
                className="flex items-center space-x-1 px-2 py-1.5 rounded-lg border border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-700 hover:text-slate-900 transition-colors text-xs font-semibold shrink-0 cursor-pointer whitespace-nowrap"
                title="Reset Cache Memory, Reset Data & Storage Settings"
              >
                <Settings className="w-3.5 h-3.5 text-slate-500" />
                <span className="hidden lg:inline text-[11px]">Settings</span>
              </button>

              {/* User Candidate Info Pill */}
              <button
                onClick={() => onOpenSettings('profile')}
                className="flex items-center space-x-2 text-left pl-1.5 pr-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 hover:bg-slate-100 transition-colors text-xs shrink-0 cursor-pointer"
                title="Click to edit Candidate Profile & View App Settings"
              >
                <div className="w-7 h-7 rounded-full bg-emerald-700 text-white flex items-center justify-center font-bold text-xs shrink-0 shadow-2xs">
                  {userProfile.name.charAt(0) || 'V'}
                </div>
                <div className="hidden sm:block min-w-0">
                  <span className="font-semibold text-slate-800 block truncate max-w-[80px] xl:max-w-[120px] leading-tight text-xs">
                    {userProfile.name}
                  </span>
                  <span className="text-[10px] text-emerald-700 font-mono block leading-none hidden xl:block">
                    {userProfile.rollNumber}
                  </span>
                </div>
              </button>
            </div>

          </div>
        </div>
      </header>

      {/* Mobile / Tablet Bottom Navigation Bar */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-white border-t border-slate-200 shadow-lg px-2 pt-1.5 pb-[max(0.6rem,env(safe-area-inset-bottom,0px))] flex items-center justify-around">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`flex flex-col items-center justify-center py-1 px-1.5 rounded-lg transition-colors relative min-w-[48px] ${
                isActive
                  ? 'text-emerald-700 font-bold'
                  : 'text-slate-500 hover:text-slate-900'
              }`}
            >
              <Icon className={`w-5 h-5 ${item.iconClass || ''}`} />
              <span className="text-[10px] mt-0.5 tracking-tight leading-none truncate max-w-[58px]">
                {item.shortLabel}
              </span>
              {item.badge !== undefined && (
                <span className="absolute top-0 right-1 bg-amber-400 text-slate-950 text-[9px] font-black px-1 rounded-full leading-none">
                  {item.badge}
                </span>
              )}
            </button>
          );
        })}
      </nav>
    </>
  );
};
