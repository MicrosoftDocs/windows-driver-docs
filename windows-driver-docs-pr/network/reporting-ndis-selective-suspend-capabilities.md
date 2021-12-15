---
title: Reporting NDIS Selective Suspend Capabilities
description: Reporting NDIS Selective Suspend Capabilities
ms.date: 04/20/2017
---

# Reporting NDIS Selective Suspend Capabilities


Starting with NDIS 6.30, miniport drivers must report whether the driver has enabled the support for NDIS selective suspend. The support for NDIS selective suspend is enabled or disabled through the setting of the **\*SelectiveSuspend** standardized INF keyword. For more information about this INF keyword, see [Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md).

When NDIS calls the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the miniport driver reports its support for NDIS selective suspend support by following these steps:

1.  The driver initializes an [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure with the power management capabilities of the underlying hardware.

    If the driver enables the support for NDIS selective suspend, it must set the members of the [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure as follows:

    -   The miniport driver must specify NDIS\_PM\_CAPABILITIES\_REVISION\_2 and NDIS\_SIZEOF\_NDIS\_PM\_CAPABILITIES\_REVISION\_2 for the revision and length of the [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure within the structure's **Header** member.
    -   If the **\*SelectiveSuspend** keyword has a value of one, the miniport driver support for NDIS selective suspend is enabled. The miniport driver reports this by setting the NDIS\_PM\_SELECTIVE\_SUSPEND\_SUPPORTED flag within the **Flags** member of this structure.

2.  Once it has initialized the [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure, the miniport driver sets the **PowerManagementCapabilitiesEx** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure to point to the initialized **NDIS\_PM\_CAPABILITIES** structure. The miniport driver passes a pointer to an **NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES** structure in the *MiniportAttributes* parameter when the driver calls the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

The method that is used by miniport drivers to report the support status of NDIS selective suspend is based on the NDIS 6.20 method for reporting power management capabilities. For more information about this method, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

 

