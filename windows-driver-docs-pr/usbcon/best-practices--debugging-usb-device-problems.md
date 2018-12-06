---
Description: This topic provides tips for debugging USB device problems by using ETW events.
title: Debugging USB device issues by using ETW events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging USB device issues by using ETW events


This topic provides tips for debugging USB device problems by using ETW events.

-   [Diagnosing Device Enumeration Failures](#diagnosing-device-enumeration-failures)
-   [Diagnosing Device Start Failures](#diagnosing-device-start-failures)
-   [Profiling Device Insertion Timing](#profiling-device-insertion-timing)
-   [Software-Initiated Device Resume Timing](#software-initiated-device-resume-timing)
-   [Hardware-Initiated Device Resume Timing](#hardware-initiated-device-resume-timing)
-   [HUB RESUME FROM Selective Suspend Timing](#hub-resume-from-selective-suspend-timing)

## Diagnosing Device Enumeration Failures


You can use the ETW events that are associated with the USB hub enumeration task to determine the root cause of most device enumeration failures.

**To view the events in a trace log that are associated with the USB hub enumeration task**

1.  Open Netmon and locate an enumeration event, such as "Start Enumeration of Port". Click the event in the **Frame Summary** pane.
2.  Confirm that the task for this event is USB hub enumeration by examining the **Task** field for the event:
    1.  In the **Frame Details** pane, expand the **Net Event**, expand the **Header**, expand the **Descriptor**, and then locate the **Task** field.
    2.  Confirm that the Task field contains the value 2 (USB hub enumeration).

3.  Filter the events to show only those from the hub driver that have the task value 2:
    1.  Right-click the **Task** field.
    2.  Select **Add Selected Value** to **Display Filter**.
    3.  Right-click the event in the **Frame Summary** pane and select **Add**"Protocol Name" to **Display Filter**.
    4.  In the **Display Filter** pane, change "OR" to "AND". The following sample shows the resulting filter:
        ```cpp
        NetEvent.Header.Descriptor.Task == 0x2 AND ProtocolName == "USBHub_MicrosoftWindowsUSBUSBHUB"
        ```

        For more information on using filters in Netmon, see "USB Netmon Filters" in [Case Study: Troubleshooting an Unknown USB Device by Using ETW and Netmon](case-study--troubleshooting-an-unknown-usb-device-by-using-etw-and-netmon.md).

## Diagnosing Device Start Failures


If a device fails to start during the hub driver’s handling of the device’s start I/O request packet (IRP), you can use the ETW events that are associated with the USB device start task to troubleshoot the failure. In Netmon, locate a device-start event such as "USB Device Start IRP Dispatched". You can filter the events to only show those from the hub driver with a task value of 21 (USB device start). For more information on creating such a filter, see "Diagnosing Device Enumeration Failures" in this topic.

## Profiling Device Insertion Timing


You can determine where time is being spent in the hub driver during device insertion by looking at the timestamps of the enumeration events.

**Enumeration Timing**

The portion of device insertion time that the hub driver consumed to enumerate a device is the time elapsed between the following two events:

-   Start Enumeration of Port
-   Enumeration of Port Completed

**Profiling Enumeration Tasks**

When the USB hub driver enumerates a device, it logs the following events in the following order:

-   Start Enumeration of Port
-   Enumeration Debounce Completed
-   PDO Created for Enumeration
-   First Enumeration Port Reset Complete
-   Enumeration - CreateDevice Complete
-   Second Enumeration Port Reset Complete
-   Enumeration - InitializeDevice Complete
-   Enumeration - SetupDevice Complete
-   Enumeration of Port Completed

To determine the time that the hub driver consumed for each enumeration task, calculate the time that elapses between the preceding events.
**Elapsed Time between IoInvalidateDeviceRelations and IRP\_MN\_QUERY\_DEVICE\_RELATIONS**

To determine the portion of device-insertion time that the system consumed while it waited for the query device relations IRP, measure the elapsed time between the following two events:

-   Enumeration of Port Completed
-   USB Hub Query Device Relations (BusRelations) IRP Dispatched

**Elapsed Time between Completion of IRP\_MN\_QUERY\_DEVICE\_RELATIONS and IRP\_MN\_START\_DEVICE**

To determine the portion of device-insertion time between reporting the new physical device object (PDO) to the Plug and Play manager and receipt of the start IRP, measure the elapsed time between the following two events:

-   USB Hub Query Device Relations IRP Completed
-   USB Device Start IRP Dispatched

**Start IRP Timing**

To determine the time spent in the hub driver handling the start IRP, measure the elapsed time between the following two events:

-   USB Device Start IRP Dispatched
-   USB Device Start IRP Completed

## Software-Initiated Device Resume Timing


A device’s function driver can send a D0 device power request to resume the device from the suspend state. To determine the required amount of time for the device to resume from suspend and to be ready for transfer requests, measure the elapsed time between the following two events:

-   USB Device Set D0 Device Power IRP Dispatched
-   USB Device Set D0 Device Power IRP Completed

## Hardware-Initiated Device Resume Timing


A resume signal on the bus causes a device to resume from the suspended state. To determine the required amount of time for the device to resume to a state where it is ready for transfer requests, measure the elapsed time between the following two events:

-   Parent hub is not suspended:
    -   USB Device Wait Wake IRP Completed
    -   USB Device Set D0 Device Power IRP Completed
-   Parent hub is suspended:
    -   Started Resume of Hub from Selective Suspend (first of these events for any hub between the device and host controller)
    -   USB Device Set D0 Device Power IRP Completed

## HUB RESUME FROM Selective Suspend Timing


You can determine the required amount of time for a hub to resume from selective suspend by measuring the elapsed time between the following two events:

-   Started Resume of Hub from Selective Suspend
-   Resume of Hub Completed

**Note**  Hub resume timing depends on resume timing of all devices below the hub and possibly some or all hubs above the hub that is being resumed.

 

## Related topics
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  



