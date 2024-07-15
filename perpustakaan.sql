-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 15, 2024 at 08:15 AM
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
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `penulis` varchar(255) NOT NULL,
  `penerbit` varchar(255) DEFAULT NULL,
  `tahun_terbit` int(11) DEFAULT NULL,
  `konten` text DEFAULT NULL,
  `iktisar` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id`, `judul`, `penulis`, `penerbit`, `tahun_terbit`, `konten`, `iktisar`) VALUES
(1, 'Mathematics for Machine Learning', 'Marc Peter Deisenroth', 'Cambridge University Press', 2020, 'Introduction, Linear Algebra, Calculus, Probability', 'A comprehensive introduction to the mathematical foundations of machine learning.'),
(2, 'Deep Learning', 'Ian Goodfellow', 'MIT Press', 2016, 'Introduction, Deep Networks, Optimization', 'An authoritative textbook on deep learning by prominent researchers in the field.'),
(3, 'Clean Code', 'Robert C. Martin', 'Prentice Hall', 2008, 'Introduction, Meaningful Names, Functions', 'A handbook of agile software craftsmanship that provides guidelines for writing clean and maintainable code.'),
(4, 'Design Patterns', 'Erich Gamma', 'Addison-Wesley', 1994, 'Introduction, Creational Patterns, Structural Patterns', 'A catalog of object-oriented design patterns and best practices.'),
(5, 'The Pragmatic Programmer', 'Andrew Hunt', 'Addison-Wesley', 1999, 'Introduction, A Pragmatic Approach, The Basic Tools', 'A book about becoming a better programmer by adopting a pragmatic approach to software development.'),
(6, 'Deep Learning for Dummies', 'Naufal Rahfi Anugerah', 'Oxford Press', 2021, 'Introduction, Deep Networks, Neural Networks', 'Super deep learning book for beginners');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
