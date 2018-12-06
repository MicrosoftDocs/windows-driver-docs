---
title: Requirements for Accessing Attribute Memory of a PCMCIA Device
description: Requirements for Accessing Attribute Memory of a PCMCIA Device
ms.assetid: 8af41eb0-c057-43c9-a50f-b7d88e1bed6a
keywords:
- attribute memory WDK PCMCIA bus , requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for Accessing Attribute Memory of a PCMCIA Device





This section describes the requirements for the following types of access to attribute memory of a PCMCIA device:

<a href="" id="query-device-information"></a>**Query Device Information**  
A driver typically queries the following device information:

-   Identity of the device

-   Device parameters, such as capacity or speed that the driver uses to configure a device

-   Static data, such as a MAC address

Information queries are usually read-only, and are done relatively infrequently.

<a href="" id="configure-a-device"></a>**Configure a Device**  
Some drivers require write access to configuration registers in attribute memory.

A driver usually configures a device infrequently.

Note that the PCMCIA bus driver manages the standard PCMCIA configuration registers in attribute memory. Drivers must not write to these registers. If they do, unpredictable system behavior can occur. System setup and the Plug and Play manager support INF file directives - for example, the [**INF LogConfig Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547448) - that must be used to configure these registers.

<a href="" id="operate-a-device"></a>**Operate a device**  
Some PCMCIA devices use control registers located in attribute memory. Drivers must typically directly access these registers within an ISR. Accesses of this type can be relatively high in frequency, and require fast direct memory access.

 

 





