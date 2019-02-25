---
title: OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS
description: OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS returns a list of commands supported for a device service.NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS status notification containing a NDIS_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS structure that describes the result of the operation.
ms.assetid: 9888E4EC-D4BB-4BAC-B20B-DFA51005EEDA
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS


OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS returns a list of commands supported for a device service.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh846210) status notification containing a [**NDIS\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh831862) structure that describes the result of the operation.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support specified device service or operation.

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
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh846210)

[**NDIS\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh831862)

 

 




