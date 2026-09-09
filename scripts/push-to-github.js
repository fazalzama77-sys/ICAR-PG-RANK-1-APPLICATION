import { execSync } from 'child_process';

function run(command, options = {}) {
  try {
    return execSync(command, { stdio: 'pipe', encoding: 'utf-8', ...options }).trim();
  } catch (err) {
    if (options.ignoreError) return '';
    throw err;
  }
}

console.log('\n========================================================');
console.log('       🚀 1-CLICK PUSH & DEPLOY TO GITHUB PAGES         ');
console.log('========================================================\n');

try {
  // Step 1: Check git status
  console.log('🔍 [1/4] Checking Git status...');
  const remotes = run('git remote -v', { ignoreError: true });
  if (!remotes.includes('origin')) {
    console.error('❌ Error: No Git remote "origin" found.');
    process.exit(1);
  }

  // Step 2: Stage and Commit if changes exist
  console.log('📦 [2/4] Staging source code changes...');
  run('git add -A');

  const stagedDiff = run('git diff --cached --name-only', { ignoreError: true });
  
  if (stagedDiff) {
    const customMsg = process.argv.slice(2).join(' ').trim();
    const now = new Date();
    const timestamp = now.toLocaleString('en-IN', {
      timeZone: 'Asia/Kolkata',
      dateStyle: 'medium',
      timeStyle: 'medium'
    });
    const commitMsg = customMsg || `feat: update project files (${timestamp})`;
    
    console.log(`💾 Committing changes to main: "${commitMsg}"...`);
    run(`git commit -m "${commitMsg.replace(/"/g, '\\"')}"`);
  } else {
    console.log('ℹ️  No new or modified files to commit.');
  }

  // Step 3: Push main branch to GitHub
  console.log('🚀 [3/4] Pushing source code to GitHub (main branch)...');
  execSync('git push origin main', { stdio: 'inherit' });

  // Step 4: Build and Deploy to GitHub Pages (gh-pages branch)
  console.log('\n🌐 [4/4] Building production bundle and publishing to GitHub Pages...');
  execSync('npx gh-pages -d dist', { stdio: 'inherit' });

  console.log('\n========================================================');
  console.log('🎉 SUCCESS! Both Source Code & Live Website Updated!');
  console.log('🔗 Live Website : https://fazalzama77-sys.github.io/ICAR-PG-RANK-1-APPLICATION/');
  console.log('📂 GitHub Repo  : https://github.com/fazalzama77-sys/ICAR-PG-RANK-1-APPLICATION');
  console.log('========================================================\n');
} catch (error) {
  console.error('\n❌ Push/Deploy failed:');
  console.error(error.message || error);
  console.log('\nPlease check your internet connection or GitHub credentials.\n');
  process.exit(1);
}
