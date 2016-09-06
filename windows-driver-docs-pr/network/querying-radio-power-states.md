---
title: Querying Radio Power States
description: Querying Radio Power States
ms.assetid: fb69af55-ff9f-4f6e-b4be-0aa1cef9089c
keywords: ["radio power management WDK Native 802.11 miniport", "querying power state"]
---

# Querying Radio Power States


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following Native 802.11 object identifiers (OIDs) query the power state of the radio on the 802.11 NIC:

<a href="" id="oid-dot11-nic-power-state"></a>[OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392)  
This OID returns the current software setting for the NIC's radio power state.

<a href="" id="oid-dot11-hardware-phy-state"></a>[OID\_DOT11\_HARDWARE\_PHY\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569370)  
This OID returns the status of the hardware setting that controls the radio power on the NIC. When OID\_DOT11\_HARDWARE\_PHY\_STATE is queried, the miniport driver returns the hardware setting based on the conditions described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Returned hardware setting</th>
<th align="left">Condition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Enabled</p></td>
<td align="left"><p>Either a hardware setting is not present on the NIC or the setting is enabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Disabled</p></td>
<td align="left"><p>A hardware setting is present on the NIC and is disabled.</p></td>
</tr>
</tbody>
</table>

 

**Note**  [OID\_DOT11\_HARDWARE\_PHY\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569370) is only supported when a miniport driver is operating in the Extensible Station (ExtSTA) mode.

 

If the miniport driver is operating in ExtSTA mode, the driver returns the power state of the PHY referenced through the current PHY identifier (ID). The operating system sets or queries the current PHY ID through [OID\_DOT11\_CURRENT\_PHY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135). For more information about the method used to reference PHYs within the ExtSTA operation mode, see [802.11 PHY Configuration](802-11-phy-configuration.md).

 

 





