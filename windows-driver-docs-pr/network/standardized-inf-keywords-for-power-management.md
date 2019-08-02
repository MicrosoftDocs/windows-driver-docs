---
title: Standardized INF Keywords for Power Management
description: Standardized INF Keywords for Power Management
ms.assetid: bec8dd96-f64a-40eb-ade9-73c9a66a756e
ms.date: 08/01/2019
ms.localizationpriority: medium
---

# Standardized INF Keywords for Power Management

The power management standardized keywords are defined in the device driver INF file. The operating system reads these standardized keywords and adjusts the current power management capabilities of the device. The device driver should always indicate the device's hardware power management capabilities to NDIS in the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure.

The following standardized INF keywords are defined to enable or disable support for power management features of network adapters.

<a href="" id="-wakeonpattern"></a>**\*WakeOnPattern**  
A value that describes whether the device should be enabled to wake the computer when a network packet matches a specified pattern.

<a href="" id="-wakeonmagicpacket"></a>**\*WakeOnMagicPacket**  
A value that describes whether the device should be enabled to wake the computer when the device receives a *magic packet*. (A *magic packet* is a packet that contains 16 contiguous copies of the receiving network adapter's Ethernet address)

<a href="" id="-modernstandbywolmagicpacket"></a>**\*ModernStandyWoLMagicPacket**  
A value that describes whether the device should be enabled to wake the computer when the device receives a *magic paket* and the system is in the *S0ix* power state. This does not apply when the system is in the *S4* power state.

> [!NOTE]
> **\*ModernStandyWoLMagicPacket** is supported in NDIS 6.60 and later, or Windows 10, version 1607 and later.

<a href="" id="-devicesleepondisconnect"></a>**\*DeviceSleepOnDisconnect**  
A value that describes whether the device should be enabled to put the device into a low-power state (sleep state) when media is disconnected and return to a full-power state (wake state) when media is connected again.

<a href="" id="-pmarpoffload"></a>**\*PMARPOffload**  
A value that describes whether the device should be enabled to offload the Address Resolution Protocol (ARP) when the system enters a sleep state.

<a href="" id="-pmnsoffload"></a>**\*PMNSOffload**  
A value that describes whether the device should be enabled to offload neighbor solicitation (NS) when the system enters a sleep state.

<a href="" id="-pmwifirekeyoffload"></a>**\*PMWiFiRekeyOffload**  
A value that describes whether the device should be enabled to offload group temporal key (GTK) rekeying for wake-on-wireless-LAN (WOL) when the computer enters a sleep state.

<a href="" id="-eee"></a>**\*EEE**  
A value that describes whether the device should enable IEEE 802.3az Energy-Efficient Ethernet.

The columns in the table at the end of this topic describe the following attributes for enumeration keywords:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each option in the list. This value is stored in **NDI\\params\\**<em>SubkeyName\\Value.</em>

<a href="" id="enumdesc"></a>EnumDesc  
The display text that is associated with each value that appears in the menu.

The following table describes the possible INF entries for the Power Management keywords.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
<th align="left">EnumDesc</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em>WakeOnPattern</strong></p></td>
<td align="left"><p>Wake on pattern match</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>WakeOnMagicPacket</strong></p></td>
<td align="left"><p>Wake on magic packet</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>ModernStandyWoLMagicPacket</strong></p></td>
<td align="left"><p>Wake on magic packet when system is in the <i>S0ix</i> power state</p></td>
<td align="left"><p>0 (Default)</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>DeviceSleepOnDisconnect</strong></p></td>
<td align="left"><p>Device sleep on disconnect</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>PMARPOffload</strong></p></td>
<td align="left"><p>ARP offload</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>PMNSOffload</strong></p></td>
<td align="left"><p>NS offload</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>PMWiFiRekeyOffload</strong></p></td>
<td align="left"><p>WiFi rekeying offload</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*EEE</strong></p></td>
<td align="left"><p>Energy-Efficient Ethernet</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
</tbody>
</table>

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

 

 





