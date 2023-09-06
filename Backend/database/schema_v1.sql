CREATE TABLE [IF NOT EXISTS] `Follows` (
  `userId` integer,
  `followingId` integer,
  `created_at` timestamp
);

CREATE TABLE [IF NOT EXISTS] `Users` (
  `userId` integer PRIMARY KEY,
  `username` varchar(255),
  `email` varchar(255),
  `password` varchar(255),
  `created_at` timestamp
);

CREATE TABLE [IF NOT EXISTS] `Activities` (
  `activityId` integer PRIMARY KEY,
  `movieId` integer,
  `rating` NULL decimal(2,1),
  `userId` integer,
  `created_at` timestamp
);

CREATE TABLE [IF NOT EXISTS] `Movies` (
  `movieId` integer PRIMARY KEY,
  `title` varchar(255),
  `genre` varchar(255)
);

ALTER TABLE `Rankings` ADD FOREIGN KEY (`userId`) REFERENCES `Users` (`userId`);

ALTER TABLE `Rankings` ADD FOREIGN KEY (`movieId`) REFERENCES `Movies` (`movieId`);

ALTER TABLE `Follows` ADD FOREIGN KEY (`userId`) REFERENCES `Users` (`userId`);

ALTER TABLE `Follows` ADD FOREIGN KEY (`followingId`) REFERENCES `Users` (`userId`);
