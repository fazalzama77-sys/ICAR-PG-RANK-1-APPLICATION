import React, { useState } from 'react';
import { ShieldCheck, Sliders, CheckCircle2, AlertCircle, BookOpen, Clock, Play } from 'lucide-react';
import { Question, TestConfig, Domain, AcademicYear } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';

interface TestConfigModalProps {
  questions: Question[];
  onStartExam: (config: TestConfig, selectedQuestions: Question[]) => void;
  onNavigateToBank: () => void;
  preSelectedQuestions?: Question[] | null;
}

export const TestConfigModal: React.FC<TestConfigModalProps> = ({
  questions,
  onStartExam,
  onNavigateToBank,
  preSelectedQuestions
}) => {
  // Mode: full_mock (120 Qs, 120 mins) or custom_practice
  const [mode, setMode] = useState<'full_mock' | 'custom_practice'>('full_mock');
  const [title, setTitle] = useState<string>('ICAR AIEEA PG (M.V.Sc.) CBT Mock Exam');
  
  // Custom settings
  const [questionCount, setQuestionCount] = useState<number>(120);
  const [durationMinutes, setDurationMinutes] = useState<number>(120);
  const [isUntimed, setIsUntimed] = useState<boolean>(false);

  const [selectedDomains, setSelectedDomains] = useState<Domain[]>([
    'veterinary_science',
    'animal_science'
  ]);

  const [selectedYears, setSelectedYears] = useState<AcademicYear[]>([
    '1st_year',
    '2nd_year'
  ]);

  const [selectedSubjectIds, setSelectedSubjectIds] = useState<string[]>(
    SUBJECT_LIST.filter(s => s.year === '1st_year' || s.year === '2nd_year').map(s => s.id)
  );

  const [positiveMarks, setPositiveMarks] = useState<number>(4);
  const [negativeMarks, setNegativeMarks] = useState<number>(1);
  const [shuffleQuestions, setShuffleQuestions] = useState<boolean>(true);

  // Toggle domain
  const toggleDomain = (domain: Domain) => {
    if (selectedDomains.includes(domain)) {
      if (selectedDomains.length > 1) {
        setSelectedDomains(selectedDomains.filter(d => d !== domain));
      }
    } else {
      setSelectedDomains([...selectedDomains, domain]);
    }
  };

  // Toggle year
  const toggleYear = (year: AcademicYear) => {
    if (selectedYears.includes(year)) {
      if (selectedYears.length > 1) {
        setSelectedYears(selectedYears.filter(y => y !== year));
      }
    } else {
      setSelectedYears([...selectedYears, year]);
    }
  };

  // Toggle individual subject
  const toggleSubject = (subjectId: string) => {
    if (selectedSubjectIds.includes(subjectId)) {
      if (selectedSubjectIds.length > 1) {
        setSelectedSubjectIds(selectedSubjectIds.filter(id => id !== subjectId));
      }
    } else {
      setSelectedSubjectIds([...selectedSubjectIds, subjectId]);
    }
  };

  const selectAllSubjects = () => {
    const relevant = SUBJECT_LIST.filter(
      s => selectedDomains.includes(s.domain) && selectedYears.includes(s.year)
    ).map(s => s.id);
    setSelectedSubjectIds(relevant);
  };

  // Available matching questions
  const availablePool = preSelectedQuestions || questions.filter(q => {
    const matchesDomain = selectedDomains.includes(q.domain);
    const matchesYear = selectedYears.includes(q.year);
    const matchesSubject = selectedSubjectIds.includes(q.subjectId);
    return matchesDomain && matchesYear && matchesSubject;
  });

  const handleLaunch = () => {
    if (availablePool.length === 0) {
      alert('No questions in your Question Bank match your selected criteria. Please add questions first or select different subjects.');
      return;
    }

    let pool = [...availablePool];
    if (shuffleQuestions) {
      pool.sort(() => Math.random() - 0.5);
    }

    // Limit to requested question count (or total available)
    const effectiveQCount = mode === 'full_mock' 
      ? Math.min(120, pool.length)
      : Math.min(questionCount, pool.length);

    const testQuestions = pool.slice(0, effectiveQCount);

    const config: TestConfig = {
      mode,
      title: mode === 'full_mock' ? 'ICAR AIEEA PG (M.V.Sc.) Full CBT Mock Exam' : (title.trim() || 'ICAR PG Practice Drill'),
      totalQuestions: testQuestions.length,
      durationMinutes: isUntimed ? 0 : (mode === 'full_mock' ? 120 : durationMinutes),
      selectedDomains,
      selectedYears,
      selectedSubjectIds,
      positiveMarks,
      negativeMarks,
      shuffleQuestions
    };

    onStartExam(config, testQuestions);
  };

  const firstYearSubjects = SUBJECT_LIST.filter(s => s.year === '1st_year');
  const secondYearSubjects = SUBJECT_LIST.filter(s => s.year === '2nd_year');

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Title Header */}
      <div>
        <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight flex items-center space-x-2.5">
          <ShieldCheck className="w-7 h-7 text-emerald-600" />
          <span>Launch CBT Examination</span>
        </h2>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          Configure an authentic NTA Computer Based Test with official 2-hour 120-question format or customized subject-wise practice.
        </p>
      </div>

      {/* Mode Selection Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Option 1: Official ICAR AIEEA PG Full Mock */}
        <div
          onClick={() => {
            setMode('full_mock');
            setQuestionCount(120);
            setDurationMinutes(120);
            setIsUntimed(false);
          }}
          className={`p-5 rounded-xl border-2 transition-all cursor-pointer relative ${
            mode === 'full_mock'
              ? 'bg-emerald-50/70 border-emerald-600 shadow-md ring-1 ring-emerald-500'
              : 'bg-white border-slate-200 hover:border-slate-300 shadow-xs'
          }`}
        >
          {mode === 'full_mock' && (
            <div className="absolute top-4 right-4 text-emerald-600">
              <CheckCircle2 className="w-5 h-5" />
            </div>
          )}
          <div className="flex items-center space-x-2 mb-2">
            <span className="bg-emerald-600 text-white text-[11px] font-bold px-2 py-0.5 rounded uppercase">
              Recommended
            </span>
            <span className="text-xs font-bold text-slate-700">Official Exam Format</span>
          </div>
          <h3 className="font-extrabold text-slate-900 text-base sm:text-lg">
            Full 120-Question ICAR PG Mock Exam
          </h3>
          <p className="text-xs text-slate-600 mt-1.5 leading-relaxed">
            Exact replica of the entrance test: 120 questions across Veterinary Science and Animal Science, 120 minutes (2 Hours), +4 for correct, -1 for negative marking.
          </p>
          <div className="mt-4 flex items-center space-x-4 text-xs font-semibold text-slate-700">
            <span className="flex items-center space-x-1">
              <Clock className="w-3.5 h-3.5 text-slate-500" />
              <span>120 Minutes</span>
            </span>
            <span>&bull;</span>
            <span>120 MCQs</span>
            <span>&bull;</span>
            <span>Total Marks: 480</span>
          </div>
        </div>

        {/* Option 2: Custom Practice Drill */}
        <div
          onClick={() => setMode('custom_practice')}
          className={`p-5 rounded-xl border-2 transition-all cursor-pointer relative ${
            mode === 'custom_practice'
              ? 'bg-emerald-50/70 border-emerald-600 shadow-md ring-1 ring-emerald-500'
              : 'bg-white border-slate-200 hover:border-slate-300 shadow-xs'
          }`}
        >
          {mode === 'custom_practice' && (
            <div className="absolute top-4 right-4 text-emerald-600">
              <CheckCircle2 className="w-5 h-5" />
            </div>
          )}
          <div className="flex items-center space-x-2 mb-2">
            <span className="bg-blue-600 text-white text-[11px] font-bold px-2 py-0.5 rounded uppercase">
              Customizable
            </span>
            <span className="text-xs font-bold text-slate-700">Targeted Revision</span>
          </div>
          <h3 className="font-extrabold text-slate-900 text-base sm:text-lg">
            Custom Subject &amp; Speed Practice
          </h3>
          <p className="text-xs text-slate-600 mt-1.5 leading-relaxed">
            Choose exact number of questions (e.g. 20, 30, 50), custom timer or untimed, and focus specifically on 1st or 2nd year subjects you are currently studying.
          </p>
          <div className="mt-4 flex items-center space-x-4 text-xs font-semibold text-slate-700">
            <span className="flex items-center space-x-1">
              <Sliders className="w-3.5 h-3.5 text-slate-500" />
              <span>Custom Time &amp; Qs</span>
            </span>
            <span>&bull;</span>
            <span>Subject-wise Filters</span>
          </div>
        </div>
      </div>

      {/* Custom Configuration Panel */}
      {mode === 'custom_practice' && (
        <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6">
          <h4 className="font-bold text-slate-900 text-sm sm:text-base border-b border-slate-100 pb-3 flex items-center space-x-2">
            <Sliders className="w-4 h-4 text-emerald-600" />
            <span>Customize Your Practice Session</span>
          </h4>

          {/* Test Title */}
          <div>
            <label className="block text-xs font-bold uppercase text-slate-700 mb-1">
              Session Title
            </label>
            <input
              type="text"
              value={title}
              onChange={e => setTitle(e.target.value)}
              placeholder="e.g. 1st Year Anatomy & LPM Speed Test"
              className="w-full text-xs sm:text-sm px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:outline-hidden"
            />
          </div>

          {/* Questions Count and Duration */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label className="block text-xs font-bold uppercase text-slate-700 mb-2">
                Number of Questions ({questionCount})
              </label>
              <div className="flex items-center space-x-3 mb-2">
                {[10, 20, 30, 60, 120].map(val => (
                  <button
                    key={val}
                    type="button"
                    onClick={() => setQuestionCount(val)}
                    className={`px-3 py-1 rounded text-xs font-bold border transition-colors ${
                      questionCount === val
                        ? 'bg-emerald-600 text-white border-emerald-600'
                        : 'bg-slate-50 text-slate-700 border-slate-300 hover:bg-slate-100'
                    }`}
                  >
                    {val}
                  </button>
                ))}
              </div>
              <input
                type="range"
                min="5"
                max="120"
                step="5"
                value={questionCount}
                onChange={e => setQuestionCount(parseInt(e.target.value))}
                className="w-full accent-emerald-600 cursor-pointer"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase text-slate-700 mb-2">
                Time Limit ({isUntimed ? 'Untimed Practice' : `${durationMinutes} Minutes`})
              </label>
              <div className="flex items-center space-x-2 mb-2">
                <button
                  type="button"
                  onClick={() => { setIsUntimed(false); setDurationMinutes(15); }}
                  className={`px-2.5 py-1 rounded text-xs font-bold border ${!isUntimed && durationMinutes === 15 ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-slate-50 text-slate-700 border-slate-300'}`}
                >
                  15 min
                </button>
                <button
                  type="button"
                  onClick={() => { setIsUntimed(false); setDurationMinutes(30); }}
                  className={`px-2.5 py-1 rounded text-xs font-bold border ${!isUntimed && durationMinutes === 30 ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-slate-50 text-slate-700 border-slate-300'}`}
                >
                  30 min
                </button>
                <button
                  type="button"
                  onClick={() => { setIsUntimed(false); setDurationMinutes(60); }}
                  className={`px-2.5 py-1 rounded text-xs font-bold border ${!isUntimed && durationMinutes === 60 ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-slate-50 text-slate-700 border-slate-300'}`}
                >
                  60 min
                </button>
                <button
                  type="button"
                  onClick={() => { setIsUntimed(false); setDurationMinutes(120); }}
                  className={`px-2.5 py-1 rounded text-xs font-bold border ${!isUntimed && durationMinutes === 120 ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-slate-50 text-slate-700 border-slate-300'}`}
                >
                  120 min
                </button>
                <button
                  type="button"
                  onClick={() => setIsUntimed(true)}
                  className={`px-2.5 py-1 rounded text-xs font-bold border ${isUntimed ? 'bg-emerald-600 text-white border-emerald-600' : 'bg-slate-50 text-slate-700 border-slate-300'}`}
                >
                  Untimed
                </button>
              </div>

              {!isUntimed && (
                <input
                  type="range"
                  min="5"
                  max="180"
                  step="5"
                  value={durationMinutes}
                  onChange={e => setDurationMinutes(parseInt(e.target.value))}
                  className="w-full accent-emerald-600 cursor-pointer"
                />
              )}
            </div>
          </div>

          {/* Marking Scheme */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-50 p-4 rounded-lg border border-slate-200">
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">
                Marks for Correct Answer (+{positiveMarks})
              </label>
              <input
                type="number"
                min="1"
                max="10"
                value={positiveMarks}
                onChange={e => setPositiveMarks(parseInt(e.target.value) || 4)}
                className="w-24 text-xs font-bold px-2 py-1.5 border border-slate-300 rounded bg-white"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">
                Negative Marks for Wrong Answer (-{negativeMarks})
              </label>
              <input
                type="number"
                min="0"
                max="5"
                value={negativeMarks}
                onChange={e => setNegativeMarks(parseInt(e.target.value) || 0)}
                className="w-24 text-xs font-bold px-2 py-1.5 border border-slate-300 rounded bg-white"
              />
              <span className="text-[11px] text-slate-500 ml-2 font-normal">(Set 0 to disable negative marking)</span>
            </div>
          </div>
        </div>
      )}

      {/* Domain & Subject Filters */}
      <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
          <div>
            <h4 className="font-bold text-slate-900 text-sm sm:text-base">
              Target Domains &amp; Subject Selection
            </h4>
            <p className="text-xs text-slate-500">
              Pick subjects based on your 1st and 2nd year preparation syllabus.
            </p>
          </div>

          <button
            type="button"
            onClick={selectAllSubjects}
            className="text-xs font-bold text-emerald-700 hover:text-emerald-800 underline"
          >
            Select All 1st &amp; 2nd Year Subjects
          </button>
        </div>

        {/* Domain Toggles */}
        <div className="flex flex-wrap gap-3">
          <button
            type="button"
            onClick={() => toggleDomain('veterinary_science')}
            className={`px-4 py-2 rounded-lg text-xs font-bold border transition-colors flex items-center space-x-2 ${
              selectedDomains.includes('veterinary_science')
                ? 'bg-blue-600 text-white border-blue-600 shadow-2xs'
                : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-50'
            }`}
          >
            <span>Veterinary Science Domain</span>
            {selectedDomains.includes('veterinary_science') && <span>✓</span>}
          </button>

          <button
            type="button"
            onClick={() => toggleDomain('animal_science')}
            className={`px-4 py-2 rounded-lg text-xs font-bold border transition-colors flex items-center space-x-2 ${
              selectedDomains.includes('animal_science')
                ? 'bg-teal-600 text-white border-teal-600 shadow-2xs'
                : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-50'
            }`}
          >
            <span>Animal Science Domain</span>
            {selectedDomains.includes('animal_science') && <span>✓</span>}
          </button>
        </div>

        {/* Year Groups: 1st Year & 2nd Year */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
          {/* 1st Professional Year Subjects */}
          <div className="p-4 rounded-xl border border-indigo-100 bg-indigo-50/30 space-y-3">
            <div className="flex items-center justify-between">
              <span className="font-bold text-xs uppercase tracking-wider text-indigo-900">
                1st Professional Year Subjects
              </span>
              <span className="text-[10px] bg-indigo-200 text-indigo-800 font-bold px-2 py-0.5 rounded">
                Completed Year
              </span>
            </div>

            <div className="space-y-2">
              {firstYearSubjects.map(sub => {
                const isSelected = selectedSubjectIds.includes(sub.id);
                return (
                  <label
                    key={sub.id}
                    className={`flex items-center justify-between p-2 rounded border cursor-pointer select-none text-xs transition-colors ${
                      isSelected
                        ? 'bg-white border-indigo-400 font-semibold text-slate-800 shadow-2xs'
                        : 'bg-white/60 border-slate-200 text-slate-500 hover:bg-white'
                    }`}
                  >
                    <div className="flex items-center space-x-2">
                      <input
                        type="checkbox"
                        checked={isSelected}
                        onChange={() => toggleSubject(sub.id)}
                        className="rounded text-indigo-600 focus:ring-indigo-500"
                      />
                      <span>{sub.name} ({sub.code})</span>
                    </div>
                    <span className="text-[10px] text-slate-400 capitalize">
                      {sub.domain === 'veterinary_science' ? 'Vet Sci' : 'Animal Sci'}
                    </span>
                  </label>
                );
              })}
            </div>
          </div>

          {/* 2nd Professional Year Subjects */}
          <div className="p-4 rounded-xl border border-purple-100 bg-purple-50/30 space-y-3">
            <div className="flex items-center justify-between">
              <span className="font-bold text-xs uppercase tracking-wider text-purple-900">
                2nd Professional Year Subjects
              </span>
              <span className="text-[10px] bg-purple-200 text-purple-800 font-bold px-2 py-0.5 rounded">
                Current Year
              </span>
            </div>

            <div className="space-y-2">
              {secondYearSubjects.map(sub => {
                const isSelected = selectedSubjectIds.includes(sub.id);
                return (
                  <label
                    key={sub.id}
                    className={`flex items-center justify-between p-2 rounded border cursor-pointer select-none text-xs transition-colors ${
                      isSelected
                        ? 'bg-white border-purple-400 font-semibold text-slate-800 shadow-2xs'
                        : 'bg-white/60 border-slate-200 text-slate-500 hover:bg-white'
                    }`}
                  >
                    <div className="flex items-center space-x-2">
                      <input
                        type="checkbox"
                        checked={isSelected}
                        onChange={() => toggleSubject(sub.id)}
                        className="rounded text-purple-600 focus:ring-purple-500"
                      />
                      <span>{sub.name} ({sub.code})</span>
                    </div>
                    <span className="text-[10px] text-slate-400 capitalize">
                      {sub.domain === 'veterinary_science' ? 'Vet Sci' : 'Animal Sci'}
                    </span>
                  </label>
                );
              })}
            </div>
          </div>
        </div>
      </div>

      {/* Summary Banner & Launch CTA */}
      <div className="bg-gradient-to-r from-[#1f3f60] to-[#2b547e] rounded-xl p-6 text-white shadow-md flex flex-wrap items-center justify-between gap-4">
        <div className="space-y-1">
          <div className="flex items-center space-x-2">
            <span className="text-amber-300 font-bold text-xs tracking-wider uppercase">Ready for Examination</span>
            <span>&bull;</span>
            <span className="text-xs text-slate-200">
              Matching Questions in Pool: <span className="font-bold text-white font-mono">{availablePool.length}</span>
            </span>
          </div>
          <h3 className="font-extrabold text-lg text-white">
            {mode === 'full_mock'
              ? 'ICAR AIEEA PG (M.V.Sc.) Official CBT Exam Replica'
              : `${questionCount} Qs &bull; ${isUntimed ? 'Untimed' : `${durationMinutes} Mins`} &bull; Custom Drill`}
          </h3>
          <p className="text-xs text-slate-200 max-w-xl">
            {availablePool.length === 0
              ? 'Your Question Bank has no questions matching the selected subjects yet. Add questions or import sample MCQs to test.'
              : `Launching with ${Math.min(availablePool.length, mode === 'full_mock' ? 120 : questionCount)} questions in official NTA interface.`}
          </p>
        </div>

        <div className="flex items-center space-x-3">
          {availablePool.length === 0 ? (
            <button
              type="button"
              onClick={onNavigateToBank}
              className="bg-amber-400 hover:bg-amber-500 text-slate-900 font-bold text-xs sm:text-sm px-5 py-2.5 rounded-lg shadow-sm flex items-center space-x-2 transition-transform transform active:scale-98"
            >
              <BookOpen className="w-4 h-4" />
              <span>Go to Question Bank to Add MCQs</span>
            </button>
          ) : (
            <button
              type="button"
              onClick={handleLaunch}
              className="bg-emerald-500 hover:bg-emerald-600 text-white font-black text-sm sm:text-base px-6 py-3 rounded-lg shadow-lg flex items-center space-x-2 transition-transform transform active:scale-98 cursor-pointer"
            >
              <Play className="w-5 h-5 fill-current" />
              <span>Start CBT Exam Now</span>
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
