---
title: OID_WWAN_ENUMERATE_DEVICE_SERVICES
description: OID_WWAN_ENUMERATE_DEVICE_SERVICES returns the list of device services supported by the miniport driver.NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS status notification containing a NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure that provides the list of supported device service GUIDs.
ms.assetid: 12AB2235-DDF8-44CB-BD3D-61D0FFCB4080
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_ENUMERATE_DEVICE_SERVICES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICES


OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICES returns the list of device services supported by the miniport driver.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](https://msdn.microsoft.com/library/windows/hardware/hh846210) status notification containing a [**NDIS\_WWAN\_SUPPORTED\_DEVICE\_SERVICES**](https://msdn.microsoft.com/library/windows/hardware/hh831867) structure that provides the list of supported device service GUIDs.

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

[**NDIS\_WWAN\_SUPPORTED\_DEVICE\_SERVICES**](https://msdn.microsoft.com/library/windows/hardware/hh831867)

 

 




