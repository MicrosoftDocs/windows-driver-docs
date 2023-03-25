---
title: WDDM 1.3 display miniport driver support for wireless displays
description: Driver support for Windows 8.1 Miracast wireless displays
ms.date: 03/24/2023
---

# WDDM 1.3 display miniport driver tasks to support Miracast wireless displays on Windows 8.1

> [!NOTE]
> Starting in Windows 10 (WDDM 2.0), the operating system ships with a built-in Miracast stack that can work on any GPU. For information about the Microsoft Miracast stack and the requirements of drivers and hardware to support Miracast displays starting in Windows 10, see the following documentation:
>
> * [Building best-in-class Wireless projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection)
>
> * The relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**
>
> Driver developers should no longer implement a custom Miracast stack. Microsoft might remove support for custom Miracast stacks in a future version of Windows.

To support Miracast wireless displays on Windows 8.1, WDDM 1.3 display miniport drivers that run in kernel mode need to do the following tasks.

## Supporting the Miracast interface

If the WDDM 8.1 display miniport driver supports Miracast displays, it must report the [**DXGK_MIRACAST_DISPLAY_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_interface) structure, which has pointers to driver-implemented Miracast functions, when the Microsoft DirectX graphics kernel subsystem calls the [*DxgkDdiQueryInterface*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function.

If the operating system's DirectX graphics kernel subsystem (Dxgkrnl.sys) doesn't call the [*DxgkDdiQueryInterface*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function to query the Miracast display interface, then it doesn't support Miracast wireless displays, and the display miniport driver shouldn't report any Miracast target.

The driver shouldn't report more than one Miracast target on any full WDDM graphics device, otherwise the operating system fails to start the adapter.

After Dxgkrnl calls [*DxgkDdiQueryInterface*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) to query the Miracast display interface, the driver can then report the target type as **D3DKMDT_VOT_MIRACAST** during device initialization when Dxgkrnl calls the [*DxgkDdiQueryChildRelations*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations) function.

The Miracast target should remain in a disconnected state until Dxgkrnl starts a Miracast connected session. When a Miracast session is starting, and a monitor is connected to the Miracast sink or the driver receives an I/O request from the Miracast user-mode driver because a new monitor has connected to the Miracast sink, the display miniport driver should report a monitor arrival hot-plug detection (HPD) awareness value to the operating system by calling the [**DxgkCbIndicateChildStatus**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_indicate_child_status) function. In this call, the driver should set the following values in the [**DXGK_CHILD_STATUS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_status) structure:

| Member | Value |
| ------ | ----- |
| **Type**                             | **StatusMiracast** constant value of the [**DXGK_CHILD_STATUS_TYPE**](/windows-hardware/drivers/ddi/dispmprt/ne-dispmprt-_dxgk_child_status_type) enumeration  |
| **Miracast**.**Connected**           | **TRUE**   |
| **Miracast**.**MiracastMonitorType** | Value that indicates the connection type. If the Miracast sink is embedded in the monitor or TV, this member should be set to the **D3DKMDT_VOT_MIRACAST** constant value of the [**D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_video_output_technology) enumeration. |

The following table lists the Miracast functions that the WDDM 1.3 display miniport driver implements:

| Function | Description |
| -------- | ----------- |
| [*DxgkDdiMiracastCreateContext*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_create_context)     | Creates a context to start a kernel-mode instance of a Miracast display device. |
| [*DxgkDdiMiracastDestroyContext*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_destroy_context)    | Creates a context to start a kernel-mode instance of a Miracast display device. |
| [*DxgkDdiMiracastIoControl*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_handle_io_control)  | Processes a synchronous I/O request that originates from a Miracast user-mode driver call to [**MiracastIoControl**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_miracast_io_control). |
| [*DxgkDdiMiracastQueryCaps*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_query_caps)         | Queries the Miracast capabilities of the current display adapter. |

## Starting the Miracast session

When the Miracast session has been started, the operating system calls the [*DxgkDdiQueryChildStatus*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_status) function. The display miniport driver should set [**DXGK_CHILD_STATUS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_status).**Type** to a value of **StatusMiracast** and should use the **Miracast** child structure in **DXGK_CHILD_STATUS**. If a monitor is connected to the Miracast sink, the driver should set **Miracast**.**Connected** to **D3DKMDT_VOT_MIRACAST**.

The driver must specify the value of [**D3DKMDT_VIDEO_SIGNAL_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info).**VsyncFreqDivider**, which is the ratio of the VSync rate of a monitor that displays through a Miracast connected session to the VSync rate of the Miracast sink. For example, if the Miracast sink vertical refresh rate is 240 Hz and the VSync interrupt frequency of the connected display is 30 Hz, the driver should set **VsyncFreqDivider** to 8.

## Handling interrupts for completed encode chunks

The data for a single frame transmitted across the wireless Miracast connection can be broken into one or more encode chunks. Each time the GPU finishes encoding one of these chunks, it must generate an interrupt. In response to this interrupt, the display miniport driver must call the [*DxgkCbNotifyInterrupt*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_notify_interrupt) function and complete the **MiracastEncodeChunkCompleted** child structure in the [**DXGKARGCB_NOTIFY_INTERRUPT_DATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data) structure, including setting the [**DXGK_INTERRUPT_TYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_interrupt_type) interrupt type to **DXGK_INTERRUPT_MICACAST_CHUNK_PROCESSING_COMPLETE**.

As part of the interrupt handling, the driver can optionally specify the **MiracastEncodeChunkCompleted**.**pPrivateDriverData** and **PrivateDataDriverSize** members in the [**DXGKARGCB_NOTIFY_INTERRUPT_DATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data) structure. The user-mode driver can access this private driver data in the [**MIRACAST_CHUNK_DATA**](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_data).**PrivateDriverData** member.

If, over a period of time, the display miniport driver generates more packets with chunk data than the user-mode display driver consumes, then the available free memory space for new chunks can run out. In this case the display miniport driver returns **STATUS_NO_MEMORY** in **MiracastEncodeChunkCompleted**.**Status**, and it must call the [*DxgkCbNotifyDpc*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_notify_dpc) function to notify the operating system's GPU scheduler about the error condition. A call to the [**GetNextChunkData**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data) function will return the **STATUS_CONNECTION_RESET** status code, and subsequent calls will start receiving chunks that were submitted after the reset operation. Because some chunks were lost, the driver should generate and transmit a new I-frame.

## Restrictions on source modes

To handle constraints of the pixel pipeline, a WDDM 1.3 display miniport driver typically restricts source modes that are exposed to the operating system. The driver does so by only populating the list of source modes with modes exposed by the monitor that the pixel pipeline also supports. For example, the driver doesn't modify the EDID based on pixel pipeline constraints.

Similarly, for Miracast displays the display miniport driver restricts the set of source modes that are exposed to the operating system when it enumerates the set of source and target modes. For Miracast displays the GPU encode capabilities, network properties, and sink decode capabilities can reduce the number of source modes that the Miracast pixel pipeline can support.

If a display miniport driver calls the [*DXGK_VIDPNSOURCEMODESET_INTERFACE::pfnAddMode*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_addmode) function to attempt to add a 3-D stereo mode to a source that's connected to a Miracast target, the function call fails.

## Calling operating system-provided callback functions

The operating system provides the following Miracast kernel-mode callback functions:

| Function | Description |
| -------- | ----------- |
| [**DxgkCbMiracastSendMessage**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message)  | Sends an asynchronous message to the user-mode display driver. |
| [**DxgkCbMiracastSendMessageCallback**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message_callback) | Used in a call to [**DxgkCbMiracastSendMessage**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message) to specify the [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure for the completed IRP. |
| [**DxgkCbReportChunkInfo**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_report_chunk_info)  
Reports info about an encode chunk. |

## Sending messages asynchronously from kernel-mode to user-mode

Any message that the display miniport driver sends to its associated user-mode driver through a [*DxgkCbMiracastSendMessage*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message) call isn't delivered until the Miracast connected session has started. Therefore, if the user-mode driver's [*StartMiracastSession*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_start_miracast_session) function hasn't yet been called, the sent message is deferred until *StartMiracastSession* returns. If a message is sent after the [*StopMiracastSession*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_stop_miracast_session) function is called, then the message is dropped by the operating system, and the [*DxgkCbMiracastSendMessageCallback*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message_callback) function is called with the error status set in *pIoStatusBlock*-&gt;**Status**.

## Modifying an existing display miniport driver to support Miracast displays

When the [*DxgkDdiStartDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) function is called, the display miniport driver needs to add a new Miracast target and should mark the target's hot-plug detection (HPD) awareness value as **HpdAwarenessInterruptible** so that the operating system doesn't poll this target. Also, when the [*DxgkDdiQueryChildRelations*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations) function is called, the driver should report **D3DKMDT_VOT_MIRACAST** as its connection type.

The driver shouldn't report more than one Miracast target on any full WDDM graphics device. If a driver reports more than one Miracast target, the operating system fails the starting of the adapter. The driver should also not report any monitor on this target if the Miracast connected session isn't started.

The driver also needs to report a correct [**DXGK_MIRACAST_DISPLAY_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_miracast_interface) structure, with pointers to functions that are in kernel-mode address space, when the DirectX graphics kernel subsystem calls the [*DxgkDdiQueryInterface*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function.

When a Miracast session is starting, and a monitor is connected the Miracast sink, the display miniport driver should set the [**DXGK_CHILD_STATUS**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_child_status).**Type** member to the **StatusMiracast** constant value, and should also set **DXGK_CHILD_STATUS**.**Miracast**.**Connected** to **TRUE**, to report a monitor arrival HPD to the operating system. The driver should set the **DXGK_CHILD_STATUS**.**Miracast**.**MiracastMonitorType** member to the correct monitor type that's connected to the sink. If the sink is part of the monitor, this member should be set to **D3DKMDT_VOT_MIRACAST**.

If the driver knows the EDID of the monitor, it should report this EDID when the operating system calls the [*DxgkDdiQueryDeviceDescriptor*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_device_descriptor) function.

Depending on hardware capabilities, the Miracast sink mode list, and network bandwidth, the driver should report the correct source mode, target mode, rotation mode, and scaling mode. For the target mode, driver should report the correct **VSyncFreqDivider** member value in [**D3DKMDT_VIDEO_SIGNAL_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info). The operating system matches the target mode against the monitor mode and prunes any mode that the monitor doesn't support.
