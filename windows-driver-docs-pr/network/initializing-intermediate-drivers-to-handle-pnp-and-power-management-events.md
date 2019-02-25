---
title: Handling PnP and Power Management Events in Intermediate Drivers
description: Initializing Intermediate Drivers to Handle PnP and Power Management Events
ms.assetid: 7c9f10f1-1094-4b43-990b-fc3b3fee5ed1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing Intermediate Drivers to Handle PnP and Power Management Events


To handle Plug and Play (PnP) and power management events, NDIS intermediate drivers must do the following:

-   When NDIS calls the intermediate driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function, the *BindParameters* parameter points to an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure that contains the capabilities of the underlying miniport adapter. The power management capabilities are reported in one of the following members:

    -   **PowerManagementCapabilities**

        For NDIS 6.0 and NDIS 6.1 intermediate drivers, this member contains the power management capabilities within an NDIS\_PNP\_CAPABILITIES structure. For more information about this structure, see [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774).

        **Note**  For NDIS 6.20 and later intermediate drivers, the **PowerManagementCapabilities** member is set to **NULL** and the power management capabilities are reported in the **PowerManagementCapabilitiesEx** member.



    -   **PowerManagementCapabilitiesEx**

        For NDIS 6.20 and later intermediate drivers, this member contains the power management capabilities within an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure.

        **Note**  For NDIS 6.0 and NDIS 6.1 intermediate drivers, the **PowerManagementCapabilitiesEx** member is set to **NULL** and the power management capabilities are reported in the **PowerManagementCapabilities** member.




**Note**  If the underlying miniport adapter does not support power management events, the **PowerManagementCapabilities** and **PowerManagementCapabilitiesEx** members are set to **NULL**.




-   When NDIS calls [MiniportInitializeEx](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_initialize) for each virtual miniport supported by the NDIS intermediate driver, the driver reports its power management capabilities by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) in the following ways:

    1.  Depending on the version of the NDIS intermediate driver, the power management capabilities are reported in either the **PowerManagementCapabilities** member (for NDIS 6.0 and NDIS 6.1 intermediate drivers) or **PowerManagementCapabilitiesEx** member (for NDIS 6.20 and later intermediate drivers) of [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923). If either the **PowerManagementCapabilities** or **PowerManagementCapabilitiesEx** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure is not **NULL**, the intermediate driver must do the following:

        -   Save the original values of the **MinMagicPacketWakeUp**, **MinPatternWakeUp**, and **MinLinkChangeWakeUp** members of the **PowerManagementCapabilities**(NDIS 6.0 and NDIS 6.1) or **PowerManagementCapabilitiesEx**(NDIS 6.20 and later) members.

        -   Disable the power management functionality by setting the **MinMagicPacketWakeUp**, **MinPatternWakeUp**, and **MinLinkChangeWakeUp** members to **NdisDeviceStateUnspecified**.

        -   Pass the address of the modified [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure as the *MiniportAttributes* parameter in the call to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

    2.  An intermediate driver must set the NDIS\_MINIPORT\_ATTRIBUTES\_NO\_HALT\_ON\_SUSPEND flag in the **AttributeFlags** member of the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934) structure. The driver must pass the address of this structure as the *MiniportAttributes* parameter in the call to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

    For more information about the initialization requirements of NDIS intermediate drivers, see [Initializing Virtual Miniports](initializing-virtual-miniports.md).









