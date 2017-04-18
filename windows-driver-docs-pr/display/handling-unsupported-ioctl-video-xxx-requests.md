---
title: Handling Unsupported IOCTL\_VIDEO\_XXX Requests
description: Handling Unsupported IOCTL\_VIDEO\_XXX Requests
ms.assetid: e3a96cc2-bb7f-4060-bf71-d8a63b918329
keywords: ["video miniport drivers WDK Windows 2000 , processing requests", "request processing WDK video miniport", "unsupported IOCTL_VIDEO_XXX requests WDK video miniport", "IOCTL_VIDEO_XXX requests WDK video miniport", "I/O WDK video miniport"]
---

# Handling Unsupported IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_handling_unsupported_ioctl_video_xxx_requests_gg"></span><span id="DDK_HANDLING_UNSUPPORTED_IOCTL_VIDEO_XXX_REQUESTS_GG"></span>


Every [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function also must handle the receipt of an unsupported IOCTL\_VIDEO\_*XXX*, as follows:

1.  Set the input VRP's **Status** field to ERROR\_INVALID\_FUNCTION.

2.  Set the input VRP's **Information** field to zero.

3.  Return **TRUE** to indicate the request was processed.

See the [**VIDEO\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff570547) and [**STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff569732) structures for more details.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Unsupported%20IOCTL_VIDEO_XXX%20Requests%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




