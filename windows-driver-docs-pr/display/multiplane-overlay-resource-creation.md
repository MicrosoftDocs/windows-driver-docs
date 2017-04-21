---
title: Multiplane overlay resource creation
description: When multiplane overlays are used, these requirements apply to allocations that are created within Microsoft DirectX apps.
ms.assetid: B3E9BEF8-5CB8-45A3-9491-19AB1EA3D74F
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiplane overlay resource creation


When multiplane overlays are used, these requirements apply to allocations that are created within Microsoft DirectX apps.

## <span id="DirectX_11_resource_creation"></span><span id="directx_11_resource_creation"></span><span id="DIRECTX_11_RESOURCE_CREATION"></span>DirectX 11 resource creation


When the [*CreateResource(D3D11)*](https://msdn.microsoft.com/library/windows/hardware/ff540694) function is called:

-   The **D3D10\_DDI\_BIND\_PRESENT** and **D3D10\_DDI\_RESOURCE\_MISC\_SHARED** constant values are set in the **BindFlags** member of the [**D3D11DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542062) structure, indicating that the allocation can be scanned out.
-   It's possible that other bit-field flags in **Flags** will also be set, such as:
    -   **D3D10\_DDI\_BIND\_SHADER\_RESOURCE**
    -   **D3D10\_DDI\_BIND\_RENDER\_TARGET**
    -   **D3D11\_DDI\_BIND\_UNORDERED\_ACCESS**
    -   **D3D11\_DDI\_BIND\_DECODER**
    -   **D3D11\_1DDI\_RESOURCE\_MISC\_RESTRICTED\_CONTENT**
    -   **D3D11\_1DDI\_RESOURCE\_MISC\_RESTRICT\_SHARED\_RESOURCE\_DRIVER**
-   When the [**DXGI\_DDI\_PRIMARY\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff557511) structure is passed in the [*CreateResource(D3D11)*](https://msdn.microsoft.com/library/windows/hardware/ff540694) call:
    -   [**DXGI\_DDI\_PRIMARY\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff557511) has an appropriate value for the **VidPnSourceId** member.
    -   [**DXGI\_DDI\_PRIMARY\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff557511).**ModeDesc** matches the current mode.
    -   For multiplane overlay resources, the driver must not set the **DXGI\_DDI\_PRIMARY\_DRIVER\_FLAG\_NO\_SCANOUT** flag value in the **DriverFlags** member of [**DXGI\_DDI\_PRIMARY\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff557511).

## <span id="DirectX_9_resource_creation"></span><span id="directx_9_resource_creation"></span><span id="DIRECTX_9_RESOURCE_CREATION"></span>DirectX 9 resource creation


When the [*CreateResource2*](https://msdn.microsoft.com/library/windows/hardware/hh406287) function is called:

-   The **Primary** and **SharedResource** bit-field flags in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE2**](https://msdn.microsoft.com/library/windows/hardware/hh451074) structure are set.
-   It's possible that other bit-field flags in **Flags** will also be set, such as:
    -   **RenderTarget**
    -   **Texture**
    -   **DecodeRenderTarget**
    -   **RestrictedContent**
    -   **RestrictSharedAccess**
-   The **VidPnSourceId** member of the [**D3DDDIARG\_CREATERESOURCE2**](https://msdn.microsoft.com/library/windows/hardware/hh451074) structure is properly initialized.
-   The **RefreshRate** member of the [**D3DDDIARG\_CREATERESOURCE2**](https://msdn.microsoft.com/library/windows/hardware/hh451074) structure contains zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiplane%20overlay%20resource%20creation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




