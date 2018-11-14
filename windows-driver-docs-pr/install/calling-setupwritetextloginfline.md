---
title: Calling SetupWriteTextLogInfLine
description: Calling SetupWriteTextLogInfLine
ms.assetid: 7b7a08bf-b97a-4dfe-8695-dc947481ad2b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling SetupWriteTextLogInfLine


An application can call [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236) to write a log entry in a [SetupAPI text log](setupapi-text-logs.md) that contains the text of a specified INF file line.

To call **SetupWriteTextLogInfLine**, an application supplies the following information:

-   The log token for a section in a text log that was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or one of the system-defined [log tokens](log-tokens.md). If the log token is associated with a text log section, **SetupWriteTextLogInfLine** writes the log entry in that section. Otherwise, **SetupWriteTextLogInfLine** adds the log entry to a part of the log that is not included in a text log section.

    In addition, whether **SetupWriteTextLogInfLine** writes a log entry, and to which text log **SetupWriteTextLogInfLine** writes the entry, depends on the system-defined log token value.

    For more information about log tokens, see [Setting and Getting a Log Token for a Thread](setting-and-getting-a-log-token-for-a-thread.md).

-   A flag value that is a bitwise OR of system-defined constants that specify the event level, the indentation depth, and whether to include a time stamp. Event levels are described in [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md).

    If the event level set for the text log is greater than or equal to the event level for the entry, [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236) writes a log entry in the text log. Otherwise, **SetupWriteTextLogInfLine** does not write a log entry in the text log. By using indentation, formatted messages can be arranged to make the information in a section easier to read and understand.

    For more information, see [Writing Indented Log Entries](writing-indented-log-entries.md).

-   A handle to the INF file that contains the INF file line.

-   The context for the INF file line.

**SetupWriteTextLogInfLine** writes a log entry in the following format:

*entry_prefix time_stamp* **inf:**<em>indentation inf-line-text</em> **(**<em>inf-file-name</em> **line** <em>line-number</em>**)**

Where:

-   The *entry_prefix*, *time-stamp*, and *indentation* fields are the same as those that are described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md).

-   The **inf:** field specifies the TXTLOG_INF event category. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

-   The *inf-line-text* field contains the text of the specified INF file line.

-   The *inf-file-name* field contains the name of the INF file that contains the specified INF file line.

-   The **line** field indicates that what follows is a line number in the INF file.

-   The *line-number* field contains the line number of the specified line in the INF file.

The following example shows how an application might typically log the text of an INF line in a text log. The INF line in this example is an INF **AddReg** line. The application calls [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236), supplying the following input parameter values:

-   *LogToken* is set to a log token that was returned by [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or to a system-defined [log token](log-tokens.md).

-   *LogFlags* is set to TXTLOG_DETAILS. This example does not include a time stamp or change the indentation depth. In the example, the indentation depth is five monospace text spaces.

-   *InfHandle* is set to a handle to the INF file *hidserv.inf.* This handle is obtained by calling the **SetupOpenInfFile** function, which is documented in the Platform SDK.

-   *Context* is set to the INF file context of the INF file line that contains the text "AddReg=HidServ_AddService_AddReg." An INF file context for the line is obtained by calling the **SetupFind*Xxx*Line** functions, which are documented in the Platform SDK.

The values of *LogToken* and *LogFlags* affect the operation of [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236) in the same manner as that described for [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218). In addition, **SetupWriteTextLogInfLine** uses the event catalog TXTLOG_INF.

For this example, the following shows the type of log entry that **SetupWriteTextLogInfLine** would write to a text log:

```cpp
   inf:      AddReg=HidServ_AddService_AddReg  (hidserv.inf line 98)
```

 

 





