---
title: Writing an Information Log Entry
description: Writing an Information Log Entry
ms.assetid: 624d2a3e-2a11-47fd-941e-1ab59e299821
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing an Information Log Entry


The following example shows how an application might typically call [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to write an information entry in a [SetupAPI text log](setupapi-text-logs.md) that is not a warning message or an error message.

For information about calling **SetupWriteTextLog** to log an error message, see [Calling SetupWriteTextLog to Log an Error or Warning Entry](writing-an-error-or-warning-log-entry.md).

The application calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218), supplying the following parameter values:

-   *LogToken* is set to a log token value that either was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or is one of the system-defined log token values that are described in the [Log Tokens](log-tokens.md).

-   *Category* is set to TXTLOG_VENDOR, which indicates that the log entry is made by a vendor-supplied application. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

-   *Flags* is set to a bitwise OR of TXTLOG_DETAILS and TXTLOG_TIMESTAMP. In this example, the indentation depth is not changed and the current indentation depth was previously set to five monospace text spaces. For information about how to change the indentation depth, see [Writing Indented Log Entries](writing-indented-log-entries.md). Event levels are described in the [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md) topic.

-   *MessageStr* is set to TEXT("Variable of interest: = %d").

-   The comma-separated parameter list supplies the variable *SomeVariable*, which corresponds to "%d" field in *MessageStr*.

```cpp
//The LogToken value was previously returned by call to
//SetupGetThreadLogToken or one of the system-defined log token values
DWORD Category = TXTLOG_VENDOR; 
DWORD Flags = TXTLOG_DETAILS | TXTLOG_TIMESTAMP;
DWORD SomeVariable = 1;   // The variable whose value will be logged

SetupWriteTextLog(LogToken, Category, Flags, TEXT("Variable of interest: = %d"), SomeVariable);
```

If the TXTLOG_VENDOR event category is enabled and the TXTLOG_DETAILS event level is set for the device installation text log, this code would create an entry in the device installation log in the following format, where the time stamp would be replaced by an actual time stamp.

```cpp
     2005/02/13 22:06:28.109:    :  Variable of interest: Abc = 1
```

 

 





