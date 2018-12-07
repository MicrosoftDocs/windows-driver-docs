---
title: NDIS_STATUS_TAPI_INDICATION
description: The NDIS_STATUS_TAPI_INDICATION status indicates that a TAPI event occurred. A WAN-capable miniport driver can indicate TAPI status.
ms.assetid: b90c5524-2e03-45e1-9ec9-478112eba01b
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_TAPI_INDICATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_TAPI\_INDICATION


The NDIS\_STATUS\_TAPI\_INDICATION status indicates that a TAPI event occurred. A WAN-capable miniport driver can indicate TAPI status.

Remarks
-------

NDIS 4.*x* and earlier NDIS WAN miniport drivers use this status indication. NDIS 5.0 and later WAN miniport drivers must use the CoNDIS WAN interface. For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546752).

The *StatusBuffer* parameter of the [**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538) function contains a pointer to an [**NDIS\_TAPI\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff558986) structure.The NDIS\_TAPI\_EVENT structure describes the TAPI line or call event that occurs (for example, changes in line and call states, the arrival of an incoming call, and the closing by a remote node or by the miniport driver of an existing call or line).

For more information about NDIS\_STATUS\_TAPI\_INDICATION, see [Indicating NDIS WAN Miniport Driver Status (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546867).

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
<td><p>Not supported for NDIS 6.0 drivers or NDIS 5.1 drivers in Windows Vista or Windows XP. Supported for NDIS 4.x drivers.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_TAPI\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff558986)

[**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538)

 

 




