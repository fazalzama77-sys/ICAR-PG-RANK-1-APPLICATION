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
console.log('       🚀 1-CLICK PUSH TO GITHUB (ICAR PG RANK 1)       ');
console.log('========================================================\n');

try {
  // Step 1: Check git status
  console.log('🔍 [1/3] Checking Git status...');
  const remotes = run('git remote -v', { ignoreError: true });
  if (!remotes.includes('origin')) {
    console.error('❌ Error: No Git remote "origin" found.');
    process.exit(1);
  }

  // Step 2: Stage and Commit if changes exist
  console.log('📦 [2/3] Staging files...');
  run('git add -A');

  const stagedDiff = run('git diff --cached --name-only', { ignoreError: true });
  
  if (stagedDiff) {
    // Custom message from args or timestamped message
    const customMsg = process.argv.slice(2).join(' ').trim();
    const now = new Date();
    const timestamp = now.toLocaleString('en-IN', {
      timeZone: 'Asia/Kolkata',
      dateStyle: 'medium',
      timeStyle: 'medium'
    });
    const commitMsg = customMsg || `feat: update project files (${timestamp})`;
    
    console.log(`💾 Committing changes: "${commitMsg}"...`);
    run(`git commit -m "${commitMsg.replace(/"/g, '\\"')}"`);
  } else {
    console.log('ℹ️  No new or modified files to commit.');
  }

  // Step 3: Push to GitHub
  console.log('🚀 [3/3] Pushing to GitHub (origin main)...');
  execSync('git push origin main', { stdio: 'inherit' });

  console.log('\n========================================================');
  console.log('✅ SUCCESS! All changes pushed to GitHub successfully!');
  console.log('🔗 Repository: https://github.com/fazalzama77-sys/ICAR-PG-RANK-1-APPLICATION');
  console.log('========================================================\n');
} catch (error) {
  console.error('\n❌ Push failed:');
  console.error(error.message || error);
  console.log('\nPlease check your internet connection or GitHub credentials.\n');
  process.exit(1);
}
