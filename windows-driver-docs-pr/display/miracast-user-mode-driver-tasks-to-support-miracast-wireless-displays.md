---
title: WDDM 1.3 Miracast user-mode drivers to support wireless displays
description: User-mode driver support for Miracast on Windows 8.1
ms.date: 03/24/2023
---

# Miracast user-mode driver tasks to support Miracast wireless displays on Windows 8.1

> [!NOTE]
> Starting in Windows 10 (WDDM 2.0), the operating system ships with a built-in Miracast stack that can work on any GPU. For information about the Microsoft Miracast stack and the requirements of drivers and hardware to support Miracast displays starting in Windows 10, see the following documentation:
>
> * [Building best-in-class Wireless projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection)
>
> * The relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**
>
> Driver developers should no longer implement a custom Miracast stack. Microsoft might remove support for custom Miracast stacks in a future version of Windows.

To enable Miracast wireless displays on windows 8.1, you need to create a standalone, unique DLL that implements a Miracast user-mode driver. This driver is loaded in a dedicated session 0 process. Add the name of the driver in device software settings in the INF file as **MiracastDriverName**:

``` syntax
[MyDevice_DeviceSettings]
HKR,, MiracastDriverName, %REG_SZ%, Miracast.dll
```

The DLL should have an export function named [*QueryMiracastDriverInterface*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-query_miracast_driver_interface) that the operating system can call. This driver binary must not use an existing Direct3D user-mode display driver DLL.

Because the Miracast user-mode driver is loaded into the UMDF0 process, no separate Windows on Windows (WOW) version of this driver is needed. For example, a 64-bit version of the driver is used on a 64-bit processor.

When the operating system is ready to prepare for a Miracast connected session, it calls the Miracast user-mode driver's [*CreateMiracastContext*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_create_miracast_context) function. When this function is called, the Miracast user-mode driver allocates all the software resources it needs to start a Miracast connected session. In this call, the operating system also provides pointers to callback functions that the driver can call during the lifetime of the current Miracast context. Then after a Real-Time Streaming Protocol (RTSP) link is established, the operating system calls [*StartMiracastSession*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_start_miracast_session) to actually start the Miracast connected session. When the driver responds to this function call, it should use the Winsock [**getaddrinfo**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfo) function, or other relevant functions, to get the Internet Protocol (IP) address of the Miracast sink and use standard Winsock functions to create a Hypertext Caching Protocol (HTCP) Remote Desktop Protocol (RDP) socket.

If a Miracast display becomes available, the Miracast user-mode driver calls the operating system-supplied [**MiracastIoControl**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_miracast_io_control) function to send an I/O control request to the display miniport driver to report a monitor arrival hot-plug detection (HPD) awareness value. The Miracast user-mode driver should also query Miracast sink info and capabilities and report some of this info, such as the monitor description, to the display miniport driver by calling **MiracastIoControl**.

After the Miracast connected session has been started, and after streaming data has been prepared and before sending it to the network, the driver needs to call the [**ReportStatistic**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic) callback function to report the statistics of the Miracast link to the operating system.

When the operating system stops a Miracast connected session, it calls the Miracast user-mode driver's [*StopMiracastSession*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_stop_miracast_session) function. In response to this function call, the driver should close all the sockets it created and drop all the further data streaming. The driver shouldn't close the RTSP socket that the operating system gave it. It also shouldn't send a request to the display miniport driver to report an HPD on monitor departure.

The Miracast user-mode driver should release all the software resources that it allocated in [*CreateMiracastContext*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_create_miracast_context) in response to the operating system's calls to the [*DestroyMiracastContext*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_destroy_miracast_context) function.

When the display miniport driver receives a [*DxgkDdiCommitVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_commitvidpn) request to power off the connected Miracast monitor, the driver should call the operating system-supplied [*DxgkCbMiracastSendMessage*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_send_message) callback function to send a message to the Miracast user-mode driver. The Miracast user-mode driver should then put the Miracast sink into a low-power state.

The [**RegisterForDataRateNotifications**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_register_datarate_notifications) callback function can optionally be called by the Miracast user-mode driver to register with the operating system to receive, once a second, network quality of service (QoS) notifications and the current network bandwidth of the Miracast connection. This network info is provided by operating system calls to the [*pfnDataRateNotify*](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_datarate_notification) function.

The Miracast user-mode driver can also call these optional callback functions provided by the operating system:

| Function | Description |
| -------- | ----------- |
| [**GetNextChunkData**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data) | Provides info about the next encode chunk. |
| [**ReportSessionStatus**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_session_status) | The driver calls this function to report the status of the current Miracast connected session. |
