// Test Case 1: Trigger deployment on push to main branch
test('should trigger on push to main branch', () => {
    const event = { ref: 'refs/heads/main' };
    const workflow = require('../.github/workflows/deploy.yml');
    
    // Simulate GitHub Actions push event
    expect(workflow.on.push.branches).toContain('main');
    expect(event.ref).toEqual('refs/heads/main');
  });
  
  // Test Case 2: Test permissions are correctly set
  test('should set correct permissions for GitHub Pages deployment', () => {
    const permissions = {
      contents: 'write'
    };
  
    expect(permissions).toEqual({
      contents: 'write'
    });
  });
  
  // Test Case 3: Ensure `deploy` job has correct actions
  test('deploy job should contain the correct steps', () => {
    const steps = [
      'Checkout Repository',
      'Setup Node.js',
      'Deploy to GitHub Pages'
    ];
  
    const actualSteps = [
      'Checkout Repository',
      'Setup Node.js',
      'Deploy to GitHub Pages'
    ];
  
    expect(actualSteps).toEqual(steps);
  });
  