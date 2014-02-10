CREATE DATABASE  IF NOT EXISTS `hc` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `hc`;
-- MySQL dump 10.13  Distrib 5.6.11, for Win32 (x86)
--
-- Host: localhost    Database: hc
-- ------------------------------------------------------
-- Server version	5.6.13

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
-- Table structure for table `name_map`
--

DROP TABLE IF EXISTS `name_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `name_map` (
  `category` varchar(70) DEFAULT NULL,
  `tblname` varchar(70) DEFAULT NULL,
  `abbr` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `name_map`
--

LOCK TABLES `name_map` WRITE;
/*!40000 ALTER TABLE `name_map` DISABLE KEYS */;
INSERT INTO `name_map` VALUES ('Hospital_Process_of_Care_Measures','children_s_asthma','POC_csa'),('Hospital_Process_of_Care_Measures','heart_attack','POC_ha'),('Hospital_Process_of_Care_Measures','heart_failure','POC_hf'),('Hospital_Process_of_Care_Measures','pneumonia','POC_p'),('Hospital_Process_of_Care_Measures','surgical_care_improvement_project','POC_scip'),('Hospital_Value_Based_Purchasing','Acute_Myocardial_Infarction_Scores','HVBP_amis'),('Hospital_Value_Based_Purchasing','Healthcare_Associated_Infection_Scores','HVBP_hais'),('Hospital_Value_Based_Purchasing','Heart_Failure_Scores','HVBP_hfs'),('Hospital_Value_Based_Purchasing','Patient_Experience_of_Care_Domain_Scores_HCAHPS_','HVBP_peocdsh'),('Hospital_Value_Based_Purchasing','Pneumonia_Scores','HVBP_ps'),('Hospital_Value_Based_Purchasing','Surgical_Care_Improvement_Project_Scores','HVBP_scips'),('Hospital_Value_Based_Purchasing','Total_Performance_Scores','HVBP_tps'),('None','Emergency Department Care Measures','EDCM'),('None','Healthcare Associated Infections','HAI'),('None','Hospital Acquired Condition Measures','HACM'),('None','Hospital ACS Measures','HAM'),('None','Hospital General Information','HGI'),('None','Hospital Medicare Volume Measures','HMVM'),('None','Hospital Outcome Of Care Measures','HOOCM'),('None','Hospital Readmission Reduction','HRR'),('None','Hospital Structural Measures Cardiac Surgery Registry','HSMCSR'),('None','Medicare Spending Per Patient','MSPP'),('None','Preventive Care Measures','PCM'),('None','Spending Breakdown by Claim','SBBC'),('None','Survey of Patients Hospital Experiences HCAHPS','SOPHEH'),('None','Use Of Medical Imaging Measures','UOMIM');
/*!40000 ALTER TABLE `name_map` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-29  2:13:32
