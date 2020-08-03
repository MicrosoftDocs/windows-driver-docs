---
title: Initializing an NDK Miniport Adapter
description: This section describes how to initialize an NDK miniport adapter
ms.assetid: 0A920057-3C12-4770-BA08-6C3BB24072EB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing an NDK Miniport Adapter


A Network Direct kernel (NDK) miniport adapter is initialized in the same way as other miniport adapters: NDIS calls the miniport adapter's [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function as described in [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md). This topic describes the NDK-specific requirements for the miniport adapter's *MiniportInitializeEx* function.

In its [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the miniport driver must do the following:

1.  Populate an [**NDIS\_MINIPORT\_ADAPTER\_NDK\_ATTRIBUTES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_ndk_attributes) structure for the adapter as follows:

    - The miniport driver sets the **Header** member as described in the member description to identify the adapter as an NDK-capable miniport adapter.

    - The miniport driver sets the **Enabled** member to **TRUE** if its NDK functionality is enabled, or **FALSE** otherwise.

        > [!NOTE]
        > For more information about querying and setting the current state of the miniport driver's NDK functionality, see [Enabling and Disabling NDK Functionality](enabling-and-disabling-ndk-functionality.md).         

    - In the **NdkCapabilities** member, the miniport driver stores a pointer to an [**NDIS\_NDK\_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ndk_capabilities) structure that specifies the capabilities of the adapter.

2.  Call [**NdisMSetMiniportAttributes**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) to set these attributes for the adapter.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






