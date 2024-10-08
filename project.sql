-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 08, 2024 at 10:41 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_user_name` varchar(30) NOT NULL,
  `admin_pass` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_user_name`, `admin_pass`) VALUES
(1, 'zahid', 'zahid123'),
(2, 'toha', 'toha123');

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `bus_id` int(11) NOT NULL,
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
  `stopage10` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`bus_id`, `bus_name`, `stopage1`, `stopage2`, `stopage3`, `stopage4`, `stopage5`, `stopage6`, `stopage7`, `stopage8`, `stopage9`, `stopage10`) VALUES
(1, 'ABC', 'A', 'B', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'asdfas', 'asdfgasd', 'asdfawee', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '15 number', 'Azimpur', 'New Market', 'Science Lab', 'Jigatola', 'Shangkar', 'Mohammadpur', NULL, NULL, NULL, NULL),
(4, 'Thikana', 'Sign Board', 'Jatrabari', 'Chankharpool', 'Azimpur', 'New Market', 'Science Lab', 'Kalyanpur', 'Gabtoli', 'Savar', 'Chandra'),
(5, 'Savar', 'Shadarghat', 'Gulisthan', 'Paltan', 'Shahbag', 'Science Lab', 'Kalyanpur', 'Gabtoli', 'Savar', 'Nabinagar', 'Chandra');

-- --------------------------------------------------------

--
-- Table structure for table `passenger`
--

CREATE TABLE `passenger` (
  `passenger_id` int(11) NOT NULL,
  `passenger_name` varchar(30) NOT NULL,
  `passenger_nid` int(11) NOT NULL,
  `passenger_balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `passenger`
--

INSERT INTO `passenger` (`passenger_id`, `passenger_name`, `passenger_nid`, `passenger_balance`) VALUES
(1, 'Netul', 12345, 1000),
(2, 'Mitul', 45678, 1000),
(3, 'Roni', 147852, 200),
(4, 'Fardin', 456789, 400),
(5, 'Nisa', 654987, 200),
(6, '', 0, 200);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`bus_id`);

--
-- Indexes for table `passenger`
--
ALTER TABLE `passenger`
  ADD PRIMARY KEY (`passenger_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `bus_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `passenger`
--
ALTER TABLE `passenger`
  MODIFY `passenger_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
