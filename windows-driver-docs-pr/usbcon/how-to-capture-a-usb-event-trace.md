---
title: How to Capture a USB Event Trace With Logman
description: This article provides information about using the Logman tool to capture a USB ETW event trace.
ms.date: 01/12/2024
---

# How to capture a USB event trace with Logman

This article provides information about using the [Logman](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753820(v=ws.10)) tool to capture a USB ETW event trace. Logman is a tracing tool that is built into Windows. You can use Logman to capture events into an event trace log file.

## Prerequisites

Event trace log files can grow very quickly, but a smaller log file is easier to navigate and easier to transmit. Before you start a trace, consider taking the following steps to exclude extraneous events from the log so that you can focus on the device activity that you want to examine:

- Disconnect any non-critical USB devices that are not the device of interest. Fewer devices result in smaller traces making it easier to read and analyze.
- If your system has a USB keyboard or mouse, enter the trace commands by using Remote Desktop instead.
- Narrow the start and the end of the trace as much as possible around the operations of interest.
- If you are interested in only a certain category of USB events, you can use keywords to filter the events that are recorded. For more information, see Remarks.

Event traces from the USB 3.0 driver stack are similar to the USB 2.0 driver stack traces, which were introduced in Windows 7. Event traces from the USB 2.0 driver stack can be captured on a Windows 8 computer. The way you capture event traces from USB 2.0 and USB 3.0 driver stacks is similar. You can capture events from the USB 2.0 or USB 3.0 driver stack independently. When you connect a USB 2.0 device to a USB 3.0 host controller, you get event traces from the USB 3.0 driver stack. In that case, you will view new USB 3.0 driver stack events for a USB 2.0 device.

## Instructions

### To collect USB trace events

1. Open a command-prompt window that has administrative privileges. To do so, select Start, type **cmd** in the search box, Select and hold (or right-click) cmd.exe, and then select **Run as administrator**.

1. In the command-prompt window, enter these commands to start a capture session:

    ```cpp
    logman create trace -n usbtrace -o %SystemRoot%\Tracing\usbtrace.etl -nb 128 640 -bs 128
    logman update trace -n usbtrace -p Microsoft-Windows-USB-USBXHCI (Default,PartialDataBusTrace)
    logman update trace -n usbtrace -p Microsoft-Windows-USB-UCX (Default,PartialDataBusTrace)
    logman update trace -n usbtrace -p Microsoft-Windows-USB-USBHUB3 (Default,PartialDataBusTrace)
    logman update trace -n usbtrace -p Microsoft-Windows-USB-USBPORT
    logman update trace -n usbtrace -p Microsoft-Windows-USB-USBHUB
    logman update trace -n usbtrace -p Microsoft-Windows-Kernel-IoTrace 0 2
    logman start -n usbtrace

    ```

    After each of these commands completes, Logman displays `The command completed successfully.`

1. Perform the operations that you'll want to capture. For example, to capture events for device enumeration, you can plug in a USB flash drive that shows up as an "Unknown device" in **Device Manager**. Keep the command prompt window open.

1. Stop the session after you have completed the scenario. Enter these commands to end the capture session:

    You can stop USB hub and port event collection by running the following command:

    ```cpp
    logman stop -n usbtrace
    logman delete -n usbtrace
    move /Y %SystemRoot%\Tracing\usbtrace_000001.etl %SystemRoot%\Tracing\usbtrace.etl

    ```

The preceding capture session generates an etl file, named usbtrace.etl. The trace file is stored at %SystemRoot%\\Tracing\\usbtrace.etl (C:\\Windows\\Tracing\\usbtrace.etl). Move the file to another location or rename it in order to avoid overwriting it when you capture the next session.

The file contains event traces from the USB 3.0 and USB 2.0 driver stacks. If you want to reduce the event traces to just one USB driver stack, remove the other driver stack from your next trace session. You can do so by modifying the command sequence shown in step 2 to remove the "logman update" lines corresponding to the driver stack you want to remove from the trace session.

## Remarks

### Capture filters for USB 3.0 driver stack events

Notice ETW keywords such as **Default** and **PartialDataBusTrace** in the Logman capture commands. Those words are ETW keywords that indicate the types of events you want to view. You can use ETW keywords to filter the events that USB drivers write to a trace log and customize how much information you want to view about events captured from the USB 3.0 driver stack. Events that match any of your keywords are saved. Note that this method of filtering is for use at capture time, not during analysis.

You can filter events based on keywords depending on your requirements. Here are keywords for filtering USB 3.0 driver stack events:

| ETW keyword | Description |
|---|---|
| **Default** | Shows events that are useful for general troubleshooting. The events are similar to USB 2.0 ETW events but do not include any USB transfer events. |
| **StateMachine** | Shows driver-internal state machine transitions. The events are not included in the **Default** keyword. |
| **Rundown** | Shows device information events at the beginning of the trace and captures the starting state of the USB tree. The device information **Rundown** events are important to save so that the trace contains details, such as the USB descriptors and USB Device Description, of connected devices. These events are included in the **Default** keyword. When you don't use the **Default** keyword, you should use the **Rundown** keyword. The remaining Rundown events provide information on recent state transitions of the driver-internal state machines. These events are included in the **StateMachine** keyword. |
| **Power** | Shows a subset of **Default** events. Shows device power transition events. |
| **IRP** | Shows a subset of **Default** events. The events show IRPs from the client driver and IRPs resulting from user-mode requests. However, valid USB transfer (URB) requests are not shown with the **IRP** keyword, and require **HeadersBusTrace**, **PartialDataBusTrace**, or **FullDataBusTrace** in order to be shown. |
| **HeadersBusTrace** | Shows all USB transfer events but doesn't save data packets. |
| **PartialDataBusTrace** | Shows all USB transfer events and saves a limited payload of bus data. |
| **FullDataBusTrace** | Shows all USB transfer events and saves up to 4 KB of bus data for bulk, interrupt, and control transfers. Note that only the first buffer of a chained MDL is logged. Isochronous bus data is never logged (though the **[URB_ISOCH_TRANSFER](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_isoch_transfer)** request structure is saved). For more information, see [How to send chained MDLs](how-to-send-chained-mdls.md) and [How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md). |
| **HWVerifyHost** | Shows a subset of **Default** events. The events indicate when an error occurs in the USB host controller hardware. |
| **HWVerifyHub** | Shows a subset of **Default** events. The events indicate when an error occurs in the USB hub hardware. |
| **HWVerifyDevice** | Shows a subset of **Default** events. The events indicate when an error occurs in the USB device hardware. |

As an example, here is a sequence of commands that start a session to capture USB device power transitions. Due to the selection of providers (the USB 3.0 driver stack), events are captured only for devices that are connected downstream of a USB 3.0 host controller.

```console
logman create trace -n usbtrace -o %SystemRoot%\Tracing\usbtrace.etl -nb 128 640 -bs 128
logman update trace -n usbtrace -p Microsoft-Windows-USB-USBXHCI (Rundown,Power)
logman update trace -n usbtrace -p Microsoft-Windows-USB-UCX (Rundown,Power)
logman update trace -n usbtrace -p Microsoft-Windows-USB-USBHUB3 (Rundown,Power)
logman update trace -n usbtrace -p Microsoft-Windows-Kernel-IoTrace 0 2
logman start -n usbtrace
```

### Capture filters for power events

A useful ETW keyword for USB devices is the USB port driver's PowerDiagnostics flag. When you use this keyword, the port driver logs host-controller and endpoint information but omits all events that describe transfers. If you do not need to see the transfer events, you can use the PowerDiagnostics keyword to reduce the size of a trace log by as much as 85 percent. Specify the PowerDiagnostics keyword when you start the trace, as shown in the following example:

```console
Logman start Usbtrace -p Microsoft-Windows-USB-USBPORT PowerDiagnostics -o usbtrace.etl -ets -nb 128 640 -bs 128

Logman update Usbtrace -p Microsoft-Windows-USB-USBHUB –ets
```

If your filtered trace log has many host controller asynchronous schedule enable and disable events, you can filter them out when viewing the log by using a Netmon filter, as shown in the following example:

```console
NOT (Description == "USBPort_MicrosoftWindowsUSBUSBPORT:Host Controller Async Schedule Enable"
OR Description == "USBPort_MicrosoftWindowsUSBUSBPORT:Host Controller Async Schedule Disable")
```

For more information on Netmon filters, see "USB Netmon Filters" in [Case Study: Troubleshooting an unknown USB device by using ETW and Netmon](case-study--troubleshooting-an-unknown-usb-device-by-using-etw-and-netmon.md).

Sometimes it is helpful to have the transfer events in your trace log, such as hub requests and device requests that result in errors such as an XACT error or a stall. You might first capture a log without the transfer events and analyze that smaller log. Then run the trace again without filtering after you have a general understanding of the issues in your problem scenario.

## Related topics

- [Using USB ETW](using-usb-etw.md)
- [USB Event Tracing for Windows](usb-event-tracing-for-windows.md)
- [Defining Keywords Used to Classify Types of Events](/windows/desktop/WES/defining-keywords-used-to-classify-types-of-events)
