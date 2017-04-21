---
title: Present overhead improvements
ms.assetid: 92B282D6-0D04-4352-AE03-E0A7A43711E7
description: Improvements to internal swap buffers to reduce GPU processing loads
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Present overhead improvements


Starting with Windows 8.1, the Microsoft Direct3D runtime handles internal swap buffers more efficiently, reducing the processing load on the GPU. To support this better performance, Windows Display Driver Model (WDDM) 1.3 and later drivers must support a new present device driver interface (DDI) and new texture formats as shared surfaces:

## <span id="wddm_1.3_present_ddi"></span><span id="WDDM_1.3_PRESENT_DDI"></span>WDDM 1.3 present DDI


These reference topics describe how to implement this capability in your display miniport driver and user-mode display driver:

-   [*pfnPresent1(D3D)*](https://msdn.microsoft.com/library/windows/hardware/dn458010)
-   [*pfnPresent1(DXGI)*](https://msdn.microsoft.com/library/windows/hardware/dn469267)
-   [**D3DDDIARG\_PRESENT1**](https://msdn.microsoft.com/library/windows/hardware/dn457997)
-   [**D3DDDIARG\_PRESENTSURFACE**](https://msdn.microsoft.com/library/windows/hardware/dn457998)
-   [**D3DKMT\_COMPOSITION\_PRESENTHISTORYTOKEN**](https://msdn.microsoft.com/library/windows/hardware/dn458001)
-   [**DXGI\_DDI\_ARG\_PRESENT1**](https://msdn.microsoft.com/library/windows/hardware/dn457714)
-   [**DXGI\_DDI\_ARG\_PRESENTSURFACE**](https://msdn.microsoft.com/library/windows/hardware/dn457715)
-   [**D3DDDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff544519) (new **pfnPresent1** function pointer)
-   [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) (new **D3DDDIFMT\_G8R8** and **D3DDDIFMT\_R8** constant values)
-   [**D3DKMT\_PRESENT\_MODEL**](https://msdn.microsoft.com/library/windows/hardware/ff548197) (new **D3DKMT\_PM\_REDIRECTED\_COMPOSITION** constant value)
-   [**D3DKMT\_PRESENTHISTORYTOKEN**](https://msdn.microsoft.com/library/windows/hardware/ff548188) (new **Composition** member)
-   [**DXGI\_DDI\_BASE\_ARGS**](https://msdn.microsoft.com/library/windows/hardware/ff557485) (new **pDXGIDDIBaseFunctions4** member)
-   [**DXGI1\_3\_DDI\_BASE\_FUNCTIONS**](https://msdn.microsoft.com/library/windows/hardware/dn465883) (new **pfnPresent1** function pointer)

## <span id="Texture_format_support_for_shared_surfaces"></span><span id="texture_format_support_for_shared_surfaces"></span><span id="TEXTURE_FORMAT_SUPPORT_FOR_SHARED_SURFACES"></span>Texture format support for shared surfaces


Drivers should support both sharing resources and shareable backbuffers for these additional texture formats from the [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) enumeration:

-   **DXGI\_FORMAT\_A8\_UNORM**
-   **DXGI\_FORMAT\_R8\_UNORM**
-   **DXGI\_FORMAT\_R8G8\_UNORM**
-   **DXGI\_FORMAT\_BC1\_TYPELESS\***
-   **DXGI\_FORMAT\_BC1\_UNORM**
-   **DXGI\_FORMAT\_BC1\_UNORM\_SRGB**
-   **DXGI\_FORMAT\_BC2\_TYPELESS\***
-   **DXGI\_FORMAT\_BC2\_UNORM**
-   **DXGI\_FORMAT\_BC2\_UNORM\_SRGB**
-   **DXGI\_FORMAT\_BC3\_TYPELESS\***
-   **DXGI\_FORMAT\_BC3\_UNORM**
-   **DXGI\_FORMAT\_BC3\_UNORM\_SRGB**

In addition, drivers should support the **DXGI\_FORMAT\_L8\_UNORM** placeholder format if they support Microsoft Direct3D 11 and later on Direct3D feature level 9 hardware. **DXGI\_FORMAT\_L8\_UNORM** is functionally equivalent to the **D3DDDIFMT\_L8** format.

Drivers should also support additional texture formats from the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration:

-   **D3DDDIFMT\_G8R8**
-   **D3DDDIFMT\_R8**

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Present%20overhead%20improvements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




