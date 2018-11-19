---
title: Features of Serial and Serenum
description: Features of Serial and Serenum
ms.assetid: 47202203-935a-4e1a-9b05-5555f7cbcfa8
keywords:
- serial devices WDK , Serial driver
- serial devices WDK , Serenum driver
- Serial driver WDK , about Serial driver
- Serenum driver WDK , about Serenum driver
- Serial service WDK
- serial drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Features of Serial and Serenum





Starting with Windows 2000, the system-supplied Serial.sys and Serenum.sys drivers are available to manage serial controller devices that have hardware interfaces that are compatible with the 16550 universal asynchronous receiver-transmitter (UART). Serial.sys controls stand-alone serial ports, COM ports, and multiport boards. Serenum.sys enumerates devices that are connected to a serial port that is controlled by Serial.sys or a compatible serial driver.

For a comparison of Serial.sys to the serial framework extensions, SerCx2 and SerCx, see [Serial Controller Drivers Overview](serial-drivers-overview.md). SerCx2 is available starting with Windows 8.1. SerCx is available starting with Windows 8.

Serial implements the Serial service; its executable image is Serial.sys.

Serial is used as:

-   A function driver for legacy and Plug and Play serial devices.

-   A lower-level device filter driver for Plug and Play devices that require a 16550 UART-compatible interface. An example of this configuration is a modem on a [PCMCIA bus](http://go.microsoft.com/fwlink/p/?LinkId=799534).

    Serial's operation as a filter driver is identical to its operation as a function driver.

Serial features the following:

-   Plug and Play, power management, and Windows Management Instrumentation (WMI).

-   Power policy owner for a serial device stack that includes Serial.

-   Support for an unlimited number of stand-alone serial ports, [COM ports](configuration-of-com-ports.md), and multiport boards.

-   Control of interrupts and communication with device hardware.

Serenum implements the Serenum service; its executable image is Serenum.sys.

Serenum is an upper-level device filter driver that is used with a serial port function driver to enumerate the following types of devices that are connected to a serial port:

-   Plug and Play serial devices that comply with *Plug and Play External COM Device Specification, Version 1.00, February 28, 1995*.

-   Pointer devices that comply with legacy mouse detection in Microsoft Windows NT 4.0 and earlier versions.

The combined operation of Serial and Serenum provides the function of a Plug and Play bus driver for a serial port.

Serenum supports Plug and Play and power management.

Serenum does not support the Windows Driver Model, and should only be used with Windows 2000 and later versions.

Starting with Windows 2000, Serenum supports Serial and other serial port function drivers that need to enumerate a serial port. Hardware vendors do not have to create their own enumerator for serial ports. For example, a device driver can use Serenum to enumerate the devices that are attached to the individual serial ports on a multiport device.

 

 




