---
title: Standardized INF Keywords for Power Management
description: Standardized INF Keywords for Power Management
ms.date: 01/29/2021
ms.localizationpriority: medium
ms.custom: contperf-fy21q3
---

# Standardized INF Keywords for Power Management

The power management standardized keywords are defined in the device driver INF file. The operating system reads these standardized keywords and adjusts the current power management capabilities of the device. 

Both [Network Adapter WDF Class Extension (NetAdapterCx)](../netcx/index.md) client drivers and traditional NDIS miniport device drivers use these power management keywords. However, some keywords are used exclusively by NetAdapterCx drivers while others are used exclusively by NDIS drivers as the following sections describe:

* [Power management keywords for NetAdapterCx and NDIS](#power-management-keywords-for-netadaptercx-and-ndis)

* [Power management keywords exclusive to NetAdapterCx](#power-management-keywords-exclusive-to-netadaptercx)

* [Power management keywords exclusive to NDIS](#power-management-keywords-exclusive-to-ndis)

The traditional NDIS miniport device driver should always indicate the device's hardware power management capabilities to NDIS in the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure.

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## Power management keywords for NetAdapterCx and NDIS

The following standardized INF keywords are defined to enable or disable support for power management features of network adapters. They are used by both NetAdapterCx client drivers and traditional NDIS miniport device drivers.

<a href="" id="-wakeonpattern"></a>**\*WakeOnPattern**  
A value that describes whether the device should be enabled to wake the computer when a network packet matches a specified pattern.

<a href="" id="-wakeonmagicpacket"></a>**\*WakeOnMagicPacket**  
A value that describes whether the device should be enabled to wake the computer when the device receives a *magic packet*. (A *magic packet* is a packet that contains 16 contiguous copies of the receiving network adapter's Ethernet address)

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

The following table describes the possible INF entries for the power management keywords used by NDIS and NetAdapterCx drivers.


|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**_WakeOnPattern_**|Wake on pattern match|0|Disabled|
|||1 (Default)|Enabled|
|**WakeOnMagicPacket**|Wake on magic packet|0|Disabled|
|||1 (Default)|Enabled|
|**PMARPOffload**|ARP offload|0|Disabled|
|||1 (Default)|Enabled|
|**_PMNSOffload_**|NS offload|0|Disabled|
|||1 (Default)|Enabled|
|**PMWiFiRekeyOffload**|WiFi rekeying offload|0|Disabled|
|||1 (Default)|Enabled|
|***EEE**|Energy-Efficient Ethernet|0|Disabled|
|||1 (Default)|Enabled|

## Power management keywords exclusive to NetAdapterCx

The following power management keywords are for NetAdapterCx client driver use only. 

In addition to the standard WDF process for giving user control over the device idle and wake behavior as described in [User Control of Device Idle and Wake Behavior](../wdf/user-control-of-device-idle-and-wake-behavior.md), NetAdapterCx also defines a network device specific standardized INF keyword for allowing more control.

**\*IdleRestriction**  
If a network device has both idle power down and wake on packet filter capabilities, this setting allows the user to decide when the device idle power down can happen.

**\*IdleRestriction** is an enumeration standardized INF keyword and has the following attributes:

The following table describes the possible INF entries for the **\*IdleRestriction** keyword.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**_*IdleRestriction_**|idle power down restriction|0 (Default)|No Restriction|
|||1|Only idle when user is not present|


## Power management keywords exclusive to NDIS

The following power management keywords are for traditional NDIS miniport driver use only. They must not be used by NetAdapterCx client drivers.

<a href="" id="-modernstandbywolmagicpacket"></a>**\*ModernStandbyWoLMagicPacket**  
A value that describes whether the device should be enabled to wake the computer when the device receives a *magic paket* and the system is in the *S0ix* power state. This does not apply when the system is in the *S4* power state.

> [!NOTE]
> **\*ModernStandbyWoLMagicPacket** is supported in NDIS 6.60 and later, or Windows 10, version 1607 and later. 

<a href="" id="-devicesleepondisconnect"></a>**\*DeviceSleepOnDisconnect**  
A value that describes whether the device should be enabled to put the device into a low-power state (sleep state) when media is disconnected and return to a full-power state (wake state) when media is connected again.

The following table describes the possible INF entries for the power management keywords used by NDIS miniport drivers.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**ModernStandbyWoLMagicPacket**|Wake on magic packet when system is in the _S0ix_ power state|0 (Default)|Disabled|
|||1|Enabled|
|**_DeviceSleepOnDisconnect_**|Device sleep on disconnect|0|Disabled|
|||1 (Default)|Enabled|
 

