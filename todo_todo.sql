-- Table structure for table `todo`

DROP TABLE IF EXISTS `todo`;

CREATE TABLE `todo` (
  `sno` int NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `descp` varchar(1000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
