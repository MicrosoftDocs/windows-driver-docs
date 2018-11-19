---
title: Supporting NULL DMA Transfers
description: Supporting NULL DMA Transfers
ms.assetid: 74e278ce-d346-4bec-ad07-12f1cd95474a
keywords:
- memory-to-memory data transfers WDK NetDMA , NULL DMA transfers
- data transfers WDK NetDMA , NULL DMA transfers
- transferring data WDK NetDMA , NULL DMA transfers
- DMA transfers WDK NetDMA , NULL DMA transfers
- NetDMA WDK networking , NULL DMA transfe
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NULL DMA Transfers


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




A *NULL DMA transfer* is a zero-length data transfer that is specified in a dynamic memory access (DMA) descriptor. NetDMA providers must provide the completion status for **NULL** DMA transfers.

**Note**  In theory, a DMA engine could improve performance in some cases by not signaling the completion of a **NULL** transfer. However, if the engine does not signal the completion, the NetDMA interface will not receive a notice that the preceding transfers in the linked list of DMA descriptors are complete.

 

Overall performance can be improved in some applications by submitting a list of DMA descriptors without requesting completion notifications for any descriptors except for the last descriptor. The final descriptor in the list could be a **NULL** transfer that provides the completion information for the entire list. If the NetDMA interface submits a **NULL** transfer and requests completion notification in the **NULL** transfer descriptor, this can provide a simple way to ensure that all of the descriptors that were submitted before the **NULL** transfer were processed.

DMA providers must support **NULL** transfers and process the associated DMA descriptor as they would for other DMA descriptors, except that no data transfer should take place. The NET\_DMA\_NULL\_TRANSFER flag in the **ControlFlags** member of the [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure provides an additional optimization that enables hardware to more easily detect **NULL** transfers.

For more information about completing DMA transfers, see [Completing a DMA Transfer](completing-a-dma-transfer.md).

 

 





