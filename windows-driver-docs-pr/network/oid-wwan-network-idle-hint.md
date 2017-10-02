---
title: OID_WWAN_NETWORK_IDLE_HINT
author: windows-driver-content
description: OID\_WWAN\_NETWORK\_IDLE\_HINT sends a hint to the network interface regarding whether data is expected to be active or idle on the interface.
ms.assetid: 1FE758C1-543A-45B4-A377-336A1307689F
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_NETWORK_IDLE_HINT Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_NETWORK\_IDLE\_HINT


OID\_WWAN\_NETWORK\_IDLE\_HINT sends a hint to the network interface regarding whether data is expected to be active or idle on the interface. The network service uses heuristics to determine when to send this request to the interface, typically when it estimates that for a period of time there will be a reduction in network traffic or if the system is entering an idle state (such as connected standby). The network interface can use this as an input to its heuristics to implement procedures such as "fast dormancy".

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later completing the request with the [**NDIS\_WWAN\_NETWORK\_IDLE\_HINT**](https://msdn.microsoft.com/library/windows/hardware/dn931088) structure that indicates the network idle hint.

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
<td><p>Available in Windows 10 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_NETWORK\_IDLE\_HINT**](https://msdn.microsoft.com/library/windows/hardware/dn931088)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_NETWORK_IDLE_HINT%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


