---
title: Required and Optional OIDs for Power Management
description: Required and Optional OIDs for Power Management
ms.assetid: 147e35b2-dfa5-4238-82e6-5c48ffa30af5
keywords:
- OIDs WDK networking , power management
- wake-up capabilities WDK networking , OIDs
- power management WDK NDIS miniport , OIDs
- object identifiers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required and Optional OIDs for Power Management





For a miniport driver, supporting power management involves supporting power management object identifiers (OIDs). For a detailed description of how miniport drivers process queries and sets to OIDs, see [Obtaining and SettingMiniport Driver Information and NDIS Support for WMI](obtaining-and-setting-miniport-driver-information-and-ndis-support-for.md).

There are two levels of power management support for miniport drivers:

1.  A miniport driver can support a network adapter making a transition between power states. This support is the minimum level of power management support. For a description of device power states for network adapters, see [Device Power States for Network Adapters](device-power-states-for-network-adapters.md).

2.  A miniport driver can also support one or more [network wake-up events](network-wake-up-events.md).

Miniport drivers report power management capabilities during initialization. For more information about power management capabilities that are reported during initialization, see [**NDIS\_MINIPORT\_ADAPTER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920) and the related attributes structures.

A miniport driver must support the following OIDs directly or in attributes for a network adapter to make a transition between power states:

-   [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774)

    Intermediate drivers must respond to this OID query. NDIS responds to OID\_PNP\_CAPABILITIES requests on behalf of physical network adapters. For more information about responding to this OID in an intermediate driver, see [Handling PnP Events and Power Management Events in an Intermediate Driver](handling-pnp-events-and-power-management-events-in-an-intermediate-dri.md).

-   [OID\_PNP\_QUERY\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569778)

    This OID specifies a device power state to which the network adapter should prepare to transition. A miniport driver must always return NDIS\_STATUS\_SUCCESS in response to a query of OID\_PNP\_QUERY\_POWER. By returning NDIS\_STATUS\_SUCCESS in response to this OID request, the miniport driver guarantees that it will transition the network adapter to the specified device power state on receipt of a subsequent OID\_PNP\_SET\_POWER request. The miniport driver, in this case, must do nothing to jeopardize the transition.

-   [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)

    This OID indicates that the network adapter must transition to the indicated device power state. A miniport driver must set the network adapter to the specified state before the driver returns NDIS\_STATUS\_SUCCESS. A miniport driver must always return NDIS\_STATUS\_SUCCESS in response to this OID. If OID\_PNP\_SET\_POWER sets a network adapter to working power state and the miniport driver fails this OID, NDIS assumes that the device is in a unrecoverable state.

To support network wake-up events, a miniport driver must also support the [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775) OID. Both protocol drivers and NDIS use this OID to enable a network adapter's wake-up capabilities. For more information, see [Enabling Wake-Up Events](enabling-wake-up-events.md).

To support network wake-up frames (see [Network Wake-Up Events](network-wake-up-events.md)), a miniport driver must also support the following OIDs that are related to wake-up events:

-   [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569773)

    A protocol driver uses this OID to add a wake-up pattern to a list that either the network adapter or miniport driver or both maintain.

-   [OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569779)

    A protocol driver uses this OID to delete a wake-up pattern that it previously specified with OID\_PNP\_ADD\_WAKE\_UP\_PATTERN.

NDIS miniport drivers that support network wake-up events can optionally support the following statistical OIDs that are related to wake-up events:

-   [OID\_PNP\_WAKE\_UP\_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569781)

    Protocol drivers query this OID to determine the number of false wake-ups signaled by the miniport driver's network adapter.

-   [OID\_PNP\_WAKE\_UP\_OK](https://msdn.microsoft.com/library/windows/hardware/ff569782)

    Protocol drivers query this OID to determine the number of valid wake-ups that are signaled by the miniport driver's network adapter.

 

 





