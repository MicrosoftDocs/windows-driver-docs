---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS notification to report the completion of a query of OID_WWAN_ENUMERATE_DEVICE_SERVICE_COMMANDS.NDIS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS structure.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS notification to report the completion of a query of [OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS](./oid-wwan-enumerate-device-service-commands.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_supported_commands) structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_ENUMERATE\_DEVICE\_SERVICE\_COMMANDS](./oid-wwan-enumerate-device-service-commands.md)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SUPPORTED\_COMMANDS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_supported_commands)

 

