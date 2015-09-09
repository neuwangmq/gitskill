[url=home.php?mod=space&uid=266048]@echo[/url] off
title Sublime Text Tools By:Joker`ST
echo.
echo. Sublime Text Tools
echo --------------------
echo 1.Add Sublime Text to the system menu.
echo 2.Uninstall Sublime Text system menu.
echo 3.Exit
echo.
echo Sublime Text Tools Expain
echo -------------------------
echo 1.Please copy this script to the Sublime Text folder.
echo 2.Ensure that the Sublime Text executable file named sublime_text.exe.(The default installation name)
echo 3.Please extend will need to bind name saved to the SublimeText.txt file and directory.
echo 4.Please put Sublime Text in the right position, not the location of the mobile Sublime Text to run this script. (such as the emergence of the associated error, run this script can)
echo.
:first
set /p v=Input number and press enter:
if "%v%" == "" goto first
if "%v%" == "1" goto regmenu
if "%v%" == "2" goto unregmenu
if "%v%" == "3" goto exit
:regmenu
reg add "HKCR\*\shell\Sublime Text" /ve /d "Open With Sublime Text" /f
reg add "HKCR\*\shell\Sublime Text\command" /ve /d "%cd%\sublime_text.exe ""%%1"" /f
reg add "HKCR\SublimeText" /ve /d "文本文档" /f
reg add "HKCR\SublimeText\DefaultIcon" /ve /d "%cd%\sublime_text.exe" /f
reg add "HKCR\SublimeText\shell\open\command" /ve /d "%cd%\sublime_text.exe ""%%1"" /f
For /F "eol=;" %%e in (SublimeText.txt) Do (
        Rem echo %%e
        (for /f "skip=2 tokens=1,2,* delims= " %%a in ('reg query "HKCR\.%%e" /ve') do (
            If NOT "%%c" == "SublimeText" (
                reg add "HKCR\.%%e" /v "SublimeText" /d "%%c" /f
            )
        ))
        assoc .%%e=SublimeText
    )
echo.
echo Registration successful,Press any key to exit.
pause>nul
exit
 
:unregmenu
reg delete "HKCR\*\shell\Sublime Text" /f
reg delete "HKCR\SublimeText" /f
For /F "eol=;" %%e in (SublimeText.txt) Do (
        Rem echo %%e
        (for /f "skip=2 tokens=1,2,* delims= " %%a in ('reg query "HKCR\.%%e" /v "SublimeText"') do (
            reg add "HKCR\.%%e" /ve /d "%%c" /f
            reg delete "HKCR\.%%e" /V "SublimeText" /f
        ))
    )
echo.
echo Uninstall success,Press any key to exit.
pause>nul
exit
:exit
exit