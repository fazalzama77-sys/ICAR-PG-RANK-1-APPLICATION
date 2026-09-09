# ICAR AIEEA PG (M.V.Sc.) CBT Examination Preparation Platform
> **Mission: All India Rank 1 (AIR 1) &bull; Precision 1st & 2nd Year CBT Training**

This web application is a high-fidelity Computer-Based Test (CBT) replica of the official National Testing Agency (NTA) ICAR AIEEA PG entrance examination, built for B.V.Sc. & A.H. students preparing early to secure All India Rank 1.

---

## ⚡ Quick Start: How to Run the Site

### 1. Install Dependencies
If you have just cloned or moved this folder, run:
```powershell
npm install
```

### 2. Start the Development Server
```powershell
npm run dev
```

### 3. Open in Your Web Browser
Open your browser and navigate to:
```
http://localhost:5173/
```

### 4. Build for Production (Optional)
```powershell
npm run build
npm run preview
```

---

## 📖 Key Features & Architecture

- **Official NTA CBT Interface Replica**:
  - Top header with Candidate Name, Roll Number, Exam Title, and Countdown Timer.
  - Section Switcher Tabs: **Veterinary Science** and **Animal Science**.
  - Authentic 5-State Question Palette with official NTA shapes & colors:
    - ⬜ **Not Visited** (White/Gray)
    - 🟥 **Not Answered** (Red)
    - 🟩 **Answered** (Green)
    - 🟪 **Marked for Review** (Purple)
    - 🟣 **Answered & Marked for Review** (Purple with green dot — evaluated for marks)
  - Full Action Buttons: *Save & Next*, *Save & Mark for Review*, *Clear Response*, *Mark for Review & Next*, *Previous*, and *Next*.
  - NTA Examination Summary Confirmation Modal before final scoring.
- **Configurable Practice & Mock Engine**:
  - Full 120-question, 120-minute, $+4/-1$ mock exam mode.
  - Custom practice drill (custom question count, custom timer or untimed, custom marking).
- **Targeted MSVE VCI Syllabus Coverage**:
  - **1st Year Subjects**: Veterinary Anatomy (VAN), Veterinary Physiology (VPY), Veterinary Biochemistry (VBC), Livestock Production Management (LPM).
  - **2nd Year Subjects**: Veterinary Pathology (VPP), Veterinary Microbiology (VMC), Veterinary Parasitology (VPA), Animal Genetics & Breeding (AGB), Animal Nutrition (ANN).
- **Question Bank Management (Starts Clean & Empty)**:
  - Add individual MCQs with options, correct answer, tags, and detailed high-yield explanations.
  - Bulk JSON import and export with downloadable JSON template.
  - 100% offline and persistent via browser LocalStorage.
- **AIR 1 Performance Diagnostics**:
  - Instant scorecard with positive marks, negative marks deducted, and accuracy rate.
  - Domain-wise and subject-wise precision matrix highlighting weak areas.
  - Question-by-question review with filters for incorrect, correct, and unattempted questions.

- **100% Offline Progressive Web App (PWA)**:
  - **Service Worker Precaching**: All HTML, JavaScript, CSS stylesheets, icons, and test engine assets are automatically cached for instant offline loading.
  - **Zero Network Required**: Take full 120-question mock exams or practice drills completely offline without an internet connection. All questions and test records persist locally in the browser's storage.
  - **Desktop & Mobile App Installation**: Click the **"Install App"** button in the top navigation bar or your browser's install icon to install the platform as a standalone desktop or mobile application.
  - **Live Offline Status Indicator**: Real-time badge indicators show connectivity status and confirm local evaluation security during exams.

---

## 📚 Detailed Documentation
For the full curriculum syllabus blueprint, NTA marking guidelines, and strategic study methodology, please read [`CONTEXT.md`](./CONTEXT.md).

