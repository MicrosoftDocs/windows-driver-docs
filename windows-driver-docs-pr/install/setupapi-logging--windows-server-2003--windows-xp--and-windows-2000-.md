---
title: SetupAPI Logging (Windows Server 2003, Windows XP, Windows 2000)
description: SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)
keywords:
- SetupAPI WDK device installations , logging
- logging WDK SetupAPI
- SetupAPI logging WDK Windows Server 2003
- SetupAPI logging WDK Windows 2000
- SetupAPI logging WDK Windows XP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)





The Windows Setup and Device Installer Services, also known as SetupAPI, include the Windows functions that control Setup and device installation. As Setup proceeds, the [general Setup functions](/previous-versions/ff544985(v=vs.85)) (**Setup***Xxx* functions) and [device installation functions](/previous-versions/ff541299(v=vs.85)) (**SetupDi***Xxx* functions) create a log file that provides useful information for troubleshooting device installation problems.

SetupAPI logs to the file %*systemroot*%\\*setupapi.log*. The log file is a plain text file. To reset the log, rename or delete the file.

This section includes the following information:

[Setting SetupAPI Logging Levels](setting-setupapi-logging-levels.md)

[Interpreting a Sample SetupAPI Log File](interpreting-a-sample-setupapi-log-file.md)

 

