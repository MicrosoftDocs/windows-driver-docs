---
title: Debugging Bluetooth Profile Drivers
description: Debugging Bluetooth Profile Drivers
ms.assetid: 3c04017e-7f5c-49d4-ad7e-36c7405133a1
keywords:
- debugging profile drivers WDK Bluetooth
- Bluetooth WDK , debugging profile drivers
- debugging drivers WDK Bluetooth
- profile drivers WDK Bluetooth , debugging
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging Bluetooth Profile Drivers


While you develop your Bluetooth profile driver, you can use [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) to assist with its debugging.

To enable the verification check you must [enable Driver Verifier for Bthusb.sys](https://msdn.microsoft.com/library/windows/hardware/ff551729). If you do not do this, the verification checks will be disabled.

To utilize the verification checks fully, make sure you use the Bluetooth Request Block (BRB) allocation routines, for example, [**BthAllocateBrb**](https://msdn.microsoft.com/library/windows/hardware/ff536634) and [**BthInitializeBrb**](https://msdn.microsoft.com/library/windows/hardware/ff536639), that are provided by the Bluetooth driver stack to [build and send BRBs](building-and-sending-a-brb.md). These routines include additional functionality to help debug profile drivers.

The verification checks can help to catch the following kinds of errors:

-   Attempts to resubmit a BRB before it has been completed

-   Attempts to allocate or initialize an invalid BRB type

-   Attempts to submit a BRB with an invalid size

While debugging your profile driver, you can use the **!analyze-v** debugger command after a BC\_BLUETOOTH\_VERIFIER\_FAULT to obtain an explanation of the fault.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Debugging%20Bluetooth%20Profile%20Drivers%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




