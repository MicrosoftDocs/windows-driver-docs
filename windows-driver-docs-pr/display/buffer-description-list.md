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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Buffer Description List


## <span id="ddk_buffer_description_list_gg"></span><span id="DDK_BUFFER_DESCRIPTION_LIST_GG"></span>


DirectX VA operates primarily by passing buffers of data from the host decoder to the hardware accelerator. When a set of buffers is passed from the host to the accelerator, a buffer description list is sent to describe the buffers. A buffer description list is an array of [**DXVA\_BufferDescription**](https://msdn.microsoft.com/library/windows/hardware/ff563122) structures. The buffer description list contains one DXVA\_BufferDescription structure for each buffer in the set of buffers being sent. The buffer description list starts with one or more DXVA\_BufferDescription structures for the first type of buffer being sent. This is followed by one or more DXVA\_BufferDescription structures for the next type of buffer being sent, and so on.

The value of the **dwTypeIndex** member of the [**DXVA\_BufferDescription**](https://msdn.microsoft.com/library/windows/hardware/ff563122) structure specifies what type of buffer is passed from the host to the accelerator.

 

 





