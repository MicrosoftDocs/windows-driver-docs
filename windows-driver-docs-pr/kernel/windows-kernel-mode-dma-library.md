---
title: Windows Kernel-Mode DMA Library
description: Windows Kernel-Mode DMA Library
ms.assetid: db6cc33a-474b-44a2-bd55-769ff31abae7
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode DMA Library


To enhance performance, a device may need direct access to memory in a way that bypasses the central processing unit (CPU). This technology is called direct memory access (DMA). Windows provides a DMA library for device driver developers.

For more information about DMA for drivers, see [DMA](https://docs.microsoft.com/windows-hardware/drivers/ddi/index).

For a listing of DMA routines, see [Direct Memory Access (DMA) Library Routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/index).

Note that DMA is a technology for communicating directly between device and memory and is not the same as [Device Memory Access](https://docs.microsoft.com/windows-hardware/drivers/ddi/index), which is a set of macros provided to read and write to I/O ports and CPU registers.

 

 




