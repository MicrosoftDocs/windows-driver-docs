---
title: OID_DOT11_CURRENT_TX_POWER_LEVEL
author: windows-driver-content
description: OID_DOT11_CURRENT_TX_POWER_LEVEL
ms.assetid: 082c900c-9037-4c16-8c42-6896b762c9be
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_TX_POWER_LEVEL Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_TX\_POWER\_LEVEL


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_CURRENT\_TX\_POWER\_LEVEL object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11CurrentTxPowerLevel** management information base (MIB) object for the current PHY type on the 802.11 station.

This MIB object specifies the power level of the current PHY type. Depending upon the PHY type, this MIB object can be used to determine the receiver sensitivity requirements for the PHY's clear channel assessment (CCA) mechanism.

The data type for OID\_DOT11\_CURRENT\_TX\_POWER\_LEVEL is a ULONG value from 1 through 8.

The current TX power level for the current PHY type in use must be within the range of TX power levels previously specified by the miniport driver when queried by [OID\_DOT11\_SUPPORTED\_POWER\_LEVELS](oid-dot11-supported-power-levels.md).

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

 

 




