---
title: Required DirectX 9.0 Driver Support
description: Required DirectX 9.0 Driver Support
ms.assetid: 9bc68101-c1be-470c-9eb7-9a689a2dd47c
keywords:
- required driver support WDK DirectX 9.0
- DirectX 9.0 driver support WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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









