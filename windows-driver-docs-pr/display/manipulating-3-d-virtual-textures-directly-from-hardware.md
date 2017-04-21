---
title: Manipulating 3-D Virtual Textures Directly from Hardware
description: Manipulating 3-D Virtual Textures Directly from Hardware
ms.assetid: 5390f62d-3359-4f19-ab6c-07239e598b20
keywords:
- three-dimensional textures WDK display
- textures WDK display
- 3-D textures WDK display
- manipulating 3-D textures directly WDK display
- hardware 3-D texture manipulation WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Manipulating 3-D Virtual Textures Directly from Hardware


## <span id="ddk_manipulating_3_d_virtual_textures_directly_from_hardware_gg"></span><span id="DDK_MANIPULATING_3_D_VIRTUAL_TEXTURES_DIRECTLY_FROM_HARDWARE_GG"></span>


The user-mode display driver can create an allocation on top of an existing virtual address (for example, the virtual address for the view of a three-dimensional (3-D) texture file). Creating an allocation on top of an existing virtual address makes the 3-D texture available to hardware manipulation with a system-memory copy. However, in this scenario, the user-mode display driver's *Lock* function must always evict pages from local video memory back to system memory because the virtual address for the allocation was not allocated by the video memory manager. Therefore, the video memory manager cannot transparently remap the virtual address for the texture from system memory to video memory and vice versa. In other words, a virtual address with this property cannot be a mapped view.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Manipulating%203-D%20Virtual%20Textures%20Directly%20from%20Hardware%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




