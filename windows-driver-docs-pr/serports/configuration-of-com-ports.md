---
title: Configuration of COM ports
description: Configuration of COM ports
keywords:
- COM ports WDK serial devices
- serial devices WDK, COM ports
ms.date: 10/19/2022
---

# Configuration of COM ports

A COM port is a type of serial port that complies with the following additional requirements:

- You access the COM port through an instance of the COM port device interface class. The GUID for this class is GUID_DEVINTERFACE_COMPORT, which is defined in Ntddser.h.

- You operate the COM port by using the 16550 UART-compatible interface that is defined in Ntddser.h.

- To ensure compatibility with most applications that access COM ports, you should assign a symbolic link name that uses the standard naming convention `COM<n>`, where `<n>` is the COM port number (for example, COM1). If you use a `COM<n>` name, you must obtain the COM port number `<n>` from the [COM port database](com-port-database.md). COM port numbers should only be used with `COM<n>` names.

By default, the combined operation of the class installer for the Ports [device setup class](../install/overview-of-device-setup-classes.md) and the Serial function driver configure a device as a COM port.

For information about how the Ports class installer and Serial function driver create a COM port device interface for a COM port, see [External naming of COM ports](external-naming-of-com-ports.md).
