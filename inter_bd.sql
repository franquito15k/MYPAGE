-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-11-2024 a las 04:35:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inter_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descargas_videos`
--

CREATE TABLE `descargas_videos` (
  `idDescarga` int(11) NOT NULL,
  `cantidades` int(11) DEFAULT 1,
  `nombre_video` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `descargas_videos`
--

INSERT INTO `descargas_videos` (`idDescarga`, `cantidades`, `nombre_video`) VALUES
(9, 3, 'TARJETA GRÁFICA DE $25 vs $2500.mp4'),
(10, 1, 'Ridiculous Engine Swaps in Car Mechanic Simulator.mp4'),
(11, 2, '😱¡¡DIOOOS!! LA BRUTAL PRIMERA LEGENDARIA DE JAYCE (ARCANE SKIN) -REACCIÓN Y GAMEPLAY.mp4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `clave` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `descargas_videos`
--
ALTER TABLE `descargas_videos`
  ADD PRIMARY KEY (`idDescarga`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `descargas_videos`
--
ALTER TABLE `descargas_videos`
  MODIFY `idDescarga` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
