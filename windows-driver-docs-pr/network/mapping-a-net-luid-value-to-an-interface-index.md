---
title: Mapping a NET_LUID Value to an Interface Index
description: Mapping a NET_LUID Value to an Interface Index
ms.assetid: a535d886-186e-4abe-9ca0-ebef262614b3
keywords:
- NDIS network interfaces WDK , NET_LUID
- network interfaces WDK , NET_LUID
- NET_LUID
- mapping NET_LUID value
- interface index WDK networking
- index operations WDK network interface
- locally unique identifier WDK network interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping a NET\_LUID Value to an Interface Index





NDIS provides services to obtain the interface index for a given [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value, and vice versa. Note that the NET\_LUID value is the persistent identification for an interface, and the interface index that corresponds to a particular NET\_LUID value can change even if the computer does not restart (for example, when a filter module is attached and detached because the associated miniport adapter was disabled and reenabled).

NDIS provides the following mapping functions:

-   [**NdisIfGetInterfaceIndexFromNetLuid**](https://msdn.microsoft.com/library/windows/hardware/ff562707)

-   [**NdisIfGetNetLuidFromInterfaceIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562711)

These functions return NDIS\_STATUS\_INTERFACE\_NOT\_FOUND if the given NET\_LUID or interface index is not present in the list of registered interfaces.

 

 





