-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: den1.mysql6.gear.host    Database: innovaccersde
-- ------------------------------------------------------
-- Server version	5.7.23-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `email_responses`
--

DROP TABLE IF EXISTS `email_responses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `email_responses` (
  `email_id` varchar(100) DEFAULT NULL,
  `show_response` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_responses`
--

LOCK TABLES `email_responses` WRITE;
/*!40000 ALTER TABLE `email_responses` DISABLE KEYS */;
INSERT INTO `email_responses` VALUES ('shubham@octonoius.com','NARCOS'),('shubham@octonoius.com','GAME OF THRONES');
/*!40000 ALTER TABLE `email_responses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series`
--

DROP TABLE IF EXISTS `tv_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series` (
  `TV_SERIES_NAME` varchar(50) DEFAULT NULL,
  `NEXT_EPISODE` tinyint(1) DEFAULT NULL,
  `NEXT_EPISODE_DATE` date DEFAULT NULL,
  `NEXT_SEASON` tinyint(1) DEFAULT NULL,
  `NEXT_SEASON_YEAR` date DEFAULT NULL,
  `FINISHED_STREAMING` tinyint(1) DEFAULT NULL,
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series`
--

LOCK TABLES `tv_series` WRITE;
/*!40000 ALTER TABLE `tv_series` DISABLE KEYS */;
INSERT INTO `tv_series` VALUES ('GAME OF THRONES',1,'2019-04-01',1,'2019-04-01',0,101),('NARCOS',0,NULL,1,'2019-01-01',0,102),('FRIENDS',0,NULL,0,NULL,1,103);
/*!40000 ALTER TABLE `tv_series` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-12 19:04:29
