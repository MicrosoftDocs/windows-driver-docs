---
title: Including Header Files for IP Helper
description: Including Header Files for IP Helper
ms.assetid: f4642717-223c-425a-8389-cbbc75567ae3
keywords:
- IP Helper WDK networking , including header files
- header files WDK IP Helper
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Including Header Files for IP Helper


Driver code that uses the kernel-mode IP Helper functions, MIB structures, and enumerations that are declared in Netioapi.h must have **\#include** statements in the following sequence.

```C++
#include <ntddk.h>
#include <netioapi.h>
```

**Note**  Do not include Iphlpapi.h in driver code. It is used only for user-mode applications.

 

When Netioapi.h is used with kernel-mode drivers, it already includes networking header files that define Winsock Kernel, network interface information, the network layer, and Network Driver Interface Specification (NDIS) types.

Therefore, do not include the following header files in your driver code:

- Ifdef.h
- Nldef.h
- Ws2def.h
- Ws2ipdef.h

For information about the user-mode versions of the IP Helper functions and MIB structures, see the Windows SDK documentation.

 

 





