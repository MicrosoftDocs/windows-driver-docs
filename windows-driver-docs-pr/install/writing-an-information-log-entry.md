---
title: Writing an Information Log Entry
description: Writing an Information Log Entry
ms.assetid: 624d2a3e-2a11-47fd-941e-1ab59e299821
---

# Writing an Information Log Entry


The following example shows how an application might typically call [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to write an information entry in a [SetupAPI text log](setupapi-text-logs.md) that is not a warning message or an error message.

For information about calling **SetupWriteTextLog** to log an error message, see [Calling SetupWriteTextLog to Log an Error or Warning Entry](writing-an-error-or-warning-log-entry.md).

The application calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218), supplying the following parameter values:

-   *LogToken* is set to a log token value that either was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or is one of the system-defined log token values that are described in the [Log Tokens](log-tokens.md).

-   *Category* is set to TXTLOG\_VENDOR, which indicates that the log entry is made by a vendor-supplied application. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

-   *Flags* is set to a bitwise OR of TXTLOG\_DETAILS and TXTLOG\_TIMESTAMP. In this example, the indentation depth is not changed and the current indentation depth was previously set to five monospace text spaces. For information about how to change the indentation depth, see [Writing Indented Log Entries](writing-indented-log-entries.md). Event levels are described in the [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md) topic.

-   *MessageStr* is set to TEXT("Variable of interest: = %d").

-   The comma-separated parameter list supplies the variable *SomeVariable*, which corresponds to "%d" field in *MessageStr*.

```
//The LogToken value was previously returned by call to
//SetupGetThreadLogToken or one of the system-defined log token values
DWORD Category = TXTLOG_VENDOR; 
DWORD Flags = TXTLOG_DETAILS | TXTLOG_TIMESTAMP;
DWORD SomeVariable = 1;   // The variable whose value will be logged

SetupWriteTextLog(LogToken, Category, Flags, TEXT("Variable of interest: = %d"), SomeVariable);
```

If the TXTLOG\_VENDOR event category is enabled and the TXTLOG\_DETAILS event level is set for the device installation text log, this code would create an entry in the device installation log in the following format, where the time stamp would be replaced by an actual time stamp.

```
     2005/02/13 22:06:28.109:    :  Variable of interest: Abc = 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Writing%20an%20Information%20Log%20Entry%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




