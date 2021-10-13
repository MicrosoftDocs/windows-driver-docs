---
title: NDIS_STATUS_WWAN_DEVICE_CAPS
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_CAPS notification to respond to OID_WWAN_DEVICE_CAPS query requests. Miniport drivers cannot use this notification to send unsolicited events.This notification uses the NDIS_WWAN_DEVICE_CAPS structure.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_CAPS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_CAPS


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_CAPS notification to respond to [OID\_WWAN\_DEVICE\_CAPS](./oid-wwan-device-caps.md) query requests.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_CAPS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_caps) structure.

## Remarks

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


[OID\_WWAN\_DEVICE\_CAPS](./oid-wwan-device-caps.md)

[**NDIS\_WWAN\_DEVICE\_CAPS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_caps)

 

