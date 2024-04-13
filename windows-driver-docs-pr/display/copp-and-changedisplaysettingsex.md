---
title: COPP and ChangeDisplaySettingsEx
description: COPP and ChangeDisplaySettingsEx
keywords:
- copy protection WDK COPP , ChangeDisplaySettingsEx
- video copy protection WDK COPP , ChangeDisplaySettingsEx
- COPP WDK DirectX VA , ChangeDisplaySettingsEx
- protected video WDK COPP , ChangeDisplaySettingsEx
- ChangeDisplaySettingsEx
- analog content protection WDK COPP
- ACP protection type WDK COPP
ms.date: 04/20/2017
---

# COPP and ChangeDisplaySettingsEx


## <span id="ddk_copp_and_changedisplaysettingsex_gg"></span><span id="DDK_COPP_AND_CHANGEDISPLAYSETTINGSEX_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

Because applications can alter analog content protection (ACP) levels by calling the Microsoft Win32 **ChangeDisplaySettingsEx** function, the video miniport driver should ensure that adjustments to the ACP protection type through **ChangeDisplaySettingsEx** are independent of adjustments made by the **IAMCertifiedOutputProtection** interface. In other words, if the ACP protection type is set on the physical connector through the video miniport driver's [*COPPCommand*](./coppcommand.md) function, the video miniport driver should not permit disabling the ACP protection type on the physical connector through a [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_handle_videoparameters) request. Note that user-mode calls to **ChangeDisplaySettingsEx** initiate IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS requests to the video miniport driver.

For more information about the **ChangeDisplaySettingsEx** function, see the Windows SDK documentation.

 

