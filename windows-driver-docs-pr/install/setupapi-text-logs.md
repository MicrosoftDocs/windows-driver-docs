---
title: SetupAPI Text Logs
description: SetupAPI Text Logs
ms.assetid: db2460f3-b716-4687-9b07-2047f74332d8
keywords: ["text logs WDK SetupAPI", "device installation text logs WDK", "application installation text logs WDK", "log entries WDK SetupAPI", "text log headers WDK SetupAPI", "text log sections WDK SetupAPI", "SetupAPI logging WDK Windows Vista , text logs", "text logs WDK SetupAPI , about text logs"]
---

# SetupAPI Text Logs


In Windows Vista and later versions of Windows, [SetupAPI](setupapi.md) supports a device installation text log (*SetupAPI.dev.log*) and an application installation text log (*SetupAPI.app.log*). The Plug and Play (PnP) manager and SetupAPI write entries to the device installation text log to provide information about operations that install devices and drivers. The PnP manager and SetupAPI write entries to the application installation text log that provide information about installation operations other than those that pertain specifically to device and driver installations.

Installation applications, class installers, and co-installers can use the [SetupAPI logging functions](using-the-setupapi-logging-functions.md) to write entries to the device installation log and the application installation text log.

The SetupAPI text logs are ANSI plain text files, which are located by default in the *%SystemRoot%\\inf* directory. The text logs are in the English (Standard) language.

The SetupAPI text logs have the following internal format:

-   A *log entry* is one line in a text log.

-   The first few log entries provide a *text log header* that contains information about the operating system and computer architecture. For more information, see [Format of a Text Log Header](format-of-a-text-log-header.md).

-   Following the text log header are zero or more *text log sections*. Each text log section records the events during a single device installation.

    The purpose of a text log section is to group and format a contiguous sequence of log entries that provide information about a particular installation operation. By creating text log sections, the PnP manager, SetupAPI, or a custom installation application can organize log entries in a conceptually meaningful way. For example, the PnP manager might create a text log section to group all log entries that apply to installing a device. Text log sections appear in a text log in the order in which they are created. For more information, see [Format of a Text Log Section](format-of-a-text-log-section.md).

-   A text log can contain log entries that are not part of the text log header or a text log section. Such entries are associated with operations that are not part of any particular text log section and, in general, are interspersed between text log sections. Log entries that are not part of a text log section appear in the log in the same order in which they are written to the text log. For more information about such log entries, see [Format of Log Entries That Are Not Part of a Text Log Section](format-of-log-entries-that-are-not-part-of-a-text-log-section.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20SetupAPI%20Text%20Logs%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




