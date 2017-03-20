---
title: New DDSCAPS2 Flags
description: New DDSCAPS2 Flags
ms.assetid: a5171865-7339-422f-8470-154a0aadc496
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , presentation", "presentation WDK DirectX 8.0", "rendering results visible WDK DirectX 8.0", "visible results WDK DirectX 8.0"]
---

# New DDSCAPS2 Flags


## <span id="ddk_new_ddscaps2_flags_gg"></span><span id="DDK_NEW_DDSCAPS2_FLAGS_GG"></span>


A new flag, DDSCAPS2\_DISCARDBACKBUFFER, has been introduced to indicate that preservation of the back buffer is not required. It is set on the primary surface and the back buffers if the application has set D3DSWAPEFFECT\_DISCARD on the **Present** API.

DX8 runtimes now set another new flag, DDSCAPS2\_NOTUSERLOCKABLE, on the primary and the back buffers if the flipping chain is not lockable, or on any render target that is not lockable. This allows drivers to do behind the scenes optimization. Note that it is still possible to lock the surfaces so the driver must handle these cases, but such locks are infrequent and are not expected to be fast.

The driver can also determine whether the depth/stencil buffer is lockable by the presence of the DDSCAPS2\_NOTUSERLOCKABLE flag.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20New%20DDSCAPS2%20Flags%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




