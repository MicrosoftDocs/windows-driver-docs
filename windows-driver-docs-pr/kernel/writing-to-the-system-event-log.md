---
title: Writing to the System Event Log
author: windows-driver-content
description: Writing to the System Event Log
MS-HAID:
- 'Other\_0af109e1-fb0c-42b8-8eb0-e0acb66be9c3.xml'
- 'kernel.writing\_to\_the\_system\_event\_log'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 19be8bb4-8736-4d1a-92e5-b63a5f04e254
keywords: ["NTSTATUS values WDK kernel", "dump data WDK kernel", "predefined error codes WDK kernel", "system event logs WDK kernel", "property sheets WDK errors", "Event Viewer WDK kernel", "sample log entry property sheets WDK kernel", "log entries WDK kernel", "entries WDK error logs"]
---

# Writing to the System Event Log


## <a href="" id="ddk-writing-to-the-system-event-log-kg"></a>


Errors are specified by their NTSTATUS value. The system predefines particular NTSTATUS values that can be used by drivers, and driver writers can define additional errors. Note that only certain NTSTATUS values can be used when logging errors.

Each NTSTATUS value that can be used when logging errors has an associated error message. For example, the parallel port driver uses the NTSTATUS value PAR\_INTERRUPT\_CONFLICT to represent hardware interrupt conflicts, with message text "Interrupt conflict detected for %1".

The Event Viewer displays the message text in the **Description** text box on the log entry's property sheet. If the message text string contains "%1", the Event Viewer replaces it with the name of the device that logged the entry. The message text can contain additional parameters of the form "%2", "%3", and so on. When the driver logs the error, it can provide string values for those parameters. These string values are known as *insertion strings*. The Event Viewer will automatically insert them in place of the percent values.

The driver can also include binary data in the log entry, known as *dump data*. The Event Viewer displays the dump data in the **Data** text box of the log entry's property sheet.

You can bring up the property sheet for a log entry by double-clicking the entry in the Event Viewer. The following screen shot shows a sample log entry property sheet.

![screen shot of an event property sheet](images/event-properties.png)

Drivers use the [**IoAllocateErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548245) routine to allocate an error log entry. Log entries consist of a variable-length [**IO\_ERROR\_LOG\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff550571) header, followed by insertion strings.

The following diagram shows the layout of an error log entry in memory.

![diagram illustrating a layout of an error log packet in memory ](images/errorlogentry.png)

The **ErrorCode** member of **IO\_ERROR\_LOG\_PACKET** specifies the NTSTATUS value of the error. The **DumpData** member specifies any dump data for the log entry. **DumpData** is a variable-sized array, whose size is specified by the **DumpDataSize** member. Drivers specify the beginning of the first insertion string with the **StringOffset** member, and the number of strings in the **NumberOfStrings** member. Each insertion string itself is a null-terminated Unicode string.

Once the driver fills out the allocated error log entry, it writes the entry to the error log by using [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527). **IoWriteErrorLogEntry** automatically frees the memory allocated for the log entry. Drivers can use [**IoFreeErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff549107) to free any unused log entries.

Predefined error codes (of the form IO\_ERR\_*XXX*) are defined in the ntiologc.h header file that is included with the Windows Driver Kit (WDK). The error message associated with each error code can be found in the comments for ntiologc.h, next to the error code's declaration. To use a predefined error code, the driver must register the system file, iologmsg.dll, as the source of the associated error messages. For further information, see [Registering as a Source of Error Messages](registering-as-a-source-of-error-messages.md).

Drivers can also define their own custom error types, and associated error messages. For further information, see [Defining Custom Error Types](defining-custom-error-types.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20to%20the%20System%20Event%20Log%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


