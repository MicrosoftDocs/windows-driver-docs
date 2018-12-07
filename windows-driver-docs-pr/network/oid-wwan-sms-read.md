---
title: OID_WWAN_SMS_READ
description: OID_WWAN_SMS_READ reads SMS text messages stored in the MB device, or Subscriber Identity Module (SIM card), or any other auxiliary non-volatile memory or memories.
ms.assetid: f4dbb7e8-1348-4fa8-abac-f644a443df48
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SMS_READ Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_SMS\_READ


OID\_WWAN\_SMS\_READ reads SMS text messages stored in the MB device, or Subscriber Identity Module (SIM card), or any other auxiliary non-volatile memory or memories.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SMS\_RECEIVE**](ndis-status-wwan-sms-receive.md) status notification containing an [**NDIS\_WWAN\_SMS\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff567941) structure to provide the SMS messages requested that was initially provided by the caller when completing query requests.

Callers requesting to read SMS text messages provide an NDIS\_WWAN\_SMS\_READ structure to indicate which SMS messages the caller wants the miniport to return.

Remarks
-------

For more information about using this OID, see [WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131).

When processing this OID, miniport drivers can access the Subscriber Identity Module (SIM card), but should not access the provider network.

OID\_WWAN\_SMS\_READ supports reading both PDU-mode and CDMA-mode SMS text messages, depending on the capabilities of the device.

Miniport drivers may receive requests to read SMS text messages based on an index, or to read all SMS text messages. Read requests may consist of any one of the basic filters such as new (unread) messages, old (read) messages, draft messages, or sent messages.

Miniport drivers that implement SMS text message functionality must support the reading of new messages using the basic filter for *WwanSmsFlagNew*. All other filter types are optional to support.

Miniport drivers must logically project a single SMS text message store across all available physically different SMS text message stores.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support SMS text messages.

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


[**NDIS\_WWAN\_SMS\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff567941)

[WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131)

 

 




