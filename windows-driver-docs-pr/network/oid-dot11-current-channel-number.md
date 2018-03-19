---
title: OID_DOT11_CURRENT_CHANNEL_NUMBER
author: windows-driver-content
description: OID_DOT11_CURRENT_CHANNEL_NUMBER
ms.assetid: e4f5cea0-54f8-44cb-99d4-05a4e711d199
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_CHANNEL_NUMBER Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_CHANNEL\_NUMBER


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_CURRENT\_CHANNEL\_NUMBER object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11CurrentChannelNumber** management information base (MIB) object for the current PHY type on the 802.11 station.

The **dot11CurrentChannelNumber** MIB object stores the current channel number used by the physical media dependent (PMD) sublayer of the current PHY type for transmit and receive operations. For more information about channel numbers, refer to Clause 14.9.2.17 of the IEEE 802.11-2012 standard.

**Note**  Support for OID\_DOT11\_CURRENT\_CHANNEL\_NUMBER is mandatory if the NIC supports the **dot11\_phy\_type\_fhss** PHY type. For more information about how the miniport driver specifies its list of supported PHY types, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

 

The data type for OID\_DOT11\_CURRENT\_CHANNEL\_NUMBER is a ULONG value that specifies the channel number from 0 through 99.

The **dot11CurrentChannelNumber** MIB object is only valid for the frequency-hopping spread spectrum (FHSS) PHY type. If the current PHY type is not set to **dot11\_phy\_type\_fhss**, the miniport driver must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

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

 

 




