---
title: NDIS_STATUS_WWAN_CONTEXT_STATE
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_CONTEXT_STATE notification to send an event notification when the activation state of a particular context changes.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_CONTEXT_STATE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_CONTEXT\_STATE


Miniport drivers use the NDIS\_STATUS\_WWAN\_CONTEXT\_STATE notification to send an event notification when the activation state of a particular context changes.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_CONTEXT\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_context_state) structure.

## Remarks

Miniport drivers must also notify the MB Service when context state changes are not caused as a result of a *set* request from the MB Service. For example, miniport drivers must notify the MB Service if the network deactivates a context. Miniport drivers should not implement network initiated context activations.

Miniport drivers must notify Windows directly about all applicable context state changes, such as when processing NDIS\_STATUS\_WWAN\_PACKET\_SERVICE or NDIS\_STATUS\_WWAN\_REGISTER\_STATE status notifications.

Miniport drivers of MB devices that support separate voice and data connections must follow these guidelines:

-   At the time of initialization, the VoiceCallState must be set to WwanVoiceCallStateNone.

-   On the start of the voice call, send an event notification with VoiceCallState set to WwanVoiceCallStateInProgress. All the other members must reflect their current state. In case of no active connection during the voice call, the ConnectionId should be set to "0" .

-   Once the voice call is completed, send an event notification with VoiceCallState set to WwanVoiceCallStateHangUp. All the other members must reflect their current state. In case of no active connection during the voice call hang up, the ConnectionId should be set to "0". After this event, the VoiceCallState must be set to **WwanVoiceCallStateNone** in the miniport driver.

## Requirements

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_CONTEXT\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_context_state)

[OID\_WWAN\_PROVISIONED\_CONTEXTS](oid-wwan-provisioned-contexts.md)

 

