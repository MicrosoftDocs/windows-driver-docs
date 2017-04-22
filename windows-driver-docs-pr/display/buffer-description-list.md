---
title: Buffer Description List
description: Buffer Description List
ms.assetid: 7d820491-2df2-4036-8f3d-e6bcff4cd1f6
keywords:
- video decoding WDK DirectX VA , buffer description list
- decoding video WDK DirectX VA , buffer description list
- picture decoding WDK DirectX VA , buffer description list
- buffers WDK DirectX VA
- buffer description list WDK DirectX VA
- DXVA_BufferDescription
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Buffer Description List


## <span id="ddk_buffer_description_list_gg"></span><span id="DDK_BUFFER_DESCRIPTION_LIST_GG"></span>


DirectX VA operates primarily by passing buffers of data from the host decoder to the hardware accelerator. When a set of buffers is passed from the host to the accelerator, a buffer description list is sent to describe the buffers. A buffer description list is an array of [**DXVA\_BufferDescription**](https://msdn.microsoft.com/library/windows/hardware/ff563122) structures. The buffer description list contains one DXVA\_BufferDescription structure for each buffer in the set of buffers being sent. The buffer description list starts with one or more DXVA\_BufferDescription structures for the first type of buffer being sent. This is followed by one or more DXVA\_BufferDescription structures for the next type of buffer being sent, and so on.

The value of the **dwTypeIndex** member of the [**DXVA\_BufferDescription**](https://msdn.microsoft.com/library/windows/hardware/ff563122) structure specifies what type of buffer is passed from the host to the accelerator.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Buffer%20Description%20List%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




