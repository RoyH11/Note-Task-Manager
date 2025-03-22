// src/App.tsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import TaskList from './components/TaskList';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TaskList />} />
        {/* add other routes here */}
      </Routes>
    </Router>
  );
}

export default App;
