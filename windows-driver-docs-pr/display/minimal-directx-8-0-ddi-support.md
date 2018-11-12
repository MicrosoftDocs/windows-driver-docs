---
title: Minimal DirectX 8.0 DDI Support
description: Minimal DirectX 8.0 DDI Support
ms.assetid: 8758e25e-e54f-42e5-a23d-354af634bce9
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , minimal support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minimal DirectX 8.0 DDI Support


## <span id="ddk_minimal_directx_8_0_ddi_support_gg"></span><span id="DDK_MINIMAL_DIRECTX_8_0_DDI_SUPPORT_GG"></span>


DirectX 8.0 provides hardware acceleration by DirectX 7.0 level drivers. However, for a driver to expose any of the new features of DirectX 8.0 such as multiple vertex streams, index buffers, or vertex and pixel shaders, it must identify itself by reporting DirectX 8.0 style capabilities and support the new [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) rendering tokens. In order to support the new D3dDrawPrimitives2 rendering tokens the driver is required to provide basic support for vertex streams and fixed function vertex shaders.

Reporting DirectX 8.0 style capabilities involves the following steps:

-   Handling the new **GetDriverInfo2** variant of the existing [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) entry point.

-   Returning a D3DCAPS8 structure containing the capabilities of the device when requested.

-   Ensuring that defined fields of that structure have certain minimum values.

-   Returning a texture format list that includes DirectX 8.0 style surface format descriptions.

These various requirements are discussed in the following sections.

 

 





