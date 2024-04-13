---
title: Previous Versions of Windows -  Serial Controller Drivers Overview
description: Windows provides driver support for traditional serial controller devices.
ms.date: 05/04/2022
---

# Previous Versions of Windows - Serial Controller Drivers Overview

Windows provides driver support for traditional serial controller devices. The term *serial controller* refers to a 16550 universal asynchronous receiver-transmitter (UART) or compatible device. A serial controller has a serial port through which it communicates with a serially connected peripheral device. To support serial communication, Windows includes the Serial.sys and Serenum.sys drivers, and versions 1 and 2 of the serial framework extension (SerCx and SerCx2).

## SerCx

In  Windows 8, SerCx is a system-supplied component that supports serial communication between integrated circuits on a printed circuit board. SerCx is an extension to the Kernel-Mode Driver Framework (KMDF). This extension simplifies the development of custom drivers for serial controllers. SerCx assists an extension-based serial controller driver by handling many of the processing tasks that are common to serial controllers. This driver communicates with SerCx through the [SerCx device driver interface](/windows-hardware/drivers/ddi/_serports).

## SerCx2

Starting with Windows 8.1, SerCx was superceded by SerCx2. SerCx2 has many improvements over SerCx to reduce the size and complexity of serial controller drivers. In particular, SerCx2 relieves the serial controller driver of the processing work required to manage time-outs, and to coordinate I/O transactions that compete for access to the serial controller. As a result, the serial controller driver is smaller and simpler. The hardware vendor for the serial controller supplies an extension-based serial controller driver that manages the hardware-specific functions in the serial controller, and that relies on SerCx2 to perform generic serial-controller tasks. This driver communicates with SerCx2 through the [SerCx2 device driver interface](/windows-hardware/drivers/ddi/_serports).

For more information about SerCx2, see [Using Version 2 of the Serial Framework Extension (SerCx2)](using-version-2-of-the-serial-framework-extension.md).

For general information about the driver framework, see [Using WDF to Develop a Driver](../wdf/using-the-framework-to-develop-a-driver.md)

## Serial.sys and Serenum.sys

In older versions of Windows such as Windows 2000, the system-supplied serial driver, Serial.sys, supported stand-alone serial ports, [COM ports](configuration-of-com-ports.md), and multiport boards. The system-supplied serial enumeration driver, Serenum.sys, enumerates devices that are connected to a serial port that is controlled by Serial.sys or a compatible serial port driver. Serial.sys typically controls the COM ports (typically named COM1, COM2, and so on) physically located on the case of a PC that is running Windows. These ports conform loosely to the RS-232 standard, but additionally incorporate de facto standards (for example, for voltage levels, pin connections, and hardware flow control) that have evolved to support PCs. For more information, see [Using Serial.sys and Serenum.sys](using-serial-sys-and-serenum-sys.md).

The Windows driver samples repository on GitHub contains the source code for the [Serial](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/serial) and [Serenum](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/serenum) driver samples, which operate similarly to, and can be installed in place of, the inbox Serial.sys and Serenum.sys drivers.
