-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 04, 2024 at 12:18 PM
-- Server version: 10.6.18-MariaDB-cll-lve
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inshopping_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `authuser_account`
--

CREATE TABLE `authuser_account` (
  `id` bigint(20) NOT NULL,
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
  `phone` varchar(15) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `authuser_account`
--

INSERT INTO `authuser_account` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`) VALUES
(1, 'pbkdf2_sha256$600000$IojZlJHs1b7lyWM20Rlt8B$OnD1r1UiA2T4KJGfBdj4vJAX/8eDiMM6rQWEwgGeHS8=', '2024-12-04 06:16:49.941298', 1, 'mahsan', '', '', 'mahsan.ps@gmail.com', 1, 1, '2024-12-04 06:13:39.604613', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `authuser_account_groups`
--

CREATE TABLE `authuser_account_groups` (
  `id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `authuser_account_user_permissions`
--

CREATE TABLE `authuser_account_user_permissions` (
  `id` bigint(20) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add Account', 1, 'add_account'),
(2, 'Can change Account', 1, 'change_account'),
(3, 'Can delete Account', 1, 'delete_account'),
(4, 'Can view Account', 1, 'view_account'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add blog', 7, 'add_blog'),
(26, 'Can change blog', 7, 'change_blog'),
(27, 'Can delete blog', 7, 'delete_blog'),
(28, 'Can view blog', 7, 'view_blog'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add color', 9, 'add_color'),
(34, 'Can change color', 9, 'change_color'),
(35, 'Can delete color', 9, 'delete_color'),
(36, 'Can view color', 9, 'view_color'),
(37, 'Can add contact', 10, 'add_contact'),
(38, 'Can change contact', 10, 'change_contact'),
(39, 'Can delete contact', 10, 'delete_contact'),
(40, 'Can view contact', 10, 'view_contact'),
(41, 'Can add homepage content', 11, 'add_homepagecontent'),
(42, 'Can change homepage content', 11, 'change_homepagecontent'),
(43, 'Can delete homepage content', 11, 'delete_homepagecontent'),
(44, 'Can view homepage content', 11, 'view_homepagecontent'),
(45, 'Can add order', 12, 'add_order'),
(46, 'Can change order', 12, 'change_order'),
(47, 'Can delete order', 12, 'delete_order'),
(48, 'Can view order', 12, 'view_order'),
(49, 'Can add otp', 13, 'add_otp'),
(50, 'Can change otp', 13, 'change_otp'),
(51, 'Can delete otp', 13, 'delete_otp'),
(52, 'Can view otp', 13, 'view_otp'),
(53, 'Can add product', 14, 'add_product'),
(54, 'Can change product', 14, 'change_product'),
(55, 'Can delete product', 14, 'delete_product'),
(56, 'Can view product', 14, 'view_product'),
(57, 'Can add shop', 15, 'add_shop'),
(58, 'Can change shop', 15, 'change_shop'),
(59, 'Can delete shop', 15, 'delete_shop'),
(60, 'Can view shop', 15, 'view_shop'),
(61, 'Can add sub category', 16, 'add_subcategory'),
(62, 'Can change sub category', 16, 'change_subcategory'),
(63, 'Can delete sub category', 16, 'delete_subcategory'),
(64, 'Can view sub category', 16, 'view_subcategory'),
(65, 'Can add shop image', 17, 'add_shopimage'),
(66, 'Can change shop image', 17, 'change_shopimage'),
(67, 'Can delete shop image', 17, 'delete_shopimage'),
(68, 'Can view shop image', 17, 'view_shopimage'),
(69, 'Can add shop auth', 18, 'add_shopauth'),
(70, 'Can change shop auth', 18, 'change_shopauth'),
(71, 'Can delete shop auth', 18, 'delete_shopauth'),
(72, 'Can view shop auth', 18, 'view_shopauth'),
(73, 'Can add product variation', 19, 'add_productvariation'),
(74, 'Can change product variation', 19, 'change_productvariation'),
(75, 'Can delete product variation', 19, 'delete_productvariation'),
(76, 'Can view product variation', 19, 'view_productvariation'),
(77, 'Can add product image', 20, 'add_productimage'),
(78, 'Can change product image', 20, 'change_productimage'),
(79, 'Can delete product image', 20, 'delete_productimage'),
(80, 'Can view product image', 20, 'view_productimage'),
(81, 'Can add order item', 21, 'add_orderitem'),
(82, 'Can change order item', 21, 'change_orderitem'),
(83, 'Can delete order item', 21, 'delete_orderitem'),
(84, 'Can view order item', 21, 'view_orderitem'),
(85, 'Can add order delivery', 22, 'add_orderdelivery'),
(86, 'Can change order delivery', 22, 'change_orderdelivery'),
(87, 'Can delete order delivery', 22, 'delete_orderdelivery'),
(88, 'Can view order delivery', 22, 'view_orderdelivery'),
(89, 'Can add bank account', 23, 'add_bankaccount'),
(90, 'Can change bank account', 23, 'change_bankaccount'),
(91, 'Can delete bank account', 23, 'delete_bankaccount'),
(92, 'Can view bank account', 23, 'view_bankaccount'),
(93, 'Can add account info', 24, 'add_accountinfo'),
(94, 'Can change account info', 24, 'change_accountinfo'),
(95, 'Can delete account info', 24, 'delete_accountinfo'),
(96, 'Can view account info', 24, 'view_accountinfo');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-12-04 06:40:50.486225', '1', 'مد و پوشاک زنان', 1, '[{\"added\": {}}]', 8, 1),
(2, '2024-12-04 06:41:22.860300', '1', 'مد و پوشاک زنان', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 8, 1),
(3, '2024-12-04 06:42:21.595803', '2', 'مد و پوشاک مردان', 1, '[{\"added\": {}}]', 8, 1),
(4, '2024-12-04 06:43:18.630054', '3', 'پوشاک کودکان', 1, '[{\"added\": {}}]', 8, 1),
(5, '2024-12-04 06:44:49.007319', '4', 'وسایل حیوانات خانگی', 1, '[{\"added\": {}}]', 8, 1),
(6, '2024-12-04 06:46:19.486319', '5', 'آرایشی بهداشتی', 1, '[{\"added\": {}}]', 8, 1),
(7, '2024-12-04 06:47:28.238266', '6', 'ورزشی و سفر', 1, '[{\"added\": {}}]', 8, 1),
(8, '2024-12-04 06:48:29.169115', '7', 'خانه و آشپزخانه', 1, '[{\"added\": {}}]', 8, 1),
(9, '2024-12-04 06:49:08.165711', '8', 'هنر و صنایع دستی', 1, '[{\"added\": {}}]', 8, 1),
(10, '2024-12-04 06:50:22.361817', '9', 'بازی و سرگرمی', 1, '[{\"added\": {}}]', 8, 1),
(11, '2024-12-04 06:51:04.783800', '1', 'مشکی', 1, '[{\"added\": {}}]', 9, 1),
(12, '2024-12-04 06:51:09.283956', '2', 'سفید', 1, '[{\"added\": {}}]', 9, 1),
(13, '2024-12-04 06:51:14.721771', '3', 'سورمه ای', 1, '[{\"added\": {}}]', 9, 1),
(14, '2024-12-04 06:51:19.080824', '4', 'سبز', 1, '[{\"added\": {}}]', 9, 1),
(15, '2024-12-04 06:51:27.018456', '5', 'یشمی', 1, '[{\"added\": {}}]', 9, 1),
(16, '2024-12-04 06:51:31.709581', '6', 'بنفش', 1, '[{\"added\": {}}]', 9, 1),
(17, '2024-12-04 06:51:39.922596', '7', 'آبی', 1, '[{\"added\": {}}]', 9, 1),
(18, '2024-12-04 06:51:48.256618', '8', 'نارنجی', 1, '[{\"added\": {}}]', 9, 1),
(19, '2024-12-04 06:51:52.196120', '9', 'نقره ای', 1, '[{\"added\": {}}]', 9, 1),
(20, '2024-12-04 06:51:59.272815', '10', 'کرم', 1, '[{\"added\": {}}]', 9, 1),
(21, '2024-12-04 06:52:14.222551', '11', 'قهوه ای', 1, '[{\"added\": {}}]', 9, 1),
(22, '2024-12-04 06:52:21.207876', '12', 'قرمز', 1, '[{\"added\": {}}]', 9, 1),
(23, '2024-12-04 06:52:26.702230', '13', 'صورتی', 1, '[{\"added\": {}}]', 9, 1),
(24, '2024-12-04 06:52:33.658164', '14', 'طلایی', 1, '[{\"added\": {}}]', 9, 1),
(25, '2024-12-04 06:52:38.070864', '15', 'طوسی', 1, '[{\"added\": {}}]', 9, 1),
(26, '2024-12-04 06:52:43.602605', '16', 'زرد', 1, '[{\"added\": {}}]', 9, 1),
(27, '2024-12-04 06:52:48.055685', '17', 'زرشکی', 1, '[{\"added\": {}}]', 9, 1),
(28, '2024-12-04 06:54:52.003523', '1', 'کت زنانه', 1, '[{\"added\": {}}]', 16, 1),
(29, '2024-12-04 06:55:35.684596', '2', 'تاپ و کراپ', 1, '[{\"added\": {}}]', 16, 1),
(30, '2024-12-04 06:56:22.150273', '3', 'تیشرت زنانه', 1, '[{\"added\": {}}]', 16, 1),
(31, '2024-12-04 06:57:07.366033', '4', 'شلوار زنانه', 1, '[{\"added\": {}}]', 16, 1),
(32, '2024-12-04 06:57:55.317680', '5', 'پبراهن زنانه', 1, '[{\"added\": {}}]', 16, 1),
(33, '2024-12-04 06:58:50.713222', '6', 'شلوارک زنانه', 1, '[{\"added\": {}}]', 16, 1),
(34, '2024-12-04 06:59:35.649258', '7', 'دامن', 1, '[{\"added\": {}}]', 16, 1),
(35, '2024-12-04 07:00:03.380164', '8', 'سرهمی', 1, '[{\"added\": {}}]', 16, 1),
(36, '2024-12-04 07:01:04.159706', '9', 'شومیز', 1, '[{\"added\": {}}]', 16, 1),
(37, '2024-12-04 07:01:48.890064', '10', 'ست زنانه', 1, '[{\"added\": {}}]', 16, 1),
(38, '2024-12-04 07:02:44.778265', '11', 'کیف زنانه', 1, '[{\"added\": {}}]', 16, 1),
(39, '2024-12-04 07:03:45.331567', '12', 'کفش و صندل', 1, '[{\"added\": {}}]', 16, 1),
(40, '2024-12-04 07:04:29.135515', '13', 'مانتو', 1, '[{\"added\": {}}]', 16, 1),
(41, '2024-12-04 07:05:07.605134', '14', 'شال و روسری', 1, '[{\"added\": {}}]', 16, 1),
(42, '2024-12-04 07:05:54.991827', '15', 'کلاه زنانه', 1, '[{\"added\": {}}]', 16, 1),
(43, '2024-12-04 07:07:05.774715', '16', 'کت مردانه', 1, '[{\"added\": {}}]', 16, 1),
(44, '2024-12-04 07:07:49.181312', '17', 'پیراهن مردانه', 1, '[{\"added\": {}}]', 16, 1),
(45, '2024-12-04 07:08:29.444371', '18', 'تیشرت مردانه', 1, '[{\"added\": {}}]', 16, 1),
(46, '2024-12-04 07:09:07.727882', '19', 'شلوار مردانه', 1, '[{\"added\": {}}]', 16, 1),
(47, '2024-12-04 07:09:54.601293', '20', 'شلوارک مردانه', 1, '[{\"added\": {}}]', 16, 1),
(48, '2024-12-04 07:10:38.842284', '21', 'ست مردانه', 1, '[{\"added\": {}}]', 16, 1),
(49, '2024-12-04 07:11:40.881551', '22', 'کفش مردانه', 1, '[{\"added\": {}}]', 16, 1),
(50, '2024-12-04 07:12:17.069988', '23', 'کیف مردانه', 1, '[{\"added\": {}}]', 16, 1),
(51, '2024-12-04 07:12:47.586919', '24', 'کلاه مردانه', 1, '[{\"added\": {}}]', 16, 1),
(52, '2024-12-04 07:13:45.505349', '25', 'کت بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(53, '2024-12-04 07:14:12.366573', '26', 'تیشرت بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(54, '2024-12-04 07:15:06.329293', '27', 'سرهمی بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(55, '2024-12-04 07:15:47.284863', '28', 'سرهمی بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(56, '2024-12-04 07:16:54.050019', '29', 'پیراهن دخترانه', 1, '[{\"added\": {}}]', 16, 1),
(57, '2024-12-04 07:17:35.888233', '30', 'پیراهن پسرانه', 1, '[{\"added\": {}}]', 16, 1),
(58, '2024-12-04 07:18:24.867971', '31', 'ست پچگانه', 1, '[{\"added\": {}}]', 16, 1),
(59, '2024-12-04 07:19:14.615136', '32', 'دورس و هودی', 1, '[{\"added\": {}}]', 16, 1),
(60, '2024-12-04 07:20:11.444594', '33', 'بافت و هودی', 1, '[{\"added\": {}}]', 16, 1),
(61, '2024-12-04 07:20:57.816817', '34', 'دامن بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(62, '2024-12-04 07:21:43.940012', '35', 'شلوار بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(63, '2024-12-04 07:22:21.998774', '36', 'شلوارک بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(64, '2024-12-04 07:22:58.643836', '37', 'کفش بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(65, '2024-12-04 07:23:25.124879', '38', 'کلاه بچگانه', 1, '[{\"added\": {}}]', 16, 1),
(66, '2024-12-04 07:26:39.366676', '39', 'محصولات خوراکی حیوانات', 1, '[{\"added\": {}}]', 16, 1),
(67, '2024-12-04 07:27:38.713383', '40', 'لباس و قلاده', 1, '[{\"added\": {}}]', 16, 1),
(68, '2024-12-04 07:28:28.366683', '41', 'باکس و سایر ملزومات', 1, '[{\"added\": {}}]', 16, 1),
(69, '2024-12-04 07:29:26.224540', '42', 'وسایل بازی', 1, '[{\"added\": {}}]', 16, 1),
(70, '2024-12-04 07:30:13.432845', '43', 'لوازم آرایشی', 1, '[{\"added\": {}}]', 16, 1),
(71, '2024-12-04 07:30:50.709935', '44', 'مراقبت از مو', 1, '[{\"added\": {}}]', 16, 1),
(72, '2024-12-04 07:31:26.640036', '45', 'مراقبت از پوست', 1, '[{\"added\": {}}]', 16, 1),
(73, '2024-12-04 07:32:20.080386', '46', 'عطر و ادکن', 1, '[{\"added\": {}}]', 16, 1),
(74, '2024-12-04 07:33:40.166660', '47', 'لوازم برقی شخصی', 1, '[{\"added\": {}}]', 16, 1),
(75, '2024-12-04 07:34:39.585947', '48', 'بهداشتی', 1, '[{\"added\": {}}]', 16, 1),
(76, '2024-12-04 07:35:54.002224', '49', 'ظروف و لوازم دکوری سنتی', 1, '[{\"added\": {}}]', 16, 1),
(77, '2024-12-04 07:36:43.719896', '50', 'اکسسوری و زیورآلات', 1, '[{\"added\": {}}]', 16, 1),
(78, '2024-12-04 07:38:02.250510', '51', 'لوازم پذیرایی', 1, '[{\"added\": {}}]', 16, 1),
(79, '2024-12-04 07:38:29.142630', '52', 'لوازم پخت و پز', 1, '[{\"added\": {}}]', 16, 1),
(80, '2024-12-04 07:39:22.271134', '53', 'لوازم اتاق خواب', 1, '[{\"added\": {}}]', 16, 1),
(81, '2024-12-04 07:39:49.682902', '54', 'دکوراسیون خانگی', 1, '[{\"added\": {}}]', 16, 1),
(82, '2024-12-04 07:41:44.109919', '55', 'کمپینگ و کوهنوردی', 1, '[{\"added\": {}}]', 16, 1),
(83, '2024-12-04 07:42:45.383527', '56', 'لوازم ورزشی', 1, '[{\"added\": {}}]', 16, 1),
(84, '2024-12-04 07:43:17.491992', '57', 'ساک و چمدان', 1, '[{\"added\": {}}]', 16, 1),
(85, '2024-12-04 07:43:47.742907', '58', 'لباس ورزشی', 1, '[{\"added\": {}}]', 16, 1),
(86, '2024-12-04 07:44:52.602392', '59', 'بازی های فکری', 1, '[{\"added\": {}}]', 16, 1),
(87, '2024-12-04 07:45:26.851142', '60', 'پازل و لگو', 1, '[{\"added\": {}}]', 16, 1),
(88, '2024-12-04 07:46:10.495815', '61', 'اسباب بازی', 1, '[{\"added\": {}}]', 16, 1),
(89, '2024-12-04 07:47:34.076767', '62', 'لوازم تحریر', 1, '[{\"added\": {}}]', 16, 1),
(90, '2024-12-04 07:49:33.725346', '10', 'محصولات خوراکی', 1, '[{\"added\": {}}]', 8, 1),
(91, '2024-12-04 07:50:28.206998', '63', 'شکلات ونتقلات', 1, '[{\"added\": {}}]', 16, 1),
(92, '2024-12-04 07:51:05.262504', '64', 'قهوه و دمنوش', 1, '[{\"added\": {}}]', 16, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'authuser', 'account'),
(2, 'admin', 'logentry'),
(3, 'auth', 'permission'),
(4, 'auth', 'group'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'store', 'blog'),
(8, 'store', 'category'),
(9, 'store', 'color'),
(10, 'store', 'contact'),
(11, 'store', 'homepagecontent'),
(12, 'store', 'order'),
(13, 'store', 'otp'),
(14, 'store', 'product'),
(15, 'store', 'shop'),
(16, 'store', 'subcategory'),
(17, 'store', 'shopimage'),
(18, 'store', 'shopauth'),
(19, 'store', 'productvariation'),
(20, 'store', 'productimage'),
(21, 'store', 'orderitem'),
(22, 'store', 'orderdelivery'),
(23, 'store', 'bankaccount'),
(24, 'store', 'accountinfo');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-12-04 06:11:54.493529'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-12-04 06:11:54.541941'),
(3, 'auth', '0001_initial', '2024-12-04 06:11:54.673943'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-12-04 06:11:54.696856'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-12-04 06:11:54.714891'),
(6, 'auth', '0004_alter_user_username_opts', '2024-12-04 06:11:54.728608'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-12-04 06:11:54.744618'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-12-04 06:11:54.748373'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-12-04 06:11:54.761325'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-12-04 06:11:54.774914'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-12-04 06:11:54.786015'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-12-04 06:11:54.810062'),
(13, 'auth', '0011_update_proxy_permissions', '2024-12-04 06:11:54.827795'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-12-04 06:11:54.843454'),
(15, 'authuser', '0001_initial', '2024-12-04 06:11:54.999496'),
(16, 'admin', '0001_initial', '2024-12-04 06:11:55.087841'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-12-04 06:11:55.109008'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-04 06:11:55.129539'),
(19, 'authuser', '0002_account_phone', '2024-12-04 06:11:55.158965'),
(20, 'sessions', '0001_initial', '2024-12-04 06:11:55.192872'),
(21, 'store', '0001_initial', '2024-12-04 06:11:56.245809'),
(22, 'store', '0002_alter_category_title_alter_subcategory_title', '2024-12-04 06:25:51.381001'),
(23, 'store', '0003_alter_shopimage_banner_image1_and_more', '2024-12-04 08:42:00.844561');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('nu00hv1ne4wlotru574z9b8dz27cvav8', '.eJxVjDsOwjAQRO_iGlle_1hT0nMGy581DiBbipMKcXcSKQU0U8x7M2_mw7pUvw6a_ZTZhQE7_XYxpCe1HeRHaPfOU2_LPEW-K_ygg996ptf1cP8Oahh1W9sYEaQOSCi1QWGNKVZKVaxyWqHOdHYCXUpqSxEzuWCBAEiCKUYJ9vkCsYg2jw:1tIigr:KCAaxq4glyI69tIBItVFusHLtuFpH6xE07O_FVfcO1E', '2024-12-18 06:16:49.945229');

-- --------------------------------------------------------

--
-- Table structure for table `store_accountinfo`
--

CREATE TABLE `store_accountinfo` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `firstname` varchar(300) NOT NULL,
  `lastname` varchar(300) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_bankaccount`
--

CREATE TABLE `store_bankaccount` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(200) NOT NULL,
  `bankName` varchar(200) NOT NULL,
  `cartNumber` varchar(200) NOT NULL,
  `accountNumber` varchar(200) NOT NULL,
  `shop_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_blog`
--

CREATE TABLE `store_blog` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `slug` varchar(50) NOT NULL,
  `content` longtext DEFAULT NULL,
  `meta_description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `seo_keywords` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_category`
--

CREATE TABLE `store_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `slug` varchar(100) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `meta_description` longtext DEFAULT NULL,
  `seo_keywords` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `store_category`
--

INSERT INTO `store_category` (`id`, `name`, `image`, `slug`, `title`, `content`, `meta_description`, `seo_keywords`) VALUES
(1, 'مد و پوشاک زنان', 'images/Photoroom-20241011_145513_ahmqrcf.png', 'women-fashion', 'مد و پوشاک زنان', '', '', NULL),
(2, 'مد و پوشاک مردان', 'images/jacket_KZcDV7w.png', 'men-fashion', 'مد و پوشاک مردان', '', '', NULL),
(3, 'پوشاک کودکان', 'images/overall_ayD8z33.png', 'kids-fashion', 'پوشاک کودکان', '', '', NULL),
(4, 'وسایل حیوانات خانگی', 'images/pet_awMAgZG.png', 'petshop', 'وسایل حیوانات خانگی', '', '', NULL),
(5, 'آرایشی بهداشتی', 'images/beauty_tHofRIE.png', 'beauty', 'آرایشی بهداشتی', '', '', NULL),
(6, 'ورزشی و سفر', 'images/sport_czT2VFJ.png', 'sport-and-travel', 'ورزشی و سفر', '', '', NULL),
(7, 'خانه و آشپزخانه', 'images/homekitchen_VKC3JeQ.png', 'home-and-kitchen', 'خانه و آشپزخانه', '', '', NULL),
(8, 'هنر و صنایع دستی', 'images/artifacts_nPiUyPD.png', 'art-and-artifacts', 'هنر و صنایع دستی', '', '', NULL),
(9, 'بازی و سرگرمی', 'images/toys_40BQrfu.png', 'game-and-entertainment', 'بازی و سرگرمی', '', '', NULL),
(10, 'محصولات خوراکی', 'images/afzudani_GFx7Egz.png', 'edible', 'محصولات خوراکی', '', '', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `store_color`
--

CREATE TABLE `store_color` (
  `id` bigint(20) NOT NULL,
  `color` varchar(400) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `store_color`
--

INSERT INTO `store_color` (`id`, `color`) VALUES
(1, 'مشکی'),
(2, 'سفید'),
(3, 'سورمه ای'),
(4, 'سبز'),
(5, 'یشمی'),
(6, 'بنفش'),
(7, 'آبی'),
(8, 'نارنجی'),
(9, 'نقره ای'),
(10, 'کرم'),
(11, 'قهوه ای'),
(12, 'قرمز'),
(13, 'صورتی'),
(14, 'طلایی'),
(15, 'طوسی'),
(16, 'زرد'),
(17, 'زرشکی');

-- --------------------------------------------------------

--
-- Table structure for table `store_contact`
--

CREATE TABLE `store_contact` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(200) NOT NULL,
  `title` varchar(400) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `message` varchar(3000) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_homepagecontent`
--

CREATE TABLE `store_homepagecontent` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `title` varchar(255) NOT NULL,
  `main_text` longtext DEFAULT NULL,
  `meta_description` longtext DEFAULT NULL,
  `seo_keywords` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_order`
--

CREATE TABLE `store_order` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_paid` tinyint(1) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `total_discount` decimal(10,2) NOT NULL,
  `delivery_address_unit_number` varchar(200) DEFAULT NULL,
  `delivery_address_street_name` varchar(200) DEFAULT NULL,
  `delivery_address_suburb` varchar(200) DEFAULT NULL,
  `delivery_address_city` varchar(200) DEFAULT NULL,
  `delivery_address_state` varchar(200) DEFAULT NULL,
  `delivery_address_country` varchar(200) DEFAULT NULL,
  `delivery_address_postcode` varchar(200) DEFAULT NULL,
  `mobile_number` varchar(200) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `payment_authority` varchar(50) DEFAULT NULL,
  `payment_status` tinyint(1) NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `shop_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_orderdelivery`
--

CREATE TABLE `store_orderdelivery` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `status` varchar(200) NOT NULL,
  `tracking_number` varchar(250) DEFAULT NULL,
  `order_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_orderitem`
--

CREATE TABLE `store_orderitem` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `total_price` double NOT NULL,
  `variation_price` double NOT NULL,
  `discount` double NOT NULL,
  `quantity` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `variation_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_otp`
--

CREATE TABLE `store_otp` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `otp_code` varchar(6) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_product`
--

CREATE TABLE `store_product` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `name` varchar(200) NOT NULL,
  `productCode` varchar(500) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `material` varchar(200) DEFAULT NULL,
  `madeIn` varchar(200) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `isactive` tinyint(1) NOT NULL,
  `instagram_post_id` varchar(250) DEFAULT NULL,
  `discount` decimal(5,2) NOT NULL,
  `is_ready` tinyint(1) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `subcategory_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_productimage`
--

CREATE TABLE `store_productimage` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_productvariation`
--

CREATE TABLE `store_productvariation` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `size` varchar(400) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `color_id` bigint(20) DEFAULT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_shop`
--

CREATE TABLE `store_shop` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `store_name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `instagramId` varchar(400) NOT NULL,
  `email` varchar(254) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `address` varchar(400) NOT NULL,
  `delivery_cost` int(11) NOT NULL,
  `delivery_policy` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `account_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_shopauth`
--

CREATE TABLE `store_shopauth` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `instagram_user_id` varchar(255) NOT NULL,
  `access_token` longtext NOT NULL,
  `token_expiry` datetime(6) NOT NULL,
  `last_authenticated` datetime(6) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `profile_picture_url` varchar(200) DEFAULT NULL,
  `shop_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_shopimage`
--

CREATE TABLE `store_shopimage` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `banner_image1` varchar(100) DEFAULT NULL,
  `banner_image2` varchar(100) DEFAULT NULL,
  `banner_image3` varchar(100) DEFAULT NULL,
  `shop_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_subcategory`
--

CREATE TABLE `store_subcategory` (
  `id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `subname` varchar(200) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `slug` varchar(100) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `meta_description` longtext DEFAULT NULL,
  `seo_keywords` varchar(500) DEFAULT NULL,
  `categoryname_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `store_subcategory`
--

INSERT INTO `store_subcategory` (`id`, `is_deleted`, `subname`, `image`, `slug`, `title`, `content`, `meta_description`, `seo_keywords`, `categoryname_id`) VALUES
(1, 0, 'کت زنانه', 'images/coat1png_6m4jg8j.webp', 'women-coat', 'کت زنانه', '', '', NULL, 1),
(2, 0, 'تاپ و کراپ', 'images/top1png_RXzWDQx.webp', 'women-top', 'تاپ و کراپ', '', '', NULL, 1),
(3, 0, 'تیشرت زنانه', 'images/tshirt1png_DeAHUev.webp', 'women-tshirt', 'تیشرت زنانه', '', '', NULL, 1),
(4, 0, 'شلوار زنانه', 'images/pants1png.webp', 'women-pants', 'شلوار زنانه', '', '', NULL, 1),
(5, 0, 'پبراهن زنانه', 'images/dress1_TbJa3O0.webp', 'dress', 'پبراهن زنانه', '', '', NULL, 1),
(6, 0, 'شلوارک زنانه', 'images/short1png_OPqPHyx.webp', 'women-shortpants', 'شلوارک زنانه', '', '', NULL, 1),
(7, 0, 'دامن', 'images/skirt1png_lag4RKM.webp', 'skirt', 'دامن', '', '', NULL, 1),
(8, 0, 'سرهمی', 'images/overall1png_7s0r94g.webp', 'overall', 'سرهمی', '', '', NULL, 1),
(9, 0, 'شومیز', 'images/shirt1_lJE3OZN.webp', 'women-shirt', 'شومیز', '', '', NULL, 1),
(10, 0, 'ست زنانه', 'images/suit1_cMQod7t.webp', 'women-set', 'ست زنانه', '', '', NULL, 1),
(11, 0, 'کیف زنانه', 'images/bag2_H6zVIVj.webp', 'women-bag', 'کیف زنانه', '', '', NULL, 1),
(12, 0, 'کفش و صندل', 'images/Photoroom-20241020_111107_fQM9u9K.webp', 'women-shoes', 'کفش و صندل', '', '', NULL, 1),
(13, 0, 'مانتو', 'images/manto1png_EkWJqbC.webp', 'manto', 'مانتو', '', '', NULL, 1),
(14, 0, 'شال و روسری', 'images/scarf1_Cb92HWg.webp', 'scarf', 'شال و روسری', '', '', NULL, 1),
(15, 0, 'کلاه زنانه', 'images/hat1png_knwXVHR.webp', 'women-hat', 'کلاه زنانه', '', '', NULL, 1),
(16, 0, 'کت مردانه', 'images/jacketmen_3cLuUYF.webp', 'men-coat', 'کت مردانه', '', '', NULL, 2),
(17, 0, 'پیراهن مردانه', 'images/shirtmen_TPu7t5J.webp', 'men-shirt', 'پیراهن مردانه', '', '', NULL, 2),
(18, 0, 'تیشرت مردانه', 'images/tshirtmen_6Sd87ZY.webp', 'men-tshirt', 'تیشرت مردانه', '', '', NULL, 2),
(19, 0, 'شلوار مردانه', 'images/pantsmen_2ltzHOr.webp', 'men-pants', 'شلوار مردانه', '', '', NULL, 2),
(20, 0, 'شلوارک مردانه', 'images/shortmen_R8MAldh.webp', 'men-short', 'شلوارک مردانه', '', '', NULL, 2),
(21, 0, 'ست مردانه', 'images/suitmen_Et593om.webp', 'men-set', 'ست مردانه', '', '', NULL, 2),
(22, 0, 'کفش مردانه', 'images/shoesmen_jEUwqAy.webp', 'men-shoes', 'کفش مردانه', '', '', NULL, 2),
(23, 0, 'کیف مردانه', 'images/bagMen_F8BStKH.webp', 'men-bag', 'کیف مردانه', '', '', NULL, 2),
(24, 0, 'کلاه مردانه', '', 'men-hat', 'کلاه مردانه', '', '', NULL, 2),
(25, 0, 'کت بچگانه', 'images/jacketk_KXlHfBD.webp', 'kids-coat', 'کت بچگانه', '', '', NULL, 3),
(26, 0, 'تیشرت بچگانه', 'images/tshirtk_SfVSg8s.webp', 'kids-tshirt', 'تیشرت بچگانه', '', '', NULL, 3),
(27, 0, 'سرهمی بچگانه', 'images/overallk_2XBnYoa.webp', 'kids-overall', 'سرهمی بچگانه', '', '', NULL, 3),
(28, 0, 'سرهمی بچگانه', 'images/overallk_F6jD3j2.webp', 'kids-overall', 'سرهمی بچگانه', '', '', NULL, 3),
(29, 0, 'پیراهن دخترانه', 'images/Untitled_TsvW52l.webp', 'kids-dress', 'پیراهن دخترانه', '', '', NULL, 3),
(30, 0, 'پیراهن پسرانه', 'images/Photoroom-20241020_105628_TAowRL7.webp', 'kids-shirt', 'پیراهن پسرانه', '', '', NULL, 3),
(31, 0, 'ست پچگانه', 'images/Photoroom-20241020_105723_S5AJE4Q.webp', 'kids-set', 'ست پچگانه', '', '', NULL, 3),
(32, 0, 'دورس و هودی', 'images/Photoroom-20241020_105755_svFJxaG.webp', 'women-hudie', 'دورس و هودی', '', '', NULL, 1),
(33, 0, 'بافت و هودی', 'images/Photoroom-20241020_105755_YR25AOu.webp', 'men-hudie', 'بافت و هودی', '', '', NULL, 2),
(34, 0, 'دامن بچگانه', 'images/skirtk_RvrUyg1.webp', 'kids-skirt', 'دامن بچگانه', '', '', NULL, 3),
(35, 0, 'شلوار بچگانه', 'images/pantsk_oI7eFAy.webp', 'kids-pants', 'شلوار بچگانه', '', '', NULL, 3),
(36, 0, 'شلوارک بچگانه', 'images/shortk_0HwhZiT.webp', 'kids-short', 'شلوارک بچگانه', '', '', NULL, 3),
(37, 0, 'کفش بچگانه', 'images/shoesk_IBgHvmF.webp', 'kids-shoes', 'کفش بچگانه', '', '', NULL, 3),
(38, 0, 'کلاه بچگانه', 'images/hatk_HU9Aj8H.webp', 'kids-hat', 'کلاه بچگانه', '', '', NULL, 3),
(39, 0, 'محصولات خوراکی حیوانات', 'images/ghaza_bbUFP9i.webp', 'pet-food', 'محصولات خوراکی حیوانات', '', '', NULL, 4),
(40, 0, 'لباس و قلاده', 'images/ghalade_6BerOkI.webp', 'pet-clothes', 'لباس و قلاده', '', '', NULL, 4),
(41, 0, 'باکس و سایر ملزومات', 'images/bos_QZ1wNuV.webp', 'pet-box', 'باکس پت', '', '', NULL, 4),
(42, 0, 'وسایل بازی', 'images/pettoys_Pck7tvn.webp', 'pet-toys', 'وسایل بازی حیوانات', '', '', NULL, 4),
(43, 0, 'لوازم آرایشی', 'images/arayesh_KV7Ld7q.webp', 'cosmetics', 'لوازم آرایشی', '', '', NULL, 5),
(44, 0, 'مراقبت از مو', 'images/moo_bsa8GpQ.webp', 'hair-care', 'مراقبت از مو', '', '', NULL, 5),
(45, 0, 'مراقبت از پوست', 'images/pust_QSpizfx.webp', 'skin-care', 'مراقبت از پوست', '', '', NULL, 5),
(46, 0, 'عطر و ادکن', 'images/atr_f0DHeeL.webp', 'perfume', 'عطر و ادکن', '', '', NULL, 5),
(47, 0, 'لوازم برقی شخصی', 'images/seshvar_u5ymKvE.webp', 'personal-electronic-devices', 'لوازم برقی شخصی', '', '', NULL, 5),
(48, 0, 'بهداشتی', 'images/behdashti_3Nr2LBz.webp', 'personal-care', 'بهداشتی', '', '', NULL, 5),
(49, 0, 'ظروف و لوازم دکوری سنتی', 'images/zurufesonati_q32KDwD.webp', 'traditional-dish', 'ظروف و لوازم دکوری سنتی', '', '', NULL, 8),
(50, 0, 'اکسسوری و زیورآلات', 'images/accessori_NF3OMQv.webp', 'accessories', 'اکسسوری و زیورآلات', '', '', NULL, 8),
(51, 0, 'لوازم پذیرایی', 'images/zarf_6khisDS.webp', 'dining-dish', 'لوازم پذیرایی', '', '', NULL, 7),
(52, 0, 'لوازم پخت و پز', '', 'cooking-dish', 'لوازم پخت و پز', '', '', NULL, 7),
(53, 0, 'لوازم اتاق خواب', 'images/khab_eoMIilQ.webp', 'bedroom', 'لوازم اتاق خواب', '', '', NULL, 7),
(54, 0, 'دکوراسیون خانگی', '', 'decor', 'دکوراسیون خانگی', '', '', NULL, 7),
(55, 0, 'کمپینگ و کوهنوردی', 'images/camp_9gSux2w.webp', 'camping', 'کمپینگ و کوهنوردی', '', '', NULL, 6),
(56, 0, 'لوازم ورزشی', 'images/varzesh_1MoQs86.webp', 'sport-equipment', 'لوازم ورزشی', '', '', NULL, 6),
(57, 0, 'ساک و چمدان', 'images/sak_J19bjcw.webp', 'luggage', 'ساک و چمدان', '', '', NULL, 6),
(58, 0, 'لباس ورزشی', '', 'sport-clothes', 'لباس ورزشی', '', '', NULL, 6),
(59, 0, 'بازی های فکری', 'images/f514030b-f9ae-4913-a1b2-7a5287c89f41_dgqvNhO.webp', 'boardgame', 'بازی های فکری', '', '', NULL, 9),
(60, 0, 'پازل و لگو', 'images/pazel_kqPlBfU.webp', 'lego', 'پازل و لگو', '', '', NULL, 9),
(61, 0, 'اسباب بازی', 'images/toys_2_p8fzLF4.webp', 'toys', 'اسباب بازی', '', '', NULL, 9),
(62, 0, 'لوازم تحریر', 'images/tahrir_B2kLbDX.webp', 'stationery', 'لوازم تحریر', '', '', NULL, 9),
(63, 0, 'شکلات ونتقلات', 'images/chocolate_fLVYabp.webp', 'chocolate', 'شکلات ونتقلات', '', '', NULL, 10),
(64, 0, 'قهوه و دمنوش', 'images/ghahve_WYUF9V7.webp', 'coffee', 'قهوه و دمنوش', '', '', NULL, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authuser_account`
--
ALTER TABLE `authuser_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `authuser_account_groups`
--
ALTER TABLE `authuser_account_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `authuser_account_groups_account_id_group_id_e501e71e_uniq` (`account_id`,`group_id`),
  ADD KEY `authuser_account_groups_account_id_2d63e4a0` (`account_id`),
  ADD KEY `authuser_account_groups_group_id_09658de5` (`group_id`);

--
-- Indexes for table `authuser_account_user_permissions`
--
ALTER TABLE `authuser_account_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `authuser_account_user_pe_account_id_permission_id_2a2db1db_uniq` (`account_id`,`permission_id`),
  ADD KEY `authuser_account_user_permissions_account_id_ab152fa8` (`account_id`),
  ADD KEY `authuser_account_user_permissions_permission_id_32e65fa5` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  ADD KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  ADD KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `store_accountinfo`
--
ALTER TABLE `store_accountinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `store_bankaccount`
--
ALTER TABLE `store_bankaccount`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_bankaccount_shop_id_1cc8aa2e` (`shop_id`);

--
-- Indexes for table `store_blog`
--
ALTER TABLE `store_blog`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `store_category`
--
ALTER TABLE `store_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_category_slug_2d349264` (`slug`);

--
-- Indexes for table `store_color`
--
ALTER TABLE `store_color`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `store_contact`
--
ALTER TABLE `store_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `store_homepagecontent`
--
ALTER TABLE `store_homepagecontent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `store_order`
--
ALTER TABLE `store_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_order_account_id_f37a6735` (`account_id`),
  ADD KEY `store_order_shop_id_846fb8ee` (`shop_id`);

--
-- Indexes for table `store_orderdelivery`
--
ALTER TABLE `store_orderdelivery`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_id` (`order_id`);

--
-- Indexes for table `store_orderitem`
--
ALTER TABLE `store_orderitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_orderitem_order_id_acf8722d` (`order_id`),
  ADD KEY `store_orderitem_variation_id_10b2cc08` (`variation_id`);

--
-- Indexes for table `store_otp`
--
ALTER TABLE `store_otp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_otp_mobile_number_4554ba64` (`mobile_number`);

--
-- Indexes for table `store_product`
--
ALTER TABLE `store_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_product_category_id_574bae65` (`category_id`),
  ADD KEY `store_product_shop_id_9324fcd9` (`shop_id`),
  ADD KEY `store_product_subcategory_id_4a875c72` (`subcategory_id`);

--
-- Indexes for table `store_productimage`
--
ALTER TABLE `store_productimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_productimage_product_id_e50e4046` (`product_id`);

--
-- Indexes for table `store_productvariation`
--
ALTER TABLE `store_productvariation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_productvariation_color_id_9dc4b28f` (`color_id`),
  ADD KEY `store_productvariation_product_id_279b7a52` (`product_id`);

--
-- Indexes for table `store_shop`
--
ALTER TABLE `store_shop`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `store_name` (`store_name`),
  ADD KEY `store_shop_account_id_1bf5aae2` (`account_id`);

--
-- Indexes for table `store_shopauth`
--
ALTER TABLE `store_shopauth`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `instagram_user_id` (`instagram_user_id`),
  ADD UNIQUE KEY `shop_id` (`shop_id`);

--
-- Indexes for table `store_shopimage`
--
ALTER TABLE `store_shopimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_shopimage_shop_id_62616569` (`shop_id`);

--
-- Indexes for table `store_subcategory`
--
ALTER TABLE `store_subcategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `store_subcategory_slug_c7e435fe` (`slug`),
  ADD KEY `store_subcategory_categoryname_id_be36096a` (`categoryname_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authuser_account`
--
ALTER TABLE `authuser_account`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `authuser_account_groups`
--
ALTER TABLE `authuser_account_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `authuser_account_user_permissions`
--
ALTER TABLE `authuser_account_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `store_accountinfo`
--
ALTER TABLE `store_accountinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_bankaccount`
--
ALTER TABLE `store_bankaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_blog`
--
ALTER TABLE `store_blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_category`
--
ALTER TABLE `store_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `store_color`
--
ALTER TABLE `store_color`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `store_contact`
--
ALTER TABLE `store_contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_homepagecontent`
--
ALTER TABLE `store_homepagecontent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_order`
--
ALTER TABLE `store_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_orderdelivery`
--
ALTER TABLE `store_orderdelivery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_orderitem`
--
ALTER TABLE `store_orderitem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_otp`
--
ALTER TABLE `store_otp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_product`
--
ALTER TABLE `store_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_productimage`
--
ALTER TABLE `store_productimage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_productvariation`
--
ALTER TABLE `store_productvariation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_shop`
--
ALTER TABLE `store_shop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_shopauth`
--
ALTER TABLE `store_shopauth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_shopimage`
--
ALTER TABLE `store_shopimage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_subcategory`
--
ALTER TABLE `store_subcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
