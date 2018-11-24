---
title: Using the SetupAPI Logging Functions
description: Using the SetupAPI Logging Functions
ms.assetid: a2ba0da4-b891-4ff9-827b-0d64a7a02c0d
keywords:
- SetupAPI logging WDK Windows Vista , functions
- functions WDK SetupAPI
- text logs WDK SetupAPI , functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the SetupAPI Logging Functions


SetupAPI supports functions that installation applications, class installers, and co-installers can use to write log entries in the SetupAPI text logs, as follows:

-   To write log entries in a [SetupAPI text log](setupapi-text-logs.md), an installation application calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218), [**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232), or [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236). For more information about how to write text log entries, see [Writing Log Entries in a Text Log](writing-log-entries-in-a-text-log.md).

-   SetupAPI supports a mechanism to establish a log context for a thread. A log context is established for a thread by setting a log token for the thread. To set a log token for a thread, an installation application calls [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216). To retrieve a log token for a thread, an installation application calls [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211).

    For more information about log tokens, see [Log Tokens](log-tokens.md).

    For more information about how to use log tokens, see [Setting and Getting a Log Token for a Thread](setting-and-getting-a-log-token-for-a-thread.md).

 

 





