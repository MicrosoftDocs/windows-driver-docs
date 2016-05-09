---
title: Overview of Storage Virtual Miniport Drivers
author: windows-driver-content
description: Overview of Storage Virtual Miniport Drivers
ms.assetid: 5aee56e6-610c-4718-8566-9285682049cb
keywords: ["storage virtual miniport drivers WDK , about", "virtual miniport drivers WDK", "miniport drivers WDK storage , virtual"]
---

# Overview of Storage Virtual Miniport Drivers


To extend the usefulness of the Storport interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, Microsoft has defined the Virtual Miniport (VMiniport) driver interface. This interface is designed for miniport drivers that currently have no strict association with the physical hardware. These changes do not remove the restriction on hardware-associated ("physical") miniport drivers to call only Storport routines. Unlike physical miniport drivers, virtual miniport drivers can make calls to Windows Driver Model (WDM) routines, as WDM documentation states. Unless stated otherwise, from this point forward the term "miniport" will be used to refer to a "virtual miniport".

The virtual miniport driver interface frees the miniport from relying on the port driver (Storport) for handling memory and synchronization. The interface enables the virtual miniport driver to do I/O in ways unavailable before now. These changes are targeted at, but not limited to, enabling storage technologies such as iSCSI and Infiniband as well as non-standard storage interfaces in the future.

Use caution when you implement VMiniport drivers. Though the expansions give greater flexibility, they demand greater care in detecting errors, validating paths, and I/O timing. Some examples are provided here, but it is impossible to anticipate all possible results of using kernel interfaces incorrectly.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Overview%20of%20Storage%20Virtual%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


