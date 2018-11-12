---
title: Miracast user-mode driver tasks to support Miracast wireless displays
description: To enable Miracast wireless displays, you need to create a standalone, unique DLL that implements a Miracast user-mode driver.
ms.assetid: FF5D7760-2407-487A-8363-7AC3B6385F6C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="display.miracast_user-mode_driver_tasks_to_support_miracast_wireless_displays"></span>Miracast user-mode driver tasks to support Miracast wireless displays


To enable Miracast wireless displays, you need to create a standalone, unique DLL that implements a Miracast user-mode driver. This driver will be loaded in a dedicated session 0 process. Add the name of the driver in device software settings in the INF file as **MiracastDriverName**:

``` syntax
[MyDevice_DeviceSettings]
HKR,, MiracastDriverName, %REG_SZ%, Miracast.dll
```

The DLL should have an export function named [*QueryMiracastDriverInterface*](https://msdn.microsoft.com/library/windows/hardware/dn265499) that the operating system can call. This driver binary must not use an existing Microsoft Direct3D user-mode display driver DLL.

Note that because the Miracast user-mode driver is loaded into the UMDF0 process, no separate Windows on Windows (WOW) version of this driver is needed. For example, on a 64-bit processor a 64-bit version of the driver is used.

When the operating system is ready to prepare for a Miracast connected session, it calls the Miracast user-mode driver's [*CreateMiracastContext*](https://msdn.microsoft.com/library/windows/hardware/dn265169) function. When this function is called, the Miracast user-mode driver allocates all the software resources it needs to start a Miracast connected session. In this call the operating system also provides pointers to callback functions that the driver can call during the lifetime of the current Miracast context. Then after a Real-Time Streaming Protocol (RTSP) link is established, the operating system calls [*StartMiracastSession*](https://msdn.microsoft.com/library/windows/hardware/dn265504) to actually start the Miracast connected session. When responding to this function call, the driver should use the Winsock [**getaddrinfo**](https://msdn.microsoft.com/library/windows/desktop/ms738520) function, or other relevant functions, to get the Internet Protocol (IP) address of the Miracast sink and use standard Winsock functions to create a Hypertext Caching Protocol (HTCP) Remote Desktop Protocol (RDP) socket.

If a Miracast display becomes available, the Miracast user-mode driver calls the operating system-supplied [**MiracastIoControl**](https://msdn.microsoft.com/library/windows/hardware/dn265469) function to send an I/O control request to the display miniport driver to report a monitor arrival hot-plug detection (HPD) awareness value. The Miracast user-mode driver should also query Miracast sink info and capabilities and report some of this info, such as the monitor description, to the display miniport driver by calling **MiracastIoControl**.

After the Miracast connected session has been started, and after streaming data has been prepared and before sending it to the network, the driver needs to call the [**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) callback function to report the statistics of the Miracast link to the operating system.

When the operating system stops a Miracast connected session, it calls the Miracast user-mode driver's [*StopMiracastSession*](https://msdn.microsoft.com/library/windows/hardware/dn265505) function. In response to this function call, the driver should close all the sockets it created and drop all the further data streaming. The driver should not close the RTSP socket that the operating system gave it. It also should not send a request to the display miniport driver to report an HPD on monitor departure.

In responding to the operating system's calls to the [*DestroyMiracastContext*](https://msdn.microsoft.com/library/windows/hardware/dn265304) function, the Miracast user-mode driver should release all the software resources that it allocated in [*CreateMiracastContext*](https://msdn.microsoft.com/library/windows/hardware/dn265169).

When the display miniport driver receives a [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597) request to power off the connected Miracast monitor, the driver should call the operating system-supplied [*DxgkCbMiracastSendMessage*](https://msdn.microsoft.com/library/windows/hardware/dn344646) callback function to send a message to the Miracast user-mode driver. The Miracast user-mode driver should then put the Miracast sink into a low-power state.

The [**RegisterForDataRateNotifications**](https://msdn.microsoft.com/library/windows/hardware/dn265500) callback function can optionally be called by the Miracast user-mode driver to register with the operating system to receive, once a second, network quality of service (QoS) notifications and the current network bandwidth of the Miracast connection. This network info is provided by operating system calls to the [*pfnDataRateNotify*](https://msdn.microsoft.com/library/windows/hardware/dn265492) function.

The Miracast user-mode driver can also call these optional callback functions provided by the operating system:

<span id="GetNextChunkData"></span><span id="getnextchunkdata"></span><span id="GETNEXTCHUNKDATA"></span>[**GetNextChunkData**](https://msdn.microsoft.com/library/windows/hardware/dn265462)  
Provides info about the next encode chunk.

<span id="ReportSessionStatus"></span><span id="reportsessionstatus"></span><span id="REPORTSESSIONSTATUS"></span>[**ReportSessionStatus**](https://msdn.microsoft.com/library/windows/hardware/dn265502)  
The driver calls this function to report the status of the current Miracast connected session.

 

 





