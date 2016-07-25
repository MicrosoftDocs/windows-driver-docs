---
title: Calling SetupWriteTextLogInfLine
description: Calling SetupWriteTextLogInfLine
ms.assetid: 7b7a08bf-b97a-4dfe-8695-dc947481ad2b
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

*entry\_prefix time\_stamp* **inf:***indentation inf-line-text* **(***inf-file-name* **line** *line-number***)**

Where:

-   The *entry\_prefix*, *time-stamp*, and *indentation* fields are the same as those that are described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md).

-   The **inf:** field specifies the TXTLOG\_INF event category. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

-   The *inf-line-text* field contains the text of the specified INF file line.

-   The *inf-file-name* field contains the name of the INF file that contains the specified INF file line.

-   The **line** field indicates that what follows is a line number in the INF file.

-   The *line-number* field contains the line number of the specified line in the INF file.

The following example shows how an application might typically log the text of an INF line in a text log. The INF line in this example is an INF **AddReg** line. The application calls [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236), supplying the following input parameter values:

-   *LogToken* is set to a log token that was returned by [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or to a system-defined [log token](log-tokens.md).

-   *LogFlags* is set to TXTLOG\_DETAILS. This example does not include a time stamp or change the indentation depth. In the example, the indentation depth is five monospace text spaces.

-   *InfHandle* is set to a handle to the INF file *hidserv.inf.* This handle is obtained by calling the **SetupOpenInfFile** function, which is documented in the Platform SDK.

-   *Context* is set to the INF file context of the INF file line that contains the text "AddReg=HidServ\_AddService\_AddReg." An INF file context for the line is obtained by calling the **SetupFind*Xxx*Line** functions, which are documented in the Platform SDK.

The values of *LogToken* and *LogFlags* affect the operation of [**SetupWriteTextLogInfLine**](https://msdn.microsoft.com/library/windows/hardware/ff552236) in the same manner as that described for [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218). In addition, **SetupWriteTextLogInfLine** uses the event catalog TXTLOG\_INF.

For this example, the following shows the type of log entry that **SetupWriteTextLogInfLine** would write to a text log:

```
   inf:      AddReg=HidServ_AddService_AddReg  (hidserv.inf line 98)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Calling%20SetupWriteTextLogInfLine%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




