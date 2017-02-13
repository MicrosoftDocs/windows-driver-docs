---
title: Required DirectX 9.0 Driver Support
description: Required DirectX 9.0 Driver Support
ms.assetid: 9bc68101-c1be-470c-9eb7-9a689a2dd47c
keywords: ["required driver support WDK DirectX 9.0", "DirectX 9.0 driver support WDK"]
---

# Required DirectX 9.0 Driver Support


## <span id="ddk_required_directx_9_0_driver_support_gg"></span><span id="DDK_REQUIRED_DIRECTX_9_0_DRIVER_SUPPORT_GG"></span>


The DirectX 9.0 runtime will supply hardware acceleration if the display driver is a DirectX 7.0 or later driver. However, for a driver to be loaded by the operating system as a version 9.0 driver, it must implement the features that are described in the following sections:

[Supporting Two-Dimensional Operations](supporting-two-dimensional-operations.md)

[Supporting Dynamic Resources](supporting-dynamic-resources.md)

[Supporting Vertex Shader Declarations](supporting-vertex-shader-declarations.md)

[Supporting Stream Offsets](supporting-stream-offsets.md)

[Reporting Support of UBYTE4 Vertex Element](reporting-support-of-ubyte4-vertex-element.md)

[Supporting Commands for Setting Render Target](supporting-commands-for-setting-render-target.md)

[Setting Scissor Rectangle](setting-scissor-rectangle.md)

[Notifying about DirectX Version](notifying-about-directx-version.md)

[Reporting DDI Version](reporting-ddi-version.md)

A DirectX 9.0 version driver must support:

-   Reporting the capabilities of its device by returning a D3DCAPS9 structure when requested. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETD3DCAPS9 value similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this request is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md). D3DCAPS9 contains both DirectX 9.0 and DirectX 8.0 related capabilities.

     

    The driver must continue to report only DirectX 8.0 related capabilities in D3DCAPS8 when queried by the DirectX 8.0 runtime.

-   Setting the D3DFORMAT\_OP\_BUMPMAP flag in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for all surface formats that can support bump mapping in either fixed-function or programmable-pixel pipes.

-   Reporting [support of asynchronous query operations](supporting-asynchronous-query-operations.md), even if the driver just responds by indicating that no query types are supported. For more information, see [Verifying Support of Query Types](verifying-support-of-query-types.md).

     

    Querying asynchronously imposes two new requirements on the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) DDI. For more information, see [Imposing Requirements on the D3dDrawPrimitives2 DDI](imposing-requirements-on-the-d3ddrawprimitives2-ddi.md).

-   Letting applications perform other [processing with busy present queues](processing-with-busy-present-queues.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Required%20DirectX%209.0%20Driver%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




