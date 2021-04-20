---
title: Handling PnP and Power Management Events in Intermediate Drivers
description: Initializing Intermediate Drivers to Handle PnP and Power Management Events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing Intermediate Drivers to Handle PnP and Power Management Events


To handle Plug and Play (PnP) and power management events, NDIS intermediate drivers must do the following:

-   When NDIS calls the intermediate driver's [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function, the *BindParameters* parameter points to an [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure that contains the capabilities of the underlying miniport adapter. The power management capabilities are reported in one of the following members:

    -   **PowerManagementCapabilities**

        For NDIS 6.0 and NDIS 6.1 intermediate drivers, this member contains the power management capabilities within an NDIS\_PNP\_CAPABILITIES structure. For more information about this structure, see [OID\_PNP\_CAPABILITIES](./oid-pnp-capabilities.md).

        **Note**  For NDIS 6.20 and later intermediate drivers, the **PowerManagementCapabilities** member is set to **NULL** and the power management capabilities are reported in the **PowerManagementCapabilitiesEx** member.



    -   **PowerManagementCapabilitiesEx**

        For NDIS 6.20 and later intermediate drivers, this member contains the power management capabilities within an [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure.

        **Note**  For NDIS 6.0 and NDIS 6.1 intermediate drivers, the **PowerManagementCapabilitiesEx** member is set to **NULL** and the power management capabilities are reported in the **PowerManagementCapabilities** member.




**Note**  If the underlying miniport adapter does not support power management events, the **PowerManagementCapabilities** and **PowerManagementCapabilitiesEx** members are set to **NULL**.




-   When NDIS calls [MiniportInitializeEx](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) for each virtual miniport supported by the NDIS intermediate driver, the driver reports its power management capabilities by calling [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) in the following ways:

    1.  Depending on the version of the NDIS intermediate driver, the power management capabilities are reported in either the **PowerManagementCapabilities** member (for NDIS 6.0 and NDIS 6.1 intermediate drivers) or **PowerManagementCapabilitiesEx** member (for NDIS 6.20 and later intermediate drivers) of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes). If either the **PowerManagementCapabilities** or **PowerManagementCapabilitiesEx** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure is not **NULL**, the intermediate driver must do the following:

        -   Save the original values of the **MinMagicPacketWakeUp**, **MinPatternWakeUp**, and **MinLinkChangeWakeUp** members of the **PowerManagementCapabilities**(NDIS 6.0 and NDIS 6.1) or **PowerManagementCapabilitiesEx**(NDIS 6.20 and later) members.

        -   Disable the power management functionality by setting the **MinMagicPacketWakeUp**, **MinPatternWakeUp**, and **MinLinkChangeWakeUp** members to **NdisDeviceStateUnspecified**.

        -   Pass the address of the modified [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure as the *MiniportAttributes* parameter in the call to [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

    2.  An intermediate driver must set the NDIS\_MINIPORT\_ATTRIBUTES\_NO\_HALT\_ON\_SUSPEND flag in the **AttributeFlags** member of the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. The driver must pass the address of this structure as the *MiniportAttributes* parameter in the call to [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

    For more information about the initialization requirements of NDIS intermediate drivers, see [Initializing Virtual Miniports](initializing-virtual-miniports.md).
