---
title: OID_WWAN_USSD
author: windows-driver-content
description: OID\_WWAN\_USSD sends Unstructured Supplementary Service Data (USSD) requests to the underlying MB device.
ms.assetid: 9DFAAABD-8213-4B83-8FE8-1EC2BB9F735B
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_USSD Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_USSD


OID\_WWAN\_USSD sends Unstructured Supplementary Service Data (USSD) requests to the underlying MB device.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [NDIS\_STATUS\_WWAN\_USSD](https://msdn.microsoft.com/library/windows/hardware/hh439822) status notification containing the status of the initial USSD request when they have completed the transaction.

Windows does not send an OID\_WWAN\_USSD request to a miniport driver if a previous request is still in progress, with the exception of a request to cancel a pending operation by setting the [WWAN\_USSD\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh464138) **RequestType** member of the request to *WwanUssdRequestCancel*.

When a request is canceled, the miniport driver must respond to both the canceled request and the cancel request.

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[NDIS\_STATUS\_WWAN\_USSD](https://msdn.microsoft.com/library/windows/hardware/hh439822)

[WWAN\_USSD\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh464138)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_USSD%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


