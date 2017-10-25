---
title: IRP_MN_QUERY_PNP_DEVICE_STATE
author: windows-driver-content
description: Function, filter, and bus drivers can handle this request.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 24362a20-9e9d-4566-bc95-ce52b91056af
keywords:
 - IRP_MN_QUERY_PNP_DEVICE_STATE Kernel-Mode Driver Architecture
---

# IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE


Function, filter, and bus drivers can handle this request.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP after the drivers for a device return success from the [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md) request sent when a device is first started. This IRP is not sent on a start after a stop for resource rebalancing. The PnP manager also sends this IRP when a driver for the device calls [**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361).

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of an arbitrary thread.

## Input Parameters


None

## Output Parameters


Returned in I/O status block.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as STATUS\_UNSUCCESSFUL.

On success, a driver sets **Irp-&gt;IoStatus.Information** to a [**PNP\_DEVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff559618) bitmask.

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
<td><p>Do not display the device in the user interface. Set for a device that is physically present but not usable in the current configuration, such as a game port on a laptop that is not usable when the laptop is undocked. (Also see the <strong>NoDisplayInUI</strong> flag in the [<strong>DEVICE_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure.)</p></td>
</tr>
<tr class="odd">
<td>PNP_DEVICE_FAILED</td>
<td><p>The device is present but not functioning properly.</p>
<p>When both this flag and PNP_DEVICE_RESOURCE_REQUIREMENTS_CHANGED are set, the device must be stopped before the PnP manager assigns new hardware resources (nonstop rebalance is not supported for the device).</p></td>
</tr>
<tr class="even">
<td>PNP_DEVICE_NOT_DISABLEABLE</td>
<td><p>The device is required when the computer starts. Such a device must not be disabled.</p>
<p>A driver sets this bit for a device that is required for proper system operation. For example, if a driver receives notification that a device is in the paging path ([<strong>IRP_MN_DEVICE_USAGE_NOTIFICATION</strong>](irp-mn-device-usage-notification.md) for <strong>DeviceUsageTypePaging</strong>), the driver calls [<strong>IoInvalidateDeviceState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549361) and sets this flag in the resulting <strong>IRP_MN_QUERY_PNP_DEVICE_STATE</strong> request.</p>
<p>If this bit is set for a device, the PnP manager propagates this setting to the device's parent device, its parent's parent device, and so forth.</p>
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

If a function or filter driver does not handle this IRP, it calls [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355), does not set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, and passes the IRP down to the next driver. Such a driver must not modify **Irp-&gt;IoStatus** and must not complete the IRP.

If a bus driver does not handle this IRP, it leaves **Irp-&gt;IoStatus.Status** as is and completes the IRP.

Operation
---------

This IRP is handled first by the driver at the top of the device stack and then by each next lower driver in the stack.

A driver handles this IRP if it has information about the PnP state of a device. A driver can set or clear the flags in the PNP\_DEVICE\_STATE bitmask. If another driver has set a PNP\_DEVICE\_STATE in **Irp-&gt;IoStatus.Information**, a driver must take care to modify the flags in that bitmask rather than overwrite the whole structure.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361)

[**PNP\_DEVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff559618)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_QUERY_PNP_DEVICE_STATE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


