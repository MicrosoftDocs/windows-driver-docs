---
title: Destroying Objects Associated with a Direct3D Context
description: Destroying Objects Associated with a Direct3D Context
ms.assetid: b464eb31-6062-4c0c-90a2-2de39b5a85ac
keywords:
- memory leaks WDK DirectX 9.0
- context WDK Direct3D , DirectX 9.0
- destroying objects associated with context WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Destroying Objects Associated with a Direct3D Context


## <span id="ddk_destroying_objects_associated_with_a_direct3d_context_gg"></span><span id="DDK_DESTROYING_OBJECTS_ASSOCIATED_WITH_A_DIRECT3D_CONTEXT_GG"></span>


This topic applies to DirectX 7.0 and later.

To prevent memory leaks, a display driver must release all objects associated with a Direct3D context when the driver's [**D3dContextDestroy**](https://msdn.microsoft.com/library/windows/hardware/ff542180) function is called. These objects include, for example, vertex and pixel [shaders](direct3d-shaders.md), [declarations and code for vertex shaders](separating-declarations-and-code-for-vertex-shaders.md), resources for [asynchronous queries](supporting-asynchronous-query-operations.md), and texture resources.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Destroying%20Objects%20Associated%20with%20a%20Direct3D%20Context%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




