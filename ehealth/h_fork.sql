-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: h_fork
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add doctor',7,'add_doctor'),(26,'Can change doctor',7,'change_doctor'),(27,'Can delete doctor',7,'delete_doctor'),(28,'Can view doctor',7,'view_doctor'),(29,'Can add patient',8,'add_patient'),(30,'Can change patient',8,'change_patient'),(31,'Can delete patient',8,'delete_patient'),(32,'Can view patient',8,'view_patient'),(33,'Can add person',9,'add_person'),(34,'Can change person',9,'change_person'),(35,'Can delete person',9,'delete_person'),(36,'Can view person',9,'view_person'),(37,'Can add vital signs',10,'add_vitalsigns'),(38,'Can change vital signs',10,'change_vitalsigns'),(39,'Can delete vital signs',10,'delete_vitalsigns'),(40,'Can view vital signs',10,'view_vitalsigns'),(41,'Can add user account',11,'add_useraccount'),(42,'Can change user account',11,'change_useraccount'),(43,'Can delete user account',11,'delete_useraccount'),(44,'Can view user account',11,'view_useraccount'),(45,'Can add phone numbers',12,'add_phonenumbers'),(46,'Can change phone numbers',12,'change_phonenumbers'),(47,'Can delete phone numbers',12,'delete_phonenumbers'),(48,'Can view phone numbers',12,'view_phonenumbers'),(49,'Can add doctor acount',13,'add_doctoracount'),(50,'Can change doctor acount',13,'change_doctoracount'),(51,'Can delete doctor acount',13,'delete_doctoracount'),(52,'Can view doctor acount',13,'view_doctoracount'),(53,'Can add patient diagnostic',14,'add_patientdiagnostic'),(54,'Can change patient diagnostic',14,'change_patientdiagnostic'),(55,'Can delete patient diagnostic',14,'delete_patientdiagnostic'),(56,'Can view patient diagnostic',14,'view_patientdiagnostic');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'w_page','doctor'),(13,'w_page','doctoracount'),(8,'w_page','patient'),(14,'w_page','patientdiagnostic'),(9,'w_page','person'),(12,'w_page','phonenumbers'),(11,'w_page','useraccount'),(10,'w_page','vitalsigns');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-06-25 14:40:36.070638'),(2,'auth','0001_initial','2022-06-25 14:40:38.255985'),(3,'admin','0001_initial','2022-06-25 14:40:38.782491'),(4,'admin','0002_logentry_remove_auto_add','2022-06-25 14:40:38.829816'),(5,'admin','0003_logentry_add_action_flag_choices','2022-06-25 14:40:38.856404'),(6,'contenttypes','0002_remove_content_type_name','2022-06-25 14:40:39.177747'),(7,'auth','0002_alter_permission_name_max_length','2022-06-25 14:40:39.411029'),(8,'auth','0003_alter_user_email_max_length','2022-06-25 14:40:39.509968'),(9,'auth','0004_alter_user_username_opts','2022-06-25 14:40:39.568218'),(10,'auth','0005_alter_user_last_login_null','2022-06-25 14:40:39.765972'),(11,'auth','0006_require_contenttypes_0002','2022-06-25 14:40:39.785701'),(12,'auth','0007_alter_validators_add_error_messages','2022-06-25 14:40:39.816292'),(13,'auth','0008_alter_user_username_max_length','2022-06-25 14:40:40.156794'),(14,'auth','0009_alter_user_last_name_max_length','2022-06-25 14:40:40.372986'),(15,'auth','0010_alter_group_name_max_length','2022-06-25 14:40:40.473146'),(16,'auth','0011_update_proxy_permissions','2022-06-25 14:40:40.499856'),(17,'auth','0012_alter_user_first_name_max_length','2022-06-25 14:40:40.712891'),(18,'sessions','0001_initial','2022-06-25 14:40:40.865040'),(19,'w_page','0001_initial','2022-06-25 14:40:43.051272'),(20,'w_page','0002_phonenumbers_phone_content','2022-06-27 23:28:21.333772');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `doctor_id` int unsigned NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `person_id` int unsigned NOT NULL,
  PRIMARY KEY (`doctor_id`),
  KEY `doctor_person_id_a9bc8020_fk_person_person_id` (`person_id`),
  CONSTRAINT `doctor_person_id_a9bc8020_fk_person_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`person_id`),
  CONSTRAINT `doctor_chk_1` CHECK ((`doctor_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (6567888,'Medico',6567888),(12344556,'qwee',12344556),(12644135,'Ginecologo',12644135),(234345667,'qweqwe',234345667),(1003066588,'cirujano',1003066588),(1004066788,'Cirujano',1004066788);
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_acount`
--

DROP TABLE IF EXISTS `doctor_acount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_acount` (
  `doctor_account_id` int unsigned NOT NULL,
  `doctor_username` varchar(100) DEFAULT NULL,
  `doctor_email` varchar(100) DEFAULT NULL,
  `doctor_password` varchar(100) DEFAULT NULL,
  `doctor_id` int unsigned NOT NULL,
  PRIMARY KEY (`doctor_account_id`),
  KEY `doctor_acount_doctor_id_8a2c7768_fk_doctor_doctor_id` (`doctor_id`),
  CONSTRAINT `doctor_acount_doctor_id_8a2c7768_fk_doctor_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`),
  CONSTRAINT `doctor_acount_chk_1` CHECK ((`doctor_account_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_acount`
--

LOCK TABLES `doctor_acount` WRITE;
/*!40000 ALTER TABLE `doctor_acount` DISABLE KEYS */;
INSERT INTO `doctor_acount` VALUES (6567888,'Juan','6567888@gmail.com','Jua656',6567888),(12344556,'qwe','12344556@gmail.com','qwe123',12344556),(12644135,'Antonio','12644135@gmail.com','Ant126',12644135),(234345667,'qwe','234345667@gmail.com','qwe234',234345667),(1004066788,'Pedro','1004066788@gmail.com','Ped100',1004066788);
/*!40000 ALTER TABLE `doctor_acount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `patient_id` int unsigned NOT NULL,
  `person_id` int unsigned NOT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `patient_person_id_f2355195_fk_person_person_id` (`person_id`),
  CONSTRAINT `patient_person_id_f2355195_fk_person_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`person_id`),
  CONSTRAINT `patient_chk_1` CHECK ((`patient_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (12328,12328),(111111,111111),(454545,454545),(655555,655555),(892234,892234),(1111222,1111222),(1233434,1233434),(2333454,2333454),(13334556,13334556),(34335556,34335556),(55454547,55454547),(334544464,334544464),(555555555,555555555),(1003066555,1003066555),(1003066575,1003066575),(1003066576,1003066576);
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_diagnostic`
--

DROP TABLE IF EXISTS `patient_diagnostic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_diagnostic` (
  `diagnostic_id` int unsigned NOT NULL,
  `diagnostic_text` longtext NOT NULL,
  `doctor_id` int unsigned NOT NULL,
  `patient_id` int unsigned NOT NULL,
  PRIMARY KEY (`diagnostic_id`),
  UNIQUE KEY `patient_diagnostic_diagnostic_id_doctor_id_e80f57b5_uniq` (`diagnostic_id`,`doctor_id`),
  KEY `patient_diagnostic_doctor_id_06ca5ad7_fk_doctor_doctor_id` (`doctor_id`),
  KEY `patient_diagnostic_patient_id_4e44a7b2_fk_patient_patient_id` (`patient_id`),
  CONSTRAINT `patient_diagnostic_doctor_id_06ca5ad7_fk_doctor_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`),
  CONSTRAINT `patient_diagnostic_patient_id_4e44a7b2_fk_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`),
  CONSTRAINT `patient_diagnostic_chk_1` CHECK ((`diagnostic_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_diagnostic`
--

LOCK TABLES `patient_diagnostic` WRITE;
/*!40000 ALTER TABLE `patient_diagnostic` DISABLE KEYS */;
INSERT INTO `patient_diagnostic` VALUES (1,'Veo que estas muy bien',1003066588,1003066575),(2,'nada mal',6567888,12328),(123,'revisar los pulmones',12644135,12328),(1234,'revisar presion todos los dias en la tarde',12644135,111111),(12456,'revisar temperatura',12644135,1003066555);
/*!40000 ALTER TABLE `patient_diagnostic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `person_id` int unsigned NOT NULL,
  `name` varchar(100) NOT NULL,
  `second_name` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) NOT NULL,
  `second_lastname` varchar(100) DEFAULT NULL,
  `age` int unsigned NOT NULL,
  PRIMARY KEY (`person_id`),
  CONSTRAINT `person_chk_1` CHECK ((`person_id` >= 0)),
  CONSTRAINT `person_chk_2` CHECK ((`age` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (0,'Adolfo','x','y','z',12),(123,'qwe','qwe','wqe','12',12),(12328,'qwe','wqe','qwe','qwe',1),(12387,'qw','qwe','qwe','qwe',1),(111111,'sir','astolf','now','time',15),(444444,'qw','qwe','qwe','qwe',1),(454545,'aang','avatar','none','none',12),(655555,'tux','sudo','nano','ls',14),(881109,'qwe','qwe','qwe','qwe',1),(892234,'Pedro','Luis','Snachez','Sanchez',33),(1111222,'Amarillo','verde','rosa','qwe',1),(1122222,'qwe','qwe','qwe','qwe',1),(1233434,'qweqewew','qwe','qwe','qwe',8),(2218222,'qwe','qwe','qwe','qwe',1),(2333454,'qwe','qwe','qwe','qwe',34),(6567888,'Nelson','Pablo','Jaramillo','Hojeda',45),(12344556,'qwe','qwe','qwe','qwe',1),(12644135,'Antonio','Fernando','Movilla','Quintero',44),(13334556,'qwe','qwe','qwe','qwe',1),(34335556,'qwe','qwe','qwe','qwe',1),(55454547,'katara','tribu sur','none','none',88),(234345667,'qwe','qwe','qwe','qwe',11),(334544464,'qqqqqq','wwwww','aaaaaa','ddddd',1),(555555555,'Mario','Armando','Mendoza','Ramos',45),(1003066555,'Nelson','David','Ortega','Blanco',22),(1003066575,'Nelson','David','Ortega','Blanco',20),(1003066576,'None','Astolf','Ortega','Blanco',20),(1003066577,'Nelson','David','Ortega','Blanco',20),(1003066578,'Nelson','David','Ortega','Blanco',20),(1003066579,'Nelson','David','Ortega','Blanco',20),(1003066588,'Nelson','David','Ortega','Blanco',20),(1003066599,'Nelson','David','Ortega','Blanco',20),(1004066788,'Camilo','Pablo','Torres','Fuentes',88);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone_numbers`
--

DROP TABLE IF EXISTS `phone_numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone_numbers` (
  `phone_number` varchar(10) NOT NULL,
  `patient_id` int unsigned NOT NULL,
  `phone_content` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`phone_number`),
  KEY `phone_numbers_patient_id_5af4aca8_fk_patient_patient_id` (`patient_id`),
  CONSTRAINT `phone_numbers_patient_id_5af4aca8_fk_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone_numbers`
--

LOCK TABLES `phone_numbers` WRITE;
/*!40000 ALTER TABLE `phone_numbers` DISABLE KEYS */;
INSERT INTO `phone_numbers` VALUES ('2',1003066555,'310450614');
/*!40000 ALTER TABLE `phone_numbers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_account`
--

DROP TABLE IF EXISTS `user_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_account` (
  `user_account_id` int unsigned NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `patient_id` int unsigned NOT NULL,
  PRIMARY KEY (`user_account_id`),
  KEY `user_account_patient_id_705cf6c1_fk_patient_patient_id` (`patient_id`),
  CONSTRAINT `user_account_patient_id_705cf6c1_fk_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`),
  CONSTRAINT `user_account_chk_1` CHECK ((`user_account_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_account`
--

LOCK TABLES `user_account` WRITE;
/*!40000 ALTER TABLE `user_account` DISABLE KEYS */;
INSERT INTO `user_account` VALUES (12328,'12328@gmail.com','qwe123','qwe',12328),(111111,'111111@gmail.com','111111','sir',111111),(454545,'454545@gmail.com','454545','aang',454545),(655555,'655555@gmail.com','tux655','tux',655555),(892234,'892234@gmail.com','Ped892','Pedro',892234),(1111222,'1111222@gmail.com','Ama111','Amarillo',1111222),(2333454,'2333454@gmail.com','qwe233','qwe',2333454),(13334556,'13334556@gmail.com','qwe133','qwe',13334556),(34335556,'34335556@gmail.com','qwe343','qwe',34335556),(55454547,'55454547@gmail.com','kat554','katara',55454547),(334544464,'334544464@gmail.com','qqq334','qqqqqq',334544464),(555555555,'555555555@gmail.com','Mar555','Mario',555555555),(1003066555,'David@gmail.com','Ortega','Nelson',1003066555);
/*!40000 ALTER TABLE `user_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vital_signs`
--

DROP TABLE IF EXISTS `vital_signs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vital_signs` (
  `register_number` int NOT NULL AUTO_INCREMENT,
  `oxigen` double DEFAULT NULL,
  `heart_rate` double DEFAULT NULL,
  `temperature` double DEFAULT NULL,
  `resp_rate` double DEFAULT NULL,
  `weight` int unsigned DEFAULT NULL,
  `height` int unsigned DEFAULT NULL,
  `day_taken` int unsigned DEFAULT NULL,
  `year_taken` int unsigned DEFAULT NULL,
  `month_taken` int unsigned DEFAULT NULL,
  `hour_taken` int unsigned DEFAULT NULL,
  `patient_id` int unsigned NOT NULL,
  PRIMARY KEY (`register_number`),
  KEY `vital_signs_patient_id_1f798dbe_fk_patient_patient_id` (`patient_id`),
  CONSTRAINT `vital_signs_patient_id_1f798dbe_fk_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`),
  CONSTRAINT `vital_signs_chk_1` CHECK ((`weight` >= 0)),
  CONSTRAINT `vital_signs_chk_2` CHECK ((`height` >= 0)),
  CONSTRAINT `vital_signs_chk_3` CHECK ((`day_taken` >= 0)),
  CONSTRAINT `vital_signs_chk_4` CHECK ((`year_taken` >= 0)),
  CONSTRAINT `vital_signs_chk_5` CHECK ((`month_taken` >= 0)),
  CONSTRAINT `vital_signs_chk_6` CHECK ((`hour_taken` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vital_signs`
--

LOCK TABLES `vital_signs` WRITE;
/*!40000 ALTER TABLE `vital_signs` DISABLE KEYS */;
INSERT INTO `vital_signs` VALUES (1,0,99,26.37,110,100,80,1,2022,6,0,1003066575),(2,95,99,30.66,110,100,80,1,2022,7,10,1003066575),(3,95,99,32.19,110,100,80,1,2022,7,11,1003066575);
/*!40000 ALTER TABLE `vital_signs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-18 21:04:52
