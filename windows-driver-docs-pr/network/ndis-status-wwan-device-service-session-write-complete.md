---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE notification to report the status of a write operation on a device service session.NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure.
ms.assetid: 39C0FE62-E262-4D7D-8A93-6C31431AF846
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE notification to report the status of a write operation on a device service session.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh831861) structure.

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


[**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh831861)

 

 




