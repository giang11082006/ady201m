
-- MỤC ĐÍCH: Tạo database riêng để lưu trữ dữ liệu Zillow
-- HỆ QUẢN TRỊ: SQL Server
-- ============================================================
USE master;
GO

-- ============================================================
-- TẠO DATABASE NẾU CHƯA TỒN TẠI
-- ============================================================
-- Kiểm tra xem database ZillowRealEstateDB đã tồn tại chưa.
-- Nếu chưa tồn tại thì tạo mới.
-- Nếu đã tồn tại thì không tạo lại để tránh xóa nhầm dữ liệu.

IF DB_ID(N'ZillowRealEstateDB') IS NULL
BEGIN
    CREATE DATABASE ZillowRealEstateDB;
END;
GO

-- ============================================================
-- CHỌN DATABASE ĐỂ SỬ DỤNG
-- ============================================================
-- Sau khi tạo xong, dùng lệnh USE để đảm bảo các bảng,
-- khóa chính, khóa ngoại và dữ liệu sau này đều được tạo
-- trong database ZillowRealEstateDB.

USE ZillowRealEstateDB;
GO

-- ============================================================
-- KIỂM TRA DATABASE HIỆN TẠI
-- ============================================================
-- Câu lệnh này dùng để kiểm tra xem mình đã chọn đúng database chưa.

SELECT DB_NAME() AS current_database;
GO