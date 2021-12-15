---
title: Using the SetupAPI Logging Functions
description: Using the SetupAPI Logging Functions
keywords:
- SetupAPI logging WDK Windows Vista , functions
- functions WDK SetupAPI
- text logs WDK SetupAPI , functions
ms.date: 04/20/2017
---

# Using the SetupAPI Logging Functions


SetupAPI supports functions that installation applications, class installers, and co-installers can use to write log entries in the SetupAPI text logs, as follows:

-   To write log entries in a [SetupAPI text log](setupapi-text-logs.md), an installation application calls [**SetupWriteTextLog**](/windows/win32/api/setupapi/nf-setupapi-setupwritetextlog), [**SetupWriteTextLogError**](/windows/win32/api/setupapi/nf-setupapi-setupwritetextlogerror), or [**SetupWriteTextLogInfLine**](/windows/win32/api/setupapi/nf-setupapi-setupwritetextloginfline). For more information about how to write text log entries, see [Writing Log Entries in a Text Log](writing-log-entries-in-a-text-log.md).

-   SetupAPI supports a mechanism to establish a log context for a thread. A log context is established for a thread by setting a log token for the thread. To set a log token for a thread, an installation application calls [**SetupSetThreadLogToken**](/windows/win32/api/setupapi/nf-setupapi-setupsetthreadlogtoken). To retrieve a log token for a thread, an installation application calls [**SetupGetThreadLogToken**](/windows/win32/api/setupapi/nf-setupapi-setupgetthreadlogtoken).

    For more information about log tokens, see [Log Tokens](log-tokens.md).

    For more information about how to use log tokens, see [Setting and Getting a Log Token for a Thread](setting-and-getting-a-log-token-for-a-thread.md).

 

