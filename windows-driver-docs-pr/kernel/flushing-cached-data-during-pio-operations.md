---
title: Flushing Cached Data during PIO Operations
description: Flushing Cached Data during PIO Operations
ms.assetid: 8b15f1c4-d3c9-4d61-be37-ee1593f9d5e5
keywords: ["flushing cached data", "KeFlushIoBuffers", "PIO transfer operations WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Flushing Cached Data during PIO Operations





On some platforms, the instruction and data caches in the processor exhibit cache coherency anomalies during PIO read operations.

**Note**   To maintain data integrity during their read operations, drivers that use PIO must follow this guideline:
Call [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) at the end of each read operation.

For example, a driver making a PIO transfer from its device to system memory should call **KeFlushIoBuffers** at the end of each device transfer operation. As another example, a driver that reads a sequence of device registers into system memory should call **KeFlushIoBuffers** at the end of the sequence. Otherwise, such a driver might attempt to access data that is still in the processor's data cache, rather than in system memory, on some platforms.

 

**KeFlushIoBuffers** does nothing if the processor can be relied on to maintain cache coherency, so calls to this support routine have almost no overhead in such a platform.

 

 




