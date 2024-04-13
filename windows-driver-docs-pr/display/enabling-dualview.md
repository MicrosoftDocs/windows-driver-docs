---
title: Enabling DualView
description: Enabling DualView
keywords:
- DualView WDK video miniport
ms.date: 04/20/2017
---

# Enabling DualView


## <span id="ddk_enabling_dualview_gg"></span><span id="DDK_ENABLING_DUALVIEW_GG"></span>


For a minimal DualView implementation, perform the following actions:

-   Just before the miniport driver's [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter) returns, call the new video port driver entry point, [**VideoPortCreateSecondaryDisplay**](/windows-hardware/drivers/ddi/video/nf-video-videoportcreatesecondarydisplay), to generate a device extension for the secondary view. In the secondary device extension, add two new private members:

    1.  A flag that indicates the device extension is for a secondary display
    2.  A pointer that contains the address of the primary display's device extension
-   Four changes must be made in the miniport driver's [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) callback routine, modifying the way it responds to the four IOCTL requests shown. The fourth item in the following list presents two ways of accomplishing the same outcome.

    1.  In response to the [**IOCTL\_VIDEO\_MAP\_VIDEO\_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_map_video_memory) request, each view's frame buffer pointer and length should be properly set.
    2.  The response to the [**IOCTL\_VIDEO\_SET\_CURRENT\_MODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_current_mode) request should be made specific to the secondary view.
    3.  The response to the [**IOCTL\_VIDEO\_RESET\_DEVICE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_reset_device) request depends on whether the device is the primary or the secondary display. If the device is the primary display, carry out any needed operations. If the device is the secondary display, however, it is recommended that no action be taken.
    4.  Change the response to the [**IOCTL\_VIDEO\_SHARE\_VIDEO\_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_share_video_memory) request, to get a correct map of both views. Note that for DirectDraw implementations, you can modify the DirectDraw function [*DdMapMemory*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mapmemory) to get the correct map of both views.
-   The display driver should take care of the adjustment between the logical frame buffer address and the physical video memory offset. This is especially important for DirectDraw implementations, because in Dualview the primary surface may start anywhere other than memory location 0. The display driver should notify DirectDraw by filling **pHalInfo-&gt;vmiData.pvPrimary** and **pHalInfo-&gt;vmiData.fpPrimary** with the appropriate video memory offsets on handling [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo).

### <span id="Additional_Implementation_Notes"></span><span id="additional_implementation_notes"></span><span id="ADDITIONAL_IMPLEMENTATION_NOTES"></span>Additional Implementation Notes

-   [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) is called only once for the primary device object. Any secondary device objects must be initialized in this call.

-   For a [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode) call in which *bEnable* is set to **FALSE**, the miniport driver should check the status of the other views. It should avoid turning off the video chip while other views are still active.

-   Never assume that drawing operations have the same drawing context (for example, color depth and stride). This is especially important for chips that use tile frame buffers.

-   GDI can only set the primary view on a built-in device. Some systems, such as laptop computers, have built-in monitor devices (LCDs), but can also be connected to external monitors. The miniport driver should mark a view as removable by passing the VIDEO\_DUALVIEW\_REMOVABLE flag when it calls [**VideoPortCreateSecondaryDisplay**](/windows-hardware/drivers/ddi/video/nf-video-videoportcreatesecondarydisplay).

-   On laptop computers in DualView mode, hotkey switches should be disabled. On a video ACPI-enabled system, the miniport driver should reject [**IOCTL\_VIDEO\_VALIDATE\_CHILD\_STATE\_CONFIGURATION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_validate_child_state_configuration) requests.

-   For laptop computers supporting multichild devices, the miniport driver should handle [**IOCTL\_VIDEO\_GET\_CHILD\_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_child_state) requests and return logical child relationships (discussed in the following section).

 

