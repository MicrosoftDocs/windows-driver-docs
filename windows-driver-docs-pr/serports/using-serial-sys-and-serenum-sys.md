---
title: Using Serial.sys and Serenum.sys
description: Using Serial.sys and Serenum.sys
keywords:
- serial ports WDK
- serial devices WDK
- ports WDK , serial
- universal asynchronous receiver-transmitters WDK serial devices
- UART WDK serial devices
- function drivers WDK serial ports
- serial drivers WDK
- 16550 UART-compatible interfaces WDK serial devices
- lower-level device filter drivers WDK serial devices
- higher-level device filter drivers WDK serial devices
- filter drivers WDK serial devices
ms.date: 04/20/2017
---

# Using Serial.sys and Serenum.sys

The following system components are available for use with serial controller devices that have hardware interfaces that are compatible with the 16550 universal asynchronous receiver-transmitter (UART):

-   Serial and Serenum drivers

    Serial.sys (Serial) is a system-supplied function driver for serial devices. You can also use Serial as a lower-level device filter driver for any type of Plug and Play device that requires a 16550 UART-compatible interface.

    Serenum.sys (Serenum) is a system-supplied upper-level device filter driver that you can use in conjunction with Serial (or a vendor-supplied function driver) to provide the function of a Plug and Play bus driver for an RS-232 port.

    For more information about the operation of Serial and Serenum, see the following topics:

    - [Serial Controller Drivers Overview](serial-drivers-overview.md)
    - [Features of Serial and Serenum](features-of-serial-and-serenum.md)
    - [Configuration of Serial Devices and Drivers](configuration-of-serial-devices-and-drivers.md)
    - [Operation of Serenum and Serial](operation-of-serenum-and-serial.md)
    - [Registry Settings for Serial](registry-settings-for-serial.md)
    - [Registry Settings for Serenum](registry-settings-for-serenum.md)
    - [Serial Driver Reference](/windows-hardware/drivers/ddi/_serports)
    - [Serenum Driver Reference](/windows-hardware/drivers/ddi/ntddser)
    - Data definitions in the Ntddser.h header file in the WDK.

<!-- -->

- Ports [device setup class](../install/overview-of-device-setup-classes.md)

    The Ports class includes *serial ports* and *COM ports*. A serial port is a serial communication hardware interface on a 16550 UART or compatible device. An RS-232 port on a computer is typically a DB-9 or DB-25 connector that is electrically connected to the serial port on a UART. A COM port is a serial port that complies with additional Windows-specific requirements. For more information, see [Configuration of COM Ports](configuration-of-com-ports.md).

- COM port [device interface class](../install/overview-of-device-interface-classes.md)

    You must use a COM port device interface to access a COM port. (The GUID for the COM port device interface class is [**GUID\_DEVINTERFACE\_COMPORT**](../install/guid-devinterface-comport.md).)

- [COM port database](com-port-database.md) and [COM port database support routines](/windows/win32/api/msports/)

    The COM port database arbitrates the use of COM port numbers by COM ports.

For information about installing serial devices, see [Installing Serial Devices](installing-serial-devices.md).

For general information about the high-level operation of a serial device, see the information about the communications resources that are supported by the Windows Base Services in the Microsoft Windows SDK.

## Serial driver samples

These samples demonstrates serial drivers.

- The [Serial](https://github.com/Microsoft/Windows-driver-samples/tree/master/serial/serial) sample builds a function driver for serial devices.
- The [Serenum](https://github.com/Microsoft/Windows-driver-samples/tree/master/serial/serenum) sample provides Plug and Play functionality of a bus driver for an RS-232 port.
- A simple virtual serial driver (ComPort) and a controller-less modem driver (FakeModem).
    -   [The Virtual serial driver sample (UMDF 1.0)](https://github.com/Microsoft/Windows-driver-samples/tree/master/serial/VirtualSerial)
    -   [The Virtual serial2 driver sample (KMDF)](https://github.com/Microsoft/Windows-driver-samples/tree/master/serial/VirtualSerial2)
