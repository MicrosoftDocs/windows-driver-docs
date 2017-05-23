---
title: Debugging with Visual SourceSafe
description: Debugging with Visual SourceSafe
ms.assetid: 65cc4eda-7aed-489f-a622-27a42afc0e4a
keywords: ["Visual SourceSafe, debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging with Visual SourceSafe


In order for source files indexed using Visual SourceSafe to work properly with the debugger, you must configure your system properly.

If the Visual SourceSafe database requires a user and optional password for access, these values must be set using the SSUSER and SSPWD environment variables. Furthermore, the version of SrcSrv that ships with Visual Studio 2005 cannot detect whether Visual SourceSafe is prompting for credentials, which causes the application to stop responding.. Upgrade to the version of SrcSrv that ships with Debugging Tools for Windows to prevent this.

If Visual SourceSafe is not set in the path of your debugging computer, you can get around this by adding an entry to the [Srcsrv.ini](the-srcsrv-ini-file.md) file that works with your debugger. When using a standard installation of Visual Studio, this file should be located in

```
%PROGRAMFILES%\Microsoft Visual Studio 8\Common7\IDE\srcsrv.ini
```

In the \[trusted commands\] section of Srcsrv.ini, add an entry of the form

```
ss.exe="Path"
```

where *Path* is the location of Ss.exe.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20with%20Visual%20SourceSafe%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




