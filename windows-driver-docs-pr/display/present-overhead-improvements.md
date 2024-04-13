---
title: Present Overhead Improvements
description: Improvements to internal swap buffers to reduce GPU processing loads
ms.date: 04/20/2017
---

# Present overhead improvements


Starting with Windows 8.1, the Microsoft Direct3D runtime handles internal swap buffers more efficiently, reducing the processing load on the GPU. To support this better performance, Windows Display Driver Model (WDDM) 1.3 and later drivers must support a new present device driver interface (DDI) and new texture formats as shared surfaces:

## <span id="wddm_1.3_present_ddi"></span><span id="WDDM_1.3_PRESENT_DDI"></span>WDDM 1.3 present DDI


These reference topics describe how to implement this capability in your display miniport driver and user-mode display driver:

-   [*pfnPresent1(D3D)*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_present1)
-   [*pfnPresent1(DXGI)*](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions)
-   [**D3DDDIARG\_PRESENT1**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_present1)
-   [**D3DDDIARG\_PRESENTSURFACE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddiarg_presentsurface)
-   [**D3DKMT\_COMPOSITION\_PRESENTHISTORYTOKEN**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_composition_presenthistorytoken)
-   [**DXGI\_DDI\_ARG\_PRESENT1**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_arg_present1)
-   [**DXGI\_DDI\_ARG\_PRESENTSURFACE**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_arg_presentsurface)
-   [**D3DDDI\_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) (new **pfnPresent1** function pointer)
-   [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat) (new **D3DDDIFMT\_G8R8** and **D3DDDIFMT\_R8** constant values)
-   [**D3DKMT\_PRESENT\_MODEL**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_d3dkmt_present_model) (new **D3DKMT\_PM\_REDIRECTED\_COMPOSITION** constant value)
-   [**D3DKMT\_PRESENTHISTORYTOKEN**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_presenthistorytoken) (new **Composition** member)
-   [**DXGI\_DDI\_BASE\_ARGS**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_args) (new **pDXGIDDIBaseFunctions4** member)
-   [**DXGI1\_3\_DDI\_BASE\_FUNCTIONS**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) (new **pfnPresent1** function pointer)

## <span id="Texture_format_support_for_shared_surfaces"></span><span id="texture_format_support_for_shared_surfaces"></span><span id="TEXTURE_FORMAT_SUPPORT_FOR_SHARED_SURFACES"></span>Texture format support for shared surfaces


Drivers should support both sharing resources and shareable backbuffers for these additional texture formats from the [**DXGI\_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) enumeration:

- **DXGI\_FORMAT\_A8\_UNORM**
- **DXGI\_FORMAT\_R8\_UNORM**
- **DXGI\_FORMAT\_R8G8\_UNORM**
- **DXGI\_FORMAT\_BC1\_TYPELESS\\***
- **DXGI\_FORMAT\_BC1\_UNORM**
- **DXGI\_FORMAT\_BC1\_UNORM\_SRGB**
- **DXGI\_FORMAT\_BC2\_TYPELESS\\***
- **DXGI\_FORMAT\_BC2\_UNORM**
- **DXGI\_FORMAT\_BC2\_UNORM\_SRGB**
- **DXGI\_FORMAT\_BC3\_TYPELESS\\***
- **DXGI\_FORMAT\_BC3\_UNORM**
- **DXGI\_FORMAT\_BC3\_UNORM\_SRGB**

In addition, drivers should support the **DXGI\_FORMAT\_L8\_UNORM** placeholder format if they support Microsoft Direct3D 11 and later on Direct3D feature level 9 hardware. **DXGI\_FORMAT\_L8\_UNORM** is functionally equivalent to the **D3DDDIFMT\_L8** format.

Drivers should also support additional texture formats from the [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat) enumeration:

-   **D3DDDIFMT\_G8R8**
-   **D3DDDIFMT\_R8**

 

