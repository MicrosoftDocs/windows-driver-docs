---
title: Intermediate Driver Design Concepts
description: Intermediate Driver Design Concepts
ms.assetid: cee13268-5df0-4d71-a115-3168c56be06c
keywords:
- intermediate drivers WDK networking , writing
- NDIS intermediate drivers WDK , writing
- writing NDIS intermediate drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver Design Concepts





This section provides some basic information to help you start writing an NDIS intermediate driver. To write an NDIS intermediate driver, you must understand the NDIS miniport driver and protocol driver operations and functions.

The MUX intermediate driver sample in the Microsoft Windows Driver Kit (WDK) provides a basic example of an *n*-to-one MUX intermediate driver that you can adapt to your specific needs.

The virtual miniport of an NDIS intermediate driver must be deserialized. *Deserialized drivers* serialize the operation of their own *MiniportXxx* functions and queue internally all incoming send network data instead of relying on NDIS to perform these operations. This action results in significantly better full-duplex performance, if the driver's critical sections (code that can be executed by only one thread at a time) are kept small. For more information about deserialized drivers, see [Deserialized NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md).

An NDIS intermediate driver can support only connectionless communication at its virtual miniport. At its protocol interface, however, an NDIS intermediate driver can support either connectionless communication or connection-oriented communication. For more information about connection-oriented communication, see [Connection-Oriented NDIS](connection-oriented-ndis.md).

An intermediate driver is typically layered above one or more NDIS miniport drivers and below a transport driver. Intermediate drivers can also be layered with other intermediate drivers.

The following topics provide additional information about writing NDIS intermediate drivers:

[Intermediate Driver DriverEntry Function](intermediate-driver-driverentry-function.md)

[Dynamic Binding in an Intermediate Driver](dynamic-binding-in-an-intermediate-driver.md)

[Intermediate Driver Query and Set Operations](intermediate-driver-query-and-set-operations.md)

[Intermediate Driver Network Data Management](intermediate-driver-network-data-management.md)

[Receiving Data in an Intermediate Driver](receiving-data-in-an-intermediate-driver.md)

[Transmitting Network Data Through an Intermediate Driver](transmitting-network-data-through-an-intermediate-driver.md)

[Handling PnP Events and Power Management Events in an Intermediate Driver](handling-pnp-events-and-power-management-events-in-an-intermediate-dri.md)

[Intermediate Driver Reset Operations](intermediate-driver-reset-operations.md)

[Status Indications in an Intermediate Driver](status-indications-in-an-intermediate-driver.md)

 

 





