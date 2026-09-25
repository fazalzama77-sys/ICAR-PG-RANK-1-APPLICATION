import { Question } from '../../types';
import masterQuestions from './high_yield_master_clean.json';

export { ALL_ICAR_PG_PYQ_QUESTIONS } from './pyqQuestions';
export const ALL_HIGH_YIELD_QUESTIONS: Question[] = masterQuestions as unknown as Question[];
