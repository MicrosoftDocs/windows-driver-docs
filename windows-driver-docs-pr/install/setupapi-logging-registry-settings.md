---
title: SetupAPI Logging Registry Settings
description: SetupAPI Logging Registry Settings
ms.assetid: 24694bce-5941-479f-9e2d-f9c7577a4f6a
keywords: ["SetupAPI logging WDK Windows Vista , registry settings", "registry WDK SetupAPI logging", "event levels WDK SetupAPI logging", "event categories WDK SetupAPI logging", "text logs WDK SetupAPI , registry entries"]
---

# SetupAPI Logging Registry Settings


[SetupAPI](setupapi.md) logging supports a global *event level* and a global *event category* that control whether information is written to a text log. The event level controls the level of detail that is written to a text log and the event category determines the type of operations that can make log entries. If a log entry has an event level numerically less than or equal to the global event level of a text log, and if the event category of the log entry is enabled for the text log, the log entry is written to the text log; otherwise, the log entry is not written to the text log.

For information about how to set the event level, see [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md).

For information about how to set the event categories that are enabled for a log, see [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

By default, the SetupAPI text logs are located in the %*SystemRoot*%*\\Inf* directory. For information about how to change the directory where the text logs are located, see [Setting the Directory Path of the Text Logs](setting-the-directory-path-of-the-text-logs.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20SetupAPI%20Logging%20Registry%20Settings%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




