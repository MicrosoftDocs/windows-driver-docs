---
title: Locking Memory
description: Locking Memory
ms.assetid: bf14e0f7-13cc-4e55-bbb1-a6b6f6b6271f
keywords:
- locking memory WDK display
- GPU stall prevention WDK display
- memory locking WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locking Memory


## <span id="ddk_locking_memory_gg"></span><span id="DDK_LOCKING_MEMORY_GG"></span>


To keep the graphics processing unit (GPU) from stalling, a preparation worker thread locks memory while the GPU is busy with other operations. However, if a large allocation is completely paged to disk, the GPU might stall while the driver waits for the GPU scheduler to page in the allocation.

 

 





