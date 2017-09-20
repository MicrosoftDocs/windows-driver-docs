---
title: IRP\_MJ\_SHUTDOWN
author: windows-driver-content
description: Drivers of mass-storage devices that have internal caches for data must handle this request in a DispatchShutdown routine.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: af0b01b5-5f81-42da-aa4b-433bd422a51f
keywords:
 - IRP_MJ_SHUTDOWN Kernel-Mode Driver Architecture
---

# IRP\_MJ\_SHUTDOWN


Drivers of mass-storage devices that have internal caches for data must handle this request in a [*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405) routine. Drivers of mass-storage devices and intermediate drivers layered over them also must handle this request if an underlying driver maintains internal buffers for data.

When Sent
---------

Receipt of a shutdown request indicates that a file system driver is sending notice that the system is being shut down.

One or more file system drivers can send such a lower-level driver more than one shutdown request when a user logs off or when the system is being shut down for some other reason.

## Input Parameters


None

## Output Parameters


None

Operation
---------

The driver must complete the transfer of any data currently cached in the device or held in the driver's internal buffers before completing the shutdown request.

A driver does not receive an **IRP\_MJ\_SHUTDOWN** request for a device object unless it registers to do so with either [**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541) or [**IoRegisterLastChanceShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549518).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405)

[**IoRegisterLastChanceShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549518)

[**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_SHUTDOWN%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


