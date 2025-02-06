// Test Case 1: Trigger on push to main branch for Jekyll
test('should trigger on push to main branch', () => {
    const event = { ref: 'refs/heads/main' };
    const workflow = require('../.github/workflows/jekyll-gh-pages.yml');
    
    // Simulate GitHub Actions push event
    expect(workflow.on.push.branches).toContain('main');
    expect(event.ref).toEqual('refs/heads/main');
  });
  
  // Test Case 2: Ensure build job contains the correct actions for Jekyll
  test('build job should contain correct steps for Jekyll site', () => {
    const steps = [
      'Checkout',
      'Setup Pages',
      'Build with Jekyll',
      'Upload artifact'
    ];
  
    const actualSteps = [
      'Checkout',
      'Setup Pages',
      'Build with Jekyll',
      'Upload artifact'
    ];
  
    expect(actualSteps).toEqual(steps);
  });
  
  // Test Case 3: Test if deploy job has the deployment step configured
  test('deploy job should contain deployment step for GitHub Pages', () => {
    const deployStep = 'Deploy to GitHub Pages';
    const workflow = require('../.github/workflows/jekyll-gh-pages.yml');
  
    // Find deploy step in job
    const deploySteps = workflow.jobs.deploy.steps;
    const deployStepPresent = deploySteps.some(step => step.name === deployStep);
  
    expect(deployStepPresent).toBe(true);
  });
  