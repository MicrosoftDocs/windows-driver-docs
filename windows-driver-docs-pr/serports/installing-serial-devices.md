---
title: Programming Serial Device Installation
description: Programming Serial Device Installation
keywords:
- serial devices WDK , programming
ms.date: 06/30/2022
ms.custom: contperf-fy22q4
---

# Programming Serial Device Installation

> [!NOTE]
> This topic describes programming traditional COM ports. For information on USB attached serial ports, see [USB serial driver (Usbser.sys)](../usbcon/usb-driver-installation-based-on-compatible-ids.md).

This section includes the following topics about programming installation for serial devices:

[Programming Serial Ports and COM Port Installation](installing-serial-ports-and-com-ports.md)

[Programming Installation for Plug and Play Serial Ports and COM Ports](installing-plug-and-play-serial-ports-and-com-ports.md)

[Create an Advanced Properties Page for a COM Port](installing-an-advanced-properties-page-for-a-com-port.md)

There are no other serial-specific requirements for installing serial devices.

For general information about installing devices, see the [Device Installation Design Guide](../install/index.md) section.

For more information about serial devices, see [Serial Devices and Drivers](using-serial-sys-and-serenum-sys.md).## In This Topic

This topic includes the following legacy COM port topics.

[Programming Installation for Serial Devices that Use a 16550 UART-Compatible Interface](#programming-installation-for-serial-devices-that-use-a-16550-uart-compatible-interface)

[Programming Installation for Serenum Devices](#programming-installation-for-serenum-devices)

[Programming Installation for Legacy COM Ports](#programming-installation-for-legacy-com-ports)

## Programming Installation for Serial Devices that Use a 16550 UART-Compatible Interface

To install a Plug and Play device that uses Serial as a lower-level device filter driver, do the following:

- Specify Serial as a lower-level device filter driver in the device's INF file -- see [Installing a Filter Driver](../install/installing-a-filter-driver.md).

- Set the **SerialSkipExternalNaming** entry value for the device to a nonzero value -- see [Registry Settings for a Plug and Play Serial Device](registry-settings-for-a-plug-and-play-serial-device.md).

## Programming Installation for Serenum Devices

To install a device that is enumerated by Serenum, use the following *hardware ID* format for the device:

Serenum\\*XxxxYyyy*

Where: *Xxxx* is a field of four ASCII characters that specify the EISA Manufacturing ID; *Yyyy* is a field of four ASCII characters that specify the Product ID. Serenum IDs are documented in the [Plug and Play External COM Device Specification](/previous-versions/windows/hardware/design/dn614609(v=vs.85))

## Programming Installation for Legacy COM Ports

The Serial function driver always configures a legacy serial port as a [COM port](configuration-of-com-ports.md).

Serial detects the presence of legacy ports by reading corresponding COM port subkeys under the **..\\Services\\Serial\\Parameters** key. To install a legacy COM port, you must set a legacy COM port subkey for the device under this key. The COM port subkey contains the [registry settings for a legacy COM port](registry-settings-for-a-legacy-com-port.md).

When Serial is loaded it determines which legacy ports were not previously detected by checking the **LegacyDiscovered** entry value for a legacy port. If this entry value does not exist or is zero, Serial performs the following tasks:

1. Calls [**IoReportDetectedDevice**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportdetecteddevice) to report the device to the Plug and Play manager.

2. Sets the **LegacyDiscovered** entry value for the port to 0x00000001, which indicates that the port has been reported.

3. Copies some of the entry values under the COM port subkey to the Plug and Play device key for the physical device object (*PDO*) that is returned by **IoReportDetectedDevice**.

4. Serial sets the **PortName** entry value under the Plug and Play device key to the value of the **DosDevices** entry value under the legacy COM port subkey. For all other entry values that Serial copies, it retains the same entry value name. For more information about which entry values that Serial copies, see the Serial sample code provided in the Microsoft Windows Driver Kit (WDK).

The **IoReportDetectedDevice** call marks the port as a root-enumerated device. On subsequent system boots, the Plug and Play manager automatically configures the device based on the information in its INF file.

The Plug and Play manager creates the following [compatible IDs](../install/compatible-ids.md) for a legacy COM port: DETECTEDInternal\\Serial and DETECTED\\Serial.
