---
title: OID_WWAN_SERVICE_ACTIVATION
description: OID_WWAN_SERVICE_ACTIVATION instructs miniport drivers to initiate service activation in order to gain access to the provider's network.
ms.assetid: a70c087d-0650-4aab-b78e-0d5a7aa49eb6
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SERVICE_ACTIVATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_SERVICE\_ACTIVATION


OID\_WWAN\_SERVICE\_ACTIVATION instructs miniport drivers to initiate service activation in order to gain access to the provider's network.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION**](ndis-status-wwan-service-activation.md) status notification containing an [**NDIS\_WWAN\_SERVICE\_ACTIVATION**](https://msdn.microsoft.com/library/windows/hardware/ff567918) structure to initiate service activation in order to gain access to the provider's network when they have completed the transaction.

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

[**NDIS\_WWAN\_SERVICE\_ACTIVATION**](https://msdn.microsoft.com/library/windows/hardware/ff567918)

[**NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION**](ndis-status-wwan-service-activation.md)

[MB Service Detection and Activation](https://msdn.microsoft.com/library/windows/hardware/ff559122)

 

 




