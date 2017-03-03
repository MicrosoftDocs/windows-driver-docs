---
Description: 'This topic provides information for client driver developers about the tracing and logging features for Universal Serial Bus (USB).'
MS-HAID: 'buses.usb\_event\_tracing\_for\_windows'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Event Tracing for Windows
author: windows-driver-content
---

# USB Event Tracing for Windows


This topic provides information for client driver developers about the tracing and logging features for Universal Serial Bus (USB). This information is provided for the benefit of those who develop and debug USB devices. It includes information on how to install the tools, create trace files, and analyze the events in a USB trace file. The topic assumes that you have a comprehensive understanding of the USB ecosystem and hardware that is required to successfully use the USB tracing and logging features.

To interpret the event traces, you must also understand the Windows [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md), the [official USB Specifications, and the USB Device Class Specifications](http://www.usb.org/developers/docs/).

-   [About Event Tracing for Windows](#about-event-tracing-for-windows)
-   [USB Support for ETW Logging](#usb-support-for-etw-logging)
-   [USB ETW Support in Windows 7](#usb-etw-support-in-windows-7)
-   [USB ETW Support in Windows 8](#usb-etw-support-in-windows-8)

## About Event Tracing for Windows


Event Tracing for Windows (ETW) is a general-purpose, high-speed tracing facility that is provided by the operating system. It uses a buffering and logging mechanism that is implemented in the kernel to provide a tracing mechanism for events that are raised by both user-mode applications and kernel-mode device drivers. Additionally, ETW provides the ability to dynamically enable and disable logging, which makes it easy to perform detailed tracing in production environments without requiring reboots or application restarts. The logging mechanism uses per-processor buffers that are written to disk by an asynchronous writer thread. This buffering allows large-scale server applications to write events with minimum disturbance.

ETW was introduced in Windows 2000. Since then, various core operating system and server components have adopted ETW to instrument their activities. ETW is now one of the key instrumentation technologies on Windows platforms. A growing number of third-party applications use ETW for instrumentation, and some take advantage of the events that Windows provides. ETW has also been abstracted into the Windows preprocessor (WPP) software tracing technology, which provides a set of easy-to-use macros for tracing **printf**-style messages for debugging during development.

ETW was significantly upgraded for Windows Vista and Windows 7. One of the most significant new features is the unified event provider model and APIs. In short, the new unified APIs combine logging traces and writing to the Event Viewer into one consistent, easy-to-use mechanism for event providers. At the same time, several new features have been added to ETW to improve the developer and end-user experiences.

For more information about ETW and WPP, see Event Tracing and [Event Tracing for Windows (ETW)](https://msdn.microsoft.com/library/windows/hardware/ff545699).

## USB Support for ETW Logging


USB is one of the most prevalent means of connecting an ever-increasing variety of peripheral devices to PCs. There is a very large installed base of USB host PCs and USB peripheral devices, and system vendors, device vendors, and end users expect and demand that USB devices operate flawlessly at the system and device level.

The large installed base and proliferation of USB devices have uncovered compatibility issues between the Windows USB software stack, the USB host controller, and USB devices. These compatibility issues cause problems for customers such as device operation failures, system hangs, and system crashes.

It has been difficult or impossible to investigate and debug USB device issues without direct access to the system, and/or devices, or in some cases a system crash dump. Even with full access to the hardware and a crash dump, extracting the relevant information has been a time-intensive technique that is known only by a few core USB driver developers. You can debug USB problems by using hardware or software analyzers, but they are very expensive and are available to only a small percentage of professionals.

## USB ETW Support in Windows 7


In Windows 7, ETW provides an event logging mechanism that the USB driver stack can exploit to aid in investigating, diagnosing, and debugging USB-related issues. USB driver stack ETW event logging supports most or all debugging capabilities that are provided by the existing ad hoc logging mechanism in the USB driver stack, without any of its limitations. This translates into ease of debugging USB-related issues, which should provide a more robust USB driver stack in the long term.

We added ETW logging to the USB host controller drivers and to the USB hub driver in Windows 7. The USB host controller driver layer includes the host controller port driver (usbport.sys) and the miniport drivers (usbehci.sys, usbohci.sys, and usbuhci.sys). The USB hub driver layer consists of the USB hub driver (usbhub.sys). The USB driver ETW event providers are included in all editions and SKUs of Windows 7.

-   USB Hub Events

    While USB event collection is enabled, the USB hub event provider reports the addition and removal of USB hubs, the device summary events of all hubs, and port status changes. You can use these events to determine the root cause of most device enumeration failures.

-   USB Port Events

    While USB event collection is enabled, the USB port event provider reports I/O from client drivers, opening and closing of device endpoints, and miniport state transitions such as miniport start and stop. Logged I/O includes requests for the state of physical USB ports. State transitions on physical USB ports are one of the key initiators of activity in the core USB driver stack.

## USB ETW Support in Windows 8


Windows 8 provides a USB driver stack to support USB 3.0 devices. The Microsoft-provided USB 3.0 driver stack consists of three drivers: Usbxhci.sys, Ucx01000.sys, and Usbhub3.sys. All three drivers work together to add native support to Windows for most USB 3.0 host controllers. The new driver stack supports SuperSpeed, high-speed, full-speed, and low-speed devices. The USB 2.0 driver stack is supported on Windows 8. Through event traces, the USB 3.0 driver stack provides a view into the fine-grained activity of the host controller and all devices connected to it.

-   USB Hub3 Events

    While USB event collection is enabled, the USB Hub3 event provider reports the addition and removal of USB hubs, the device summary events of all hubs, port status changes, and power states of USB devices and hubs. Port status changes are state transitions on physical USB ports and are one of the key initiators of activity in the core USB driver stack. Hub3 reports the stages of the enumeration process, which point to the root cause most device enumeration failures. With the **StateMachine** keyword enabled, Hub3 reports the internal state machine activity for software device, hub, and port objects, which provide deeper visibility into the logic of the driver.

-   USB UCX Events

    While USB event collection is enabled, the USB UCX event provider reports I/O from client drivers and opening and closing of device endpoints and endpoint streams. With the **StateMachine** keyword enabled, UCX reports internal state machine activity for host controller and endpoint objects, which provide deeper visibility into the logic of the driver.

-   USB xHCI Events

    While USB event collection is enabled, the USB xHCI event provider reports the properties of the system's xHCI controllers and low-level details of xHCI operation. xHCI reports command requests sent to and completed by the xHCI hardware, including xHCI-specific completion codes.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Capture and view USB traces with Microsoft Message Analyzer](capture-and-view-ing-usb-traces-with-microsoft-message-analyzer-.md)</p></td>
<td><p>You can use Microsoft Message Analyzer (MMA) to capture and view live USB traces, or view an existing trace.</p></td>
</tr>
<tr class="even">
<td><p>[How to capture a USB event trace with Logman](how-to-capture-a-usb-event-trace.md)</p></td>
<td><p>This topic provides information about using the [Logman](http://go.microsoft.com/fwlink/p/?linkid=617153) tool to capture a USB ETW event trace. Logman is a tracing tool that is built into Windows. You can use Logman to capture events into an event trace log file.</p></td>
</tr>
<tr class="odd">
<td><p>[Using activity ID GUIDs in USB ETW traces](using-usb-etw.md)</p></td>
<td><p>This topic provides information about Activity ID GUIDs, how to add those GUIDs in the event trace providers, and view them in Netmon.</p></td>
</tr>
<tr class="even">
<td><p>[USB ETW traces in Netmon](viewing-etw-traces-in-netmon.md)</p></td>
<td><p>You can view USB ETW event traces using Microsoft Network Monitor, also referred to as Netmon. Netmon does not parse the trace automatically. It requires USB ETW parsers. USB ETW parsers are text files, written in Network Monitor Parser Language (NPL), that describe the structure of USB ETW event traces. The parsers also define USB-specific columns and filters. These parsers make Netmon the best tool for analyzing USB ETW traces.</p></td>
</tr>
<tr class="odd">
<td><p>[Using Xperf with USB ETW](using-xperf-with-usb-etw.md)</p></td>
<td><p>This topic describes how to use Xperf with Netmon to analyze USB trace data.</p></td>
</tr>
<tr class="even">
<td><p>[USB ETW and Power Management](usb-etw-and-power-management.md)</p></td>
<td><p>This topic provides a brief overview about using ETW to examine USB selective suspend state and identifying system energy efficiency problems by using the Windows PowerCfg utility.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Using USB ETW](using-usb-etw.md)  
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Event%20Tracing%20for%20Windows%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


