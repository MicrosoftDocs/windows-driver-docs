---
title: Regulatory Domain Configuration
description: Regulatory Domain Configuration
ms.assetid: 53fae694-976f-4d5b-b576-97c98e7e0ca4
keywords:
- configurations WDK Native 802.11 , regulatory domain
- regulatory domain WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Regulatory Domain Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

An 802.11 regulatory domain specifies:

-   The number of channels supported within the domain.

-   The radio frequency of each channel.

The following object identifiers (OIDs) set or query the regulatory domain configuration of the 802.11 station.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_COUNTRY_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569123)</p></td>
<td align="left"><p>Queries the regulatory domain (identified by an IEEE 802.11 country string) in which the 802.11 station is operating.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CURRENT_REG_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136)</p></td>
<td align="left"><p>Sets or queries the current regulatory domain used by the physical media dependent (PMD) sublayer of the PHY on the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_DESIRED_COUNTRY_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569143)</p></td>
<td align="left"><p>Sets or queries the IEEE 802.11d country string used by the 802.11 station whenever it performs one of the following:</p>
<ul>
<li><p>Starts an independent basic service set (IBSS) network during a connection operation. For more information, see [Connection Operations](connection-operations.md).</p>
<div class="alert">
<strong>Note</strong>  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).
</div>
<div>
 
</div></li>
<li><p>A scan operation. For more information, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_MULTI_DOMAIN_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569389)</p></td>
<td align="left"><p>Queries the list of attributes for all regulatory domains supported by the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_MULTI_DOMAIN_CAPABILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390)</p></td>
<td align="left"><p>Sets or queries whether the 802.11 station can operate in multiple regulatory domains.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_MULTI_DOMAIN_CAPABILITY_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569391)</p></td>
<td align="left"><p>Queries whether the 802.11 station supports interoperability within multiple regulatory domains as defined in the IEEE 802.11d-2001 standard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_REG_DOMAINS_SUPPORT_VALUE](https://msdn.microsoft.com/library/windows/hardware/ff569408)</p></td>
<td align="left"><p>Queries the list of regulatory domains supported by the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_COUNTRY_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569421)</p></td>
<td align="left"><p>Queries the list of regulatory domains (as identified by IEEE 802.11d country strings) supported by the 802.11 station.</p></td>
</tr>
</tbody>
</table>

 

If the 802.11 station supports multiple regulatory domains, the miniport driver and 802.11 station must follow these guidelines:

-   If the 802.11 station supports the IEEE 802.11d-2001 standard, the miniport driver must always return a value of **TRUE** when [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569391) is queried.

-   If the 802.11 station has enabled 802.11d support for interoperability with multiple regulatory domains, the miniport driver must return a value of **TRUE** when [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390) is queried.

    In this mode, the 802.11 station dynamically determines the regulatory domain it operates in through the 802.11 frame formats that are defined in Clause 7 of the IEEE 802.11d-2001 standard. The miniport driver must return a value of DOT11\_REG\_DOMAIN\_OTHER when [OID\_DOT11\_CURRENT\_REG\_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136) is queried.

-   If the 802.11 station has disabled interoperability with multiple regulatory domains, the miniport driver must return a value of **FALSE** when [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390) is queried.

    In this mode, the 802.11 station statically configures the regulatory domain based on the value of the IEEE 802.11 **dot11CurrentRegDomain** MIB object. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_REG\_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136).

 

 





