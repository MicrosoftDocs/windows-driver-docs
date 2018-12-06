---
title: Starting and Pausing a Miniport Adapter
description: Starting and Pausing a Miniport Adapter
ms.assetid: d278b331-90d9-4d19-bf00-732981962522
keywords:
- miniport adapters WDK networking , starting
- adapters WDK networking , starting
- miniport adapters WDK networking , pausing
- adapters WDK networking , pausing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting and Pausing a Miniport Adapter





NDIS pauses an adapter to stop data flow that could interfere with Plug and Play operations, such as adding or removing a filter driver, or requests, such as setting a packet filter or multicast address list on the NIC. For more information about how to modify a running driver stack, see [Modifying a Running Driver Stack](modifying-a-running-driver-stack.md).

NDIS restarts an adapter from the Paused state. The adapter enters the Paused start after adapter initialization is complete or after a pause operation is complete.

The following topics provide more information about starting and pausing and adapter:

-   [Starting an Adapter](starting-an-adapter.md)
-   [Pausing an Adapter](pausing-an-adapter.md)

 

 





