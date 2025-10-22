---
title: Buses and Sensors measures
description: Buses and Sensors measures guards against errors and bad user experiences
ms.date: 10/21/2025
ms.topic: concept-article
---

# Buses and Sensors Measures

## Overview

The Buses and Sensors device classes encompass critical hardware connectivity and environmental sensing components that enable modern computing experiences. These device classes include USB connectivity, system buses (PCIe, I2C, SPI), and various sensors (accelerometers, gyroscopes, ambient light, proximity) that provide essential data for adaptive computing, security, and user experience features across desktop, mobile, and IoT scenarios.

**USB** drivers leverage multiple framework options depending on complexity and device type. **WinUSB** provides the simplest path for custom devices, allowing user-mode applications to communicate directly through the WinUSB API without requiring custom kernel drivers. Standard USB device classes utilize inbox drivers like HID (hidusb.sys) for input devices and Mass Storage (usbstor.sys) for storage devices. Complex USB implementations use the **Windows Driver Framework (WDF)** with KMDF for kernel-mode drivers requiring direct hardware access and UMDF for user-mode drivers with enhanced security.

**Buses** such as PCIe, I2C, and SPI rely on specialized frameworks including the **Simple Peripheral Bus (SPB)** framework for I2C/SPI controllers and **PCIe miniport drivers** that integrate with the Windows PCI bus driver architecture.

**Sensors** development primarily uses the **Windows Sensor Framework** and **Sensor Class Extension (SensorsCx)** which provide standardized APIs for environmental, motion, orientation, and biometric sensors. The framework abstracts hardware complexity through the **Universal Sensor Driver Model** enabling consistent sensor data delivery to applications via the **Windows Runtime Sensor APIs**. Modern sensor implementations also leverage the **Human Interface Device (HID)** framework for sensors that report through HID descriptors, and increasingly utilize **Windows IoT Core** extensions for edge computing scenarios where sensors integrate with cloud services and machine learning pipelines
