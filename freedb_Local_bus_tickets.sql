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
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `ticket_id` int NOT NULL AUTO_INCREMENT,
  `passenger_id` int NOT NULL,
  `bus_id` int NOT NULL,
  `st` varchar(30) NOT NULL,
  `en` varchar(30) NOT NULL,
  `amount` int NOT NULL,
  `check_ticket` tinyint(1) DEFAULT NULL,
  `transaction_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ticket_id`),
  KEY `passenger_id` (`passenger_id`),
  KEY `bus_id` (`bus_id`),
  CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`passenger_id`) REFERENCES `passenger` (`passenger_id`),
  CONSTRAINT `tickets_ibfk_2` FOREIGN KEY (`bus_id`) REFERENCES `bus` (`bus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (1,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:17:30'),(2,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:20:36'),(3,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:21:37'),(4,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:23:24'),(5,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:24:42'),(6,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:25:08'),(7,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:30:34'),(8,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:32:15'),(9,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:34:13'),(10,1,1,'Savar','Kalampur',19,1,'2024-10-25 22:38:32'),(11,1,1,'Signboard','Gabtoli',21,1,'2024-10-26 00:39:01'),(12,2,1,'Savar','Kalampur',19,1,'2024-10-26 01:25:35'),(13,3,1,'Savar','Kalampur',38,1,'2024-10-26 02:19:00'),(14,3,1,'Savar','Kalampur',38,0,'2024-10-26 13:02:02'),(15,3,1,'Savar','Kalampur',38,0,'2024-10-26 13:03:22'),(16,2,1,'Savar','Azimpur',23,0,'2024-10-26 13:15:57'),(17,2,1,'Gabtoli','Savar',14,0,'2024-10-28 13:15:09'),(18,1,1,'Savar','Azimpur',23,0,'2024-10-29 13:03:13'),(19,1,1,'Savar','Kalampur',19,0,'2024-10-29 13:06:10'),(20,4,1,'Signboard','Savar',35,1,'2024-10-29 13:31:06'),(21,1,1,'Savar','Azimpur',23,1,'2024-10-30 01:30:51'),(22,1,1,'Savar','Azimpur',23,0,'2024-10-30 01:31:11'),(23,3,1,'Savar','Kalampur',38,0,'2024-11-05 02:40:42'),(24,4,1,'Savar','NewMarket',22,0,'2024-11-25 23:17:12'),(25,4,1,'NewMarket','Savar',22,0,'2024-11-25 23:18:24'),(26,1,1,'Savar','Kalampur',19,0,'2024-12-09 23:51:38'),(27,4,3,'Mirpur1','AsadGate',10,0,'2024-12-11 22:42:56'),(28,1,6,'ECB','Mirpur10',10,0,'2024-12-12 00:44:30'),(29,1,6,'ECB','Mirpur10',10,0,'2024-12-12 00:44:32'),(30,1,6,'ECB','Mirpur10',10,0,'2024-12-12 00:44:33'),(31,2,8,'Mirpur10','Mirpur1',10,0,'2024-12-12 07:57:43'),(32,5,1,'Savar','Signboard',35,0,'2024-12-12 09:23:22');
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
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

-- Dump completed on 2025-03-08 23:24:33
