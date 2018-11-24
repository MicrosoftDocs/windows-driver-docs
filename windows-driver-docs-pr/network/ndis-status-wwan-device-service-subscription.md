---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION notification to inform the MB Service about a device service subscription in response to an OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS set request.NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION structure.
ms.assetid: E2B839AE-F81A-41EE-8374-F830B79D1E74
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION notification to inform the MB Service about a device service subscription in response to an [OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS](https://msdn.microsoft.com/library/windows/hardware/hh440096) set request.

Miniport drivers cannot use this notification to send unsolicited events.

This indication uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/hh439839) structure.

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


[OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS](https://msdn.microsoft.com/library/windows/hardware/hh440096)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/hh439839)

 

 




