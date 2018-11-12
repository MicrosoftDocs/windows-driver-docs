---
title: Wall Clock and Link Position Registers
description: Wall Clock and Link Position Registers
ms.assetid: 6764affc-a4f0-4568-aa27-7f12e86b818b
keywords:
- wall clock registers WDK audio
- link position registers WDK audio
- HD Audio, wall clock registers
- High Definition Audio (HD Audio), wall clock registers
- HD Audio, link position registers
- High Definition Audio (HD Audio), link position registers
- clocks WDK audio , HD Audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wall Clock and Link Position Registers


The HD Audio controller contains a 32-bit wall clock counter register that increments at the bit-clock rate of the HD Audio Link and rolls over approximately every 89 seconds. Software uses this counter to synchronize between two or more controller devices by measuring the relative drift between the devices' hardware clocks.

In addition, the HD Audio controller contains a set of link position registers. Each DMA engine has a link position register that indicates the current read or write position of the data that the engine is transmitting over the HD Audio Link. The position register expresses the current position as a byte offset from the beginning of the cyclic buffer:

-   In a render stream, the link position register indicates the cyclic buffer offset of the next byte that the DMA engine will send over the link to the codec.

-   In a capture stream, the link position register indicates the cyclic buffer offset of the next byte that the DMA engine will receive from the codec over the link.

The cyclic buffer offset is simply the offset in bytes of the current read or write position from the start of the cyclic buffer. Upon reaching the end of the buffer, the position wraps around to the start of the buffer and the cyclic buffer offset resets to zero. The cyclic buffer resides in system memory. For more information, see the *Intel High Definition Audio Specification* at the [Intel HD Audio](https://go.microsoft.com/fwlink/p/?linkid=42508) website.

A kernel-mode function driver can read the wall clock and link position registers directly. To enable direct access, the HD Audio bus driver maps the physical memory that contains the registers into system virtual memory. The function driver calls the [**GetWallClockRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536401) or [**GetLinkPositionRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536398) routine to obtain a system virtual address pointer to the wall clock register or a link position register. These two routines are available in both versions of the HD Audio DDI.

The HD Audio controller hardware mirrors the wall clock and link position registers into memory pages that do not contain any of the other registers in the controller. Thus, if the function driver maps the mirrored wall clock or position registers to user mode, no user-mode programs can access any of the controller's other registers. The driver never allows a user-mode program to touch these other registers and program the hardware.

Register mirroring must accommodate the host processor's page size. Depending on the host processor architecture, a typical page size might be 4,096 or 8,192 bytes.

 

 




