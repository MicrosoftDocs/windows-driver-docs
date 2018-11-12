---
title: GDI Hardware Acceleration
description: GDI Hardware Acceleration
ms.assetid: 03db58e6-a6d5-4b6f-ba71-d22a985f9c57
keywords:
- miniport drivers WDK display
- GDI hardware acceleration WDK display
- Connecting and Configuring Displays (CCD) WDK display
- hardware acceleration with GDI WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Hardware Acceleration


The GDI Hardware Acceleration feature introduced with Windows 7 provides accelerated core graphics device interface (GDI) operations on a graphics processing unit (GPU).

To indicate that the GPU and the driver support this feature, the display miniport driver must set DXGKDDI\_INTERFACE\_VERSION to &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7.

The display miniport driver also should set [**DXGK\_PRESENTATIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562004)-&gt;**SupportKernelModeCommandBuffer** to **TRUE** to indicate that it supports GDI Hardware Acceleration command buffer processing. The driver should report this type of support only if the cache-coherent GPU aperture segment exists and there is no significant performance penalty when the CPU accesses GPU memory.

The following reference topics describe how to use this feature:

<span id="Driver-Implemented_Functions"></span><span id="driver-implemented_functions"></span><span id="DRIVER-IMPLEMENTED_FUNCTIONS"></span>**Driver-Implemented Functions**  
The following functions must be implemented by display miniport drivers that support GDI Hardware Acceleration:

[**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606)

[**DxgkDdiGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff559673)

[**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800)

<span id="Structures"></span><span id="structures"></span><span id="STRUCTURES"></span>**Structures**
[**D3DKM\_TRANSPARENTBLTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff548468)

[**D3DKMDT\_GDISURFACEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff546021)

[**D3DKMDT\_GDISURFACEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff546031)

[**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169)

[**DXGK\_CREATECONTEXTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff561037)

[**DXGK\_CREATEDEVICEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff561039)

[**DXGK\_GDIARG\_ALPHABLEND**](https://msdn.microsoft.com/library/windows/hardware/ff561074)

[**DXGK\_GDIARG\_BITBLT**](https://msdn.microsoft.com/library/windows/hardware/ff561079)

[**DXGK\_GDIARG\_CLEARTYPEBLEND**](https://msdn.microsoft.com/library/windows/hardware/ff561082)

[**DXGK\_GDIARG\_COLORFILL**](https://msdn.microsoft.com/library/windows/hardware/ff561083)

[**DXGK\_GDIARG\_STRETCHBLT**](https://msdn.microsoft.com/library/windows/hardware/ff561089)

[**DXGK\_GDIARG\_TRANSPARENTBLT**](https://msdn.microsoft.com/library/windows/hardware/ff561091)

[**DXGK\_RENDERKM\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff562026)

[**DXGK\_PRESENTATIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562004)

[**DXGKARG\_GETSTANDARDALLOCATIONDRIVERDATA**](https://msdn.microsoft.com/library/windows/hardware/ff557598)

[**DXGKARG\_RENDER**](https://msdn.microsoft.com/library/windows/hardware/ff557648)

<span id="Enumerations"></span><span id="enumerations"></span><span id="ENUMERATIONS"></span>**Enumerations**
[**D3DKMDT\_STANDARDALLOCATION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff546589)

[**D3DKMDT\_GDISURFACETYPE**](https://msdn.microsoft.com/library/windows/hardware/ff546039)

[**DXGK\_GDIROP\_BITBLT**](https://msdn.microsoft.com/library/windows/hardware/ff561095)

[**DXGK\_GDIROP\_COLORFILL**](https://msdn.microsoft.com/library/windows/hardware/ff561102)

[**DXGK\_RENDERKM\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff562029)

For more details on how to implement GDI Hardware Acceleration in your display miniport driver, see the following topics:

[Setting the Size and Pitch of the Memory Allocation](setting-the-size-and-pitch-of-the-memory-allocation.md)

[Initialization and DMA Buffer Creation](initialization-and-dma-buffer-creation.md)

[Reporting Optional Support for Rendering Operations](reporting-optional-support-for-rendering-operations.md)

[Supporting Kernel-Mode Command Buffers](supporting-kernel-mode-command-buffers.md)

[Specifying GDI Hardware-Accelerated Rendering Operations](specifying-gdi-hardware-accelerated-rendering-operations.md)

 

 





