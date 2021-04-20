---
title: GDI Hardware Acceleration
description: GDI Hardware Acceleration
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

The display miniport driver also should set [**DXGK\_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps)-&gt;**SupportKernelModeCommandBuffer** to **TRUE** to indicate that it supports GDI Hardware Acceleration command buffer processing. The driver should report this type of support only if the cache-coherent GPU aperture segment exists and there is no significant performance penalty when the CPU accesses GPU memory.

The following reference topics describe how to use this feature:

<span id="Driver-Implemented_Functions"></span><span id="driver-implemented_functions"></span><span id="DRIVER-IMPLEMENTED_FUNCTIONS"></span>**Driver-Implemented Functions**  
The following functions must be implemented by display miniport drivers that support GDI Hardware Acceleration:

[**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation)

[**DxgkDdiGetStandardAllocationDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata)

[**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm)

<span id="Structures"></span><span id="structures"></span><span id="STRUCTURES"></span>**Structures**
[**D3DKM\_TRANSPARENTBLTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_d3dkm_transparentbltflags)

[**D3DKMDT\_GDISURFACEDATA**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfacedata)

[**D3DKMDT\_GDISURFACEFLAGS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfaceflags)

[**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data)

[**DXGK\_CREATECONTEXTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createcontextflags)

[**DXGK\_CREATEDEVICEFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createdeviceflags)

[**DXGK\_GDIARG\_ALPHABLEND**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_alphablend)

[**DXGK\_GDIARG\_BITBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_bitblt)

[**DXGK\_GDIARG\_CLEARTYPEBLEND**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_cleartypeblend)

[**DXGK\_GDIARG\_COLORFILL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_colorfill)

[**DXGK\_GDIARG\_STRETCHBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_stretchblt)

[**DXGK\_GDIARG\_TRANSPARENTBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_transparentblt)

[**DXGK\_RENDERKM\_COMMAND**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_renderkm_command)

[**DXGK\_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps)

[**DXGKARG\_GETSTANDARDALLOCATIONDRIVERDATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_getstandardallocationdriverdata)

[**DXGKARG\_RENDER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_render)

<span id="Enumerations"></span><span id="enumerations"></span><span id="ENUMERATIONS"></span>**Enumerations**
[**D3DKMDT\_STANDARDALLOCATION\_TYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_standardallocation_type)

[**D3DKMDT\_GDISURFACETYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_gdisurfacetype)

[**DXGK\_GDIROP\_BITBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_gdirop_bitblt)

[**DXGK\_GDIROP\_COLORFILL**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_gdirop_colorfill)

[**DXGK\_RENDERKM\_OPERATION**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_renderkm_operation)

For more details on how to implement GDI Hardware Acceleration in your display miniport driver, see the following topics:

[Setting the Size and Pitch of the Memory Allocation](setting-the-size-and-pitch-of-the-memory-allocation.md)

[Initialization and DMA Buffer Creation](initialization-and-dma-buffer-creation.md)

[Reporting Optional Support for Rendering Operations](reporting-optional-support-for-rendering-operations.md)

[Supporting Kernel-Mode Command Buffers](supporting-kernel-mode-command-buffers.md)

[Specifying GDI Hardware-Accelerated Rendering Operations](specifying-gdi-hardware-accelerated-rendering-operations.md)

 

