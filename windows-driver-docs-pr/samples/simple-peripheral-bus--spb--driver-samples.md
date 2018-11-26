---
title: Simple peripheral bus (SPB) driver samples
description: The driver samples in this directory provide a starting point for writing a custom SPB driver for your device.
ms.assetid: E9A667EA-3AE5-4A0E-BC3F-CD442141886B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Simple peripheral bus (SPB) driver samples


The driver samples in this directory provide a starting point for writing a custom SPB driver for your device.

## Simple peripheral bus (SPB)


| Sample Name                | Solution                                                       | Description                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Skeleton I2C Sample Driver | [SkeletonI2C](http://go.microsoft.com/fwlink/p/?LinkId=617969) | Demonstrates how to design a KMDF controller driver for Windows that conforms to the simple peripheral bus (SPB) device driver interface (DDI). SPB is an abstraction for low-speed serial buses (for example, I2C and SPI) that allows peripheral drivers to be developed for cross-platform use without any knowledge of the underlying bus hardware or device connections. |
| SpbTestTool                | [SpbTestTool](http://go.microsoft.com/fwlink/p/?LinkId=617970) | Demonstrates how to open a handle to the [SPB controller](https://docs.microsoft.com/windows-hardware/drivers/spb/spb-controller-drivers), use the SPB interface from a KMDF driver, and employ GPIO [passive-level interrupts](https://docs.microsoft.com/windows-hardware/drivers/wdf/supporting-passive-level-interrupts).                                                 |










