import { Question, TestResult, SRSRecord, SRSRating, SRSMetrics, DailyProgress } from '../types';
import { ALL_HIGH_YIELD_QUESTIONS } from '../data/questionPacks/allQuestions';

const STORAGE_KEYS = {
  QUESTIONS: 'icar_pg_questions_v1',
  RESULTS: 'icar_pg_results_v1',
  USER_PROFILE: 'icar_pg_user_profile_v1',
  SRS_RECORDS: 'icar_pg_srs_records_v1',
  DAILY_PROGRESS: 'icar_pg_daily_progress_v1'
};

export interface UserProfile {
  name: string;
  rollNumber: string;
  targetExam: string;
  targetRank: string;
  college: string;
}

export const DEFAULT_USER_PROFILE: UserProfile = {
  name: 'B.V.Sc. & A.H. Scholar',
  rollNumber: 'ICAR-AIEEA-PG-001',
  targetExam: 'ICAR AIEEA PG (M.V.Sc.)',
  targetRank: 'All India Rank 1',
  college: 'Veterinary College'
};

export const StorageService = {
  // Questions Bank Management
  getQuestions(): Question[] {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.QUESTIONS);
      if (!data) {
        // Auto-seed with all 1,080 high-yield questions across all 9 subjects
        localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(ALL_HIGH_YIELD_QUESTIONS));
        return ALL_HIGH_YIELD_QUESTIONS;
      }
      const parsed = JSON.parse(data) as Question[];
      if (parsed.length === 0) {
        localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(ALL_HIGH_YIELD_QUESTIONS));
        return ALL_HIGH_YIELD_QUESTIONS;
      }
      return parsed;
    } catch (e) {
      console.error('Failed to load questions from localStorage', e);
      return ALL_HIGH_YIELD_QUESTIONS;
    }
  },

  loadAll1080Questions(): { count: number } {
    localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(ALL_HIGH_YIELD_QUESTIONS));
    return { count: ALL_HIGH_YIELD_QUESTIONS.length };
  },


  saveQuestions(questions: Question[]): void {
    try {
      localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(questions));
    } catch (e) {
      console.error('Failed to save questions to localStorage', e);
    }
  },

  addQuestion(question: Question): Question {
    const questions = this.getQuestions();
    const updated = [question, ...questions];
    this.saveQuestions(updated);
    return question;
  },

  updateQuestion(updatedQuestion: Question): void {
    const questions = this.getQuestions();
    const index = questions.findIndex(q => q.id === updatedQuestion.id);
    if (index !== -1) {
      questions[index] = updatedQuestion;
      this.saveQuestions(questions);
    }
  },

  deleteQuestion(id: string): void {
    const questions = this.getQuestions();
    const filtered = questions.filter(q => q.id !== id);
    this.saveQuestions(filtered);
  },

  bulkAddQuestions(newQuestions: Question[]): { addedCount: number; totalCount: number } {
    const current = this.getQuestions();
    const currentIds = new Set(current.map(q => q.id));
    
    // Add only questions with unique IDs or assign new IDs
    const prepared = newQuestions.map(q => {
      if (!q.id || currentIds.has(q.id)) {
        return { ...q, id: 'q_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9) };
      }
      return q;
    });

    const combined = [...prepared, ...current];
    this.saveQuestions(combined);
    return { addedCount: prepared.length, totalCount: combined.length };
  },

  clearAllQuestions(): void {
    localStorage.removeItem(STORAGE_KEYS.QUESTIONS);
  },

  // Test Results Management
  getTestResults(): TestResult[] {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.RESULTS);
      if (!data) return [];
      return JSON.parse(data) as TestResult[];
    } catch (e) {
      console.error('Failed to load test results', e);
      return [];
    }
  },

  saveTestResult(result: TestResult): void {
    try {
      const results = this.getTestResults();
      const updated = [result, ...results];
      localStorage.setItem(STORAGE_KEYS.RESULTS, JSON.stringify(updated));

      // Record daily progress
      this.recordQuestionsAttempted(result.attemptedCount);

      // Auto-enroll incorrect questions into Spaced Repetition queue
      const missedIds = result.questionRecords
        .filter(r => !r.isCorrect && r.response.selectedOptionIndex !== null)
        .map(r => r.question.id);
      
      if (missedIds.length > 0) {
        this.autoEnrollMissedQuestions(missedIds);
      }
    } catch (e) {
      console.error('Failed to save test result', e);
    }
  },

  deleteTestResult(id: string): void {
    const results = this.getTestResults();
    const filtered = results.filter(r => r.id !== id);
    localStorage.setItem(STORAGE_KEYS.RESULTS, JSON.stringify(filtered));
  },

  // User Profile
  getUserProfile(): UserProfile {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.USER_PROFILE);
      if (!data) return DEFAULT_USER_PROFILE;
      return JSON.parse(data) as UserProfile;
    } catch {
      return DEFAULT_USER_PROFILE;
    }
  },

  saveUserProfile(profile: UserProfile): void {
    try {
      localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(profile));
    } catch (e) {
      console.error('Failed to save profile', e);
    }
  },

  // ==========================================
  // SPACED REPETITION SYSTEM (SRS) - SM-2
  // ==========================================
  getSRSRecords(): Record<string, SRSRecord> {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.SRS_RECORDS);
      if (!data) return {};
      return JSON.parse(data) as Record<string, SRSRecord>;
    } catch (e) {
      console.error('Failed to load SRS records', e);
      return {};
    }
  },

  saveSRSRecord(record: SRSRecord): void {
    try {
      const records = this.getSRSRecords();
      records[record.questionId] = record;
      localStorage.setItem(STORAGE_KEYS.SRS_RECORDS, JSON.stringify(records));
    } catch (e) {
      console.error('Failed to save SRS record', e);
    }
  },

  recordSRSReview(questionId: string, rating: SRSRating): SRSRecord {
    const records = this.getSRSRecords();
    const existing = records[questionId] || {
      questionId,
      intervalDays: 0,
      repetition: 0,
      easeFactor: 2.5,
      dueDate: Date.now(),
      lastReviewed: Date.now(),
      status: 'new' as const,
      timesCorrect: 0,
      timesIncorrect: 0
    };

    let intervalDays = existing.intervalDays;
    let repetition = existing.repetition;
    let easeFactor = existing.easeFactor;
    let status = existing.status;
    let timesCorrect = existing.timesCorrect;
    let timesIncorrect = existing.timesIncorrect;

    const DAY_MS = 24 * 60 * 60 * 1000;

    switch (rating) {
      case 'again': {
        repetition = 0;
        intervalDays = 1;
        easeFactor = Math.max(1.3, easeFactor - 0.2);
        status = 'learning';
        timesIncorrect += 1;
        break;
      }
      case 'hard': {
        intervalDays = Math.max(1, Math.round((intervalDays || 1) * 1.2));
        easeFactor = Math.max(1.3, easeFactor - 0.15);
        status = 'learning';
        repetition += 1;
        timesCorrect += 1;
        break;
      }
      case 'good': {
        if (repetition === 0) {
          intervalDays = 1;
        } else if (repetition === 1) {
          intervalDays = 3;
        } else {
          intervalDays = Math.round(intervalDays * easeFactor);
        }
        repetition += 1;
        status = repetition >= 3 ? 'mastered' : 'review';
        timesCorrect += 1;
        break;
      }
      case 'easy': {
        if (repetition === 0) {
          intervalDays = 3;
        } else if (repetition === 1) {
          intervalDays = 6;
        } else {
          intervalDays = Math.round(intervalDays * easeFactor * 1.3);
        }
        easeFactor = Math.min(3.0, easeFactor + 0.15);
        repetition += 1;
        status = repetition >= 2 ? 'mastered' : 'review';
        timesCorrect += 1;
        break;
      }
    }

    const updated: SRSRecord = {
      questionId,
      intervalDays,
      repetition,
      easeFactor,
      dueDate: Date.now() + intervalDays * DAY_MS,
      lastReviewed: Date.now(),
      status,
      timesCorrect,
      timesIncorrect
    };

    this.saveSRSRecord(updated);
    this.recordQuestionsAttempted(1);
    return updated;
  },

  autoEnrollMissedQuestions(questionIds: string[]): void {
    const records = this.getSRSRecords();
    let updated = false;

    questionIds.forEach(qId => {
      const existing = records[qId];
      if (!existing) {
        records[qId] = {
          questionId: qId,
          intervalDays: 0,
          repetition: 0,
          easeFactor: 2.3,
          dueDate: Date.now(),
          lastReviewed: Date.now(),
          status: 'learning',
          timesCorrect: 0,
          timesIncorrect: 1
        };
        updated = true;
      } else {
        records[qId] = {
          ...existing,
          dueDate: Date.now(),
          status: 'learning',
          timesIncorrect: existing.timesIncorrect + 1
        };
        updated = true;
      }
    });

    if (updated) {
      try {
        localStorage.setItem(STORAGE_KEYS.SRS_RECORDS, JSON.stringify(records));
      } catch (e) {
        console.error('Failed to save auto-enrolled SRS records', e);
      }
    }
  },

  getSRSMetrics(questions: Question[]): SRSMetrics {
    const records = this.getSRSRecords();
    const now = Date.now();
    const qIds = new Set(questions.map(q => q.id));

    let dueToday = 0;
    let learning = 0;
    let review = 0;
    let mastered = 0;
    let totalEnrolled = 0;

    Object.values(records).forEach(rec => {
      if (!qIds.has(rec.questionId)) return;
      totalEnrolled += 1;

      if (rec.status === 'mastered') {
        mastered += 1;
      } else if (rec.status === 'review') {
        review += 1;
      } else {
        learning += 1;
      }

      if (rec.dueDate <= now + 4 * 60 * 60 * 1000) {
        dueToday += 1;
      }
    });

    return {
      dueToday,
      learning,
      review,
      mastered,
      totalEnrolled
    };
  },

  getDueQuestions(questions: Question[]): {
    due: Question[];
    learning: Question[];
    review: Question[];
    mastered: Question[];
    unreviewed: Question[];
  } {
    const records = this.getSRSRecords();
    const now = Date.now();

    const due: Question[] = [];
    const learning: Question[] = [];
    const review: Question[] = [];
    const mastered: Question[] = [];
    const unreviewed: Question[] = [];

    questions.forEach(q => {
      const rec = records[q.id];
      if (!rec) {
        unreviewed.push(q);
      } else {
        if (rec.status === 'mastered') {
          mastered.push(q);
        } else if (rec.status === 'review') {
          review.push(q);
        } else {
          learning.push(q);
        }

        if (rec.dueDate <= now + 4 * 60 * 60 * 1000) {
          due.push(q);
        }
      }
    });

    return { due, learning, review, mastered, unreviewed };
  },

  // ==========================================
  // DAILY GOAL & STREAK TRACKING
  // ==========================================
  getDailyProgress(): DailyProgress {
    const today = new Date().toISOString().slice(0, 10);
    try {
      const data = localStorage.getItem(STORAGE_KEYS.DAILY_PROGRESS);
      if (!data) {
        return {
          date: today,
          questionsSolvedToday: 0,
          dailyTarget: 30,
          streakDays: 1,
          lastActiveDate: today
        };
      }

      const parsed = JSON.parse(data) as DailyProgress;
      if (parsed.date !== today) {
        const lastDate = new Date(parsed.lastActiveDate);
        const currentDate = new Date(today);
        const diffDays = Math.round((currentDate.getTime() - lastDate.getTime()) / (1000 * 3600 * 24));

        let newStreak = parsed.streakDays;
        if (diffDays === 1) {
          // Studied yesterday, continue streak
        } else if (diffDays > 1) {
          newStreak = 1;
        }

        const fresh: DailyProgress = {
          date: today,
          questionsSolvedToday: 0,
          dailyTarget: parsed.dailyTarget || 30,
          streakDays: newStreak,
          lastActiveDate: parsed.lastActiveDate
        };
        localStorage.setItem(STORAGE_KEYS.DAILY_PROGRESS, JSON.stringify(fresh));
        return fresh;
      }

      return parsed;
    } catch {
      return {
        date: today,
        questionsSolvedToday: 0,
        dailyTarget: 30,
        streakDays: 1,
        lastActiveDate: today
      };
    }
  },

  recordQuestionsAttempted(count: number): DailyProgress {
    const progress = this.getDailyProgress();
    const today = new Date().toISOString().slice(0, 10);
    
    const updated: DailyProgress = {
      ...progress,
      date: today,
      questionsSolvedToday: progress.questionsSolvedToday + count,
      lastActiveDate: today
    };

    try {
      localStorage.setItem(STORAGE_KEYS.DAILY_PROGRESS, JSON.stringify(updated));
    } catch (e) {
      console.error('Failed to save daily progress', e);
    }

    return updated;
  },

  setDailyTarget(target: number): void {
    const progress = this.getDailyProgress();
    const updated = { ...progress, dailyTarget: Math.max(5, target) };
    try {
      localStorage.setItem(STORAGE_KEYS.DAILY_PROGRESS, JSON.stringify(updated));
    } catch (e) {
      console.error('Failed to update daily target', e);
    }
  },


  // Export questions to JSON
  exportQuestionsJSON(): string {
    const questions = this.getQuestions();
    return JSON.stringify(questions, null, 2);
  },

  // Generate Sample JSON Template for user to fill
  getSampleTemplateJSON(): string {
    const sampleQuestions: Question[] = [
      {
        id: 'sample_van_01',
        domain: 'veterinary_science',
        year: '1st_year',
        subjectId: 'van',
        topic: 'Osteology & Arthrology',
        questionText: 'Which of the following bones in the bovine skeleton possesses the "fossa extensoria"?',
        options: [
          'Distal lateral condyle of femur',
          'Proximal cranial border of tibia',
          'Distal extremity of humerus',
          'Proximal extremity of radius'
        ],
        correctOptionIndex: 0,
        explanation: 'The extensor fossa (fossa extensoria) is a depression situated on the lateral condyle of the femur in cattle, providing origin to the peroneus tertius and long digital extensor muscles.',
        difficulty: 'Medium',
        tags: ['Osteology', 'Femur', 'Bovine Anatomy']
      },
      {
        id: 'sample_lpm_01',
        domain: 'animal_science',
        year: '1st_year',
        subjectId: 'lpm',
        topic: 'Dairy Cattle & Buffalo Management',
        questionText: 'What is the optimum floor space requirement (covered area) for an adult dairy cow in a loose housing system?',
        options: [
          '3.5 square meters',
          '7.0 square meters',
          '1.5 square meters',
          '10.0 square meters'
        ],
        correctOptionIndex: 0,
        explanation: 'According to standard Bureau of Indian Standards (BIS) norms for loose housing systems, an adult dairy cow requires approximately 3.5 sq. meters (35 sq. ft.) of covered area and 7.0 sq. meters of open paddock area.',
        difficulty: 'Easy',
        tags: ['Housing', 'Space Requirement', 'Dairy Cattle']
      },
      {
        id: 'sample_vpp_01',
        domain: 'veterinary_science',
        year: '2nd_year',
        subjectId: 'vpp',
        topic: 'General Pathology',
        questionText: 'Zenker’s degeneration is a specific type of hyaline degeneration classically observed in which tissue?',
        options: [
          'Striated (skeletal) muscle',
          'Hepatic parenchymal cells',
          'Renal tubular epithelial cells',
          'Cardiac Purkinje fibers'
        ],
        correctOptionIndex: 0,
        explanation: 'Zenker’s degeneration (hyaline or waxy degeneration) specifically affects striated skeletal muscles and is commonly observed in conditions such as White Muscle Disease (Vitamin E / Selenium deficiency) or acute severe infections.',
        difficulty: 'Medium',
        tags: ['General Pathology', 'Degenerations', 'Muscle Pathology']
      },
      {
        id: 'sample_agb_01',
        domain: 'animal_science',
        year: '2nd_year',
        subjectId: 'agb',
        topic: 'Population Genetics',
        questionText: 'In a random mating population at Hardy-Weinberg equilibrium, if the frequency of recessive allele (q) is 0.3, what is the frequency of heterozygous carriers (2pq)?',
        options: [
          '0.42',
          '0.49',
          '0.09',
          '0.21'
        ],
        correctOptionIndex: 0,
        explanation: 'Given q = 0.3. Since p + q = 1, p = 1 - 0.3 = 0.7. The heterozygous genotype frequency is 2pq = 2 * 0.7 * 0.3 = 0.42.',
        difficulty: 'Easy',
        tags: ['Hardy-Weinberg', 'Population Genetics', 'Gene Frequency']
      }
    ];

    return JSON.stringify(sampleQuestions, null, 2);
  }
};
