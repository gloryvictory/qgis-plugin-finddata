@echo off
SET OSGEO4W_ROOT=D:\OSGeo4W64

call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
call "%OSGEO4W_ROOT%\bin\qt5_env.bat"
call "%OSGEO4W_ROOT%\bin\py3_env.bat"

@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass79\lib
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin\
path %PATH%;%OSGEO4W_ROOT%\apps\Python37\Scripts\
path %PATH%;%OSGEO4W_ROOT%\apps\qgis-dev\python\qgis\PyQt\
path %PATH%;c:\python38\lib\site-packages
path %PATH%;C:\Apps\Git\bin\

set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis

set GDAL_FILENAME_IS_UTF8=YES

set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins

SET PYCHARM="C:\Program Files\JetBrains\PyCharm Community Edition 2020.3.2\bin\pycharm64.exe"


rem set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python
rem set PYTHONHOME=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python37

set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python
set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37
set PYTHONPATH=%OSGEO4W_ROOT%\apps\Python37\lib\site-packages;%PYTHONPATH%

set QT_QPA_PLATFORM_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis

CD C:\Glory\Projects\Python\gloryvictory\qgis-plugin-finddata\

cmd.exe


rem start "PyCharm aware of QGIS" /B %PYCHARM% %*




