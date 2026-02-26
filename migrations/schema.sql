CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(50),
    event_type VARCHAR(50),
    message TEXT,
    decision VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    event_id INTEGER,
    decision VARCHAR(20),
    reason TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);