CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_title TEXT,
    date TEXT NOT NULL,
    description TEXT,
    time TEXT NOT NULL,
    category TEXT
);
