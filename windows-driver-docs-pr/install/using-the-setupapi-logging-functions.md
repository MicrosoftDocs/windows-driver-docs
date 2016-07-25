---
title: Using the SetupAPI Logging Functions
description: Using the SetupAPI Logging Functions
ms.assetid: a2ba0da4-b891-4ff9-827b-0d64a7a02c0d
keywords: ["SetupAPI logging WDK Windows Vista , functions", "functions WDK SetupAPI", "text logs WDK SetupAPI , functions"]
---

# Using the SetupAPI Logging Functions


SetupAPI supports functions that installation applications, class installers, and co-installers can use to write log entries in the SetupAPI text logs, as follows:

-   To write log entries in a [SetupAPI text log](setupapi-text-logs.md), an installation application calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218), [**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232), or [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236). For more information about how to write text log entries, see [Writing Log Entries in a Text Log](writing-log-entries-in-a-text-log.md).

-   SetupAPI supports a mechanism to establish a log context for a thread. A log context is established for a thread by setting a log token for the thread. To set a log token for a thread, an installation application calls [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216). To retrieve a log token for a thread, an installation application calls [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211).

    For more information about log tokens, see [Log Tokens](log-tokens.md).

    For more information about how to use log tokens, see [Setting and Getting a Log Token for a Thread](setting-and-getting-a-log-token-for-a-thread.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20the%20SetupAPI%20Logging%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




