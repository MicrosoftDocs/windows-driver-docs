---
title: Handling Unsupported IOCTL_VIDEO_XXX Requests
description: Handling Unsupported IOCTL_VIDEO_XXX Requests
ms.assetid: e3a96cc2-bb7f-4060-bf71-d8a63b918329
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- unsupported IOCTL_VIDEO_XXX requests WDK video miniport
- IOCTL_VIDEO_XXX requests WDK video miniport
- I/O WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Unsupported IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_handling_unsupported_ioctl_video_xxx_requests_gg"></span><span id="DDK_HANDLING_UNSUPPORTED_IOCTL_VIDEO_XXX_REQUESTS_GG"></span>


Every [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function also must handle the receipt of an unsupported IOCTL\_VIDEO\_*XXX*, as follows:

1.  Set the input VRP's **Status** field to ERROR\_INVALID\_FUNCTION.

2.  Set the input VRP's **Information** field to zero.

3.  Return **TRUE** to indicate the request was processed.

See the [**VIDEO\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff570547) and [**STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff569732) structures for more details.

 

 





