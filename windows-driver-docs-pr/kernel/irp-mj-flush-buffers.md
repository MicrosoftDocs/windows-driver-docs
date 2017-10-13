---
title: IRP_MJ_FLUSH_BUFFERS
author: windows-driver-content
description: Drivers of devices with internal caches for data and drivers that maintain internal buffers for data must handle this request in a DispatchFlushBuffers routine.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: c1023999-0c80-4c09-a9ea-a9422184bba7
keywords:
 - IRP_MJ_FLUSH_BUFFERS Kernel-Mode Driver Architecture
---

# IRP\_MJ\_FLUSH\_BUFFERS


Drivers of devices with internal caches for data and drivers that maintain internal buffers for data must handle this request in a [*DispatchFlushBuffers*](https://msdn.microsoft.com/library/windows/hardware/ff543314) routine.

When Sent
---------

Receipt of a flush request indicates that the driver should flush the device's cache or its internal buffer, or, possibly, should discard the data in its internal buffer.

## Input Parameters


None

## Output Parameters


None

Operation
---------

The driver transfers any data currently cached in the device or held in the driver's internal buffers before completing the flush request. The driver of an input-only device that buffers data internally might simply discard the currently buffered device data before completing the flush IRP, depending on the nature of its device.

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


[*DispatchFlushBuffers*](https://msdn.microsoft.com/library/windows/hardware/ff543314)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_FLUSH_BUFFERS%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


