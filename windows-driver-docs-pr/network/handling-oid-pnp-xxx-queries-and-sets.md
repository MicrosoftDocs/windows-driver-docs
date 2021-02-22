---
title: Handling OID_PNP_Xxx Queries and Sets
description: Handling OID_PNP_Xxx Queries and Sets
keywords:
- OID_PNP_Xxx
- query operations WDK NDIS intermediate
- set operations WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling OID\_PNP\_Xxx Queries and Sets





The virtual miniport of an intermediate driver must export the [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function. NDIS calls the intermediate driver's *MiniportOidRequest* function when an overlying driver that is bound to the intermediate driver's virtual miniport calls [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) to query or set information objects (OID\_*Xxx*). NDIS can also call *MiniportOidRequest* on its own behalf. For more information about miniport driver handling of sets and queries to information objects, see [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](ndis-management-information-and-oids.md).

The intermediate driver should retain information about the capabilities of the underlying miniport adapters that it receives in the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function. If the miniport adapter is not power management-aware, NDIS sets the **PowerManagementCapabilities** member of [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) to **NULL**.

The intermediate driver can query or set an OID\_*Xxx* that is maintained by the underlying miniport driver. It does this with **NdisOidRequest**(if the intermediate driver has a connectionless lower edge), or with [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest)(if the intermediate driver has a connection-oriented lower edge).

An intermediate driver should handle queries and sets as follows:

-   [OID\_PNP\_CAPABILITIES](./oid-pnp-capabilities.md)

    In response to this OID query, intermediate drivers must report the PnP capabilites of the underlying physical miniport adapters. Note that miniport adapters for physical devices do not receive this OID query.

    The intermediate driver receives the PnP capabilities of the underlying miniport adapters in the bind parameters. It should pass them to overlying drivers as appropriate for the intermediate driver's intended use. Intermediate drivers and miniport drivers report PnP capabilities in miniport adapter attributes. The intermediate driver does not issue OID\_PNP\_CAPABILITIES requests to the underlying miniport driver. If the underlying miniport adapter is power management-aware, in the NDIS\_PM\_WAKE\_UP\_CAPABILITIES structure in the virtual miniport attributes, the intermediate driver must specify a device power state of **NdisDeviceStateUnspecified** for each wake-up capability:

    -   MinMagicPacketWakeUp
    -   MinPatternWakeUp
    -   MinLinkChangeWakeUp

    Such a setting indicates that the intermediate driver is power management-aware but cannot wake up the system.

-   [OID\_PNP\_QUERY\_POWER](./oid-pnp-query-power.md) and [OID\_PNP\_SET\_POWER](./oid-pnp-set-power.md)

    The intermediate driver must always return NDIS\_STATUS\_SUCCESS to a query of OID\_PNP\_QUERY\_POWER or a set of OID\_PNP\_SET\_POWER. The intermediate driver must never propagate either of these OID requests to the underlying miniport driver.

-   "Wake-up OIDs"

    If an underlying NIC is power management-aware, the intermediate driver must pass to the underlying miniport driver (by calling **NdisOidRequest** or **NdisCoOidRequest**) the following OID\_PNP\_*Xxx* that relate to wake-up events:

    [OID\_PNP\_ENABLE\_WAKE\_UP](./oid-pnp-enable-wake-up.md)

    [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](./oid-pnp-add-wake-up-pattern.md)

    [OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN](./oid-pnp-remove-wake-up-pattern.md)

    [OID\_PNP\_WAKE\_UP\_PATTERN\_LIST](./oid-pnp-wake-up-pattern-list.md)

    [OID\_PNP\_WAKE\_UP\_ERROR](./oid-pnp-wake-up-error.md)

    [OID\_PNP\_WAKE\_UP\_OK](./oid-pnp-wake-up-ok.md)

The intermediate driver must also propagate the underlying miniport driver's response to these OIDs to the overlying protocol drivers.

If the underlying miniport adapter is not power management-aware, the miniport driver sets the **PowerManagementCapabilities** member of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) to **NULL** and NDIS sets the **PowerManagementCapabilities** member of [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) to **NULL**.

If an underlying miniport adapter is not power management-aware, the intermediate driver should return NDIS\_STATUS\_NOT\_SUPPORTED in response to a query or set of these OIDs.

 

