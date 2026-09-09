import React, { useRef, useState } from 'react';
import { Download, Upload, FileText, CheckCircle2, AlertCircle, FileCode } from 'lucide-react';
import { Question } from '../../types';
import { StorageService } from '../../storage/db';

interface BulkImportExportProps {
  onQuestionsImported: () => void;
  currentQuestionCount: number;
}

export const BulkImportExport: React.FC<BulkImportExportProps> = ({
  onQuestionsImported,
  currentQuestionCount
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [feedback, setFeedback] = useState<{ type: 'success' | 'error'; message: string } | null>(null);

  // Download Sample JSON Template
  const handleDownloadTemplate = () => {
    const templateContent = StorageService.getSampleTemplateJSON();
    const blob = new Blob([templateContent], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'ICAR_PG_Questions_Template.json';
    link.click();
    URL.revokeObjectURL(url);
  };

  // Export Current Questions as JSON
  const handleExportQuestions = () => {
    const data = StorageService.exportQuestionsJSON();
    const blob = new Blob([data], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `ICAR_PG_QuestionBank_${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  // Trigger File Input Click
  const handleTriggerFileInput = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  // Handle JSON File Upload
  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const text = event.target?.result as string;
        const parsed = JSON.parse(text);

        if (!Array.isArray(parsed)) {
          throw new Error('The JSON file must contain an array of question objects.');
        }

        // Validate basic fields
        const validQuestions: Question[] = [];
        for (let i = 0; i < parsed.length; i++) {
          const item = parsed[i];
          if (!item.questionText || !Array.isArray(item.options) || item.options.length !== 4) {
            throw new Error(`Question at index ${i + 1} has invalid structure (must have questionText and exactly 4 options).`);
          }
          validQuestions.push({
            id: item.id || 'imported_' + Date.now() + '_' + i,
            domain: item.domain === 'animal_science' ? 'animal_science' : 'veterinary_science',
            year: item.year || '1st_year',
            subjectId: item.subjectId || 'van',
            topic: item.topic || undefined,
            questionText: item.questionText,
            options: [item.options[0], item.options[1], item.options[2], item.options[3]],
            correctOptionIndex: typeof item.correctOptionIndex === 'number' ? item.correctOptionIndex : 0,
            explanation: item.explanation || '',
            difficulty: item.difficulty || 'Medium',
            tags: item.tags || [],
            createdAt: Date.now()
          });
        }

        const res = StorageService.bulkAddQuestions(validQuestions);
        setFeedback({
          type: 'success',
          message: `Successfully imported ${res.addedCount} questions into your Question Bank!`
        });
        onQuestionsImported();
      } catch (err: any) {
        setFeedback({
          type: 'error',
          message: `Import failed: ${err.message || 'Invalid JSON format'}`
        });
      } finally {
        if (fileInputRef.current) {
          fileInputRef.current.value = '';
        }
      }
    };

    reader.readAsText(file);
  };

  // Load High-Yield Verification Template (Loads 4 initial starter questions)
  const handleLoadSampleStarterPack = () => {
    const sampleJson = StorageService.getSampleTemplateJSON();
    const parsed = JSON.parse(sampleJson) as Question[];
    const res = StorageService.bulkAddQuestions(parsed);
    setFeedback({
      type: 'success',
      message: `Loaded ${res.addedCount} starter verification MCQs (Anatomy, Pathology, LPM, AGB) successfully!`
    });
    onQuestionsImported();
  };

  return (
    <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-xs">
      <div className="flex flex-wrap items-center justify-between gap-4 mb-4">
        <div>
          <h3 className="font-bold text-slate-900 text-sm sm:text-base flex items-center space-x-2">
            <FileCode className="w-4 h-4 text-emerald-600" />
            <span>Bulk Question Operations</span>
          </h3>
          <p className="text-xs text-slate-500">
            Import batches of questions prepared from your notes, export backups, or download the template.
          </p>
        </div>

          {/* Load 120 Questions Per Subject (All 9 Subjects) */}
          <button
            onClick={() => {
              const res = StorageService.loadAll1080Questions();
              setFeedback({
                type: 'success',
                message: `Loaded all ${res.count} high-yield MCQs! Exactly 120 questions across all 9 subjects are now ready.`
              });
              onQuestionsImported();
            }}
            className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg border border-amber-500 bg-amber-500 hover:bg-amber-600 text-slate-900 font-extrabold text-xs shadow-xs transition-colors cursor-pointer"
            title="Populates the Question Bank with 120 most important questions per subject across all 9 subjects (1,080 questions total)"
          >
            <span>⚡ Load 120 Qs Per Subject (1,080 Qs)</span>
          </button>

          {/* Download JSON Template */}
          <button
            onClick={handleDownloadTemplate}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-slate-700 text-xs font-semibold shadow-2xs transition-colors"
          >
            <Download className="w-3.5 h-3.5 text-blue-600" />
            <span>Download JSON Template</span>
          </button>

          {/* Import JSON File */}
          <button
            onClick={handleTriggerFileInput}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-emerald-500 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 text-xs font-semibold transition-colors"
          >
            <Upload className="w-3.5 h-3.5 text-emerald-700" />
            <span>Import Questions (.json)</span>
          </button>
          <input
            ref={fileInputRef}
            type="file"
            accept=".json"
            onChange={handleFileUpload}
            className="hidden"
          />

          {/* Export Questions */}
          {currentQuestionCount > 0 && (
            <button
              onClick={handleExportQuestions}
              className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-slate-700 text-xs font-semibold shadow-2xs transition-colors"
            >
              <FileText className="w-3.5 h-3.5 text-amber-600" />
              <span>Export All ({currentQuestionCount})</span>
            </button>
          )}
      </div>

      {/* Feedback Banner */}
      {feedback && (
        <div
          className={`p-3 rounded-lg flex items-center justify-between text-xs font-medium ${
            feedback.type === 'success'
              ? 'bg-emerald-50 text-emerald-800 border border-emerald-200'
              : 'bg-red-50 text-red-800 border border-red-200'
          }`}
        >
          <div className="flex items-center space-x-2">
            {feedback.type === 'success' ? (
              <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
            ) : (
              <AlertCircle className="w-4 h-4 text-red-600 shrink-0" />
            )}
            <span>{feedback.message}</span>
          </div>
          <button
            onClick={() => setFeedback(null)}
            className="text-xs underline hover:no-underline font-bold ml-4"
          >
            Dismiss
          </button>
        </div>
      )}
    </div>
  );
};
