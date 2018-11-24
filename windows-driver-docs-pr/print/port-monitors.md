---
title: Port Monitors
description: Port Monitors
ms.assetid: 4758ebda-f93e-49fb-8605-17cf43194afc
keywords:
- print monitors WDK , port monitors
- port monitors WDK print
- port monitors WDK print , about port monitors
- port monitors WDK print , DLLs
- print queues WDK , port monitors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Port Monitors





Port monitors consist of user-mode DLLs. They are responsible for providing a communications path between the user-mode print spooler and the kernel-mode port drivers that access I/O port hardware. A port monitor typically uses the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **WriteFile**, **ReadFile**, and **DeviceIOControl** functions, described in the Microsoft Windows SDK documentation, to communicate with kernel-mode port drivers. Port monitors are also responsible for management and configuration of a server's printer ports, as described in [Managing a Port](managing-a-port.md).

An NT-based-operating system user's view of a "printer" is really a print queue, to which one or more physical printer devices can be connected. A port is the physical connection between the print queue and a single printer device. Each port monitor supports one or more instances of one or more types of ports. For example Localmon.dll, the [sample port monitor](sample-port-monitor.md), can support all of a server's local COM and LPT ports. (The print folder assigns ports to port monitors by calling the Windows SDK documentation's **AddPrinter** function.)

For print queues representing multiple printer devices (through multiple ports), the spooler sends each print job to the first available port. If the port monitor indicates that a specified port is busy or has encountered an error, the spooler resubmits the job to the queue, specifying another port supported by the port monitor.

Besides Localmon.dll, Windows 2000 and later operating system versions provide several additional port monitors. The *Windows 2000 Server Resource Kit* describes each of these port monitors. (This resource may not be available in some languages and countries.)

Customized port monitors can be written to support additional types of I/O port hardware.

For Windows 2000 and later, each port monitor is divided into two DLLs:

<a href="" id="port-monitor-ui-dll-"></a>**Port Monitor UI DLL**   
A port monitor's user interface DLL contains user interface functionality and executes on print client systems.

This DLL must reside in the client system's System32 subdirectory.

<a href="" id="port-monitor-server-dll-"></a>**Port Monitor Server DLL**   
A port monitor's server DLL contains port communications functionality and executes on print servers. It must not display a user interface.

The UI DLL communicates with the server DLL by calling the spooler's [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function.

A [sample port monitor](sample-port-monitor.md) is included in the Windows Driver Kit (WDK).

 

 




