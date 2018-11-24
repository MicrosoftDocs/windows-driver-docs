---
title: Reporting Multiple-Head Video Memory
description: Reporting Multiple-Head Video Memory
ms.assetid: 664b60f5-9e19-4dfc-8bd7-73ceccf6cbea
keywords:
- multiple-head hardware WDK DirectX 9.0 , memory reporting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Multiple-Head Video Memory


## <span id="ddk_reporting_multiple_head_video_memory_gg"></span><span id="DDK_REPORTING_MULTIPLE_HEAD_VIDEO_MEMORY_GG"></span>


In multiple-head mode, the master head must respond to a call to the driver's [*DdGetAvailDriverMemory*](https://msdn.microsoft.com/library/windows/hardware/ff549377) function as if the master head were the only head controlling the multiple-head card. The amount of free memory that the driver returns must include the video memory of any subordinate head whose video memory was surrendered to the master head (that is, any subordinate head that received *DdCreateSurface* calls with the DDSCAPS2\_ADDITIONALPRIMARY bit set).

 

 





