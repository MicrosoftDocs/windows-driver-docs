---
title: Registering a Network Interface
description: Registering a Network Interface
ms.assetid: 7e3c3b0f-2013-4133-8b52-fa9e66f963cb
keywords:
- NDIS network interfaces WDK , registering
- network interfaces WDK , registering
- registering network interfaces
- NdisIfRegisterInterface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a Network Interface





Whenever a computer restarts, NDIS starts with an empty list of registered network interfaces. An interface provider calls the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function whenever it starts or detects an interface and its [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value is known. The mechanism for starting or detecting an interface is application-specific.

**NdisIfRegisterInterface** returns NDIS\_STATUS\_SUCCESS only if NDIS successfully adds the specified interface to its list of known interfaces on the computer. In this case, **NdisIfRegisterInterface** returns an interface index at the *pIfIndex* parameter. However, a call to **NdisIfRegisterInterface** does not imply that the interface is active; this call guarantees only that the interface exists. **NdisIfRegisterInterface** returns NDIS\_STATUS\_RESOURCES if NDIS does not have sufficient resources available to register the interface. **NdisIfRegisterInterface** can also return other NDIS status values.

The *ProviderIfContext* parameter of **NdisIfRegisterInterface** contains a handle to the caller's context area for the interface--this handle is passed to the caller's OID query and set functions. The *pIfInfo* parameter contains a pointer to a [**NET\_IF\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff568743) structure that includes information about the interface.

The following topics provide more information about network interfaces that **NdisIfRegisterInterface** successfully registers:

[Allocating an Interface Index](allocating-an-interface-index.md)

[Network Interface Information](network-interface-information.md)

 

 





