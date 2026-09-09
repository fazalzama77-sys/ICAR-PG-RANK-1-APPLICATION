import React, { useState } from 'react';
import { Plus, Search, Trash2, Edit3, BookOpen, ChevronDown, ChevronUp, Layers } from 'lucide-react';
import { Question, Domain, AcademicYear } from '../../types';
import { SUBJECT_LIST, DOMAIN_LABELS, YEAR_LABELS } from '../../data/subjects';
import { StorageService } from '../../storage/db';
import { AddQuestionModal } from './AddQuestionModal';
import { BulkImportExport } from './BulkImportExport';

interface QuestionBankViewProps {
  questions: Question[];
  onRefreshQuestions: () => void;
  onLaunchPracticeWithFiltered: (filtered: Question[]) => void;
}

export const QuestionBankView: React.FC<QuestionBankViewProps> = ({
  questions,
  onRefreshQuestions,
  onLaunchPracticeWithFiltered
}) => {
  const [selectedDomain, setSelectedDomain] = useState<string>('all');
  const [selectedYear, setSelectedYear] = useState<string>('all');
  const [selectedSubject, setSelectedSubject] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Add/Edit modal state
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingQuestion, setEditingQuestion] = useState<Question | null>(null);

  // Expanded explanations toggle tracker
  const [expandedQuestionIds, setExpandedQuestionIds] = useState<Record<string, boolean>>({});

  const toggleExplanation = (id: string) => {
    setExpandedQuestionIds(prev => ({ ...prev, [id]: !prev[id] }));
  };

  // Filter questions
  const filteredQuestions = questions.filter(q => {
    if (selectedDomain !== 'all' && q.domain !== selectedDomain) return false;
    if (selectedYear !== 'all' && q.year !== selectedYear) return false;
    if (selectedSubject !== 'all' && q.subjectId !== selectedSubject) return false;
    if (searchQuery.trim()) {
      const qText = q.questionText.toLowerCase();
      const topicText = (q.topic || '').toLowerCase();
      const tagsText = (q.tags || []).join(' ').toLowerCase();
      const query = searchQuery.toLowerCase();
      if (!qText.includes(query) && !topicText.includes(query) && !tagsText.includes(query)) {
        return false;
      }
    }
    return true;
  });

  // Handle Save Question
  const handleSaveQuestion = (q: Question) => {
    if (editingQuestion) {
      StorageService.updateQuestion(q);
    } else {
      StorageService.addQuestion(q);
    }
    setEditingQuestion(null);
    onRefreshQuestions();
  };

  // Handle Delete Question
  const handleDeleteQuestion = (id: string) => {
    if (window.confirm('Are you sure you want to delete this question from the Question Bank?')) {
      StorageService.deleteQuestion(id);
      onRefreshQuestions();
    }
  };

  // Handle Clear All Questions
  const handleClearAll = () => {
    if (window.confirm('Are you sure you want to delete ALL questions in your Question Bank? This cannot be undone.')) {
      StorageService.clearAllQuestions();
      onRefreshQuestions();
    }
  };

  // Counts
  const vetCount = questions.filter(q => q.domain === 'veterinary_science').length;
  const animalCount = questions.filter(q => q.domain === 'animal_science').length;
  const y1Count = questions.filter(q => q.year === '1st_year').length;
  const y2Count = questions.filter(q => q.year === '2nd_year').length;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      {/* Top Banner & Quick Stats */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight flex items-center space-x-2.5">
            <BookOpen className="w-6 h-6 text-emerald-600" />
            <span>Question Bank & Repository</span>
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
            Manage your high-yield ICAR AIEEA PG question collection across 1st & 2nd year subjects.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          {questions.length > 0 && (
            <button
              onClick={handleClearAll}
              className="text-xs text-red-600 hover:text-red-700 hover:bg-red-50 px-3 py-2 rounded-lg border border-red-200 font-medium transition-colors"
            >
              Clear Bank
            </button>
          )}

          <button
            onClick={() => {
              setEditingQuestion(null);
              setIsModalOpen(true);
            }}
            className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg shadow-sm flex items-center space-x-2 transition-colors"
          >
            <Plus className="w-4 h-4" />
            <span>Add Single MCQ</span>
          </button>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 sm:gap-4">
        <div className="bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs">
          <p className="text-xs font-semibold text-slate-500">Total in Bank</p>
          <p className="text-xl sm:text-2xl font-black text-slate-900 mt-1">{questions.length}</p>
        </div>
        <div className="bg-white p-3.5 rounded-xl border border-blue-200 shadow-2xs">
          <p className="text-xs font-semibold text-blue-700">Veterinary Science</p>
          <p className="text-xl sm:text-2xl font-black text-blue-900 mt-1">{vetCount}</p>
        </div>
        <div className="bg-white p-3.5 rounded-xl border border-teal-200 shadow-2xs">
          <p className="text-xs font-semibold text-teal-700">Animal Science</p>
          <p className="text-xl sm:text-2xl font-black text-teal-900 mt-1">{animalCount}</p>
        </div>
        <div className="bg-white p-3.5 rounded-xl border border-indigo-200 shadow-2xs">
          <p className="text-xs font-semibold text-indigo-700">1st Year Subjects</p>
          <p className="text-xl sm:text-2xl font-black text-indigo-900 mt-1">{y1Count}</p>
        </div>
        <div className="bg-white p-3.5 rounded-xl border border-purple-200 shadow-2xs">
          <p className="text-xs font-semibold text-purple-700">2nd Year Subjects</p>
          <p className="text-xl sm:text-2xl font-black text-purple-900 mt-1">{y2Count}</p>
        </div>
      </div>

      {/* Bulk Operations Component */}
      <BulkImportExport
        onQuestionsImported={onRefreshQuestions}
        currentQuestionCount={questions.length}
      />

      {/* Filter and Search Bar */}
      <div className="bg-white border border-slate-200 rounded-xl p-4 shadow-xs space-y-3">
        <div className="grid grid-cols-1 sm:grid-cols-4 gap-3">
          {/* Domain Filter */}
          <div>
            <label className="block text-[11px] font-bold uppercase text-slate-500 mb-1">Domain</label>
            <select
              value={selectedDomain}
              onChange={e => setSelectedDomain(e.target.value)}
              className="w-full text-xs bg-slate-50 border border-slate-300 rounded px-2.5 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
            >
              <option value="all">All Domains</option>
              <option value="veterinary_science">Veterinary Science</option>
              <option value="animal_science">Animal Science</option>
            </select>
          </div>

          {/* Year Filter */}
          <div>
            <label className="block text-[11px] font-bold uppercase text-slate-500 mb-1">Year</label>
            <select
              value={selectedYear}
              onChange={e => setSelectedYear(e.target.value)}
              className="w-full text-xs bg-slate-50 border border-slate-300 rounded px-2.5 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
            >
              <option value="all">All Years</option>
              <option value="1st_year">1st Professional Year</option>
              <option value="2nd_year">2nd Professional Year</option>
              <option value="3rd_year">3rd Professional Year</option>
            </select>
          </div>

          {/* Subject Filter */}
          <div>
            <label className="block text-[11px] font-bold uppercase text-slate-500 mb-1">Subject</label>
            <select
              value={selectedSubject}
              onChange={e => setSelectedSubject(e.target.value)}
              className="w-full text-xs bg-slate-50 border border-slate-300 rounded px-2.5 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
            >
              <option value="all">All Subjects</option>
              {SUBJECT_LIST.map(s => (
                <option key={s.id} value={s.id}>
                  {s.code} - {s.name}
                </option>
              ))}
            </select>
          </div>

          {/* Search */}
          <div>
            <label className="block text-[11px] font-bold uppercase text-slate-500 mb-1">Search Questions</label>
            <div className="relative">
              <input
                type="text"
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                placeholder="Search stem, topic, tag..."
                className="w-full text-xs bg-slate-50 border border-slate-300 rounded pl-8 pr-3 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
              />
              <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-2.5" />
            </div>
          </div>
        </div>

        {/* Filter summary & practice with current set */}
        <div className="flex flex-wrap items-center justify-between pt-2 border-t border-slate-100 text-xs text-slate-500">
          <div>
            Showing <span className="font-bold text-slate-800">{filteredQuestions.length}</span> of {questions.length} questions
          </div>

          {filteredQuestions.length > 0 && (
            <button
              onClick={() => onLaunchPracticeWithFiltered(filteredQuestions)}
              className="font-semibold text-emerald-700 hover:text-emerald-800 flex items-center space-x-1"
            >
              <span>Practice this filtered set ({filteredQuestions.length} Qs) in CBT</span>
              <Layers className="w-3.5 h-3.5" />
            </button>
          )}
        </div>
      </div>

      {/* Questions Listing */}
      {filteredQuestions.length === 0 ? (
        <div className="bg-white border border-dashed border-slate-300 rounded-xl p-12 text-center">
          <BookOpen className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <h3 className="font-bold text-slate-800 text-base">No Questions in Selected Filter</h3>
          <p className="text-xs text-slate-500 max-w-md mx-auto mt-1 mb-5">
            {questions.length === 0
              ? 'Your Question Bank is currently empty as requested. You can add questions one-by-one or import them in bulk.'
              : 'Try clearing your search query or subject filters to view more questions.'}
          </p>

          <div className="flex justify-center space-x-3">
            <button
              onClick={() => {
                setEditingQuestion(null);
                setIsModalOpen(true);
              }}
              className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-4 py-2 rounded-lg shadow-sm"
            >
              Add First MCQ
            </button>
          </div>
        </div>
      ) : (
        <div className="space-y-3.5">
          {filteredQuestions.map((q, idx) => {
            const subject = SUBJECT_LIST.find(s => s.id === q.subjectId);
            const isExpanded = !!expandedQuestionIds[q.id];

            return (
              <div
                key={q.id}
                className="bg-white border border-slate-200 rounded-xl p-4 sm:p-5 shadow-2xs hover:shadow-xs transition-shadow space-y-3"
              >
                {/* Meta Badges */}
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="flex flex-wrap items-center gap-1.5 text-[11px]">
                    <span className="font-mono font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">
                      #{idx + 1}
                    </span>
                    <span className={`font-semibold px-2 py-0.5 rounded ${
                      q.domain === 'veterinary_science' ? 'bg-blue-100 text-blue-800' : 'bg-teal-100 text-teal-800'
                    }`}>
                      {q.domain === 'veterinary_science' ? 'Veterinary Science' : 'Animal Science'}
                    </span>
                    <span className="bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-medium">
                      {subject ? subject.name : q.subjectId.toUpperCase()}
                    </span>
                    {q.topic && (
                      <span className="bg-amber-50 text-amber-800 px-2 py-0.5 rounded border border-amber-200">
                        {q.topic}
                      </span>
                    )}
                    <span className="text-slate-400">&bull;</span>
                    <span className="text-slate-500 capitalize">{q.difficulty || 'Medium'}</span>
                  </div>

                  {/* Actions (Edit / Delete) */}
                  <div className="flex items-center space-x-2">
                    <button
                      onClick={() => {
                        setEditingQuestion(q);
                        setIsModalOpen(true);
                      }}
                      className="p-1.5 text-slate-400 hover:text-blue-600 hover:bg-slate-100 rounded transition-colors"
                      title="Edit Question"
                    >
                      <Edit3 className="w-3.5 h-3.5" />
                    </button>
                    <button
                      onClick={() => handleDeleteQuestion(q.id)}
                      className="p-1.5 text-slate-400 hover:text-red-600 hover:bg-red-50 rounded transition-colors"
                      title="Delete Question"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>

                {/* Question Stem */}
                <p className="text-sm font-medium text-slate-900 leading-relaxed">
                  {q.questionText}
                </p>

                {/* 4 Options Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                  {q.options.map((opt, optIdx) => {
                    const isCorrect = q.correctOptionIndex === optIdx;
                    const letter = ['A', 'B', 'C', 'D'][optIdx];
                    return (
                      <div
                        key={optIdx}
                        className={`p-2 rounded border flex items-start space-x-2 ${
                          isCorrect
                            ? 'bg-emerald-50/80 border-emerald-300 text-emerald-900 font-semibold'
                            : 'bg-slate-50 border-slate-200 text-slate-700'
                        }`}
                      >
                        <span className={`font-bold px-1.5 py-0.2 rounded text-[10px] shrink-0 ${
                          isCorrect ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-600'
                        }`}>
                          {letter}
                        </span>
                        <span className="flex-1 leading-snug">{opt}</span>
                        {isCorrect && (
                          <span className="text-[10px] font-bold text-emerald-700 shrink-0">✓ Correct</span>
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* Toggle Explanation Button */}
                {q.explanation && (
                  <div>
                    <button
                      onClick={() => toggleExplanation(q.id)}
                      className="text-xs font-semibold text-slate-600 hover:text-slate-900 flex items-center space-x-1"
                    >
                      <span>{isExpanded ? 'Hide' : 'View'} High-Yield Concept / Explanation</span>
                      {isExpanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                    </button>

                    {isExpanded && (
                      <div className="mt-2 p-3 bg-amber-50/60 border border-amber-200 rounded text-xs text-slate-800 leading-relaxed">
                        <span className="font-bold text-amber-900 block mb-0.5">High-Yield Note:</span>
                        {q.explanation}
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* Add / Edit Question Modal */}
      <AddQuestionModal
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setEditingQuestion(null);
        }}
        onSave={handleSaveQuestion}
        initialQuestion={editingQuestion}
      />
    </div>
  );
};
