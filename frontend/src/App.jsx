import React from 'react';
import TaskList from './components/TaskList';

function App() {
  console.log("🔍 App component rendered");

  return (
    <div>
      <h1>Hello from App</h1>
      <TaskList />
    </div>
  );
}

export default App;
