---
title: Using IoConnectInterruptEx Prior to Windows Vista
description: Using IoConnectInterruptEx Prior to Windows Vista
ms.assetid: a08b2869-93f8-440b-9fbe-068604c6007d
keywords: ["IoConnectInterruptEx", "iointex.h", "line-based interrupts WDK kernel", "message-signaled interrupts WDK kernel", "CONNECT_LINE_BASED", "CONNECT_MESSAGE_BASED", "CONNECT_FULLY_SPECIFIED"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using IoConnectInterruptEx Prior to Windows Vista


A driver for Windows 2000, Windows XP, or Windows Server 2003 can link to the Iointex.lib library to use [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) on those versions of the operating system.

To use **IoConnectInterruptEx** in such a driver, include Iointex.h in the source code for your driver, immediately following Wdm.h or Ntddk.h. The Iointex.h header declares a prototype for the routine. When you build your driver, make sure that it is statically linked to Iointex.lib.

For operating systems prior to Windows Vista, the version of **IoConnectInterruptEx** provided by Iointex.lib only supports the CONNECT\_FULLY\_SPECIFIED version of the routine. If any other version is specified, the routine returns an NTSTATUS error code, and sets *Parameters*-&gt;**Version** to CONNECT\_FULLY\_SPECIFIED.

Using this behavior, you can write your driver so that it uses CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED on Windows Vista, and CONNECT\_FULLY\_SPECIFIED on earlier operating systems. First call **IoConnectInterruptEx** with *Parameters*-&gt;**Version** equal to CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED. If the return value is an error code and *Parameters*-&gt;**Version** != CONNECT\_FULLY\_SPECIFIED, then retry the operation with *Parameters*-&gt;**Version** set to CONNECT\_FULLY\_SPECIFIED.

The following code example illustrates the technique:

```cpp
IO_CONNECT_INTERRUPT_PARAMETERS params;

// deviceExtension is a pointer to the driver&#39;s device extension. 
//     deviceExtension->MessageUsed is a BOOLEAN.

RtlZeroMemory( &params, sizeof(IO_CONNECT_INTERRUPT_PARAMETERS) );
params.Version = CONNECT_MESSAGE_BASED;

// Set members of params.MessageBased here.

status = IoConnectInterruptEx(&params);

if ( NT_SUCCESS(status) ) {
    // Operation succeeded. We are running on Windows Vista.
    devExt->MessageUsed = TRUE; // We save this for posterity.
} else {
    // Check to see if we are running on an operating system prior to Windows Vista.
    if (params.Version == CONNECT_FULLY_SPECIFIED) {
        devExt->MessageUsed = FALSE;  // We&#39;re not using message-signaled interrupts.
 
        // Set members of params.FullySpecified here.
 
        status = IoConnectInterruptEx(&params);
    } else {
        // Other error.
    }
}
```

 

 




