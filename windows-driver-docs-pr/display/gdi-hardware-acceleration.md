---
title: GDI Hardware Acceleration
description: GDI Hardware Acceleration
keywords:
- miniport drivers WDK display
- GDI hardware acceleration WDK display
- Connecting and Configuring Displays (CCD) WDK display
- hardware acceleration with GDI WDK display
ms.date: 12/18/2024
---

# GDI Hardware Acceleration

The GDI Hardware Acceleration feature provides accelerated core graphics device interface (GDI) operations on a GPU. This feature was introduced in Windows 7.

To indicate that the GPU and the driver support this feature, the kernel-mode display miniport driver (KMD) must set DXGKDDI_INTERFACE_VERSION to ```>= DXGKDDI_INTERFACE_VERSION_WIN7```.

The KMD should also set [**DXGK_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps)**->SupportKernelModeCommandBuffer** to TRUE to indicate that it supports GDI Hardware Acceleration command buffer processing. The driver should report this type of support only if the cache-coherent GPU aperture segment exists and there's no significant performance penalty when the CPU accesses GPU memory.

The following reference pages describe how to use this feature:

* KMDs that support GDI Hardware Acceleration must implement the following functions:

  * [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation)
  * [**DxgkDdiGetStandardAllocationDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata)
  * [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm)

* The following structures are used in the GDI Hardware Acceleration feature:

  * [**D3DKM_TRANSPARENTBLTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_d3dkm_transparentbltflags)
  * [**D3DKMDT_GDISURFACEDATA**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfacedata)
  * [**D3DKMDT_GDISURFACEFLAGS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfaceflags)
  * [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data)
  * [**DXGK_CREATECONTEXTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createcontextflags)
  * [**DXGK_CREATEDEVICEFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createdeviceflags)
  * [**DXGK_GDIARG_ALPHABLEND**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_alphablend)
  * [**DXGK_GDIARG_BITBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_bitblt)
  * [**DXGK_GDIARG_CLEARTYPEBLEND**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_cleartypeblend)
  * [**DXGK_GDIARG_COLORFILL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_colorfill)
  * [**DXGK_GDIARG_STRETCHBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_stretchblt)
  * [**DXGK_GDIARG_TRANSPARENTBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gdiarg_transparentblt)
  * [**DXGK_RENDERKM_COMMAND**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_renderkm_command)
  * [**DXGK_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps)
  * [**DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_getstandardallocationdriverdata)
  * [**DXGKARG_RENDER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_render)

* The following enumerations are used in the GDI Hardware Acceleration feature:

  * [**D3DKMDT_STANDARDALLOCATION_TYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_standardallocation_type)
  * [**D3DKMDT_GDISURFACETYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_gdisurfacetype)
  * [**DXGK_GDIROP_BITBLT**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_gdirop_bitblt)
  * [**DXGK_GDIROP_COLORFILL**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_gdirop_colorfill)
  * [**DXGK_RENDERKM_OPERATION**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_renderkm_operation)

For more details on how to implement GDI Hardware Acceleration in your KMD, see the following articles:

[Setting the Size and Pitch of the Memory Allocation](setting-the-size-and-pitch-of-the-memory-allocation.md)

[Initialization and DMA Buffer Creation](initialization-and-dma-buffer-creation.md)

[Reporting Optional Support for Rendering Operations](reporting-optional-support-for-rendering-operations.md)

[Supporting Kernel-Mode Command Buffers](supporting-kernel-mode-command-buffers.md)

[Specifying GDI Hardware-Accelerated Rendering Operations](specifying-gdi-hardware-accelerated-rendering-operations.md)
