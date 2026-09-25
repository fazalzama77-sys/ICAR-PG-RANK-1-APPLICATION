import { STORAGE_KEYS, DEFAULT_USER_PROFILE } from './db';
import { ALL_HIGH_YIELD_QUESTIONS } from '../data/questionPacks/allQuestions';

export interface StorageSummary {
  questionsCount: number;
  resultsCount: number;
  srsCardsCount: number;
  streakDays: number;
  localStorageKb: number;
  cacheBucketsCount: number;
  quotaUsageMb: number | null;
  quotaTotalMb: number | null;
  isServiceWorkerActive: boolean;
}

export const CacheService = {
  /**
   * Calculates a detailed snapshot of stored data and cache footprint
   */
  async getStorageSummary(): Promise<StorageSummary> {
    let questionsCount = 0;
    let resultsCount = 0;
    let srsCardsCount = 0;
    let streakDays = 0;
    let localStorageBytes = 0;

    // 1. Analyze localStorage items
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key) {
          const val = localStorage.getItem(key) || '';
          localStorageBytes += (key.length + val.length) * 2; // Approximate UTF-16 bytes
        }
      }

      const qData = localStorage.getItem(STORAGE_KEYS.QUESTIONS);
      if (qData) {
        try {
          const parsed = JSON.parse(qData);
          if (Array.isArray(parsed)) questionsCount = parsed.length;
        } catch {
          // ignore
        }
      }

      const rData = localStorage.getItem(STORAGE_KEYS.RESULTS);
      if (rData) {
        try {
          const parsed = JSON.parse(rData);
          if (Array.isArray(parsed)) resultsCount = parsed.length;
        } catch {
          // ignore
        }
      }

      const srsData = localStorage.getItem(STORAGE_KEYS.SRS_RECORDS);
      if (srsData) {
        try {
          const parsed = JSON.parse(srsData);
          srsCardsCount = Object.keys(parsed || {}).length;
        } catch {
          // ignore
        }
      }

      const progData = localStorage.getItem(STORAGE_KEYS.DAILY_PROGRESS);
      if (progData) {
        try {
          const parsed = JSON.parse(progData);
          streakDays = parsed?.streakDays || 0;
        } catch {
          // ignore
        }
      }
    } catch (e) {
      console.error('Error analyzing localStorage:', e);
    }

    // 2. Cache API buckets count
    let cacheBucketsCount = 0;
    try {
      if (typeof window !== 'undefined' && 'caches' in window) {
        const keys = await caches.keys();
        cacheBucketsCount = keys.length;
      }
    } catch (e) {
      console.warn('Unable to query caches:', e);
    }

    // 3. Quota estimate from StorageManager API
    let quotaUsageMb: number | null = null;
    let quotaTotalMb: number | null = null;
    try {
      if (typeof navigator !== 'undefined' && navigator.storage && navigator.storage.estimate) {
        const estimate = await navigator.storage.estimate();
        if (typeof estimate.usage === 'number') {
          quotaUsageMb = Math.round((estimate.usage / (1024 * 1024)) * 10) / 10;
        }
        if (typeof estimate.quota === 'number') {
          quotaTotalMb = Math.round((estimate.quota / (1024 * 1024)) * 10) / 10;
        }
      }
    } catch {
      // Storage estimate not supported or denied
    }

    // 4. Service worker status
    const isServiceWorkerActive = typeof navigator !== 'undefined' && !!navigator.serviceWorker?.controller;

    return {
      questionsCount,
      resultsCount,
      srsCardsCount,
      streakDays,
      localStorageKb: Math.round((localStorageBytes / 1024) * 10) / 10,
      cacheBucketsCount,
      quotaUsageMb,
      quotaTotalMb,
      isServiceWorkerActive
    };
  },

  /**
   * Resets Cache Memory:
   * - Deletes all Cache Storage containers (Workbox precache, dynamic assets)
   * - Unregisters active service workers
   * - Clears sessionStorage
   * - Calls AndroidBridge.resetCacheMemory() if hosted inside Android APK
   * NOTE: Preserves question bank, test scores, and study progress!
   */
  async resetCacheMemory(): Promise<{ success: boolean; clearedCaches: number; message: string }> {
    let clearedCount = 0;

    // 1. Delete all Cache API entries
    try {
      if (typeof window !== 'undefined' && 'caches' in window) {
        const keys = await caches.keys();
        for (const key of keys) {
          const deleted = await caches.delete(key);
          if (deleted) clearedCount++;
        }
      }
    } catch (e) {
      console.error('Error clearing Cache Storage:', e);
    }

    // 2. Unregister Service Workers so fresh workers/assets are fetched
    try {
      if (typeof navigator !== 'undefined' && 'serviceWorker' in navigator) {
        const registrations = await navigator.serviceWorker.getRegistrations();
        for (const reg of registrations) {
          await reg.unregister();
        }
      }
    } catch (e) {
      console.warn('Error unregistering service workers:', e);
    }

    // 3. Clear session storage
    try {
      if (typeof sessionStorage !== 'undefined') {
        sessionStorage.clear();
      }
    } catch (e) {
      console.warn('Error clearing sessionStorage:', e);
    }

    // 4. Trigger Android Native Bridge if running inside Android APK
    try {
      if (typeof window !== 'undefined' && (window as any).AndroidBridge?.resetCacheMemory) {
        (window as any).AndroidBridge.resetCacheMemory();
      }
    } catch (e) {
      console.warn('Error communicating with AndroidBridge:', e);
    }

    return {
      success: true,
      clearedCaches: clearedCount,
      message: `Successfully cleared ${clearedCount} cache container(s) and refreshed service workers. Your test records & question bank remain safe.`
    };
  },

  /**
   * Factory Reset: Clears all user data and restores default pristine state
   */
  async resetAllData(): Promise<{ success: boolean; message: string }> {
    try {
      // 1. Clear application data keys in localStorage
      localStorage.removeItem(STORAGE_KEYS.RESULTS);
      localStorage.removeItem(STORAGE_KEYS.SRS_RECORDS);
      localStorage.removeItem(STORAGE_KEYS.DAILY_PROGRESS);
      
      // 2. Re-seed default 1,515 official questions (balanced options across A, B, C, D)
      localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(ALL_HIGH_YIELD_QUESTIONS));
      localStorage.setItem(STORAGE_KEYS.QUESTIONS_BALANCED_VERSION, 'true');

      // 3. Reset Candidate Profile to Default
      localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(DEFAULT_USER_PROFILE));

      // 4. Reset today's daily progress
      const today = new Date().toISOString().slice(0, 10);
      localStorage.setItem(STORAGE_KEYS.DAILY_PROGRESS, JSON.stringify({
        date: today,
        questionsSolvedToday: 0,
        dailyTarget: 30,
        streakDays: 1,
        lastActiveDate: today
      }));

      // 5. Trigger Android Native Bridge if running inside Android APK
      if (typeof window !== 'undefined' && (window as any).AndroidBridge?.resetData) {
        try {
          (window as any).AndroidBridge.resetData();
        } catch (e) {
          console.warn('Error communicating with AndroidBridge for resetData:', e);
        }
      }

      return {
        success: true,
        message: 'All application data has been reset to pristine factory defaults with all 1,515 verified questions reloaded.'
      };
    } catch (e: any) {
      console.error('Failed to reset all data:', e);
      return {
        success: false,
        message: `Failed to reset data: ${e?.message || 'Unknown error'}`
      };
    }
  },

  /**
   * Resets only CBT Test Results and Scorecard history
   */
  resetTestResults(): void {
    localStorage.removeItem(STORAGE_KEYS.RESULTS);
  },

  /**
   * Resets only Spaced Repetition (SRS) Flashcard memory & learning schedules
   */
  resetSRSProgress(): void {
    localStorage.removeItem(STORAGE_KEYS.SRS_RECORDS);
  },

  /**
   * Restores Question Bank to the official 1,515 high-yield questions
   */
  restoreDefaultQuestionBank(): { count: number } {
    localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(ALL_HIGH_YIELD_QUESTIONS));
    localStorage.setItem(STORAGE_KEYS.QUESTIONS_BALANCED_VERSION, 'true');
    return { count: ALL_HIGH_YIELD_QUESTIONS.length };
  },

  /**
   * Resets Candidate Profile to default
   */
  resetUserProfile(): void {
    localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(DEFAULT_USER_PROFILE));
  },

  /**
   * Resets Daily Goal & Streak Tracking
   */
  resetDailyStreak(): void {
    const today = new Date().toISOString().slice(0, 10);
    localStorage.setItem(STORAGE_KEYS.DAILY_PROGRESS, JSON.stringify({
      date: today,
      questionsSolvedToday: 0,
      dailyTarget: 30,
      streakDays: 1,
      lastActiveDate: today
    }));
  }
};
