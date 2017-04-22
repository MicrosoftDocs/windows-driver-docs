---
title: 802.11 Power Management
description: 802.11 Power Management
ms.assetid: 4c766f9a-b0cf-46e9-a9ad-2fd2f5680562
keywords:
- power management WDK Native 802.11 miniport , settings
- power save polling mode WDK Native 802.11 miniport
- PSP mode WDK Native 802.11 miniport
- constantly awake mode WDK Native 802.11 miniport
- CAM mode WDK Native 802.11 miniport
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# 802.11 Power Management


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Power management for 802.11 stations is defined in Clause 10.2 of the IEEE 802.11-2012 standard. Power management is invoked through the media access control (MAC) layer management entity (MLME) MLME-POWERMGMT.request service primitive, which is defined in Clause 6.3.2 of the IEEE 802.11-2012 standard.

The miniport driver operating in the Extensible Station (ExtSTA) mode invokes the media access control (MAC) layer management entity (MLME) MLME-POWERMGMT.request service primitive through a set of [OID\_DOT11\_POWER\_MGMT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569402).

When OID\_DOT11\_POWER\_MGMT\_REQUEST is set, the miniport driver configures the 802.11 station with the power management settings from the DOT11\_STA\_POWER\_MGMT\_REQUEST structure that accompanies the set request. Power management settings include:

-   Power management mode, such as active or power-save modes.

    When configured in the active mode, also referred to as the constantly awake mode (CAM), the 802.11 station never turns the radio off. The 802.11 station will usually be in this mode if the portable computer is operating from an AC power source.

    When configured in the power-save mode, also referred to as the power save polling (PSP) mode, the 802.11 station periodically turns off the radio. In order to maintain the basic service set (BSS) network connection, the 802.11 station will turn on the radio so that the station can send or receive packets. The 802.11 station will be in this mode if the portable computer is operating from its battery.

    When the power management mode of the 802.11 station is changed, the station must follow the procedure and protocol defined in Clause 10.2 of the IEEE 802.11-2012 standard.

-   Power-save levels, which specify the method for power conservation by the 802.11 station when configured for the power-save mode. The following power-save levels are defined:

    <a href="" id="dot11-power-save-level-max-psp"></a>DOT11\_POWER\_SAVE\_LEVEL\_MAX\_PSP  
    This level requires that the 802.11 station turn off the radio for as long as possible without losing BSS network connectivity, resulting in the greatest power savings at the sake of network performance.

    <a href="" id="dot11-power-save-level-fast-psp"></a>DOT11\_POWER\_SAVE\_LEVEL\_FAST\_PSP  
    This level requires that the 802.11 station turn off the radio for small periods in order to provide optimal network performance.

When [OID\_DOT11\_POWER\_MGMT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569402) is queried, the miniport driver returns the current power management settings for the 802.11 station.

For more information about the MLME-POWERMGMT.request service primitive, refer to Clause 6.3.2 of the IEEE 802.11-2012 standard.

Beginning with Windows 7, additional power management requirements apply to Native 802.11 Wireless LAN NICs. These requirements are described in [Wake-on-Wireless LAN](wake-on-wireless-lan.md).

 

 





