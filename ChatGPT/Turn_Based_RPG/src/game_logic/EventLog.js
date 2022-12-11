import React, { useState } from 'react';

// The EventLog component displays a list of events that have occurred in the game
// and provides features for scrolling, filtering, and pagination
const EventLog = ({ events }) => {
  // Initialize state variables
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage, setItemsPerPage] = useState(10);
  const [searchTerm, setSearchTerm] = useState('');

  // Function to handle pagination
  const handlePageChange = direction => {
    if (direction === 'next' && currentPage < events.length / itemsPerPage) {
      setCurrentPage(currentPage + 1);
    } else if (direction === 'prev' && currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  // Function to handle filtering
  const handleSearchChange = e => {
    setSearchTerm(e.target.value);
    setCurrentPage(1);
  };

  // Function to handle changing the number of items per page
  const handleItemsPerPageChange = e => {
    setItemsPerPage(parseInt(e.target.value, 10));
    setCurrentPage(1);
  };

  // Filter the events array based on the search term
  const filteredEvents = events.filter(event => event.includes(searchTerm));

  // Calculate the start and end indices for the current page
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  // Get the events for the current page
  const currentPageEvents = filteredEvents.slice(startIndex, endIndex);

  return (
    <div>
      {/* Search input for filtering events */}
      <input
        type="text"
        placeholder="Search events..."
        value={searchTerm}
        onChange={handleSearchChange} />
      {/* Select input for changing the number of items per page */}
      <select value={itemsPerPage} onChange={handleItemsPerPageChange}>
        <option value="10">10</option>
        <option value="20">20</option>
        <option value="50">50</option>
      </select>
      {/* Button to go to the previous page */}
      <button
        onClick={() => handlePageChange('prev')}
        disabled={currentPage === 1}>
        Prev
      </button>
      {/* Button to go to the next page */}
      <button
        onClick={() => handlePageChange('next')}
        disabled={currentPage === Math.ceil(filteredEvents.length / itemsPerPage)}>
        Next
      </button>
      {/* Display the events for the current page */}
      <ul>
        {currentPageEvents.map((event, index) => (
          <li key={index}>{event}</li>
        ))}
      </ul>
    </div>
  );
};

export default EventLog;