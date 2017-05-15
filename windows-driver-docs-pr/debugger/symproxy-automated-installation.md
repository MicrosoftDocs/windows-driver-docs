---
title: SymProxy Automated Installation
description: These steps along with the Install.cmd script below can help automate the installation of SymProxy to a default IIS installation. You will likely need to adapt these steps to the specific needs of your environment.
ms.assetid: 9E5433D8-D024-4E2B-AEAA-2271C133FD0E
---

# SymProxy Automated Installation


These steps along with the Install.cmd script below can help automate the installation of SymProxy to a default IIS installation. You will likely need to adapt these steps to the specific needs of your environment.

1.  Create D:\\SymStore\\Symbols folder.

    - Grant Read to Everyone

    - Grant Read\\Write to the SymProxy App Pool user account (Domain\\User)

2.  Share D:\\SymStore\\Symbols as Symbols.

    - Grant Read to Everyone (or be more specific)

3.  (Optionally) Create an empty file called index2.txt in D:\\SymStore\\Symbols.
4.  (Optionally) Create an empty file called %WINDIR%\\system32\\inetsrv\\symsrv.yes. This accepts the EULA for the Microsoft Public Symbol Store.
5.  Determine the parameters for Install.cmd and run it.
6.  Configure the clients symbol path using the server name that you created.
    ```
    SRV*\\MachineName\Symbols*http://MachineName/Symbols
    ```

The Install.cmd script requires 3 parameters:

-   Virtual Directory path (e.g. D:\\SymStore\\Symbols )
-   Username (for the Application Pool)
-   Password (for the Application Pool)

To clear the MIME Type inheritance, an XML file is needed to drive the associated AppCmd.exe command. Place the staticContentClear.xml file shown below in the same folder as the Install.cmd script to achieve this result.

Example Install.Cmd parameter usage:

```
Install.cmd D:\SymStore\Symbols CONTOSO\SymProxyService Pa$$word
```

## <span id="install.cmd"></span><span id="INSTALL.CMD"></span>Install.cmd


```
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

rem Make the &#39;Default Web Site&#39;
%windir%\system32\inetsrv\appcmd.exe add site -site.name:"Default Web Site" -bindings:"http/*:80:" -physicalPath:C:\inetpub\wwwroot

rem Enabled Directory Browsing on the &#39;Default Web Site&#39;
%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -section:system.webServer/directoryBrowse /enabled:"True"

rem Make the &#39;SymProxy App Pool&#39;
%windir%\system32\inetsrv\appcmd.exe add apppool -apppool.name:SymProxyAppPool -managedRuntimeVersion:
%windir%\system32\inetsrv\appcmd.exe set apppool -apppool.name:SymProxyAppPool -processModel.identityType:SpecificUser -processModel.userName:%UserName% -processModel.password:%Password% 

rem Make the &#39;Symbols&#39; Virtual Directory and assign the &#39;SymProxy App Pool&#39;
%windir%\system32\inetsrv\appcmd.exe add app -site.name:"Default Web Site" -path:/Symbols -physicalpath:%VirDirectory%
%windir%\system32\inetsrv\appcmd.exe set app -app.name:"Default Web Site/Symbols" -applicationPool:SymProxyAppPool

rem Disable &#39;web.config&#39; for folders under virtual directories in the &#39;Default Web Site&#39;
%windir%\system32\inetsrv\appcmd.exe set config -section:system.applicationHost/sites "/[name=&#39;Default Web Site&#39;].virtualDirectoryDefaults.allowSubDirConfig:false

rem Add the &#39;SymProxy ISAPI Filter&#39;
%windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/isapiFilters /+"[name=&#39;SymProxy&#39;,path=&#39;%windir%\system32\inetsrv\SymProxy.dll&#39;,enabled=&#39;True&#39;]

rem Clear the MIME Types on the &#39;Default Web Site&#39;
%windir%\system32\inetsrv\appcmd.exe set config -in "Default Web Site" < staticContentClear.xml

rem Add * to the MIME Types of the &#39;Default Web Site&#39;
%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -section:staticContent /+"[fileExtension=&#39;.*&#39;,mimeType=&#39;application/octet-stream&#39;]"
```

## <span id="staticcontentclear.xml"></span><span id="STATICCONTENTCLEAR.XML"></span>staticContentClear.xml


```
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

```
srv*\\MachineName\Symbols*http://MachineName/Symbols
```

If *MissTimeout* is enabled (it is set to 300 seconds by default), running the .reload /f command twice should result in much faster execution the second time.

To view the location of the PDBs being referenced, use the lm (list modules) command. The path to the PDBs should all begin with \\\\MachineName\\Symbols.

If directory browsing is enabled on the web site, browse to http://MachineName/Symbols to see the files that are cached.

Open the Performance Monitor and view the Symbol Proxy counters.

Open the Event Viewer and view the Microsoft\\Windows\\SymProxy events.

## <span id="related_topics"></span>Related topics


[Installing SymProxy](installing-symproxy.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20SymProxy%20Automated%20Installation%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





