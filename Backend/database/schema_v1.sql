USE Critix;

DROP TABLE IF EXISTS `Followers`;
DROP TABLE IF EXISTS `Likes`;
DROP TABLE IF EXISTS `Comments`;
DROP TABLE IF EXISTS `Activities`;
DROP TABLE IF EXISTS `Users`;
DROP TABLE IF EXISTS `Movies`;

CREATE TABLE `Followers` (
  `follower_id` INT AUTO_INCREMENT PRIMARY KEY,
  `follower_user_id` INT,
  `following_user_id` INT,
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY unique_followers (follower_user_id, following_user_id)
);

CREATE TABLE `Users` (
  `user_id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(50) NOT NULL UNIQUE,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `password_hash` VARBINARY(64) NOT NULL,
  `password_salt` VARBINARY(16) NOT NULL,
  `phone_number` VARCHAR(15),
  `name` VARCHAR(100),
  `profile_picture` VARCHAR(255),
  `temporary_nonce` VARBINARY(64),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `Activities` (
  `activity_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `movie_id` INT,
  `watchlist` BOOLEAN NOT NULL,
  `rating` DECIMAL(3,2),
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `Likes` (
  `like_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `activity_id` INT,
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `Comments` (
  `comment_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `activity_id` INT,
  `content` TEXT NOT NULL,
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `Movies` (
  `movie_id` integer PRIMARY KEY,
  `title` varchar(255),
  `genre` varchar(255)
);

ALTER TABLE `Activities` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `Activities` ADD FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`movie_id`);

ALTER TABLE `Followers` ADD FOREIGN KEY (`follower_user_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `Followers` ADD FOREIGN KEY (`following_user_id`) REFERENCES `Users` (`user_id`);

ALTER TABLE `Likes` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `Likes` ADD FOREIGN KEY (`activity_id`) REFERENCES `Activities` (`activity_id`);

ALTER TABLE `Comments` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`);
ALTER TABLE `Comments` ADD FOREIGN KEY (`activity_id`) REFERENCES `Activities` (`activity_id`);
