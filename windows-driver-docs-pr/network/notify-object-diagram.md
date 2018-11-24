---
title: Notify Object Diagram
description: Notify Object Diagram
ms.assetid: d7c177c0-2dc6-47ed-97fb-5c87cbbc8d6f
keywords:
- notify objects WDK networking , diagram
- network notify objects WDK , diagram
- network configuration subsystem WDK
- subsystem WDK network configuration
- notifications WDK networking , notifyo object diagram
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notify Object Diagram





The following diagram shows how client applications that install or control networking call the *network configuration subsystem*. This subsystem calls network class installers to install network components and to register notify objects for those components. Notify objects call back to the subsystem to configure the network on behalf of those components that own the objects.

![diagram illustrating how client applications that install or control networking call the network configuration subsystem](images/netcfg.png)

 

 





