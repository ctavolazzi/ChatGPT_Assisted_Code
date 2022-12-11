import React, { useState } from 'react';

class AllChapters extends React.Component {
  constructor() {
    super();
    // Initialize state variable to store the list of chapters
    this.chapters = [];
  }

  // Method to add a chapter to the list of chapters
  addChapter(chapter) {
    this.chapters = [...this.chapters, chapter];
  }

  // Method to remove a chapter from the list of chapters
  removeChapter(chapter) {
    this.chapters = this.chapters.filter(c => c !== chapter);
  }
}

export default AllChapters;
