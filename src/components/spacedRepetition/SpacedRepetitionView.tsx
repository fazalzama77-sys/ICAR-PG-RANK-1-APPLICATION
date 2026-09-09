import React, { useState, useEffect, useCallback } from 'react';
import confetti from 'canvas-confetti';
import { 
  RotateCw, 
  CheckCircle2, 
  XCircle, 
  Sparkles, 
  ArrowLeft, 
  Flame 
} from 'lucide-react';
import { Question, SRSRating, SRSMetrics } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { StorageService } from '../../storage/db';

interface SpacedRepetitionViewProps {
  questions: Question[];
  onBackToDashboard: () => void;
  onRefreshData: () => void;
  initialSubjectFilter?: string | null;
}

export const SpacedRepetitionView: React.FC<SpacedRepetitionViewProps> = ({
  questions,
  onBackToDashboard,
  onRefreshData,
  initialSubjectFilter
}) => {
  // Deck Filters
  const [deckMode, setDeckMode] = useState<'due' | 'all' | 'learning' | 'mastered'>('due');
  const [selectedSubject, setSelectedSubject] = useState<string>(initialSubjectFilter || 'all');
  const [selectedDomain, setSelectedDomain] = useState<string>('all');

  const buildDeck = useCallback((mode: 'due' | 'all' | 'learning' | 'mastered', subj: string, dom: string) => {
    const srsData = StorageService.getDueQuestions(questions);
    let pool: Question[] = [];
    if (mode === 'due') {
      pool = srsData.due.length > 0 ? srsData.due : [...srsData.learning, ...srsData.unreviewed.slice(0, 30)];
    } else if (mode === 'learning') {
      pool = srsData.learning;
    } else if (mode === 'mastered') {
      pool = srsData.mastered;
    } else {
      pool = questions;
    }

    const filtered = pool.filter(q => {
      if (dom !== 'all' && q.domain !== dom) return false;
      if (subj !== 'all' && q.subjectId !== subj) return false;
      return true;
    });

    return [...filtered].sort(() => Math.random() - 0.5);
  }, [questions]);

  // Study Deck State
  const [activeDeck, setActiveDeck] = useState<Question[]>(() => 
    buildDeck('due', initialSubjectFilter || 'all', 'all')
  );
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [reviewedInSession, setReviewedInSession] = useState(0);
  const [sessionCompleted, setSessionCompleted] = useState(false);

  // SRS metrics cache
  const [srsMetrics, setSrsMetrics] = useState<SRSMetrics>(() => StorageService.getSRSMetrics(questions));
  const dailyProgress = StorageService.getDailyProgress();

  const handleDeckFilterChange = (newMode: 'due' | 'all' | 'learning' | 'mastered', newSubj: string, newDom: string) => {
    setDeckMode(newMode);
    setSelectedSubject(newSubj);
    setSelectedDomain(newDom);
    setSrsMetrics(StorageService.getSRSMetrics(questions));
    setActiveDeck(buildDeck(newMode, newSubj, newDom));
    setCurrentIndex(0);
    setIsFlipped(false);
    setSelectedOption(null);
    setSessionCompleted(false);
  };

  const handleRestartDeck = () => {
    setSrsMetrics(StorageService.getSRSMetrics(questions));
    setActiveDeck(buildDeck(deckMode, selectedSubject, selectedDomain));
    setCurrentIndex(0);
    setIsFlipped(false);
    setSelectedOption(null);
    setSessionCompleted(false);
  };

  const currentCard = activeDeck[currentIndex];
  const srsRecords = StorageService.getSRSRecords();
  const currentCardRecord = currentCard ? srsRecords[currentCard.id] : undefined;

  // Rating action handler
  const handleRate = useCallback((rating: SRSRating) => {
    if (!currentCard) return;

    StorageService.recordSRSReview(currentCard.id, rating);
    setReviewedInSession(prev => prev + 1);

    if (currentIndex + 1 < activeDeck.length) {
      setCurrentIndex(prev => prev + 1);
      setIsFlipped(false);
      setSelectedOption(null);
    } else {
      // End of deck
      setSessionCompleted(true);
      try {
        confetti({ particleCount: 70, spread: 60, origin: { y: 0.6 } });
      } catch {}
      onRefreshData();
    }
  }, [currentCard, currentIndex, activeDeck.length, onRefreshData]);

  // Keyboard shortcut listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (sessionCompleted || !currentCard) return;

      if (e.code === 'Space') {
        e.preventDefault();
        setIsFlipped(prev => !prev);
      } else if (isFlipped) {
        if (e.key === '1') handleRate('again');
        if (e.key === '2') handleRate('hard');
        if (e.key === '3') handleRate('good');
        if (e.key === '4') handleRate('easy');
      } else {
        // Option selection shortcuts A, B, C, D
        if (e.key === 'a' || e.key === 'A') setSelectedOption(0);
        if (e.key === 'b' || e.key === 'B') setSelectedOption(1);
        if (e.key === 'c' || e.key === 'C') setSelectedOption(2);
        if (e.key === 'd' || e.key === 'D') setSelectedOption(3);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isFlipped, currentCard, sessionCompleted, handleRate]);

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 space-y-6">
      
      {/* Top Breadcrumb & Controls */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBackToDashboard}
          className="flex items-center space-x-1.5 text-xs font-semibold text-slate-600 hover:text-slate-900 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Dashboard</span>
        </button>

        <div className="flex items-center space-x-3 text-xs">
          <span className="flex items-center space-x-1 bg-amber-50 text-amber-800 border border-amber-200 px-2.5 py-1 rounded-full font-bold">
            <Flame className="w-3.5 h-3.5 text-amber-500 fill-amber-500" />
            <span>{dailyProgress.streakDays} Day Streak</span>
          </span>
          <span className="text-slate-500">
            Today: <strong className="text-slate-800">{dailyProgress.questionsSolvedToday}</strong> / {dailyProgress.dailyTarget} Qs
          </span>
        </div>
      </div>

      {/* Hero / Deck Overview Card */}
      <div className="bg-gradient-to-r from-[#172e48] via-[#1f3f60] to-[#28537d] rounded-2xl p-5 sm:p-6 text-white shadow-md">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2">
              <span className="bg-indigo-400 text-slate-900 font-extrabold text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
                Active Recall &bull; SM-2 Engine
              </span>
              <span className="text-xs text-indigo-200 font-medium">Spaced Repetition System</span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-white mt-1">
              High-Yield Veterinary Flashcards
            </h1>
            <p className="text-xs text-slate-200 mt-1 max-w-xl">
              Cement long-term memory for anatomy, microbial stains, drug mechanisms, pathologies, and production formulas using optimal spaced repetition intervals.
            </p>
          </div>

          {/* Metric Pills */}
          <div className="flex items-center space-x-2 sm:space-x-3">
            <div className="bg-white/10 border border-white/15 px-3 py-2 rounded-xl text-center">
              <span className="text-[10px] text-amber-200 uppercase font-bold block">Due Today</span>
              <span className="text-lg font-black text-amber-300">{srsMetrics.dueToday}</span>
            </div>
            <div className="bg-white/10 border border-white/15 px-3 py-2 rounded-xl text-center">
              <span className="text-[10px] text-blue-200 uppercase font-bold block">Learning</span>
              <span className="text-lg font-black text-blue-300">{srsMetrics.learning}</span>
            </div>
            <div className="bg-white/10 border border-white/15 px-3 py-2 rounded-xl text-center">
              <span className="text-[10px] text-emerald-200 uppercase font-bold block">Mastered</span>
              <span className="text-lg font-black text-emerald-300">{srsMetrics.mastered}</span>
            </div>
          </div>
        </div>

        {/* Deck Filters Row */}
        <div className="mt-5 pt-4 border-t border-white/15 flex flex-wrap items-center justify-between gap-3 text-xs">
          <div className="flex items-center space-x-2">
            <button
              onClick={() => handleDeckFilterChange('due', selectedSubject, selectedDomain)}
              className={`px-3 py-1 rounded-lg font-bold transition-colors ${
                deckMode === 'due' ? 'bg-amber-400 text-slate-900 shadow-xs' : 'bg-white/10 text-white hover:bg-white/20'
              }`}
            >
              Due For Review ({srsMetrics.dueToday})
            </button>
            <button
              onClick={() => handleDeckFilterChange('all', selectedSubject, selectedDomain)}
              className={`px-3 py-1 rounded-lg font-bold transition-colors ${
                deckMode === 'all' ? 'bg-white text-slate-900 shadow-xs' : 'bg-white/10 text-white hover:bg-white/20'
              }`}
            >
              Full Question Deck ({questions.length})
            </button>
            <button
              onClick={() => handleDeckFilterChange('learning', selectedSubject, selectedDomain)}
              className={`px-3 py-1 rounded-lg font-bold transition-colors ${
                deckMode === 'learning' ? 'bg-blue-400 text-slate-900 shadow-xs' : 'bg-white/10 text-white hover:bg-white/20'
              }`}
            >
              Learning ({srsMetrics.learning})
            </button>
          </div>

          <div className="flex items-center space-x-2">
            <select
              value={selectedDomain}
              onChange={e => handleDeckFilterChange(deckMode, selectedSubject, e.target.value)}
              className="bg-slate-900/60 border border-white/20 text-white text-xs rounded-lg px-2.5 py-1 focus:outline-hidden"
            >
              <option value="all">All Domains</option>
              <option value="veterinary_science" className="text-slate-900">Veterinary Science</option>
              <option value="animal_science" className="text-slate-900">Animal Science</option>
            </select>

            <select
              value={selectedSubject}
              onChange={e => handleDeckFilterChange(deckMode, e.target.value, selectedDomain)}
              className="bg-slate-900/60 border border-white/20 text-white text-xs rounded-lg px-2.5 py-1 focus:outline-hidden"
            >
              <option value="all">All Subjects</option>
              {SUBJECT_LIST.map(s => (
                <option key={s.id} value={s.id} className="text-slate-900">
                  {s.code} - {s.name}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Main Flashcard View */}
      {sessionCompleted ? (
        <div className="bg-white border border-slate-200 rounded-2xl p-8 text-center space-y-4 shadow-sm">
          <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto shadow-inner">
            <Sparkles className="w-8 h-8" />
          </div>
          <h2 className="text-2xl font-black text-slate-900">Spaced Repetition Deck Completed!</h2>
          <p className="text-sm text-slate-600 max-w-md mx-auto">
            Outstanding dedication! You reviewed <strong className="text-slate-900">{reviewedInSession}</strong> cards in this session. Your optimal review intervals have been recalculated.
          </p>

          <div className="flex items-center justify-center gap-3 pt-3">
            <button
              onClick={handleRestartDeck}
              className="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs sm:text-sm rounded-lg shadow-sm flex items-center space-x-2 transition-colors"
            >
              <RotateCw className="w-4 h-4" />
              <span>Review Another Round</span>
            </button>

            <button
              onClick={onBackToDashboard}
              className="px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm rounded-lg transition-colors"
            >
              Return to Dashboard
            </button>
          </div>
        </div>
      ) : activeDeck.length === 0 ? (
        <div className="bg-white border border-dashed border-slate-300 rounded-2xl p-10 text-center space-y-3">
          <CheckCircle2 className="w-12 h-12 text-emerald-500 mx-auto" />
          <h3 className="text-lg font-bold text-slate-900">All Caught Up! No Cards Due</h3>
          <p className="text-xs text-slate-500 max-w-sm mx-auto">
            You have reviewed all due cards for the current filter. Switch to "Full Question Deck" to practice ahead of schedule or take a Drill Test.
          </p>
          <div className="flex justify-center gap-2 pt-2">
            <button
              onClick={() => setDeckMode('all')}
              className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-xs font-bold transition-colors"
            >
              Review All Cards
            </button>
          </div>
        </div>
      ) : currentCard ? (
        <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden transition-all">
          
          {/* Progress bar */}
          <div className="bg-slate-100 h-1.5 w-full">
            <div 
              className="bg-emerald-500 h-1.5 transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / activeDeck.length) * 100}%` }}
            />
          </div>

          {/* Card Header */}
          <div className="p-4 sm:p-5 border-b border-slate-100 flex flex-wrap items-center justify-between gap-2 bg-slate-50/50">
            <div className="flex flex-wrap items-center gap-2">
              <span className="bg-emerald-100 text-emerald-800 text-[11px] font-bold px-2 py-0.5 rounded font-mono">
                {currentCard.subjectId.toUpperCase()}
              </span>
              <span className="text-xs font-bold text-slate-700">
                {SUBJECT_LIST.find(s => s.id === currentCard.subjectId)?.name || 'Subject'}
              </span>
              {currentCard.topic && (
                <span className="text-xs text-slate-400 font-medium">
                  &bull; {currentCard.topic}
                </span>
              )}
            </div>

            <div className="flex items-center space-x-2 text-xs font-semibold text-slate-500">
              {currentCardRecord && (
                <span className="text-[10px] bg-slate-200 text-slate-700 px-2 py-0.5 rounded">
                  Rep #{currentCardRecord.repetition} &bull; {currentCardRecord.intervalDays}d interval
                </span>
              )}
              <span className="font-mono text-slate-400">
                {currentIndex + 1} / {activeDeck.length}
              </span>
            </div>
          </div>

          {/* Card Body */}
          <div className="p-6 sm:p-8 space-y-6">
            <div className="space-y-2">
              <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 block">
                Recall Prompt
              </span>
              <h3 className="text-base sm:text-lg font-bold text-slate-900 leading-relaxed">
                {currentCard.questionText}
              </h3>
            </div>

            {/* Interactive Options (Pre-reveal active recall check) */}
            <div className="space-y-2.5">
              {currentCard.options.map((opt, idx) => {
                const isSelected = selectedOption === idx;
                const isCorrect = idx === currentCard.correctOptionIndex;

                let optionStyle = 'border-slate-200 hover:border-slate-300 hover:bg-slate-50 text-slate-700';
                if (isFlipped) {
                  if (isCorrect) {
                    optionStyle = 'border-emerald-500 bg-emerald-50 text-emerald-900 font-bold ring-1 ring-emerald-500';
                  } else if (isSelected) {
                    optionStyle = 'border-red-400 bg-red-50 text-red-800 line-through';
                  } else {
                    optionStyle = 'border-slate-200 opacity-60 text-slate-500';
                  }
                } else if (isSelected) {
                  optionStyle = 'border-indigo-500 bg-indigo-50 text-indigo-900 font-semibold ring-1 ring-indigo-500';
                }

                return (
                  <div
                    key={idx}
                    onClick={() => {
                      if (!isFlipped) setSelectedOption(idx);
                    }}
                    className={`p-3 sm:p-3.5 rounded-xl border text-xs sm:text-sm flex items-center justify-between cursor-pointer transition-all ${optionStyle}`}
                  >
                    <div className="flex items-center space-x-3">
                      <span className="w-6 h-6 rounded-full border border-current flex items-center justify-center font-bold text-xs shrink-0">
                        {String.fromCharCode(65 + idx)}
                      </span>
                      <span>{opt}</span>
                    </div>

                    {isFlipped && isCorrect && (
                      <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
                    )}
                    {isFlipped && isSelected && !isCorrect && (
                      <XCircle className="w-5 h-5 text-red-500 shrink-0" />
                    )}
                  </div>
                );
              })}
            </div>

            {/* Flip / Reveal Explanation Card */}
            {!isFlipped ? (
              <div className="pt-2 text-center">
                <button
                  onClick={() => setIsFlipped(true)}
                  className="w-full sm:w-auto px-8 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs sm:text-sm rounded-xl shadow-md transition-transform transform active:scale-98"
                >
                  <span>Reveal Correct Answer &amp; High-Yield Explanation</span>
                  <span className="text-[10px] opacity-75 ml-2 font-mono">(Spacebar)</span>
                </button>
              </div>
            ) : (
              <div className="bg-emerald-50/70 border border-emerald-200 rounded-xl p-5 space-y-2 animate-in fade-in duration-200">
                <div className="flex items-center space-x-2">
                  <span className="bg-emerald-600 text-white text-[10px] font-extrabold px-2 py-0.5 rounded uppercase">
                    High-Yield Explanation &bull; Official Reference
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-slate-800 leading-relaxed font-medium">
                  {currentCard.explanation}
                </p>
                {currentCard.tags && currentCard.tags.length > 0 && (
                  <div className="flex flex-wrap gap-1.5 pt-2">
                    {currentCard.tags.map((t, idx) => (
                      <span key={idx} className="text-[10px] bg-white text-emerald-700 border border-emerald-300 px-2 py-0.5 rounded-full font-medium">
                        #{t}
                      </span>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* SM-2 Recall Rating Controls */}
          {isFlipped && (
            <div className="bg-slate-50 border-t border-slate-200 p-4 sm:p-5">
              <p className="text-[11px] font-extrabold uppercase tracking-wider text-slate-500 text-center mb-3">
                Rate Your Recall Confidence:
              </p>
              
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 max-w-2xl mx-auto">
                {/* 1. Again */}
                <button
                  onClick={() => handleRate('again')}
                  className="p-3 rounded-xl border border-red-300 bg-red-50 hover:bg-red-100 text-red-800 text-center transition-colors shadow-2xs"
                >
                  <span className="font-black text-xs sm:text-sm block">Again</span>
                  <span className="text-[10px] text-red-600 font-medium block">&lt; 1 Day &bull; [1]</span>
                </button>

                {/* 2. Hard */}
                <button
                  onClick={() => handleRate('hard')}
                  className="p-3 rounded-xl border border-amber-300 bg-amber-50 hover:bg-amber-100 text-amber-800 text-center transition-colors shadow-2xs"
                >
                  <span className="font-black text-xs sm:text-sm block">Hard</span>
                  <span className="text-[10px] text-amber-600 font-medium block">+1 Day &bull; [2]</span>
                </button>

                {/* 3. Good */}
                <button
                  onClick={() => handleRate('good')}
                  className="p-3 rounded-xl border border-blue-300 bg-blue-50 hover:bg-blue-100 text-blue-800 text-center transition-colors shadow-2xs"
                >
                  <span className="font-black text-xs sm:text-sm block">Good</span>
                  <span className="text-[10px] text-blue-600 font-medium block">+3-6 Days &bull; [3]</span>
                </button>

                {/* 4. Easy */}
                <button
                  onClick={() => handleRate('easy')}
                  className="p-3 rounded-xl border border-emerald-300 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 text-center transition-colors shadow-2xs"
                >
                  <span className="font-black text-xs sm:text-sm block">Easy</span>
                  <span className="text-[10px] text-emerald-600 font-medium block">Mastered &bull; [4]</span>
                </button>
              </div>
            </div>
          )}

        </div>
      ) : null}

    </div>
  );
};
