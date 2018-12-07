---
title: Managing Multiple-Head Memory
description: Managing Multiple-Head Memory
ms.assetid: 37cda124-0c3b-4af4-92b8-329440dd3221
keywords:
- multiple-head hardware WDK DirectX 9.0 , memory management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Multiple-Head Memory


## <span id="ddk_managing_multiple_head_memory_gg"></span><span id="DDK_MANAGING_MULTIPLE_HEAD_MEMORY_GG"></span>


Setting the DDSCAPS2\_ADDITIONALPRIMARY capability bit in the **dwCaps2** member of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure for each surface on the subordinate head notifies that head that these surfaces are the last surfaces that are allocated from the video memory assigned to that head. The subordinate head should then relinquish control of the allocation of its video memory to the master head because the subordinate head is guaranteed that it does not receive subsequent [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) calls for the lifetime of the application.

The driver must ensure that the master head is able to allocate memory that is associated with subordinate heads.

When the runtime calls the driver's [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) function to destroy surfaces on the subordinate head in which the DDSCAPS2\_ADDITIONALPRIMARY capability bit is set, the driver is notified that the subordinate head is again in control of its video memory management.

For the most part, this choice of which head owns video memory is inherent in the existing DirectDraw process. Specifically:

-   The runtime guarantees that no subsequent allocation requests are made on subordinate heads after *DdCreateSurface* calls are made using the DDSCAPS2\_ADDITIONALPRIMARY bit. Therefore, the driver is not required to restrict allocations from its own video memory pool at any time.

-   When the application is terminated or minimized, all surfaces are destroyed. Therefore, all textures that were created by the master head from the subordinate head's pool are cleaned up.

-   If the DDSCAPS2\_ADDITIONALPRIMARY bit is not set for surfaces on subordinate heads, then those heads continue to allocate video memory as if they were stand-alone heads. In fact, such subordinate heads are functionally identical to any other multiple-monitor adapter.

-   The driver is required to provide an implementation in which the master head allocates memory from a subordinate head's pool, including the determination about when a particular resource can be allocated from a subordinate head's pool. Note that the master head does not have any information itself about whether it is participating in a multiple-head scenario. When the master head runs out of its own video memory, it must traverse all the subordinate heads in its group to determine if any of these heads have pools that can be used by the master (in other words, to determine if any of the subordinate heads received *DdCreateSurface* calls with the DDSCAPS2\_ADDITIONALPRIMARY bit set).

-   Finally, note that the runtime guarantees that all heads in the group participate in the multiple-head scenario. Therefore, the driver must only maintain one bit of state indicating whether it is currently in multiple-head mode.

 

 





