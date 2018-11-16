---
title: Simple Peripheral Bus (SPB) Driver Design Guide
description: This section describes how to write a driver for a simple peripheral bus (SPB) controller device or for a peripheral device that is connected to an SPB.
ms.assetid: 7E9F688B-F473-4343-A1E0-525273391935
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Simple Peripheral Bus (SPB) Driver Design Guide


This section describes how to write a driver for a [simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPB) controller device or for a peripheral device that is connected to an SPB. The SPB category includes buses such as I²C and SPI. The hardware vendor for an SPB controller device provides an SPB controller driver to manage the hardware functions in the controller. This driver might support a family of similar controller devices. The hardware vendor for an SPB-connected peripheral device provides an SPB peripheral driver to manage the hardware functions in the peripheral device. This driver might support a family of peripheral devices across a variety of hardware platforms that provide compatible SPBs.

In versions of Windows before Windows 8, the operating system obtained information from SPB-connected devices on a PC motherboard only indirectly through the platform firmware. Starting with Windows 8, hardware vendors can supply Windows drivers to directly control their SPB controllers and their SPB-connected peripheral devices, and to make these devices available for use by the operating system and by applications. For more information, see [SPB Controller Drivers](https://msdn.microsoft.com/library/windows/hardware/hh698220) and [SPB Peripheral Device Drivers](https://msdn.microsoft.com/library/windows/hardware/hh698225).

SPBs are frequently used to connect low-speed peripheral devices to motherboard chipsets and System on a Chip (SoC) modules. An integrated circuit requires fewer pins to connect to a serial bus than to a parallel bus, which transmits multiple bits of data per clock cycle. Typically, SPBs are used in cost-sensitive applications in which low pin counts and simple connections are more important than data transmission speed. Because SPBs run at low speeds and require few electrical connections, they are frequently used in applications in which battery power must be conserved.

For example, the PC motherboard in a laptop computer might use an I²C bus to communicate with a low-speed device that monitors the battery level. Similarly, the SoC module in a smart phone or other mobile device might use an I²C bus to connect to a sensor device, such as an accelerometer, a GPS device, or a temperature sensor.

An SPB is not a Plug and Play bus. Peripheral devices typically have fixed connections to an SPB and cannot be removed. Even if a peripheral device can be unplugged from a slot on an SPB, the slot is typically dedicated to this device. During system startup, the ACPI firmware in the hardware platform enumerates the SPB-connected peripheral devices for the Plug and Play manager, and specifies the hardware resources that are dedicated to each device.

Included in these resources is a connection ID that identifies the device's connection to the SPB. The connection ID encapsulates the information (for example, a bus address and a bus clock frequency) that an SPB controller requires to establish a connection to the device. Other hardware resources might include an interrupt to which the driver connects its ISR. However, the hardware resources for the device do not include memory for device registers. An SPB-connected peripheral device is not memory mapped and can be accessed only through the SPB. For more information, see [Connection IDs for SPB-Connected Peripheral Devices](https://msdn.microsoft.com/library/windows/hardware/hh698216).

An SPB provides no bus-specific means to convey interrupt requests from peripheral devices to the processor. Instead, an SPB-connected peripheral device signals an interrupt through a separate hardware path that lies outside of both the SPB and the SPB controller. The interrupt service routine (ISR) for an SPB-connected peripheral device must run at IRQL = PASSIVE\_LEVEL so that it can synchronously send I/O requests to serially access the hardware registers of the device over the SPB. For more information, see [Interrupts from SPB-Connected Peripheral Devices](https://msdn.microsoft.com/library/windows/hardware/hh698218).

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698220" data-raw-source="[SPB controller drivers](https://msdn.microsoft.com/library/windows/hardware/hh698220)">SPB controller drivers</a></p></td>
<td><p>An SPB controller is a device that controls a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450903" data-raw-source="[simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903)">simple peripheral bus</a> (SPB) and that transfers data to and from the peripheral devices that are connected to the SPB. The hardware vendor for an SPB controller provides an SPB controller driver to manage the hardware functions in the controller.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698225" data-raw-source="[SPB peripheral device drivers](https://msdn.microsoft.com/library/windows/hardware/hh698225)">SPB peripheral device drivers</a></p></td>
<td><p>An SPB peripheral device driver controls a peripheral device that is connected to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450903" data-raw-source="[simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903)">simple peripheral bus</a> (SPB). The hardware registers of this device are available only through the SPB. To read from or write to the device, the driver must send I/O requests to the SPB controller. Only this controller can initiate data transfers to and from the device over the SPB.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919874" data-raw-source="[Test with Multi Interface Test Tool (MITT)](https://msdn.microsoft.com/library/windows/hardware/dn919874)">Test with Multi Interface Test Tool (MITT)</a></p></td>
<td><p>The Multiple Interface Test Tool (MITT) is a test tool for validating hardware and software for simple peripheral buses, such as UART, I2C, SPI, and GPIO. MITT uses the FPGA development board and includes a software package with firmware, test binaries, and drivers that provide an inexpensive test solution.</p></td>
</tr>
</tbody>
</table>

 

 

 




