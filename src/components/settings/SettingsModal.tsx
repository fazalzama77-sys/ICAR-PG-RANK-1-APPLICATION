import React, { useState, useEffect } from 'react';
import { 
  X, 
  Settings, 
  User, 
  Cpu, 
  Database, 
  RefreshCw, 
  Trash2, 
  AlertTriangle, 
  CheckCircle2, 
  HardDrive, 
  RotateCcw,
  Check,
  ShieldAlert,
  Layers,
  BarChart3,
  Brain
} from 'lucide-react';
import { UserProfile, StorageService } from '../../storage/db';
import { CacheService, StorageSummary } from '../../storage/cacheService';

interface SettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  userProfile: UserProfile;
  onProfileUpdate: (updated: UserProfile) => void;
  onDataReset: () => void;
  defaultTab?: 'profile' | 'cache' | 'data';
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  onClose,
  userProfile,
  onProfileUpdate,
  onDataReset,
  defaultTab = 'profile'
}) => {
  const [activeTab, setActiveTab] = useState<'profile' | 'cache' | 'data'>(defaultTab);
  const [editProfile, setEditProfile] = useState<UserProfile>(userProfile);
  
  // Storage summary state
  const [storageSummary, setStorageSummary] = useState<StorageSummary | null>(null);
  const [isLoadingSummary, setIsLoadingSummary] = useState(false);

  // Cache reset state
  const [isClearingCache, setIsClearingCache] = useState(false);
  const [cacheClearMessage, setCacheClearMessage] = useState<string | null>(null);
  const [autoReload, setAutoReload] = useState(true);

  // Granular action feedback
  const [actionFeedback, setActionFeedback] = useState<string | null>(null);

  // Factory reset confirmation modal state
  const [showConfirmFactoryReset, setShowConfirmFactoryReset] = useState(false);
  const [confirmInputText, setConfirmInputText] = useState('');
  const [isResettingAll, setIsResettingAll] = useState(false);

  // Refresh summary data
  const loadSummary = async () => {
    setIsLoadingSummary(true);
    try {
      const summary = await CacheService.getStorageSummary();
      setStorageSummary(summary);
    } finally {
      setIsLoadingSummary(false);
    }
  };

  useEffect(() => {
    if (isOpen) {
      setEditProfile(userProfile);
      setCacheClearMessage(null);
      setActionFeedback(null);
      setShowConfirmFactoryReset(false);
      setConfirmInputText('');
      loadSummary();
    }
  }, [isOpen, userProfile]);

  useEffect(() => {
    if (defaultTab) {
      setActiveTab(defaultTab);
    }
  }, [defaultTab]);

  if (!isOpen) return null;

  // Handle Profile Save
  const handleSaveProfile = (e: React.FormEvent) => {
    e.preventDefault();
    StorageService.saveUserProfile(editProfile);
    onProfileUpdate(editProfile);
    setActionFeedback('Candidate profile updated successfully!');
    setTimeout(() => setActionFeedback(null), 3000);
  };

  // Handle Reset Cache Memory
  const handleResetCacheMemory = async () => {
    setIsClearingCache(true);
    setCacheClearMessage(null);
    try {
      const res = await CacheService.resetCacheMemory();
      setCacheClearMessage(res.message);
      await loadSummary();

      if (autoReload) {
        setTimeout(() => {
          window.location.reload();
        }, 1200);
      }
    } catch (e: any) {
      setCacheClearMessage(`Error clearing cache: ${e?.message || 'Unknown error'}`);
    } finally {
      setIsClearingCache(false);
    }
  };

  // Handle Granular: Clear Test History
  const handleClearTestHistory = () => {
    if (window.confirm('Are you sure you want to clear all past CBT test history and scorecards?')) {
      CacheService.resetTestResults();
      onDataReset();
      loadSummary();
      setActionFeedback('Test history and scorecards cleared.');
      setTimeout(() => setActionFeedback(null), 3000);
    }
  };

  // Handle Granular: Reset SRS
  const handleResetSRS = () => {
    if (window.confirm('Reset all Spaced Repetition flashcards and active recall schedules back to initial state?')) {
      CacheService.resetSRSProgress();
      onDataReset();
      loadSummary();
      setActionFeedback('Spaced Repetition cards reset.');
      setTimeout(() => setActionFeedback(null), 3000);
    }
  };

  // Handle Granular: Restore Question Bank
  const handleRestoreQuestionBank = () => {
    if (window.confirm('Restore Question Bank to the official 1,380 verified questions?')) {
      const res = CacheService.restoreDefaultQuestionBank();
      onDataReset();
      loadSummary();
      setActionFeedback(`Question bank restored to ${res.count} verified questions.`);
      setTimeout(() => setActionFeedback(null), 3000);
    }
  };

  // Handle Granular: Reset Streak & Profile
  const handleResetStreak = () => {
    if (window.confirm('Reset study streak and today\'s question count?')) {
      CacheService.resetDailyStreak();
      onDataReset();
      loadSummary();
      setActionFeedback('Daily streak and study targets reset.');
      setTimeout(() => setActionFeedback(null), 3000);
    }
  };

  // Handle Factory Reset (All Data)
  const handleExecuteFactoryReset = async () => {
    setIsResettingAll(true);
    try {
      const res = await CacheService.resetAllData();
      setShowConfirmFactoryReset(false);
      setConfirmInputText('');
      onDataReset();
      await loadSummary();
      setActionFeedback(res.message);
      setTimeout(() => {
        setActionFeedback(null);
        window.location.reload();
      }, 1500);
    } finally {
      setIsResettingAll(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-3 sm:p-4 overflow-y-auto">
      <div className="bg-white rounded-2xl shadow-2xl max-w-2xl w-full border border-slate-200 overflow-hidden my-6 flex flex-col max-h-[90vh]">
        
        {/* Header */}
        <div className="bg-gradient-to-r from-[#172e48] via-[#1f3f60] to-[#28537d] text-white px-5 py-4 flex items-center justify-between shrink-0">
          <div className="flex items-center space-x-3">
            <div className="w-9 h-9 rounded-lg bg-white/10 flex items-center justify-center border border-white/20">
              <Settings className="w-5 h-5 text-amber-300" />
            </div>
            <div>
              <h3 className="font-extrabold text-base sm:text-lg tracking-tight leading-tight">
                App Settings &amp; Storage Controls
              </h3>
              <p className="text-xs text-slate-200 font-medium">
                Manage Profile, Cache Memory &amp; Stored Application Data
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-white/10 transition-colors"
            title="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Switcher */}
        <div className="flex border-b border-slate-200 bg-slate-50 px-4 pt-2 gap-2 shrink-0">
          <button
            onClick={() => setActiveTab('profile')}
            className={`flex items-center space-x-2 px-3 py-2.5 text-xs sm:text-sm font-bold border-b-2 transition-colors ${
              activeTab === 'profile'
                ? 'border-emerald-600 text-emerald-800 bg-white rounded-t-lg shadow-2xs'
                : 'border-transparent text-slate-600 hover:text-slate-900'
            }`}
          >
            <User className="w-4 h-4" />
            <span>Candidate Profile</span>
          </button>

          <button
            onClick={() => setActiveTab('cache')}
            className={`flex items-center space-x-2 px-3 py-2.5 text-xs sm:text-sm font-bold border-b-2 transition-colors ${
              activeTab === 'cache'
                ? 'border-indigo-600 text-indigo-800 bg-white rounded-t-lg shadow-2xs'
                : 'border-transparent text-slate-600 hover:text-slate-900'
            }`}
          >
            <Cpu className="w-4 h-4 text-indigo-600" />
            <span>Reset Cache Memory</span>
          </button>

          <button
            onClick={() => setActiveTab('data')}
            className={`flex items-center space-x-2 px-3 py-2.5 text-xs sm:text-sm font-bold border-b-2 transition-colors ${
              activeTab === 'data'
                ? 'border-rose-600 text-rose-800 bg-white rounded-t-lg shadow-2xs'
                : 'border-transparent text-slate-600 hover:text-slate-900'
            }`}
          >
            <Database className="w-4 h-4 text-rose-600" />
            <span>Reset Data</span>
          </button>
        </div>

        {/* Feedback Alert Toast */}
        {actionFeedback && (
          <div className="bg-emerald-50 border-b border-emerald-200 text-emerald-800 px-5 py-2.5 text-xs font-semibold flex items-center space-x-2 shrink-0 animate-in fade-in">
            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
            <span>{actionFeedback}</span>
          </div>
        )}

        {/* Body Viewport */}
        <div className="p-5 overflow-y-auto space-y-5 flex-1">
          
          {/* TAB 1: CANDIDATE PROFILE */}
          {activeTab === 'profile' && (
            <form onSubmit={handleSaveProfile} className="space-y-4">
              <div className="bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-xs text-slate-600 leading-relaxed">
                Candidate credentials reflect on the authentic NTA Computer Based Test top ribbon and official generated scorecards.
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Candidate Full Name</label>
                <input
                  type="text"
                  required
                  value={editProfile.name}
                  onChange={e => setEditProfile({ ...editProfile, name: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden bg-white"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Roll / Application Number</label>
                <input
                  type="text"
                  required
                  value={editProfile.rollNumber}
                  onChange={e => setEditProfile({ ...editProfile, rollNumber: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden font-mono bg-white"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Target Examination</label>
                <input
                  type="text"
                  value={editProfile.targetExam}
                  onChange={e => setEditProfile({ ...editProfile, targetExam: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden bg-white"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Veterinary College / University</label>
                <input
                  type="text"
                  value={editProfile.college}
                  onChange={e => setEditProfile({ ...editProfile, college: e.target.value })}
                  className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden bg-white"
                />
              </div>

              <div className="pt-2 flex justify-end">
                <button
                  type="submit"
                  className="px-5 py-2 text-xs sm:text-sm font-bold text-white bg-emerald-600 hover:bg-emerald-700 rounded-lg shadow-sm transition-colors flex items-center space-x-1.5 cursor-pointer"
                >
                  <Check className="w-4 h-4" />
                  <span>Save Profile</span>
                </button>
              </div>
            </form>
          )}

          {/* TAB 2: RESET CACHE MEMORY */}
          {activeTab === 'cache' && (
            <div className="space-y-5">
              
              {/* Informational Banner */}
              <div className="bg-indigo-50/70 border border-indigo-200 rounded-xl p-4 text-xs text-indigo-900 space-y-1.5">
                <div className="flex items-center space-x-2 font-bold text-indigo-950 text-sm">
                  <Cpu className="w-4 h-4 text-indigo-600" />
                  <span>What is Cache Memory?</span>
                </div>
                <p className="leading-relaxed text-indigo-800">
                  Cache Memory holds temporary network bundles, compiled JavaScript, stylesheet assets, and offline PWA precaches. Resetting cache flushes out outdated app bundles and downloads the newest version.
                </p>
                <div className="flex items-center space-x-1.5 text-[11px] font-bold text-emerald-800 bg-emerald-100/80 px-2.5 py-1 rounded-md mt-2 w-fit">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                  <span>Your test scorecards, question bank, and study streak are 100% SAFE and preserved.</span>
                </div>
              </div>

              {/* Cache Memory Diagnostics */}
              <div>
                <h4 className="text-xs font-bold text-slate-600 uppercase tracking-wider mb-2 flex items-center space-x-1.5">
                  <HardDrive className="w-3.5 h-3.5 text-slate-500" />
                  <span>Live Cache &amp; Storage Diagnostics</span>
                </h4>

                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center">
                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Cache Buckets</span>
                    <span className="text-base font-extrabold text-slate-800">
                      {isLoadingSummary ? '...' : `${storageSummary?.cacheBucketsCount || 0} active`}
                    </span>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Service Worker</span>
                    <span className={`text-xs font-bold ${storageSummary?.isServiceWorkerActive ? 'text-emerald-700' : 'text-slate-600'}`}>
                      {isLoadingSummary ? '...' : (storageSummary?.isServiceWorkerActive ? 'Active' : 'Standby')}
                    </span>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Storage Quota</span>
                    <span className="text-xs font-bold text-slate-800">
                      {isLoadingSummary ? '...' : (storageSummary?.quotaUsageMb ? `${storageSummary.quotaUsageMb} MB` : 'Available')}
                    </span>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Android Bridge</span>
                    <span className="text-xs font-bold text-slate-800">
                      {(typeof window !== 'undefined' && (window as any).AndroidBridge) ? 'Connected' : 'Web/PWA'}
                    </span>
                  </div>
                </div>
              </div>

              {/* Action Box */}
              <div className="border border-slate-200 rounded-xl p-4 bg-slate-50/50 space-y-3">
                <div className="flex items-center justify-between">
                  <div>
                    <h4 className="text-sm font-extrabold text-slate-900">Purge &amp; Reset Cache Memory</h4>
                    <p className="text-xs text-slate-500 mt-0.5">
                      Frees cached memory, resets service workers, and forces fresh download.
                    </p>
                  </div>
                </div>

                <label className="flex items-center space-x-2 text-xs text-slate-700 cursor-pointer select-none">
                  <input
                    type="checkbox"
                    checked={autoReload}
                    onChange={e => setAutoReload(e.target.checked)}
                    className="rounded border-slate-300 text-indigo-600 focus:ring-indigo-500"
                  />
                  <span>Automatically reload application after clearing cache</span>
                </label>

                {cacheClearMessage && (
                  <div className="p-3 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-medium flex items-center space-x-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                    <span>{cacheClearMessage}</span>
                  </div>
                )}

                <button
                  type="button"
                  onClick={handleResetCacheMemory}
                  disabled={isClearingCache}
                  className="w-full py-2.5 px-4 bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 text-white font-bold text-xs sm:text-sm rounded-lg shadow-sm flex items-center justify-center space-x-2 transition-colors disabled:opacity-50 cursor-pointer"
                >
                  <RefreshCw className={`w-4 h-4 ${isClearingCache ? 'animate-spin' : ''}`} />
                  <span>{isClearingCache ? 'Clearing Cache Memory...' : 'Reset Cache Memory Now'}</span>
                </button>
              </div>

            </div>
          )}

          {/* TAB 3: RESET DATA */}
          {activeTab === 'data' && (
            <div className="space-y-5">
              
              {/* Informational Banner */}
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 text-xs text-amber-900 space-y-1.5">
                <div className="flex items-center space-x-2 font-bold text-amber-950 text-sm">
                  <AlertTriangle className="w-4 h-4 text-amber-600" />
                  <span>Application Data Management</span>
                </div>
                <p className="leading-relaxed text-amber-800">
                  Manage your offline study data. You can perform targeted resets (e.g. clear only test history or restore default questions) or execute a full Factory Reset.
                </p>
              </div>

              {/* Stored Data Metrics */}
              <div>
                <h4 className="text-xs font-bold text-slate-600 uppercase tracking-wider mb-2 flex items-center space-x-1.5">
                  <Database className="w-3.5 h-3.5 text-slate-500" />
                  <span>Current Stored Data Breakdown</span>
                </h4>

                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center">
                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Questions in Bank</span>
                    <span className="text-base font-extrabold text-slate-800">
                      {storageSummary?.questionsCount || 0}
                    </span>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Completed Tests</span>
                    <span className="text-base font-extrabold text-slate-800">
                      {storageSummary?.resultsCount || 0}
                    </span>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">SRS Flashcards</span>
                    <span className="text-base font-extrabold text-slate-800">
                      {storageSummary?.srsCardsCount || 0}
                    </span>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <span className="block text-[11px] text-slate-500 font-medium">Storage Size</span>
                    <span className="text-base font-extrabold text-slate-800">
                      {storageSummary?.localStorageKb || 0} KB
                    </span>
                  </div>
                </div>
              </div>

              {/* Granular Reset Actions */}
              <div className="space-y-2.5">
                <h4 className="text-xs font-bold text-slate-600 uppercase tracking-wider">
                  Targeted Data Reset Options
                </h4>

                {/* 1. Clear Test History */}
                <div className="flex items-center justify-between p-3 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 transition-colors">
                  <div className="pr-3">
                    <span className="font-bold text-xs text-slate-800 block">Clear CBT Test History &amp; Scorecards</span>
                    <span className="text-[11px] text-slate-500">Deletes test attempts and scorecards without touching question bank.</span>
                  </div>
                  <button
                    type="button"
                    onClick={handleClearTestHistory}
                    className="px-3 py-1.5 rounded-lg border border-slate-300 hover:border-red-300 hover:bg-red-50 text-slate-700 hover:text-red-700 text-xs font-bold shrink-0 transition-colors cursor-pointer"
                  >
                    Clear History
                  </button>
                </div>

                {/* 2. Reset Spaced Repetition */}
                <div className="flex items-center justify-between p-3 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 transition-colors">
                  <div className="pr-3">
                    <span className="font-bold text-xs text-slate-800 block">Reset Spaced Repetition (SRS) Flashcards</span>
                    <span className="text-[11px] text-slate-500">Resets active recall intervals and due dates back to new status.</span>
                  </div>
                  <button
                    type="button"
                    onClick={handleResetSRS}
                    className="px-3 py-1.5 rounded-lg border border-slate-300 hover:border-indigo-300 hover:bg-indigo-50 text-slate-700 hover:text-indigo-700 text-xs font-bold shrink-0 transition-colors cursor-pointer"
                  >
                    Reset SRS
                  </button>
                </div>

                {/* 3. Restore Default 1,380 Questions */}
                <div className="flex items-center justify-between p-3 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 transition-colors">
                  <div className="pr-3">
                    <span className="font-bold text-xs text-slate-800 block">Restore Official Question Bank (1,380 MCQs)</span>
                    <span className="text-[11px] text-slate-500">Restores all 1,080 base questions + 300 PYQs to their textbook default.</span>
                  </div>
                  <button
                    type="button"
                    onClick={handleRestoreQuestionBank}
                    className="px-3 py-1.5 rounded-lg border border-slate-300 hover:border-emerald-300 hover:bg-emerald-50 text-slate-700 hover:text-emerald-700 text-xs font-bold shrink-0 transition-colors cursor-pointer"
                  >
                    Restore Bank
                  </button>
                </div>

                {/* 4. Reset Daily Streak */}
                <div className="flex items-center justify-between p-3 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 transition-colors">
                  <div className="pr-3">
                    <span className="font-bold text-xs text-slate-800 block">Reset Daily Goal &amp; Study Streak</span>
                    <span className="text-[11px] text-slate-500">Resets today's solved count and streak counter back to day 1.</span>
                  </div>
                  <button
                    type="button"
                    onClick={handleResetStreak}
                    className="px-3 py-1.5 rounded-lg border border-slate-300 hover:border-amber-300 hover:bg-amber-50 text-slate-700 hover:text-amber-700 text-xs font-bold shrink-0 transition-colors cursor-pointer"
                  >
                    Reset Streak
                  </button>
                </div>
              </div>

              {/* DANGER ZONE: Full Factory Reset */}
              <div className="border-2 border-rose-200 bg-rose-50/50 rounded-xl p-4 space-y-3">
                <div className="flex items-start space-x-2.5">
                  <ShieldAlert className="w-5 h-5 text-rose-600 shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-xs sm:text-sm font-extrabold text-rose-950">
                      Danger Zone: Factory Reset (Reset All Data)
                    </h4>
                    <p className="text-xs text-rose-800 mt-0.5 leading-relaxed">
                      Permanently wipes all test history, scorecards, SRS flashcard progress, and custom questions, re-seeding the clean default 1,380 official questions and candidate profile.
                    </p>
                  </div>
                </div>

                <button
                  type="button"
                  onClick={() => {
                    setShowConfirmFactoryReset(true);
                    setConfirmInputText('');
                  }}
                  className="w-full py-2.5 px-4 bg-rose-600 hover:bg-rose-700 active:bg-rose-800 text-white font-extrabold text-xs sm:text-sm rounded-lg shadow-sm flex items-center justify-center space-x-2 transition-colors cursor-pointer"
                >
                  <Trash2 className="w-4 h-4" />
                  <span>Factory Reset (Reset All Data)</span>
                </button>
              </div>

            </div>
          )}

        </div>

        {/* Footer */}
        <div className="px-5 py-3 bg-slate-50 border-t border-slate-200 flex justify-between items-center text-xs text-slate-500 shrink-0">
          <span>ICAR AIEEA PG (M.V.Sc.) CBT Prep &bull; AIR 1 Engine</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 font-bold text-slate-700 hover:bg-slate-200 rounded-lg transition-colors"
          >
            Close
          </button>
        </div>

      </div>

      {/* Confirmation Modal for Factory Reset */}
      {showConfirmFactoryReset && (
        <div className="fixed inset-0 z-60 flex items-center justify-center bg-black/70 backdrop-blur-xs p-4">
          <div className="bg-white rounded-xl shadow-2xl max-w-md w-full p-6 border-2 border-rose-500 space-y-4 animate-in zoom-in-95">
            <div className="flex items-center space-x-3 text-rose-600">
              <AlertTriangle className="w-7 h-7 shrink-0" />
              <div>
                <h4 className="font-black text-base text-slate-900 leading-tight">Confirm Factory Reset</h4>
                <p className="text-xs text-rose-700 font-semibold">This action cannot be undone!</p>
              </div>
            </div>

            <p className="text-xs text-slate-600 leading-relaxed">
              You are about to wipe all saved test scores, analysis history, SRS flashcards, and custom questions. The question bank will be restored to the 1,380 official questions.
            </p>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">
                Type <span className="font-mono text-rose-600 font-black">RESET</span> to confirm:
              </label>
              <input
                type="text"
                placeholder="RESET"
                value={confirmInputText}
                onChange={e => setConfirmInputText(e.target.value)}
                className="w-full text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-rose-500 focus:outline-hidden font-mono uppercase bg-white"
              />
            </div>

            <div className="flex justify-end space-x-2 pt-2">
              <button
                type="button"
                onClick={() => {
                  setShowConfirmFactoryReset(false);
                  setConfirmInputText('');
                }}
                className="px-4 py-2 text-xs font-bold text-slate-600 hover:bg-slate-100 rounded-lg transition-colors cursor-pointer"
              >
                Cancel
              </button>
              <button
                type="button"
                disabled={confirmInputText.trim().toUpperCase() !== 'RESET' || isResettingAll}
                onClick={handleExecuteFactoryReset}
                className="px-4 py-2 text-xs font-black text-white bg-rose-600 hover:bg-rose-700 rounded-lg shadow-sm transition-colors disabled:opacity-40 flex items-center space-x-1.5 cursor-pointer"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>{isResettingAll ? 'Resetting...' : 'Yes, Reset All Data'}</span>
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};
