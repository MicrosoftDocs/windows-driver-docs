---
title: About Notify Objects
description: About Notify Objects
ms.assetid: 87e4bcb6-dbdc-487d-9e21-0738165bf834
keywords:
- notify objects WDK networking , about notify objects
- network notify objects WDK , about notify objects
- notifications WDK networking , about notify objects
- network configuration subsystem WDK
- subsystem WDK network configuration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# About Notify Objects





A notify object processes notifications that the network configuration subsystem sends to the object on behalf of a specific network component. This network component owns the notify object. Network components that can own a notify object are:

-   Transports such as a protocol driver

-   Services such as an intermediate driver

-   Clients such as a Client for Microsoft Networks

**Note**  Network cards do not support and cannot own notify objects. Physical or virtual network cards that participate in either configuring the network or installing and uninstalling must use INF files or the device co-installer mechanism.
For more information, see [Writing a Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff554011).

 

A notify object performs the following actions:

-   Exposes interface methods to the network configuration subsystem so that the network configuration subsystem can inform the notify object about the occurrence of events on which the notify object requested notification.

-   Calls methods of the network configuration subsystem's public interfaces to perform actions that include but are not limited to installing and removing network devices. For more information, see [Network Configuration Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff559080).

To request and receive notifications and to communicate with each other, the notify object and the network configuration subsystem implement Component Object Model (COM) interfaces.

Notify objects are COM objects that reside within dynamic-link libraries (DLLs). These DLLs are COM *component servers*. Each type of network component is associated with a *class installer* which installs specific types of network components and registers COM *class objects* that are owned by these network components. After the main install phase for network components is complete, the objects are registered. To register a COM class object, the class installer calls the object's DLL entry-point function.

Whenever the operating system installs, upgrades, or removes networking functionality, or whenever applications configure the network, the operating system or those applications must start the network configuration subsystem. After the network configuration subsystem starts, it creates an instance of a notify object, and the notify object performs particular operations.

The following topics describe the types of notifications that notify objects receive and the operations that notify objects perform:

[Notify Object Diagram](notify-object-diagram.md)

[Processing Notifications](processing-notifications.md)

[Installing Network Components](installing-network-components.md)

[Removing Network Components](removing-network-components.md)

[Upgrading Network Components](upgrading-network-components.md)

[Displaying and Changing Properties](displaying-and-changing-properties.md)

[Configuring the Network](configuring-the-network.md)

 

 





