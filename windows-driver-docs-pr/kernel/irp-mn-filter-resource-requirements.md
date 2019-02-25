---
title: IRP_MN_FILTER_RESOURCE_REQUIREMENTS
description: The PnP manager sends this IRP to a device stack so the function driver can adjust the resources required by the device, if appropriate.The function driver typically handles this IRP.
ms.date: 08/12/2017
ms.assetid: f43dc60e-de88-4af0-ad83-3ce3a414d880
keywords:
 - IRP_MN_FILTER_RESOURCE_REQUIREMENTS Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS


The PnP manager sends this IRP to a device stack so the function driver can adjust the resources required by the device, if appropriate.

The function driver typically handles this IRP.

The parent bus driver (and bus filter drivers) should not handle this request for a child PDO; instead, such a driver should report resource requirements in response to an [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](irp-mn-query-resource-requirements.md) request.

Upper and lower-filter drivers do not handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP when it is preparing to allocate resource(s) to a device.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of an arbitrary thread.

## Input Parameters


**Irp-&gt;IoStatus.Information** points to an [**IO\_RESOURCE\_REQUIREMENTS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff550609) containing the hardware resource requirements for the device. The pointer is **NULL** if the device consumes no hardware resources.

**Parameters.FilterResourceRequirements.IoResourceRequirementList** also points to an **IO\_RESOURCE\_REQUIREMENTS\_LIST**, but the function driver should use the list in the **IoStatus** block.

## Output Parameters


Returned in the I/O status block.

## I/O Status Block


If a function driver handles this IRP, it handles it on the IRP's way back up the stack. If the function driver handles the IRP successfully, it sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS and sets **Irp-&gt;IoStatus.Information** to a pointer to an [**IO\_RESOURCE\_REQUIREMENTS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff550609) containing the filtered resource requirements. See the "Operation" section below for more information about setting the filtered resource list. If a function driver encounters an error when handling this IRP, it sets the error in **Irp-&gt;IoStatus.Status**. If a function driver does not handle this IRP, it uses [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) to pass the IRP down the stack unchanged.

Upper and lower-filter drivers do not handle this IRP. Such a driver calls **IoSkipCurrentIrpStackLocation**, passes the IRP down to the next driver, must not modify **Irp-&gt;IoStatus**, and must not complete the IRP.

The parent bus driver does not handle this IRP. It leaves **Irp-&gt;IoStatus** as is and completes the IRP.

Operation
---------

The PnP manager sends an [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](irp-mn-query-resource-requirements.md) request to the parent bus driver for the device, before the function driver has attached its device object to the device stack. To give the function driver an opportunity to modify the device's resource requirements, if appropriate, the PnP manager later sends an **IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS** request to the full device stack. The PnP manager sends this IRP before it allocates hardware resources to the device during initial device configuration. The PnP manager might also send this IRP during resource rebalancing.

When the PnP manager sends this IRP, it supplies the driver stack with a resource requirements list, which drivers can modify and return. The PnP manager supplies one of the following types of resource requirements list (listed in order of priority):

-   Forced configuration (modified from a resource list to a resource requirements list)

-   Override configuration

-   Basic configuration

-   Boot configuration (modified from a resource list to a resource requirements list)

If a function driver handles this IRP, it must set a completion routine and handle the IRP on its way back up the device stack. See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for information about handling a PnP IRP on its way back up the device stack.

If the function driver is not changing the size of the current list pointed to by **Irp-&gt;IoStatus.Information**, the driver can modify the list in place. If the driver needs to change the size of the requirements list, the driver must allocate a new [**IO\_RESOURCE\_REQUIREMENTS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff550609) list from paged memory and free the previous list. The PnP manager frees the returned structure when it is no longer needed.

A function driver must preserve the order of resources in the list pointed to by **Irp-&gt;IoStatus.Information** and must not alter resource tags that it does not handle. The driver must take care to adjust the requirements list in a way that the device's parent bus supports. If a function driver adds a new resource to the requirements list, and that resource is assigned to the device, the function driver should filter that resource out of the [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md) before passing the start IRP down to the bus driver.

If the function driver for the device does not handle this IRP, the PnP manager uses the resource requirements as specified by the parent bus driver in response to the [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](irp-mn-query-resource-requirements.md) request.

A function driver must be prepared to handle this IRP for a device at any time after the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine has been called for the device.

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


[**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)

[**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590)

[**IO\_RESOURCE\_REQUIREMENTS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff550609)

[**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md)

 

 




