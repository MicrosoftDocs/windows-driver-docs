---
title: SetupAPI Logging
description: SetupAPI Logging
ms.assetid: 25beff4d-742a-4d46-bb91-16b3e14f2d6c
keywords: ["SetupAPI WDK , logging", "logging WDK SetupAPI", "SetupAPI logging WDK Windows Vista", "SetupAPI logging WDK Windows Vista , about SetupAPI logging"]
---

# SetupAPI Logging


In Windows Vista and later versions of Windows, [SetupAPI](setupapi.md) includes the following logging components:

-   The Plug and Play (PnP) manager and SetupAPI log information about installation events in the device installation text log (*SetupAPI.dev.log*) and the application installation text log (*SetupAPI.app.log*). The device installation text log contains information about device and driver installations and the application installation text log contains information about application software installations that are associated with device driver installations. For more information about the content of SetupAPI text logs, see [SetupAPI Text Logs](setupapi-text-logs.md), and for information about how to enable logging, see [SetupAPI Logging Registry Settings](setupapi-logging-registry-settings.md).

-   The [SetupAPI logging functions](https://msdn.microsoft.com/library/windows/hardware/ff550878), which PnP device installation applications, class installers, and co-installers can use to write log entries to the SetupAPI text logs. For information about how to use these functions, see [Using the SetupAPI Logging Functions](using-the-setupapi-logging-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20SetupAPI%20Logging%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




