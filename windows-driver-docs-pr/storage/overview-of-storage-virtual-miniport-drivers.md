---
title: Overview of Storage Virtual Miniport Drivers
description: Overview of Storage Virtual Miniport Drivers
ms.assetid: 5aee56e6-610c-4718-8566-9285682049cb
keywords:
- storage virtual miniport drivers WDK , about
- virtual miniport drivers WDK
- miniport drivers WDK storage , virtual
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Storage Virtual Miniport Drivers


To extend the usefulness of the Storport interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, Microsoft has defined the Virtual Miniport (VMiniport) driver interface. This interface is designed for miniport drivers that currently have no strict association with the physical hardware. These changes do not remove the restriction on hardware-associated ("physical") miniport drivers to call only Storport routines. Unlike physical miniport drivers, virtual miniport drivers can make calls to Windows Driver Model (WDM) routines, as WDM documentation states. Unless stated otherwise, from this point forward the term "miniport" will be used to refer to a "virtual miniport".

The virtual miniport driver interface frees the miniport from relying on the port driver (Storport) for handling memory and synchronization. The interface enables the virtual miniport driver to do I/O in ways unavailable before now. These changes are targeted at, but not limited to, enabling storage technologies such as iSCSI and Infiniband as well as non-standard storage interfaces in the future.

Use caution when you implement VMiniport drivers. Though the expansions give greater flexibility, they demand greater care in detecting errors, validating paths, and I/O timing. Some examples are provided here, but it is impossible to anticipate all possible results of using kernel interfaces incorrectly.

 

 




