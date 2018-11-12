---
title: Debugging with Visual SourceSafe
description: Debugging with Visual SourceSafe
ms.assetid: 65cc4eda-7aed-489f-a622-27a42afc0e4a
keywords: ["Visual SourceSafe, debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging with Visual SourceSafe


In order for source files indexed using Visual SourceSafe to work properly with the debugger, you must configure your system properly.

If the Visual SourceSafe database requires a user and optional password for access, these values must be set using the SSUSER and SSPWD environment variables. Furthermore, the version of SrcSrv that ships with Visual Studio 2005 cannot detect whether Visual SourceSafe is prompting for credentials, which causes the application to stop responding.. Upgrade to the version of SrcSrv that ships with Debugging Tools for Windows to prevent this.

If Visual SourceSafe is not set in the path of your debugging computer, you can get around this by adding an entry to the [Srcsrv.ini](the-srcsrv-ini-file.md) file that works with your debugger. When using a standard installation of Visual Studio, this file should be located in

```text
%PROGRAMFILES%\Microsoft Visual Studio 8\Common7\IDE\srcsrv.ini
```

In the \[trusted commands\] section of Srcsrv.ini, add an entry of the form

```ini
ss.exe="Path"
```

where *Path* is the location of Ss.exe.

 

 





