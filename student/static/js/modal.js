function openModal() {
    document.getElementById('myModal').classList.remove('hidden');
  }

  function closeModal() {
    document.getElementById('myModal').classList.add('hidden');
  }

  // Add an event listener to the "Add Student" button
  document.querySelector('.add_student').addEventListener('click', function() {
    openModal();
  });