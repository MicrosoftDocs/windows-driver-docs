---
title: Using IoConnectInterruptEx Prior to Windows Vista
author: windows-driver-content
description: Using IoConnectInterruptEx Prior to Windows Vista
MS-HAID:
- 'Intrupts\_49c9e529-8d6d-49c8-a24e-511c29478f22.xml'
- 'kernel.using\_ioconnectinterruptex\_prior\_to\_windows\_vista'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a08b2869-93f8-440b-9fbe-068604c6007d
keywords: ["IoConnectInterruptEx", "iointex.h", "line-based interrupts WDK kernel", "message-signaled interrupts WDK kernel", "CONNECT_LINE_BASED", "CONNECT_MESSAGE_BASED", "CONNECT_FULLY_SPECIFIED"]
---

# Using IoConnectInterruptEx Prior to Windows Vista


A driver for Windows 2000, Windows XP, or Windows Server 2003 can link to the Iointex.lib library to use [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) on those versions of the operating system.

To use **IoConnectInterruptEx** in such a driver, include Iointex.h in the source code for your driver, immediately following Wdm.h or Ntddk.h. The Iointex.h header declares a prototype for the routine. When you build your driver, make sure that it is statically linked to Iointex.lib.

For operating systems prior to Windows Vista, the version of **IoConnectInterruptEx** provided by Iointex.lib only supports the CONNECT\_FULLY\_SPECIFIED version of the routine. If any other version is specified, the routine returns an NTSTATUS error code, and sets *Parameters*-&gt;**Version** to CONNECT\_FULLY\_SPECIFIED.

Using this behavior, you can write your driver so that it uses CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED on Windows Vista, and CONNECT\_FULLY\_SPECIFIED on earlier operating systems. First call **IoConnectInterruptEx** with *Parameters*-&gt;**Version** equal to CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED. If the return value is an error code and *Parameters*-&gt;**Version** != CONNECT\_FULLY\_SPECIFIED, then retry the operation with *Parameters*-&gt;**Version** set to CONNECT\_FULLY\_SPECIFIED.

The following code example illustrates the technique:

```
IO_CONNECT_INTERRUPT_PARAMETERS params;

// deviceExtension is a pointer to the driver&#39;s device extension. 
//     deviceExtension->MessageUsed is a BOOLEAN.

RtlZeroMemory( &amp;params, sizeof(IO_CONNECT_INTERRUPT_PARAMETERS) );
params.Version = CONNECT_MESSAGE_BASED;

// Set members of params.MessageBased here.

status = IoConnectInterruptEx(&amp;params);

if ( NT_SUCCESS(status) ) {
    // Operation succeeded. We are running on Windows Vista.
    devExt->MessageUsed = TRUE; // We save this for posterity.
} else {
    // Check to see if we are running on an operating system prior to Windows Vista.
    if (params.Version == CONNECT_FULLY_SPECIFIED) {
        devExt->MessageUsed = FALSE;  // We&#39;re not using message-signaled interrupts.
 
        // Set members of params.FullySpecified here.
 
        status = IoConnectInterruptEx(&amp;params);
    } else {
        // Other error.
    }
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20IoConnectInterruptEx%20Prior%20to%20Windows%20Vista%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


