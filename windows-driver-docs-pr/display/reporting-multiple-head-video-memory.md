---
title: Reporting Multiple-Head Video Memory
description: Reporting Multiple-Head Video Memory
ms.assetid: 664b60f5-9e19-4dfc-8bd7-73ceccf6cbea
keywords:
- multiple-head hardware WDK DirectX 9.0 , memory reporting
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Multiple-Head Video Memory


## <span id="ddk_reporting_multiple_head_video_memory_gg"></span><span id="DDK_REPORTING_MULTIPLE_HEAD_VIDEO_MEMORY_GG"></span>


In multiple-head mode, the master head must respond to a call to the driver's [*DdGetAvailDriverMemory*](https://msdn.microsoft.com/library/windows/hardware/ff549377) function as if the master head were the only head controlling the multiple-head card. The amount of free memory that the driver returns must include the video memory of any subordinate head whose video memory was surrendered to the master head (that is, any subordinate head that received *DdCreateSurface* calls with the DDSCAPS2\_ADDITIONALPRIMARY bit set).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Multiple-Head%20Video%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




