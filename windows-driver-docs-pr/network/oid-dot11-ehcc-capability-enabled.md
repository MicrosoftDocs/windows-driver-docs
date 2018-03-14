---
title: OID_DOT11_EHCC_CAPABILITY_ENABLED
author: windows-driver-content
description: OID_DOT11_EHCC_CAPABILITY_ENABLED
ms.assetid: 3c930dd2-3351-4c3d-911c-8e4aabd1ac91
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_EHCC_CAPABILITY_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_EHCC\_CAPABILITY\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_EHCC\_CAPABILITY\_ENABLED object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11d **dot11EHCCCapabilityEnabled** management information base (MIB) object for the current PHY type on the 802.11 station.

This MIB object specifies whether the frequency-hopping spread spectrum (FHSS) PHY is capable of enabling the hyperbolic congruence codes (HCC) or extended hyperbolic congruence codes (EHCC) algorithms to generate hopping patterns. For more information about the HCC/EHCC algorithms, refer to Clause 9.9.2.1 of the IEEE 802.11d-2001 standard.

This MIB object does not explicitly enable the use of these algorithms. The IEEE 802.11d **dot11HopAlgorithmAdopted** MIB object enables or disables the use of these algorithms to generate hopping patterns. For more information about the **dot11HopAlgorithmAdopted** MIB object, see [OID\_DOT11\_HOP\_ALGORITHM\_ADOPTED](oid-dot11-hop-algorithm-adopted.md).

**Note**  Support for OID\_DOT11\_EHCC\_CAPABILITY\_ENABLED is mandatory if the NIC supports the **dot11\_phy\_type\_fhss** PHY type and more than one regulatory domain. For more information about how the miniport driver specifies its list of supported PHY types, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

 

The data type for OID\_DOT11\_EHCC\_CAPABILITY\_ENABLED is a BOOLEAN value. A value of **TRUE** indicates that the current PHY type is capable of enabling the HCC/EHCC algorithms.

When queried by OID\_DOT11\_EHCC\_CAPABILITY\_ENABLED, the miniport driver fails the request under the following conditions:

-   The **dot11EHCCCapabilityEnabled** MIB object is valid for only the FHSS PHY type. If the current PHY type is not set to **dot11\_phy\_type\_fhss**, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

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

 

 




