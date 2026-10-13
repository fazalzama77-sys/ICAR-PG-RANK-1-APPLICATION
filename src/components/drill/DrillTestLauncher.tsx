import React, { useState } from 'react';
import { 
  Zap, 
  Clock, 
  Sliders, 
  CheckCircle2, 
  Play, 
  ArrowLeft,
  AlertTriangle,
  Sparkles,
  Layers
} from 'lucide-react';
import { Question, DrillConfig, DrillPreset, DrillFeedbackMode, TestConfig } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { StorageService } from '../../storage/db';

interface DrillTestLauncherProps {
  questions: Question[];
  onLaunchInstantDrill: (config: DrillConfig, selectedQuestions: Question[]) => void;
  onLaunchCbtExam: (config: TestConfig, selectedQuestions: Question[]) => void;
  onBackToDashboard: () => void;
}

export const DrillTestLauncher: React.FC<DrillTestLauncherProps> = ({
  questions,
  onLaunchInstantDrill,
  onLaunchCbtExam,
  onBackToDashboard
}) => {
  const [selectedPreset, setSelectedPreset] = useState<DrillPreset>('standard_20');
  const [feedbackMode, setFeedbackMode] = useState<DrillFeedbackMode>('instant');
  
  // Custom drill settings
  const [customCount, setCustomCount] = useState(20);
  const [customDuration, setCustomDuration] = useState(15);
  const [selectedSubjectIds, setSelectedSubjectIds] = useState<string[]>(['vpp']);
  const [selectedTopics, setSelectedTopics] = useState<string[]>([]);

  const testResults = StorageService.getTestResults();
  const srsRecords = StorageService.getSRSRecords();

  // Find missed question IDs from results and SRS
  const missedQIds = new Set<string>();
  testResults.forEach(res => {
    res.questionRecords.forEach(r => {
      if (!r.isCorrect && r.response.selectedOptionIndex !== null) {
        missedQIds.add(r.question.id);
      }
    });
  });
  Object.values(srsRecords).forEach(rec => {
    if (rec.timesIncorrect > 0) {
      missedQIds.add(rec.questionId);
    }
  });

  const toggleSubject = (id: string) => {
    if (selectedSubjectIds.includes(id)) {
      if (selectedSubjectIds.length > 1) {
        const nextSubjects = selectedSubjectIds.filter(s => s !== id);
        setSelectedSubjectIds(nextSubjects);
        const removedSub = SUBJECT_LIST.find(s => s.id === id);
        if (removedSub) {
          setSelectedTopics(prev => prev.filter(t => !removedSub.topics.includes(t)));
        }
      }
    } else {
      setSelectedSubjectIds([...selectedSubjectIds, id]);
    }
  };

  const selectSingleSubjectForUnits = (id: string) => {
    setSelectedPreset('custom');
    setSelectedSubjectIds([id]);
    setSelectedTopics([]);
  };

  const toggleTopic = (topic: string) => {
    if (selectedTopics.includes(topic)) {
      setSelectedTopics(selectedTopics.filter(t => t !== topic));
    } else {
      setSelectedTopics([...selectedTopics, topic]);
    }
  };

  const handleStartDrill = () => {
    let pool: Question[] = [];
    let title = 'ICAR PG Rapid Drill';
    let qCount = 20;
    let duration = 15;

    switch (selectedPreset) {
      case 'lightning_10':
        title = '⚡ Lightning 10-Q Fire Drill';
        qCount = 10;
        duration = 7;
        pool = [...questions];
        break;
      case 'standard_20':
        title = '🎯 Daily 20-Q Exam Standard Drill';
        qCount = 20;
        duration = 15;
        pool = [...questions];
        break;
      case 'deep_30':
        title = '🔥 Deep Focus 30-Q Drill';
        qCount = 30;
        duration = 25;
        pool = [...questions];
        break;
      case 'weak_blitz':
        title = '🛡️ Weak Areas Blitz Drill';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => missedQIds.has(q.id));
        if (pool.length < 5) {
          // If not enough missed questions, pull from 2nd year paraclinical core
          pool = questions.filter(q => ['vpp', 'vmc', 'vpa'].includes(q.subjectId));
        }
        break;
      case 'vet_science_blitz':
        title = '🩺 Veterinary Science Core Blitz (VAN, VPP, VMC, VPA)';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => q.domain === 'veterinary_science' || ['van', 'vpp', 'vmc', 'vpa'].includes(q.subjectId));
        break;
      case 'clinical_blitz':
        title = '🔬 Paraclinical & Diagnostic Blitz (VPP, VMC, VPA)';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => ['vpp', 'vmc', 'vpa'].includes(q.subjectId));
        break;
      case 'animal_blitz':
        title = '🐄 Animal Science & Production Blitz (LPM, AGB, ANN)';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => q.domain === 'animal_science' || ['lpm', 'agb', 'ann'].includes(q.subjectId));
        break;
      case 'custom':
        qCount = customCount;
        duration = customDuration;
        pool = questions.filter(q => {
          if (!selectedSubjectIds.includes(q.subjectId)) return false;
          if (selectedTopics.length > 0 && (!q.topic || !selectedTopics.includes(q.topic))) return false;
          return true;
        });
        if (selectedTopics.length === 1) {
          title = `📚 Unit Drill: ${selectedTopics[0]}`;
        } else if (selectedTopics.length > 1) {
          title = `📚 Custom Multi-Unit Drill (${selectedTopics.length} Units)`;
        } else if (selectedSubjectIds.length === 1) {
          const sObj = SUBJECT_LIST.find(s => s.id === selectedSubjectIds[0]);
          title = `⚙️ ${sObj ? sObj.name : 'Subject'} Rapid Drill`;
        } else {
          title = '⚙️ Custom Rapid Drill';
        }
        break;
    }

    if (pool.length === 0) {
      alert('No questions in your bank match this drill selection. Please select different subjects/units or add questions.');
      return;
    }

    // Shuffle and pick
    const shuffled = [...pool].sort(() => Math.random() - 0.5);
    const selectedQuestions = shuffled.slice(0, Math.min(qCount, shuffled.length));

    if (feedbackMode === 'instant') {
      const drillConfig: DrillConfig = {
        preset: selectedPreset,
        title,
        totalQuestions: selectedQuestions.length,
        durationMinutes: duration,
        feedbackMode: 'instant',
        selectedSubjectIds,
        selectedTopics: selectedTopics.length > 0 ? selectedTopics : undefined
      };
      onLaunchInstantDrill(drillConfig, selectedQuestions);
    } else {
      // Launch as CBT Exam Mode
      const cbtConfig: TestConfig = {
        mode: 'custom_practice',
        title,
        totalQuestions: selectedQuestions.length,
        durationMinutes: duration,
        selectedDomains: ['veterinary_science', 'animal_science'],
        selectedYears: ['1st_year', '2nd_year'],
        selectedSubjectIds,
        selectedTopics: selectedTopics.length > 0 ? selectedTopics : undefined,
        positiveMarks: 4,
        negativeMarks: 1,
        shuffleQuestions: true
      };
      onLaunchCbtExam(cbtConfig, selectedQuestions);
    }
  };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8 space-y-8">
      
      {/* Top Header */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBackToDashboard}
          className="flex items-center space-x-1.5 text-xs font-semibold text-slate-600 hover:text-slate-900 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Dashboard</span>
        </button>

        <span className="text-xs bg-amber-100 text-amber-900 font-bold px-2.5 py-0.5 rounded-full border border-amber-300">
          Daily Rapid Testing Habit
        </span>
      </div>

      {/* Hero */}
      <div className="bg-gradient-to-r from-[#172e48] via-[#1f3f60] to-[#28537d] rounded-2xl p-6 sm:p-8 text-white shadow-md">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="space-y-2">
            <div className="flex items-center space-x-2">
              <span className="bg-amber-400 text-slate-950 font-black text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
                AIR 1 Daily Discipline
              </span>
              <span className="text-xs text-slate-300">Context: Section 7 Practice Recommendations</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-black tracking-tight">
              Rapid Drill Test Engine
            </h1>
            <p className="text-xs sm:text-sm text-slate-200 max-w-xl leading-relaxed">
              Build speed, negative marking discipline, and instantaneous recall with 10 to 30 question high-intensity practice drills.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-xs p-4 rounded-xl border border-white/15 text-center min-w-[160px]">
            <span className="text-[10px] text-amber-200 uppercase font-bold block">Available Bank</span>
            <span className="text-2xl font-black text-white">{questions.length} MCQs</span>
            <span className="text-[11px] text-slate-300 block mt-1">9 Core Subjects</span>
          </div>
        </div>
      </div>

      {/* 1. Mode Selector: Instant Feedback vs Timed Exam */}
      <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-xs space-y-3">
        <h3 className="font-extrabold text-slate-900 text-sm sm:text-base flex items-center space-x-2">
          <span>Step 1: Choose Feedback Mode</span>
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {/* Instant Feedback Mode */}
          <div
            onClick={() => setFeedbackMode('instant')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              feedbackMode === 'instant'
                ? 'border-amber-500 bg-amber-50/50 shadow-xs'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-1.5">
              <div className="flex items-center space-x-2">
                <span className="w-2.5 h-2.5 rounded-full bg-amber-500" />
                <h4 className="font-black text-slate-900 text-sm">Interactive Active Learning</h4>
              </div>
              {feedbackMode === 'instant' && <CheckCircle2 className="w-4 h-4 text-amber-600" />}
            </div>
            <p className="text-xs text-slate-600 leading-relaxed">
              See the correct answer, negative mark calculation, and textbook explanation <strong>immediately</strong> after answering each question. Best for active learning and revision.
            </p>
          </div>

          {/* Timed CBT Mode */}
          <div
            onClick={() => setFeedbackMode('exam')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              feedbackMode === 'exam'
                ? 'border-emerald-600 bg-emerald-50/50 shadow-xs'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-1.5">
              <div className="flex items-center space-x-2">
                <span className="w-2.5 h-2.5 rounded-full bg-emerald-600" />
                <h4 className="font-black text-slate-900 text-sm">Authentic Speed Test (CBT)</h4>
              </div>
              {feedbackMode === 'exam' && <CheckCircle2 className="w-4 h-4 text-emerald-600" />}
            </div>
            <p className="text-xs text-slate-600 leading-relaxed">
              Continuous countdown clock with the official NTA 5-state palette. Scorecard and comprehensive explanations are generated <strong>at the end</strong>.
            </p>
          </div>
        </div>
      </div>

      {/* 2. Drill Preset Selection */}
      <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-xs space-y-4">
        <h3 className="font-extrabold text-slate-900 text-sm sm:text-base">
          Step 2: Select Drill Preset
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          
          {/* Preset 1: Standard 20-Q */}
          <div
            onClick={() => setSelectedPreset('standard_20')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'standard_20'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-emerald-600 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Recommended Daily
              </span>
              <Clock className="w-4 h-4 text-slate-400" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">🎯 Daily 20-Q Standard</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              20 Questions across all 1st & 2nd year subjects. 15 Minutes timer.
            </p>
          </div>

          {/* Preset 2: Lightning 10-Q */}
          <div
            onClick={() => setSelectedPreset('lightning_10')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'lightning_10'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-amber-500 text-slate-950 text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Speed Fire
              </span>
              <Zap className="w-4 h-4 text-amber-500" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">⚡ Lightning 10-Q Drill</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              10 Questions in 7 Minutes. Perfect for rapid warm-ups and commute practice.
            </p>
          </div>

          {/* Preset 3: Weak Areas Blitz */}
          <div
            onClick={() => setSelectedPreset('weak_blitz')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'weak_blitz'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-red-500 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Targeted Weakness
              </span>
              <AlertTriangle className="w-4 h-4 text-red-500" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">🛡️ Weak Areas Blitz</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              Pulls questions you previously got wrong or subjects with lowest accuracy.
            </p>
          </div>

          {/* Preset 4: Veterinary Science Blitz */}
          <div
            onClick={() => setSelectedPreset('vet_science_blitz')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'vet_science_blitz'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-blue-600 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Veterinary Science
              </span>
              <Sparkles className="w-4 h-4 text-blue-500" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">🩺 Vet Science Core</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              Comprehensive Anatomy, Pathology, Microbiology & Parasitology (Code 13).
            </p>
          </div>

          {/* Preset 5: Animal Science Blitz */}
          <div
            onClick={() => setSelectedPreset('animal_blitz')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'animal_blitz'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-teal-600 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Animal Science
              </span>
              <Layers className="w-4 h-4 text-teal-500" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">🐄 Animal Science Core</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              LPM housing norms, Genetics & Breeding calculations, and Animal Nutrition.
            </p>
          </div>

          {/* Preset 6: Paraclinical Blitz */}
          <div
            onClick={() => setSelectedPreset('clinical_blitz')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'clinical_blitz'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-purple-600 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                2nd Year Core
              </span>
              <Sparkles className="w-4 h-4 text-purple-500" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">🔬 Paraclinical Trio</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              High-weightage Pathology, Microbiology & Parasitology questions.
            </p>
          </div>

          {/* Preset 7: Chapter / Unit & Custom Drill */}
          <div
            onClick={() => setSelectedPreset('custom')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all sm:col-span-2 lg:col-span-3 ${
              selectedPreset === 'custom'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-1.5">
              <span className="bg-emerald-700 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Chapter / Unit-Wise &amp; Custom
              </span>
              <Sliders className="w-4 h-4 text-emerald-700" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">📚 Chapter / Unit-Wise &amp; Custom Subject Drill</h4>
            <p className="text-xs text-slate-600 mt-1 leading-relaxed">
              Target a specific chapter or syllabus unit (e.g., <em>General Pathology</em>, <em>Systemic Pathology</em>, <em>General Bacteriology</em>, <em>Mendelian Genetics</em>, or <em>Proximate Analysis</em>) — ideal when starting 2nd year!
            </p>
          </div>

        </div>

        {/* Custom & Chapter-Wise Settings Panel */}
        {selectedPreset === 'custom' && (
          <div className="pt-4 border-t border-slate-200 space-y-5">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  Question Count ({customCount} Qs)
                </label>
                <input
                  type="range"
                  min="5"
                  max="60"
                  step="5"
                  value={customCount}
                  onChange={e => setCustomCount(parseInt(e.target.value))}
                  className="w-full accent-emerald-600 cursor-pointer"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  Time Limit ({customDuration} Mins)
                </label>
                <input
                  type="range"
                  min="5"
                  max="60"
                  step="5"
                  value={customDuration}
                  onChange={e => setCustomDuration(parseInt(e.target.value))}
                  className="w-full accent-emerald-600 cursor-pointer"
                />
              </div>
            </div>

            <div>
              <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                <label className="block text-xs font-bold text-slate-700">
                  Step 2A: Choose Subject(s) (Click a subject to focus on its Chapters/Units):
                </label>
                <button
                  type="button"
                  onClick={() => {
                    setSelectedSubjectIds(SUBJECT_LIST.map(s => s.id));
                    setSelectedTopics([]);
                  }}
                  className="text-[11px] font-bold text-emerald-700 hover:underline"
                >
                  Select All Subjects
                </button>
              </div>
              <div className="flex flex-wrap gap-2">
                {SUBJECT_LIST.map(sub => {
                  const isSelected = selectedSubjectIds.includes(sub.id);
                  const count = questions.filter(q => q.subjectId === sub.id).length;
                  return (
                    <div key={sub.id} className="inline-flex items-center rounded-lg border overflow-hidden shadow-2xs">
                      <button
                        type="button"
                        onClick={() => selectSingleSubjectForUnits(sub.id)}
                        className={`px-2.5 py-1.5 text-xs font-bold transition-colors cursor-pointer ${
                          isSelected
                            ? 'bg-emerald-600 text-white'
                            : 'bg-slate-50 text-slate-700 hover:bg-slate-100'
                        }`}
                        title="Focus exclusively on this subject and its chapters"
                      >
                        {sub.code} - {sub.name} ({count})
                      </button>
                      <button
                        type="button"
                        onClick={() => toggleSubject(sub.id)}
                        className={`px-2 py-1.5 text-[10px] font-extrabold border-l transition-colors cursor-pointer ${
                          isSelected
                            ? 'bg-emerald-700 text-emerald-100 border-emerald-500'
                            : 'bg-white text-slate-400 border-slate-200 hover:text-slate-700'
                        }`}
                        title="Toggle subject in multi-subject selection"
                      >
                        {isSelected ? '✓' : '+'}
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Step 2B: Syllabus Units / Chapters (Subsections) */}
            <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 space-y-3">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div>
                  <h5 className="text-xs font-extrabold uppercase tracking-wider text-slate-800 flex items-center space-x-1.5">
                    <Layers className="w-3.5 h-3.5 text-emerald-600" />
                    <span>Step 2B: Select Specific Chapters / Syllabus Units (Optional)</span>
                  </h5>
                  <p className="text-[11px] text-slate-500 mt-0.5">
                    {selectedTopics.length === 0
                      ? 'All chapters of the selected subject(s) are currently included. Check specific units below to practice only those chapters!'
                      : `Filtering strictly to ${selectedTopics.length} selected chapter(s)/unit(s).`}
                  </p>
                </div>
                {selectedTopics.length > 0 && (
                  <button
                    type="button"
                    onClick={() => setSelectedTopics([])}
                    className="text-xs font-bold text-amber-700 hover:text-amber-900 underline cursor-pointer"
                  >
                    Clear Unit Filter (Include All Chapters)
                  </button>
                )}
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3 max-h-96 overflow-y-auto pr-1">
                {SUBJECT_LIST.filter(s => selectedSubjectIds.includes(s.id)).map(sub => (
                  <div key={sub.id} className="bg-white rounded-lg border border-slate-200 p-3 space-y-2">
                    <div className="flex items-center justify-between border-b border-slate-100 pb-1.5">
                      <span className="font-extrabold text-xs text-slate-900">
                        {sub.name} ({sub.code})
                      </span>
                      <span className="text-[10px] font-semibold text-slate-400">
                        {sub.topics.length} Units
                      </span>
                    </div>
                    <div className="space-y-1.5">
                      {sub.topics.map((unitName, idx) => {
                        const isChecked = selectedTopics.includes(unitName);
                        const uCount = questions.filter(q => q.subjectId === sub.id && q.topic === unitName).length;
                        return (
                          <label
                            key={unitName}
                            className={`flex items-start justify-between gap-2 p-2 rounded-lg border text-xs cursor-pointer transition-colors ${
                              isChecked
                                ? 'bg-emerald-50 border-emerald-500 text-emerald-950 font-bold'
                                : 'bg-slate-50/60 border-slate-200 text-slate-700 hover:bg-slate-100/70'
                            }`}
                          >
                            <div className="flex items-start space-x-2">
                              <input
                                type="checkbox"
                                checked={isChecked}
                                onChange={() => toggleTopic(unitName)}
                                className="mt-0.5 rounded text-emerald-600 focus:ring-emerald-500"
                              />
                              <span className="leading-snug">
                                <span className="text-[10px] font-extrabold uppercase text-emerald-700 mr-1">
                                  Unit {idx + 1}:
                                </span>
                                {unitName}
                              </span>
                            </div>
                            <span className="text-[10px] font-mono font-bold bg-white px-1.5 py-0.5 rounded border border-slate-200 shrink-0">
                              {uCount} Qs
                            </span>
                          </label>
                        );
                      })}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Launch CTA */}
      <div className="bg-gradient-to-r from-[#1f3f60] to-[#2b547e] rounded-xl p-6 text-white shadow-md flex flex-wrap items-center justify-between gap-4">
        <div>
          <span className="text-amber-300 font-extrabold text-xs uppercase tracking-wider block">
            Ready to Drill
          </span>
          <h3 className="font-extrabold text-lg text-white">
            {feedbackMode === 'instant' ? 'Interactive Active Learning Drill' : 'Authentic Timed CBT Drill'}
          </h3>
          <p className="text-xs text-slate-200 mt-0.5">
            Evaluate negative marking control and retain concepts effortlessly.
          </p>
        </div>

        <button
          onClick={handleStartDrill}
          className="px-6 py-3 bg-amber-400 hover:bg-amber-500 text-slate-950 font-black text-sm sm:text-base rounded-xl shadow-lg flex items-center space-x-2 transition-transform transform active:scale-98 cursor-pointer"
        >
          <Play className="w-5 h-5 fill-current" />
          <span>Start Drill Test Now</span>
        </button>
      </div>

    </div>
  );
};
