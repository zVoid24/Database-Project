-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: mysql-3b828684-diu-259e.h.aivencloud.com    Database: freedb_Local_bus
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '1d606536-aad9-11ef-968c-0a7e26c63711:1-15,
2a7377db-fc3e-11ef-a7ec-7ae6bf908738:1-15,
81d4c3f3-8bd9-11ef-9ece-024877108519:1-187,
9155a8f5-ab50-11ef-9bcf-0214da334a71:1-125,
e3bb9a8f-b8a6-11ef-8d99-9af0e7f7deb7:1-20';

--
-- Table structure for table `A344`
--

DROP TABLE IF EXISTS `A344`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `A344` (
  `route_id` varchar(30) NOT NULL,
  `NationalZoo` int NOT NULL,
  `Mirpur2` int NOT NULL,
  `Mirpur10` int NOT NULL,
  `Kazipara` int NOT NULL,
  `Shewrapara` int NOT NULL,
  `Agargaon` int NOT NULL,
  `Farmgate` int NOT NULL,
  `BanglaMotor` int NOT NULL,
  `Moghbazar` int NOT NULL,
  `Mouchak` int NOT NULL,
  `Komlapur` int NOT NULL,
  `Motijheel` int NOT NULL,
  `Sayedabad` int NOT NULL,
  `Jatrabari` int NOT NULL,
  `PostogolaBridge` int NOT NULL,
  `Ekuria` int NOT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `A344`
--

LOCK TABLES `A344` WRITE;
/*!40000 ALTER TABLE `A344` DISABLE KEYS */;
INSERT INTO `A344` VALUES ('A344',0,3,4,5,6,7,10,12,13,14,17,18,19,20,22,24);
/*!40000 ALTER TABLE `A344` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-08 23:24:27
