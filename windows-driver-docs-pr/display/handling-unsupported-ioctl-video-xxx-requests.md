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


Every [*HwVidStartIO*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/nc-video-pvideo_hw_start_io) function also must handle the receipt of an unsupported IOCTL\_VIDEO\_*XXX*, as follows:

1.  Set the input VRP's **Status** field to ERROR\_INVALID\_FUNCTION.

2.  Set the input VRP's **Information** field to zero.

3.  Return **TRUE** to indicate the request was processed.

See the [**VIDEO\_REQUEST\_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/ns-video-_video_request_packet) and [**STATUS\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/video/ns-video-_status_block) structures for more details.

 

 





