---
title: Handling an IRP_MN_SURPRISE_REMOVAL Request
description: Handling an IRP_MN_SURPRISE_REMOVAL Request
ms.assetid: 39a90617-40ad-4c10-95d3-2b618d66d70e
keywords: ["surprise removals WDK PnP", "IRP_MN_SURPRISE_REMOVAL"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_SURPRISE\_REMOVAL Request





The Windows 2000 and later PnP manager sends this IRP to notify drivers that a device is no longer available for I/O operations and has probably been unexpectedly removed from the machine ("surprise removal").

The PnP manager sends an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request for the following reasons:

-   If the bus has hot-plug notification, it notifies the device's parent bus driver that the device has disappeared. The bus driver calls [**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353). In response, the PnP manager queries the bus driver for its children ([**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) for **BusRelations**). The PnP manager determines that the device is not in the new list of children and initiates its surprise-removal operations for the device.

-   The bus is enumerated for another reason and the surprise-removed device is not included in the list of children. The PnP manager initiates its surprise removal operations.

-   The function driver for the device determines that the device is no longer present (because, for example, its requests repeatedly time out). The bus might be enumerable but it does not have hot-plug notification. In this case, the function driver calls [**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361). In response, the PnP manager sends an [**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff551698) request to the device stack. The function driver sets the PNP\_DEVICE\_FAILED flag in the [**PNP\_DEVICE\_STATE**](#about-pnp_device_state) bitmask indicating that the device has failed.

-   The driver stack successfully completes an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request but then fails a subsequent [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. In such cases, the device is probably still connected.

All PnP drivers must handle this IRP and must set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS. A driver for a PnP device must be prepared to handle **IRP\_MN\_SURPRISE\_REMOVAL** at any time after the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine is called. Proper handling of the IRP enables the drivers and the PnP manager to:

1.  Disable the device, in case it is still connected.

    If the driver stack successfully completed an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request but then, for some reason, failed a subsequent [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request, the device must be disabled.

2.  Release hardware resources assigned to the device and make them available to another device.

    As soon as a device is no longer available, its hardware resources should be freed. The PnP manager can then reassign the resources to another device, including the same device, which a user might hot-plug back into the machine.

3.  Minimize the risk of data loss and system disruption.

    Devices that support hot-plugging and their drivers should be designed to handle surprise removal. Users expect to be able to remove devices that support hot-plugging at any time.

The PnP manager sends an **IRP\_MN\_SURPRISE\_REMOVAL** at IRQL = PASSIVE\_LEVEL in the context of a system thread.

The PnP manager sends this IRP to drivers before notifying user-mode applications and other kernel-mode components. After the IRP completes, the PnP manager sends an **EventCategoryTargetDeviceChange** notification with GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE to kernel-mode components that registered for such notification on the device.

The **IRP\_MN\_SURPRISE\_REMOVAL** IRP is handled first by the top driver in the device stack and then by each next lower driver.

In response to **IRP\_MN\_SURPRISE\_REMOVAL**, a driver must do the following, in the listed order:

1.  Determine if the device has been removed.

    The driver must always attempt to determine if the device is still connected. If it is, the driver must attempt to stop the device and disable it.

2.  Release the device's hardware resources (interrupts, I/O ports, memory registers, and DMA channels).

3.  In a parent bus driver, power down the bus slot if the driver is capable of doing so. Call [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to notify the power manager. For additional information, see [Power Management](implementing-power-management.md).

4.  Prevent any new I/O operations on the device.

    A driver should process subsequent [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718), [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720), [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784), and [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) requests, but the driver must prevent any new I/O operations. A driver must fail any subsequent IRPs that the driver would have handled if the device were present, besides close, clean-up, and PnP IRPs.

    A driver can set a bit in the device extension to indicate that the device has been surprise-removed. The driver's dispatch routines should check this bit.

5.  Fail outstanding I/O requests on the device.

6.  Continue to pass down any IRPs that the driver does not handle for the device.

7.  Disable device interfaces with [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700).

8.  Clean up any device-specific allocations, memory, events, or other system resources.

    A driver could postpone such clean-up until it receives the subsequent [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request, but if a legacy component has an open handle that cannot be closed, the remove IRP will never be sent.

9.  Leave the device object attached to the device stack.

    Do not detach and delete the device object until the subsequent **IRP\_MN\_REMOVE\_DEVICE** request.

10. Finish the IRP.

    In a function or filter driver:

    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Set up the next stack location with [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and pass the IRP to the next lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

    -   Propagate the status from **IoCallDriver** as the return status from the [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

    -   Do not complete the IRP.

    In a bus driver (that is handling this IRP for a child PDO):

    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

    -   Complete the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)) with IO\_NO\_INCREMENT.

    -   Return from the *DispatchPnP* routine.

After this IRP succeeds and all open handles to the device are closed, the PnP manager sends an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to the device stack. In response to the remove IRP, drivers detach their device objects from the stack and delete them. If a legacy component has a handle open to the device and it leaves the handle open despite I/O failures, the PnP manager never sends the remove IRP.

All drivers should handle this IRP and should note that the device has been physically removed from the machine. Some drivers, however, will not cause adverse results if they do not handle the IRP. For example, a device that consumes no system hardware resources and resides on a protocol-based bus, such as USB or 1394, cannot tie up hardware resources because it does not consume any. There is no risk of drivers attempting to access the device after it has been removed because the function and filter drivers access the device only through the parent bus driver. Because the bus supports removal notification, the parent bus driver is notified when the device disappears and the bus driver fails all subsequent attempts to access the device.

On Windows 98/Me, the PnP manager does not send this IRP. If a user removes a device without first using the appropriate user interface, the PnP manager sends only an **IRP\_MN\_REMOVE\_DEVICE** request to the drivers for the device. All WDM drivers must handle both **IRP\_MN\_SURPRISE\_REMOVAL** and **IRP\_MN\_REMOVE\_DEVICE**. The code for **IRP\_MN\_REMOVE\_DEVICE** should check whether the driver received a prior surprise-remove IRP and should handle both cases.

 ## Using GUID_REENUMERATE_SELF_INTERFACE_STANDARD

The GUID_REENUMERATE_SELF_INTERFACE_STANDARD interface enables a driver to request that its device be reenumerated.

To use this interface, send an IRP_MN_QUERY_INTERFACE IRP to your bus driver with InterfaceType = GUID_REENUMERATE_SELF_INTERFACE_STANDARD. The bus driver supplies a pointer to a REENUMERATE_SELF_INTERFACE_STANDARD structure that contains pointers to the individual routines of the interface. A [ReenumerateSelf routine](https://msdn.microsoft.com/library/windows/hardware/ff560837) requests that a bus driver reenumerate a child device.


## About PNP_DEVICE_STATE

The PNP\_DEVICE\_STATE type is a bitmask that describes the PnP state of a device. A driver returns a value of this type in response to an **IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE** request.

``` syntax
typedef ULONG PNP_DEVICE_STATE, *PPNP_DEVICE_STATE;
```

The flag bits in a PNP\_DEVICE\_STATE value are defined as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag bit</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PNP_DEVICE_DISABLED</td>
<td><p>The device is physically present but is disabled in hardware.</p></td>
</tr>
<tr class="even">
<td>PNP_DEVICE_DONT_DISPLAY_IN_UI</td>
<td><p>Do not display the device in the user interface. Set for a device that is physically present but not usable in the current configuration, such as a game port on a laptop that is not usable when the laptop is undocked. (Also see the <strong>NoDisplayInUI</strong> flag in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543095" data-raw-source="[&lt;strong&gt;DEVICE_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543095)"><strong>DEVICE_CAPABILITIES</strong></a> structure.)</p></td>
</tr>
<tr class="odd">
<td>PNP_DEVICE_FAILED</td>
<td><p>The device is present but not functioning properly.</p>
<p>When both this flag and PNP_DEVICE_RESOURCE_REQUIREMENTS_CHANGED are set, the device must be stopped before the PnP manager assigns new hardware resources (nonstop rebalance is not supported for the device).</p></td>
</tr>
<tr class="even">
<td>PNP_DEVICE_NOT_DISABLEABLE</td>
<td><p>The device is required when the computer starts. Such a device must not be disabled.</p>
<p>A driver sets this bit for a device that is required for proper system operation. For example, if a driver receives notification that a device is in the paging path (<a href="irp-mn-device-usage-notification.md" data-raw-source="[&lt;strong&gt;IRP_MN_DEVICE_USAGE_NOTIFICATION&lt;/strong&gt;](irp-mn-device-usage-notification.md)"><strong>IRP_MN_DEVICE_USAGE_NOTIFICATION</strong></a> for <strong>DeviceUsageTypePaging</strong>), the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549361" data-raw-source="[&lt;strong&gt;IoInvalidateDeviceState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549361)"><strong>IoInvalidateDeviceState</strong></a> and sets this flag in the resulting <strong>IRP_MN_QUERY_PNP_DEVICE_STATE</strong> request.</p>
<p>If this bit is set for a device, the PnP manager propagates this setting to the device&#39;s parent device, its parent&#39;s parent device, and so forth.</p>
<p>If this bit is set for a root-enumerated device, the device cannot be disabled or uninstalled.</p></td>
</tr>
<tr class="odd">
<td>PNP_DEVICE_REMOVED</td>
<td><p>The device has been physically removed.</p></td>
</tr>
<tr class="even">
<td>PNP_DEVICE_RESOURCE_REQUIREMENTS_CHANGED</td>
<td><p>The resource requirements for the device have changed.</p>
<p>Typically, a bus driver sets this flag when it has determined that it must expand its resource requirements in order to enumerate a new child device.</p></td>
</tr>
<tr class="odd">
<td>PNP_DEVICE_DISCONNECTED</td>
<td><p>The device driver is loaded, but this driver has detected that the device is no longer connected to the computer. Typically, this flag is used for function drivers that communicate with wireless devices. For example, the flag is set when the device moves out of range, and is cleared after the device moves back into range and re-connects.</p>
<p>A bus driver does not typically set this flag. The bus driver should instead stop enumerating the child device if the device is no longer connected. This flag is used only if the function driver manages the connection.</p>
<p>The sole purpose of this flag is to let clients know whether the device is connected. Setting the flag does not affect whether the driver is loaded.</p></td>
</tr>
</tbody>
</table>

 

The PnP manager queries a device's PNP\_DEVICE\_STATE right after starting the device by sending an **IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE** request to the device stack. In response to this IRP, the drivers for the device set the appropriate flags in PNP\_DEVICE\_STATE.

If any of the state characteristics change after the initial query, a driver notifies the PnP manager by calling [**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361). In response to a call to **IoInvalidateDeviceState**, the PnP manager queries the device's PNP\_DEVICE\_STATE again.

If a device is marked PNP\_DEVICE\_NOT\_DISABLEABLE, the debugger displays a DNUF\_NOT\_DISABLEABLE user flag for the devnode. The debugger also displays a **DisableableDepends** value that counts the number of reasons why the device cannot be disabled. This value is the sum of X+Y, where X is one if the device cannot be disabled and Y is the count of the device's child devices that cannot be disabled.




