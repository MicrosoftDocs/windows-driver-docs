---
title: Default Allocators
author: windows-driver-content
description: Default Allocators
ms.assetid: ef61a33d-eabf-4449-8d11-cfd97aa2e403
keywords:
- default allocators WDK kernel streaming
- system memory allocators WDK kernel streaming
- memory allocators WDK kernel streaming
- multiple destination sinks WDK kernel streaming
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Default Allocators


## <a href="" id="ddk-default-allocator-ksg"></a>


The default allocator provides a system memory allocator for device drivers that transfer data from system memory and require specific memory allocation properties. When using the default allocator, a filter need only handle the allocator requirements request.

If using the default allocator, minidrivers must set the KSALLOCATOR\_REQUIREMENTF\_SYSTEM\_MEMORY flag in the **RequirementsFlags** member of the relevant [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979) structure. When an IRP\_MJ\_CREATE is submitted and the create type is KSCREATE\_REQUEST\_ALLOCATOR, the filter forwards the IRP to the default allocator handler by calling the [**KsCreateDefaultAllocator**](https://msdn.microsoft.com/library/windows/hardware/ff561641) function. All remaining processing is handled by the default allocator.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Default%20Allocators%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


