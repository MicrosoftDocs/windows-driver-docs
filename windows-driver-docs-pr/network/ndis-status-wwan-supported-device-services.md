---
title: NDIS_STATUS_WWAN_SUPPORTED_DEVICE_SERVICES
description: Miniport drivers use the NDIS_STATUS_WWAN_SUPPORTED_DEVICE_SERVICES notification to inform the MB Service about the completion of OID_WWAN_ENUMERATE_DEVICE_SERVICES query requests.NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure.
ms.assetid: 6364DDF7-CE68-4E00-8532-221DD209F145
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_SUPPORTED_DEVICE_SERVICES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SUPPORTED\_DEVICE\_SERVICES


Miniport drivers use the NDIS\_STATUS\_WWAN\_SUPPORTED\_DEVICE\_SERVICES notification to inform the MB Service about the completion of [OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICES](https://msdn.microsoft.com/library/windows/hardware/hh846220) query requests.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_SUPPORTED\_DEVICE\_SERVICES**](https://msdn.microsoft.com/library/windows/hardware/hh831867) structure.

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


[OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICES](https://msdn.microsoft.com/library/windows/hardware/hh846220)

[**NDIS\_WWAN\_SUPPORTED\_DEVICE\_SERVICES**](https://msdn.microsoft.com/library/windows/hardware/hh831867)

 

 




