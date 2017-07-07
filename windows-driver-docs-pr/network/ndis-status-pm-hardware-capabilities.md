---
title: NDIS\_STATUS\_PM\_HARDWARE\_CAPABILITIES
description: The NDIS\_STATUS\_PM\_HARDWARE\_CAPABILITIES status indicates to overlying drivers that a change in the power management (PM) hardware capabilities of a network adapter has occurred.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A4AACA48-DCD2-44FA-B016-52C37EE9A1D6
keywords: ["NDIS_STATUS_PM_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_PM_HARDWARE_CAPABILITIES
api_location:
- Ndis.h
api_type:
- HeaderDef
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_PM_HARDWARE_CAPABILITIES%20%20RELEASE:%20%287/6/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





