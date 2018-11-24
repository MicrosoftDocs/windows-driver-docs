---
title: NDIS_STATUS_PM_HARDWARE_CAPABILITIES
description: The NDIS_STATUS_PM_HARDWARE_CAPABILITIES status indicates to overlying drivers that a change in the power management (PM) hardware capabilities of a network adapter has occurred.
ms.assetid: A4AACA48-DCD2-44FA-B016-52C37EE9A1D6
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PM_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PM\_HARDWARE\_CAPABILITIES


The **NDIS\_STATUS\_PM\_HARDWARE\_CAPABILITIES** status indicates to overlying drivers that a change in the power management (PM) hardware capabilities of a network adapter has occurred.

Remarks
-------

The miniport driver generates an **NDIS\_STATUS\_PM\_HARDWARE\_CAPABILITIES** status indication when an update to the previously reported power management capabilities is required.

The miniport driver for an 802.11 network adapter can generate this status indication.

A MUX intermediate driver that provides load balancing failover (LBFO) support can also generate this status indication. The MUX driver aggregates the PM capabilities of the underlying network adapters that are part of the LBFO team. If the PM capabilities change because an adapter has been either added or removed from the team, the MUX driver must generate this status indication. For more information on LBFO MUX intermediate drivers, see [NDIS MUX Intermediate Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566498).

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a pointer to an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure with the updated power management capabilities.

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
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

 

 




