---
title: Programming Installation for Plug and Play Serial Ports and COM Ports
description: Programming Installation for Plug and Play Serial Ports and COM Ports
keywords:
- Serial driver WDK , Plug and Play devices
- Plug and Play serial devices WDK
- serial devices WDK , Plug and Play
ms.date: 03/17/2022
---

# Programming Installation for Plug and Play Serial Ports and COM Ports

> [!NOTE]
> This topic describes programming traditional COM ports. For information on USB attached serial ports, see [USB serial driver (Usbser.sys)](../usbcon/usb-driver-installation-based-on-compatible-ids.md).

By default, the combined operation of the Ports class installer and the Serial function driver configure a serial port as a COM port. Serial creates a COM port device interface for a serial port if the **SerialSkipExternalNaming** entry value for a device does not exist or is set to zero. For more information about how Serial creates a COM port device interface for a COM port and how to override this operation, see [External Naming of COM Ports](external-naming-of-com-ports.md).

The Ports class installer performs the following tasks when it installs a serial port:

1. Selects a COM port number and sets a port name in the **PortName** entry value under the device's hardware key. The port name has the format COM<em>&lt;n&gt;</em>, where *&lt;n&gt;* is the port number. If Serial creates a COM port interface for the serial port, Serial uses the value of **PortName** as the symbolic link name for the COM port.

2. Displays a default property page dialog box, which allows a user to select settings for the port. For information about how to install a custom properties page, see [Create an Advanced Properties Page for a COM Port](installing-an-advanced-properties-page-for-a-com-port.md).

3. Sets the device friendly name for the device. You obtain the name using the SPDRP\_FRIENDLYNAME flag with **SetupDiGetDeviceRegistryProperty**.

You can supply a co-installer to set [Registry settings for a Plug and Play serial device](registry-settings-for-a-plug-and-play-serial-device.md). If an entry value is not present in the registry, Serial uses a default value for the port.
