---
title: Writing an Error or Warning Log Entry
description: Writing an Error or Warning Log Entry
ms.assetid: 80393368-7430-46ca-a53e-c94b7e8acfa0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing an Error or Warning Log Entry


The following example shows how an application might typically call [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to write an error or warning entry in a [SetupAPI text log](setupapi-text-logs.md). However, if an event is associated with a SetupAPI-specific error or a Win32 error, an application can call [**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232) instead. **SetupWriteTextLogError** facilitates logging and interpreting information about these types of errors.

For information about calling **SetupWriteTextLog** to log an error message, see [Logging an Error Message](#logging-an-error-message) and for information about calling **SetupWriteTextLog** to log a warning message, see [Logging a Warning Message](#logging-a-warning-message).

### <a href="" id="logging-an-error-message"></a> Logging an Error Message

In this example, the application calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218), supplying the following parameter values:

-   *LogToken* is set to a log token value that either was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or is one of the system-defined log token values that are described in the [Log Tokens](log-tokens.md).

-   *Category* is set to TXTLOG_VENDOR, which indicates that the log entry is made by a vendor-supplied application. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

-   *Flags* is set to a bitwise OR of TXTLOG_ERROR and TXTLOG_TIMESTAMP. In this example, the indentation depth is not changed and the current indentation depth was previously set to five monospace text spaces. For information about how to change the indentation depth, see [Writing Indented Log Entries](writing-indented-log-entries.md). Event levels are described in the [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md) topic.

-   *MessageStr* is set to TEXT("Application Error (%d)").

-   The comma-separated list supplies the variable ErrorCode.

The following code calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to write a log entry for this example:

```cpp
//The LogToken value was previously returned by call to
//SetupGetThreadLogToken or one of the system-defined log token values
DWORD Category = TXTLOG_VENDOR; 
DWORD Flags = TXTLOG_ERROR | TXTLOG_TIMESTAMP;
DWORD ErrorCode = 1111; // An error code value

SetupWriteTextLog(LogToken, Category, Flags, TEXT("Application Error (%d)"),ErrorCode);
```

If the TXTLOG_VENDOR event category is enabled and the TXTLOG_ERROR event level is set for the text log, this code would create an entry in the text log that would be formatted as follows:

```cpp
!!!  2005/02/13 22:06:28.109:    :  Application error (1111) 
```

The *entry_prefix* field "!!! " indicates that the log entry is an error message.

### <a href="" id="logging-a-warning-message"></a> Logging a Warning Message

Logging a warning message is almost identical to logging an error message. The difference is the settings for the event level. Set *Flags* to TXTLOG_WARNING instead of TXTLOG_ERROR. If **SetupWriteTextLog** is called as described in [Logging an Error Message](#logging-an-error-message), except that *Flags* is set to a bitwise OR of TXTLOG_WARNING and TXTLOG_TIMESTAMP, [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) would write the following log entry:

```cpp
!  2005/02/13 22:06:28.109:    :  Application error (1111) 
```

The *entry_prefix* field of the log entry is "! ", which indicates that this is a warning message, as opposed to "!!! ", which would indicate an error message.

 

 





