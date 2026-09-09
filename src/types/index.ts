export type Domain = 'veterinary_science' | 'animal_science';

export type AcademicYear = '1st_year' | '2nd_year' | '3rd_year' | '4th_year' | '5th_year';

export interface Subject {
  id: string;
  name: string;
  code: string;
  domain: Domain;
  year: AcademicYear;
  description: string;
  topics: string[];
}

export interface Question {
  id: string;
  domain: Domain;
  year: AcademicYear;
  subjectId: string;
  topic?: string;
  questionText: string;
  options: [string, string, string, string]; // [A, B, C, D]
  correctOptionIndex: number; // 0, 1, 2, 3
  explanation: string;
  difficulty?: 'Easy' | 'Medium' | 'Hard';
  tags?: string[];
  createdAt?: number;
}

// NTA CBT 5 Official States
export type QuestionState = 
  | 'NOT_VISITED'                    // 0: Grey/White
  | 'NOT_ANSWERED'                   // 1: Red/Orange
  | 'ANSWERED'                       // 2: Green
  | 'MARKED_FOR_REVIEW'              // 3: Purple
  | 'ANSWERED_AND_MARKED_FOR_REVIEW';// 4: Purple with green dot

export interface UserResponseState {
  selectedOptionIndex: number | null;
  state: QuestionState;
  timeSpentSeconds: number;
  visited: boolean;
}

export interface TestConfig {
  mode: 'full_mock' | 'custom_practice';
  title: string;
  totalQuestions: number;
  durationMinutes: number; // 0 for untimed
  selectedDomains: Domain[];
  selectedYears: AcademicYear[];
  selectedSubjectIds: string[];
  positiveMarks: number; // default +4
  negativeMarks: number; // default -1
  shuffleQuestions: boolean;
}

export interface SubjectPerformance {
  subjectId: string;
  subjectName: string;
  domain: Domain;
  totalQuestions: number;
  attempted: number;
  correct: number;
  incorrect: number;
  score: number;
  maxScore: number;
  accuracy: number;
}

export interface DomainPerformance {
  domain: Domain;
  totalQuestions: number;
  attempted: number;
  correct: number;
  incorrect: number;
  score: number;
  maxScore: number;
  accuracy: number;
}

export interface TestResult {
  id: string;
  title: string;
  timestamp: number;
  dateString: string;
  config: TestConfig;
  totalQuestions: number;
  attemptedCount: number;
  correctCount: number;
  incorrectCount: number;
  unattemptedCount: number;
  markedForReviewCount: number;
  totalScore: number;
  maxPossibleScore: number;
  percentage: number;
  accuracy: number;
  timeSpentSeconds: number;
  domainPerformance: Record<Domain, DomainPerformance>;
  subjectPerformance: Record<string, SubjectPerformance>;
  questionRecords: {
    question: Question;
    response: UserResponseState;
    isCorrect: boolean;
    scoreAwarded: number;
  }[];
}

// Spaced Repetition (SRS) Engine Types
export type SRSRating = 'again' | 'hard' | 'good' | 'easy';
export type SRSStatus = 'new' | 'learning' | 'review' | 'mastered';

export interface SRSRecord {
  questionId: string;
  intervalDays: number;
  repetition: number;
  easeFactor: number;
  dueDate: number; // timestamp in ms
  lastReviewed: number; // timestamp in ms
  status: SRSStatus;
  timesCorrect: number;
  timesIncorrect: number;
}

export interface SRSMetrics {
  dueToday: number;
  learning: number;
  review: number;
  mastered: number;
  totalEnrolled: number;
}

// Drill Test Types
export type DrillPreset =
  | 'lightning_10'
  | 'standard_20'
  | 'deep_30'
  | 'weak_blitz'
  | 'clinical_blitz'
  | 'animal_blitz'
  | 'custom';

export type DrillFeedbackMode = 'instant' | 'exam';

export interface DrillConfig {
  preset: DrillPreset;
  title: string;
  totalQuestions: number;
  durationMinutes: number;
  feedbackMode: DrillFeedbackMode;
  selectedSubjectIds?: string[];
}

// Daily Goal & Streak Tracking
export interface DailyProgress {
  date: string;
  questionsSolvedToday: number;
  dailyTarget: number;
  streakDays: number;
  lastActiveDate: string;
}

export type NavigationTab = 
  | 'dashboard' 
  | 'cbt_config' 
  | 'drill_test' 
  | 'spaced_repetition' 
  | 'question_bank' 
  | 'analytics' 
  | 'summary';

