---
title: OID_DOT11_HIDDEN_NETWORK_ENABLED
author: windows-driver-content
description: OID_DOT11_HIDDEN_NETWORK_ENABLED
ms.assetid: ecbcc751-3c05-464e-adee-d07463bc3b1b
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_HIDDEN_NETWORK_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_HIDDEN\_NETWORK\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_HIDDEN\_NETWORK\_ENABLED object identifier (OID) requests that the miniport driver enable the 802.11 station's ability to access an infrastructure network that includes hidden access points (APs). Hidden APs do not broadcast their SSIDs.

When queried, this OID requests that the miniport driver return the value of the **msDot11HiddenNetworkEnabled** MIB object.

The data type for this OID is a Boolean value.

An OID value of **TRUE** indicates that the infrastructure network might contain APs that do not broadcast their SSIDs. The NIC might include the desired SSID in the probe request transmitted during roaming scanning.

An OID value of **FALSE** indicates that the NIC must assume that all APs in the infrastructure network will broadcast their SSIDs. The default OID value is **FALSE**.

This OID only applies to situations where the NIC connects to an infrastructure network. When resuming from standby or hibernation and the OID value is **FALSE**, the NIC must use the wildcard SSID in the probe requests until it determines a set of visible candidate APs. In normal roaming cases that do not involve standby or hibernation, the NIC can choose its own probe requests. APs cached prior to standby or hibernation are considered hidden unless the NIC can see their packets after waking up.

The miniport driver must fail a set request with error code NDIS\_STATUS\_INVALID\_STATE if the 802.11 station is in any state except the initialization (INIT) state.

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

 

 




