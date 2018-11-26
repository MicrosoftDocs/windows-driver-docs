---
title: NDIS_STATUS_RESET_START
description: The NDIS_STATUS_RESET_START status indicates that a miniport adapter is being reset.
ms.assetid: 8758652b-137b-43e3-a896-8360f2b5051c
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_RESET_START Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RESET\_START


The NDIS\_STATUS\_RESET\_START status indicates that a miniport adapter is being reset.

Remarks
-------

Miniport drivers should not call the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to signal the start and finish of each reset operation because NDIS notifies overlying drivers when a reset operation begins and ends.

A miniport driver resets a miniport adapter when NDIS calls the miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function. NDIS calls the [*ProtocolStatusEx*](https://msdn.microsoft.com/library/windows/hardware/ff570270) function of each bound protocol and intermediate driver and the [*FilterStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549973) function of the overlying filter modules with a status of NDIS\_STATUS\_RESET\_START. When the miniport driver completes the reset, NDIS notifies the overlying drivers with a status of [**NDIS\_STATUS\_RESET\_END**](ndis-status-reset-end.md).

When a protocol driver receives an NDIS\_STATUS\_RESET\_START status indication, it should:

-   Hold any data that is ready to transmit until its *ProtocolStatusEx* function receives an NDIS\_STATUS\_RESET\_END status indication.

-   Not make any NDIS calls that are directed to the underlying miniport driver, except calls to return resources such as received data buffers with the [**NdisReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564534) function.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*FilterStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549973)

[*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432)

[**NDIS\_STATUS\_RESET\_END**](ndis-status-reset-end.md)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

[**NdisReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564534)

[*ProtocolStatusEx*](https://msdn.microsoft.com/library/windows/hardware/ff570270)

 

 




