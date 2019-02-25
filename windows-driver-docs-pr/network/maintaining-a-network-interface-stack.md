---
title: Maintaining a Network Interface Stack
description: Maintaining a Network Interface Stack
ms.assetid: c51a2e5b-28ad-4e86-8b37-1491f85a17bb
keywords:
- NDIS network interfaces WDK , stack maintenance
- network interfaces WDK , stack maintenance
- stacks WDK networking
- interface stack table WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Maintaining a Network Interface Stack





NDIS provides services to maintain the interface stack table (*ifStackTable* in RFC 2863). NDIS maintains the stack table for NDIS miniport adapters, NDIS 5.*x* filter intermediate drivers, and NDIS filter modules. NDIS also provides services to enable NDIS drivers to add and delete entries in this table. For MUX intermediate drivers, NDIS does not have access to the relationship between the virtual miniport interface and the protocol lower interface. Therefore, NDIS 6.0 MUX intermediate drivers must specify these internal interface relationships.

To define a stack relationship between two interfaces, any NDIS driver can pass *HigherLayerIfIndex* and *LowerLayerIfIndex* parameters to the [**NdisIfAddIfStackEntry**](https://msdn.microsoft.com/library/windows/hardware/ff562693) function. These parameters specify one network interface that should be higher in the network interface stack and one network interface that should be lower in the stack.

A driver that has stack order information about an interface that is related to another interface (for example, internal bindings in a MUX intermediate driver that are not visible to NDIS) calls **NdisIfAddIfStackEntry** to populate the interface stack table. This function returns NDIS\_STATUS\_SUCCESS if the stack entry was successfully made. Typically, the component that owns or is the interface provider for the higher layer interface (which *HigherLayerIfIndex* identifies) calls **NdisIfAddIfStackEntry**.

To remove a stack table entry, a driver passes *HigherLayerIfIndex* and *LowerLayerIfIndex* parameters to the [**NdisIfDeleteIfStackEntry**](https://msdn.microsoft.com/library/windows/hardware/ff562698) function.

For an example of maintaining the interface stack, see the MUX 6.0 sample driver.

 

 





