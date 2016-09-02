---
title: Extensible Station Operating States
description: Extensible Station Operating States
ms.assetid: 1fc407a7-aebc-4cb9-9a2e-d0b3337fce28
keywords: ["operating states WDK Native 802.11", "Extensible Station operating states WDK Native 802.11", "ExtSTA operating states WDK Native 802.11"]
---

# Extensible Station Operating States


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Extensible Station (ExtSTA) operation mode consists of the following states:

<a href="" id="initialization--init-"></a>**Initialization (INIT)**  
In this state, the 802.11 station is configured for all subsequent connection attempts to a basic service set (BSS) network. All of the 802.11 MAC and PHY attributes can be configured while the miniport driver is in this state. For example, the service set identifier (SSID) and BSS type can be configured from this state.

When the NIC is operating in the ExtSTA INIT state, it can receive NDIS OIDs listed in the "ExtSTA INIT" column of [Native 802.11 Extensible Station OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560602).

In addition, any 802.11 MAC or PHY extensions developed by the independent hardware vendor (IHV) can be configured in this state.

For more information about initialization requirements, see [Native 802.11 Miniport Driver Initialization](native-802-11-miniport-driver-initialization.md).

<a href="" id="operation--op-"></a>**Operation (OP)**  
In this state, the 802.11 station is connected to or is attempting to connect to a BSS network. Only a few MAC- or PHY-layer attributes, such as 802.11 fragmentation and request-to-send (RTS) threshold values, can be configured in this state.

When the NIC is operating in the ExtSTA OP state, it can receive NDIS OIDs listed in the "ExtSTA OP" column of [Native 802.11 Extensible Station OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560602).

The miniport driver transitions from the INIT state to the OP state only when the operating system sets [OID\_DOT11\_CONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122). When this happens, the 802.11 station must connect to any BSS network that matches the current 802.11 MAC and PHY configuration. After it is connected, the 802.11 station can roam to another BSS identifier (BSSID) within the connected BSS network.

The miniport driver transitions from the OP state to the INIT state whenever the operating system sets one of the following object identifiers (OIDs):

<a href="" id="oid-dot11-reset-request"></a>[OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409)  
A method request of this OID is made whenever 802.11 MAC or PHY attributes are to be changed. For example, the operating system sets OID\_DOT11\_RESET\_REQUEST whenever the user has selected a new wireless LAN (WLAN) profile.

<a href="" id="oid-dot11-disconnect-request"></a>[OID\_DOT11\_DISCONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569147)  
The operating system sets this OID to prevent the 802.11 station from attempting to connect to the currently configured BSS network.

 

 





