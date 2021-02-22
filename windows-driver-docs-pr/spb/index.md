---
title: Simple Peripheral Bus (SPB) Driver Design Guide
description: This section describes how to write a driver for a simple peripheral bus (SPB) controller device or for a peripheral device that is connected to an SPB.
ms.assetid: 7E9F688B-F473-4343-A1E0-525273391935
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Simple Peripheral Bus (SPB) Driver Design Guide

This section describes how to write a driver for a [simple peripheral bus](/previous-versions/hh450903(v=vs.85)) (SPB) controller device or for a peripheral device that is connected to an SPB. The SPB category includes buses such as I²C and SPI. The hardware vendor for an SPB controller device provides an SPB controller driver to manage the hardware functions in the controller. This driver might support a family of similar controller devices. The hardware vendor for an SPB-connected peripheral device provides an SPB peripheral driver to manage the hardware functions in the peripheral device. This driver might support a family of peripheral devices across a variety of hardware platforms that provide compatible SPBs.

In versions of Windows before Windows 8, the operating system obtained information from SPB-connected devices on a PC motherboard only indirectly through the platform firmware. Starting with Windows 8, hardware vendors can supply Windows drivers to directly control their SPB controllers and their SPB-connected peripheral devices, and to make these devices available for use by the operating system and by applications. For more information, see [SPB Controller Drivers](./spb-controller-drivers.md) and [SPB Peripheral Device Drivers](./spb-peripheral-device-drivers.md).

SPBs are frequently used to connect low-speed peripheral devices to motherboard chipsets and System on a Chip (SoC) modules. An integrated circuit requires fewer pins to connect to a serial bus than to a parallel bus, which transmits multiple bits of data per clock cycle. Typically, SPBs are used in cost-sensitive applications in which low pin counts and simple connections are more important than data transmission speed. Because SPBs run at low speeds and require few electrical connections, they are frequently used in applications in which battery power must be conserved.

For example, the PC motherboard in a laptop computer might use an I²C bus to communicate with a low-speed device that monitors the battery level. Similarly, the SoC module in a smart phone or other mobile device might use an I²C bus to connect to a sensor device, such as an accelerometer, a GPS device, or a temperature sensor.

An SPB is not a Plug and Play bus. Peripheral devices typically have fixed connections to an SPB and cannot be removed. Even if a peripheral device can be unplugged from a slot on an SPB, the slot is typically dedicated to this device. During system startup, the ACPI firmware in the hardware platform enumerates the SPB-connected peripheral devices for the Plug and Play manager, and specifies the hardware resources that are dedicated to each device.

Included in these resources is a connection ID that identifies the device's connection to the SPB. The connection ID encapsulates the information (for example, a bus address and a bus clock frequency) that an SPB controller requires to establish a connection to the device. Other hardware resources might include an interrupt to which the driver connects its ISR. However, the hardware resources for the device do not include memory for device registers. An SPB-connected peripheral device is not memory mapped and can be accessed only through the SPB. For more information, see [Connection IDs for SPB-Connected Peripheral Devices](./connection-ids-for-spb-connected-peripheral-devices.md).

An SPB provides no bus-specific means to convey interrupt requests from peripheral devices to the processor. Instead, an SPB-connected peripheral device signals an interrupt through a separate hardware path that lies outside of both the SPB and the SPB controller. The interrupt service routine (ISR) for an SPB-connected peripheral device must run at IRQL = PASSIVE\_LEVEL so that it can synchronously send I/O requests to serially access the hardware registers of the device over the SPB. For more information, see [Interrupts from SPB-Connected Peripheral Devices](./interrupts-from-spb-connected-peripheral-devices.md).
