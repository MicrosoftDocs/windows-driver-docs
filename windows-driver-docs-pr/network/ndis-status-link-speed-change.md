---
title: NDIS_STATUS_LINK_SPEED_CHANGE
description: The NDIS_STATUS_LINK_SPEED_CHANGE status indicates a link speed change.
ms.assetid: 084e43c9-598c-4c30-8004-2d1876a1cddd
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_LINK_SPEED_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_LINK\_SPEED\_CHANGE


The NDIS\_STATUS\_LINK\_SPEED\_CHANGE status indicates a link speed change.

Remarks
-------

NDIS translates NDIS\_STATUS\_LINK\_SPEED\_CHANGE status indications to [**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md) status indications for overlying NDIS 6.0 drivers. When NDIS receives an NDIS\_STATUS\_LINK\_SPEED\_CHANGE status, NDIS issues an OID query request of [OID\_GEN\_LINK\_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593). NDIS uses the results of the OID\_GEN\_LINK\_SPEED query to issue an NDIS\_STATUS\_LINK\_STATE status to overlying NDIS 6.0 drivers.

The NDIS 5.*x* or earlier miniport driver supplies a DWORD-type value at the *StatusBuffer* parameter of the [**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538) function. For more information about NDIS\_STATUS\_LINK\_SPEED\_CHANGE, see [OID\_IRDA\_RATE\_SNIFF](https://msdn.microsoft.com/library/windows/hardware/ff560287).

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
<td><p>Not supported in NDIS 6.0 and later (use <a href="ndis-status-link-state.md" data-raw-source="[&lt;strong&gt;NDIS_STATUS_LINK_STATE&lt;/strong&gt;](ndis-status-link-state.md)"><strong>NDIS_STATUS_LINK_STATE</strong></a> instead). Supported only for NDIS 5.1 drivers in Windows Vista and Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md)

[**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538)

[OID\_GEN\_LINK\_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593)

[OID\_IRDA\_RATE\_SNIFF](https://msdn.microsoft.com/library/windows/hardware/ff560287)

 

 




