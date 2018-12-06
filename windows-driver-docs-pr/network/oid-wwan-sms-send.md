---
title: OID_WWAN_SMS_SEND
description: OID_WWAN_SMS_SEND sends SMS text messages to another MB device.
ms.assetid: 557d2bdc-8414-4fcb-903c-23bb68955d07
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SMS_SEND Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




