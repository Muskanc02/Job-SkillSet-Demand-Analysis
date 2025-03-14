CREATE SCHEMA Job_Listings_DB;
USE Job_Listings_DB;
CREATE TABLE `Listings`(
    `ListingID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `JobID` BIGINT NOT NULL,
    `JobTitle` VARCHAR(255) NOT NULL,
    `LocationID` BIGINT NOT NULL,
    `ModeID` BIGINT NOT NULL,
    `CompanyID` BIGINT NOT NULL
);
ALTER TABLE
    `Listings` ADD UNIQUE `listings_jobid_unique`(`JobID`);
CREATE TABLE `Locations`(
    `LocationID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `City` VARCHAR(255) NOT NULL,
    `District` VARCHAR(255) NOT NULL,
    `Country` VARCHAR(255) NOT NULL
);
CREATE TABLE `JobMode`(
    `ModeID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `WorkMode` VARCHAR(255) NOT NULL,
    `JobType` VARCHAR(255) NOT NULL
);
CREATE TABLE `Company`(
    `CompanyID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `CompanyName` VARCHAR(255) NOT NULL,
    `Industry` BIGINT NOT NULL
);
CREATE TABLE `ListingHaveSkillSet`(
    `ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `ListingID` BIGINT NOT NULL,
    `SkillSetID` BIGINT NOT NULL
);
CREATE TABLE `SkillSets`(
    `SkillSetID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Skills` VARCHAR(255) NOT NULL,
    `LanguageID` BIGINT NOT NULL
);
CREATE TABLE `Language`(
    `LanguageID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL
);

ALTER TABLE `Listings` MODIFY `ModeID` bigint unsigned;
ALTER TABLE `Listings` MODIFY `CompanyID` bigint unsigned;
ALTER TABLE `Listings` MODIFY `LocationID` bigint unsigned;
ALTER TABLE `SkillSets` MODIFY `LanguageID` bigint unsigned;
ALTER TABLE `ListingHaveSkillSet` MODIFY `ListingID` bigint unsigned;
ALTER TABLE `ListingHaveSkillSet` MODIFY `SkillSetID` bigint unsigned;
ALTER TABLE
    `Listings` ADD CONSTRAINT `listings_modeid_foreign` FOREIGN KEY(`ModeID`) REFERENCES `JobMode`(`ModeID`);
ALTER TABLE
    `ListingHaveSkillSet` ADD CONSTRAINT `listinghaveskillset_listingid_foreign` FOREIGN KEY(`ListingID`) REFERENCES `Listings`(`ListingID`);
ALTER TABLE
    `SkillSets` ADD CONSTRAINT `skillsets_languageid_foreign` FOREIGN KEY(`LanguageID`) REFERENCES `Language`(`LanguageID`);
ALTER TABLE
    `Listings` ADD CONSTRAINT `listings_companyid_foreign` FOREIGN KEY(`CompanyID`) REFERENCES `Company`(`CompanyID`);
ALTER TABLE
    `Listings` ADD CONSTRAINT `listings_locationid_foreign` FOREIGN KEY(`LocationID`) REFERENCES `Locations`(`LocationID`);
ALTER TABLE
    `ListingHaveSkillSet` ADD CONSTRAINT `listinghaveskillset_skillsetid_foreign` FOREIGN KEY(`SkillSetID`) REFERENCES `SkillSets`(`SkillSetID`);
    
   



