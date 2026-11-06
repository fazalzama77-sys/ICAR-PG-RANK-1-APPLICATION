import React, { useState } from 'react';
import { 
  Zap, 
  Clock, 
  CheckCircle2, 
  Play, 
  ArrowLeft,
  Sparkles,
  Layers,
  Flame,
  ShieldAlert,
  Brain,
  Sliders,
  Award
} from 'lucide-react';
import { Question, DrillConfig, DrillPreset, DrillFeedbackMode, TestConfig } from '../../types';
import { SUBJECT_LIST } from '../../data/subjects';
import { StorageService } from '../../storage/db';
import { soundFx } from '../../utils/soundEffects';

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
    soundFx.playPop();
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

  const toggleTopic = (topic: string) => {
    soundFx.playPop();
    if (selectedTopics.includes(topic)) {
      setSelectedTopics(selectedTopics.filter(t => t !== topic));
    } else {
      setSelectedTopics([...selectedTopics, topic]);
    }
  };

  const handleStartDrill = () => {
    soundFx.playCorrect();
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
        title = '🎯 Daily 20-Q Champion Drill';
        qCount = 20;
        duration = 15;
        pool = [...questions];
        break;
      case 'deep_30':
        title = '🔥 Deep Focus 30-Q Marathon';
        qCount = 30;
        duration = 25;
        pool = [...questions];
        break;
      case 'weak_blitz':
        title = '🛡️ Mistake Buster Drill';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => missedQIds.has(q.id));
        if (pool.length < 5) {
          // If not enough missed questions, pull from paraclinical core
          pool = questions.filter(q => ['vpp', 'vmc', 'vpa'].includes(q.subjectId));
        }
        break;
      case 'vet_science_blitz':
        title = '🩺 Veterinary Science Core Blitz';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => q.domain === 'veterinary_science' || ['van', 'vpp', 'vmc', 'vpa'].includes(q.subjectId));
        break;
      case 'clinical_blitz':
        title = '🔬 Paraclinical Core Blitz';
        qCount = 20;
        duration = 15;
        pool = questions.filter(q => ['vpp', 'vmc', 'vpa'].includes(q.subjectId));
        break;
      case 'animal_blitz':
        title = '🐄 Animal Science Core Blitz';
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
          title = `📚 Chapter Quiz: ${selectedTopics[0]}`;
        } else if (selectedTopics.length > 1) {
          title = `📚 Custom Quiz (${selectedTopics.length} Chapters)`;
        } else if (selectedSubjectIds.length === 1) {
          const sObj = SUBJECT_LIST.find(s => s.id === selectedSubjectIds[0]);
          title = `⚙️ ${sObj ? sObj.name : 'Subject'} Quiz`;
        } else {
          title = '⚙️ Custom Rapid Quiz';
        }
        break;
    }

    if (pool.length === 0) {
      alert('No questions in your bank match this selection. Please pick different subjects or chapters.');
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

  // Preset Card definition
  const presetCards = [
    {
      id: 'standard_20' as DrillPreset,
      title: 'Daily Champion Drill',
      count: '20 Questions',
      time: '15 Mins',
      desc: 'The official ICAR PG daily standard. Tests all subjects with high-yield questions.',
      icon: '🎯',
      gradient: 'from-emerald-500 to-teal-600',
      badge: 'RECOMMENDED',
      bgLight: 'bg-emerald-50/70 border-emerald-300'
    },
    {
      id: 'lightning_10' as DrillPreset,
      title: 'Lightning Fire Drill',
      count: '10 Questions',
      time: '7 Mins',
      desc: 'Quick rapid-fire test! Perfect for a fast 5-minute break or before bed.',
      icon: '⚡',
      gradient: 'from-amber-500 to-orange-600',
      badge: 'SPEED BOOST',
      bgLight: 'bg-amber-50/70 border-amber-300'
    },
    {
      id: 'deep_30' as DrillPreset,
      title: 'Deep Focus Marathon',
      count: '30 Questions',
      time: '25 Mins',
      desc: 'High-intensity session testing clinical diagnostic acumen and numericals.',
      icon: '🔥',
      gradient: 'from-indigo-500 to-purple-600',
      badge: 'MASTERY',
      bgLight: 'bg-indigo-50/70 border-indigo-300'
    },
    {
      id: 'weak_blitz' as DrillPreset,
      title: 'Mistake Buster Drill',
      count: '20 Questions',
      time: '15 Mins',
      desc: 'Targeted drill pulling exclusively from questions you answered incorrectly.',
      icon: '🛡️',
      gradient: 'from-rose-500 to-pink-600',
      badge: 'FIX MISTAKES',
      bgLight: 'bg-rose-50/70 border-rose-300'
    },
    {
      id: 'vet_science_blitz' as DrillPreset,
      title: 'Veterinary Science Core',
      count: '20 Questions',
      time: '15 Mins',
      desc: 'Focus exclusively on Anatomy, Pathology, Microbiology, and Parasitology (Code 13).',
      icon: '🩺',
      gradient: 'from-blue-500 to-cyan-600',
      badge: 'CODE 13',
      bgLight: 'bg-blue-50/70 border-blue-300'
    },
    {
      id: 'animal_blitz' as DrillPreset,
      title: 'Animal Sciences Core',
      count: '20 Questions',
      time: '15 Mins',
      desc: 'Focus on Genetics, Animal Nutrition, Physiology, Biochemistry, and LPM (Code 14).',
      icon: '🐄',
      gradient: 'from-teal-500 to-emerald-600',
      badge: 'CODE 14',
      bgLight: 'bg-teal-50/70 border-teal-300'
    },
    {
      id: 'custom' as DrillPreset,
      title: 'Custom Adventure',
      count: 'Custom Qs',
      time: 'Custom Time',
      desc: 'Choose your own subjects, specific syllabus chapters, time limits, and question count.',
      icon: '🎨',
      gradient: 'from-violet-500 to-fuchsia-600',
      badge: 'CUSTOM',
      bgLight: 'bg-violet-50/70 border-violet-300'
    }
  ];

  return (
    <div className="max-w-5xl mx-auto px-3.5 sm:px-6 py-6 sm:py-8 space-y-6 sm:space-y-8 pb-24 md:pb-12">
      
      {/* Top Header Navigation */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBackToDashboard}
          className="flex items-center space-x-2 text-xs sm:text-sm font-bold text-slate-600 hover:text-slate-900 bg-white border border-slate-200 px-3.5 py-1.5 rounded-xl shadow-2xs transition-transform active:scale-95 cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Dashboard</span>
        </button>

        <span className="text-xs bg-amber-100 text-amber-900 font-black px-3 py-1 rounded-full border border-amber-300 shadow-2xs">
          3,125 MCQs Bank Ready ⚡
        </span>
      </div>

      {/* Hero Banner */}
      <div className="bg-gradient-to-br from-[#122840] via-[#1c3d5f] to-[#25527a] rounded-3xl p-6 sm:p-8 text-white shadow-xl border border-white/10 relative overflow-hidden">
        <div className="absolute -top-20 -right-20 w-60 h-60 rounded-full bg-amber-400/15 blur-3xl pointer-events-none" />
        <div className="absolute -bottom-20 -left-20 w-60 h-60 rounded-full bg-emerald-400/15 blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-5">
          <div className="space-y-2 max-w-xl">
            <span className="bg-amber-400 text-slate-950 font-black text-[10px] sm:text-[11px] px-2.5 py-0.5 rounded-full uppercase tracking-wider shadow-2xs">
              AIR 1 Rapid Quiz Arcade
            </span>
            <h1 className="text-2xl sm:text-4xl font-black tracking-tight leading-tight">
              Pick Your Quiz &amp; Play! 🚀
            </h1>
            <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
              Fast, playful, interactive testing with instantaneous feedback, sound chimes, and streak rewards. Choose a quick preset below or build a custom chapter adventure!
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-md p-4 rounded-2xl border border-white/15 text-center min-w-[170px] shrink-0">
            <span className="text-[10px] text-amber-200 uppercase font-black block">Questions Bank</span>
            <span className="text-3xl font-black text-white">{questions.length}</span>
            <span className="text-[11px] text-emerald-300 font-bold block mt-0.5">54 Syllabus Chapters</span>
          </div>
        </div>
      </div>

      {/* 1. Mode Selector: Interactive Quiz vs Timed Mock */}
      <div className="bg-white border-2 border-slate-200/90 rounded-3xl p-5 shadow-sm space-y-3">
        <h3 className="font-black text-slate-900 text-sm sm:text-base flex items-center space-x-2">
          <span>1. How Do You Want to Play?</span>
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
          
          {/* Interactive Quiz Mode */}
          <div
            onClick={() => {
              soundFx.playPop();
              setFeedbackMode('instant');
            }}
            className={`p-4.5 rounded-2xl border-2 cursor-pointer transition-all active:scale-[0.99] ${
              feedbackMode === 'instant'
                ? 'border-amber-500 bg-amber-50/70 shadow-sm ring-4 ring-amber-500/10'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-1.5">
              <div className="flex items-center space-x-2">
                <span className="text-xl">🎮</span>
                <h4 className="font-black text-slate-900 text-sm sm:text-base">
                  Interactive Quiz Mode
                </h4>
              </div>
              {feedbackMode === 'instant' && <CheckCircle2 className="w-5 h-5 text-amber-600" />}
            </div>
            <p className="text-xs text-slate-600 leading-relaxed font-medium">
              Instant answers, cheerful audio chimes, 50:50 lifelines, and streak bonuses after every question!
            </p>
          </div>

          {/* Timed Mock Drill Mode */}
          <div
            onClick={() => {
              soundFx.playPop();
              setFeedbackMode('exam');
            }}
            className={`p-4.5 rounded-2xl border-2 cursor-pointer transition-all active:scale-[0.99] ${
              feedbackMode === 'exam'
                ? 'border-emerald-600 bg-emerald-50/70 shadow-sm ring-4 ring-emerald-500/10'
                : 'border-slate-200 hover:border-slate-300 bg-white'
            }`}
          >
            <div className="flex items-center justify-between mb-1.5">
              <div className="flex items-center space-x-2">
                <span className="text-xl">⏱️</span>
                <h4 className="font-black text-slate-900 text-sm sm:text-base">
                  Timed Exam Mode
                </h4>
              </div>
              {feedbackMode === 'exam' && <CheckCircle2 className="w-5 h-5 text-emerald-600" />}
            </div>
            <p className="text-xs text-slate-600 leading-relaxed font-medium">
              Continuous countdown clock with the official NTA palette. Scorecard generated at the end.
            </p>
          </div>

        </div>
      </div>

      {/* 2. Choose Game Mode Presets */}
      <div className="space-y-3">
        <h3 className="font-black text-slate-900 text-sm sm:text-base">
          2. Choose Your Drill Mode
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          {presetCards.map(preset => {
            const isSelected = selectedPreset === preset.id;
            return (
              <div
                key={preset.id}
                onClick={() => {
                  soundFx.playPop();
                  setSelectedPreset(preset.id);
                }}
                className={`p-4 rounded-2xl border-2 cursor-pointer transition-all flex flex-col justify-between space-y-3 active:scale-[0.98] ${
                  isSelected 
                    ? `border-indigo-600 bg-indigo-50/70 shadow-md ring-4 ring-indigo-500/15`
                    : 'border-slate-200/90 hover:border-slate-300 bg-white shadow-2xs'
                }`}
              >
                <div>
                  <div className="flex items-start justify-between gap-2">
                    <span className="text-2xl p-2 rounded-xl bg-slate-100 shadow-2xs">
                      {preset.icon}
                    </span>
                    <span className={`text-[10px] font-black px-2 py-0.5 rounded-full uppercase border ${
                      isSelected ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-slate-100 text-slate-700 border-slate-200'
                    }`}>
                      {preset.badge}
                    </span>
                  </div>

                  <h4 className="font-black text-slate-900 text-base mt-2">
                    {preset.title}
                  </h4>

                  <p className="text-xs text-slate-500 font-medium mt-1 leading-relaxed">
                    {preset.desc}
                  </p>
                </div>

                <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-bold">
                  <span className="text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded-md">
                    {preset.count}
                  </span>
                  <span className="text-slate-500">
                    {preset.time}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* 3. Custom Adventure Configuration (When Custom is selected) */}
      {selectedPreset === 'custom' && (
        <div className="bg-white border-2 border-violet-300 rounded-3xl p-5 sm:p-6 shadow-sm space-y-5 animate-scale-in">
          
          <div className="flex items-center space-x-2 text-violet-900">
            <Sliders className="w-5 h-5 text-violet-600" />
            <h3 className="font-black text-base">Customize Your Adventure</h3>
          </div>

          {/* Quick Count & Time Chips */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            
            {/* Question Count */}
            <div className="space-y-2">
              <label className="text-xs font-black text-slate-700 uppercase tracking-wide">
                How Many Questions?
              </label>
              <div className="flex flex-wrap gap-2">
                {[10, 20, 30, 50].map(cnt => (
                  <button
                    key={cnt}
                    type="button"
                    onClick={() => {
                      soundFx.playPop();
                      setCustomCount(cnt);
                    }}
                    className={`px-4 py-2 rounded-xl font-black text-xs transition-all active:scale-95 cursor-pointer ${
                      customCount === cnt 
                        ? 'bg-violet-600 text-white shadow-xs' 
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    {cnt} Qs
                  </button>
                ))}
              </div>
            </div>

            {/* Duration */}
            <div className="space-y-2">
              <label className="text-xs font-black text-slate-700 uppercase tracking-wide">
                Time Limit (Minutes)
              </label>
              <div className="flex flex-wrap gap-2">
                {[5, 10, 15, 25, 0].map(dur => (
                  <button
                    key={dur}
                    type="button"
                    onClick={() => {
                      soundFx.playPop();
                      setCustomDuration(dur);
                    }}
                    className={`px-4 py-2 rounded-xl font-black text-xs transition-all active:scale-95 cursor-pointer ${
                      customDuration === dur 
                        ? 'bg-violet-600 text-white shadow-xs' 
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    {dur === 0 ? 'Untimed ♾️' : `${dur} Mins`}
                  </button>
                ))}
              </div>
            </div>

          </div>

          {/* Subject Pills */}
          <div className="space-y-2">
            <label className="text-xs font-black text-slate-700 uppercase tracking-wide">
              Select Subjects to Include ({selectedSubjectIds.length} Selected)
            </label>
            
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
              {SUBJECT_LIST.map(sub => {
                const isSelected = selectedSubjectIds.includes(sub.id);
                const subQCount = questions.filter(q => q.subjectId === sub.id).length;
                return (
                  <div
                    key={sub.id}
                    onClick={() => toggleSubject(sub.id)}
                    className={`p-2.5 rounded-xl border-2 text-xs font-bold flex items-center justify-between cursor-pointer transition-all ${
                      isSelected 
                        ? 'border-violet-600 bg-violet-50 text-violet-950 shadow-2xs' 
                        : 'border-slate-200 text-slate-600 hover:bg-slate-50'
                    }`}
                  >
                    <span className="truncate pr-1">{sub.name}</span>
                    <span className="text-[10px] font-mono font-bold bg-white/80 px-1.5 py-0.5 rounded border border-current shrink-0">
                      {subQCount}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Chapter / Subsection Pills */}
          {selectedSubjectIds.length === 1 && (
            <div className="space-y-2 pt-2 border-t border-slate-100">
              <label className="text-xs font-black text-slate-700 uppercase tracking-wide">
                Filter Specific Chapters / Units ({selectedTopics.length === 0 ? 'All Chapters' : `${selectedTopics.length} Chapters Selected`})
              </label>
              
              <div className="flex flex-wrap gap-1.5">
                {SUBJECT_LIST.find(s => s.id === selectedSubjectIds[0])?.topics.map(topicName => {
                  const isSelected = selectedTopics.includes(topicName);
                  const topicCount = questions.filter(q => q.subjectId === selectedSubjectIds[0] && q.topic === topicName).length;
                  return (
                    <button
                      key={topicName}
                      type="button"
                      onClick={() => toggleTopic(topicName)}
                      className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 cursor-pointer active:scale-95 ${
                        isSelected 
                          ? 'bg-emerald-600 text-white shadow-2xs' 
                          : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                      }`}
                    >
                      <span>{topicName}</span>
                      <span className="text-[10px] font-mono opacity-80">({topicCount})</span>
                    </button>
                  );
                })}
              </div>
            </div>
          )}

        </div>
      )}

      {/* 4. Giant Vibrant Launch Bar */}
      <div className="sticky bottom-4 z-40 bg-white/95 backdrop-blur-md border-2 border-slate-200 p-4 rounded-3xl shadow-xl flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-400 text-slate-950 flex items-center justify-center font-black shadow-xs shrink-0">
            <Zap className="w-5 h-5 fill-current" />
          </div>
          <div>
            <span className="text-xs font-extrabold text-slate-900 block">
              Ready to Launch! 🎯
            </span>
            <span className="text-[11px] text-slate-500 font-medium">
              Mode: {feedbackMode === 'instant' ? 'Interactive Quiz' : 'Timed Mock Exam'}
            </span>
          </div>
        </div>

        <button
          onClick={handleStartDrill}
          className="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-amber-400 via-orange-400 to-amber-500 hover:from-amber-500 hover:to-orange-500 text-slate-950 font-black text-sm sm:text-base rounded-2xl shadow-lg transition-transform active:scale-95 cursor-pointer touch-manipulation flex items-center justify-center space-x-2"
        >
          <span>Launch Quiz Now</span>
          <Play className="w-4 h-4 fill-current" />
        </button>
      </div>

    </div>
  );
};
