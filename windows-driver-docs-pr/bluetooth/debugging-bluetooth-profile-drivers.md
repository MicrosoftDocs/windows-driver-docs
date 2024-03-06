---
title: Debugging Bluetooth Profile Drivers
description: Debugging Bluetooth Profile Drivers
keywords:
- debugging profile drivers WDK Bluetooth
- Bluetooth WDK , debugging profile drivers
- debugging drivers WDK Bluetooth
- profile drivers WDK Bluetooth , debugging
ms.date: 01/10/2024
---

# Debugging Bluetooth profile drivers

While you develop your Bluetooth profile driver, you can use [Driver Verifier](../devtest/driver-verifier.md) to assist with its debugging.

To enable the verification check you must [enable Driver Verifier for Bthusb.sys](../devtest/selecting-drivers-to-be-verified.md). If you do not do this, the verification checks will be disabled.

To utilize the verification checks fully, make sure you use the Bluetooth Request Block (BRB) allocation routines, for example, [**BthAllocateBrb**](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbth_allocate_brb) and [**BthInitializeBrb**](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbth_initialize_brb), that are provided by the Bluetooth driver stack to [build and send BRBs](building-and-sending-a-brb.md). These routines include additional functionality to help debug profile drivers.

The verification checks can help to catch the following kinds of errors:

- Attempts to resubmit a BRB before it has been completed

- Attempts to allocate or initialize an invalid BRB type

- Attempts to submit a BRB with an invalid size

While debugging your profile driver, you can use the **!analyze-v** debugger command after a BC\_BLUETOOTH\_VERIFIER\_FAULT to obtain an explanation of the fault.
