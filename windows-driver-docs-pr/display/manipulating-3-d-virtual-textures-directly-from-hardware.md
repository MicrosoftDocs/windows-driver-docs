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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Manipulating 3-D Virtual Textures Directly from Hardware


## <span id="ddk_manipulating_3_d_virtual_textures_directly_from_hardware_gg"></span><span id="DDK_MANIPULATING_3_D_VIRTUAL_TEXTURES_DIRECTLY_FROM_HARDWARE_GG"></span>


The user-mode display driver can create an allocation on top of an existing virtual address (for example, the virtual address for the view of a three-dimensional (3-D) texture file). Creating an allocation on top of an existing virtual address makes the 3-D texture available to hardware manipulation with a system-memory copy. However, in this scenario, the user-mode display driver's *Lock* function must always evict pages from local video memory back to system memory because the virtual address for the allocation was not allocated by the video memory manager. Therefore, the video memory manager cannot transparently remap the virtual address for the texture from system memory to video memory and vice versa. In other words, a virtual address with this property cannot be a mapped view.

 

 





