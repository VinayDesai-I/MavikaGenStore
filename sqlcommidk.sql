-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: idk
-- Source Schemata: vinayproject2
-- Created: Mon Nov 20 15:05:10 2023
-- Workbench Version: 8.0.32
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema idk
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `idk` ;
CREATE SCHEMA IF NOT EXISTS `idk` ;

-- ----------------------------------------------------------------------------
-- Table idk.admins
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `idk`.`admins` (
  `adm_name` VARCHAR(20) NULL DEFAULT NULL,
  `adm_password` VARCHAR(20) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table idk.bills
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `idk`.`bills` (
  `Cust_Name` VARCHAR(30) NULL DEFAULT NULL,
  `All_Items` VARCHAR(80) NULL DEFAULT NULL,
  `Total_Units` INT NULL DEFAULT NULL,
  `Total_Price` INT NULL DEFAULT NULL,
  `Delivery` VARCHAR(5) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table idk.delivery
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `idk`.`delivery` (
  `user_name` VARCHAR(30) NULL DEFAULT NULL,
  `user_number` INT NULL DEFAULT NULL,
  `user_address` VARCHAR(60) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table idk.items
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `idk`.`items` (
  `ITEM_ID` INT NULL DEFAULT NULL,
  `ITEM_NAME` VARCHAR(20) NULL DEFAULT NULL,
  `STOCK_QTY` INT NULL DEFAULT NULL,
  `ITEM_PRICE` INT NULL DEFAULT NULL,
  `ITEM_MANU_DATE` DATE NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table idk.user
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `idk`.`user` (
  `user_name` VARCHAR(30) NULL DEFAULT NULL,
  `user_password` VARCHAR(20) NULL DEFAULT NULL,
  `user_number` BIGINT NULL DEFAULT NULL,
  `user_address` VARCHAR(35) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;
