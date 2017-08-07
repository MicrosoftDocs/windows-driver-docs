---
title: OID\_WWAN\_SMS\_READ
author: windows-driver-content
description: OID\_WWAN\_SMS\_READ reads SMS text messages stored in the MB device, or Subscriber Identity Module (SIM card), or any other auxiliary non-volatile memory or memories.
ms.assetid: f4dbb7e8-1348-4fa8-abac-f644a443df48
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WWAN_SMS_READ Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SMS\_READ


OID\_WWAN\_SMS\_READ reads SMS text messages stored in the MB device, or Subscriber Identity Module (SIM card), or any other auxiliary non-volatile memory or memories.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SMS\_RECEIVE**](ndis-status-wwan-sms-receive.md) status notification containing an [**NDIS\_WWAN\_SMS\_READ**](ndis-wwan-sms-read.md) structure to provide the SMS messages requested that was initially provided by the caller when completing query requests.

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


[**NDIS\_WWAN\_SMS\_READ**](ndis-wwan-sms-read.md)

[WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SMS_READ%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


