-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-08-2022 a las 08:22:05
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `eventos_cs`
--

CREATE DATABASE `eventos_cs`;
USE `eventos_cs`;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona_registrada`
--

CREATE TABLE `persona_registrada` (
	`id_registrado` INT NOT NULL,
    `persona` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `password` VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
	`id_administrador` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participante`
--

CREATE TABLE `participante` (
	`id_participante` INT NOT NULL,
	`universidad` VARCHAR(100) NOT NULL,
	`ciclo` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ponente`
--

CREATE TABLE `ponente` (
	`id_ponente` INT NOT NULL,
	`grado_academico` VARCHAR(100) NOT NULL,
	`descripcion` TEXT NOT NULL,
	`especialidad` VARCHAR(50) NOT NULL,
	`telefono` VARCHAR(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evento`
--

CREATE TABLE `evento` (
	`id_evento` INT NOT NULL,
	`titulo` VARCHAR(100) NOT NULL,
	`tema` VARCHAR(200) NOT NULL,
	`descripcion` TEXT NOT NULL,
	`id_administrador` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evento_ponente`
--

CREATE TABLE `evento_ponente` (
	`id_evento` INT NOT NULL,
	`id_ponente` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participante_concurso`
--

CREATE TABLE `evento_participante` (
	`id_evento` INT NOT NULL,
	`id_participante` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Indices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `persona_registrada`
	ADD PRIMARY KEY (`id_registrado`),
	ADD UNIQUE KEY `id_registrado_UNIQUE` (`id_registrado`);

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
	ADD PRIMARY KEY (`id_administrador`),
	ADD UNIQUE KEY `id_administrador_UNIQUE` (`id_administrador`);

--
-- Indices de la tabla `participante`
--
ALTER TABLE `participante`
	ADD PRIMARY KEY (`id_participante`),
	ADD UNIQUE KEY `id_participante_UNIQUE` (`id_participante`);

--
-- Indices de la tabla `ponente`
--
ALTER TABLE `ponente`
	ADD PRIMARY KEY (`id_ponente`),
	ADD UNIQUE KEY `id_ponente_UNIQUE` (`id_ponente`);

--
-- Indices de la tabla `evento`
--
ALTER TABLE `evento`
	ADD PRIMARY KEY (`id_evento`),
	ADD UNIQUE KEY `id_eventos_UNIQUE` (`id_evento`);

--
-- Indices de la tabla `evento_ponente`
--
ALTER TABLE `evento_ponente`
	ADD PRIMARY KEY (`id_evento`, `id_ponente`);

--
-- Indices de la tabla `participante_concurso`
--
ALTER TABLE `evento_participante`
	ADD PRIMARY KEY (`id_evento`, `id_participante`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador`
--
ALTER TABLE `administrador`
	ADD CONSTRAINT `id_administrador` FOREIGN KEY (`id_administrador`) REFERENCES `persona_registrada` (`id_registrado`) ON DELETE NO ACTION ON UPDATE NO ACTION;
  
--
-- Filtros para la tabla `participante`
--
ALTER TABLE `participante`
	ADD CONSTRAINT `id_participante` FOREIGN KEY (`id_participante`) REFERENCES `persona_registrada` (`id_registrado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `participante`
--
ALTER TABLE `ponente`
	ADD CONSTRAINT `id_ponente` FOREIGN KEY (`id_ponente`) REFERENCES `persona_registrada` (`id_registrado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `evento`
--
ALTER TABLE `evento`
  ADD CONSTRAINT `id_administrador` FOREIGN KEY (`id_administrador`) REFERENCES `administrador` (`id_administrador`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `evento_ponente`
--
ALTER TABLE `evento_ponente`
  ADD CONSTRAINT `id_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_ponente` FOREIGN KEY (`id_ponente`) REFERENCES `ponente` (`id_ponente`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `participante_concurso`
--
ALTER TABLE `evento_participante`
  ADD CONSTRAINT `id_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_participante` FOREIGN KEY (`id_participante`) REFERENCES `participante` (`id_participante`) ON DELETE NO ACTION ON UPDATE NO ACTION;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
