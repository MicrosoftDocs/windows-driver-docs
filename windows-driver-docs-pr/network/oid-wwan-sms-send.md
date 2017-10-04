---
title: OID_WWAN_SMS_SEND
author: windows-driver-content
description: OID\_WWAN\_SMS\_SEND sends SMS text messages to another MB device.
ms.assetid: 557d2bdc-8414-4fcb-903c-23bb68955d07
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_SMS_SEND Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SMS\_SEND


OID\_WWAN\_SMS\_SEND sends SMS text messages to another MB device.

Query requests are not supported.

Set requests use the [**NDIS\_WWAN\_SMS\_SEND**](https://msdn.microsoft.com/library/windows/hardware/ff567943) structure.

Miniport drivers process this OID asynchronously, and should return an NDIS\_STATUS\_INDICATION\_REQUIRED provisional response to any set requests. Miniport drivers should send an [**NDIS\_STATUS\_WWAN\_SMS\_SEND**](ndis-status-wwan-sms-send.md) indication when they have completed the transaction.

Remarks
-------

For more information about using this OID, see [WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131).

When processing this OID, miniport drivers can access the provider network, but should not access the Subscriber Identity Module (SIM card).

OID\_WWAN\_SMS\_SEND supports sending both PDU-mode and CDMA-mode SMS text messages, depending on the capabilities of the device.

GSM-based devices are expected to support only PDU-mode SMS text messages. CDMA-based devices are expected to support only CDMA-mode SMS text messages. Miniport drivers must be able to complete set requests irrespective of SMS text message mode.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support SMS text messages, or the ability to send SMS text messages.

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


[**NDIS\_WWAN\_SMS\_SEND**](https://msdn.microsoft.com/library/windows/hardware/ff567943)

[WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SMS_SEND%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


