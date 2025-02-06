// Test Case 1: Trigger on push to main branch for Static content
test('should trigger on push to main branch', () => {
    const event = { ref: 'refs/heads/main' };
    const workflow = require('../.github/workflows/static.yml');
    
    // Simulate GitHub Actions push event
    expect(workflow.on.push.branches).toContain('main');
    expect(event.ref).toEqual('refs/heads/main');
  });
  
  // Test Case 2: Verify if the repository is uploaded correctly
  test('should upload entire repository as artifact', () => {
    const artifact = './';  // Path to the repository
    const expectedArtifact = '.';
  
    // Simulate the upload of the repository
    expect(artifact).toBe(expectedArtifact);
  });
  
  // Test Case 3: Ensure the deployment action is correctly set up
  test('should have correct deploy step in the deploy job', () => {
    const deployStep = 'Deploy to GitHub Pages';
    const workflow = require('../.github/workflows/static.yml');
  
    // Check if deploy step exists
    const deploySteps = workflow.jobs.deploy.steps;
    const deployStepPresent = deploySteps.some(step => step.name === deployStep);
  
    expect(deployStepPresent).toBe(true);
  });
  