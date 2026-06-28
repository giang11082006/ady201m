# PLAN

# ĐỀ TÀI

# **Xây dựng và Tối ưu hóa Mô hình Machine Learning cho Bài toán Dự đoán Giá Nhà**

* **Môn học:** ADY201m – Introduction to Data Science
* **Lớp:** AI2013
* **Giảng viên hướng dẫn:** ....................................

---

# 1. MỤC TIÊU

Mục tiêu của dự án là xây dựng một mô hình Machine Learning có khả năng dự đoán giá nhà dựa trên các đặc trưng của bất động sản như diện tích, số phòng ngủ, số phòng tắm, loại nhà, vị trí và các thông tin liên quan. Đồng thời, nhóm sẽ đánh giá, so sánh nhiều thuật toán hồi quy và tối ưu hóa mô hình nhằm nâng cao độ chính xác của dự đoán. Kết quả của dự án giúp người dùng có thể ước lượng giá trị bất động sản và hỗ trợ ra quyết định trong lĩnh vực mua bán nhà ở.

---

# 2. BẢNG THÀNH VIÊN VÀ PHÂN CÔNG NHIỆM VỤ

| STT | Họ và tên    | MSSV     | Vai trò                                         | Nhiệm vụ chi tiết                                                                                                                                                                      | Output dự kiến                                                              |
| --- | ------------ | -------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 1   | Thành viên 1 | ........ | Data Engineer                                   | Thu thập dữ liệu, kiểm tra chất lượng dữ liệu, thiết kế cấu trúc dữ liệu, xử lý dữ liệu thiếu, chuẩn hóa dữ liệu, lưu trữ dataset và quản lý GitHub.                                   | Dataset gốc, Dataset đã làm sạch, Source code tiền xử lý                    |
| 2   | Thành viên 2 | ........ | Data Analyst                                    | Xây dựng Business Questions, thực hiện EDA, trực quan hóa dữ liệu, phân tích Insight, viết báo cáo phần phân tích dữ liệu và hỗ trợ thiết kế Slide thuyết trình.                       | Biểu đồ, Insight, Báo cáo EDA, Slide                                        |
| 3   | Thành viên 3 | ........ | Data Scientist                                  | Phân tích thống kê, Feature Engineering, xây dựng các mô hình hồi quy (Linear Regression, Decision Tree, Random Forest), tối ưu Hyperparameter, đánh giá mô hình bằng MAE, RMSE và R². | Notebook xây dựng mô hình, Báo cáo đánh giá mô hình                         |
| 4   | Thành viên 4 | ........ | Machine Learning Engineer / Project Coordinator | Tổng hợp code, kiểm tra tính nhất quán của toàn bộ dự án, hỗ trợ tối ưu mô hình, chuẩn bị phần trình bày, tổng hợp báo cáo cuối cùng và quản lý tiến độ nhóm.                          | Notebook hoàn chỉnh, Báo cáo tổng hợp, Slide thuyết trình, Source code cuối |

---

# 3. LỘ TRÌNH THỰC HIỆN DỰ ÁN

## Giai đoạn 1: Business Understanding & Data Collection

**Deadline:** ....................................

### Công việc

* Xác định mục tiêu bài toán.
* Xây dựng các Business Questions.
* Thu thập dữ liệu giá nhà.
* Tìm hiểu ý nghĩa của các thuộc tính.
* Kiểm tra số lượng mẫu và chất lượng dữ liệu.

**Nhân sự chính**

* Thành viên 1
* Thành viên 2

**Phân công cụ thể**

* **Thành viên 1:** Thu thập dữ liệu, kiểm tra định dạng, lưu trữ dataset ban đầu.
* **Thành viên 2:** Xây dựng Business Questions, xác định các vấn đề cần phân tích từ dữ liệu.

**Output**

* Dataset ban đầu.
* Danh sách Business Questions.
* Báo cáo mô tả dữ liệu.

---

## Giai đoạn 2: Data Preprocessing

**Deadline:** ....................................

### Công việc

* Kiểm tra Missing Values.
* Kiểm tra Duplicate.
* Phát hiện và xử lý Outlier.
* Chuyển đổi kiểu dữ liệu.
* Feature Encoding (One-Hot Encoding).
* Chuẩn hóa dữ liệu khi cần.
* Phân tích phân phối của biến Price.
* Áp dụng Log Transformation nếu phù hợp.

**Nhân sự chính**

* Thành viên 1
* Thành viên 3

**Phân công cụ thể**

* **Thành viên 1:** Làm sạch dữ liệu, xử lý missing values, duplicate, outlier và chuẩn hóa dữ liệu đầu vào.
* **Thành viên 3:** Kiểm tra ảnh hưởng của các bước tiền xử lý đến dữ liệu, hỗ trợ feature engineering và chuẩn bị dữ liệu cho mô hình.

**Output**

* Dataset đã làm sạch.
* Notebook tiền xử lý dữ liệu.

---

## Giai đoạn 3: Exploratory Data Analysis (EDA)

**Deadline:** ....................................

### Công việc

* Phân tích thống kê mô tả.

* Phân tích phân phối dữ liệu.

* Phân tích tương quan giữa các biến.

* Trực quan hóa dữ liệu bằng:

  * Histogram
  * Boxplot
  * Scatter Plot
  * Heatmap Correlation
  * Pairplot (nếu cần)

* Đưa ra các Insight từ dữ liệu.

**Nhân sự chính**

* Thành viên 2
* Thành viên 4

**Phân công cụ thể**

* **Thành viên 2:** Thực hiện EDA, trực quan hóa dữ liệu và rút ra insight chính.
* **Thành viên 4:** Tổng hợp kết quả EDA, chuẩn hóa nội dung trình bày và hỗ trợ viết phần báo cáo phân tích.

**Output**

* Các biểu đồ trực quan.
* Báo cáo EDA.
* Insight của dữ liệu.

---

## Giai đoạn 4: Modeling & Evaluation

**Deadline:** ....................................

### Công việc

* Chia dữ liệu Train/Test.

* Huấn luyện các mô hình:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor

* So sánh hiệu năng giữa các mô hình.

* Tối ưu Random Forest bằng RandomizedSearchCV.

* Đánh giá mô hình bằng:

  * MAE
  * RMSE
  * R² Score

* Phân tích Feature Importance.

* Chọn mô hình cuối cùng.

**Nhân sự chính**

* Thành viên 3
* Thành viên 4

**Phân công cụ thể**

* **Thành viên 3:** Xây dựng và đánh giá các mô hình hồi quy, thực hiện tối ưu hyperparameter.
* **Thành viên 4:** Kiểm tra kết quả mô hình, tổng hợp bảng so sánh, phân tích feature importance và lựa chọn mô hình cuối cùng cùng nhóm.

**Output**

* Notebook Modeling.
* Bảng so sánh các mô hình.
* Mô hình tốt nhất.

---

## Giai đoạn 5: Reporting & Presentation

**Deadline:** ....................................

### Công việc

* Tổng hợp toàn bộ kết quả.
* Phân tích ưu điểm và hạn chế của mô hình.
* Hoàn thiện báo cáo.
* Thiết kế Slide.
* Chuẩn bị thuyết trình.

**Nhân sự chính**

* Toàn bộ nhóm

**Phân công cụ thể**

* **Thành viên 1:** Cung cấp phần dữ liệu, tiền xử lý và mô tả quy trình làm sạch.
* **Thành viên 2:** Trình bày phần EDA, insight và trực quan hóa dữ liệu.
* **Thành viên 3:** Trình bày phần xây dựng mô hình, đánh giá và tối ưu mô hình.
* **Thành viên 4:** Tổng hợp nội dung, hoàn thiện báo cáo, chỉnh sửa slide và điều phối phần thuyết trình.

**Output**

* Báo cáo hoàn chỉnh.
* Slide thuyết trình.
* Source Code.
* Dataset.
* Notebook cuối cùng.

---

# Deliverables

* Dataset gốc.
* Dataset sau tiền xử lý.
* Notebook EDA.
* Notebook Modeling.
* Notebook Hyperparameter Tuning.
* Báo cáo phân tích.
* Slide thuyết trình.
* Source Code.
* Mô hình Machine Learning cuối cùng.

---

# Công nghệ sử dụng

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# Kết quả mong đợi

* Xây dựng thành công mô hình dự đoán giá nhà.
* So sánh nhiều thuật toán hồi quy để lựa chọn mô hình phù hợp.
* Đạt mô hình có độ chính xác cao (đánh giá bằng MAE, RMSE và R²).
* Phân tích các yếu tố ảnh hưởng lớn nhất đến giá nhà thông qua Feature Importance.
* Hoàn thiện quy trình Data Science từ thu thập dữ liệu, tiền xử lý, trực quan hóa, xây dựng mô hình đến đánh giá kết quả.
