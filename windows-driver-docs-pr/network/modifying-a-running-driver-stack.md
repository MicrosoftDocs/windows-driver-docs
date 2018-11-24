---
title: Modifying a Running Driver Stack
description: Modifying a Running Driver Stack
ms.assetid: b8279471-50f4-46f5-8c77-d354dd9b94b5
keywords:
- driver stacks WDK networking , modifying a running stack
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying a Running Driver Stack





NDIS modifies a driver stack for operations such as inserting, removing, or reconfiguring a filter module. NDIS can activate or deactivate the bypass mode in a filter module. For more information about bypass mode in filter drivers, see [Data Bypass Mode](data-bypass-mode.md).

**Note**  If filter driver entry points change (that is, because of bypass mode), NDIS pauses and restarts the driver stack. Pause and restart could cause some network packets to be dropped on the transmit path, or receive path. Network protocols that provide a reliable transport mechanism might retry the network I/O operation in the case of a lost packet, but other protocols that do not guarantee reliability do not retry the operation.

 

NDIS modifies a running driver stack as follows:

1.  NDIS pauses the driver stack.

    For more information, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

2.  NDIS modifies the stack.

    For example, to add a filter module, NDIS determines where to insert the new filter module into the stack and creates, inserts, and attaches the filter module.

3.  When a filter module is inserted or deleted, the characteristics of the driver stack might change. In this case, NDIS sends a Plug and Play event notification to all of the protocol bindings and filter modules in the driver stack to notify the drivers of this change.

4.  NDIS restarts the driver stack.

    For more information, see [Restarting a Driver Stack](restarting-a-driver-stack.md).

 

 





