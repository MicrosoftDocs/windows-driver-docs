---
title: Locking Memory
description: Locking Memory
ms.assetid: bf14e0f7-13cc-4e55-bbb1-a6b6f6b6271f
keywords:
- locking memory WDK display
- GPU stall prevention WDK display
- memory locking WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Locking Memory


## <span id="ddk_locking_memory_gg"></span><span id="DDK_LOCKING_MEMORY_GG"></span>


To keep the graphics processing unit (GPU) from stalling, a preparation worker thread locks memory while the GPU is busy with other operations. However, if a large allocation is completely paged to disk, the GPU might stall while the driver waits for the GPU scheduler to page in the allocation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Locking%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




