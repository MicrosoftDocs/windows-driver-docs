---
title: Specifying Maximum Size of Bug-check Data in a Video Miniport Driver
description: Specifying Maximum Size of Bug-check Data in a Video Miniport Driver
ms.assetid: 1644fe85-b5f5-44b5-96b7-258f43607171
keywords:
- BugcheckDataSize
- video miniport driver bug-check data WDK DirectX 9.0
- bug-check data size WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Maximum Size of Bug-check Data in a Video Miniport Driver


## <span id="ddk_specifying_maximum_size_of_bug_check_data_in_a_video_miniport_driv"></span><span id="DDK_SPECIFYING_MAXIMUM_SIZE_OF_BUG_CHECK_DATA_IN_A_VIDEO_MINIPORT_DRIV"></span>


**This topic applies only to Microsoft Windows XP with Service Pack 1 (SP1) and later.**

A video miniport driver must set the value for the *BugcheckDataSize* parameter of the **VideoPortRegisterBugcheckCallback** function to be no greater than 0x0F20 (4000) bytes for Windows XP SP1 and Microsoft Windows Server 2003 releases. In Windows Server 2003 and later releases, the maximum value for *BugcheckDataSize* is the MAX\_SECONDARY\_DUMP\_SIZE constant. The value of this constant might change in releases later than Windows Server 2003.

The Windows XP SP1 DDK documentation incorrectly specified the maximum value for *BugcheckDataSize*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20Maximum%20Size%20of%20Bug-check%20Data%20in%20a%20Video%20Miniport%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




