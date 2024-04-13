---
title: Deregistering a Network Interface
description: Deregistering a Network Interface
keywords:
- NDIS network interfaces WDK , deregistering
- network interfaces WDK , deregistering
- deregistering network interfaces
- removing network interfaces
- unregistering network interfaces
- NdisIfDeregisterInterface
ms.date: 04/20/2017
---

# Deregistering a Network Interface





An NDIS interface provider calls the [**NdisIfDeregisterInterface**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifderegisterinterface) function to indicate that a specified interface should be removed from the list of known interfaces on the computer, for example, because the interface has been uninstalled. Other reasons for deregistering interfaces are application-specific. To promote good resource management, interface providers should always deregister interfaces that are no longer useful.

**NdisIfDeregisterInterface** releases the interface index that is associated with the specified interface. NDIS can reassign the index to an interface that is registered in the future. However the [**NET\_LUID**](/windows/win32/api/ifdef/ns-ifdef-net_luid_lh) index that is associated with the corresponding NET\_LUID value is not reclaimed--if necessary, the interface provider can release the NET\_LUID index by calling the [**NdisIfFreeNetLuidIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiffreenetluidindex) function.

**Note**  The NDIS proxy provider deregisters interfaces for miniport adapters when they are uninstalled and filter modules when they are detached.

 

 

