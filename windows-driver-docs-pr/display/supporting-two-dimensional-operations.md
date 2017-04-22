---
title: Supporting Two-Dimensional Operations
description: Supporting Two-Dimensional Operations
ms.assetid: 09611bba-5b36-4b7d-8d93-a99590eb5bbe
keywords:
- two-dimensional operations WDK DirectX 9.0
- 2D operations WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Two-Dimensional Operations


## <span id="ddk_supporting_two_dimensional_operations_gg"></span><span id="DDK_SUPPORTING_TWO_DIMENSIONAL_OPERATIONS_GG"></span>


The DirectX 9.0 runtime directs a driver to perform two-dimensional (2D) pixel-copy operations differently depending on the version of the driver that the runtime detects. For a DirectX 8.1 and earlier driver, the runtime calls the driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function and synchronizes this call with the [command stream](command-stream.md). For a DirectX 9.0 and later driver, the runtime passes the D3DDP2OP\_BLT, D3DDP2OP\_SURFACEBLT, or D3DDP2OP\_COLORFILL operation code along with the [**D3DHAL\_DP2BLT**](https://msdn.microsoft.com/library/windows/hardware/ff545426), [**D3DHAL\_DP2SURFACEBLT**](https://msdn.microsoft.com/library/windows/hardware/ff545858), or [**D3DHAL\_DP2COLORFILL**](https://msdn.microsoft.com/library/windows/hardware/ff545450) structure respectively in the command stream. DirectX 9.0 and later drivers must support these 2D operation codes.

If the runtime specifies the DDBLT\_COLORFILL flag in a call to a DirectX 8.1 or earlier driver's *DdBlt* function, the runtime converts the D3DCOLOR fill-color type to an explicit pixel value as long as the runtime recognizes the target surface format (that is, the code for the format is one of the codes in the D3DFORMAT enumerated type). If the format is supplied by the vendor and not recognized by the runtime, the runtime passes the D3DCOLOR fill-color type directly to the driver for processing. However, the runtime converts, to explicit pixel values, the D3DCOLOR fill-color types of certain color formats that are used by DirectShow but are otherwise private to the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Two-Dimensional%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




