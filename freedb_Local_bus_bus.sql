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
-- Table structure for table `bus`
--

DROP TABLE IF EXISTS `bus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus` (
  `bus_id` int NOT NULL AUTO_INCREMENT,
  `bus_name` varchar(30) NOT NULL,
  `stopage1` varchar(30) DEFAULT NULL,
  `stopage2` varchar(30) DEFAULT NULL,
  `stopage3` varchar(30) DEFAULT NULL,
  `stopage4` varchar(30) DEFAULT NULL,
  `stopage5` varchar(30) DEFAULT NULL,
  `stopage6` varchar(30) DEFAULT NULL,
  `stopage7` varchar(30) DEFAULT NULL,
  `stopage8` varchar(30) DEFAULT NULL,
  `stopage9` varchar(30) DEFAULT NULL,
  `stopage10` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`bus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus`
--

LOCK TABLES `bus` WRITE;
/*!40000 ALTER TABLE `bus` DISABLE KEYS */;
INSERT INTO `bus` VALUES (1,'Nilachol','Signboard','Chankharpul','Azimpur','NewMarket','Gabtoli','Savar','Nabinagar','Islampur','Kalampur',NULL),(2,'Bikash','Azimpur','Nilkhet','Kolabagan','Dhanmondi32','ManikMiaAvenue','Mohakhali','Banani','Kurmitola','Airport','Abdullahpur'),(3,'Mirpur Link','Gulisthan','BUET','ScienceLab','AsadGate','Technical','AnsarCamp','Mirpur1','Mirpur2','Proshika','Duaripara'),(4,'Himachol','Mirpur12','Mirpur10','Kazipara','Shewrapara','Farmgate','Shahbag','Paltan','Sayedabad','Jatrabari','KanchpurBridge'),(5,'Bihannga','Duaripara','Proshika','Mirpur2','Mirpur1','AnsarCamp','Technical','AsadGate','ScienceLab','BUET','Gulisthan'),(6,'Safety','Mirpur12','ECB','Mirpur10','Kazipara','Shewrapara','Agargaon','ShishuMela','CollegeGate','ManikMiaAvenue','Azimpur'),(7,'BRTC','Uttara','NotunBazar','Rampura','Malibag','Kakrail','Gulisthan','VictoriaPark',NULL,NULL,NULL),(8,'Purbachal','Mirpur14','Mirpur10','Mirpur1','EasternHousing','Zirabo','Fantasy','Baipail','EPZ','NandanPark','Chandra'),(9,'Arnob','Savar','Gabtoli','Mirpur1','Mirpur10','Mohakhali','Gulshan1','Amulia',NULL,NULL,NULL),(10,'VIP','Tongi','Azimpur','Mohakhali','Farmgate','ManikMiaAvenue','CityCollege','Nilkhet','Dhakeshwari',NULL,NULL),(11,'Anabil','Sayedabad','Malibagh','Satrasta','Mohakhali','Airport','TongiBazar','CheragAli','BoardBazar','Chowrasta','Gazipur'),(12,'Green Bangla','Demra','Sayedabad',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(13,'Bikash','Sayedabad','Gulistan','PressClub','Shahbagh','Nilkhet','Azimpur',NULL,NULL,NULL,NULL),(14,'Anabil','KachpurBridge','Sayedabad','Malibagh','NotunBazar','Airport','Tongi',NULL,NULL,NULL,NULL),(15,'Asmani Paribahan','Madanpur','Motijheel','Malibagh','Moghbazar','Mohakhali','Kakoli','Abdullahpur',NULL,NULL,NULL),(16,'Doel','Chankharpool','Gulisthan','Jatrabari','KachpurBridge','Madanpur','Sonargaon','MeghnaGhat',NULL,NULL,NULL),(17,'Gazipur Paribahan','KachpurBridge','Motijheel','Malibagh','ProgotiShoroni','Airport','Abdullahpur','BoardBazar',NULL,NULL,NULL),(18,'Dishari','NationalZoo','Mirpur1','AnsarCamp','Farmgate','Fulbaria','NayaBazar','Keraniganj',NULL,NULL,NULL),(19,'Shuveccha','JagannathUniversity','Fulbaria','Paltan','Mohakhali','Kakoli','Airport','Chandra',NULL,NULL,NULL),(20,'Shikor Paribahan','Mirpur12','Kalapani','Mirpur11','Mirpur10','Kazipara','Farmgate','Gulisthan','Sayedabad','Jatrabari','KachpurBridge'),(21,'Best Transport','NationalZoo','Mirpur2','Mirpur10','Kazipara','Farmgate','Moghbazar','Mouchak','Komlapur','Jatrabari','Ekuria'),(22,'VIP','Azimpur','Nilkhet','Kolabagan','ManikMiaAvenue','Mohakhali','Banani','Airport','Abdullahpur','Ashulia','NandanPark'),(23,'Thikana','Signboard','Chankharpul','Azimpur','NewMarket','Gabtoli','Savar','Nabinagar','Islampur','Kalampur',NULL);
/*!40000 ALTER TABLE `bus` ENABLE KEYS */;
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

-- Dump completed on 2025-03-08 23:24:47
