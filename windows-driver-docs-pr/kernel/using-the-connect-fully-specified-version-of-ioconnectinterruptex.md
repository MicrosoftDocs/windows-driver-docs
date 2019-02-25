---
title: Using the CONNECT_FULLY_SPECIFIED Version of IoConnectInterruptEx
description: Using the CONNECT_FULLY_SPECIFIED Version of IoConnectInterruptEx
ms.assetid: 5b75c32e-77e5-4761-b709-fedb8e33b57a
keywords: ["IoConnectInterruptEx", "CONNECT_FULLY_SPECIFIED", "manual interrupt detections WDK kernel", "line-based interrupts WDK kernel", "message-signaled interrupts WDK kernel", "FullySpecified"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using the CONNECT\_FULLY\_SPECIFIED Version of IoConnectInterruptEx


A driver can use the CONNECT\_FULLY\_SPECIFIED version of [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) to register an [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine for a specific interrupt. A driver can use the CONNECT\_FULLY\_SPECIFIED version starting with Windows Vista. By linking to the Iointex.lib library, the driver can use the CONNECT\_FULLY\_SPECIFIED version in Windows 2000, Windows XP, and Windows Server 2003. For more information, see [Using IoConnectInterruptEx Prior to Windows Vista](using-ioconnectinterruptex-prior-to-windows-vista.md).

The driver specifies a value of CONNECT\_FULLY\_SPECIFIED for *Parameters***-&gt;Version** and uses the members of *Parameters***-&gt;FullySpecified** to specify the other parameters of the operation:

-   *Parameters***-&gt;FullySpecified.PhysicalDeviceObject** specifies the PDO for the device that the ISR services.

-   *Parameters*-&gt;**FullySpecified.ServiceRoutine** points to the *InterruptService* routine, while *Parameters*-&gt;**FullySpecified**.**ServiceContext** specifies the value that the system passes as the *ServiceContext* parameter to *InterruptService*. The driver can use this to pass context information. For more information about passing context information, see [Providing ISR Context Information](providing-isr-context-information.md).

-   The driver provides a pointer to a PKINTERRUPT variable in *Parameters***-&gt;FullySpecified.InterruptObject**. The **IoConnectInterruptEx** routine sets this variable to point to the interrupt object for the interrupt, which can be used when [removing the ISR](removing-an-isr.md).

-   Drivers can optionally specify a spin lock in *Parameters***-&gt;FullySpecified.SpinLock** for the system to use when synchronizing with the ISR. Most drivers can just specify **NULL** to enable the system to allocate a spin lock on behalf of the driver. For more information about synchronizing with an ISR, see [Synchronizing Access to Device Data](synchronizing-access-to-device-data.md).

The driver must specify the key properties of the interrupt in other members of *Parameters***-&gt;FullySpecified**. The system provides the necessary information in the array of [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structures when it sends the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) IRP to the driver.

The system provides for each interrupt a **CM\_PARTIAL\_RESOURCE\_DESCRIPTOR** structure with **Type** member equal to **CmResourceTypeInterrupt**. For a message-signaled interrupt, the CM\_RESOURCE\_INTERRUPT\_MESSAGE bit of the **Flags** member is set; otherwise, it is cleared.

The **u.Interrupt** member of **CM\_PARTIAL\_RESOURCE\_DESCRIPTOR** contains the description of a line-based interrupt, while the **u.MessageInterrupt.Translated** member contains the description of a message-signaled interrupt. The following table indicates where, in the **CM\_PARTIAL\_RESOURCE\_DESCRIPTOR** structure, to find the information required to set the members of *Parameters*-&gt;**FullySpecified** for both types of interrupt. For more information, see the code example that follows the table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Line-based interrupt</th>
<th>Message-signaled interrupt</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>ShareVector</strong></p></td>
<td><p><strong>ShareDisposition</strong></p></td>
<td><p><strong>ShareDisposition</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>Vector</strong></p></td>
<td><p><strong>u.Interrupt.Vector</strong></p></td>
<td><p><strong>u.MessageInterrupt.Translated.Vector</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>Irql</strong></p></td>
<td><p><strong>u.Interrupt.Level</strong></p></td>
<td><p><strong>u.MessageInterrupt.Translated.Level</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>InterruptMode</strong></p></td>
<td><p><strong>Flags</strong> &amp; CM_RESOURCE_INTERRUPT_LATCHED</p></td>
<td><p><strong>Flags</strong> &amp; CM_RESOURCE_INTERRUPT_LATCHED</p></td>
</tr>
<tr class="odd">
<td><p><strong>ProcessorEnableMask</strong></p></td>
<td><p><strong>u.Interrupt.Affinity</strong></p></td>
<td><p><strong>u.MessageInterrupt.Translated.Affinity</strong></p></td>
</tr>
</tbody>
</table>

 

A driver will only receive **CM\_PARTIAL\_RESOURCE\_DESCRIPTOR** structures for message-signaled interrupts on Windows Vista and later versions of Windows.

The following code example demonstrates how to register an *InterruptService* routine using CONNECT\_FULLY\_SPECIFIED.

```cpp
IO_CONNECT_INTERRUPT_PARAMETERS params;

// deviceExtension is a pointer to the driver&#39;s device extension. 
//     deviceExtension->IntObj is a PKINTERRUPT.
// deviceInterruptService is a pointer to the driver&#39;s InterruptService routine.
// IntResource is a CM_PARTIAL_RESOURCE_DESCRIPTOR structure of either type CmResourceTypeInterrupt or CmResourceTypeMessageInterrupt.
// PhysicalDeviceObject is a pointer to the device&#39;s PDO. 
// ServiceContext is a pointer to driver-specified context for the ISR.

RtlZeroMemory( &params, sizeof(IO_CONNECT_INTERRUPT_PARAMETERS) );
params.Version = CONNECT_FULLY_SPECIFIED;
params.FullySpecified.PhysicalDeviceObject = PhysicalDeviceObject;
params.FullySpecified.InterruptObject = &devExt->IntObj;
params.FullySpecified.ServiceRoutine = deviceInterruptService;
params.FullySpecified.ServiceContext = ServiceContext;
params.FullySpecified.FloatingSave = FALSE;
params.FullySpecified.SpinLock = NULL;

if (IntResource->Flags & CM_RESOURCE_INTERRUPT_MESSAGE) {
    // The resource is for a message-signaled interrupt. Use the u.MessageInterrupt.Translated member of IntResource.
 
    params.FullySpecified.Vector = IntResource->u.MessageInterrupt.Translated.Vector;
    params.FullySpecified.Irql = (KIRQL)IntResource->u.MessageInterrupt.Translated.Level;
    params.FullySpecified.SynchronizeIrql = (KIRQL)IntResource->u.MessageInterrupt.Translated.Level;
    params.FullySpecified.ProcessorEnableMask = IntResource->u.MessageInterrupt.Translated.Affinity;
} else {
    // The resource is for a line-based interrupt. Use the u.Interrupt member of IntResource.
 
    params.FullySpecified.Vector = IntResource->u.Interrupt.Vector;
    params.FullySpecified.Irql = (KIRQL)IntResource->u.Interrupt.Level;
    params.FullySpecified.SynchronizeIrql = (KIRQL)IntResource->u.Interrupt.Level;
    params.FullySpecified.ProcessorEnableMask = IntResource->u.Interrupt.Affinity;
}

params.FullySpecified.InterruptMode = (IntResource->Flags & CM_RESOURCE_INTERRUPT_LATCHED ? Latched : LevelSensitive);
params.FullySpecified.ShareVector = (BOOLEAN)(IntResource->ShareDisposition == CmResourceShareShared);

status = IoConnectInterruptEx(&params);

if (!NT_SUCCESS(status)) {
    ...
}
```

 

 




