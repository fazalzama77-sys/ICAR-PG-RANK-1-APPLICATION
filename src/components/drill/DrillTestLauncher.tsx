import React, { useState } from 'react';
import { 
  Zap, 
  Flame, 
  Clock, 
  Sliders, 
  CheckCircle2, 
  Play, 
  ArrowLeft,
  AlertTriangle,
  Sparkles,
  BookOpen,
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
  const [selectedSubjectIds, setSelectedSubjectIds] = useState<string[]>(
    SUBJECT_LIST.map(s => s.id)
  );

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
        setSelectedSubjectIds(selectedSubjectIds.filter(s => s !== id));
      }
    } else {
      setSelectedSubjectIds([...selectedSubjectIds, id]);
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
        pool = questions.filter(q => ['lpm', 'agb', 'ann'].includes(q.subjectId));
        break;
      case 'custom':
        title = '⚙️ Custom Rapid Drill';
        qCount = customCount;
        duration = customDuration;
        pool = questions.filter(q => selectedSubjectIds.includes(q.subjectId));
        break;
    }

    if (pool.length === 0) {
      alert('No questions in your bank match this drill selection. Please select different subjects or add questions.');
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
        selectedSubjectIds
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

          {/* Preset 4: Paraclinical Blitz */}
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

          {/* Preset 6: Custom Drill */}
          <div
            onClick={() => setSelectedPreset('custom')}
            className={`p-4 rounded-xl border-2 cursor-pointer transition-all ${
              selectedPreset === 'custom'
                ? 'border-emerald-600 bg-emerald-50/60 shadow-xs ring-1 ring-emerald-500'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <span className="bg-slate-700 text-white text-[10px] font-black px-2 py-0.5 rounded uppercase">
                Customized
              </span>
              <Sliders className="w-4 h-4 text-slate-500" />
            </div>
            <h4 className="font-bold text-slate-900 text-sm">⚙️ Custom Drill Settings</h4>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">
              Configure your own question count, duration, and subject filters.
            </p>
          </div>

        </div>

        {/* Custom Settings Panel */}
        {selectedPreset === 'custom' && (
          <div className="pt-4 border-t border-slate-200 space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  Question Count ({customCount} Qs)
                </label>
                <input
                  type="range"
                  min="5"
                  max="50"
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
                  max="45"
                  step="5"
                  value={customDuration}
                  onChange={e => setCustomDuration(parseInt(e.target.value))}
                  className="w-full accent-emerald-600 cursor-pointer"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 mb-2">
                Included Subjects:
              </label>
              <div className="flex flex-wrap gap-2">
                {SUBJECT_LIST.map(sub => {
                  const isSelected = selectedSubjectIds.includes(sub.id);
                  return (
                    <button
                      key={sub.id}
                      type="button"
                      onClick={() => toggleSubject(sub.id)}
                      className={`px-2.5 py-1 rounded text-xs font-bold border transition-colors ${
                        isSelected
                          ? 'bg-emerald-600 text-white border-emerald-600'
                          : 'bg-slate-50 text-slate-600 border-slate-200 hover:bg-slate-100'
                      }`}
                    >
                      {sub.code} - {sub.name}
                    </button>
                  );
                })}
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
