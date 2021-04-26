---
title: Multiplane overlay resource creation
description: When multiplane overlays are used, these requirements apply to allocations that are created within Microsoft DirectX apps.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiplane overlay resource creation


When multiplane overlays are used, these requirements apply to allocations that are created within Microsoft DirectX apps.

## <span id="DirectX_11_resource_creation"></span><span id="directx_11_resource_creation"></span><span id="DIRECTX_11_RESOURCE_CREATION"></span>DirectX 11 resource creation


When the [*CreateResource(D3D11)*](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createresource) function is called:

-   The **D3D10\_DDI\_BIND\_PRESENT** and **D3D10\_DDI\_RESOURCE\_MISC\_SHARED** constant values are set in the **BindFlags** member of the [**D3D11DDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createresource) structure, indicating that the allocation can be scanned out.
-   It's possible that other bit-field flags in **Flags** will also be set, such as:
    -   **D3D10\_DDI\_BIND\_SHADER\_RESOURCE**
    -   **D3D10\_DDI\_BIND\_RENDER\_TARGET**
    -   **D3D11\_DDI\_BIND\_UNORDERED\_ACCESS**
    -   **D3D11\_DDI\_BIND\_DECODER**
    -   **D3D11\_1DDI\_RESOURCE\_MISC\_RESTRICTED\_CONTENT**
    -   **D3D11\_1DDI\_RESOURCE\_MISC\_RESTRICT\_SHARED\_RESOURCE\_DRIVER**
-   When the [**DXGI\_DDI\_PRIMARY\_DESC**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_primary_desc) structure is passed in the [*CreateResource(D3D11)*](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createresource) call:
    -   [**DXGI\_DDI\_PRIMARY\_DESC**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_primary_desc) has an appropriate value for the **VidPnSourceId** member.
    -   [**DXGI\_DDI\_PRIMARY\_DESC**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_primary_desc).**ModeDesc** matches the current mode.
    -   For multiplane overlay resources, the driver must not set the **DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT** flag value in the **DriverFlags** member of [**DXGI\_DDI\_PRIMARY\_DESC**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_primary_desc).

## <span id="DirectX_9_resource_creation"></span><span id="directx_9_resource_creation"></span><span id="DIRECTX_9_RESOURCE_CREATION"></span>DirectX 9 resource creation


When the [*CreateResource2*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource2) function is called:

-   The **Primary** and **SharedResource** bit-field flags in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE2**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource2) structure are set.
-   It's possible that other bit-field flags in **Flags** will also be set, such as:
    -   **RenderTarget**
    -   **Texture**
    -   **DecodeRenderTarget**
    -   **RestrictedContent**
    -   **RestrictSharedAccess**
-   The **VidPnSourceId** member of the [**D3DDDIARG\_CREATERESOURCE2**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource2) structure is properly initialized.
-   The **RefreshRate** member of the [**D3DDDIARG\_CREATERESOURCE2**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource2) structure contains zero.

 

