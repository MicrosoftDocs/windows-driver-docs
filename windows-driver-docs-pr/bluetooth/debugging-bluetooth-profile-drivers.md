---
title: Debugging Bluetooth Profile Drivers
description: Debugging Bluetooth Profile Drivers
ms.assetid: 3c04017e-7f5c-49d4-ad7e-36c7405133a1
keywords:
- debugging profile drivers WDK Bluetooth
- Bluetooth WDK , debugging profile drivers
- debugging drivers WDK Bluetooth
- profile drivers WDK Bluetooth , debugging
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





