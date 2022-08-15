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
---

# System-Defined IOCTL_VIDEO_XXX Requests

Typically, most video miniport drivers support the following requests:

[**IOCTL_VIDEO_QUERY_NUM_AVAIL_MODES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_num_avail_modes)

[**IOCTL_VIDEO_QUERY_AVAIL_MODES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_avail_modes)

[**IOCTL_VIDEO_QUERY_CURRENT_MODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_current_mode)

[**IOCTL_VIDEO_SET_CURRENT_MODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_current_mode)

[**IOCTL_VIDEO_RESET_DEVICE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_reset_device)

[**IOCTL_VIDEO_MAP_VIDEO_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_map_video_memory)

[**IOCTL_VIDEO_UNMAP_VIDEO_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_unmap_video_memory)

[**IOCTL_VIDEO_SHARE_VIDEO_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_share_video_memory)

[**IOCTL_VIDEO_UNSHARE_VIDEO_MEMORY**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_unshare_video_memory)

[**IOCTL_VIDEO_QUERY_PUBLIC_ACCESS_RANGES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_public_access_ranges)

[**IOCTL_VIDEO_FREE_PUBLIC_ACCESS_RANGES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_free_public_access_ranges)

[**IOCTL_VIDEO_GET_POWER_MANAGEMENT**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_power_management)

[**IOCTL_VIDEO_SET_POWER_MANAGEMENT**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_power_management)

[**IOCTL_VIDEO_GET_CHILD_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_child_state)

[**IOCTL_VIDEO_SET_CHILD_STATE_CONFIGURATION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_child_state_configuration)

[**IOCTL_VIDEO_VALIDATE_CHILD_STATE_CONFIGURATION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_validate_child_state_configuration)

Depending on the adapter's features, video miniport drivers can support the following additional requests:

[**IOCTL_VIDEO_QUERY_COLOR_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_color_capabilities)

[**IOCTL_VIDEO_SET_COLOR_REGISTERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_color_registers) (required if the device has a palette)

[**IOCTL_VIDEO_DISABLE_POINTER**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_disable_pointer)

[**IOCTL_VIDEO_ENABLE_POINTER**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_enable_pointer)

[**IOCTL_VIDEO_QUERY_POINTER_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_pointer_capabilities)

[**IOCTL_VIDEO_QUERY_POINTER_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_pointer_attr)

[**IOCTL_VIDEO_SET_POINTER_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_pointer_attr)

[**IOCTL_VIDEO_QUERY_POINTER_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_pointer_position)

[**IOCTL_VIDEO_SET_POINTER_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_pointer_position)

[**IOCTL_VIDEO_HANDLE_VIDEOPARAMETERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_handle_videoparameters)

[**IOCTL_VIDEO_SWITCH_DUALVIEW**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_switch_dualview)

VGA-compatible SVGA miniport drivers are required to support the following additional requests:

[**IOCTL_VIDEO_SAVE_HARDWARE_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_save_hardware_state)

[**IOCTL_VIDEO_RESTORE_HARDWARE_STATE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_restore_hardware_state)

[**IOCTL_VIDEO_DISABLE_CURSOR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_disable_cursor)

[**IOCTL_VIDEO_ENABLE_CURSOR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_enable_cursor)

[**IOCTL_VIDEO_QUERY_CURSOR_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_cursor_attr)

[**IOCTL_VIDEO_SET_CURSOR_ATTR**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_cursor_attr)

[**IOCTL_VIDEO_QUERY_CURSOR_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_query_cursor_position)

[**IOCTL_VIDEO_SET_CURSOR_POSITION**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_cursor_position)

[**IOCTL_VIDEO_GET_BANK_SELECT_CODE**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_get_bank_select_code)

[**IOCTL_VIDEO_SET_PALETTE_REGISTERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_set_palette_registers)

[**IOCTL_VIDEO_LOAD_AND_SET_FONT**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_load_and_set_font)

Details for each IOCTL can be found in [Video Miniport Driver I/O Control Codes](/windows-hardware/drivers/ddi/ntddvdeo). Miniport driver writers should not use undocumented system-defined IOCTLs.
