// src/components/TaskList.tsx
import React, { useState, useEffect } from 'react';

interface Task {
  id: number;
  title: string;
  description: string;
  due_date: string;
  user_id: number;
}

const TaskList: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://localhost:5000/tasks')
      .then((res) => res.json())
      .then((data) => setTasks(data))
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <div>Error: {error}</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Task List</h1>
      <ul className="space-y-4">
        {tasks.map((task) => (
          <li key={task.id} className="p-4 shadow-md rounded bg-white">
            <h2 className="text-xl font-semibold">{task.title}</h2>
            <p>{task.description}</p>
            <p>User: {task.user_id}</p>
            <p className="text-sm text-gray-500">
              Due Date: {new Date(task.due_date).toLocaleString()}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
