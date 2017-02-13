---
title: Validating Private Data Sent from User Mode to Kernel Mode
description: Validating Private Data Sent from User Mode to Kernel Mode
ms.assetid: 7022af7b-80e7-41a5-bd53-32d7eafc4062
keywords: ["validating private data WDK display", "private data validation WDK display", "invalid private data WDK display"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Validating%20Private%20Data%20Sent%20from%20User%20Mode%20to%20Kernel%20Mode%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




