---
title: Handling OID_PNP_Xxx Queries and Sets
description: Handling OID_PNP_Xxx Queries and Sets
ms.assetid: 2d5db7fb-2a27-4359-9d75-35939e72de69
keywords:
- OID_PNP_Xxx
- query operations WDK NDIS intermediate
- set operations WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling OID\_PNP\_Xxx Queries and Sets





The virtual miniport of an intermediate driver must export the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. NDIS calls the intermediate driver's *MiniportOidRequest* function when an overlying driver that is bound to the intermediate driver's virtual miniport calls [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) to query or set information objects (OID\_*Xxx*). NDIS can also call *MiniportOidRequest* on its own behalf. For more information about miniport driver handling of sets and queries to information objects, see [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](obtaining-and-setting-miniport-driver-information-and-ndis-support-for.md).

The intermediate driver should retain information about the capabilities of the underlying miniport adapters that it receives in the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function. If the miniport adapter is not power management-aware, NDIS sets the **PowerManagementCapabilities** member of [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) to **NULL**.

The intermediate driver can query or set an OID\_*Xxx* that is maintained by the underlying miniport driver. It does this with **NdisOidRequest**(if the intermediate driver has a connectionless lower edge), or with [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711)(if the intermediate driver has a connection-oriented lower edge).

An intermediate driver should handle queries and sets as follows:

-   [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774)

    In response to this OID query, intermediate drivers must report the PnP capabilites of the underlying physical miniport adapters. Note that miniport adapters for physical devices do not receive this OID query.

    The intermediate driver receives the PnP capabilities of the underlying miniport adapters in the bind parameters. It should pass them to overlying drivers as appropriate for the intermediate driver's intended use. Intermediate drivers and miniport drivers report PnP capabilities in miniport adapter attributes. The intermediate driver does not issue OID\_PNP\_CAPABILITIES requests to the underlying miniport driver. If the underlying miniport adapter is power management-aware, in the NDIS\_PM\_WAKE\_UP\_CAPABILITIES structure in the virtual miniport attributes, the intermediate driver must specify a device power state of **NdisDeviceStateUnspecified** for each wake-up capability:

    -   MinMagicPacketWakeUp
    -   MinPatternWakeUp
    -   MinLinkChangeWakeUp

    Such a setting indicates that the intermediate driver is power management-aware but cannot wake up the system.

-   [OID\_PNP\_QUERY\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569778) and [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)

    The intermediate driver must always return NDIS\_STATUS\_SUCCESS to a query of OID\_PNP\_QUERY\_POWER or a set of OID\_PNP\_SET\_POWER. The intermediate driver must never propagate either of these OID requests to the underlying miniport driver.

-   "Wake-up OIDs"

    If an underlying NIC is power management-aware, the intermediate driver must pass to the underlying miniport driver (by calling **NdisOidRequest** or **NdisCoOidRequest**) the following OID\_PNP\_*Xxx* that relate to wake-up events:

    [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775)

    [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569773)

    [OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569779)

    [OID\_PNP\_WAKE\_UP\_PATTERN\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569783)

    [OID\_PNP\_WAKE\_UP\_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569781)

    [OID\_PNP\_WAKE\_UP\_OK](https://msdn.microsoft.com/library/windows/hardware/ff569782)

The intermediate driver must also propagate the underlying miniport driver's response to these OIDs to the overlying protocol drivers.

If the underlying miniport adapter is not power management-aware, the miniport driver sets the **PowerManagementCapabilities** member of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) to **NULL** and NDIS sets the **PowerManagementCapabilities** member of [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) to **NULL**.

If an underlying miniport adapter is not power management-aware, the intermediate driver should return NDIS\_STATUS\_NOT\_SUPPORTED in response to a query or set of these OIDs.

 

 





