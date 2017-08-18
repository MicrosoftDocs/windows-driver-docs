---
title: Handling WMI Requests
author: windows-driver-content
description: Handling WMI Requests
ms.assetid: d95b736c-045d-4888-8bab-b0a6201f8830
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling WMI Requests


## <a href="" id="ddk-handling-wmi-requests-kg"></a>


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

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20WMI%20Requests%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


