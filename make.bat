@echo off

setlocal enabledelayedexpansion

set "build_all="
set /a build_count=1
set build_lang=%1
set build_max=2
set build_next=""

set english_lang=en
set portuguese_lang=pt

if not defined build_lang (
    set "build_all=true"
    set build_next=%english_lang%
    goto pre-build
)

if %build_lang% == %english_lang% (
    set build_next=%english_lang%
    goto pre-build
)

if %build_lang% == %portuguese_lang% (
    set build_next=%portuguese_lang%
    goto pre-build
) else (
    echo Invalid language parameter!
    echo:
    goto :common-exit
)

:pre-build
echo Starting build of %build_next% version...
echo:
pushd %~dp0\src\%build_next%
goto :build


:build
echo Cleaning previous build...
echo:

ablog clean

echo:
echo Clean finished.
echo:

echo Build started...
echo:

ablog build

echo:
echo Build finished.
echo:

popd

if defined build_all (
    if !build_count! == %build_max% (
        echo All the available builds finished.
        echo:
        goto :common-exit 
    )

    set /a "build_count=!build_count!+1"

    echo Going to the build number !build_count!
    echo:

    if !build_count! == 2 (
        set build_next=%portuguese_lang%
        goto pre-build
    )
) else (
    goto common-exit
)

:common-exit
echo:
echo Exiting...

exit
