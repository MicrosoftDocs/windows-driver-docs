---
title: Supplying Fence Identifiers
description: Supplying Fence Identifiers
ms.assetid: 0ec8a4eb-c441-47ae-b5de-d86e6065ffd4
keywords:
- fence identifiers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supplying Fence Identifiers


The Microsoft DirectX graphics kernel subsystem supplies an identical fence identifier in the **SubmissionFenceId** members of the [**DXGKARG\_PATCH**](https://msdn.microsoft.com/library/windows/hardware/ff557610) and [**DXGKARG\_SUBMITCOMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff559490) structures in calls to the display miniport driver's [**DxgkDdiPatch**](https://msdn.microsoft.com/library/windows/hardware/ff559737) and [**DxgkDdiSubmitCommand**](https://msdn.microsoft.com/library/windows/hardware/ff560790) functions. Depending on how the graphics hardware is implemented, the driver is only required to use the fence identifier passed to one of either the *DxgkDdiPatch* or *DxgkDdiSubmitCommand* function for the following reasons:

-   The driver uses the fence identifier passed to *DxgkDdiPatch* to write into the end of the direct memory access (DMA) buffer.

-   The driver uses the fence identifier passed to *DxgkDdiSubmitCommand* to write into the ring buffer, which is the buffer where DMA buffers are queued for execution by the graphics processing unit (GPU) (most GPU types use a DMA buffer queuing model).

 

 





