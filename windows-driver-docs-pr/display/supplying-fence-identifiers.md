---
title: Supplying Fence Identifiers
description: Supplying Fence Identifiers
ms.assetid: 0ec8a4eb-c441-47ae-b5de-d86e6065ffd4
keywords:
- fence identifiers WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supplying Fence Identifiers


The Microsoft DirectX graphics kernel subsystem supplies an identical fence identifier in the **SubmissionFenceId** members of the [**DXGKARG\_PATCH**](https://msdn.microsoft.com/library/windows/hardware/ff557610) and [**DXGKARG\_SUBMITCOMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff559490) structures in calls to the display miniport driver's [**DxgkDdiPatch**](https://msdn.microsoft.com/library/windows/hardware/ff559737) and [**DxgkDdiSubmitCommand**](https://msdn.microsoft.com/library/windows/hardware/ff560790) functions. Depending on how the graphics hardware is implemented, the driver is only required to use the fence identifier passed to one of either the *DxgkDdiPatch* or *DxgkDdiSubmitCommand* function for the following reasons:

-   The driver uses the fence identifier passed to *DxgkDdiPatch* to write into the end of the direct memory access (DMA) buffer.

-   The driver uses the fence identifier passed to *DxgkDdiSubmitCommand* to write into the ring buffer, which is the buffer where DMA buffers are queued for execution by the graphics processing unit (GPU) (most GPU types use a DMA buffer queuing model).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supplying%20Fence%20Identifiers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




