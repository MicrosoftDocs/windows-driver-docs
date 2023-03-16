---
title: Serial Controller Driver Design Guide
description: You can design a driver or application that uses the serial I/O request interface to communicate with a peripheral device connected to a serial port.
ms.assetid: 66120e14-20dc-4220-b340-c05cbc59dac8
ms.date: 05/04/2022
ms.topic: article
ms.custom: contperf-fy22q4
---

# Serial Controller Driver Design Guide

You can design a driver or application that uses the [serial I/O request interface](serial-i-o-request-interface.md) to communicate with a peripheral device connected to a serial port. A serial port is a hardware communication interface on a serial controller, which is a 16550 UART or compatible device. To control a serial port to which a peripheral device is permanently connected, you can design a custom serial controller driver that works with version 2 of the serial framework extension (SerCx2), which replaces version 1 (SerCx). 

In older versions of Windows, a named serial COM port located on the case of a PC, the inbox Serial.sys and Serenum.sys drivers were used.

> [!NOTE]
> This topic describes programming traditional COM ports. For information on USB attached serial ports, see [USB serial driver (Usbser.sys)](../usbcon/usb-driver-installation-based-on-compatible-ids.md).

## SerCx2

You can write a serial controller driver that works together with version 2 of the serial framework extension (SerCx2) to manage a serial controller. You can also write a peripheral driver for a peripheral device that is connected to a port on a serial controller that is jointly managed by SerCx2 and a serial controller driver. This peripheral driver uses the serial I/O request interface to transfer data to and from the device. An extension-based serial controller driver handles all hardware-specific tasks for the serial controller, but uses SerCx2 to perform many system tasks that are common to all serial controllers. SerCx2 is a system-supplied component starting with Windows 8.1.

SerCx2 relieves the serial controller driver of the processing work required to manage time-outs, and to coordinate I/O transactions that compete for access to the serial controller. As a result, the serial controller driver is smaller and simpler. The hardware vendor for the serial controller supplies an extension-based serial controller driver that manages the hardware-specific functions in the serial controller, and that relies on SerCx2 to perform generic serial-controller tasks. This driver communicates with SerCx2 through the SerCx2 device driver interface.

For more information about SerCx2, see [Using Version 2 of the Serial Framework Extension (SerCx2)](using-version-2-of-the-serial-framework-extension.md).

## In this section

- [Using Version 2 of the Serial Framework Extension (SerCx2)](using-version-2-of-the-serial-framework-extension.md)
- [Previous Versions of Windows - Serial Controller Drivers](serial-drivers-overview.md)
- [Serial IRP major function codes](serial-irp-major-function-codes.md)
- [Serial Port Console Redirection Table (SPCR)](serial-port-console-redirection-table.md)