---
title: Driver type is " xyz ". This driver is not supported by SDV
description: Static Driver Verifier must be able to interpret the driver code, specifically, the driver's entry points and the code in functions and routines that support required driver functionality.
ms.assetid: A8126F46-3CC8-45A8-A16B-884B07C59688
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver type is "&lt;xyz&gt;". This driver is not supported by SDV


Static Driver Verifier must be able to interpret the driver code, specifically, the driver's entry points and the code in functions and routines that support required driver functionality. Static Driver Verifier supports driver that comply with the Windows Driver Model (WDM), the Kernel Mode Driver Framework (KMDF), NDIS, and Storport.

For more information, see [Supported Drivers](supported-drivers.md).

**Note**  If you see this error message and you are running SDV as part of the requirement for [Static Tools Logo Test](https://msdn.microsoft.com/library/windows/hardware/mt219212), it does not mean that the driver will fail the Static Tools Logo Test. You can still create a Driver Verification Log and run the Static Tools Logo Test. See [Creating a Driver Verification Log](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_verification_log). Having a driver model that SDV does not supported does not preclude certification of the driver.

 

 

 





