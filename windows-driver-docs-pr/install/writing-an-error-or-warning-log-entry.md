---
title: Writing an Error or Warning Log Entry
description: Writing an Error or Warning Log Entry
ms.assetid: 80393368-7430-46ca-a53e-c94b7e8acfa0
---

# Writing an Error or Warning Log Entry


The following example shows how an application might typically call [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to write an error or warning entry in a [SetupAPI text log](setupapi-text-logs.md). However, if an event is associated with a SetupAPI-specific error or a Win32 error, an application can call [**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232) instead. **SetupWriteTextLogError** facilitates logging and interpreting information about these types of errors.

For information about calling **SetupWriteTextLog** to log an error message, see [Logging an Error Message](#logging-an-error-message) and for information about calling **SetupWriteTextLog** to log a warning message, see [Logging a Warning Message](#logging-a-warning-message).

### <a href="" id="logging-an-error-message"></a> Logging an Error Message

In this example, the application calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218), supplying the following parameter values:

-   *LogToken* is set to a log token value that either was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or is one of the system-defined log token values that are described in the [Log Tokens](log-tokens.md).

-   *Category* is set to TXTLOG\_VENDOR, which indicates that the log entry is made by a vendor-supplied application. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

-   *Flags* is set to a bitwise OR of TXTLOG\_ERROR and TXTLOG\_TIMESTAMP. In this example, the indentation depth is not changed and the current indentation depth was previously set to five monospace text spaces. For information about how to change the indentation depth, see [Writing Indented Log Entries](writing-indented-log-entries.md). Event levels are described in the [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md) topic.

-   *MessageStr* is set to TEXT("Application Error (%d)").

-   The comma-separated list supplies the variable ErrorCode.

The following code calls [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) to write a log entry for this example:

```
//The LogToken value was previously returned by call to
//SetupGetThreadLogToken or one of the system-defined log token values
DWORD Category = TXTLOG_VENDOR; 
DWORD Flags = TXTLOG_ERROR | TXTLOG_TIMESTAMP;
DWORD ErrorCode = 1111; // An error code value

SetupWriteTextLog(LogToken, Category, Flags, TEXT("Application Error (%d)"),ErrorCode);
```

If the TXTLOG\_VENDOR event category is enabled and the TXTLOG\_ERROR event level is set for the text log, this code would create an entry in the text log that would be formatted as follows:

```
!!!  2005/02/13 22:06:28.109:    :  Application error (1111) 
```

The *entry\_prefix* field "!!! " indicates that the log entry is an error message.

### <a href="" id="logging-a-warning-message"></a> Logging a Warning Message

Logging a warning message is almost identical to logging an error message. The difference is the settings for the event level. Set *Flags* to TXTLOG\_WARNING instead of TXTLOG\_ERROR. If **SetupWriteTextLog** is called as described in [Logging an Error Message](#logging-an-error-message), except that *Flags* is set to a bitwise OR of TXTLOG\_WARNING and TXTLOG\_TIMESTAMP, [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) would write the following log entry:

```
!  2005/02/13 22:06:28.109:    :  Application error (1111) 
```

The *entry\_prefix* field of the log entry is "! ", which indicates that this is a warning message, as opposed to "!!! ", which would indicate an error message.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Writing%20an%20Error%20or%20Warning%20Log%20Entry%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




