@echo off

:: 가상 환경 경로 설정 (필요에 따라 수정)
set VENV_PATH=.\venv

:: Python 실행 파일 경로 설정 (필요에 따라 수정)
set PYTHON=%VENV_PATH%\Scripts\python.exe

:: 가상 환경 활성화
call %VENV_PATH%\Scripts\activate.bat

:: main.py 실행
%PYTHON% .\src\main.py

:: 실행 후 일시 중지 (오류 메시지 확인용, 필요하면 주석 처리)
pause

:: 가상 환경 비활성화
call %VENV_PATH%\Scripts\deactivate.bat