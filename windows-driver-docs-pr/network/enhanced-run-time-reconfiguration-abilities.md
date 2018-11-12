---
title: Enhanced Run-time Reconfiguration Abilities
description: Enhanced Run-time Reconfiguration Abilities
ms.assetid: 810d3acb-34ba-4b38-9410-dcdf76f1bb65
keywords:
- driver stacks WDK networking , pausing
- driver stacks WDK networking , restarting
- pausing driver stacks WDK networking
- restarting driver stacks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enhanced Run-time Reconfiguration Abilities





NDIS 6.0 introduced the ability to pause and restart a driver stack without having to tear down the stack and build a new one. All NDIS 6.0 and later drivers must support pause and restart services.

Pausing the stack eliminates synchronization problems by putting all drivers in a known state before reconfiguration occurs. The ability to pause also gives NDIS the opportunity to query driver characteristics, and reconfigure other characteristics of the stack.

NDIS can pause a driver stack, for example, to temporarily stop data flow before performing a Plug and Play operation, such as adding or removing a filter driver, or binding or unbinding a protocol driver. NDIS restarts the stack after the reconfiguration takes place.

Miniport and filter drivers handle pause and restart services through function interfaces. Protocol drivers handle pause and restart services through Plug and Play event notifications.

For more information about pause and restart operations, see [Driver Stack Management](driver-stack-management.md).

 

 





