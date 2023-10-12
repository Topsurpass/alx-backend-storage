-- Create table users if not exist on any database with the following
-- details. country is an enum with US as default value
-- It leaves one to pick between list of options.


CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY(id)
);
