---
title: SDV only supports NDIS " version " drivers
description: SDV only supports NDIS drivers which are NDIS version 6.0, 6.1, 6.20, 6.30, 6.40, or 6.50. This driver is not supported.
ms.assetid: D0C5817B-DD76-4164-9C5C-9537E4059167
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SDV only supports NDIS "&lt;version&gt;" drivers


SDV only supports NDIS drivers which are NDIS version 6.0, 6.1, 6.20, 6.30, 6.40, or 6.50. This driver is not supported.

For more information, see [Supported Drivers](supported-drivers.md) and [Determining if Static Driver Verifier supports your driver or library](determining-if-static-driver-verifier-supports-your-driver-or-library.md).

**Note**  If you see this error message and you are running SDV as part of the requirement for [Static Tools Logo Test](https://msdn.microsoft.com/library/windows/hardware/mt219212), it does not mean that the driver will fail the Static Tools Logo Test. You can still create a Driver Verification Log and run the Static Tools Logo Test. See [Creating a Driver Verification Log](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_verification_log). Having a driver model that SDV does not supported does not preclude certification of the driver.

 

 

 





