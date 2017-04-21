---
title: Automatic MAC Configuration
description: Automatic MAC Configuration
ms.assetid: 633636d7-28d6-489c-adc5-7ebf6a4b21b9
keywords:
- MAC configuration WDK Native 802.11
- automatic MAC configuration WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Automatic MAC Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, it can support the automatic MAC configuration mode. If this mode is enabled, the operating system assumes that the media access control (MAC) is configured through Native 802.11 modules that are provided by the independent hardware vendor (IHV), such as its miniport driver or IHV Extensions DLL. For more information about the Native 802.11 modules provided by the IHV, see [Native 802.11 Software Architecture](native-802-11-software-architecture.md).

The automatic MAC configuration mode is set or queried through the [OID\_DOT11\_AUTO\_CONFIG\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106) object identifier (OID).

When the automatic MAC configuration mode is enabled, the configuration of the MAC is set through one of the following:

-   Automatically, by the 802.11 station.

-   Dynamically, through NIC-specific extensions that are defined by the IHV. NIC-specific extensions are set or queried through a method request of [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393).
-   Optionally, through the OIDs defined in [802.11 MAC Configuration](802-11-mac-configuration.md). When these OIDs are set, the miniport driver can either pass or fail the set request. If it fails the set request because automatic MAC configuration mode is enabled, the miniport driver must return NDIS\_STATUS\_DOT11\_AUTO\_CONFIG\_ENABLED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

When automatic MAC configuration mode is disabled, the operating system sets the MAC configuration through the OIDs defined in [802.11 MAC Configuration](802-11-mac-configuration.md). The miniport driver must accept the set request if the data that accompanies the set request is valid.

**Note**  For the Windows Vista operating system, only the [OID\_DOT11\_FRAGMENTATION\_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569368) and [OID\_DOT11\_RTS\_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569411) OIDs are affected by automatic MAC configuration mode.

 

 

 





