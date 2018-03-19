---
title: OID_DOT11_RF_USAGE
author: windows-driver-content
description: OID_DOT11_RF_USAGE
ms.assetid: 69fd1e3b-9e6c-4420-af7f-ef4b10f03546
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_RF_USAGE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_RF\_USAGE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_RF\_USAGE object identifier (OID) requests that the miniport driver return the radio frequency (RF) usage detected on the wireless media by the current PHY type on the 802.11 station.

The data type for this OID is a ULONG value that represents the percentage of RF usage.

When OID\_DOT11\_RF\_USAGE is queried, the miniport driver reports how busy the wireless media is. The 802.11 station must start gathering RF usage data after the PHY is turned on. The 802.11 station must clear its RF usage data after each query of OID\_DOT11\_RF\_USAGE.

For more information about how to determine the RF usage of the wireless media, including physical carrier-sense and virtual carrier-sense methods, refer to clause 9.3.2.1 (for DCF operations) and clause 9.4 (for PCF operations) of the IEEE 802.11-2012 standard.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** management information base (MIB) object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about the ExtSTA **msDot11CurrentPhyID** MIB object, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

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

 

 




