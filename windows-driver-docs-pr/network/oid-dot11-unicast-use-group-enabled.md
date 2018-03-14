---
title: OID_DOT11_UNICAST_USE_GROUP_ENABLED
author: windows-driver-content
description: OID_DOT11_UNICAST_USE_GROUP_ENABLED
ms.assetid: 4ba327e9-0404-43ed-a45f-7a60e1c1892d
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_UNICAST_USE_GROUP_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_UNICAST\_USE\_GROUP\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_UNICAST\_USE\_GROUP\_ENABLED object identifier (OID) requests that the miniport driver set the Extensible Station (ExtSTA) **msDot11UnicastUseGroupEnabled** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **msDot11UnicastUseGroupEnabled** MIB object.

The **msDot11UnicastUseGroupEnabled** MIB object specifies whether the 802.11 station has enabled the support for the "Use Group Key" cipher suite. For more information about the "Use Group Key" cipher suite, refer to Clause 7.3.2.9.1 of the IEEE 802.11i-2004 standard.

**Note**  Support for OID\_DOT11\_UNICAST\_USE\_GROUP\_ENABLED is mandatory if the 802.11 station supports any Wi-Fi Protected Access (WPA) or Robust Security Network Association (RSNA) authentication algorithms. The miniport driver specifies its support for this authentication algorithm when [OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](oid-dot11-supported-unicast-algorithm-pair.md) or [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) are queried.

 

The data type for OID\_DOT11\_UNICAST\_USE\_GROUP\_ENABLED is a BOOLEAN value. A value of **TRUE** indicates that the 802.11 station has enabled the support for the "Use Group Key" cipher suite.

"Use Group Key" is a cipher suite defined for the Pairwise Key Cipher Suite List subfield of the RSN and WPA information elements (IEs). An access point (AP) uses this cipher suite if it does not support the use of a pairwise cipher algorithm for unicast packets. The AP advertises this cipher suite in the RSN and WPA IE that it sends in its Beacon and Probe Response frames. An 802.11 station that associates with the AP must use the "Use Group Key" cipher suite defined in the RSN or WPA IE for unicast packets.

The 802.11 station can associate only with an AP that advertises the "Use Group Key" cipher suite if the following are true:

-   The 802.11 station has enabled the support for the "Use Group Key" cipher suite.

-   The 802.11 station has enabled the multicast cipher suite advertised in the Beacon or Probe Response received from the AP.

The default for the **msDot11UnicastUseGroupEnabled** MIB object is **TRUE**. The miniport driver must set this MIB object to its default if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the media access control (MAC) layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

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


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




