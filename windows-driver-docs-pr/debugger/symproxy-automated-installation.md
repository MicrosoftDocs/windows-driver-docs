---
title: SymProxy Automated Installation
description: These steps along with the Install.cmd script below can help automate the installation of SymProxy to a default IIS installation. 
ms.assetid: 9E5433D8-D024-4E2B-AEAA-2271C133FD0E
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SymProxy Automated Installation


These steps along with the Install.cmd script below can help automate the installation of SymProxy to a default IIS installation. You will likely need to adapt these steps to the specific needs of your environment.

1. Create D:\\SymStore\\Symbols folder.

   - Grant Read to Everyone

   - Grant Read\\Write to the SymProxy App Pool user account (Domain\\User)

2. Share D:\\SymStore\\Symbols as Symbols.

   - Grant Read to Everyone (or be more specific)

3. (Optionally) Create an empty file called index2.txt in D:\\SymStore\\Symbols.
4. (Optionally) Create an empty file called %WINDIR%\\system32\\inetsrv\\symsrv.yes. This accepts the EULA for the Microsoft Public Symbol Store.
5. Determine the parameters for Install.cmd and run it.
6. Configure the clients symbol path using the server name that you created.
   ```dbgcmd
   SRV*\\MachineName\Symbols*https://MachineName/Symbols
   ```

The Install.cmd script requires 3 parameters:

-   Virtual Directory path (e.g. D:\\SymStore\\Symbols )
-   Username (for the Application Pool)
-   Password (for the Application Pool)

To clear the MIME Type inheritance, an XML file is needed to drive the associated AppCmd.exe command. Place the staticContentClear.xml file shown below in the same folder as the Install.cmd script to achieve this result.

Example Install.Cmd parameter usage:

```console
Install.cmd D:\SymStore\Symbols CONTOSO\SymProxyService Pa$$word
```

## <span id="install.cmd"></span><span id="INSTALL.CMD"></span>Install.cmd


```bat
@echo off

SET VirDirectory=%1
SET UserName=%2
SET Password=%3

::
::  SymProxy dll installation. 
::

copy symproxy.dll %windir%\system32\inetsrv
copy symproxy.man %windir%\system32\inetsrv
copy symsrv.dll %windir%\system32\inetsrv

lodctr.exe /m:%windir%\system32\inetsrv\symproxy.man
wevtutil.exe install-manifest %windir%\System32\inetsrv\symproxy.man
regedit.exe /s symproxy.reg

::
::  Web server Configuraiton
::

IF not exist %VirDirectory% mkdir %VirDirectory%

rem Make the 'Default Web Site'
%windir%\system32\inetsrv\appcmd.exe add site -site.name:"Default Web Site" -bindings:"http/*:80:" -physicalPath:C:\inetpub\wwwroot

rem Enabled Directory Browsing on the 'Default Web Site'
%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -section:system.webServer/directoryBrowse /enabled:"True"

rem Make the 'SymProxy App Pool'
%windir%\system32\inetsrv\appcmd.exe add apppool -apppool.name:SymProxyAppPool -managedRuntimeVersion:
%windir%\system32\inetsrv\appcmd.exe set apppool -apppool.name:SymProxyAppPool -processModel.identityType:SpecificUser -processModel.userName:%UserName% -processModel.password:%Password% 

rem Make the 'Symbols' Virtual Directory and assign the 'SymProxy App Pool'
%windir%\system32\inetsrv\appcmd.exe add app -site.name:"Default Web Site" -path:/Symbols -physicalpath:%VirDirectory%
%windir%\system32\inetsrv\appcmd.exe set app -app.name:"Default Web Site/Symbols" -applicationPool:SymProxyAppPool

rem Disable 'web.config' for folders under virtual directories in the 'Default Web Site'
%windir%\system32\inetsrv\appcmd.exe set config -section:system.applicationHost/sites "/[name='Default Web Site'].virtualDirectoryDefaults.allowSubDirConfig:false

rem Add the 'SymProxy ISAPI Filter'
%windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/isapiFilters /+"[name='SymProxy',path='%windir%\system32\inetsrv\SymProxy.dll',enabled='True']

rem Clear the MIME Types on the 'Default Web Site'
%windir%\system32\inetsrv\appcmd.exe set config -in "Default Web Site" < staticContentClear.xml

rem Add * to the MIME Types of the 'Default Web Site'
%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -section:staticContent /+"[fileExtension='.*',mimeType='application/octet-stream']"
```

## <span id="staticcontentclear.xml"></span><span id="STATICCONTENTCLEAR.XML"></span>staticContentClear.xml


```xml
<?xml version="1.0" encoding="UTF-8"?>
<appcmd>
    <CONFIG CONFIG.SECTION="system.webServer/staticContent"                  path="MACHINE/WEBROOT/APPHOST">
        <system.webServer-staticContent>
            <clear />
        </system.webServer-staticContent>
    </CONFIG>
```

## <span id="Testing_the_SymProxy_Installation_"></span><span id="testing_the_symproxy_installation_"></span><span id="TESTING_THE_SYMPROXY_INSTALLATION_"></span>Testing the SymProxy Installation


The system should now be ready to acquire and serve files. To test it, start by restarting the IISAdmin service by running iisreset.exe. This will reload the ISAPI filter with the current IIS and SymProxy configuration.

Configure a debugger to use this symbol path:

```dbgcmd
srv*\\MachineName\Symbols*https://MachineName/Symbols
```

If *MissTimeout* is enabled (it is set to 300 seconds by default), running the .reload /f command twice should result in much faster execution the second time.

To view the location of the PDBs being referenced, use the lm (list modules) command. The path to the PDBs should all begin with \\\\MachineName\\Symbols.

If directory browsing is enabled on the web site, browse to https://MachineName/Symbols to see the files that are cached.

Open the Performance Monitor and view the Symbol Proxy counters.

Open the Event Viewer and view the Microsoft\\Windows\\SymProxy events.

## <span id="related_topics"></span>Related topics


[Installing SymProxy](installing-symproxy.md)

 

 






