---
title: User Clip Planes
description: User Clip Planes
ms.assetid: ea0a7b3b-b850-46bd-b39d-927f28e8de2a
keywords:
- clip planes WDK Direct3D
- user-defined clip planes WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# User Clip Planes


## <span id="ddk_user_clip_planes_gg"></span><span id="DDK_USER_CLIP_PLANES_GG"></span>


User-defined clip planes are enabled for the latest DirectX release. These work just like other clip planes but they are settable by the application. The driver must handle these planes by responding to the D3DDP2OP\_SETCLIPPLANE operation code in [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20User%20Clip%20Planes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




