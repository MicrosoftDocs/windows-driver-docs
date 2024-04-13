---
title: Handling Unsupported IOCTL_VIDEO_XXX Requests
description: Handling Unsupported IOCTL_VIDEO_XXX Requests
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- unsupported IOCTL_VIDEO_XXX requests WDK video miniport
- IOCTL_VIDEO_XXX requests WDK video miniport
- I/O WDK video miniport
ms.date: 04/20/2017
---

# Handling Unsupported IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_handling_unsupported_ioctl_video_xxx_requests_gg"></span><span id="DDK_HANDLING_UNSUPPORTED_IOCTL_VIDEO_XXX_REQUESTS_GG"></span>


Every [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) function also must handle the receipt of an unsupported IOCTL\_VIDEO\_*XXX*, as follows:

1.  Set the input VRP's **Status** field to ERROR\_INVALID\_FUNCTION.

2.  Set the input VRP's **Information** field to zero.

3.  Return **TRUE** to indicate the request was processed.

See the [**VIDEO\_REQUEST\_PACKET**](/windows-hardware/drivers/ddi/video/ns-video-_video_request_packet) and [**STATUS\_BLOCK**](/windows-hardware/drivers/ddi/video/ns-video-_status_block) structures for more details.

 

