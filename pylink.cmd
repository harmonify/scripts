@REM by Amr Ali on https://stackoverflow.com/a/27083780\

@echo off
echo Running pylink.cmd as elevated user...
echo Log file    : %~dp0pylink.log
echo.
<!-- : --- Self-Elevating Batch Script ---------------------------
@whoami /groups | find "S-1-16-12288" > nul && goto :admin
set "ELEVATE_CMDLINE=cd /d "%~dp0" & call "%~f0" %*"
cscript //nologo "%~f0?.wsf" //job:Elevate & exit /b
-->
<job id="Elevate"><script language="VBScript">
  Set objShell = CreateObject("Shell.Application")
  Set objWshShell = WScript.CreateObject("WScript.Shell")
  Set objWshProcessEnv = objWshShell.Environment("PROCESS")
  strCommandLine = Trim(objWshProcessEnv("ELEVATE_CMDLINE"))
  objShell.ShellExecute "cmd", "/c " & strCommandLine, "", "runas"
</script></job>
:admin -----------------------------------------------------------
:: administrator commands here
:: run command and set it to %output% variable
for /f "delims=" %%i in ('cmd /k python pylink %*') do set output=%%i
:: then echo %output% with timestamp to pylink.log
echo %date% %time% %output% >> %~dp0pylink.log
exit /b