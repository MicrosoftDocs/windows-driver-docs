---
title: OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS
author: windows-driver-content
description: OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS returns a list of commands supported for a device service.NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS status notification containing a NDIS\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS structure that describes the result of the operation.
ms.assetid: 9888E4EC-D4BB-4BAC-B20B-DFA51005EEDA
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


