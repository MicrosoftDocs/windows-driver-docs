---
title: Allocating an Interface Index
description: Allocating an Interface Index
ms.assetid: f1315da2-16da-4320-9d0d-1270396af38b
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





If an interface provider successfully registers an interface by calling the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function, NDIS allocates an interface index for that interface and returns the index value at the location that the *pIfIndex* parameter specifies. The interface index is a 16-bit value that is unique on the local computer. NDIS does not guarantee that it will allocate the same interface index when an interface provider registers the same [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value after the computer restarts. The interface index value zero (NET\_IFINDEX\_UNSPECIFIED) is reserved, and NDIS does not assign it to any interface.

 

 





