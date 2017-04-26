---
title: Minimal DirectX 8.0 DDI Support
description: Minimal DirectX 8.0 DDI Support
ms.assetid: 8758e25e-e54f-42e5-a23d-354af634bce9
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , minimal support
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Minimal%20DirectX%208.0%20DDI%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




