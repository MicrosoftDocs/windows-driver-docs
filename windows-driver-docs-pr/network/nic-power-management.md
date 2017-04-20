---
title: NIC Power Management
description: NIC Power Management
ms.assetid: 2da7c9ee-22f9-42aa-ab0f-f3eb4aafdd60
keywords:
- power management WDK Native 802.11 , NIC
- NICs WDK networking , power states
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NIC Power Management


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Native 802.11 miniport drivers must be capable of NDIS power management and must support the following object identifiers (OIDs):

-   [OID\_PNP\_QUERY\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569778)

-   [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)

When an 802.11 miniport driver calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function, it reports its power management capabilities through one of the following structures. The choice of structure depends on the supported NDIS version:

-   [NDIS\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774) for NDIS versions 6.0 and 6.1

-   [NDIS\_PM\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff566748) for NDIS version 6.20 and later

The miniport driver initializes these structures with the power management capabilities of the NIC. It initializes structures by setting the **PowerManagementCapabilities** or **PowerManagementCapabilitiesEx** members of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure. The *MiniportAttributes* parameter of **NdisMSetMiniportAttributes** points to this structure. A driver that supports NDIS 6.0 or later sets **PowerManagementCapabilities** to point to [NDIS\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774). A driver that supports NDIS 6.20 and later sets **PowerManagementCapabilitiesEx** to point to NDIS\_PM\_CAPABILITIES.

An 802.11 NIC can optionally support wake-on-LAN (WOL) events, which are configured by the operating system using the appropriate [WOL OIDs](https://msdn.microsoft.com/library/windows/hardware/ff564784).

An independent hardware vendor (IHV) can also configure and enable WOL events through proprietary extensions made through method requests of [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393).

### <a href="" id="oid-pnp-query-power-queries"></a>OID\_PNP\_QUERY\_POWER Queries

When the operating system queries [OID\_PNP\_QUERY\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569778), the miniport driver must only fail the query request if the 802.11 station does not support the specified device state (D0 through D3). In this situation, the driver fails the query request by returning NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

### <a href="" id="oid-pnp-set-power-notifications"></a>OID\_PNP\_SET\_POWER Notifications

The [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) OID notifies the miniport driver that its NIC will be transitioning to a new device power state. The miniport driver must follow these guidelines when the OID\_PNP\_SET\_POWER OID is set:

-   When transitioning to a low-power state (D1 through D3), the miniport driver must:
    -   Reduce the power used by the 802.11 NIC. For example, if the NIC does not support WOL, the miniport driver could turn the radio off.
    -   If the NIC has firmware that supports 802.11 power management, configure the firmware to transition to power save (PS) mode. The NIC's firmware must perform the tasks for PS mode as defined in Clause 10.2 of the IEEE 802.11-2012 standard.
    -   If WOL events have been configured and enabled, configure the NIC to resume the system following a WOL event. While in a low-power state, the 802.11 station must be able to perform roaming and authentication operations without resuming the system to a high power state of D0.
-   When transitioning to the highest power state (D0), the miniport driver must:
    -   Turn on the radio if it was previously turned off.
    -   Configure the 802.11 station to transition to active mode (AM).
    -   Restore the NIC to its configuration prior to the transition to a low-power state.
    -   If previously connected, restore the basic service set (BSS) network connection. If the previous BSS connection is no longer valid, the miniport driver must perform roaming operations as defined in [Roaming Operations](roaming-operations.md).

Beginning with Windows 7, additional power management requirements apply to Native 802.11 Wireless LAN NICs. These requirements are described in [Wake-on-Wireless LAN](wake-on-wireless-lan.md).

For more information about NDIS power management, see [NDIS Power Management](ndis-power-management.md).

 

 





