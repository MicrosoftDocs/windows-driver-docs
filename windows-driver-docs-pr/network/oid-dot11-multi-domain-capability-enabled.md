---
title: OID_DOT11_MULTI_DOMAIN_CAPABILITY_ENABLED
author: windows-driver-content
description: OID_DOT11_MULTI_DOMAIN_CAPABILITY_ENABLED
ms.assetid: 3d2431b6-02b8-4a4c-88fb-6d3387fe6918
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_MULTI_DOMAIN_CAPABILITY_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED object identifier (OID) requests that the miniport driver set the IEEE 802.11d **dot11MultiDomainCapabilityEnabled** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **dot11MultiDomainCapabilityEnabled** MIB object.

**Note**  Support for OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED is mandatory if the 802.11 station supports more than one regulatory domain and the IEEE 802.11 **dot11MultiDomainCapabilityImplemented** MIB object is **TRUE**. For more information about this MIB object, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](oid-dot11-multi-domain-capability-implemented.md).

 

The data type for OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED is a BOOLEAN value.

If the **dot11MultiDomainCapabilityEnabled** MIB object is **TRUE**, the 802.11 station can operate in multiple regulatory domains. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_REG\_DOMAIN](oid-dot11-current-reg-domain.md).

The 802.11 station operates in multiple regulatory domains in the following way:

-   If the **dot11CurrentRegDomain** MIB object is set to DOT11\_REG\_DOMAIN\_OTHER, the 802.11 station operates dynamically in multiple regulatory domains through the procedures and protocols defined by the IEEE 802.11d-2001 standard.

-   If the **dot11CurrentRegDomain** MIB object is not set DOT11\_REG\_DOMAIN\_OTHER, the 802.11 station only operates within the regulatory domain as specified by the MIB object.

    In this situation, the value of the **dot11CurrentRegDomain** MIB object defines the default regulatory domain of the 802.11 station. For more information about the default regulatory domain, see [OID\_DOT11\_CURRENT\_REG\_DOMAIN](oid-dot11-current-reg-domain.md).

    **Note**  The default regulatory domain can only be changed while the miniport driver is operating in the initialization (INIT) state. For more information about this state, see [Native 802.11 Operating States](https://msdn.microsoft.com/library/windows/hardware/ff560664).

     

If the **dot11MultiDomainCapabilityEnabled** MIB object is **FALSE**, the 802.11 station can only operate in its default regulatory domain.

The miniport driver fails a set or query of OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED under the following conditions:

-   If the **dot11MultiDomainCapabilityImplemented** MIB object is **FALSE**, the 802.11 station does not support multiple regulatory domains. In this situation, the miniport driver must return NDIS\_STATUS\_BAD\_VERSION from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about the **dot11MultiDomainCapabilityImplemented** MIB object, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](oid-dot11-multi-domain-capability-implemented.md).

-   If the **dot11MultiDomainCapabilityImplemented** MIB object is **TRUE** and the 802.11 station does not support a default regulatory domain, it must fail the set request if the specified value of the **dot11MultiDomainCapabilityEnabled** MIB object is **FALSE**. The miniport driver must return NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the 802.11 has not completed an explicit scan initiated through a set of [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md), the miniport driver must return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

The default value for the **dot11MultiDomainCapabilityEnabled** MIB object is **FALSE**. The miniport driver must set this MIB object to this default when one of the following occurs:

-   The miniport driver initializes the current PHY type through its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

If the miniport driver supports the functionality of multiple MAC entities through [virtualization](https://msdn.microsoft.com/library/windows/hardware/ff571041), the driver should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE if the medium is blocked by another MAC.

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

 

 




