import { Question, TestResult } from '../types';

const STORAGE_KEYS = {
  QUESTIONS: 'icar_pg_questions_v1',
  RESULTS: 'icar_pg_results_v1',
  USER_PROFILE: 'icar_pg_user_profile_v1'
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
      if (!data) return [];
      return JSON.parse(data) as Question[];
    } catch (e) {
      console.error('Failed to load questions from localStorage', e);
      return [];
    }
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
    } catch (e) {
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
