---
title: Writing Log Entries in a Text Log
description: Writing Log Entries in a Text Log
ms.assetid: e969f8dd-ad19-42d5-8218-3df0633cc304
keywords:
- text logs WDK SetupAPI , writing entries
- sections WDK SetupAPI logging
- text logs WDK SetupAPI , sections
- writing text log entries
- SetupAPI logging WDK Windows Vista , text log sections
- SetupAPI logging WDK Windows Vista , writing text log entries
- SetupWriteTextLog
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing Log Entries in a Text Log


An application performs one of the following to write a log entry in a [SetupAPI text log](setupapi-text-logs.md):

-   [Calls SetupWriteTextLog](calling-setupwritetextlog.md) to write a single text log entry that contains information about an installation event.

-   [Calls SetupWriteTextLogError](calling-setupwritetextlogerror.md) to write information about a SetupAPI-specific error or a Win32 error to a text log. **SetupWriteTextLogError** writes two consecutive entries to a text log: the first entry contains the same information in the same format as that written by **SetupWriteTextLog** and the second entry logs a corresponding error code and a user-friendly description of the error.

-   [Calls SetupWriteTextLogInfLine](calling-setupwritetextloginfline.md) to write a single text log entry that contains the text of a specified INF file line.

As described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md), the SetupAPI logging functions write entries in the following format:

```cpp
entry_prefix time_stamp event_category indentation formatted_message
```

The main difference between the entries that the various SetupAPI logging functions write to a text log is in the specific information content and in the format of the *formatted-message* field.

For information about how to set the *indentation* field to indent the *formatted-message* field, see [Writing Indented Log Entries](writing-indented-log-entries.md).

 

 





