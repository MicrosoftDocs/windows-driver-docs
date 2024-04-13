---
title: NDIS_STATUS_WWAN_PRESHUTDOWN_STATE
ms.topic: reference
description: The NDIS_STATUS_WWAN_PRESHUTDOWN_STATE notification is a one-way notification from the MBB driver to the host.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WWAN_PRESHUTDOWN_STATE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_PRESHUTDOWN\_STATE


The NDIS\_STATUS\_WWAN\_PRESHUTDOWN\_STATE notification is a one-way notification from the MBB driver to the host. The MBB driver sends up this notification when the modem has finished all operations required before shutdown.

This notification uses the [**NDIS\_WWAN\_PRESHUTDOWN\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_preshutdown_state) structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 10, version 1511.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

 

