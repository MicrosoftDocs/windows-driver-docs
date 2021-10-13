---
title: Allocating an Interface Index
description: Allocating an Interface Index
keywords:
- NDIS network interfaces WDK , interface index allocation
- network interfaces WDK , interface index allocation
- interface index WDK networking
- allocating network interface index
- index operations WDK network interface
- locally unique identifier WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating an Interface Index





If an interface provider successfully registers an interface by calling the [**NdisIfRegisterInterface**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterinterface) function, NDIS allocates an interface index for that interface and returns the index value at the location that the *pIfIndex* parameter specifies. The interface index is a 16-bit value that is unique on the local computer. NDIS does not guarantee that it will allocate the same interface index when an interface provider registers the same [**NET\_LUID**](/windows/win32/api/ifdef/ns-ifdef-net_luid_lh) value after the computer restarts. The interface index value zero (NET\_IFINDEX\_UNSPECIFIED) is reserved, and NDIS does not assign it to any interface.

 

