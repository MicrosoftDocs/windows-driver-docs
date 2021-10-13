---
title: About wireless displays (Miracast)
description: Wireless (Miracast) displays can optionally be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability was introduced in Windows 8.1.
keywords:
- Wireless displays
- Miracast
- Miracast design guide
- Miracast reference
- Wireless display callback functions called by Miracast user-mode drivers
- Wireless display functions implemented by Miracast user-mode drivers
ms.date: 08/10/2021
ms.localizationpriority: medium
---

# About wireless displays (Miracast)

> [!NOTE]
> This document describes how drivers can implement a custom Miracast stack in Windows 8.1. As of Windows 10, the OS ships with a built-in Miracast stack that can work on any GPU and it is no longer recommended that drivers implement a custom Miracast stack. This documentation is therefore deprecated and Microsoft might remove support for custom Miracast stacks in a future version of Windows.

Windows Display Driver Model (WDDM) 1.3 and later drivers can optionally support wireless (Miracast) displays. This capability was introduced in Windows 8.1.

For more information on the requirements of drivers and hardware to support Miracast displays, refer to the [Building best-in-class Wireless Projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection) guide and the relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**.

The following pages describe how Windows 8.1 display miniport drivers and Miracast user-mode drivers support Miracast displays:

* [WDDM display miniport driver tasks to support Miracast wireless displays](wddm-display-miniport-driver-tasks-to-support-miracast-wireless-displays.md)
* [Miracast user-mode driver tasks to support Miracast wireless displays](miracast-user-mode-driver-tasks-to-support-miracast-wireless-displays.md)
* [Reporting Miracast encode chunks and statistics](reporting-miracast-encode-chunks-and-statistics.md)
* [Calling DisplayConfig functions for a Miracast target](calling-displayconfig-functions-for-a-miracast-target.md)

## Miracast reference

The following sections describe how to implement Miracast capability in your drivers.

### User-mode device driver interfaces (DDIs)

**Wireless display callback functions called by Miracast user-mode drivers**

The reference pages in this section describe wireless display (Miracast) user-mode functions that the operating system implements. Only Miracast user-mode drivers can call these functions. 

Pointers to the Miracast display callback functions are returned in a [MIRACAST_CALLBACKS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_callbacks) structure.

|Topic| Description |
|:--|:--|
|[PFN_GET_NEXT_CHUNK_DATA](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data)| Provides info about the next Miracast encode chunk that was reported to the Microsoft DirectX graphics kernel subsystem when the [DXGK_INTERRUPT_TYPE](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_interrupt_type) interrupt type is DXGK_INTERRUPT_MIRACAST_CHUNK_PROCESSING_COMPLETE.| 
|[PFN_MIRACAST_IO_CONTROL](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_miracast_io_control)| Called by the user-mode display driver to send the kernel-mode display miniport driver a synchronous I/O control request.|
|[PFN_REGISTER_DATARATE_NOTIFICATIONS](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_register_datarate_notifications)| Called by the user-mode driver to register with the operating system to receive network quality of service (QoS) notifications and the current network bandwidth of the Miracast connection.|
|[PFN_REPORT_SESSION_STATUS](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_session_status)| Called by the user-mode display driver to report the status of the current Miracast connected session.|
|[PFN_REPORT_STATISTIC](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic)| Called by the user-mode display driver to report the statistics of the Miracast link to the operating system.|
 
**Wireless display functions implemented by Miracast user-mode drivers**

The reference pages in this section describe wireless display (Miracast) functions that a Miracast user-mode driver must implement. This type of driver runs in a standalone DLL. 

In response to an operating system call to the [QueryMiracastDriverInterface](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-query_miracast_driver_interface) function, the Miracast user-mode driver must supply pointers to these functions in the [MIRACAST_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_driver_interface) structure, except for [pfnDataRateNotify](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_datarate_notification), which is has a pointer declared in [RegisterForDataRateNotifications](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_register_datarate_notifications).

|Topic| Description |
|:--|:--|
|[PFN_CREATE_MIRACAST_CONTEXT](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_create_miracast_context)| Called by the operating system to create a user-mode Miracast context.|
|[PFN_DESTROY_MIRACAST_CONTEXT](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_destroy_miracast_context)| Called by the operating system to destroy a user-mode Miracast context.|
|[PFN_HANDLE_KMD_MESSAGE](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_handle_kmd_message)| Called by the operating system to handle the asynchronous kernel-mode message that the Miracast user-mode driver receives when the display miniport driver calls the [DxgkCbMiracastSendMessage](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message) function.|
|[PFN_DATARATE_NOTIFICATION](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_datarate_notification)| Called by the operating system to notify the Miracast user-mode driver that the bit rate of the Miracast network link has changed. This function is registered with the operating system when the **RegisterForDataRateNotifications** function is called.|
|[QUERY_MIRACAST_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-query_miracast_driver_interface)| Called by the operating system to query the Miracast user-mode driver interface, **MIRACAST_DRIVER_INTERFACE**.|
|[PFN_START_MIRACAST_SESSION](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_start_miracast_session)| Called by the operating system to start a Miracast connected session.|
|[PFN_STOP_MIRACAST_SESSION](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_stop_miracast_session)| Called by the operating system to start a Miracast connected session that had earlier been started by a call to the **StartMiracastSession** function.|
 

**Wireless display (Miracast) structures and enumerations**

All user-mode structures and enumerations that are used with Miracast display device driver interfaces (DDIs).

|Topic |Description |
|:--|:--|
|[MIRACAST_CALLBACKS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_callbacks)| Contains pointers to wireless display (Miracast) runtime callback functions that the Miracast user-mode driver can call.|
|[MIRACAST_CHUNK_DATA](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_data)| Contains encode chunk data that is used when a user-mode driver calls the wireless display (Miracast) [GetNextChunkData](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data) function.|
|[MIRACAST_CHUNK_ID](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_id)| Stores info that identifies a wireless display (Miracast) encode chunk.|
|[MIRACAST_CHUNK_INFO](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_info)| Contains info about a specified wireless display (Miracast) encode chunk.|
|[MIRACAST_CHUNK_TYPE](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_chunk_type)| Specifies the types of wireless display (Miracast) chunk info that is to be processed.|
|[MIRACAST_DATARATE_STATS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_datarate_stats)| Contains info used in the wireless display (Miracast) pfnDataRateNotify function about the audio/video encoder bit rate and failed or retried Wi-Fi frames.|
|[MIRACAST_DRIVER_INTERFACE](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-_miracast_driver_interface)| Contains pointers to wireless display (Miracast) functions that are implemented by the Miracast user-mode driver.|
|[MIRACAST_PROTOCOL_EVENT](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_protocol_event)| Specifies the types of wireless display (Miracast) protocol event that the user-mode display driver should report.|
|[MIRACAST_SESSION_INFO](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_session_info)| Contains info on a wireless display (Miracast) connected session.|
|[MIRACAST_STATISTIC_DATA](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_statistic_data)| Contains Miracast statistics data that the user-mode display driver reports to the operating system.|
|[MIRACAST_STATISTIC_TYPE](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_statistic_type)| Specifies types of Miracast statistics data that the user-mode display driver generates.|
|[MIRACAST_STATUS](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_status)| Specifies status types that the user-mode display driver uses to report Miracast connection status.|
|[MIRACAST_WFD_CONNECTION_STATS](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_wfd_connection_stats)| Contains bit rate info on the Wi-Fi Direct connection.|

These additional user-mode structures and enumerations support Miracast displays and are new or updated for Windows 8.1:

-   [**DISPLAYCONFIG\_TARGET\_BASE\_TYPE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_base_type) (new)
-   [**DISPLAYCONFIG\_VIDEO\_SIGNAL\_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info) (**AdditionalSignalInfo** child structure added)
-   [**DISPLAYCONFIG\_DEVICE\_INFO\_TYPE**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_device_info_type) (**DISPLAYCONFIG\_DEVICE\_INFO\_GET\_TARGET\_BASE\_TYPE** constant added)
-   [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info) (**AdditionalSignalInfo** child structure added)
-   [**DISPLAYCONFIG\_DEVICE\_INFO\_TYPE**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_device_info_type) (**DISPLAYCONFIG\_DEVICE\_INFO\_GET\_TARGET\_BASE\_TYPE** constant added)

### Kernel-mode DDIs

**Wireless display (Miracast) display callback interface**

The Miracast display callback interface contains functions that are implemented by the Microsoft DirectX graphics kernel subsystem to support wireless (Miracast) displays. This interface is supported starting in Windows 8.1.

This section contains reference pages for these kernel-mode functions, which are called by Windows Display Driver Model (WDDM) 1.3 and later display miniport drivers:

|Topic |Description |
|:--|:--|
|[DXGKCB_MIRACAST_SEND_MESSAGE](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message)|Sends an asynchronous message to the user-mode display driver.|
|[DXGKCB_MIRACAST_SEND_MESSAGE_CALLBACK](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message_callback)|Called in kernel mode when the message that was sent to the user-mode driver with a call to the **DxgkCbMiracastSendMessage** function has completed or has been canceled.|
|[DXGKCB_MIRACAST_REPORT_CHUNK_INFO](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_report_chunk_info)|Called by the display miniport driver to report info about an encode chunk.|

The display miniport driver must fill in pointers to these functions in the [DXGK_MIRACAST_DISPLAY_CALLBACKS](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_display_callbacks) structure.

**Wireless display (Miracast) interface**

This section contains kernel-mode functions that are implemented by display miniport drivers that support wireless (Miracast) displays. This interface is supported starting in Windows 8.1.

Pointers to the Miracast interface functions are returned in a [DXGK_MIRACAST_INTERFACE](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_interface) structure.

|Topic |Description |
|:--|:--|
|[DXGKCB_MIRACAST_SEND_MESSAGE_CALLBACK](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message_callback)|Called in kernel mode when the message that was sent to the user-mode driver with a call to the DxgkCbMiracastSendMessage function has completed or has been canceled.|
|[DXGKDDI_MIRACAST_CREATE_CONTEXT](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_create_context)|Creates a kernel-mode context for a Miracast device.|
|[DXGKDDI_MIRACAST_DESTROY_CONTEXT](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_destroy_context)|Destroys an instance of a Miracast device.|
|[DXGKDDI_MIRACAST_HANDLE_IO_CONTROL](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_handle_io_control)|Called by the operating system to request that the display miniport driver process a synchronous I/O control request in response to a user-mode display driver call to the MiracastIoControl function.|
|[DXGKDDI_MIRACAST_QUERY_CAPS](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_query_caps) |Queries the Miracast capabilities of the current display adapter. The operating system calls this function only when the display adapter is first started and then stores the capabilities that are returned.|


These additional kernel-mode structures and enumerations support Miracast displays and are new or updated for Windows 8.1:

-   [**DXGK\_MIRACAST\_CAPS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_caps)
-   [**D3DKMDT\_VIDEO\_OUTPUT\_TECHNOLOGY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_video_output_technology) (**D3DKMDT\_VOT\_MIRACAST** constant added)
-   [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info) (**AdditionalSignalInfo** child structure added)
-   [**DXGK\_CHILD\_STATUS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_status) (**Miracast** child structure added)
-   [**DXGK\_CHILD\_STATUS\_TYPE**](/windows-hardware/drivers/ddi/dispmprt/ne-dispmprt-_dxgk_child_status_type) (**StatusMiracast** constant added)
-   [**DXGKARGCB\_NOTIFY\_INTERRUPT\_DATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data) (**MiracastEncodeChunkCompleted** child structure added)

 

