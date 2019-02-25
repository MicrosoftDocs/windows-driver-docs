---
title: Reporting NDIS Selective Suspend Capabilities
description: Reporting NDIS Selective Suspend Capabilities
ms.assetid: 8A738A51-D116-4DDC-96B7-17D046B6890D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting NDIS Selective Suspend Capabilities


Starting with NDIS 6.30, miniport drivers must report whether the driver has enabled the support for NDIS selective suspend. The support for NDIS selective suspend is enabled or disabled through the setting of the **\*SelectiveSuspend** standardized INF keyword. For more information about this INF keyword, see [Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md).

When NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the miniport driver reports its support for NDIS selective suspend support by following these steps:

1.  The driver initializes an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure with the power management capabilities of the underlying hardware.

    If the driver enables the support for NDIS selective suspend, it must set the members of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure as follows:

    -   The miniport driver must specify NDIS\_PM\_CAPABILITIES\_REVISION\_2 and NDIS\_SIZEOF\_NDIS\_PM\_CAPABILITIES\_REVISION\_2 for the revision and length of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure within the structure's **Header** member.
    -   If the **\*SelectiveSuspend** keyword has a value of one, the miniport driver support for NDIS selective suspend is enabled. The miniport driver reports this by setting the NDIS\_PM\_SELECTIVE\_SUSPEND\_SUPPORTED flag within the **Flags** member of this structure.

2.  Once it has initialized the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure, the miniport driver sets the **PowerManagementCapabilitiesEx** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure to point to the initialized **NDIS\_PM\_CAPABILITIES** structure. The miniport driver passes a pointer to an **NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES** structure in the *MiniportAttributes* parameter when the driver calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

The method that is used by miniport drivers to report the support status of NDIS selective suspend is based on the NDIS 6.20 method for reporting power management capabilities. For more information about this method, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

 

 





