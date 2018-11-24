---
title: Handling WMI Requests
description: Handling WMI Requests
ms.assetid: d95b736c-045d-4888-8bab-b0a6201f8830
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling WMI Requests





All drivers must set a dispatch table entry point for a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine to handle WMI requests. If a driver [registers as a WMI data provider](registering-as-a-wmi-data-provider.md), it must handle all WMI requests. Otherwise, the driver must forward all WMI requests to the next lower driver.

All WMI IRPs have the major code [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) and a one of the following minor codes:

-   [**IRP\_MN\_REGINFO**](irp-mn-reginfo.md), [**IRP\_MN\_REGINFO\_EX**](irp-mn-reginfo-ex.md)—Queries or updates a driver's registration information after the driver has called [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480).

-   [**IRP\_MN\_QUERY\_ALL\_DATA**](irp-mn-query-all-data.md), [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](irp-mn-query-single-instance.md)—Queries for all instances or a single instance of a given data block.

-   [**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](irp-mn-change-single-item.md), [**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](irp-mn-change-single-instance.md)—Requests the driver to change a single item or multiple items in an instance of a data block.

-   [**IRP\_MN\_ENABLE\_COLLECTION**](irp-mn-enable-collection.md), [**IRP\_MN\_DISABLE\_COLLECTION**](irp-mn-disable-collection.md)—Requests the driver to start accumulating data for a block that the driver registered as expensive to collect, or to stop accumulating data for such a block.

-   [**IRP\_MN\_ENABLE\_EVENTS**](irp-mn-enable-events.md), [**IRP\_MN\_DISABLE\_EVENTS**](irp-mn-disable-events.md)—Requests the driver to start sending notification of a given event if the event occurs while it is enabled, or to stop sending notification of such an event.

-   [**IRP\_MN\_EXECUTE\_METHOD**](irp-mn-execute-method.md)—Requests the driver to execute a method associated with a data block.

The WMI kernel-mode component sends WMI IRPs any time following a driver's successful registration as a WMI data provider, typically when a user-mode data consumer has requested WMI information for a driver's device. If a driver registers as a WMI data provider by calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480), it must handle each subsequent WMI request in one of the following ways:

-   Call the kernel-mode WMI library routine [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834). A driver can call **WmiSystemControl** to handle requests concerning only blocks that do not use dynamic instance names, and that base static instance names on a single base name string or the [*device instance ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance-id) of a PDO. For more information, see [Calling WmiSystemControl to Handle WMI IRPs](calling-wmisystemcontrol-to-handle-wmi-irps.md).

-   In its [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine, process and complete any such request tagged with the pointer to its device object that the driver passed in its call to **IoWMIRegistrationControl**, and forward other [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) requests to the next lower driver. For more information, see [Processing WMI IRPs in a DispatchSystemControl Routine](processing-wmi-irps-in-a-dispatchsystemcontrol-routine.md).

For a list of the WMI minor IRPs, see [WMI Minor IRPs](wmi-minor-irps.md). 

 




