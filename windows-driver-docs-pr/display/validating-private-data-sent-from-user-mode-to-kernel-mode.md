---
title: Validating Private Data Sent from User Mode to Kernel Mode
description: Validating Private Data Sent from User Mode to Kernel Mode
keywords:
- validating private data WDK display
- private data validation WDK display
- invalid private data WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating Private Data Sent from User Mode to Kernel Mode


A display miniport driver must validate all private data sent from the user-mode display driver to prevent the miniport driver from crashing, not responding (hanging), asserting, or corrupting memory if the private data is invalid. However, because the operating system resets hardware that "hangs," the display miniport driver can send instructions to the graphics processing unit (GPU) that cause the GPU to "hang." Private data can include any of the following items:

-   Command buffer content sent to the miniport driver's [**DxgkDdiRender**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_render) or [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) function in the **pCommand** buffer member of the [**DXGKARG\_RENDER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_render) structure.

-   Data sent to the following miniport driver functions:
    -   The [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function in the **pPrivateDriverData** buffer members of the [**DXGKARG\_CREATEALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createallocation) and [**DXGK\_ALLOCATIONINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfo) structures.
    -   The [**DxgkDdiEscape**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_escape) function in the **pPrivateDriverData** buffer member of the [**DXGKARG\_ESCAPE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_escape) structure.
    -   The [**DxgkDdiAcquireSwizzlingRange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_acquireswizzlingrange) function in the **PrivateDriverData** 32-bit member of the [**DXGKARG\_ACQUIRESWIZZLINGRANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_acquireswizzlingrange) structure.
    -   The [**DxgkDdiReleaseSwizzlingRange**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_releaseswizzlingrange) function in the **PrivateDriverData** 32-bit member of the [**DXGKARG\_RELEASESWIZZLINGRANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_releaseswizzlingrange) structure.
    -   The [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) function in the **pInputData** buffer member of the [**DXGKARG\_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryadapterinfo) structure when the DXGKQAITYPE\_UMDRIVERPRIVATE value is specified in the **Type** member.

 

