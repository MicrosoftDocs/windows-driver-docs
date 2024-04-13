---
title: NDIS_STATUS_WWAN_IP_ADDRESS_STATE
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_IP_ADDRESS_STATE notification to inform the MB service about changes to the IP configuration for an additional PDP context.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WWAN_IP_ADDRESS_STATE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_IP\_ADDRESS\_STATE


Miniport drivers use the NDIS\_STATUS\_WWAN\_IP\_ADDRESS\_STATE notification to inform the MB service about changes to the IP configuration for an additional PDP context.

This notification uses the [**NDIS\_WWAN\_IP\_ADDRESS\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_ip_address_state) structure.

## Remarks

This notification must be sent on the NDIS port associated with the additional PDP context session.

Miniport drivers should send this notification after an additional PDP context has been successfully activated and the IP configuration has been acquired for that context. If the device indicates unsolicited IP configuration changes post-context activation, then miniport drivers should send an unsolicited indication with this notification with the updated IP configuration.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 8.1 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_IP\_ADDRESS\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_ip_address_state)

 

