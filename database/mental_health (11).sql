-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2022 at 11:44 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mental_health`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_tbl`
--

CREATE TABLE `book_tbl` (
  `book_id` int(5) NOT NULL,
  `book_time` varchar(50) NOT NULL DEFAULT current_timestamp(),
  `user_id` int(5) NOT NULL,
  `mh_professional_id` int(5) NOT NULL,
  `book_question` varchar(100) NOT NULL,
  `user_mobile` varchar(12) NOT NULL,
  `charges` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book_tbl`
--

INSERT INTO `book_tbl` (`book_id`, `book_time`, `user_id`, `mh_professional_id`, `book_question`, `user_mobile`, `charges`) VALUES
(706, '2022-03-07 17:25:15', 102, 301, 'I am in depression and need  someone\'s attention.', '8520520121', '750'),
(712, '2022-03-11 19:10:36', 114, 301, 'I want to recover from my depression state.', '8741257412', '750'),
(713, '2022-03-11 19:10:36', 112, 301, 'I need a support.', '8741254162', '750'),
(715, '2022-03-11 19:10:36', 117, 301, 'I am in depression , i am daily experiencing anxiety , I need help.', '8741274159', '750');

-- --------------------------------------------------------

--
-- Stand-in structure for view `charges wise booking report`
-- (See below for the actual view)
--
CREATE TABLE `charges wise booking report` (
`book_id` int(5)
,`book_time` varchar(50)
,`name` varchar(25)
,`professional_name` varchar(25)
,`charges` varchar(5)
);

-- --------------------------------------------------------

--
-- Table structure for table `communityanswer_tbl`
--

CREATE TABLE `communityanswer_tbl` (
  `answer_id` int(5) NOT NULL,
  `communityque_id` int(5) NOT NULL,
  `community_ans` varchar(200) NOT NULL,
  `apost_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `community_group` varchar(25) NOT NULL,
  `user_id` int(5) NOT NULL,
  `mh_professional_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `communityanswer_tbl`
--

INSERT INTO `communityanswer_tbl` (`answer_id`, `communityque_id`, `community_ans`, `apost_date`, `community_group`, `user_id`, `mh_professional_id`) VALUES
(601, 501, 'Yes, Definately', '2022-03-05 12:15:47', 'Living With Depression', 102, 301),
(602, 502, '[Activity Time!] VENT IT OUT\r\n\r\nWe all have good days and bad days. And while we may love to share our pleasant experiences with our loved ones, opening up about the bad ones may not come as easy. ', '2022-03-14 12:32:12', 'Addiction Support', 103, 304),
(603, 503, 'Self-talk is that voice inside our heads that constantly tries to make sense of the world around us, and it can greatly influence the way we communicate with our own selves.\r\n', '2022-03-14 12:32:12', 'Addiction Support', 104, 305),
(604, 504, 'Starting and staying on the road to recovery can be challenging. It can be difficult to stay motivated. But knowing you\'re not alone helps. And so do words from people who have taken the same road. ', '2022-03-14 12:33:33', 'Addiction Support', 105, 304),
(605, 505, 'Yes, Do You know ? What is the first step towards addiction recovery?\r\n\r\nBelieve it or not-it\'s a step you have already taken! Acknowledging that you may have an addiction is the first step.', '2022-03-14 12:32:43', 'Addiction Support', 106, 305),
(606, 506, 'A lot of people tend to ignore their needs or find it difficult to establish boundaries because they are afraid how the other person might be affected. However, you should always know that your needs,', '2022-03-14 12:32:43', 'Living With Depression', 107, 306),
(607, 507, '“Unwell” by Matchbox Twenty. ...\r\n“Better Place” by Rachel Platten. ...\r\n“Screen” by Twenty One Pilots. ...\r\n“Last Hope” by Paramore. ...\r\n“Heavy” by Linkin Park. ...\r\n“1-800-273-8255” by Logic featur', '2022-03-14 12:33:33', 'Living With Depression', 108, 307),
(608, 508, 'Feelings of chronic emptiness are an important and challenging symptom of BPD which require clinical intervention. Strengthening identity, sense of purpose and vocational and relationship functioning.', '2022-03-14 12:34:34', 'Addiction Support', 109, 308),
(609, 509, 'It\'s normal to feel lost or stuck in life, especially in the midst of massive change or upheaval. This happens because as we grow and learn more about ourselves and the world around us.', '2022-03-14 12:34:34', 'Living With Depression', 110, 309),
(610, 510, 'Remember - A mistake is only a mistake, if you don\'t learn from it. And, self-forgiveness is the first step towards becoming the best version of yourself.\r\n\r\nLet\'s learn how to let ourselves off.', '2022-03-14 12:34:34', 'Living With Depression', 103, 310);

-- --------------------------------------------------------

--
-- Table structure for table `community_tbl`
--

CREATE TABLE `community_tbl` (
  `communityque_id` int(5) NOT NULL,
  `community_msg` varchar(150) NOT NULL,
  `Type` varchar(10) NOT NULL,
  `postdate_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `community_group` varchar(25) NOT NULL,
  `user_Name` varchar(35) NOT NULL,
  `Professional_Name` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `community_tbl`
--

INSERT INTO `community_tbl` (`communityque_id`, `community_msg`, `Type`, `postdate_time`, `community_group`, `user_Name`, `Professional_Name`) VALUES
(501, 'Can I become normal once again ?', 'Ques', '2022-03-05 12:13:21', 'Living With Depression', 'Daisy Solomon', ''),
(502, 'Hello, I have recently made an id on the website to help me with depression and addiction. I \'m addicted  to painkillers.', 'Ques', '2022-03-26 11:05:45', 'Living With Depression', 'Shivangi Shah', ''),
(503, 'I need a support.', 'Ques', '2022-03-26 11:13:26', 'Addiction Support', 'Namita Shah', ''),
(504, 'Do you have any suggestions to kind of control procastination over anxiety.', 'Ques', '2022-03-26 11:22:13', 'Addiction Support', 'John Makhija', ''),
(505, 'Hello, Anyone here ?', 'Ques', '2022-03-26 11:24:58', 'Addiction Support', 'Namita Shah', ''),
(506, 'I need a friend but I am not able to make a one . ', 'Ques', '2022-03-26 11:24:58', 'Living With depression', 'Shivangi Shah', ''),
(507, 'Could you recommend me songs for falling asleep in night when i am not able to ?', 'Ques', '2022-03-26 11:24:58', 'Living with depression', 'Jessica Mandela', ''),
(508, 'feeling like an empty pit. I just wanna eat , it\'s already an addiction.', 'Ques', '2022-03-26 11:24:58', 'Addiction Support', 'Nishant Das', ''),
(509, 'I am feeling really low. Missing friends, wish i could get a tight hug , not feeling good at all mentally, don\'t feel like doing anything.', 'Ques', '2022-03-26 11:24:58', 'Living with Depression', 'Tarun Grover', ''),
(510, 'It\'s a battle taming negative thoughts.', 'Ques', '2022-03-26 11:24:58', 'Living with depression', 'Naman Sodhani', ''),
(511, 'Yes, Definately', 'Ans', '2022-04-07 08:42:52', 'Living With Depression', '', ' Expert->Bhoomika'),
(512, '[Activity Time!] VENT IT OUT\r\n\r\nWe all have good days and bad days. And while we may love to share our pleasant experiences with our loved ones.', 'Ans', '2022-04-07 08:42:52', 'Addiction Support', '', 'Expert->Bhoomika'),
(513, 'Self-talk is that voice inside our heads that constantly tries to make sense of the world around us.', 'Ans', '2022-04-07 08:42:52', 'Addiction Support', '', 'Expert->Shreya'),
(514, 'Starting and staying on the road to recovery can be challenging. It can be difficult to stay motivated. But knowing you\'re not alone helps. ', 'Ans', '2022-04-07 08:42:52', 'Addiction Support', '', 'Expert->Srishti'),
(515, 'Yes, Do You know ? What is the first step towards addiction recovery?\r\n\r\nBelieve it or not-it\'s a step you have already taken!  ', 'Ans', '2022-04-07 08:42:52', 'Addiction Support', '', 'Expert->Shuchi'),
(516, 'A lot of people tend to ignore their needs or find it difficult to establish boundaries because they are afraid how the other person might be affected', 'Ans', '2022-04-07 08:42:52', 'Living With depression', '', 'Expert->Tanya'),
(517, '“Unwell” by Matchbox Twenty. ...\r\n“Better Place” by Rachel Platten. ...\r\n“Screen” by Twenty One Pilots. ...\r\n“Last Hope” by Paramore. ...\r\n', 'Ans', '2022-04-07 08:42:52', 'Living with depression', '', 'Expert->Mrunmayi'),
(518, 'Feelings of chronic emptiness are an important and challenging symptom of BPD which require clinical intervention. ', 'Ans', '2022-04-07 08:42:52', 'Addiction Support', '', 'Expert->Mrunmayi'),
(519, 'It\'s normal to feel lost or stuck in life, especially in the midst of massive change or upheaval.', 'Ans', '2022-04-07 08:42:52', 'Living with Depression', '', 'Expert->Shuchi'),
(520, 'Remember - A mistake is only a mistake, if you don\'t learn from it. And, self-forgiveness is the first step towards becoming the best version of yours', 'Ans`', '2022-04-07 08:42:52', 'Living with depression', '', 'Expert->Shuchi');

-- --------------------------------------------------------

--
-- Stand-in structure for view `communtiy group wise community questions report`
-- (See below for the actual view)
--
CREATE TABLE `communtiy group wise community questions report` (
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `comunty group wise communty answer report`
-- (See below for the actual view)
--
CREATE TABLE `comunty group wise communty answer report` (
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `content type wise content report`
-- (See below for the actual view)
--
CREATE TABLE `content type wise content report` (
`content_id` int(5)
,`c_name` varchar(50)
,`status` varchar(15)
,`con_description` varchar(150)
,`image` varchar(100)
,`audio` varchar(100)
,`video` varchar(100)
,`con_name` varchar(15)
);

-- --------------------------------------------------------

--
-- Table structure for table `content_tbl`
--

CREATE TABLE `content_tbl` (
  `content_id` int(5) NOT NULL,
  `con_typeid` int(5) NOT NULL,
  `c_name` varchar(50) NOT NULL,
  `status` varchar(15) NOT NULL,
  `con_description` varchar(150) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `audio` varchar(100) DEFAULT NULL,
  `video` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `content_tbl`
--

INSERT INTO `content_tbl` (`content_id`, `con_typeid`, `c_name`, `status`, `con_description`, `image`, `audio`, `video`) VALUES
(4101, 3101, 'Anxiety', 'Available', 'Intense, excessive and persistent worry and fear about everyday situations. Fast heart rate, rapid breathing, sweating and feeling tired may occur.', NULL, 'anxiety.mp3', NULL),
(4102, 3102, 'Addiction', 'Available', 'An addiction is an urge to do something that is hard to control or stop.', 'Addiction1.jpg', NULL, NULL),
(4103, 3103, 'You are important.', 'Available', '', NULL, 'You are important.mp4', NULL),
(4104, 3107, 'Depression', 'Available', 'Depression is a kind of constricted consciousness.', 'depression1.jpg', NULL, NULL),
(4105, 3104, 'Life is Tough!', 'Available', '', NULL, NULL, 'Lifeistough.mp4'),
(4106, 3106, 'MoodDisorder', 'Available', 'Time wil pass:these moods will pass:and I will eventually be myself again', 'Moodsiorder2.jpg', '', NULL),
(4107, 3107, 'SleepDisorder', 'Available', ' A good laugh and a long sleep are the best cures in the doctor\'s book.', 'sleepdisorder2.jpg', NULL, NULL),
(4108, 3105, 'Stress', 'Available', 'Sress is the inability to decide what\'s important.', NULL, 'stress.mp3', NULL),
(4109, 3110, 'Grief', 'Available', 'It’s normal to feel sadness and grief after you experience loss. But that doesn’t make it easy.', 'grief1.jpg', NULL, NULL),
(4110, 3102, 'Addiction ', 'Available', '', 'Addiction2.jpg', NULL, NULL),
(4111, 3102, 'Important', 'Unavailable', '', 'imp.jpg', NULL, NULL),
(4112, 3102, 'Mood Disorder', 'Available', '', 'MoodDisorder.png', NULL, NULL),
(4113, 3102, 'Anxiety', 'Available', '', 'anxiety.jpg', NULL, NULL),
(4114, 3102, 'Sleep Disturbances', 'Available', '', 'SleepDis.jpg', NULL, NULL),
(4115, 3102, 'Grief', 'Available', '', 'Grief.jpg', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `content_typetbl`
--

CREATE TABLE `content_typetbl` (
  `con_typeid` int(5) NOT NULL,
  `con_name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `content_typetbl`
--

INSERT INTO `content_typetbl` (`con_typeid`, `con_name`) VALUES
(3101, 'Audio'),
(3102, 'Image'),
(3103, 'Video'),
(3104, 'Video'),
(3105, 'Audio'),
(3106, 'Image'),
(3107, 'Image'),
(3108, 'Image'),
(3109, 'Image'),
(3110, 'Image'),
(3111, 'Select a conten');

-- --------------------------------------------------------

--
-- Stand-in structure for view `event wise event booking report`
-- (See below for the actual view)
--
CREATE TABLE `event wise event booking report` (
`event_bookid` int(5)
,`event_name` varchar(50)
,`name` varchar(25)
,`user_email` varchar(25)
,`user_mobile` varchar(15)
);

-- --------------------------------------------------------

--
-- Table structure for table `event_booking`
--

CREATE TABLE `event_booking` (
  `event_bookid` int(5) NOT NULL,
  `user_email` varchar(25) NOT NULL,
  `user_id` varchar(15) NOT NULL,
  `user_mobile` varchar(15) NOT NULL,
  `event_id` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event_booking`
--

INSERT INTO `event_booking` (`event_bookid`, `user_email`, `user_id`, `user_mobile`, `event_id`) VALUES
(401, 'daisy@gmail.com', '102', '9427194472', '201'),
(402, 'namita@gmail.com', '103', '8975412459', '202'),
(403, 'jessica@gmail.com', '105', '7842514236', '204'),
(404, 'john@gmail.com', '107', '6924153578', '203'),
(405, 'naman@gmail.com', '109', '7412564123', '203'),
(406, 'tanvi@gmail.com', '108', '8741253975', '201'),
(407, 'nishant@gmail.com', '106', '8417259634', '201'),
(408, 'shivangi@gmail.com', '104', '8955674182', '201'),
(409, 'tarun@gmail.com', '110', '8741529674', '202'),
(410, 'niharika@gmail.com', '111', '8741524129', '201'),
(411, 'di@gmail.com', '115', '7412564123', '201'),
(412, 'ra@gmail.com', '114', '8741257419', '201'),
(413, 'mona@gmail.com', '113', '8741256214', '201'),
(414, 'niv@gmail.com', '112', '8741254162', '201'),
(415, 'tara@gmail.com', '116', '6874125741', '201'),
(416, 'tom@gmail.com', '117', '8741274159', '201');

-- --------------------------------------------------------

--
-- Table structure for table `event_tbl`
--

CREATE TABLE `event_tbl` (
  `event_id` int(5) NOT NULL,
  `event_date` varchar(25) NOT NULL,
  `event_description` varchar(350) NOT NULL,
  `event_time` varchar(25) NOT NULL,
  `mh_professional_id` int(5) NOT NULL,
  `event_name` varchar(50) NOT NULL,
  `event_image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event_tbl`
--

INSERT INTO `event_tbl` (`event_id`, `event_date`, `event_description`, `event_time`, `mh_professional_id`, `event_name`, `event_image`) VALUES
(201, '12-2-2023', 'Increase awareness of mental health and its potential incidence and impact in the workplace, challenge existing stereotypes of mental illness, and explore how one might better support their colleagues.', '4:00 PM', 302, 'Mental Health', '1.jpg'),
(202, '12-3-2023', 'Developing strategies for oneself and for others who have experienced workplace bullying and harassment. Opportunities to contribute to the elimination of workplace bullying and harassment will be highlighted. This workshop meets the annual employee training requirements of WorksafeBC.', '5:00 PM ', 303, 'Bullying & Harrasment', '2.jpg'),
(203, '12-4-2023', 'Self care is about taking care of your mind and body, so you feel less stress and more joy. Improve the enjoyment of life and work in your workplace by implementing a self-care plan.', '04:30 PM ', 303, 'Self Care', '3.jpg'),
(204, '12-5-2023', 'When Mental Health leads to work absence for employees, special skills and tools are helpful to keep employees engaged, help them to get healthy, safely return to work, and to meet employer responsibilities for accommodation. The key to success is to empower everyone in your workplace to play their role.', '05:30 PM', 302, 'Return To Work ', '4.jpg'),
(205, '12-6-2023', 'Through the use of structured experiences, discussions and interactions, this dynamic, engaging and interactive session is designed to increase awareness of mental health and its potential incidence and impact in the workplace, challenge existing stereotypes of mental illness. Additionally participants will have an opportunity to consider their cur', '4:00 PM', 303, 'Every Mind Matters at Work!', '1.jpg'),
(206, '12-7-2023', 'This 60 minute virtual workshop will introduce tools to build communication skills related to mental health. The session introduces a framework to identify poor mental health in oneself and others and instructs on how to communicate effectively to ensure better outcomes. Participants will have opportunity to create their own conversation script.', '4:30 PM', 302, 'How to Communicate Effectively to Improve Mental H', '3.jpg'),
(207, '12-7-2022', 'Through the use of structured experiences, group discussions and practical activities, this dynamic, engaging and interactive session invites participants to understand the science of stress and happiness and build skills to thrive at work. Participants will be given the opportunity to identify and evaluate their own strategies, select specific too', '5:30 PM', 303, 'How to be Happy at Work', '1.jpg'),
(208, '12-5-2022', 'This 60 minute virtual workshop introduces tools to build personal resilience to thrive and feel better during times of stress. The session reviews the concept of the mental health continuum and introduces 3 personal strategies to promote improved mental health. Applying one of these strategies, participants will evaluate their own resiliency activ', '5:00 PM', 302, 'Building Resilience in Times of Stress - Wellness ', '4.jpg'),
(209, '12-8-2022', 'This 60 minute virtual workshop will introduce tools to build personal resilience to thrive and feel better during times of stress. The session briefly reviews the concept of the mental health continuum and introduces 3 personal strategies to promote improved mental health. Applying one of these strategies, participants will evaluate their own resi', '4:00 PM', 303, 'Social Support', '2.jpg'),
(210, '12-9-2022', 'Being aware of signs and symptoms and taking pro-active steps for prevention can help to avoid or reduce the impact of burnout. Help protect your employees with our easy to use tools.', '5:30 PM', 303, 'Workplace Burnout', '3.jpg');

-- --------------------------------------------------------

--
-- Stand-in structure for view `experience range wise professional report`
-- (See below for the actual view)
--
CREATE TABLE `experience range wise professional report` (
`mh_professional_id` int(5)
,`type` varchar(10)
,`professional_name` varchar(25)
,`email` varchar(25)
,`contact_no` double
,`gender` varchar(7)
,`active` varchar(4)
,`charges` int(4)
,`Degree` varchar(20)
,`Experience` varchar(10)
,`Language` varchar(30)
);

-- --------------------------------------------------------

--
-- Table structure for table `feedback_tbl`
--

CREATE TABLE `feedback_tbl` (
  `feedback_id` int(5) NOT NULL,
  `feedback_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `user_id` int(5) NOT NULL,
  `q1` varchar(30) NOT NULL,
  `q2` varchar(30) NOT NULL,
  `q3` varchar(30) NOT NULL,
  `q4` varchar(30) NOT NULL,
  `q5` varchar(30) NOT NULL,
  `q6` varchar(30) NOT NULL,
  `q7` varchar(30) NOT NULL,
  `q8` varchar(30) NOT NULL,
  `q9` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback_tbl`
--

INSERT INTO `feedback_tbl` (`feedback_id`, `feedback_date`, `user_id`, `q1`, `q2`, `q3`, `q4`, `q5`, `q6`, `q7`, `q8`, `q9`) VALUES
(801, '2022-03-09 08:10:00', 102, 'Yes', 'Good', '3', 'No not at all', 'LGBTQ  mental health', '', '', 'Soumya Pandya', '3'),
(802, '2022-03-11 08:09:31', 103, 'Somewhat', 'I am feeling good now.', '3', 'No', 'Add more motivational videos.', '', '', '', ''),
(803, '2022-03-11 08:11:07', 106, 'Yes ', 'Quite helpful.', '4', 'No', 'Nothing', '', '', '', ''),
(804, '2022-03-11 08:11:58', 107, 'Somewhat', 'Very Informative', '4', 'Yes ', 'Add more content', 'Bhoomika Gupta', '4', '', ''),
(805, '2022-03-11 08:30:16', 105, 'Yes', 'Satisfactory ', '3', 'No', 'Add more resources.', 'Gautam Krishnan', '4', '', ''),
(806, '2022-03-11 08:31:50', 104, 'Yes', 'Satisfactory ', '4', 'No ', 'Nothing', 'Shreya Madan', '4', '', ''),
(807, '2022-03-11 08:34:32', 109, 'Yes', 'Satisfactory ', '4', 'No', 'Nothing', '', '', '', ''),
(808, '2022-03-11 08:35:16', 110, 'Somewhat', 'Informative ', '3', 'No', 'Add more motivational content.', 'Bhoomika Gupta', '4', '', ''),
(809, '2022-03-11 08:36:33', 108, 'Yes', 'Satisfactory ', '3', 'Yes', 'No', 'Parth kalia', '5', '', ''),
(810, '2022-03-30 18:16:58', 111, 'yes', 'Amazing', '3', 'no', 'OCD disorder', '', '', 'Dr. Soumya Pandya', '4');

-- --------------------------------------------------------

--
-- Stand-in structure for view `gender wise professional report`
-- (See below for the actual view)
--
CREATE TABLE `gender wise professional report` (
`mh_professional_id` int(5)
,`type` varchar(10)
,`professional_name` varchar(25)
,`email` varchar(25)
,`contact_no` double
,`gender` varchar(7)
,`active` varchar(4)
,`charges` int(4)
,`Degree` varchar(20)
,`Experience` varchar(10)
,`Language` varchar(30)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `gender wise user report`
-- (See below for the actual view)
--
CREATE TABLE `gender wise user report` (
`user_id` int(5)
,`is_admin` varchar(4)
,`name` varchar(25)
,`email` varchar(45)
,`joining_date` timestamp
,`contact_no` varchar(11)
,`gender` varchar(6)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `language known wise professional report`
-- (See below for the actual view)
--
CREATE TABLE `language known wise professional report` (
`mh_professional_id` int(5)
,`type` varchar(10)
,`professional_name` varchar(25)
,`email` varchar(25)
,`contact_no` double
,`gender` varchar(7)
,`charges` int(4)
,`Degree` varchar(20)
,`Experience` varchar(10)
,`Language` varchar(30)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `payment mode wise payment report`
-- (See below for the actual view)
--
CREATE TABLE `payment mode wise payment report` (
`payment_id` int(5)
,`book_id` int(5)
,`payment_mode` varchar(15)
,`payment_status` varchar(7)
,`user_id` int(5)
,`payment_amount` int(5)
,`name` varchar(25)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `payment status wise payment report`
-- (See below for the actual view)
--
CREATE TABLE `payment status wise payment report` (
`payment_id` int(5)
,`book_id` int(5)
,`payment_mode` varchar(15)
,`payment_status` varchar(7)
,`payment_amount` int(5)
,`name` varchar(25)
);

-- --------------------------------------------------------

--
-- Table structure for table `payment_tbl`
--

CREATE TABLE `payment_tbl` (
  `payment_id` int(5) NOT NULL,
  `book_id` int(5) NOT NULL,
  `payment_mode` varchar(15) NOT NULL,
  `payment_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `payment_status` varchar(7) NOT NULL,
  `user_id` int(5) NOT NULL,
  `payment_amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment_tbl`
--

INSERT INTO `payment_tbl` (`payment_id`, `book_id`, `payment_mode`, `payment_date`, `payment_status`, `user_id`, `payment_amount`) VALUES
(901, 701, 'Google pay', '2022-03-19 09:26:41', 'pending', 107, 750),
(902, 702, 'Paytm', '2021-02-12 10:32:26', 'paid', 102, 750),
(903, 703, 'Phonepe', '2021-03-10 23:44:15', 'paid', 103, 750),
(904, 704, 'GooglePay', '2021-02-07 23:45:41', 'pending', 104, 1200),
(905, 705, 'Phonepe', '2021-05-06 23:47:29', 'pending', 105, 1200),
(906, 706, 'Paytm', '2021-03-13 04:19:27', 'pending', 106, 750),
(907, 707, 'GooglePay', '2021-01-09 23:52:30', 'paid', 107, 1200),
(908, 708, 'GooglePay', '2021-05-10 23:53:08', 'paid', 108, 1200),
(909, 709, 'Paytm', '2021-09-07 23:53:54', 'pending', 109, 750),
(910, 710, 'Paytm', '2021-02-01 23:54:36', 'pending', 110, 750);

-- --------------------------------------------------------

--
-- Stand-in structure for view `professional type wise booking report`
-- (See below for the actual view)
--
CREATE TABLE `professional type wise booking report` (
`book_id` int(5)
,`book_time` varchar(50)
,`name` varchar(25)
,`book_question` varchar(100)
,`charges` varchar(5)
,`user_mobile` varchar(12)
,`type` varchar(10)
,`professional_name` varchar(25)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `professional type wise professional report`
-- (See below for the actual view)
--
CREATE TABLE `professional type wise professional report` (
`mh_professional_id` int(5)
,`type` varchar(10)
,`professional_name` varchar(25)
,`email` varchar(25)
,`contact_no` double
,`gender` varchar(7)
,`active` varchar(4)
,`charges` int(4)
,`Degree` varchar(20)
,`Experience` varchar(10)
,`Language` varchar(30)
);

-- --------------------------------------------------------

--
-- Table structure for table `professional_tbl`
--

CREATE TABLE `professional_tbl` (
  `mh_professional_id` int(5) NOT NULL,
  `type` varchar(10) NOT NULL,
  `professional_name` varchar(25) NOT NULL,
  `email` varchar(25) DEFAULT NULL,
  `contact_no` double NOT NULL,
  `gender` varchar(7) NOT NULL,
  `description` varchar(200) NOT NULL,
  `joining_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `pic` varchar(75) NOT NULL,
  `active` varchar(4) NOT NULL,
  `charges` int(4) NOT NULL,
  `password` varchar(15) NOT NULL,
  `resume` varchar(25) NOT NULL,
  `Degree` varchar(20) NOT NULL,
  `Experience` varchar(10) NOT NULL,
  `Language` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `professional_tbl`
--

INSERT INTO `professional_tbl` (`mh_professional_id`, `type`, `professional_name`, `email`, `contact_no`, `gender`, `description`, `joining_date`, `pic`, `active`, `charges`, `password`, `resume`, `Degree`, `Experience`, `Language`) VALUES
(301, 'expert', 'Bhoomika Gupta', 'bgupta@gmail.com', 5645289756, 'Female', 'I\'m a human being with flaws, who aims to become better each day by staying hopeful about a better tomorrow. Keeping an open mind and a flexible attitude helps me in cultivating this hope further. I\'v', '2022-03-11 04:40:20', 'bhoomika.png', 'Yes', 750, 'b1@happy', 'bhoomika.pdf', 'B.A, M.A, ', '2+ yrs', 'Hindi, English, Marathi'),
(302, 'doctor', 'Nitish Bose', 'nitish@gmail.com', 8564879238, 'Male', 'I developed a keen interest in human behaviour while pursuing my medical internship. I became aware of the pain that people with emotional difficulties face in their day to day life, and decided to jo', '2022-03-11 04:34:19', 'DrNitish.png', 'Yes', 1200, 'n@happys', 'nitish.docx', 'B.A, M.A', '3+ yrs', 'English, Hindi, Gujarati'),
(303, 'doctor', 'Soumya Pandya', 'soumya@gmail.com', 8327194475, 'Female', 'I am a Psychiatrist, trained from National institute of mental health and Neurosciences (NIMHANS) and Kasturba medical college, Mangalore with more than 12 years of experience in this field. I was ins', '2022-03-08 11:45:47', 'DrSoumya.png', 'Yes', 1200, 's@happys', 'soumya.docx', 'M.B.B.S, DPB', '12+ yrs', 'English, Hindi, Kannada'),
(304, 'expert', 'Gautam Krishnan', 'gautam@gmail.com', 5656420139, 'Male', 'I have been a licensed Clinical Psychologist since 2018 and have spent a couple of years teaching students along with practice. I underwent training in Acceptance and Commitment Therapy (ACT), which i', '2022-03-11 04:42:43', 'Gautam.jpg', 'Yes', 750, 'g1@happy', 'gautam.pdf', 'B.A, M.Sc,', '3+ yrs', 'English, Hindi, Kannada'),
(305, 'expert', 'Path Kalia', 'kalia@gmail.com', 8585656578, 'Male', 'I\'m a clinical mental health counselor with a broad background of experience and have worked with Depression, Anxiety, Personality Disorders, Trauma and Addictions as well as non-clinical areas like w', '2022-03-11 04:45:09', 'ParthGrey.jpg', 'Yes', 750, 'k1@happy', 'kalia.pdf', 'B.A, M.Sc ', '5+ yrs', 'English, Hindi'),
(306, 'expert', 'Shreya Madan', 'shreya@gmail.com', 12340405151, 'Female', 'My interest in mental health began from my school days and has only increased over time. I have completed my Master\'s in Applied Psychology (Clinical and Counselling Practice) from Tata Institute of S', '2022-03-11 04:52:52', 'Shreya.jpg', 'Yes', 750, 's@happy', 'shreya.pdf', 'B.A, M.A ', '1.5+ yrs', 'English, Hindi'),
(307, 'expert', 'Mrunmayi Adawadkar', 'mrunmayi@gmail.com', 2323757589, 'Female', 'My relationship with psychology has evolved from it being an interesting subject to making it a life-long calling. Learning about human behavior has given me a glimpse into my own story and untangled ', '2022-03-11 04:54:40', 'Mrunmayi.jpg', 'Yes', 750, 'm@happy', 'mrunmayi.pdf', 'M.Phil, M.A', '3+ yrs', 'English, Hindi, Marathi'),
(308, 'expert', 'Srishti Bajoria', 'shristhi@gmail.com', 5645307890, 'Female', 'Connecting with humans at a deeper level and understanding them has always been one of my core interests. As I dived deeper into the field and pursued psychology academically, it gave me a glimpse of ', '2022-03-11 04:58:15', 'Srishti.jpg', 'Yes', 425, 'sh@happy', 'shristhi.pdf', 'B.A, M.A ', '1.5+ yrs', 'English, Hindi'),
(309, 'expert', 'Pratishtha Trivedi Mirza', 'pratishtha@gmail.com', 8956201378, 'Female', 'I have been passionate about psychology since high school, where I got my first glimpse into understanding and interpreting human behaviour. Training and getting into practice has made my passion grow', '2022-03-11 05:17:55', 'pratishtha.jpg', 'Yes', 850, 'p@happy', 'pratishtha.pdf', 'M.A, M.Phil', '4+ yrs', 'English, Hindi, Marathi'),
(310, 'expert', 'Shuchi Sen', 'shuchi@gmail.com', 6363303020, 'Female', 'Shuchi has nine plus years of experience as psychotherapist in different capacities addressing client\'s personal, mental and emotional challenges and providing structured treatments. She assists her c', '2022-03-11 05:19:29', 'suchi.jpg', 'Yes', 425, 'shu@happy', 'shuchi.pdf', 'M.A', '9+ yrs', 'English, Hindi, Punjabi'),
(311, 'expert', 'Radhika Das', 'radhika@gmail.com', 8741254163, 'Female', '', '2022-04-06 12:14:15', '', 'Yes', 750, 'ra@happy', '', 'BA,MA ', '2+ yrs', 'English , Hindi'),
(312, 'expert', 'Tanya Mirza', 'tanya@gmail.com', 7841279574, 'Female ', '', '2022-04-06 12:14:15', '', 'Yes', 750, 'tan@happy', '', 'BA,MA', '2+yrs', 'Hindi, English'),
(313, 'expert', 'Vartika Jha ', 'var@gmail.com', 8741267451, 'Female', '', '2022-04-06 13:18:55', '', '', 750, 'var@happy', '', 'BA,MA ', '2+ yrs', 'English , Hindi'),
(314, 'expert', 'Bubbly Sodhani', 'bub@gmail.com', 8741254789, 'Female', '', '2022-04-06 13:18:55', '', 'Yes', 750, 'bo@happy', '', 'BA,MA', '2+yrs', 'Hindi, English');

-- --------------------------------------------------------

--
-- Table structure for table `testuserans_tbl`
--

CREATE TABLE `testuserans_tbl` (
  `Testuserans_id` int(5) NOT NULL,
  `User_Option` varchar(50) NOT NULL,
  `User_id` int(5) NOT NULL,
  `Test_queid` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `testuserans_tbl`
--

INSERT INTO `testuserans_tbl` (`Testuserans_id`, `User_Option`, `User_id`, `Test_queid`) VALUES
(3221, '0', 104, 1101),
(3222, '1', 104, 1102),
(3223, '1', 104, 1103),
(3224, '1', 104, 1104),
(3225, '1', 104, 1105),
(3226, '1', 104, 1106),
(3227, '1', 104, 1107),
(3228, '1', 104, 1108),
(3229, '2', 104, 1109),
(3230, '1', 104, 1110);

-- --------------------------------------------------------

--
-- Table structure for table `test_tbl`
--

CREATE TABLE `test_tbl` (
  `test_questionid` int(5) NOT NULL,
  `test_question` varchar(75) NOT NULL,
  `option1` varchar(25) NOT NULL,
  `option2` varchar(25) NOT NULL,
  `option3` varchar(25) NOT NULL,
  `option4` varchar(25) NOT NULL,
  `option1_marks` int(3) NOT NULL,
  `option2_marks` int(3) NOT NULL,
  `option3_marks` int(3) NOT NULL,
  `option4_marks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test_tbl`
--

INSERT INTO `test_tbl` (`test_questionid`, `test_question`, `option1`, `option2`, `option3`, `option4`, `option1_marks`, `option2_marks`, `option3_marks`, `option4_marks`) VALUES
(1101, 'Little interest or pleasure in doing things?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1102, 'Feeling down, depressed, or hopeless? ', 'Not at all', 'Several days', 'More than half of the day', ' Nearly every day', 0, 1, 2, 3),
(1103, 'Trouble falling or staying asleep, or sleeping too?', 'Not at all ', 'Several days        ', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1104, 'Feeling tired or having little energy? ', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1105, 'Poor appetite or overeating?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1106, 'Do you worry about lots of different things?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1107, ' Do you have trouble controlling your worries?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1108, 'Do you get irritable and/or easily annoyed when anxious?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1109, 'Does worry or anxiety make you feel fatigued or worn out?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3),
(1110, 'Does worry or anxiety interfere with falling and/or staying asleep?', 'Not at all', 'Several days', 'More than half of the day', 'Nearly every day', 0, 1, 2, 3);

-- --------------------------------------------------------

--
-- Stand-in structure for view `user type report`
-- (See below for the actual view)
--
CREATE TABLE `user type report` (
`user_id` int(5)
,`is_admin` varchar(4)
,`name` varchar(25)
,`email` varchar(45)
,`contact_no` varchar(11)
,`gender` varchar(6)
);

-- --------------------------------------------------------

--
-- Table structure for table `user_tbl`
--

CREATE TABLE `user_tbl` (
  `user_id` int(5) NOT NULL,
  `is_admin` varchar(4) NOT NULL,
  `name` varchar(25) NOT NULL,
  `email` varchar(45) NOT NULL,
  `joining_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `contact_no` varchar(11) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `password` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_tbl`
--

INSERT INTO `user_tbl` (`user_id`, `is_admin`, `name`, `email`, `joining_date`, `contact_no`, `gender`, `password`) VALUES
(101, 'Yes', 'Mental health', 'mentalhealthproject19@gmail.com', '2022-03-08 11:24:35', '9327194472', 'Female', 'f1@happy'),
(102, 'No', 'Daisy solomon', 'daisy@gmail.com', '2022-03-08 11:24:35', '8520520121', 'Female', 'd1@happy'),
(103, 'No', 'Namita shah', 'namita@gmail.com', '2022-03-08 11:25:32', '9429448655', 'Female', '12345678'),
(104, 'No', 'Shivangi Shah ', 'shivangi@gmail.com', '2022-03-11 12:21:30', '8955674182', 'Female', 's1@happy'),
(105, 'No', 'Jessica Mandela ', 'jessica@gmail.com', '2022-03-11 12:25:17', '7842514236', 'Female', 'j1@happy '),
(106, 'No', 'Nishant Das ', 'nishant@gmail.com', '2022-03-11 12:26:14', '8417259634', 'Male', 'ni@happy '),
(107, 'No', 'John Makhija ', 'john@gmail.com', '2022-03-11 12:27:02', '6924153578', 'Male', 'jo@happy'),
(108, 'No', 'Tanvi Gupta ', 'tanvi@gmail.com', '2022-03-11 12:28:09', '8741253975', 'Female', 'ta@happy'),
(109, 'No', 'Naman Sodhani ', 'naman@gmail.com', '2022-03-11 12:28:42', '7412564123', 'Male', 'nam@happy'),
(110, 'No', 'Tarun Grover ', 'tarun@gmail.com', '2022-03-11 12:29:25', '8741529674', 'Male', 'tar@happy'),
(111, 'No', 'Khushali Shah', 'khushali@gmail.com', '2022-03-30 17:57:54', '985719425', 'Female', 'k1@happy'),
(112, 'No', 'Nivedita Thakur', 'niv@gmail.com', '2022-04-06 10:41:01', '8741254162', 'Female', 'niv@happy'),
(113, 'No', 'Monali Tez', 'mona@gmail.com', '2022-04-06 10:41:01', '8741256214', 'Female', 'mon@hmail.com'),
(114, 'No', 'Ram Kapoor', 'ra@gmail.com', '2022-04-06 12:27:39', '8741257419', 'Male', 'ram@happy'),
(115, 'No', 'Diya Pathak', 'di@gmail.com', '2022-04-06 12:27:39', '7412841296', 'Female', 'diy@happy'),
(116, 'No', 'Tarang Joshi', 'tara@gmail.com', '2022-04-06 13:09:01', '6874125741', 'Male', 'an@happy'),
(117, 'No', 'Tom Das', 'tom@gmail.com', '2022-04-06 13:09:48', '8741274159', 'Male', 'tom@happy');

-- --------------------------------------------------------

--
-- Structure for view `charges wise booking report`
--
DROP TABLE IF EXISTS `charges wise booking report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `charges wise booking report`  AS SELECT `book_tbl`.`book_id` AS `book_id`, `book_tbl`.`book_time` AS `book_time`, `user_tbl`.`name` AS `name`, `professional_tbl`.`professional_name` AS `professional_name`, `book_tbl`.`charges` AS `charges` FROM ((`user_tbl` join `book_tbl` on(`user_tbl`.`user_id` = `book_tbl`.`user_id`)) join `professional_tbl` on(`professional_tbl`.`mh_professional_id` = `book_tbl`.`mh_professional_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `communtiy group wise community questions report`
--
DROP TABLE IF EXISTS `communtiy group wise community questions report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `communtiy group wise community questions report`  AS SELECT `community_tbl`.`communityque_id` AS `communityque_id`, `community_tbl`.`community_ques` AS `community_ques`, `community_tbl`.`qpost_date` AS `qpost_date`, `community_tbl`.`community_group` AS `community_group`, `user_tbl`.`user_id` AS `user_id`, `user_tbl`.`name` AS `name` FROM (`user_tbl` join `community_tbl` on(`user_tbl`.`user_id` = `community_tbl`.`user_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `comunty group wise communty answer report`
--
DROP TABLE IF EXISTS `comunty group wise communty answer report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `comunty group wise communty answer report`  AS SELECT `communityanswer_tbl`.`answer_id` AS `answer_id`, `community_tbl`.`community_ques` AS `community_ques`, `communityanswer_tbl`.`community_ans` AS `community_ans`, `communityanswer_tbl`.`apost_date` AS `apost_date`, `communityanswer_tbl`.`community_group` AS `community_group`, `professional_tbl`.`professional_name` AS `professional_name` FROM ((`communityanswer_tbl` join `professional_tbl` on(`professional_tbl`.`mh_professional_id` = `communityanswer_tbl`.`mh_professional_id`)) join `community_tbl` on(`community_tbl`.`communityque_id` = `communityanswer_tbl`.`communityque_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `content type wise content report`
--
DROP TABLE IF EXISTS `content type wise content report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `content type wise content report`  AS SELECT `content_tbl`.`content_id` AS `content_id`, `content_tbl`.`c_name` AS `c_name`, `content_tbl`.`status` AS `status`, `content_tbl`.`con_description` AS `con_description`, `content_tbl`.`image` AS `image`, `content_tbl`.`audio` AS `audio`, `content_tbl`.`video` AS `video`, `content_typetbl`.`con_name` AS `con_name` FROM (`content_tbl` join `content_typetbl` on(`content_typetbl`.`con_typeid` = `content_tbl`.`con_typeid`))  ;

-- --------------------------------------------------------

--
-- Structure for view `event wise event booking report`
--
DROP TABLE IF EXISTS `event wise event booking report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `event wise event booking report`  AS SELECT `event_booking`.`event_bookid` AS `event_bookid`, `event_tbl`.`event_name` AS `event_name`, `user_tbl`.`name` AS `name`, `event_booking`.`user_email` AS `user_email`, `event_booking`.`user_mobile` AS `user_mobile` FROM ((`event_booking` join `user_tbl` on(`user_tbl`.`user_id` = `event_booking`.`user_id`)) join `event_tbl` on(`event_tbl`.`event_id` = `event_booking`.`event_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `experience range wise professional report`
--
DROP TABLE IF EXISTS `experience range wise professional report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `experience range wise professional report`  AS SELECT `professional_tbl`.`mh_professional_id` AS `mh_professional_id`, `professional_tbl`.`type` AS `type`, `professional_tbl`.`professional_name` AS `professional_name`, `professional_tbl`.`email` AS `email`, `professional_tbl`.`contact_no` AS `contact_no`, `professional_tbl`.`gender` AS `gender`, `professional_tbl`.`active` AS `active`, `professional_tbl`.`charges` AS `charges`, `professional_tbl`.`Degree` AS `Degree`, `professional_tbl`.`Experience` AS `Experience`, `professional_tbl`.`Language` AS `Language` FROM `professional_tbl``professional_tbl`  ;

-- --------------------------------------------------------

--
-- Structure for view `gender wise professional report`
--
DROP TABLE IF EXISTS `gender wise professional report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `gender wise professional report`  AS SELECT `professional_tbl`.`mh_professional_id` AS `mh_professional_id`, `professional_tbl`.`type` AS `type`, `professional_tbl`.`professional_name` AS `professional_name`, `professional_tbl`.`email` AS `email`, `professional_tbl`.`contact_no` AS `contact_no`, `professional_tbl`.`gender` AS `gender`, `professional_tbl`.`active` AS `active`, `professional_tbl`.`charges` AS `charges`, `professional_tbl`.`Degree` AS `Degree`, `professional_tbl`.`Experience` AS `Experience`, `professional_tbl`.`Language` AS `Language` FROM `professional_tbl``professional_tbl`  ;

-- --------------------------------------------------------

--
-- Structure for view `gender wise user report`
--
DROP TABLE IF EXISTS `gender wise user report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `gender wise user report`  AS SELECT `user_tbl`.`user_id` AS `user_id`, `user_tbl`.`is_admin` AS `is_admin`, `user_tbl`.`name` AS `name`, `user_tbl`.`email` AS `email`, `user_tbl`.`joining_date` AS `joining_date`, `user_tbl`.`contact_no` AS `contact_no`, `user_tbl`.`gender` AS `gender` FROM `user_tbl``user_tbl`  ;

-- --------------------------------------------------------

--
-- Structure for view `language known wise professional report`
--
DROP TABLE IF EXISTS `language known wise professional report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `language known wise professional report`  AS SELECT `professional_tbl`.`mh_professional_id` AS `mh_professional_id`, `professional_tbl`.`type` AS `type`, `professional_tbl`.`professional_name` AS `professional_name`, `professional_tbl`.`email` AS `email`, `professional_tbl`.`contact_no` AS `contact_no`, `professional_tbl`.`gender` AS `gender`, `professional_tbl`.`charges` AS `charges`, `professional_tbl`.`Degree` AS `Degree`, `professional_tbl`.`Experience` AS `Experience`, `professional_tbl`.`Language` AS `Language` FROM `professional_tbl``professional_tbl`  ;

-- --------------------------------------------------------

--
-- Structure for view `payment mode wise payment report`
--
DROP TABLE IF EXISTS `payment mode wise payment report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `payment mode wise payment report`  AS SELECT `payment_tbl`.`payment_id` AS `payment_id`, `payment_tbl`.`book_id` AS `book_id`, `payment_tbl`.`payment_mode` AS `payment_mode`, `payment_tbl`.`payment_status` AS `payment_status`, `payment_tbl`.`user_id` AS `user_id`, `payment_tbl`.`payment_amount` AS `payment_amount`, `user_tbl`.`name` AS `name` FROM ((`payment_tbl` join `book_tbl` on(`book_tbl`.`book_id` = `payment_tbl`.`book_id`)) join `user_tbl` on(`user_tbl`.`user_id` = `payment_tbl`.`user_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `payment status wise payment report`
--
DROP TABLE IF EXISTS `payment status wise payment report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `payment status wise payment report`  AS SELECT `payment_tbl`.`payment_id` AS `payment_id`, `payment_tbl`.`book_id` AS `book_id`, `payment_tbl`.`payment_mode` AS `payment_mode`, `payment_tbl`.`payment_status` AS `payment_status`, `payment_tbl`.`payment_amount` AS `payment_amount`, `user_tbl`.`name` AS `name` FROM ((`payment_tbl` join `book_tbl` on(`book_tbl`.`book_id` = `payment_tbl`.`book_id`)) join `user_tbl` on(`user_tbl`.`user_id` = `payment_tbl`.`user_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `professional type wise booking report`
--
DROP TABLE IF EXISTS `professional type wise booking report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `professional type wise booking report`  AS SELECT `book_tbl`.`book_id` AS `book_id`, `book_tbl`.`book_time` AS `book_time`, `user_tbl`.`name` AS `name`, `book_tbl`.`book_question` AS `book_question`, `book_tbl`.`charges` AS `charges`, `book_tbl`.`user_mobile` AS `user_mobile`, `professional_tbl`.`type` AS `type`, `professional_tbl`.`professional_name` AS `professional_name` FROM ((`book_tbl` join `professional_tbl` on(`professional_tbl`.`mh_professional_id` = `book_tbl`.`mh_professional_id`)) join `user_tbl` on(`user_tbl`.`user_id` = `book_tbl`.`user_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `professional type wise professional report`
--
DROP TABLE IF EXISTS `professional type wise professional report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `professional type wise professional report`  AS SELECT `professional_tbl`.`mh_professional_id` AS `mh_professional_id`, `professional_tbl`.`type` AS `type`, `professional_tbl`.`professional_name` AS `professional_name`, `professional_tbl`.`email` AS `email`, `professional_tbl`.`contact_no` AS `contact_no`, `professional_tbl`.`gender` AS `gender`, `professional_tbl`.`active` AS `active`, `professional_tbl`.`charges` AS `charges`, `professional_tbl`.`Degree` AS `Degree`, `professional_tbl`.`Experience` AS `Experience`, `professional_tbl`.`Language` AS `Language` FROM `professional_tbl``professional_tbl`  ;

-- --------------------------------------------------------

--
-- Structure for view `user type report`
--
DROP TABLE IF EXISTS `user type report`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `user type report`  AS SELECT `user_tbl`.`user_id` AS `user_id`, `user_tbl`.`is_admin` AS `is_admin`, `user_tbl`.`name` AS `name`, `user_tbl`.`email` AS `email`, `user_tbl`.`contact_no` AS `contact_no`, `user_tbl`.`gender` AS `gender` FROM `user_tbl``user_tbl`  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book_tbl`
--
ALTER TABLE `book_tbl`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `communityanswer_tbl`
--
ALTER TABLE `communityanswer_tbl`
  ADD PRIMARY KEY (`answer_id`);

--
-- Indexes for table `community_tbl`
--
ALTER TABLE `community_tbl`
  ADD PRIMARY KEY (`communityque_id`);

--
-- Indexes for table `content_tbl`
--
ALTER TABLE `content_tbl`
  ADD PRIMARY KEY (`content_id`);

--
-- Indexes for table `content_typetbl`
--
ALTER TABLE `content_typetbl`
  ADD PRIMARY KEY (`con_typeid`);

--
-- Indexes for table `event_booking`
--
ALTER TABLE `event_booking`
  ADD PRIMARY KEY (`event_bookid`);

--
-- Indexes for table `event_tbl`
--
ALTER TABLE `event_tbl`
  ADD PRIMARY KEY (`event_id`);

--
-- Indexes for table `feedback_tbl`
--
ALTER TABLE `feedback_tbl`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `payment_tbl`
--
ALTER TABLE `payment_tbl`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `professional_tbl`
--
ALTER TABLE `professional_tbl`
  ADD PRIMARY KEY (`mh_professional_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `testuserans_tbl`
--
ALTER TABLE `testuserans_tbl`
  ADD PRIMARY KEY (`Testuserans_id`);

--
-- Indexes for table `test_tbl`
--
ALTER TABLE `test_tbl`
  ADD PRIMARY KEY (`test_questionid`);

--
-- Indexes for table `user_tbl`
--
ALTER TABLE `user_tbl`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book_tbl`
--
ALTER TABLE `book_tbl`
  MODIFY `book_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=720;

--
-- AUTO_INCREMENT for table `communityanswer_tbl`
--
ALTER TABLE `communityanswer_tbl`
  MODIFY `answer_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=611;

--
-- AUTO_INCREMENT for table `community_tbl`
--
ALTER TABLE `community_tbl`
  MODIFY `communityque_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=522;

--
-- AUTO_INCREMENT for table `content_tbl`
--
ALTER TABLE `content_tbl`
  MODIFY `content_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4116;

--
-- AUTO_INCREMENT for table `content_typetbl`
--
ALTER TABLE `content_typetbl`
  MODIFY `con_typeid` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3112;

--
-- AUTO_INCREMENT for table `event_booking`
--
ALTER TABLE `event_booking`
  MODIFY `event_bookid` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=417;

--
-- AUTO_INCREMENT for table `event_tbl`
--
ALTER TABLE `event_tbl`
  MODIFY `event_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=211;

--
-- AUTO_INCREMENT for table `feedback_tbl`
--
ALTER TABLE `feedback_tbl`
  MODIFY `feedback_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=812;

--
-- AUTO_INCREMENT for table `payment_tbl`
--
ALTER TABLE `payment_tbl`
  MODIFY `payment_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=911;

--
-- AUTO_INCREMENT for table `professional_tbl`
--
ALTER TABLE `professional_tbl`
  MODIFY `mh_professional_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3013;

--
-- AUTO_INCREMENT for table `testuserans_tbl`
--
ALTER TABLE `testuserans_tbl`
  MODIFY `Testuserans_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3231;

--
-- AUTO_INCREMENT for table `user_tbl`
--
ALTER TABLE `user_tbl`
  MODIFY `user_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=118;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
