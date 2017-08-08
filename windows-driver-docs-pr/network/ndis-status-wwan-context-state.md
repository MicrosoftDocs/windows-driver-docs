---
title: NDIS\_STATUS\_WWAN\_CONTEXT\_STATE
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_CONTEXT\_STATE notification to send an event notification when the activation state of a particular context changes.
ms.assetid: 6713f6a3-d1b7-49d0-83e1-50a33e9fff32
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_WWAN_CONTEXT_STATE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_CONTEXT\_STATE


Miniport drivers use the NDIS\_STATUS\_WWAN\_CONTEXT\_STATE notification to send an event notification when the activation state of a particular context changes.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_CONTEXT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567906) structure.

Remarks
-------

Miniport drivers must also notify the MB Service when context state changes are not caused as a result of a *set* request from the MB Service. For example, miniport drivers must notify the MB Service if the network deactivates a context. Miniport drivers should not implement network initiated context activations.

Miniport drivers must notify Windows directly about all applicable context state changes, such as when processing NDIS\_STATUS\_WWAN\_PACKET\_SERVICE or NDIS\_STATUS\_WWAN\_REGISTER\_STATE status notifications.

Miniport drivers of MB devices that support separate voice and data connections must follow these guidelines:

-   At the time of initialization, the VoiceCallState must be set to WwanVoiceCallStateNone.

-   On the start of the voice call, send an event notification with VoiceCallState set to WwanVoiceCallStateInProgress. All the other members must reflect their current state. In case of no active connection during the voice call, the ConnectionId should be set to "0" .

-   Once the voice call is completed, send an event notification with VoiceCallState set to WwanVoiceCallStateHangUp. All the other members must reflect their current state. In case of no active connection during the voice call hang up, the ConnectionId should be set to "0". After this event, the VoiceCallState must be set to **WwanVoiceCallStateNone** in the miniport driver.

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


[**NDIS\_WWAN\_CONTEXT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567906)

[OID\_WWAN\_PROVISIONED\_CONTEXTS](oid-wwan-provisioned-contexts.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_CONTEXT_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


