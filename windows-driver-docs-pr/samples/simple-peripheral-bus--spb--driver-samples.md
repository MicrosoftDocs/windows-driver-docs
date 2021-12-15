---
title: Simple peripheral bus (SPB) driver samples
description: The driver samples in this directory provide a starting point for writing a custom SPB driver for your device.
ms.date: 11/21/2019
---

# Simple peripheral bus (SPB) driver samples

The driver samples in this directory provide a starting point for writing a custom SPB driver for your device.

| Sample | Description |
| --- | --- |
| [Skeleton I2C Sample Driver](/samples/microsoft/windows-driver-samples/skeleton-i2c-sample-driver) | Demonstrates how to design a KMDF controller driver for Windows that conforms to the simple peripheral bus (SPB) device driver interface (DDI). SPB is an abstraction for low-speed serial buses (for example, I2C and SPI) that allows peripheral drivers to be developed for cross-platform use without any knowledge of the underlying bus hardware or device connections. |
| [SpbTestTool](/samples/microsoft/windows-driver-samples/spbtesttool) | Demonstrates how to open a handle to the [SPB controller](../spb/spb-controller-drivers.md), use the SPB interface from a KMDF driver, and employ GPIO [passive-level interrupts](../wdf/supporting-passive-level-interrupts.md). |
