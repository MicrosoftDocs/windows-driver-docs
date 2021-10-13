---
title: IRP_MJ_FLUSH_BUFFERS
description: Drivers of devices with internal caches for data and drivers that maintain internal buffers for data must handle this request in a DispatchFlushBuffers routine.
ms.date: 08/12/2017
keywords:
 - IRP_MJ_FLUSH_BUFFERS Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_FLUSH\_BUFFERS


Drivers of devices with internal caches for data and drivers that maintain internal buffers for data must handle this request in a [*DispatchFlushBuffers*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

## When Sent

Receipt of a flush request indicates that the driver should flush the device's cache or its internal buffer, or, possibly, should discard the data in its internal buffer.

## Input Parameters


None

## Output Parameters


None

## Operation

The driver transfers any data currently cached in the device or held in the driver's internal buffers before completing the flush request. The driver of an input-only device that buffers data internally might simply discard the currently buffered device data before completing the flush IRP, depending on the nature of its device.

## Requirements

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


[*DispatchFlushBuffers*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

 

