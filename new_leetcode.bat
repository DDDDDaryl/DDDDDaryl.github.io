@echo off
CALL E:\Anaconda\Scripts\activate.bat E:\Anaconda
start python %~dp0new.py dailyLearning/Leetcode %1
choice /c yn /t 1 /d y
start ./source/_posts/dailyLearning/Leetcode/%1
echo "Done. Opening created file..."
