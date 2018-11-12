---
title: WDDM display miniport driver tasks to support Miracast wireless displays
description: To support Miracast wireless displays, Windows Display Driver Model (WDDM) display miniport drivers that run in kernel mode need to do the following tasks.
ms.assetid: D67CAC4F-0409-4E8D-A31A-78C3EB473556
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDDM display miniport driver tasks to support Miracast wireless displays


To support Miracast wireless displays, Windows Display Driver Model (WDDM) display miniport drivers that run in kernel mode need to do the following tasks.

## <span id="Supporting_the_Miracast_interface"></span><span id="supporting_the_miracast_interface"></span><span id="SUPPORTING_THE_MIRACAST_INTERFACE"></span>Supporting the Miracast interface


If the display miniport driver supports Miracast displays, it must report the [**DXGK\_MIRACAST\_DISPLAY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/dn448486) structure, which has pointers to driver-implemented Miracast functions, when the Microsoft DirectX graphics kernel subsystem calls the [*DxgkDdiQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff559764) function.

If the operating system's DirectX graphics kernel subsystem (Dxgkrnl.sys) does not call the [*DxgkDdiQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff559764) function to query the Miracast display interface, then it does not support Miracast wireless displays, and the display miniport driver should not report any Miracast target.

The driver should not report more than one Miracast target on any full WDDM graphics device, otherwise the operating system fails to start the adapter.

After Dxgkrnl calls [*DxgkDdiQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff559764) to query the Miracast display interface, the driver can then report the target type as **D3DKMDT\_VOT\_MIRACAST** during device initialization when Dxgkrnl calls the [*DxgkDdiQueryChildRelations*](https://msdn.microsoft.com/library/windows/hardware/ff559750) function.

The Miracast target should remain in a disconnected state until Dxgkrnl starts a Miracast connected session. When a Miracast session is starting, and a monitor is connected to the Miracast sink or the driver receives an I/O request from the Miracast user-mode driver because a new monitor has connected to the Miracast sink, the display miniport driver should report a monitor arrival hot-plug detection (HPD) awareness value to the operating system by calling the [**DxgkCbIndicateChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559522) function. In this call the driver should set these values:

| [**DXGK\_CHILD\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff561010) member | Value                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**                                                    | **StatusMiracast** constant value of the [**DXGK\_CHILD\_STATUS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561015) enumeration                                                                                                                                                       |
| **Miracast**.**Connected**                                  | **TRUE**                                                                                                                                                                                                                                                                   |
| **Miracast**.**MiracastMonitorType**                        | Value that indicates the connection type. If the Miracast sink is embedded in the monitor or TV, this should be set to the **D3DKMDT\_VOT\_MIRACAST** constant value of the [**D3DKMDT\_VIDEO\_OUTPUT\_TECHNOLOGY**](https://msdn.microsoft.com/library/windows/hardware/ff546605) enumeration. |

 

These are the Miracast functions that the display miniport driver implements:

<span id="DxgkDdiMiracastCreateContext"></span><span id="dxgkddimiracastcreatecontext"></span><span id="DXGKDDIMIRACASTCREATECONTEXT"></span>[*DxgkDdiMiracastCreateContext*](https://msdn.microsoft.com/library/windows/hardware/dn323748)  
Creates a context to start a kernel-mode instance of a Miracast display device.

<span id="DxgkDdiMiracastDestroyContext"></span><span id="dxgkddimiracastdestroycontext"></span><span id="DXGKDDIMIRACASTDESTROYCONTEXT"></span>[*DxgkDdiMiracastDestroyContext*](https://msdn.microsoft.com/library/windows/hardware/dn323749)  
Creates a context to start a kernel-mode instance of a Miracast display device.

<span id="DxgkDdiMiracastIoControl"></span><span id="dxgkddimiracastiocontrol"></span><span id="DXGKDDIMIRACASTIOCONTROL"></span>[*DxgkDdiMiracastIoControl*](https://msdn.microsoft.com/library/windows/hardware/dn323750)  
Processes a synchronous I/O request that originates from a Miracast user-mode driver call to [**MiracastIoControl**](https://msdn.microsoft.com/library/windows/hardware/dn265469).

<span id="DxgkDdiMiracastQueryCaps"></span><span id="dxgkddimiracastquerycaps"></span><span id="DXGKDDIMIRACASTQUERYCAPS"></span>[*DxgkDdiMiracastQueryCaps*](https://msdn.microsoft.com/library/windows/hardware/dn323751)  
Queries the Miracast capabilities of the current display adapter.

## <span id="Miracast_session_start"></span><span id="miracast_session_start"></span><span id="MIRACAST_SESSION_START"></span>Miracast session start


When the Miracast session has been started, the operating system calls the [*DxgkDdiQueryChildStatus*](https://msdn.microsoft.com/library/windows/hardware/ff559754) function. The display miniport driver should set [**DXGK\_CHILD\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff561010).**Type** to a value of **StatusMiracast** and should use the **Miracast** child structure in **DXGK\_CHILD\_STATUS**. If a monitor is connected to the Miracast sink, the driver should set **Miracast**.**Connected** to **D3DKMDT\_VOT\_MIRACAST**.

The driver must specify the value of [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff546625).**VsyncFreqDivider**, which is the ratio of the VSync rate of a monitor that displays through a Miracast connected session to the VSync rate of the Miracast sink. For example, if the Miracast sink vertical refresh rate is 240 Hz and the VSync interrupt frequency of the connected display is 30 Hz, the driver should set **VsyncFreqDivider** to 8.

## <span id="Handling_interrupts_for_completed_encode_chunks"></span><span id="handling_interrupts_for_completed_encode_chunks"></span><span id="HANDLING_INTERRUPTS_FOR_COMPLETED_ENCODE_CHUNKS"></span>Handling interrupts for completed encode chunks


The data for a single frame transmitted across the wireless Miracast connection can be broken into one or more encode chunks. Each time the GPU finishes encoding one of these chunks, it must generate an interrupt. In response to this interrupt, the display miniport driver must call the [*DxgkCbNotifyInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559545) function and complete the **MiracastEncodeChunkCompleted** child structure in the [**DXGKARGCB\_NOTIFY\_INTERRUPT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff557538) structure, including setting the [**DXGK\_INTERRUPT\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561136) interrupt type to **DXGK\_INTERRUPT\_MICACAST\_CHUNK\_PROCESSING\_COMPLETE**.

As part of the interrupt handling, the driver can optionally specify the **MiracastEncodeChunkCompleted**.**pPrivateDriverData** and **PrivateDataDriverSize** members in the [**DXGKARGCB\_NOTIFY\_INTERRUPT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff557538) structure. The user-mode driver can access this private driver data in the [**MIRACAST\_CHUNK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn265471).**PrivateDriverData** member.

If, over a period of time, the display miniport driver generates more packets with chunk data than the user-mode display driver consumes, then the available free memory space for new chunks can run out. In this case the display miniport driver returns **STATUS\_NO\_MEMORY** in **MiracastEncodeChunkCompleted**.**Status**, and it must call the [*DxgkCbNotifyDpc*](https://msdn.microsoft.com/library/windows/hardware/ff559540) function to notify the operating system's GPU scheduler about the error condition. A call to the [**GetNextChunkData**](https://msdn.microsoft.com/library/windows/hardware/dn265462) function will return the **STATUS\_CONNECTION\_RESET** status code, and subsequent calls will start receiving chunks that were submitted after the reset operation. Because some chunks will have been lost, we recommend that the driver generate and transmit a new I-frame.

## <span id="Restrictions_on_source_modes"></span><span id="restrictions_on_source_modes"></span><span id="RESTRICTIONS_ON_SOURCE_MODES"></span>Restrictions on source modes


A WDDM display miniport driver, to handle constraints of the pixel pipeline, typically restricts source modes that are exposed to the operating system. The driver does this by only populating the list of source modes with modes that are exposed by the monitor that the pixel pipeline also supports. For example, the driver doesn't modify the EDID based on pixel pipeline constraints.

Similarly, for Miracast displays the display miniport driver restricts the set of source modes that are exposed to the operating system when it enumerates the set of source and target modes. For Miracast displays the GPU encode capabilities, network properties, and sink decode capabilities can reduce the number of source modes that the Miracast pixel pipeline can support.

If a display miniport driver calls the [*DXGK\_VIDPNSOURCEMODESET\_INTERFACE::pfnAddMode*](https://msdn.microsoft.com/library/windows/hardware/ff562077) function to attempt to add a 3-D stereo mode to a source that's connected to a Miracast target, the function call will fail.

## <span id="Calling_operating_system-provided_callback_functions"></span><span id="calling_operating_system-provided_callback_functions"></span><span id="CALLING_OPERATING_SYSTEM-PROVIDED_CALLBACK_FUNCTIONS"></span>Calling operating system-provided callback functions


These are the Miracast kernel-mode callback functions that the operating system provides:

<span id="DxgkCbMiracastSendMessage"></span><span id="dxgkcbmiracastsendmessage"></span><span id="DXGKCBMIRACASTSENDMESSAGE"></span>[**DxgkCbMiracastSendMessage**](https://msdn.microsoft.com/library/windows/hardware/dn344646)  
Sends an asynchronous message to the user-mode display driver.

<span id="DxgkCbMiracastSendMessageCallback"></span><span id="dxgkcbmiracastsendmessagecallback"></span><span id="DXGKCBMIRACASTSENDMESSAGECALLBACK"></span>[**DxgkCbMiracastSendMessageCallback**](https://msdn.microsoft.com/library/windows/hardware/dn358351)  
Used in a call to [**DxgkCbMiracastSendMessage**](https://msdn.microsoft.com/library/windows/hardware/dn344646) to specify the [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure for the completed IRP.

<span id="DxgkCbReportChunkInfo"></span><span id="dxgkcbreportchunkinfo"></span><span id="DXGKCBREPORTCHUNKINFO"></span>[**DxgkCbReportChunkInfo**](https://msdn.microsoft.com/library/windows/hardware/dn344647)  
Reports info about an encode chunk.

## <span id="Sending_messages_asynchronously_from_kernel-mode_to_user-mode"></span><span id="sending_messages_asynchronously_from_kernel-mode_to_user-mode"></span><span id="SENDING_MESSAGES_ASYNCHRONOUSLY_FROM_KERNEL-MODE_TO_USER-MODE"></span>Sending messages asynchronously from kernel-mode to user-mode


Any message that the display miniport driver sends to its associated user-mode driver when it calls the [*DxgkCbMiracastSendMessage*](https://msdn.microsoft.com/library/windows/hardware/dn344646) function won't be delivered until the Miracast connected session has started. Therefore, if the user-mode driver's [*StartMiracastSession*](https://msdn.microsoft.com/library/windows/hardware/dn265504) function has not yet been called, the sent message is deferred until *StartMiracastSession* returns. If a message is sent after the [*StopMiracastSession*](https://msdn.microsoft.com/library/windows/hardware/dn265505) function is called, then the message is dropped by the operating system, and the [*DxgkCbMiracastSendMessageCallback*](https://msdn.microsoft.com/library/windows/hardware/dn358351) function is called with the error status set in *pIoStatusBlock*-&gt;**Status**.

## <span id="Modifying_an_existing_display_miniport_driver_to_support_Miracast_displays"></span><span id="modifying_an_existing_display_miniport_driver_to_support_miracast_displays"></span><span id="MODIFYING_AN_EXISTING_DISPLAY_MINIPORT_DRIVER_TO_SUPPORT_MIRACAST_DISPLAYS"></span>Modifying an existing display miniport driver to support Miracast displays


When the [*DxgkDdiStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560775) function is called, the display miniport driver needs to add a new Miracast target and should mark the target's hot-plug detection (HPD) awareness value as **HpdAwarenessInterruptible** so that the operating system won't poll this target. Also, when the [*DxgkDdiQueryChildRelations*](https://msdn.microsoft.com/library/windows/hardware/ff559750) function is called, the driver should report **D3DKMDT\_VOT\_MIRACAST** as its connection type.

The driver should not report more than one Miracast target on any full WDDM graphics device. If a driver reports more than one Miracast target, the operating system fails the starting of the adapter. The driver should also not report any monitor on this target if the Miracast connected session is not started.

The driver also needs to report a correct [**DXGK\_MIRACAST\_DISPLAY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/dn448486) structure, with pointers to functions that are in kernel-mode address space, when the DirectX graphics kernel subsystem calls the [*DxgkDdiQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff559764) function.

When a Miracast session is starting, and a monitor is connected the Miracast sink, the display miniport driver should set the [**DXGK\_CHILD\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff561010).**Type** member to the **StatusMiracast** constant value, and should also set **DXGK\_CHILD\_STATUS**.**Miracast**.**Connected** to **TRUE**, to report a monitor arrival HPD to the operating system. The driver should set the **DXGK\_CHILD\_STATUS**.**Miracast**.**MiracastMonitorType** member to the correct monitor type that's connected to the sink. If the sink is part of the monitor, this member should be set to **D3DKMDT\_VOT\_MIRACAST**.

If the driver knows the EDID of the monitor, it should report this EDID when the operating system calls the [*DxgkDdiQueryDeviceDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff559761) function.

Depending on hardware capabilities, the Miracast sink mode list, and network bandwidth, the driver should reports the correct source mode, target mode, rotation mode, and scaling mode. For the target mode, driver should report the correct **VSyncFreqDivider** member value in [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff546625). The operating system matches the target mode against the monitor mode and prunes any mode that isn't supported by the monitor.

 

 





