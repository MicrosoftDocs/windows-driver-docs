---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE indication to implement the transaction completion response for OID_WWAN_DEVICE_SERVICE_COMMAND.NDIS_WWAN_DEVICE_SERVICE_RESPONSE structure.
ms.assetid: 2817EAFA-7A9A-4DC1-B2B7-31E1F4E5E331
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_RESPONSE


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_RESPONSE indication to implement the transaction completion response for [OID\_WWAN\_DEVICE\_SERVICE\_COMMAND](https://msdn.microsoft.com/library/windows/hardware/hh440094).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh439838) structure.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_DEVICE\_SERVICE\_COMMAND](https://msdn.microsoft.com/library/windows/hardware/hh440094)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh439838)

 

 




