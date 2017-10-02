---
title: OID_WWAN_SMS_CONFIGURATION
author: windows-driver-content
description: OID\_WWAN\_SMS\_CONFIGURATION sets or returns a MB device's SMS text message configuration.
ms.assetid: 3292a91d-4aa8-4c57-9223-d7d984dc5d69
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_SMS_CONFIGURATION Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SMS\_CONFIGURATION


OID\_WWAN\_SMS\_CONFIGURATION sets or returns a MB device's SMS text message configuration.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION**](ndis-status-wwan-sms-configuration.md) status notification regardless of completing set or query requests.

Query requests return the MB device's current SMS text message configuration stored in the device or Subscriber Identity Module (SIM) card.

Set requests use the [**NDIS\_WWAN\_SET\_SMS\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff567929) structure to change the SMS text message configuration of the MB device.

Remarks
-------

For more information about using this OID, see [WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131).

When processing this OID, miniport drivers can access the SIM card, but should not access the provider network.

Miniport drivers of GSM-based devices should support both query and set operations. Miniport drivers of CDMA-based devices should support only query operations. Miniport drivers of CDMA-based devices should return a valid value in the **ulMaxMessageIndex** member of the WWAN\_SMS\_CONFIGURATION structure for query requests and can ignore the other members.

Miniport drivers must send an unsolicited NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION indication when the MB device's SMS subsystem is ready for SMS operation. Thereafter, when responding to OID\_WWAN\_SMS\_CONFIGURATION query requests, miniport drivers must return valid values for all members of the WWAN\_SMS\_CONFIGURATION structure.

Miniport drivers should return NDIS\_STATUS\_NOT\_INITIALIZED if the device is initialized but the SMS subsystem is not yet initialized.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support configuring SMS text messages.

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


[**NDIS\_WWAN\_SET\_SMS\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff567929)

[**NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION**](ndis-status-wwan-sms-configuration.md)

[WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SMS_CONFIGURATION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


