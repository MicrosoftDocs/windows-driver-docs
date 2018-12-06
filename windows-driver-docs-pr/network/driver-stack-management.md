---
title: Driver Stack Management
description: Driver Stack Management
ms.assetid: 61d17e92-a1bf-42d9-b241-400b43b0ec0a
keywords:
- driver stacks WDK networking , managing
- miniport adapters WDK networking , driver stacks
- miniport drivers WDK networking , miniport adapters
- NDIS miniport drivers WDK , miniport adapters
- protocol bindings WDK networking
- protocol drivers WDK net
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Stack Management





NDIS 6.0 introduced the ability to pause and restart a driver stack. To support the stack management features that NDIS 6.0 provides, you must rewrite legacy drivers.

NDIS 6.0 also introduced NDIS filter drivers. Filter drivers can monitor and modify the interaction between protocol drivers and miniport drivers. Filter drivers are easier to implement and have less processing overhead than NDIS 5.*x* intermediate drivers. For these reasons, you should use filter drivers instead of filter intermediate drivers.

A driver stack contains the following logical elements:

<a href="" id="miniport-adapter"></a>Miniport Adapter  
A *miniport adapter* is an adapter instance of an NDIS miniport driver or intermediate driver. The virtual miniport of an intermediate driver is a miniport adapter. NDIS configures the other elements of a driver stack over a miniport adapter after a device becomes available.

<a href="" id="protocol-binding"></a>Protocol Binding  
A *protocol binding* is a binding instance of a protocol driver. A protocol binding binds an NDIS protocol driver to a miniport adapter. Multiple protocol drivers can bind to a miniport adapter.

<a href="" id="filter-module"></a>Filter Module  
A *filter module* is an instance of a filter driver. NDIS can pause a driver stack to insert, remove, or reconfigure a filter module. Filter modules can monitor and modify the behavior of a miniport adapter.

The following topics provide more information about the driver stack, driver states, and driver stack operations:

-   [NDIS Driver Stack](ndis-driver-stack.md)
-   [Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)
-   [Binding States of a Protocol Driver](binding-states-of-a-protocol-driver.md)
-   [Module States of a Filter Driver](module-states-of-a-filter-driver.md)
-   [NDIS Stack Operations](ndis-stack-operations.md)

## Related topics


[NDIS Filter Drivers](ndis-filter-drivers.md)

[NDIS Intermediate Drivers](ndis-intermediate-drivers.md)

 

 






