---
title: Device Power States for Network Adapters
description: Device Power States for Network Adapters
ms.assetid: 969aadc9-e797-4a07-9714-8c2c5a6357da
keywords:
- NICs WDK networking , power states
- network interface cards WDK networking , power states
- device power states WDK networking
- power states WDK networking
- power management WDK NDIS miniport , device power states
- transitioning power states WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Power States for Network Adapters





A device power state for a network adapter describes a network adapter's level of power consumption and computing activity.

There are four device power states: D0, D1, D2, and D3. D0 is the highest-powered state. D1, D2, and D3 are the sleeping states. D3 is subdivided into D3hot and D3cold.

The state number is inversely related to power consumption: higher-numbered states use less power. Power might be fully removed from the network adapter in the D3 state.

For a thorough description of device states, see the following topics:

* [Device Power States](https://msdn.microsoft.com/library/windows/hardware/ff543162)
* [Device Working State D0](https://msdn.microsoft.com/library/windows/hardware/ff543210)
* [Device Low-Power States](https://msdn.microsoft.com/library/windows/hardware/ff543186)
* [Required Support for Device Power States](https://msdn.microsoft.com/library/windows/hardware/ff561073)

**Note**  NDIS processes power management IRPs, but NDIS drivers do not.

 

The device power states for network adapters are defined as follows:

### <a href="" id="d0"></a>Device Working State D0

This power state is described for all devices in [Device Working State D0](https://msdn.microsoft.com/library/windows/hardware/ff543210). For network adapters and miniport drivers:

<a href="" id="power-consumption"></a>Power consumption  
The network adapter is fully powered and delivering full functionality and performance.

<a href="" id="device-context"></a>Device context  
The hardware device context is maintained by either the network adapter or miniport driver or both.

<a href="" id="miniport-driver-and-network-adapter-behavior"></a>Miniport driver and network adapter behavior  
The network adapter is fully compliant with the requirements of the attached network. The operation of the miniport driver and network adapter is not restricted because of low-power requirements.

<a href="" id="restore-time"></a>Restore time  
Not applicable.

### <a href="" id="d1"></a>Device Power State D1

This power state is described for all devices in [Device Low-Power States](https://msdn.microsoft.com/library/windows/hardware/ff543186). For network adapters and miniport drivers:

<a href="" id="power-consumption"></a>Power consumption  
This state is the highest-powered sleeping state. Power consumption is less than that in the D0 state and greater than or equal to that in the D2 state.

<a href="" id="device-context"></a>Device context  
The miniport driver should preserve any hardware device context that might be lost. The miniport driver should restore such context when the device returns to the D0 state.

<a href="" id="miniport-driver-and-network-adapter-behavior"></a>Miniport driver and network adapter behavior  
The miniport driver does not receive transmission requests from protocol drivers. NDIS either notifies a bound protocol driver of the network adapter's transition to the sleeping state or, if the protocol driver is an old driver that is not power management-aware, NDIS disables transmission requests from the protocol driver. However, the miniport driver should be able to handle the case in which it does receive transmission requests when it is in this low-power state. In this case, the miniport driver should fail all transmission requests.

The miniport driver does not indicate up any packets that the network adapter might receive while it is in this state.

The network adapter does not generate interrupts. However, the miniport driver must be able to handle interrupts, because a shared interrupt could be generated on the bus.

<a href="" id="restore-time"></a>Restore time  
The time to restore the network adapter to the D0 state is less than that required when the network adapter is in the D2 state.

### <a href="" id="d2"></a>Device Power State D2

This power state is described for all devices in [Device Low-Power States](https://msdn.microsoft.com/library/windows/hardware/ff543186). For network adapters and miniport drivers:

<a href="" id="power-consumption"></a>Power consumption  
An intermediate sleeping state. Power consumption is less than that in the D1 state and greater than or equal to that in the D3 state.

<a href="" id="device-context"></a>Device context  
Same as for D1.

<a href="" id="miniport-driver-and-network-adapter-behavior"></a>Miniport driver and network adapter behavior  
Same as for D1.

<a href="" id="restore-time"></a>Restore time  
The time to restore the network adapter to the D0 state is greater than that required when the network adapter is in the D1 state and less than that required when the network adapter is in the D3 state.

### <a href="" id="d3"></a>Device Power State D3

This power state is described for all devices in [Device Low-Power States](https://msdn.microsoft.com/library/windows/hardware/ff543186). For network adapters and miniport drivers:

<a href="" id="power-consumption"></a>Power consumption  
The sleeping state with the least amount of power. The amount of power may be nonzero (D3hot) or it may be exactly zero (D3cold). For more information about D3hot and D3cold, see [Device Low-Power States](https://msdn.microsoft.com/library/windows/hardware/ff543186).

<a href="" id="device-context"></a>Device context  
Same as for D1.

<a href="" id="miniport-driver-and-network-adapter-behavior"></a>Miniport driver and network adapter behavior  
Same as for D1.

<a href="" id="restore-time"></a>Restore time  
The time to restore the network adapter to the D0 state is greater than that required when the network adapter is in the D2 state.

Before a network adapter can transition to a sleeping state, its miniport driver must disable everything under the miniport driver's control: interrupts must be disabled, timers must be canceled, and so on. A miniport driver cannot access the network adapter hardware after the bus driver sets the network adapter to the D3 state.

### Transitions Allowed Between Device Power States

The only transitions allowed between device power states are from the highest-powered state (D0) to a sleeping state (D1, D2, D3), or from a sleeping state to the highest-powered state. NDIS never commands a network adapter to transition directly from one sleeping state to another.

 

 





