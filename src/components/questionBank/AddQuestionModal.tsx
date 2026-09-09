import React, { useState } from 'react';
import { X, Plus, BookOpen, Check } from 'lucide-react';
import { Question, Domain, AcademicYear } from '../../types';
import { SUBJECT_LIST, DOMAIN_LABELS, YEAR_LABELS } from '../../data/subjects';

interface AddQuestionModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSave: (question: Question) => void;
  initialQuestion?: Question | null;
}

export const AddQuestionModal: React.FC<AddQuestionModalProps> = ({
  isOpen,
  onClose,
  onSave,
  initialQuestion
}) => {
  const [domain, setDomain] = useState<Domain>(initialQuestion?.domain || 'veterinary_science');
  const [year, setYear] = useState<AcademicYear>(initialQuestion?.year || '1st_year');
  const [subjectId, setSubjectId] = useState<string>(
    initialQuestion?.subjectId || (domain === 'veterinary_science' ? 'van' : 'lpm')
  );
  const [topic, setTopic] = useState<string>(initialQuestion?.topic || '');
  const [questionText, setQuestionText] = useState<string>(initialQuestion?.questionText || '');
  const [options, setOptions] = useState<[string, string, string, string]>(
    initialQuestion?.options || ['', '', '', '']
  );
  const [correctOptionIndex, setCorrectOptionIndex] = useState<number>(
    initialQuestion ? initialQuestion.correctOptionIndex : 0
  );
  const [explanation, setExplanation] = useState<string>(initialQuestion?.explanation || '');
  const [difficulty, setDifficulty] = useState<'Easy' | 'Medium' | 'Hard'>(
    initialQuestion?.difficulty || 'Medium'
  );
  const [tagsString, setTagsString] = useState<string>(
    initialQuestion?.tags?.join(', ') || ''
  );

  if (!isOpen) return null;

  // Filter subjects based on selected Domain and Year
  const availableSubjects = SUBJECT_LIST.filter(
    s => s.domain === domain && s.year === year
  );

  // If currently selected subject does not match the filtered list, pick the first available
  const handleDomainChange = (newDomain: Domain) => {
    setDomain(newDomain);
    const validSubs = SUBJECT_LIST.filter(s => s.domain === newDomain && s.year === year);
    if (validSubs.length > 0) {
      setSubjectId(validSubs[0].id);
    }
  };

  const handleYearChange = (newYear: AcademicYear) => {
    setYear(newYear);
    const validSubs = SUBJECT_LIST.filter(s => s.domain === domain && s.year === newYear);
    if (validSubs.length > 0) {
      setSubjectId(validSubs[0].id);
    }
  };

  const handleOptionChange = (index: number, val: string) => {
    const updated: [string, string, string, string] = [...options] as [string, string, string, string];
    updated[index] = val;
    setOptions(updated);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!questionText.trim()) {
      alert('Please provide the question text.');
      return;
    }

    if (options.some(opt => !opt.trim())) {
      alert('Please fill in all 4 option choices.');
      return;
    }

    const tags = tagsString
      .split(',')
      .map(t => t.trim())
      .filter(t => t.length > 0);

    const newQuestion: Question = {
      id: initialQuestion?.id || 'q_' + Date.now() + '_' + Math.random().toString(36).substr(2, 7),
      domain,
      year,
      subjectId,
      topic: topic.trim() || undefined,
      questionText: questionText.trim(),
      options: [options[0].trim(), options[1].trim(), options[2].trim(), options[3].trim()],
      correctOptionIndex,
      explanation: explanation.trim(),
      difficulty,
      tags,
      createdAt: initialQuestion?.createdAt || Date.now()
    };

    onSave(newQuestion);
    onClose();
  };

  const selectedSubjectData = SUBJECT_LIST.find(s => s.id === subjectId);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-4 overflow-y-auto">
      <div className="bg-white rounded-xl shadow-2xl max-w-3xl w-full max-h-[92vh] flex flex-col border border-slate-200">
        {/* Modal Header */}
        <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center shadow-xs">
              <BookOpen className="w-4 h-4" />
            </div>
            <div>
              <h3 className="font-bold text-slate-900 text-base">
                {initialQuestion ? 'Edit MCQ' : 'Add New MCQ to Question Bank'}
              </h3>
              <p className="text-xs text-slate-500">ICAR PG Standard Multiple Choice Question</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-md text-slate-400 hover:text-slate-600 hover:bg-slate-200 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Scrollable Form */}
        <form onSubmit={handleSubmit} className="flex-1 overflow-y-auto p-6 space-y-5">
          {/* Classification: Domain & Year */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 bg-slate-50 p-3.5 rounded-lg border border-slate-200">
            {/* Domain */}
            <div>
              <label className="block text-xs font-bold uppercase text-slate-600 mb-1">
                Domain
              </label>
              <select
                value={domain}
                onChange={e => handleDomainChange(e.target.value as Domain)}
                className="w-full text-xs font-medium bg-white border border-slate-300 rounded px-2.5 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
              >
                <option value="veterinary_science">{DOMAIN_LABELS.veterinary_science}</option>
                <option value="animal_science">{DOMAIN_LABELS.animal_science}</option>
              </select>
            </div>

            {/* Academic Year */}
            <div>
              <label className="block text-xs font-bold uppercase text-slate-600 mb-1">
                Professional Year
              </label>
              <select
                value={year}
                onChange={e => handleYearChange(e.target.value as AcademicYear)}
                className="w-full text-xs font-medium bg-white border border-slate-300 rounded px-2.5 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
              >
                <option value="1st_year">{YEAR_LABELS['1st_year']}</option>
                <option value="2nd_year">{YEAR_LABELS['2nd_year']}</option>
                <option value="3rd_year">{YEAR_LABELS['3rd_year']}</option>
              </select>
            </div>

            {/* Subject */}
            <div>
              <label className="block text-xs font-bold uppercase text-slate-600 mb-1">
                Subject
              </label>
              <select
                value={subjectId}
                onChange={e => setSubjectId(e.target.value)}
                className="w-full text-xs font-medium bg-white border border-slate-300 rounded px-2.5 py-1.5 focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
              >
                {availableSubjects.map(sub => (
                  <option key={sub.id} value={sub.id}>
                    {sub.name} ({sub.code})
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Topic & Difficulty */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="sm:col-span-2">
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Topic / Sub-discipline
              </label>
              <input
                type="text"
                list="topic-suggestions"
                value={topic}
                onChange={e => setTopic(e.target.value)}
                placeholder="e.g., Osteology, General Pathology, Coccidia, Feed Evaluation"
                className="w-full text-xs sm:text-sm px-3 py-1.5 border border-slate-300 rounded focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
              />
              <datalist id="topic-suggestions">
                {selectedSubjectData?.topics.map((t, idx) => (
                  <option key={idx} value={t} />
                ))}
              </datalist>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Difficulty Level
              </label>
              <select
                value={difficulty}
                onChange={e => setDifficulty(e.target.value as 'Easy' | 'Medium' | 'Hard')}
                className="w-full text-xs sm:text-sm px-3 py-1.5 bg-white border border-slate-300 rounded focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
              >
                <option value="Easy">Easy (Recall / Direct Fact)</option>
                <option value="Medium">Medium (Conceptual / Applied)</option>
                <option value="Hard">Hard (Assertion-Reason / Numerical)</option>
              </select>
            </div>
          </div>

          {/* Question Text */}
          <div>
            <label className="block text-xs font-semibold text-slate-800 mb-1">
              Question Statement <span className="text-red-500">*</span>
            </label>
            <textarea
              required
              rows={3}
              value={questionText}
              onChange={e => setQuestionText(e.target.value)}
              placeholder="Type the question statement here... Supports scientific formulas, clinical vignettes, and statements."
              className="w-full text-xs sm:text-sm px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-emerald-500 focus:outline-hidden font-normal"
            />
          </div>

          {/* 4 Options */}
          <div>
            <label className="block text-xs font-semibold text-slate-800 mb-2">
              Answer Options & Correct Choice <span className="text-red-500">*</span>
            </label>
            <div className="space-y-2.5">
              {(['A', 'B', 'C', 'D'] as const).map((letter, idx) => {
                const isCorrect = correctOptionIndex === idx;
                return (
                  <div
                    key={idx}
                    className={`flex items-center space-x-2.5 p-2 rounded-md border transition-colors ${
                      isCorrect ? 'bg-emerald-50 border-emerald-400 ring-1 ring-emerald-300' : 'bg-white border-slate-300'
                    }`}
                  >
                    <label className="flex items-center cursor-pointer space-x-1.5 shrink-0">
                      <input
                        type="radio"
                        name="correct_choice_radio"
                        checked={isCorrect}
                        onChange={() => setCorrectOptionIndex(idx)}
                        className="w-4 h-4 text-emerald-600 focus:ring-emerald-500 cursor-pointer"
                      />
                      <span className={`text-xs font-bold px-2 py-0.5 rounded ${
                        isCorrect ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-700'
                      }`}>
                        Option {letter} {isCorrect && '✓ (Correct)'}
                      </span>
                    </label>
                    <input
                      type="text"
                      required
                      value={options[idx]}
                      onChange={e => handleOptionChange(idx, e.target.value)}
                      placeholder={`Enter text for Option ${letter}...`}
                      className="flex-1 text-xs sm:text-sm px-2.5 py-1 border border-slate-300 rounded focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
                    />
                  </div>
                );
              })}
            </div>
          </div>

          {/* Detailed Explanation */}
          <div>
            <label className="block text-xs font-semibold text-slate-800 mb-1">
              Detailed Explanation / Reference
            </label>
            <textarea
              rows={3}
              value={explanation}
              onChange={e => setExplanation(e.target.value)}
              placeholder="Explain why this is correct, key high-yield points, reference textbook chapter, or mnemonic..."
              className="w-full text-xs sm:text-sm px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
            />
          </div>

          {/* Tags */}
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Tags / Keywords (comma separated)
            </label>
            <input
              type="text"
              value={tagsString}
              onChange={e => setTagsString(e.target.value)}
              placeholder="e.g. Splanchnology, Spleen, Ruminant, High-Yield"
              className="w-full text-xs px-3 py-1.5 border border-slate-300 rounded focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
            />
          </div>

          {/* Form Actions */}
          <div className="flex items-center justify-end space-x-3 pt-3 border-t border-slate-200">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-xs font-medium text-slate-600 hover:bg-slate-100 rounded-lg"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-5 py-2 text-xs font-bold text-white bg-emerald-600 hover:bg-emerald-700 rounded-lg shadow-sm flex items-center space-x-1.5"
            >
              <Check className="w-4 h-4" />
              <span>{initialQuestion ? 'Update Question' : 'Save Question to Bank'}</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
