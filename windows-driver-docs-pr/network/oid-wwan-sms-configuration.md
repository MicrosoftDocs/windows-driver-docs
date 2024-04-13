---
title: OID_WWAN_SMS_CONFIGURATION
ms.topic: reference
description: OID_WWAN_SMS_CONFIGURATION sets or returns a MB device's SMS text message configuration.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SMS_CONFIGURATION Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SMS\_CONFIGURATION


OID\_WWAN\_SMS\_CONFIGURATION sets or returns a MB device's SMS text message configuration.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION**](ndis-status-wwan-sms-configuration.md) status notification regardless of completing set or query requests.

Query requests return the MB device's current SMS text message configuration stored in the device or Subscriber Identity Module (SIM) card.

Set requests use the [**NDIS\_WWAN\_SET\_SMS\_CONFIGURATION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sms_configuration) structure to change the SMS text message configuration of the MB device.

## Remarks

For more information about using this OID, see [WWAN SMS Operations](./mb-sms-operations.md).

When processing this OID, miniport drivers can access the SIM card, but should not access the provider network.

Miniport drivers of GSM-based devices should support both query and set operations. Miniport drivers of CDMA-based devices should support only query operations. Miniport drivers of CDMA-based devices should return a valid value in the **ulMaxMessageIndex** member of the WWAN\_SMS\_CONFIGURATION structure for query requests and can ignore the other members.

Miniport drivers must send an unsolicited NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION indication when the MB device's SMS subsystem is ready for SMS operation. Thereafter, when responding to OID\_WWAN\_SMS\_CONFIGURATION query requests, miniport drivers must return valid values for all members of the WWAN\_SMS\_CONFIGURATION structure.

Miniport drivers should return NDIS\_STATUS\_NOT\_INITIALIZED if the device is initialized but the SMS subsystem is not yet initialized.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support configuring SMS text messages.

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_SET\_SMS\_CONFIGURATION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sms_configuration)

[**NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION**](ndis-status-wwan-sms-configuration.md)

[WWAN SMS Operations](./mb-sms-operations.md)

 

