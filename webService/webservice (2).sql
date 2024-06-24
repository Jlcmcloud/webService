-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-06-2024 a las 20:21:53
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `webservice`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_detallepedido`
--

CREATE TABLE `app_detallepedido` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_estado`
--

CREATE TABLE `app_estado` (
  `id_estado` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `app_estado`
--

INSERT INTO `app_estado` (`id_estado`, `nombre`) VALUES
(1, 'validando'),
(2, 'confirmado'),
(3, '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_estadopago`
--

CREATE TABLE `app_estadopago` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `app_estadopago`
--

INSERT INTO `app_estadopago` (`id`, `nombre`) VALUES
(-5, 'Rechazo - Transacción con riesgo de posible fraude'),
(-4, 'Rechazo - Rechazada por parte del emisor'),
(-3, 'Rechazo - Error en Transacción'),
(-2, 'Rechazo - Se produjo fallo al procesar la transacc'),
(-1, 'Rechazo - Error en Transacción'),
(1, 'Aceptada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_metodopago`
--

CREATE TABLE `app_metodopago` (
  `id` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `app_metodopago`
--

INSERT INTO `app_metodopago` (`id`, `nombre`, `descripcion`) VALUES
('NC', 'N Cuotas sin interés', 'El comercio recibe el pago en un número de cuotas iguales y sin interés que el tarjetahabiente puede elegir de entre un rango de 2 y N (el valor N es definido por el comercio y no puede ser superior a 12)'),
('S2', '2 Cuotas sin interés', 'El comercio recibe el pago en 2 cuotas iguales sin interés.'),
('SI', '3 Cuotas sin interés', 'El comercio recibe el pago en 3 cuotas iguales sin interés.'),
('VC', 'Cuotas normales', 'El emisor ofrece al tarjetahabiente entre 2 y 48 cuotas. El emisor define si son sin interés (si ha establecido un rango de cuotas en promoción) o con interés. El emisor también puede ofrecer de 1 hasta 3 meses de pago diferida. Todo esto sin impacto para el comercio que en esta modalidad de cuotas siempre recibe el pago en 48 horas hábiles.'),
('VD', 'Venta Débito Redcompra', 'Pago con tarjeta de débito Redcompra.'),
('VN', 'Venta Normal', 'Pago en 1 cuota.'),
('VP', 'Venta Prepago', 'Pago con tarjeta de débito Redcompra.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_pago`
--

CREATE TABLE `app_pago` (
  `id_pago` int(11) NOT NULL,
  `monto` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado_pago_id` bigint(20) NOT NULL,
  `metodo_pago_id` varchar(20) NOT NULL,
  `pedido_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_transaccion`
--

CREATE TABLE `app_transaccion` (
  `id_transaccion` int(11) NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `pago_id` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('2dcfb4740bfff9f6d04156768f6fa9d1f2227bdd', '2024-06-22 01:02:26.789692', 3),
('5bd1d51f327ca4754a7652da95242969641f76ab', '2024-06-22 01:01:15.948471', 2),
('81a25458c87e5141608e885dc43b805b01fa05a5', '2024-06-22 00:58:17.241201', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add categoria producto', 7, 'add_categoriaproducto'),
(26, 'Can change categoria producto', 7, 'change_categoriaproducto'),
(27, 'Can delete categoria producto', 7, 'delete_categoriaproducto'),
(28, 'Can view categoria producto', 7, 'view_categoriaproducto'),
(29, 'Can add estado', 8, 'add_estado'),
(30, 'Can change estado', 8, 'change_estado'),
(31, 'Can delete estado', 8, 'delete_estado'),
(32, 'Can view estado', 8, 'view_estado'),
(33, 'Can add estado pago', 9, 'add_estadopago'),
(34, 'Can change estado pago', 9, 'change_estadopago'),
(35, 'Can delete estado pago', 9, 'delete_estadopago'),
(36, 'Can view estado pago', 9, 'view_estadopago'),
(37, 'Can add metodo pago', 10, 'add_metodopago'),
(38, 'Can change metodo pago', 10, 'change_metodopago'),
(39, 'Can delete metodo pago', 10, 'delete_metodopago'),
(40, 'Can view metodo pago', 10, 'view_metodopago'),
(41, 'Can add producto', 11, 'add_producto'),
(42, 'Can change producto', 11, 'change_producto'),
(43, 'Can delete producto', 11, 'delete_producto'),
(44, 'Can view producto', 11, 'view_producto'),
(45, 'Can add cliente', 12, 'add_cliente'),
(46, 'Can change cliente', 12, 'change_cliente'),
(47, 'Can delete cliente', 12, 'delete_cliente'),
(48, 'Can view cliente', 12, 'view_cliente'),
(49, 'Can add carrito', 13, 'add_carrito'),
(50, 'Can change carrito', 13, 'change_carrito'),
(51, 'Can delete carrito', 13, 'delete_carrito'),
(52, 'Can view carrito', 13, 'view_carrito'),
(53, 'Can add pedido', 14, 'add_pedido'),
(54, 'Can change pedido', 14, 'change_pedido'),
(55, 'Can delete pedido', 14, 'delete_pedido'),
(56, 'Can view pedido', 14, 'view_pedido'),
(57, 'Can add pago', 15, 'add_pago'),
(58, 'Can change pago', 15, 'change_pago'),
(59, 'Can delete pago', 15, 'delete_pago'),
(60, 'Can view pago', 15, 'view_pago'),
(61, 'Can add item carrito', 16, 'add_itemcarrito'),
(62, 'Can change item carrito', 16, 'change_itemcarrito'),
(63, 'Can delete item carrito', 16, 'delete_itemcarrito'),
(64, 'Can view item carrito', 16, 'view_itemcarrito'),
(65, 'Can add transaccion', 17, 'add_transaccion'),
(66, 'Can change transaccion', 17, 'change_transaccion'),
(67, 'Can delete transaccion', 17, 'delete_transaccion'),
(68, 'Can view transaccion', 17, 'view_transaccion'),
(69, 'Can add detalle pedido', 18, 'add_detallepedido'),
(70, 'Can change detalle pedido', 18, 'change_detallepedido'),
(71, 'Can delete detalle pedido', 18, 'delete_detallepedido'),
(72, 'Can view detalle pedido', 18, 'view_detallepedido'),
(73, 'Can add Token', 19, 'add_token'),
(74, 'Can change Token', 19, 'change_token'),
(75, 'Can delete Token', 19, 'delete_token'),
(76, 'Can view Token', 19, 'view_token'),
(77, 'Can add Token', 20, 'add_tokenproxy'),
(78, 'Can change Token', 20, 'change_tokenproxy'),
(79, 'Can delete Token', 20, 'delete_tokenproxy'),
(80, 'Can view Token', 20, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, '', NULL, 0, 'Setzler45', '', '', 'holamundo98@gmail.com', 0, 1, '2024-06-22 00:58:17.227709'),
(2, '', NULL, 0, 'Setzler55', '', '', 'holamundo98@gmail.com', 0, 1, '2024-06-22 01:01:15.931799'),
(3, 'pbkdf2_sha256$720000$Ok2b1fdq9QptXLC5gJk5UZ$3t+TZIH48XRud2q7t8JHjeOAOAYBUfV2smqGv86YtcI=', NULL, 0, 'Setzler56', '', '', '', 0, 1, '2024-06-22 01:02:25.545956');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_carrito`
--

CREATE TABLE `db_carrito` (
  `id` bigint(20) NOT NULL,
  `cliente_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `db_carrito`
--

INSERT INTO `db_carrito` (`id`, `cliente_id`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_cliente`
--

CREATE TABLE `db_cliente` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `create_at` date NOT NULL,
  `update_at` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `db_cliente`
--

INSERT INTO `db_cliente` (`id`, `nombre`, `email`, `direccion`, `create_at`, `update_at`, `user_id`) VALUES
(1, 'Setzler45', 'holamundo98@gmail.com', '', '2024-06-21', '2024-06-21', 1),
(2, 'Setzler55', 'holamundo98@gmail.com', '', '2024-06-21', '2024-06-21', 2),
(3, 'Setzler56', '', '', '2024-06-21', '2024-06-21', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_item_carrito`
--

CREATE TABLE `db_item_carrito` (
  `id` bigint(20) NOT NULL,
  `cant` int(11) NOT NULL,
  `carrito_id` bigint(20) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(13, 'app', 'carrito'),
(7, 'app', 'categoriaproducto'),
(12, 'app', 'cliente'),
(18, 'app', 'detallepedido'),
(8, 'app', 'estado'),
(9, 'app', 'estadopago'),
(16, 'app', 'itemcarrito'),
(10, 'app', 'metodopago'),
(15, 'app', 'pago'),
(14, 'app', 'pedido'),
(11, 'app', 'producto'),
(17, 'app', 'transaccion'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(19, 'authtoken', 'token'),
(20, 'authtoken', 'tokenproxy'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-14 23:47:01.486298'),
(2, 'auth', '0001_initial', '2024-06-14 23:47:02.006846'),
(3, 'admin', '0001_initial', '2024-06-14 23:47:02.123153'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-14 23:47:02.131153'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-14 23:47:02.139756'),
(6, 'app', '0001_initial', '2024-06-14 23:47:03.138071'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-06-14 23:47:03.211371'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-06-14 23:47:03.272502'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-06-14 23:47:03.337091'),
(10, 'auth', '0004_alter_user_username_opts', '2024-06-14 23:47:03.359098'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-06-14 23:47:03.408111'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-06-14 23:47:03.410909'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-06-14 23:47:03.421522'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-06-14 23:47:03.444831'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-06-14 23:47:03.466099'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-06-14 23:47:03.502219'),
(17, 'auth', '0011_update_proxy_permissions', '2024-06-14 23:47:03.522219'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-06-14 23:47:03.544223'),
(19, 'authtoken', '0001_initial', '2024-06-14 23:47:03.628531'),
(20, 'authtoken', '0002_auto_20160226_1747', '2024-06-14 23:47:03.666929'),
(21, 'authtoken', '0003_tokenproxy', '2024-06-14 23:47:03.672364'),
(22, 'authtoken', '0004_alter_tokenproxy_options', '2024-06-14 23:47:03.678479'),
(23, 'sessions', '0001_initial', '2024-06-14 23:47:03.718424'),
(24, 'app', '0002_delete_categoriaproducto_alter_pedido_iva_and_more', '2024-06-22 21:34:53.398233');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id_pedido` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `estado_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`id_pedido`, `subtotal`, `iva`, `total`, `fecha`, `cliente_id`, `estado_id`) VALUES
(1, 0, 0, 0, '2024-06-22', 1, 1),
(2, 15000, 19, 50000, '2024-06-22', 1, 1),
(3, 5000, 19, 50000, '2024-06-22', 2, 2),
(4, 5000, 19, 50000, '2024-06-22', 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` bigint(20) NOT NULL,
  `nombre_producto` varchar(50) NOT NULL,
  `precio` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre_producto`, `precio`, `cantidad`, `marca`, `descripcion`, `create_at`, `update_at`) VALUES
(1, 'Taladro', 15000, 10, 'Taladrin', 'a taladrar', '2024-06-22 22:06:34.488391', '2024-06-22 22:06:34.489864'),
(2, 'Martillo', 5000, 5, 'Mazon', 'un buen martillo para martillar todo lo que quieras', '2024-06-22 22:07:05.224589', '2024-06-22 22:07:05.224589');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `app_detallepedido`
--
ALTER TABLE `app_detallepedido`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_detallepedido_pedido_id_producto_id_f856e7b5_uniq` (`pedido_id`,`producto_id`),
  ADD KEY `app_detallepedido_producto_id_a0782732_fk_Producto_id` (`producto_id`);

--
-- Indices de la tabla `app_estado`
--
ALTER TABLE `app_estado`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `app_estadopago`
--
ALTER TABLE `app_estadopago`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `app_metodopago`
--
ALTER TABLE `app_metodopago`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `app_pago`
--
ALTER TABLE `app_pago`
  ADD PRIMARY KEY (`id_pago`),
  ADD KEY `app_pago_estado_pago_id_bbfd5ab4_fk_app_estadopago_id` (`estado_pago_id`),
  ADD KEY `app_pago_metodo_pago_id_f0c134e3_fk_app_metodopago_id` (`metodo_pago_id`),
  ADD KEY `app_pago_pedido_id_01188c3b_fk_pedido_id_pedido` (`pedido_id`);

--
-- Indices de la tabla `app_transaccion`
--
ALTER TABLE `app_transaccion`
  ADD PRIMARY KEY (`id_transaccion`),
  ADD KEY `app_transaccion_cliente_id_b9c5a30c_fk_db_cliente_id` (`cliente_id`),
  ADD KEY `app_transaccion_pago_id_61e7dd81_fk_app_pago_id_pago` (`pago_id`),
  ADD KEY `app_transaccion_pedido_id_b4e340e8_fk_pedido_id_pedido` (`pedido_id`);

--
-- Indices de la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `db_carrito`
--
ALTER TABLE `db_carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `db_carrito_cliente_id_8b7922d4_fk_db_cliente_id` (`cliente_id`);

--
-- Indices de la tabla `db_cliente`
--
ALTER TABLE `db_cliente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `db_cliente_user_id_d70d65b6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `db_item_carrito`
--
ALTER TABLE `db_item_carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `db_item_carrito_carrito_id_445a1f58_fk_db_carrito_id` (`carrito_id`),
  ADD KEY `db_item_carrito_pedido_id_83b82228_fk_pedido_id_pedido` (`pedido_id`),
  ADD KEY `db_item_carrito_producto_id_44361e86_fk_Producto_id` (`producto_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id_pedido`),
  ADD KEY `pedido_cliente_id_e6353bb4_fk_db_cliente_id` (`cliente_id`),
  ADD KEY `pedido_estado_id_0eca1334_fk_app_estado_id_estado` (`estado_id`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `app_detallepedido`
--
ALTER TABLE `app_detallepedido`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `app_estado`
--
ALTER TABLE `app_estado`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `app_estadopago`
--
ALTER TABLE `app_estadopago`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `app_pago`
--
ALTER TABLE `app_pago`
  MODIFY `id_pago` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `db_carrito`
--
ALTER TABLE `db_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `db_cliente`
--
ALTER TABLE `db_cliente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `db_item_carrito`
--
ALTER TABLE `db_item_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `app_detallepedido`
--
ALTER TABLE `app_detallepedido`
  ADD CONSTRAINT `app_detallepedido_pedido_id_78067cad_fk_pedido_id_pedido` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id_pedido`),
  ADD CONSTRAINT `app_detallepedido_producto_id_a0782732_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `app_pago`
--
ALTER TABLE `app_pago`
  ADD CONSTRAINT `app_pago_estado_pago_id_bbfd5ab4_fk_app_estadopago_id` FOREIGN KEY (`estado_pago_id`) REFERENCES `app_estadopago` (`id`),
  ADD CONSTRAINT `app_pago_metodo_pago_id_f0c134e3_fk_app_metodopago_id` FOREIGN KEY (`metodo_pago_id`) REFERENCES `app_metodopago` (`id`),
  ADD CONSTRAINT `app_pago_pedido_id_01188c3b_fk_pedido_id_pedido` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id_pedido`);

--
-- Filtros para la tabla `app_transaccion`
--
ALTER TABLE `app_transaccion`
  ADD CONSTRAINT `app_transaccion_cliente_id_b9c5a30c_fk_db_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `db_cliente` (`id`),
  ADD CONSTRAINT `app_transaccion_pago_id_61e7dd81_fk_app_pago_id_pago` FOREIGN KEY (`pago_id`) REFERENCES `app_pago` (`id_pago`),
  ADD CONSTRAINT `app_transaccion_pedido_id_b4e340e8_fk_pedido_id_pedido` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id_pedido`);

--
-- Filtros para la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `db_carrito`
--
ALTER TABLE `db_carrito`
  ADD CONSTRAINT `db_carrito_cliente_id_8b7922d4_fk_db_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `db_cliente` (`id`);

--
-- Filtros para la tabla `db_cliente`
--
ALTER TABLE `db_cliente`
  ADD CONSTRAINT `db_cliente_user_id_d70d65b6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `db_item_carrito`
--
ALTER TABLE `db_item_carrito`
  ADD CONSTRAINT `db_item_carrito_carrito_id_445a1f58_fk_db_carrito_id` FOREIGN KEY (`carrito_id`) REFERENCES `db_carrito` (`id`),
  ADD CONSTRAINT `db_item_carrito_pedido_id_83b82228_fk_pedido_id_pedido` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id_pedido`),
  ADD CONSTRAINT `db_item_carrito_producto_id_44361e86_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_cliente_id_e6353bb4_fk_db_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `db_cliente` (`id`),
  ADD CONSTRAINT `pedido_estado_id_0eca1334_fk_app_estado_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `app_estado` (`id_estado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
