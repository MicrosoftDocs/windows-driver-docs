---
title: Automatic PHY Configuration
description: Automatic PHY Configuration
ms.assetid: a2a5f689-152d-44d5-a7a6-34e8853a6cae
keywords: ["PHY configuration WDK Native 802.11 , automatic", "automatic PHY configuration WDK Native 802.11"]
---

# Automatic PHY Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, it can support the automatic PHY configuration mode. If this mode is enabled, the operating system assumes that the PHY is is configured through Native 802.11 modules that are provided by the independent hardware vendor (IHV), such as its miniport driver or IHV Extensions DLL. For more information about the Native 802.11 modules provided by the IHV, see [Native 802.11 Software Architecture](native-802-11-software-architecture.md).

The automatic PHY configuration mode is set or queried through the [OID\_DOT11\_AUTO\_CONFIG\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106) object identifier (OID).

When the automatic PHY configuration mode is enabled, the configuration of the PHY is set through one of the following:

-   Automatically, by the 802.11 station.

-   Dynamically, through NIC-specific extensions defined by the IHV. NIC-specific extensions are set or queried through a method request of [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393).

-   Optionally, through the OIDs defined in [802.11 PHY Configuration](802-11-phy-configuration.md). When these OIDs are set, the miniport driver can either pass or fail the set request. If it fails the set request because the automatic PHY configuration mode is enabled, the miniport driver must return NDIS\_STATUS\_DOT11\_AUTO\_CONFIG\_ENABLED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    **Note**  When the miniport driver is operating in the ExtSTA mode, Native 802.11 OIDs used for PHY configuration affect the PHY on the 802.11 station that is referenced through the current PHY identifier (ID). The operating system sets or queries the current PHY ID through [OID\_DOT11\_CURRENT\_PHY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135).

     

When the automatic PHY configuration mode is disabled, the operating system sets the PHY configuration through the OIDs defined in [802.11 PHY Configuration](802-11-phy-configuration.md). The miniport driver must accept the set request if the data that accompanies the set request is valid.

**Note**  For the Windows Vista operating system, only the [OID\_DOT11\_CURRENT\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127) and [OID\_DOT11\_CURRENT\_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130) OIDs are affected by the automatic PHY configuration mode.

 

 

 





