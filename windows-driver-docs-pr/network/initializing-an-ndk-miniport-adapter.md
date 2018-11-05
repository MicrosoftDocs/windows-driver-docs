---
title: Initializing an NDK Miniport Adapter
description: This section describes how to initialize an NDK miniport adapter
ms.assetid: 0A920057-3C12-4770-BA08-6C3BB24072EB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing an NDK Miniport Adapter


A Network Direct kernel (NDK) miniport adapter is initialized in the same way as other miniport adapters: NDIS calls the miniport adapter's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function as described in [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md). This topic describes the NDK-specific requirements for the miniport adapter's *MiniportInitializeEx* function.

In its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the miniport driver must do the following:

1.  Populate an [**NDIS\_MINIPORT\_ADAPTER\_NDK\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/hh451558) structure for the adapter as follows:

    - The miniport driver sets the **Header** member as described in the member description to identify the adapter as an NDK-capable miniport adapter.

    - The miniport driver sets the **Enabled** member to **TRUE** if its NDK functionality is enabled, or **FALSE** otherwise.

        > [!NOTE]
        > For more information about querying and setting the current state of the miniport driver's NDK functionality, see [Enabling and Disabling NDK Functionality](enabling-and-disabling-ndk-functionality.md).         

    - In the **NdkCapabilities** member, the miniport driver stores a pointer to an [**NDIS\_NDK\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451560) structure that specifies the capabilities of the adapter.

2.  Call [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) to set these attributes for the adapter.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






