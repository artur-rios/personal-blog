@echo off

set english_lang=en
set portuguese_lang=pt

set serve_lang=%1

if not defined serve_lang (
    echo No language specified, serving english...
    echo:

    set serve_lang=%english_lang%

    goto serve
)

if not "%serve_lang%" == "%english_lang%" (
    if not "%serve_lang%" == "%portuguese_lang%" (
        echo Invalid language parameter!
        echo:
        goto :common-exit
    )
)

:serve
pushd %~dp0\src\%serve_lang%

echo Serving %serve_lang% version on local environment...
echo:

ablog serve -n

popd

goto common-exit

:common-exit
echo:
echo Exiting...

exit
