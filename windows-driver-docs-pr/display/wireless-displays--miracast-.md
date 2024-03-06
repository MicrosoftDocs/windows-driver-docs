---
title: Supporting Miracast Wireless Display Drivers
description: Describes how to provide driver support for Miracast wireless displays.
keywords:
- Wireless displays
- Miracast
- Wireless display callback functions called by Miracast WDDM 1.3 user-mode drivers
- Wireless display functions implemented by Miracast user-mode drivers
ms.date: 03/24/2023
---

# Supporting Miracast wireless display

Support for the [Miracast](https://www.wi-fi.org/discover-wi-fi/miracast) wireless display standard was introduced in Windows 8.1 (WDDM 1.3).

## Supporting Miracast starting in Windows 10

Starting in Windows 10 (WDDM 2.0), the operating system ships with a built-in Miracast stack that can work on any GPU. For information about the Microsoft Miracast stack and the requirements of drivers and hardware to support Miracast displays starting in Windows 10, see the following documentation:

* [Building best-in-class Wireless projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection)

* The relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**

Driver developers should no longer implement a custom Miracast stack. Microsoft might remove support for custom Miracast stacks in a future version of Windows.

## Supporting Miracast in Windows 8.1

WDDM 1.3 drivers could optionally support Miracast through the Miracast DDIs provided in that release. The rest of this article and its related articles describe how to provide that support.

### User-mode device driver interfaces (DDIs)

#### Wireless display callback functions called by Miracast user-mode drivers

The following table lists the wireless display (Miracast) user-mode functions that the operating system implements. Only Windows 8.1 Miracast user-mode drivers can call these functions. Pointers to the Miracast display callback functions are returned in a [MIRACAST_CALLBACKS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_callbacks) structure.

| Function | Description |
| -------- | ----------- |
| [PFN_GET_NEXT_CHUNK_DATA](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data)     | Provides info about the next Miracast encode chunk that was reported to the DirectX graphics kernel subsystem when the [DXGK_INTERRUPT_TYPE](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_interrupt_type) interrupt type is DXGK_INTERRUPT_MIRACAST_CHUNK_PROCESSING_COMPLETE. |
| [PFN_MIRACAST_IO_CONTROL](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_miracast_io_control)     | Called by the user-mode display driver to send the kernel-mode display miniport driver a synchronous I/O control request. |
| [PFN_REGISTER_DATARATE_NOTIFICATIONS](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_register_datarate_notifications) | Called by the user-mode driver to register with the operating system to receive network quality of service (QoS) notifications and the current network bandwidth of the Miracast connection. |
| [PFN_REPORT_SESSION_STATUS](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_session_status) | Called by the user-mode display driver to report the status of the current Miracast connected session. |
| [PFN_REPORT_STATISTIC](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic)           | Called by the user-mode display driver to report the statistics of the Miracast link to the operating system. |

#### Wireless display functions implemented by Windows 8.1 Miracast user-mode drivers

The following table lists the wireless display (Miracast) functions that a Windows 8.1 Miracast user-mode driver must implement. This type of driver runs in a standalone DLL.

In response to an operating system call to the [QueryMiracastDriverInterface](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-query_miracast_driver_interface) function, the Miracast user-mode driver must supply pointers to these functions in the [MIRACAST_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_driver_interface) structure. The exception is [pfnDataRateNotify](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_datarate_notification), which has a pointer declared in [RegisterForDataRateNotifications](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_register_datarate_notifications).

| Function | Description |
| -------- | ----------- |
| [PFN_CREATE_MIRACAST_CONTEXT](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_create_miracast_context)  | Called by the operating system to create a user-mode Miracast context.|
| [PFN_DESTROY_MIRACAST_CONTEXT](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_destroy_miracast_context)| Called by the operating system to destroy a user-mode Miracast context.|
| [PFN_HANDLE_KMD_MESSAGE](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_handle_kmd_message)            | Called by the operating system to handle the asynchronous kernel-mode message that the Miracast user-mode driver receives when the display miniport driver calls the [DxgkCbMiracastSendMessage](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message) function.|
| [PFN_DATARATE_NOTIFICATION](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_datarate_notification)      | Called by the operating system to notify the Miracast user-mode driver that the bit rate of the Miracast network link has changed. This function is registered with the operating system when the **RegisterForDataRateNotifications** function is called.|
| [QUERY_MIRACAST_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-query_miracast_driver_interface)| Called by the operating system to query the Miracast user-mode driver interface, **MIRACAST_DRIVER_INTERFACE**.|
| [PFN_START_MIRACAST_SESSION](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_start_miracast_session)    | Called by the operating system to start a Miracast connected session.|
| [PFN_STOP_MIRACAST_SESSION](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_stop_miracast_session)      | Called by the operating system to start a Miracast connected session that was previously started by a call to the **StartMiracastSession** function.|

#### Related structures and enumerations

The following table lists the user-mode structures and enumerations that are used with Windows 8.1 Miracast display device driver interfaces (DDIs).

| Struct/Enum | Description |
| ----------- | ----------- |
| [MIRACAST_CALLBACKS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_callbacks)         | Contains pointers to wireless display (Miracast) runtime callback functions that the Miracast user-mode driver can call.|
| [MIRACAST_CHUNK_DATA](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_data)        | Contains encode chunk data that is used when a user-mode driver calls the wireless display (Miracast) [GetNextChunkData](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data) function.|
| [MIRACAST_CHUNK_ID](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_id)            | Stores info that identifies a wireless display (Miracast) encode chunk.|
| [MIRACAST_CHUNK_INFO](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_info)        | Contains info about a specified wireless display (Miracast) encode chunk.|
| [MIRACAST_CHUNK_TYPE](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_chunk_type)        | Specifies the types of wireless display (Miracast) chunk info that is to be processed.|
| [MIRACAST_DATARATE_STATS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_datarate_stats)| Contains info used in the wireless display (Miracast) pfnDataRateNotify function about the audio/video encoder bit rate and failed or retried Wi-Fi frames.|
| [MIRACAST_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_driver_interface)| Contains pointers to wireless display (Miracast) functions that the Miracast user-mode driver implements.|
| [MIRACAST_PROTOCOL_EVENT](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_protocol_event)| Specifies the types of wireless display (Miracast) protocol event that the user-mode display driver should report.|
| [MIRACAST_SESSION_INFO](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_session_info)    | Contains info on a wireless display (Miracast) connected session.|
| [MIRACAST_STATISTIC_DATA](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_statistic_data)| Contains Miracast statistics data that the user-mode display driver reports to the operating system.|
| [MIRACAST_STATISTIC_TYPE](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_statistic_type)| Specifies types of Miracast statistics data that the user-mode display driver generates.|
| [MIRACAST_STATUS](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_status)                | Specifies status types that the user-mode display driver uses to report Miracast connection status.|
| [MIRACAST_WFD_CONNECTION_STATS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_wfd_connection_stats)| Contains bit rate info on the Wi-Fi Direct connection.|

The following user-mode structures and enumerations support Miracast displays and were new or updated for Windows 8.1:

* [**DISPLAYCONFIG_TARGET_BASE_TYPE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_base_type) (new)
* [**DISPLAYCONFIG_VIDEO_SIGNAL_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info) (**AdditionalSignalInfo** child structure added)
* [**DISPLAYCONFIG_DEVICE_INFO_TYPE**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_device_info_type) (**DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_BASE_TYPE** constant added)
* [**D3DKMDT_VIDEO_SIGNAL_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info) (**AdditionalSignalInfo** child structure added)
* [**DISPLAYCONFIG_DEVICE_INFO_TYPE**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_device_info_type) (**DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_BASE_TYPE** constant added)

### Kernel-mode DDIs

#### Wireless display (Miracast) display callback interface

The Miracast display callback interface contains functions that the DirectX graphics kernel subsystem implements to support wireless (Miracast) displays in Windows 8.1.

The following table lists these kernel-mode functions, which are called by WDDM 1.3 display miniport drivers:

| Function | Description |
| -------- | ----------- |
| [DXGKCB_MIRACAST_SEND_MESSAGE](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message)           | Sends an asynchronous message to the user-mode display driver.|
| [DXGKCB_MIRACAST_SEND_MESSAGE_CALLBACK](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message_callback) | Called in kernel mode when the message that was sent to the user-mode driver with a call to the **DxgkCbMiracastSendMessage** function has completed or has been canceled.|
| [DXGKCB_MIRACAST_REPORT_CHUNK_INFO](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_report_chunk_info) | Called by the display miniport driver to report info about an encode chunk.|

The display miniport driver must fill in pointers to these functions in the [DXGK_MIRACAST_DISPLAY_CALLBACKS](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_display_callbacks) structure.

#### Wireless display (Miracast) interface

The following table lists the kernel-mode functions that display miniport drivers implement to support wireless (Miracast) displays in Windows 8.1. Pointers to the Miracast interface functions are returned in a [DXGK_MIRACAST_INTERFACE](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_interface) structure.

| Function | Description |
| -------- | ----------- |
| [DXGKCB_MIRACAST_SEND_MESSAGE_CALLBACK](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message_callback) | Called in kernel mode when the message that was sent to the user-mode driver with a call to the DxgkCbMiracastSendMessage function has completed or has been canceled.|
| [DXGKDDI_MIRACAST_CREATE_CONTEXT](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_create_context)             | Creates a kernel-mode context for a Miracast device.|
| [DXGKDDI_MIRACAST_DESTROY_CONTEXT](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_destroy_context)           | Destroys an instance of a Miracast device.|
| [DXGKDDI_MIRACAST_HANDLE_IO_CONTROL](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_handle_io_control)       | Called by the operating system to request that the display miniport driver process a synchronous I/O control request in response to a user-mode display driver call to the MiracastIoControl function.|
| [DXGKDDI_MIRACAST_QUERY_CAPS](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_query_caps)                     | Queries the Miracast capabilities of the current display adapter. The operating system calls this function only when the display adapter is first started and then stores the capabilities that are returned.|

These kernel-mode structures and enumerations support Miracast displays and were new or updated for Windows 8.1:

* [**DXGK_MIRACAST_CAPS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_caps)
* [**D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_video_output_technology) (**D3DKMDT_VOT_MIRACAST** constant added)
* [**D3DKMDT_VIDEO_SIGNAL_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info) (**AdditionalSignalInfo** child structure added)
* [**DXGK_CHILD_STATUS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_status) (**Miracast** child structure added)
* [**DXGK_CHILD_STATUS_TYPE**](/windows-hardware/drivers/ddi/dispmprt/ne-dispmprt-_dxgk_child_status_type) (**StatusMiracast** constant added)
* [**DXGKARGCB_NOTIFY_INTERRUPT_DATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data) (**MiracastEncodeChunkCompleted** child structure added)

### Related articles for Windows 8.1 Miracast drivers

* [WDDM 1.3 display miniport driver tasks to support Miracast wireless displays](wddm-display-miniport-driver-tasks-to-support-miracast-wireless-displays.md)
* [WDDM 1.3 Miracast user-mode driver tasks to support Miracast wireless displays](miracast-user-mode-driver-tasks-to-support-miracast-wireless-displays.md)
* [Reporting Miracast encode chunks and statistics](reporting-miracast-encode-chunks-and-statistics.md)
* [Calling DisplayConfig functions for a Miracast target](calling-displayconfig-functions-for-a-miracast-target.md)
