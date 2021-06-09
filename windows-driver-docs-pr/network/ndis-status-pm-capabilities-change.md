---
title: NDIS_STATUS_PM_CAPABILITIES_CHANGE
description: The NDIS_STATUS_PM_CAPABILITIES_CHANGE status indicates a change in the power management capabilities of a network adapter to overlying drivers.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PM_CAPABILITIES_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE


The NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE status indicates a change in the power management capabilities of a network adapter to overlying drivers.

## Remarks

NDIS generates an NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE status indication when an update to the previously reported power management capabilities is required.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure contains a pointer to an [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure with the updated power management capabilities.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

 

