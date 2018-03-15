---
title: OID_DOT11_RANDOM_TABLE_FLAG
author: windows-driver-content
description: OID_DOT11_RANDOM_TABLE_FLAG
ms.assetid: d8a42690-dd37-494f-b06a-04364a3f9637
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_RANDOM_TABLE_FLAG Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_RANDOM\_TABLE\_FLAG


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_RANDOM\_TABLE\_FLAG object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11d **dot11RandomTableFlag** MIB object for the current PHY type on the 802.11 station.

The **dot11RandomTableFlag** MIB object specifies whether the current PHY type uses hopping patterns from the Random Table field of the Hopping Pattern Table information element (IE). For more information about this IE, refer to Clause 7.3.2.14 of the IEEE 802.11d-2001 standard.

**Note**  Support for OID\_DOT11\_RANDOM\_TABLE\_FLAG is mandatory if the NIC supports the **dot11\_phy\_type\_fhss** PHY type and more than one regulatory domain. For more information about how the miniport driver specifies its list of supported PHY types, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

 

The data type for OID\_DOT11\_RANDOM\_TABLE\_FLAG is a BOOLEAN value.

If the **dot11RandomTableFlag** MIB object is **TRUE**, the 802.11 station determines its hopping patterns from the Random Table field of the Hopping Pattern Table IE. If **dot11RandomTableFlag** is **FALSE**, the 802.11 station determines its hopping patterns through the Hop Index Method as defined in Clause 9.9.2.1 of the IEEE 802.11d-2001 standard.

When queried by OID\_DOT11\_RANDOM\_TABLE\_FLAG, the miniport driver fails the request under the following conditions:

-   The **dot11RandomTableFlag** MIB object is valid for only the frequency-hopping spread spectrum (FHSS) PHY type. If the current PHY type is not set to dot11\_phy\_type\_fhss, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the IEEE 802.11d **dot11MultiDomainCapabilityImplemented** MIB object is **FALSE**, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about the **dot11MultiDomainCapabilityImplemented** MIB object, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](oid-dot11-multi-domain-capability-implemented.md).

-   If the IEEE 802.11d **dot11MultiDomainCapabilityEnabled** MIB object is **FALSE**, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about the **dot11MultiDomainCapabilityEnabled** MIB object, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED](oid-dot11-multi-domain-capability-enabled.md).

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

**Note**  A Native 802.11 miniport driver that is designed to run on the Windows Vista or Windows Server 2008 operating systems must always reset this 802.11 MIB OID to its default value. This is the case regardless of the value of the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure. This requirement applies to a miniport driver that, in a call to the **NdisMSetMiniportAttributes** function, sets **MiniportAttributes** -&gt; **Native\_802\_11\_Attributes** -&gt; **Header** -&gt; **Revision** to NDIS\_MINIPORT\_ADAPTER\_802\_11\_ATTRIBUTES\_REVISION\_1.

 

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 MIB OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560645)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




