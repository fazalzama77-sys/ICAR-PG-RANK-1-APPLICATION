import React, { useState } from 'react';
import { Award, BookOpen, Layers, BarChart3, Settings, ShieldCheck, Download, WifiOff } from 'lucide-react';
import { UserProfile, StorageService } from '../../storage/db';
import { usePwa } from '../../hooks/usePwa';
import { PwaStatusBanner } from '../pwa/PwaStatusBanner';

interface TopNavProps {
  activeTab: 'dashboard' | 'cbt_config' | 'question_bank' | 'analytics';
  setActiveTab: (tab: 'dashboard' | 'cbt_config' | 'question_bank' | 'analytics') => void;
  userProfile: UserProfile;
  onProfileUpdate: (updated: UserProfile) => void;
  isExamInProgress: boolean;
}

export const TopNav: React.FC<TopNavProps> = ({
  activeTab,
  setActiveTab,
  userProfile,
  onProfileUpdate,
  isExamInProgress
}) => {
  const [showProfileModal, setShowProfileModal] = useState(false);
  const [editProfile, setEditProfile] = useState<UserProfile>(userProfile);
  const { isOnline, canInstall, installPwa } = usePwa();

  const handleSaveProfile = (e: React.FormEvent) => {
    e.preventDefault();
    StorageService.saveUserProfile(editProfile);
    onProfileUpdate(editProfile);
    setShowProfileModal(false);
  };

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
            <nav className="hidden md:flex space-x-1">
              <button
                onClick={() => setActiveTab('dashboard')}
                className={`flex items-center space-x-2 px-3.5 py-2 rounded-md text-sm font-medium transition-colors ${
                  activeTab === 'dashboard'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <Layers className="w-4 h-4" />
                <span>Dashboard</span>
              </button>

              <button
                onClick={() => setActiveTab('cbt_config')}
                className={`flex items-center space-x-2 px-3.5 py-2 rounded-md text-sm font-medium transition-colors ${
                  activeTab === 'cbt_config'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <ShieldCheck className="w-4 h-4" />
                <span>Take CBT Test</span>
              </button>

              <button
                onClick={() => setActiveTab('question_bank')}
                className={`flex items-center space-x-2 px-3.5 py-2 rounded-md text-sm font-medium transition-colors ${
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
                className={`flex items-center space-x-2 px-3.5 py-2 rounded-md text-sm font-medium transition-colors ${
                  activeTab === 'analytics'
                    ? 'bg-emerald-50 text-emerald-700 font-semibold'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <BarChart3 className="w-4 h-4" />
                <span>Analytics & History</span>
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

              {/* User Candidate Info Pill */}
              <button
                onClick={() => {
                  setEditProfile(userProfile);
                  setShowProfileModal(true);
                }}
                className="flex items-center space-x-2 text-left pl-3 pr-3.5 py-1.5 rounded-full border border-slate-200 bg-slate-50 hover:bg-slate-100 transition-colors text-xs"
                title="Click to edit Candidate profile"
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
                <Settings className="w-3.5 h-3.5 text-slate-400 ml-1" />
              </button>
            </div>

          </div>
        </div>
      </header>

      {/* Candidate Profile Modal */}
      {showProfileModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-4">
          <div className="bg-white rounded-xl shadow-xl max-w-md w-full p-6 border border-slate-200">
            <h3 className="text-lg font-bold text-slate-900 mb-1">Candidate Profile Details</h3>
            <p className="text-xs text-slate-500 mb-4">
              These details will display in the authentic NTA CBT top bar and scorecard.
            </p>

            <form onSubmit={handleSaveProfile} className="space-y-3.5">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Candidate Full Name</label>
                <input
                  type="text"
                  required
                  value={editProfile.name}
                  onChange={e => setEditProfile({ ...editProfile, name: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Roll / Application Number</label>
                <input
                  type="text"
                  required
                  value={editProfile.rollNumber}
                  onChange={e => setEditProfile({ ...editProfile, rollNumber: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden font-mono"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Target Examination</label>
                <input
                  type="text"
                  value={editProfile.targetExam}
                  onChange={e => setEditProfile({ ...editProfile, targetExam: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Veterinary College / University</label>
                <input
                  type="text"
                  value={editProfile.college}
                  onChange={e => setEditProfile({ ...editProfile, college: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
                />
              </div>

              <div className="flex justify-end space-x-2 pt-3 border-t border-slate-100">
                <button
                  type="button"
                  onClick={() => setShowProfileModal(false)}
                  className="px-4 py-2 text-xs font-medium text-slate-600 hover:bg-slate-100 rounded-lg"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-semibold text-white bg-emerald-600 hover:bg-emerald-700 rounded-lg shadow-xs"
                >
                  Save Profile
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
};
