import React, { useEffect, useState } from 'react';

export default function TaskList() {
  const [tasks, setTasks] = useState([]);

  console.log("📦 TaskList component rendered");

  useEffect(() => {
    console.log("🚀 useEffect triggered, fetching tasks...");
    
    const fetchTasks = async () => {
      try {
        const res = await fetch("http://localhost:5000/tasks");
        const data = await res.json();
        console.log("✅ Fetched tasks:", data);
        setTasks(data);
      } catch (err) {
        console.error("❌ Failed to fetch tasks:", err);
      }
    };

    fetchTasks();
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">All Tasks</h2>
      <p className="mb-2">Task count: {tasks.length}</p>
  
      <ul className="space-y-2">
        {tasks.map(task => (
          <li key={task.id} className="border p-3 rounded shadow-sm">
            <div className="font-semibold">{task.title}</div>
            <div className="text-sm text-gray-600">{task.description}</div>
            <div className="text-sm text-gray-400">
              Due: {new Date(task.due_date).toLocaleDateString()}
            </div>
            <div className="text-sm text-gray-400">
              User ID: {task.user_id}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
  
}
