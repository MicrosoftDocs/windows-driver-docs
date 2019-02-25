---
title: Using the CONNECT_MESSAGE_BASED Version of IoConnectInterruptEx
description: Using the CONNECT_MESSAGE_BASED Version of IoConnectInterruptEx
ms.assetid: 8e06c6aa-85de-4ed2-ac0d-0179201d1272
keywords: ["IoConnectInterruptEx", "CONNECT_MESSAGE_BASED", "message-signaled interrupts WDK kernel", "automatic interrupt detections WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using the CONNECT\_MESSAGE\_BASED Version of IoConnectInterruptEx


For Windows Vista and later operating systems, a driver can use the CONNECT\_MESSAGE\_BASED version of [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) to register an ISR for the driver's message-signaled interrupts. The driver specifies a value of CONNECT\_MESSAGE\_BASED for *Parameters*-&gt;**Version**, and uses the members of *Parameters*-&gt;**MessageBased** to specify the other parameters of the operation.

-   *Parameters***-&gt;MessageBased.PhysicalDeviceObject** specifies the PDO for the device that the ISR services. The system uses the device object to automatically identify the device's message-signaled interrupts.

-   *Parameters***-&gt;MessageBased.MessageServiceRoutine** points to the [*InterruptMessageService*](https://msdn.microsoft.com/library/windows/hardware/ff547940) routine, while *Parameters***-&gt;MessageBased.ServiceContext** specifies the value that the system passes as the *ServiceContext* parameter to *InterruptMessageService*. The driver can use this to pass context information. For more information about passing context information, see [Providing ISR Context Information](providing-isr-context-information.md).

-   The driver can also specify a fallback *InterruptMessageService* routine in *Parameters***-&gt;MessageBased.FallBackServiceRoutine**. If the device has line-based interrupts, but no message-signaled interrupts, the system will instead register the *InterruptMessageService* routine to service the line-based interrupts. In this case, the system passes *Parameters***-&gt;MessageBased.ServiceContext** as the *ServiceContext* parameter to [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958). **IoConnectInterruptEx** updates *Parameters***-&gt;Version** to CONNECT\_LINE\_BASED if it registered the fallback routine.

-   *Parameters***-&gt;MessageBased.ConnectionContext** points to a variable that receives a pointer to either a [**IO\_INTERRUPT\_MESSAGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550576) (for *InterruptMessageService*) structure or a [**KINTERRUPT**](https://msdn.microsoft.com/library/windows/hardware/ff554237) structure (for *InterruptService*). The driver can use the received pointer to remove the ISR. For more information, see [Removing an ISR](removing-an-isr.md).

-   Drivers can optionally specify a spin lock in *Parameters***-&gt;MessageBased.SpinLock** for the system to use when synchronizing with the ISR. Most drivers can just specify **NULL** to enable the system to allocate a spin lock on behalf of the driver. For more information about synchronizing with an ISR, see [Synchronizing Access to Device Data](synchronizing-access-to-device-data.md).

The following code example demonstrates how to register an *InterruptMessageService* routine by using CONNECT\_MESSAGE\_BASED.

```cpp
IO_CONNECT_INTERRUPT_PARAMETERS params;

// deviceExtension is a pointer to the driver&#39;s device extension. 
//     deviceExtension->IntInfo is a PVOID.
//     deviceExtension->IntType is a ULONG.
// deviceInterruptService is a pointer to the driver&#39;s InterruptService routine.
// deviceInterruptMessageService is a pointer to the driver&#39;s InterruptMessageService routine.
// PhysicalDeviceObject is a pointer to the device&#39;s PDO. 
// ServiceContext is a pointer to driver-specified context for the ISR.

RtlZeroMemory( &params, sizeof(IO_CONNECT_INTERRUPT_PARAMETERS) );
params.Version = CONNECT_MESSAGE_BASED;
params.MessageBased.PhysicalDeviceObject = PhysicalDeviceObject;
params.MessageBased.MessageServiceRoutine = deviceInterruptMessageService;
params.MessageBased.ServiceContext = ServiceContext;
params.MessageBased.SpinLock = NULL;
params.MessageBased.SynchronizeIrql = 0;
params.MessageBased.FloatingSave = FALSE;
params.MessageBased.FallBackServiceRoutine = deviceInterruptService;

status = IoConnectInterruptEx(&params);

if (NT_SUCCESS(status)) {
    // We record the type of ISR registered.
    devExt->IsrType = params.Version;
} else {
    // Operation failed. Handle error.
    ...
}
```

 

 




