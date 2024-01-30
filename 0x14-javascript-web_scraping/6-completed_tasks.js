#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

// Make a request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const tasks = JSON.parse(body);

  // Create an object to store the count of completed tasks per user
  const completedTasksCount = {};

  // Loop through tasks to count completed tasks per user
  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTasksCount[task.userId]) {
        completedTasksCount[task.userId]++;
      } else {
        completedTasksCount[task.userId] = 1;
      }
    }
  });

  // Print the result
  console.log(completedTasksCount);
});
