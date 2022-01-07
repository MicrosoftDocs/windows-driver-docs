---
title: Installing Serial Ports and COM Ports
description: Installing Serial Ports and COM Ports
keywords:
- serial ports WDK
- COM ports WDK serial devices
- Serial driver WDK , COM ports
ms.date: 04/20/2017
---

# Installing Serial Ports and COM Ports

For most devices, the Ports [device setup class](../install/overview-of-device-setup-classes.md) and the Serial function driver provide the functionality required to operate serial ports and COM ports. To install serial ports and COM ports using these system-supplied components, do the following:

- Provide an INF file that specifies the Ports device setup class and the Serial function driver as the service for the port.

- To configure a serial port as COM port, comply with the requirements that are defined in [Configuration of COM Ports](configuration-of-com-ports.md).

For more information about installing serial ports and COM ports using the Ports device setup class and the Serial function driver, see the following topics:

[Installing Plug and Play Serial Ports and COM Ports](installing-plug-and-play-serial-ports-and-com-ports.md)

[Installing Legacy COM Ports](installing-legacy-com-ports.md)

If you do a custom installation of a COM port, you must comply with the COM port requirements that are defined in [Configuration of COM Ports](configuration-of-com-ports.md).
