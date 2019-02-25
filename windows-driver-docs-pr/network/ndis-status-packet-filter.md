---
title: NDIS_STATUS_PACKET_FILTER
description: The NDIS_STATUS_PACKET_FILTER status indicates a packet filter change to overlying drivers.
ms.assetid: 7633772a-cd3d-4030-b97a-9d503341fdeb
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PACKET_FILTER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PACKET\_FILTER


The NDIS\_STATUS\_PACKET\_FILTER status indicates a packet filter change to overlying drivers. NDIS generates this status indications for a miniport adapter to notify overlying drivers that there might be a change in the miniport adapter's packet filter setting.

Remarks
-------

NDIS does not guarantee that the packet filter has changed when NDIS generates the NDIS\_STATUS\_PACKET\_FILTER status indication.

NDIS filter drivers can also generate the NDIS\_STATUS\_PACKET\_FILTER status indication.

NDIS supplies a bitwise OR of the filter type flags in the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure. For a list of the filter type flags, see the [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575) OID. For additional information about packet filters, see [OID\_GEN\_SUPPORTED\_PACKET\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569643).

The **StatusBufferSize** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure is set to sizeof(ULONG).

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575)

[OID\_GEN\_SUPPORTED\_PACKET\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569643)

 

 




