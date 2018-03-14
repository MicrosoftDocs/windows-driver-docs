---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS notification to report the completion of a query of OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS.NDIS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure.
ms.assetid: 3EFEFB4B-6B13-44D7-8788-140B90103A93
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS notification to report the completion of a query of [OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS](https://msdn.microsoft.com/library/windows/hardware/hh846221).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh846214) structure.

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


[OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS](https://msdn.microsoft.com/library/windows/hardware/hh846221)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh846214)

 

 




