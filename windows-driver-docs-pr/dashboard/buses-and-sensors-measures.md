---
title: Buses and Sensors measures
description: Buses and Sensors measures guards against errors and bad user experiences
ms.date: 10/21/2025
ms.topic: concept-article
---

# Buses and Sensors measures

## Overview

The USB (Universal Serial Bus) device class encompasses a wide variety of USB-connected devices including storage devices, input devices, audio devices, communication devices, and custom USB peripherals. USB is one of the most prevalent connection standards in modern computing, supporting both data transfer and power delivery across multiple generations of the specification.

## USB Driver Development Frameworks

USB drivers on Windows can be built using several different frameworks optimized for specific device types and use cases. **WinUSB** is Microsoft's generic USB driver that provides the most simplified development path for custom USB devices, vendor-specific hardware, and prototyping scenarios. It eliminates the need for custom kernel drivers by allowing user-mode applications to communicate directly with devices through the WinUSB API, though it's limited to bulk, interrupt, and control transfers.

For standard device classes, Windows provides inbox class drivers including HID (hidusb.sys) for input devices, Mass Storage (usbstor.sys) for storage devices, and Audio/Video class drivers for multimedia devices.

For more complex USB devices requiring custom drivers, the Windows Driver Framework (WDF) offers both KMDF for kernel-mode drivers requiring direct hardware access and UMDF for user-mode drivers with enhanced security and stability.
