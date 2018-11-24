---
title: SetupAPI Logging
description: SetupAPI Logging
ms.assetid: 25beff4d-742a-4d46-bb91-16b3e14f2d6c
keywords:
- SetupAPI WDK , logging
- logging WDK SetupAPI
- SetupAPI logging WDK Windows Vista
- SetupAPI logging WDK Windows Vista , about SetupAPI logging
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SetupAPI Logging


In Windows Vista and later versions of Windows, [SetupAPI](setupapi.md) includes the following logging components:

-   The Plug and Play (PnP) manager and SetupAPI log information about installation events in the device installation text log (*SetupAPI.dev.log*) and the application installation text log (*SetupAPI.app.log*). The device installation text log contains information about device and driver installations and the application installation text log contains information about application software installations that are associated with device driver installations. For more information about the content of SetupAPI text logs, see [SetupAPI Text Logs](setupapi-text-logs.md), and for information about how to enable logging, see [SetupAPI Logging Registry Settings](setupapi-logging-registry-settings.md).

-   The [SetupAPI logging functions](https://msdn.microsoft.com/library/windows/hardware/ff550878), which PnP device installation applications, class installers, and co-installers can use to write log entries to the SetupAPI text logs. For information about how to use these functions, see [Using the SetupAPI Logging Functions](using-the-setupapi-logging-functions.md).

 

 





