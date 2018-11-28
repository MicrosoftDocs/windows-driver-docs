---
title: NDIS_STATUS_WAN_CO_FRAGMENT
description: The NDIS_STATUS_WAN_CO_FRAGMENT status indicates that a CoNDIS WAN miniport driver has received a partial packet from the endpoint of a VC.
ms.assetid: 5a534364-d528-45f8-a2e0-3c745b3b5ad0
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WAN_CO_FRAGMENT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WAN\_CO\_FRAGMENT


The NDIS\_STATUS\_WAN\_CO\_FRAGMENT status indicates that a CoNDIS WAN miniport driver has received a partial packet from the endpoint of a VC.

Remarks
-------

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a pointer to an [**NDIS\_WAN\_CO\_FRAGMENT**](https://msdn.microsoft.com/library/windows/hardware/ff559030) structure. The NDIS\_WAN\_CO\_FRAGMENT structure describes the reason that the partial packet was received.

For more information about NDIS\_STATUS\_WAN\_CO\_FRAGMENT, see [Indicating CoNDIS WAN Miniport Driver Status](https://msdn.microsoft.com/library/windows/hardware/ff554825). For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553805).

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


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_WAN\_CO\_FRAGMENT**](https://msdn.microsoft.com/library/windows/hardware/ff559030)

 

 




