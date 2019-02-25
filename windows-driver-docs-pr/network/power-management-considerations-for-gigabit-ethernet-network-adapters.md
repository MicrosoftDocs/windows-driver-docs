---
title: Power management considerations for gigabit Ethernet net adapters
description: Power Management Considerations for Gigabit Ethernet Network Adapters
ms.assetid: f195d295-0a2a-4c44-a3b4-217dfad76826
keywords:
- power management WDK networking , gigabit Ethernet NICs
- network interface cards WDK networking , transitioning power states
- NICs WDK networking , transitioning power states
- NICs WDK networking , gigabit Ethernet NICs
- network interface cards WDK networking , gigabit Ethernet NICs
- gigabit Ethernet NICs WDK networking
- power management WDK NDIS miniport , transitioning power states
- device power states WDK networking
- power states WDK networking
- transitioning power states WDK networking
- wake-up capabilities WDK networking , transitioning power states
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management Considerations for Gigabit Ethernet Network Adapters


When a gigabit Ethernet network adapter is operating at 1000 megabits per second (Mbps), it draws a lot of electrical power. Before such a network adapter transitions to a low-power state, its link speed is typically reduced so that the network adapter draws less power. The reduced link speed enables the network adapter to transition to a low-power state. While changing link speeds during the transition to a low-power state, the network adapter typically loses network connectivity for a short time.

Conversely, when a gigabit Ethernet network adapter transitions to the fully-on state from a low-power state, the network adapter's link speed is increased to its fully operational rate. During this transition, the network adapter might also lose connectivity for a short time.

While a miniport driver's underlying network adapter is transitioning to or from a low-power state, the miniport must not indicate either a change in link speed or a change in connection status. For more information about indicating a change in link speed, see [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391). For more information about indicating a change in connection status, see [Indicating Connection Status](indicating-connection-status.md).

 

 





