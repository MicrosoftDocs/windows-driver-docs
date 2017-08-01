---
title: NDIS_STATUS_RESET_START
author: windows-driver-content
description: The NDIS_STATUS_RESET_START status indicates that a miniport adapter is being reset.
ms.assetid: 8758652b-137b-43e3-a896-8360f2b5051c
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_RESET_START Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_RESET_START%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


