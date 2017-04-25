---
title: System-Defined IOCTL\_VIDEO\_XXX Requests
description: System-Defined IOCTL\_VIDEO\_XXX Requests
ms.assetid: 30309de1-c991-402d-a701-7e88c3367d24
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- I/O WDK video miniport
- system-defined IOCTL_VIDEO_XXX requests WDK video miniport
- IOCTL_VIDEO_XXX requests WDK video miniport
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# System-Defined IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_system_defined_ioctl_video_xxx_requests_gg"></span><span id="DDK_SYSTEM_DEFINED_IOCTL_VIDEO_XXX_REQUESTS_GG"></span>


Typically, most video miniport drivers support the following requests:

[**IOCTL\_VIDEO\_QUERY\_NUM\_AVAIL\_MODES**](https://msdn.microsoft.com/library/windows/hardware/ff567824)

[**IOCTL\_VIDEO\_QUERY\_AVAIL\_MODES**](https://msdn.microsoft.com/library/windows/hardware/ff567816)

[**IOCTL\_VIDEO\_QUERY\_CURRENT\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff567819)

[**IOCTL\_VIDEO\_SET\_CURRENT\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff567846)

[**IOCTL\_VIDEO\_RESET\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff567834)

[**IOCTL\_VIDEO\_MAP\_VIDEO\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff567812)

[**IOCTL\_VIDEO\_UNMAP\_VIDEO\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568153)

[**IOCTL\_VIDEO\_SHARE\_VIDEO\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568149)

[**IOCTL\_VIDEO\_UNSHARE\_VIDEO\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568155)

[**IOCTL\_VIDEO\_QUERY\_PUBLIC\_ACCESS\_RANGES**](https://msdn.microsoft.com/library/windows/hardware/ff567829)

[**IOCTL\_VIDEO\_FREE\_PUBLIC\_ACCESS\_RANGES**](https://msdn.microsoft.com/library/windows/hardware/ff567796)

[**IOCTL\_VIDEO\_GET\_POWER\_MANAGEMENT**](https://msdn.microsoft.com/library/windows/hardware/ff567803)

[**IOCTL\_VIDEO\_SET\_POWER\_MANAGEMENT**](https://msdn.microsoft.com/library/windows/hardware/ff568148)

[**IOCTL\_VIDEO\_GET\_CHILD\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567801)

[**IOCTL\_VIDEO\_SET\_CHILD\_STATE\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff567840)

[**IOCTL\_VIDEO\_VALIDATE\_CHILD\_STATE\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff568156)

Depending on the adapter's features, video miniport drivers can support the following additional requests:

[**IOCTL\_VIDEO\_QUERY\_COLOR\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567817)

[**IOCTL\_VIDEO\_SET\_COLOR\_REGISTERS**](https://msdn.microsoft.com/library/windows/hardware/ff567842) (required if the device has a palette)

[**IOCTL\_VIDEO\_DISABLE\_POINTER**](https://msdn.microsoft.com/library/windows/hardware/ff567786)

[**IOCTL\_VIDEO\_ENABLE\_POINTER**](https://msdn.microsoft.com/library/windows/hardware/ff567793)

[**IOCTL\_VIDEO\_QUERY\_POINTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567826)

[**IOCTL\_VIDEO\_QUERY\_POINTER\_ATTR**](https://msdn.microsoft.com/library/windows/hardware/ff567825)

[**IOCTL\_VIDEO\_SET\_POINTER\_ATTR**](https://msdn.microsoft.com/library/windows/hardware/ff568144)

[**IOCTL\_VIDEO\_QUERY\_POINTER\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff567827)

[**IOCTL\_VIDEO\_SET\_POINTER\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff568145)

[**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805)

[**IOCTL\_VIDEO\_SWITCH\_DUALVIEW**](https://msdn.microsoft.com/library/windows/hardware/ff568151)

VGA-compatible SVGA miniport drivers are required to support the following additional requests:

[**IOCTL\_VIDEO\_SAVE\_HARDWARE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567838)

[**IOCTL\_VIDEO\_RESTORE\_HARDWARE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567835)

[**IOCTL\_VIDEO\_DISABLE\_CURSOR**](https://msdn.microsoft.com/library/windows/hardware/ff567784)

[**IOCTL\_VIDEO\_ENABLE\_CURSOR**](https://msdn.microsoft.com/library/windows/hardware/ff567788)

[**IOCTL\_VIDEO\_QUERY\_CURSOR\_ATTR**](https://msdn.microsoft.com/library/windows/hardware/ff567820)

[**IOCTL\_VIDEO\_SET\_CURSOR\_ATTR**](https://msdn.microsoft.com/library/windows/hardware/ff567847)

[**IOCTL\_VIDEO\_QUERY\_CURSOR\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff567821)

[**IOCTL\_VIDEO\_SET\_CURSOR\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff567849)

[**IOCTL\_VIDEO\_GET\_BANK\_SELECT\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff567799)

[**IOCTL\_VIDEO\_SET\_PALETTE\_REGISTERS**](https://msdn.microsoft.com/library/windows/hardware/ff568142)

[**IOCTL\_VIDEO\_LOAD\_AND\_SET\_FONT**](https://msdn.microsoft.com/library/windows/hardware/ff567809)

Details for each IOCTL can be found in [Video Miniport Driver I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff570515). Miniport driver writers should not use undocumented system-defined IOCTLs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20System-Defined%20IOCTL_VIDEO_XXX%20Requests%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




