---
title: OID\_DOT11\_COUNTRY\_STRING
author: windows-driver-content
description: OID\_DOT11\_COUNTRY\_STRING
ms.assetid: 17942342-0983-46ff-a1ed-f1a37a097010
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_COUNTRY_STRING Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_COUNTRY\_STRING


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_COUNTRY\_STRING object identifier (OID) requests that the miniport driver return the value of the **dot11CountryString** management information base (MIB) object.

**Note**  Support for OID\_DOT11\_COUNTRY\_STRING is mandatory if the 802.11 station supports more than one regulatory domain. For more information about how the miniport driver specifies its support for regulatory domains, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](oid-dot11-multi-domain-capability-implemented.md).

 

The data type for OID\_DOT11\_COUNTRY\_STRING is the [**DOT11\_COUNTRY\_STRING**](dot11-country-string.md) structure.

The 802.11 station sets the **dot11CountryString** MIB object from the value of the Country Information Element (IE) from the 802.11 Beacon or Probe Response frames received within the basic service set (BSS) network to which the station has connected. For more information about this IE, refer to Clause 7.3.2.12 of the IEEE 802.1d-2001 standard.

When queried by OID\_DOT11\_COUNTRY\_STRING, the miniport driver must fail the request under the following conditions:

-   If the miniport driver does not support more than one regulatory domain, it must fail the query request by returning NDIS\_STATUS\_BAD\_VERSION from its [*MiniportOidRequest*](miniportoidrequest.md) function. The miniport driver specifies its support of regulatory domains in response to queries of [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](oid-dot11-multi-domain-capability-implemented.md).

-   If the miniport driver supports more than one regulatory domain, but this capability is currently disabled, it must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](miniportoidrequest.md) function. The miniport driver specifies the status of the multiple regulatory domain support in response to queries of [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED](oid-dot11-multi-domain-capability-enabled.md).

-   If the 802.11 station is performing a scan request, the miniport driver must fail the query request by returning NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE from its [*MiniportOidRequest*](miniportoidrequest.md) function. For more information about scan requests, see [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md).

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_COUNTRY_STRING%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


