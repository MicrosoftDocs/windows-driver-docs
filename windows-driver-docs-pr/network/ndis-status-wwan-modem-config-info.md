---
title: NDIS_STATUS_WWAN_MODEM_CONFIG_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_MODEM_CONFIG_INFO notification to inform the MB service about the completion of a previous OID_WWAN_MODEM_CONFIG_INFO query request.
ms.assetid: 9D56BCE1-2CCF-4BD0-A646-4510642EB08A
keywords: ["NDIS_STATUS_WWAN_MODEM_CONFIG_INFO, Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_WWAN_MODEM_CONFIG_INFO
api_location:
- ndis.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# NDIS_STATUS_WWAN_MODEM_CONFIG_INFO


MBB drivers use the **NDIS_STATUS_WWAN_MODEM_CONFIG_INFO** notification to inform the MB service about the completion of a previous [OID_WWAN_MODEM_CONFIG_INFO](oid-wwan-modem-config-info.md) query request.

MBB drivers must only send an unsolicited **NDIS_STATUS_WWAN_MODEM_CONFIG_INFO** when the configuration state of the modem has changed.

This notification uses the [**NDIS_WWAN_MODEM_CONFIG_INFO**](https://msdn.microsoft.com/library/windows/hardware/07C2BAED-157A-459C-B558-115C0091ECE5) structure.

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
<td><p>Windows 10, version 1709</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID_WWAN_MODEM_CONFIG_INFO](oid-wwan-modem-config-info.md)

[**NDIS_WWAN_MODEM_CONFIG_INFO**](https://msdn.microsoft.com/library/windows/hardware/07C2BAED-157A-459C-B558-115C0091ECE5)
 

