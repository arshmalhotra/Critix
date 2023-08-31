CREATE TABLE `Follows` (
  `userId` integer,
  `followingId` integer,
  `created_at` timestamp
);

CREATE TABLE `Users` (
  `userId` integer PRIMARY KEY,
  `username` varchar(255),
  `email` varchar(255),
  `password` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `Ratings` (
  `ratingId` integer PRIMARY KEY,
  `movieId` integer,
  `rating` decimal(2,1),
  `userId` integer,
  `created_at` timestamp
);

CREATE TABLE `Movies` (
  `movieId` integer PRIMARY KEY,
  `title` varchar(255),
  `genre` varchar(255)
);

ALTER TABLE `Ratings` ADD FOREIGN KEY (`userId`) REFERENCES `Users` (`userId`);

ALTER TABLE `Ratings` ADD FOREIGN KEY (`movieId`) REFERENCES `Movies` (`movieId`);

ALTER TABLE `Follows` ADD FOREIGN KEY (`userId`) REFERENCES `Users` (`userId`);

ALTER TABLE `Follows` ADD FOREIGN KEY (`followingId`) REFERENCES `Users` (`userId`);
