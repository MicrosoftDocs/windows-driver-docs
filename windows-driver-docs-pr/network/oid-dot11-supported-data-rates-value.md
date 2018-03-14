---
title: OID_DOT11_SUPPORTED_DATA_RATES_VALUE
author: windows-driver-content
description: OID_DOT11_SUPPORTED_DATA_RATES_VALUE
ms.assetid: 5daf34be-bbbf-4aca-818d-6db24aa15cd4
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SUPPORTED_DATA_RATES_VALUE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_DATA\_RATES\_VALUE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_DATA\_RATES\_VALUE OID requests that the miniport driver return the following for the current PHY type on the 802.11 station:

-   The transmit data rates supported by the Physical Layer Convergence Procedure (PLCP) and Physical Media Dependent (PMD) sublayer of the PHY.

-   The receive data rates supported by the PLCP and PMD of the PHY.

The data type for OID\_DOT11\_SUPPORTED\_DATA\_RATES\_VALUE is the [**DOT11\_SUPPORTED\_DATA\_RATES\_VALUE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548790) structure.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** management information base (MIB) object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

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

 

 




