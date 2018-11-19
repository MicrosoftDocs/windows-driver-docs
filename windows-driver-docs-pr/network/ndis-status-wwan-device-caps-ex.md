---
title: NDIS_STATUS_WWAN_DEVICE_CAPS_EX
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_CAPS_EX notification to inform the MB service about the completion of a previous OID_WWAN_DEVICE_CAPS_EX query request.
ms.assetid: 7E596CB0-2A08-45E4-9932-5E951B880D62
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_CAPS_EX Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_CAPS\_EX


Miniport drivers use the **NDIS\_STATUS\_WWAN\_DEVICE\_CAPS\_EX** notification to inform the MB service about the completion of a previous [OID\_WWAN\_DEVICE\_CAPS\_EX](https://msdn.microsoft.com/library/windows/hardware/mt799830) query request.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt782401) structure.

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
<td><p>Windows 10, version 1703</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_DEVICE\_CAPS\_EX](https://msdn.microsoft.com/library/windows/hardware/mt799830)

[**NDIS\_WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt782401)

 

 




