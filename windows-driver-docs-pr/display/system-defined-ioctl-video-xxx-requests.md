---
title: System-Defined IOCTL_VIDEO_XXX Requests
description: System-Defined IOCTL_VIDEO_XXX Requests
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- I/O WDK video miniport
- system-defined IOCTL_VIDEO_XXX requests WDK video miniport
- IOCTL_VIDEO_XXX requests WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Defined IOCTL\_VIDEO\_XXX Requests


## <span id="ddk_system_defined_ioctl_video_xxx_requests_gg"></span><span id="DDK_SYSTEM_DEFINED_IOCTL_VIDEO_XXX_REQUESTS_GG"></span>


Typically, most video miniport drivers support the following requests:

[**IOCTL\_VIDEO\_QUERY\_NUM\_AVAIL\_MODES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_num_avail_modes)

[**IOCTL\_VIDEO\_QUERY\_AVAIL\_MODES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_avail_modes)

[**IOCTL\_VIDEO\_QUERY\_CURRENT\_MODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_current_mode)

[**IOCTL\_VIDEO\_SET\_CURRENT\_MODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_current_mode)

[**IOCTL\_VIDEO\_RESET\_DEVICE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_reset_device)

[**IOCTL\_VIDEO\_MAP\_VIDEO\_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_map_video_memory)

[**IOCTL\_VIDEO\_UNMAP\_VIDEO\_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_unmap_video_memory)

[**IOCTL\_VIDEO\_SHARE\_VIDEO\_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_share_video_memory)

[**IOCTL\_VIDEO\_UNSHARE\_VIDEO\_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_unshare_video_memory)

[**IOCTL\_VIDEO\_QUERY\_PUBLIC\_ACCESS\_RANGES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_public_access_ranges)

[**IOCTL\_VIDEO\_FREE\_PUBLIC\_ACCESS\_RANGES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_free_public_access_ranges)

[**IOCTL\_VIDEO\_GET\_POWER\_MANAGEMENT**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_power_management)

[**IOCTL\_VIDEO\_SET\_POWER\_MANAGEMENT**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_power_management)

[**IOCTL\_VIDEO\_GET\_CHILD\_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_child_state)

[**IOCTL\_VIDEO\_SET\_CHILD\_STATE\_CONFIGURATION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_child_state_configuration)

[**IOCTL\_VIDEO\_VALIDATE\_CHILD\_STATE\_CONFIGURATION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_validate_child_state_configuration)

Depending on the adapter's features, video miniport drivers can support the following additional requests:

[**IOCTL\_VIDEO\_QUERY\_COLOR\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_color_capabilities)

[**IOCTL\_VIDEO\_SET\_COLOR\_REGISTERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_color_registers) (required if the device has a palette)

[**IOCTL\_VIDEO\_DISABLE\_POINTER**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_disable_pointer)

[**IOCTL\_VIDEO\_ENABLE\_POINTER**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_enable_pointer)

[**IOCTL\_VIDEO\_QUERY\_POINTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_pointer_capabilities)

[**IOCTL\_VIDEO\_QUERY\_POINTER\_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_pointer_attr)

[**IOCTL\_VIDEO\_SET\_POINTER\_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_pointer_attr)

[**IOCTL\_VIDEO\_QUERY\_POINTER\_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_pointer_position)

[**IOCTL\_VIDEO\_SET\_POINTER\_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_pointer_position)

[**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_handle_videoparameters)

[**IOCTL\_VIDEO\_SWITCH\_DUALVIEW**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_switch_dualview)

VGA-compatible SVGA miniport drivers are required to support the following additional requests:

[**IOCTL\_VIDEO\_SAVE\_HARDWARE\_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_save_hardware_state)

[**IOCTL\_VIDEO\_RESTORE\_HARDWARE\_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_restore_hardware_state)

[**IOCTL\_VIDEO\_DISABLE\_CURSOR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_disable_cursor)

[**IOCTL\_VIDEO\_ENABLE\_CURSOR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_enable_cursor)

[**IOCTL\_VIDEO\_QUERY\_CURSOR\_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_cursor_attr)

[**IOCTL\_VIDEO\_SET\_CURSOR\_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_cursor_attr)

[**IOCTL\_VIDEO\_QUERY\_CURSOR\_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_cursor_position)

[**IOCTL\_VIDEO\_SET\_CURSOR\_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_cursor_position)

[**IOCTL\_VIDEO\_GET\_BANK\_SELECT\_CODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_bank_select_code)

[**IOCTL\_VIDEO\_SET\_PALETTE\_REGISTERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_palette_registers)

[**IOCTL\_VIDEO\_LOAD\_AND\_SET\_FONT**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_load_and_set_font)

Details for each IOCTL can be found in [Video Miniport Driver I/O Control Codes](/windows-hardware/drivers/ddi/index). Miniport driver writers should not use undocumented system-defined IOCTLs.

 

