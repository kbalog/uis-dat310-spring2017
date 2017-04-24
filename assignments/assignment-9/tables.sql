--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `description` text NOT NULL,
  `price` double NOT NULL,
  `bonus_price` double NOT NULL,
  `photo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT;


--
-- Table structure for table `orders_head`
--

CREATE TABLE `orders_head` (
  `order_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `telephone` varchar(15) NOT NULL,
  `billing_city` varchar(20) NOT NULL,
  `billing_street` varchar(30) NOT NULL,
  `billing_postcode` varchar(6) NOT NULL,
  `shipping_city` varchar(20) NOT NULL,
  `shipping_street` varchar(30) NOT NULL,
  `shipping_postcode` varchar(6) NOT NULL,
  `order_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for table `orders_head`
--
ALTER TABLE `orders_head`
  ADD PRIMARY KEY (`order_id`);

--
-- AUTO_INCREMENT for table `orders_head`
--
ALTER TABLE `orders_head`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;
  
  
--
-- Table structure for table `orders_details`
--

CREATE TABLE `orders_details` (
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for table `orders_details`
--
ALTER TABLE `orders_details`
  ADD KEY `order_id` (`order_id`,`product_id`);
