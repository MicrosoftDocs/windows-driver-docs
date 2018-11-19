---
title: Porting AddDevice to EvtDriverDeviceAdd
description: Porting AddDevice to EvtDriverDeviceAdd
ms.assetid: 8FCFDA98-621E-415E-83D7-0371F55DD8A8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting AddDevice to EvtDriverDeviceAdd


Every Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver that supports Plug and Play must have an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback, which is the functional equivalent of a WDM driver’s [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) function.

A WDM [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) function creates the device object, creates the device interfaces, and initializes WMI but also initializes numerous variables in the driver’s device extension. WDM drivers typically defer the creation of I/O queues and the interrupt object until the [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) function is called to handle an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request.

The framework-based driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback creates a WDFDEVICE object to represent the device that has just been enumerated. It also performs numerous additional initialization tasks to provide the framework with the information that it requires to set up its own internal structures and the underlying WDM structures.

As a result, for most framework-based drivers the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback is significantly longer than the corresponding WDM [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) function. In a framework-based driver, nearly all of the device’s initialization code is in the *EvtDriverDeviceAdd* function. However, in the WDM version, the initialization code tends to be spread out through multiple functions in the driver.

The code in [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) appears in the following order:

1.  Fill in the [WDFDEVICE\_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure, which supplies information that is used to create the device object. For more information about using WDFDEVICE\_INIT, see [Creating a Framework Device Object](creating-a-framework-device-object.md).
2.  Set up the device object’s context area, which is analogous to the WDM device extension.
3.  [Create the device object](creating-a-framework-device-object.md).
4.  Perform additional initialization and start-up tasks, such as [creating I/O queues](creating-i-o-queues.md) and [interrupt objects](creating-an-interrupt-object.md).

A KMDF bus driver typically creates multiple device objects: an FDO for its role as the function driver for the bus itself and a PDO for each child device that is attached to the bus. The framework calls the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function when the system enumerates the bus. The driver itself then enumerates its child devices and creates PDOs to represent them. KMDF supports both [static](static-enumeration.md) and [dynamic](dynamic-enumeration.md) enumeration of child devices. It also includes additional PDO-specific features.

## Device Object Context Area


Drivers typically require storage that is associated with a device object to maintain pointers and object-specific data. In a WDM driver, the **DeviceExtension** field of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure provides such storage. In a framework-based driver, the object context area of the WDFDEVICE object serves the same purpose.

For information about allocating and accessing context space for framework objects, see [Framework Object Context Space](framework-object-context-space.md).

## Device Object Creation


A WDM driver creates a [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure to represent each device object and attaches the device object to the Plug and Play device stack. Framework-based drivers also create device objects, which are referred to by using WDFDEVICE handles.

After the WDF driver calls the required initialization methods, it sets attributes for the device object (typically, the size and type of the context area) and then calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create the device object. **WdfDeviceCreate** creates a WDFDEVICE object and an underlying WDM [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147), attaches the WDM **DEVICE\_OBJECT** to the device stack, and returns a handle to the WDFDEVICE object.

## Additional EvtDriverDeviceAdd Tasks


After the framework-based driver creates the device object, it should:

-   [Create I/O queues](creating-i-o-queues.md) and specify [request handlers](request-handlers.md) for the device object.
-   [Create device interfaces](using-device-interfaces.md).
-   Set [device idle policy](supporting-idle-power-down.md) and [wake settings](supporting-system-wake-up.md), if the device object owns power policy.
-   [Create an interrupt object](creating-an-interrupt-object.md), if the hardware supports interrupts.
-   [Initialize WMI](supporting-wmi-in-kmdf-drivers.md).<sup>†</sup>

† This functionality is only available to KMDF drivers.

A framework-based driver should set up the I/O queues and create the interrupt object in the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback, immediately after creating the device object. The framework connects the interrupt object and starts the queues at the appropriate time later, during start-device processing.

## Child Device Enumeration (PDOs, KMDF Only)


A driver that controls a bus typically creates multiple device objects: an FDO for its role as the function driver for the bus itself and a PDO for each child device that is attached to the bus. KMDF supports both static and dynamic enumeration of child devices. It also includes additional PDO-specific features.

The framework invokes the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function when the Plug and Play manager enumerates the bus. *EvtDriverDeviceAdd* creates an FDO for the bus, and then enumerates the child devices and creates a PDO for each one. The driver can enumerate the child devices either [statically](static-enumeration.md) or [dynamically](dynamic-enumeration.md).

Certain callback functions apply only to device objects that represent PDOs. When the driver initializes the device object, it registers the corresponding callbacks. PDOs respond to queries about device resources and resource requirements, requests to lock or eject the device, and requests to enable and disable the device wake signal.

In WDM drivers, these requests arrive as minor IRP codes in an [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) or [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) request. KMDF drivers handle them by implementing callbacks and registering the callbacks during device object initialization by calling [**WdfPdoInitSetEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff548805). The following table lists the PDO-specific callbacks:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">KMDF callback</th>
<th align="left">WDM IRP</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540895" data-raw-source="[&lt;em&gt;EvtDeviceResourcesQuery&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540895)"><em>EvtDeviceResourcesQuery</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551710" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_RESOURCES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551710)"><strong>IRP_MN_QUERY_RESOURCES</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540894" data-raw-source="[&lt;em&gt;EvtDeviceResourceRequirementsQuery&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540894)"><em>EvtDeviceResourceRequirementsQuery</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551715" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_RESOURCE_REQUIREMENTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551715)"><strong>IRP_MN_QUERY_RESOURCE_REQUIREMENTS</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540863" data-raw-source="[&lt;em&gt;EvtDeviceEject&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540863)"><em>EvtDeviceEject</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550853" data-raw-source="[&lt;strong&gt;IRP_MN_EJECT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550853)"><strong>IRP_MN_EJECT</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540909" data-raw-source="[&lt;em&gt;EvtDeviceSetLock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540909)"><em>EvtDeviceSetLock</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551742" data-raw-source="[&lt;strong&gt;IRP_MN_SET_LOCK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551742)"><strong>IRP_MN_SET_LOCK</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540866" data-raw-source="[&lt;em&gt;EvtDeviceEnableWakeAtBus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540866)"><em>EvtDeviceEnableWakeAtBus</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551766" data-raw-source="[&lt;strong&gt;IRP_MN_WAIT_WAKE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551766)"><strong>IRP_MN_WAIT_WAKE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540858" data-raw-source="[&lt;em&gt;EvtDeviceDisableWakeAtBus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540858)"><em>EvtDeviceDisableWakeAtBus</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551766" data-raw-source="[&lt;strong&gt;IRP_MN_WAIT_WAKE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551766)"><strong>IRP_MN_WAIT_WAKE</strong></a></p></td>
</tr>
</tbody>
</table>

 

Additional **WdfPdoInitXxx** methods enable the driver to specify device-specific data, such as device IDs.

 

 





