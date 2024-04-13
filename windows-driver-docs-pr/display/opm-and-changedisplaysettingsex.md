---
title: OPM and ChangeDisplaySettingsEx
description: OPM and ChangeDisplaySettingsEx
ms.date: 04/20/2017
---

# OPM and ChangeDisplaySettingsEx


Because applications can alter analog content protection (ACP) levels by calling the Microsoft Win32 **ChangeDisplaySettingsEx** function, the display miniport driver should ensure that adjustments to the ACP protection type through **ChangeDisplaySettingsEx** are independent of adjustments made by the **IOPMVideoOutput** interface. In other words, if the ACP protection type is set on the physical connector through the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function, the display miniport driver should not permit disabling the ACP protection type on the physical connector through a [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_handle_videoparameters) request. Note that user-mode calls to **ChangeDisplaySettingsEx** initiate IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS requests to the display miniport driver.

For more information about the **ChangeDisplaySettingsEx** function, see the Microsoft Windows SDK documentation.

 

