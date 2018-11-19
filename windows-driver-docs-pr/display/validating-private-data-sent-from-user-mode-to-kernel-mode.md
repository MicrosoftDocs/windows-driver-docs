---
title: Validating Private Data Sent from User Mode to Kernel Mode
description: Validating Private Data Sent from User Mode to Kernel Mode
ms.assetid: 7022af7b-80e7-41a5-bd53-32d7eafc4062
keywords:
- validating private data WDK display
- private data validation WDK display
- invalid private data WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating Private Data Sent from User Mode to Kernel Mode


A display miniport driver must validate all private data sent from the user-mode display driver to prevent the miniport driver from crashing, not responding (hanging), asserting, or corrupting memory if the private data is invalid. However, because the operating system resets hardware that "hangs," the display miniport driver can send instructions to the graphics processing unit (GPU) that cause the GPU to "hang." Private data can include any of the following items:

-   Command buffer content sent to the miniport driver's [**DxgkDdiRender**](https://msdn.microsoft.com/library/windows/hardware/ff559793) or [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function in the **pCommand** buffer member of the [**DXGKARG\_RENDER**](https://msdn.microsoft.com/library/windows/hardware/ff557648) structure.

-   Data sent to the following miniport driver functions:
    -   The [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function in the **pPrivateDriverData** buffer members of the [**DXGKARG\_CREATEALLOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff557559) and [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures.
    -   The [**DxgkDdiEscape**](https://msdn.microsoft.com/library/windows/hardware/ff559653) function in the **pPrivateDriverData** buffer member of the [**DXGKARG\_ESCAPE**](https://msdn.microsoft.com/library/windows/hardware/ff557588) structure.
    -   The [**DxgkDdiAcquireSwizzlingRange**](https://msdn.microsoft.com/library/windows/hardware/ff559582) function in the **PrivateDriverData** 32-bit member of the [**DXGKARG\_ACQUIRESWIZZLINGRANGE**](https://msdn.microsoft.com/library/windows/hardware/ff557539) structure.
    -   The [**DxgkDdiReleaseSwizzlingRange**](https://msdn.microsoft.com/library/windows/hardware/ff559786) function in the **PrivateDriverData** 32-bit member of the [**DXGKARG\_RELEASESWIZZLINGRANGE**](https://msdn.microsoft.com/library/windows/hardware/ff557644) structure.
    -   The [**DxgkDdiQueryAdapterInfo**](https://msdn.microsoft.com/library/windows/hardware/ff559746) function in the **pInputData** buffer member of the [**DXGKARG\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff557621) structure when the DXGKQAITYPE\_UMDRIVERPRIVATE value is specified in the **Type** member.

 

 





