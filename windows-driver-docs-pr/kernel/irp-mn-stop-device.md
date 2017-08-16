---
title: IRP\_MN\_STOP\_DEVICE
author: windows-driver-content
description: All PnP drivers must handle this IRP.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: a5c81db0-e753-4d91-97e4-c58ea05f5ce8
keywords:
 - IRP_MN_STOP_DEVICE Kernel-Mode Driver Architecture
---

# IRP\_MN\_STOP\_DEVICE


All PnP drivers must handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP to stop a device so it can reconfigure the device's hardware resources.

On Windows 2000 and later systems, the PnP manager sends this IRP only if a prior [**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md) completed successfully.

On Windows 98/Me, the PnP manager also sends this IRP when a device is being disabled and when a device stack has failed an **IRP\_MN\_START\_DEVICE** request. In cases of failed start, the PnP manager sends this IRP without a preceding [**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md) request.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver must set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

Operation
---------

This IRP is handled first by the driver at the top of the device stack and then passed down to each lower driver in the stack.

In response to this IRP, Windows 2000 and later drivers stop the device and release any hardware resources being used by the device, such as I/O ports and interrupts.

On Windows 2000 and later, a stop IRP is used solely to free a device's hardware resources so they can be reconfigured. Once the resources are reconfigured, the device is restarted. A stop IRP is not a precursor to a remove IRP. See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for more information about the order in which PnP IRPs are sent to devices.

On Windows 98/Me, a stop IRP is also used after a failed start and when a device is being disabled. WDM drivers that run on these operating systems should stop the device, fail any incoming I/O, and disable and deregister any user-mode interfaces.

A driver must not fail this IRP. If a driver cannot release the device's hardware resources, it must fail the preceding query-stop IRP.

See [Stopping a Device](https://msdn.microsoft.com/library/windows/hardware/ff563868) for detailed information about handling stop IRPs.

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


[**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md)

[**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md)

[**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)

[**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_STOP_DEVICE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


