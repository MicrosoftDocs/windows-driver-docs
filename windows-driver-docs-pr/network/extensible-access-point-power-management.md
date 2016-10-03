---
title: Extensible Access Point Power Management
description: Extensible Access Point Power Management
ms.assetid: 66a7edb8-8987-488c-a91f-679cae3e948a
keywords: ["power management WDK networking , Native 802.11 extensible AP"]
---

# Extensible Access Point Power Management


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A NIC that is operating in the [Extensible Access Point Operation Mode](extensible-access-point-operation-mode.md) must support NDIS power management OIDs as described in [NIC Power Management](nic-power-management.md).

When the computer is transitioned into a low-power state (either D1, D2, or D3), the NIC should stay in the existing INIT or OP operating state. These states are described in [Extensible Access Point Operating States](extensible-access-point-operating-states.md).

When the NIC is transitioned back to the D0 power state, the NIC should do the following:

-   If the NIC is in the OP state, it should not resume transmission of any Beacon or Probe Response packets. When the computer returns to the D0 power state, the operating system will ensure that an [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) OID is called. In response to this OID, the NIC should reset and return to the INIT state.

-   If the NIC is in the INIT state, it should remain in that state.

 

 





