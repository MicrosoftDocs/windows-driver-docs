---
title: Supporting the DXGI DDI
description: Supporting the DXGI DDI
ms.date: 10/12/2018
---

# Supporting the DXGI DDI

To support the Microsoft DirectX Graphics Infrastructure (DXGI) device driver interface (DDI), the user-mode display driver must include the [*Dxgiddi.h*](/windows-hardware/drivers/ddi/dxgiddi) header file. *Dxgiddi.h* also includes the [*Dxgitype.h*](/windows-hardware/drivers/ddi/dxgitype) header file, which contains definitions that are shared with application-level DXGI constructs. *Dxgiddi.h* defines several user-mode display driver entry points and a DXGI callback function that the driver can use to communicate with the kernel (including the display miniport driver).

The Microsoft Direct3D runtime supplies access to the DXGI DDI in the [**DXGI_DDI_BASE_ARGS**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_args) structure that the **DXGIBaseDDI** member of the [**D3D10DDIARG_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createdevice) structure points to in a call to the [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function. The user-mode display driver supplies pointers to DXGI functions.

The driver implements these functions through members of the structures that the **pDXGIDDIBaseFunctionsXxx** members of **DXGI_DDI_BASE_ARGS** point to. The driver should record the pointer to the DXGI callback function table that the **pDXGIBaseCallbacks** member of **DXGI_DDI_BASE_ARGS** points to for later use. The driver should record the pointer to the DXGI callback function table rather than record the individual pointer to the DXGI callback function because the Direct3D runtime can change the address of the callback function whenever there is no thread inside the user-mode display driver.

A further DXGI user-mode display driver requirement exists for software rasterizers. Such a user-mode display driver (more specifically, any driver that does not support hardware that is shared with the Direct3D version 9 DDI implementation on the graphics adapter) must return the **DXGI_STATUS_NO_REDIRECTION** value instead of the S_OK value from its [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function. This return value indicates to DXGI that it should not use the shared resource presentation path to affect communication with the Desktop Window Manager (DWM). The shared resource presentation path is created when calls to shared-resource functions (that is, [**CreateResource(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createresource) and [**OpenResource(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openresource) functions with the **D3D10_DDI_RESOURCE_MISC_SHARED** flag set) occur. However, DXGI should instead use techniques relevant to a swapchain whose buffers are available only to the CPU. For example, DXGI should move rendered data from the back buffer to the desktop by means other than the shared resource presentation path. In this situation, DXGI actually calls the driver's [**PresentDXGI**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions) function to move rendered data rather than effect communication with the DWM.

## Direct3D Version 10 DXGI Functions

This section describes the Microsoft DirectX Graphics Infrastructure (DXGI) functions that the user-mode display driver DLL supplies to the Microsoft Direct3D version 10 runtime. The driver supplies pointers to DXGI functions through members of the [DXGI_DDI_BASE_FUNCTIONS](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions) structure in a call to the user-mode display driver's [CreateDevice(D3D10)](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

**BltDXGI**: GetGammaCapsDXGI

**PresentDXGI**: QueryResourceResidencyDXGI

**ResolveSharedResourceDXGI**: RotateResourceIdentitiesDXGI

**SetDisplayModeDXGI**: SetResourcePriorityDXGI

## Direct3D Version 11.1 DXGI Functions

This section describes the Microsoft DirectX Graphics Infrastructure (DXGI) functions, implemented by user-mode display drivers, that are added for the Microsoft Direct3D Version 11.1 runtime. Direct3D 11.1 was introduced with Windows 8.

The user-mode display driver DLL exports the [OpenAdapter10_2](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10_2DDI_ADAPTERFUNCS](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure when the runtime calls CreateDevice(D3D10).

The driver supplies pointers to Direct3D version 11.1 DXGI functions through members of the [DXGI1_2_DDI_BASE_FUNCTIONS](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

## Direct3D Version 11.2 DXGI Functions

The reference pages in this section describe Microsoft DirectX Graphics Infrastructure (DXGI) functions, implemented by user-mode display drivers, that are added for the Microsoft Direct3D Version 11.2 runtime. Direct3D 11.2 was introduced with Windows 8.1.

The user-mode display driver DLL exports the OpenAdapter10_2 function and supplies pointers to adapter-specific functions through members of the [D3D10_2DDI_ADAPTERFUNCS](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure when the runtime calls CreateDevice(D3D10).

The driver supplies pointers to Direct3D version 11.2 DXGI functions through members of the [DXGI1_3_DDI_BASE_FUNCTIONS](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

**[PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB](/windows-hardware/drivers/ddi/dxgiddi/nc-dxgiddi-pfnddxgiddi_present_multiplane_overlaycb)**: [PFNDDXGIDDI_PRESENTCB](/windows-hardware/drivers/ddi/dxgiddi/nc-dxgiddi-pfnddxgiddi_presentcb)

**[PFNDDXGIDDI_SUBMITPRESENTBLTTOHWQUEUECB](/windows-hardware/drivers/ddi/dxgiddi/nc-dxgiddi-pfnddxgiddi_submitpresentblttohwqueuecb)**: [PFNDDXGIDDI_SUBMITPRESENTTOHWQUEUECB](/windows-hardware/drivers/ddi/dxgiddi/nc-dxgiddi-pfnddxgiddi_submitpresenttohwqueuecb)

> [!NOTE]
> Additional DXGI functions that are supported by the Direct3D 11.2 runtime are included in the section, [Multiplane overlay functions implemented by the user-mode driver](multiplane-overlay-support.md).
