---
title: OID\_WWAN\_SERVICE\_ACTIVATION
author: windows-driver-content
description: OID\_WWAN\_SERVICE\_ACTIVATION instructs miniport drivers to initiate service activation in order to gain access to the provider's network.
ms.assetid: a70c087d-0650-4aab-b78e-0d5a7aa49eb6
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WWAN_SERVICE_ACTIVATION Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SERVICE\_ACTIVATION


OID\_WWAN\_SERVICE\_ACTIVATION instructs miniport drivers to initiate service activation in order to gain access to the provider's network.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION**](ndis-status-wwan-service-activation.md) status notification containing an [**NDIS\_WWAN\_SERVICE\_ACTIVATION**](ndis-wwan-service-activation.md) structure to initiate service activation in order to gain access to the provider's network when they have completed the transaction.

Remarks
-------

For more information about using this OID, see [MB Service Detection and Activation](https://msdn.microsoft.com/library/windows/hardware/ff559122).

Miniport drivers can access the Subscriber Identity Module (SIM card) or the provider network when processing query or set requests.

The MB Service uses OID\_WWAN\_SERVICE\_ACTIVATION in the case where the service activation process requires miniport driver and user interactions.

This is not needed for miniport driver initiated or out-of-band manual service activations such as calling into the service provider's helpdesk. After the device is activated as in the above scenarios, if the current miniport driver **ReadyState** is *WwanReadyStateNotActivated*, the miniport driver shall proceed with MB initialization and notify the MB Service of ready-state change using NDIS\_STATUS\_WWAN\_READY\_INFO INDICATION .

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support miniport driver-based service activation.

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
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_READY\_INFO](oid-wwan-ready-info.md)

[**NDIS\_WWAN\_SERVICE\_ACTIVATION**](ndis-wwan-service-activation.md)

[**NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION**](ndis-status-wwan-service-activation.md)

[MB Service Detection and Activation](https://msdn.microsoft.com/library/windows/hardware/ff559122)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SERVICE_ACTIVATION%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


