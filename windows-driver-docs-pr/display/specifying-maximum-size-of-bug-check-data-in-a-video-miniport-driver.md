---
title: Specifying Maximum Size of Bug-check Data in a Video Miniport Driver
description: Specifying Maximum Size of Bug-check Data in a Video Miniport Driver
ms.assetid: 1644fe85-b5f5-44b5-96b7-258f43607171
keywords:
- BugcheckDataSize
- video miniport driver bug-check data WDK DirectX 9.0
- bug-check data size WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Maximum Size of Bug-check Data in a Video Miniport Driver


## <span id="ddk_specifying_maximum_size_of_bug_check_data_in_a_video_miniport_driv"></span><span id="DDK_SPECIFYING_MAXIMUM_SIZE_OF_BUG_CHECK_DATA_IN_A_VIDEO_MINIPORT_DRIV"></span>


**This topic applies only to Microsoft Windows XP with Service Pack 1 (SP1) and later.**

A video miniport driver must set the value for the *BugcheckDataSize* parameter of the **VideoPortRegisterBugcheckCallback** function to be no greater than 0x0F20 (4000) bytes for Windows XP SP1 and Microsoft Windows Server 2003 releases. In Windows Server 2003 and later releases, the maximum value for *BugcheckDataSize* is the MAX\_SECONDARY\_DUMP\_SIZE constant. The value of this constant might change in releases later than Windows Server 2003.

The Windows XP SP1 DDK documentation incorrectly specified the maximum value for *BugcheckDataSize*.

 

 





