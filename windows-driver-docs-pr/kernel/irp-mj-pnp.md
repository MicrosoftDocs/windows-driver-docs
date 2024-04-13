---
title: IRP_MJ_PNP
description: All drivers must be prepared to service IRP_MJ_PNP requests in a DispatchPnP routine.
ms.date: 08/12/2017
ms.topic: reference
keywords:
 - IRP_MJ_PNP Kernel-Mode Driver Architecture
---

# IRP\_MJ\_PNP


All drivers must be prepared to service **IRP\_MJ\_PNP** requests in a [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

## When Sent

The PnP manager sends **IRP\_MJ\_PNP** requests during enumeration, resource rebalancing, and any other time Plug and Play activity occurs on the system. Drivers can also send certain **IRP\_MJ\_PNP** requests, depending on the minor function code.

## Input Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP. Every **IRP\_MJ\_PNP** request specifies a minor function code that identifies the requested PnP action.

## Output Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP.

## Operation

See [Plug and Play Minor IRPs](plug-and-play-minor-irps.md) for detailed information about **IRP\_MJ\_PNP** requests.

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


[*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

 

