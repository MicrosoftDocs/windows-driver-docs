---
title: Calling SetupWriteTextLog
description: Calling SetupWriteTextLog
ms.assetid: a07118ae-bef6-4d01-94d9-98587cbff863
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling SetupWriteTextLog


[**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) adds a single entry with information about an installation event to a [SetupAPI text log](setupapi-text-logs.md).

As described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md), the format of a log entry consists of the following fields:

```cpp
entry_prefix time_stamp event_category indentation formatted_message
```

To call **SetupWriteTextLog**, an application supplies following information:

-   The log token for a section in a text log that was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211), or one of the system-defined [log tokens](log-tokens.md). If the log token is associated with a text log section, **SetupWriteTextLog** writes the log entry in that section. Otherwise, **SetupWriteTextLog** adds the log entry to a part of the log that is not included in a text log section. In addition, whether **SetupWriteTextLog** writes a log entry, and to which text log **SetupWriteTextLog** writes the entry, depends on the system-defined log token value.

    For more information about log tokens, see [Setting and Getting a Log Token for a Thread](setting-and-getting-a-log-token-for-a-thread.md).

-   One of the event categories that are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md). If the event category for the entry is enabled for the text log, [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) adds the entry to the text log; otherwise, **SetupWriteTextLog** does not write the entry to the text log.

-   A flag value that is a bitwise OR of system-defined constants that specify the event level, the indentation depth, and whether to include a time stamp. Event levels are described in [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md). If the event level set for the text log is greater than or equal to the event level for the entry, **SetupWriteTextLog** writes a log entry to the text log; otherwise, **SetupWriteTextLog** does not write a log entry to the text log. By using indentation, formatted messages can be arranged to make the information in a section easier to read and understand. For more information, see [Writing Indented Log Entries](writing-indented-log-entries.md).

-   A **printf**-compatible format string that formats both the message and the list of comma-separated variables that follows the format string.

-   A comma-separated list of variables, whose values are formatted by the **printf**-compatible format string.

For an example on how to call [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to log information about an event that is not an error or a warning, see [Writing an Information Log Entry](writing-an-information-log-entry.md).

For an example on how to call **SetupWriteTextLog** to log information about an error or a warning, see [Writing an Error or Warning Log Entry](writing-an-error-or-warning-log-entry.md).

 

 





