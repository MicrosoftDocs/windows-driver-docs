---
title: Calling SetupWriteTextLogError
description: Calling SetupWriteTextLogError
ms.assetid: 55edc72a-2d53-4084-a1e4-e7e6515a4990
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling SetupWriteTextLogError


[**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232) writes information about a SetupAPI-specific error or a Win32 error to a [SetupAPI text log](setupapi-text-logs.md). **SetupWriteTextLogError** writes two consecutive entries to a text log: the first entry contains the same information in the same format as that written by [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) and the second entry logs a corresponding error code and a user-friendly description of the error.

To call **SetupWriteTextLogError**, an application supplies the same information that it would supply to call **SetupWriteTextLog** and, in addition, supplies the value of a SetupAPI-specific error or a Win32 error.

**SetupWriteTextLogError** writes the first log entry in the following format:

*entry_prefix time_stamp category* *****indentation formatted-message*

**SetupWriteTextLogError** writes the second log entry in the following format:

*entry_prefix time_stamp category* **<strong>*indentation* **Error:</strong>*error-number error-description*

Where:

-   The *entry_prefix*, *time-stamp*, *category*, *indentation*, and *formatted-message* fields are the same as those that are described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md).

-   The *error-number* field contains the error number.

-   The *error-description* field contains a user-friendly description of the error.

The following example shows how an application might typically call [**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232) to log information about an error in a text log. The error used in the example is a system start error. The application calls **SetupWriteTextLogError**, supplying the following parameter values:

- *LogToken* is set to a log token value that either was obtained by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) or is one of the system-defined log token values that are described in [Log Tokens](log-tokens.md).

- *Category* is set to TXTLOG_VENDOR, which indicates that the log entry is made by a vendor-supplied application. Event categories are described in [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

- *LogFlags* is set to TXTLOG_ERROR. This example does not include a time stamp or change the indentation depth. The current indentation depth was previously set to five monospace text spaces. For information about how to change the indentation depth, see [Writing Indented Log Entries](writing-indented-log-entries.md). Event levels are described in [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md).

- *Error* is set to the value of the Win32 error code, ERROR_SERVICE_ALREADY_RUNNING. The decimal value of this error code is 1056.

- *MessageStr is* set to TEXT("Start Service: Failed to start service 'SomeService'").

- A comma-separated parameter list is not supplied<em>.</em>

The parameters *LogToken*, *Category*, and *LogFlags* affect the operation of **SetupWriteTextLogError** in the same manner as these parameters affect the operation of **SetupWriteTextLog**.

The following code calls [**SetupWriteTextLogError**](https://msdn.microsoft.com/library/windows/hardware/ff552232) to write the log entry for this example:

```cpp
//The LogToken value was previously returned by call to
//SetupGetThreadLogToken or one of the system-defined log token values
DWORD Category = TXTLOG_VENDOR; 
DWORD Flags = TXTLOG_ERROR ;
DWORD ErrorCode = 1056; // The corresponding Win32 error code

SetupWriteTextLog(LogToken, Category, Flags, ErrorCode, TEXT("Start Service: Failed to start service &#39;SomeService&#39;"),);
```

If the TXTLOG_VENDOR event category is enabled and the TXTLOG_ERROR event level is set for the text log, this code would create an entry in the text log that would be formatted as follows:

```cpp
!!!     :  Start Service: Failed to start service &#39;SomeService&#39; 
!!!   :  Error 1056: An instance of the service is already running.
```

Be aware that **SetupWriteTextLogError** provides the string "An instance of the service is already running." to describe the Win32 error whose value is 1056.

 

 





