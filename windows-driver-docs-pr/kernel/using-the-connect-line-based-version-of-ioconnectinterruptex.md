---
title: Using the CONNECT\_LINE\_BASED Version of IoConnectInterruptEx
author: windows-driver-content
description: Using the CONNECT\_LINE\_BASED Version of IoConnectInterruptEx
ms.assetid: 245be266-f76c-43f6-9ea7-2dc853b1d5e2
keywords: ["IoConnectInterruptEx", "CONNECT_LINE_BASED", "line-based interrupts WDK kernel", "automatic interrupt detections WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the CONNECT\_LINE\_BASED Version of IoConnectInterruptEx


For Windows Vista and later operating systems, a driver can use the CONNECT\_LINE\_BASED version of [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) to register an [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine for the driver's line-based interrupts. (Driver for earlier operating systems can use the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx**.)

**Note**   You can use this method only for drivers that register a single interrupt service routine (ISR) for all of its line-based interrupts. If the driver can receive multiple interrupts, it must use the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx**.

 

The driver specifies a value of CONNECT\_LINE\_BASED for *Parameters*-&gt;**Version** and uses the members of *Parameters*-&gt;**LineBased** to specify the other parameters of the operation:

-   *Parameters*-&gt;**LineBased.PhysicalDeviceObject** specifies the physical device object (PDO) for the device that the ISR services. The system uses the device object to automatically identify the device's line-based interrupts.

-   *Parameters*-&gt;**LineBased.ServiceRoutine** points to the *InterruptService* routine, while *Parameters*-&gt;**LineBased**.**ServiceContext** specifies the value that the system passes as the *ServiceContext* parameter to *InterruptService*. The driver can use this to pass context information. For more information about passing context information, see [Providing ISR Context Information](providing-isr-context-information.md).

-   The driver provides a pointer to a PKINTERRUPT variable in *Parameters***-&gt;LineBased.InterruptObject**. **IoConnectInterruptEx** sets this variable to point to the interrupt object for the interrupt, which can be used when removing the ISR. For more information, see [Removing an ISR](removing-an-isr.md).

-   Drivers can optionally specify a spin lock in *Parameters***-&gt;LineBased.SpinLock** for the system to use when synchronizing with the ISR. Most drivers can just specify **NULL** to enable the system to allocate a spin lock on behalf of the driver. For more information about synchronizing with an ISR, see [Synchronizing Access to Device Data](synchronizing-access-to-device-data.md).

The following code example demonstrates how to register an *InterruptService* routine using CONNECT\_LINE\_BASED:

```
IO_CONNECT_INTERRUPT_PARAMETERS params;

// deviceExtension is a pointer to the driver&#39;s device extension. 
//     deviceExtension->IntObj is a PKINTERRUPT.
// deviceInterruptService is a pointer to the driver&#39;s InterruptService routine.
// PhysicalDeviceObject is a pointer to the device&#39;s PDO. 
// ServiceContext is a pointer to driver-specified context for the ISR.

RtlZeroMemory( &params, sizeof(IO_CONNECT_INTERRUPT_PARAMETERS) );
params.Version = CONNECT_LINE_BASED;
params.LineBased.PhysicalDeviceObject = PhysicalDeviceObject;
params.LineBased.InterruptObject = &deviceExtension->IntObj;
params.LineBased.ServiceRoutine = deviceInterruptService;
params.LineBased.ServiceContext = ServiceContext;
params.LineBased.SpinLock = NULL;
params.LineBased.SynchronizeIrql = 0;
params.LineBased.FloatingSave = FALSE;

status = IoConnectInterruptEx(&params);

if (!NT_SUCCESS(status)) {
    // Operation failed. Handle error.
    ...
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20CONNECT_LINE_BASED%20Version%20of%20IoConnectInterruptEx%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


