---
title: Writing Log Entries in a Text Log
description: Writing Log Entries in a Text Log
ms.assetid: e969f8dd-ad19-42d5-8218-3df0633cc304
keywords: ["text logs WDK SetupAPI , writing entries", "sections WDK SetupAPI logging", "text logs WDK SetupAPI , sections", "writing text log entries", "SetupAPI logging WDK Windows Vista , text log sections", "SetupAPI logging WDK Windows Vista , writing text log entries", "SetupWriteTextLog"]
---

# Writing Log Entries in a Text Log


An application performs one of the following to write a log entry in a [SetupAPI text log](setupapi-text-logs.md):

-   [Calls SetupWriteTextLog](calling-setupwritetextlog.md) to write a single text log entry that contains information about an installation event.

-   [Calls SetupWriteTextLogError](calling-setupwritetextlogerror.md) to write information about a SetupAPI-specific error or a Win32 error to a text log. **SetupWriteTextLogError** writes two consecutive entries to a text log: the first entry contains the same information in the same format as that written by **SetupWriteTextLog** and the second entry logs a corresponding error code and a user-friendly description of the error.

-   [Calls SetupWriteTextLogInfLine](calling-setupwritetextloginfline.md) to write a single text log entry that contains the text of a specified INF file line.

As described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md), the SetupAPI logging functions write entries in the following format:

```
entry_prefix time_stamp event_category indentation formatted_message
```

The main difference between the entries that the various SetupAPI logging functions write to a text log is in the specific information content and in the format of the *formatted-message* field.

For information about how to set the *indentation* field to indent the *formatted-message* field, see [Writing Indented Log Entries](writing-indented-log-entries.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Writing%20Log%20Entries%20in%20a%20Text%20Log%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




