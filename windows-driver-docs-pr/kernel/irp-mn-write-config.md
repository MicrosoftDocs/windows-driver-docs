---
title: IRP_MN_WRITE_CONFIG
description: Bus drivers for buses with configuration space must handle this request for their child devices (child PDOs). Function and filter drivers do not handle this request.
ms.date: 08/12/2017
ms.assetid: d57c30b8-83bd-41c9-906d-b8c95f8ca54e
keywords:
 - IRP_MN_WRITE_CONFIG Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_WRITE\_CONFIG


Bus drivers for buses with configuration space must handle this request for their child devices (child PDOs). Function and filter drivers do not handle this request.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

A driver or other system component sends this IRP to write data to the configuration space of a device's parent bus.

A driver or other system component sends this IRP at IRQL &lt; DISPATCH\_LEVEL in an arbitrary thread context.

## Input Parameters


**Parameters.ReadWriteConfig** is a structure containing the following information:

```cpp
ULONG WhichSpace;
PVOID Buffer;
ULONG Offset;
ULONG Length
```

The members of the structure can be interpreted differently by different bus drivers, but the members are typically defined as follows:

<a href="" id="whichspace"></a>**WhichSpace**  
Specifies the configuration space. For information about values that can be specified for **WhichSpace**, see [**IRP\_MN\_READ\_CONFIG**](irp-mn-read-config.md).

<a href="" id="buffer"></a>**Buffer**  
Points to a buffer that contains the data to be written. The format of the buffer is bus-specific.

<a href="" id="offset"></a>**Offset**  
Specifies an offset into the configuration space.

<a href="" id="length"></a>**Length**  
Specifies the number of bytes to be written.

## Output Parameters


Returned in the I/O status block.

## I/O Status Block


A bus driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as STATUS\_INVALID\_PARAMETER\_*n*, STATUS\_NO\_SUCH\_DEVICE, or STATUS\_DEVICE\_NOT\_READY.

On success, a bus driver sets **Irp-&gt;IoStatus.Information** to the number of bytes written.

If a bus driver is unable to complete this request immediately, it can mark the IRP pending, return STATUS\_PENDING, and complete the IRP at a later time.

Operation
---------

A bus driver handles this IRP for its child devices (child PDOs).

Function and filter drivers do not handle this IRP; they pass it to the next lower driver with no changes to **Irp-&gt;IoStatus.Status** and do not set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Typically, a function driver sends this IRP to the device stack to which it is attached and the IRP is handled by the parent bus driver.

See [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847) for information about sending IRPs. The following steps apply specifically to this IRP:

-   Allocate a buffer from paged pool and initialize it with the data to be written.

-   Set the values in the next I/O stack location of the IRP: set **MajorFunction** to [**IRP\_MJ\_PNP**](irp-mj-pnp.md), set **MinorFunction** to **IRP\_MN\_WRITE\_CONFIG**, and set the appropriate values in **Parameters.ReadWriteConfig**.

-   Initialize **IoStatus.Status** to STATUS\_NOT\_SUPPORTED.

-   Deallocate the IRP and the buffer when they are no longer needed.

Drivers must send this IRP from IRQL &lt; DISPATCH\_LEVEL.

A driver can access a bus's configuration space at DISPATCH\_LEVEL through a bus interface routine, if the parent bus driver exports such an interface. To get a bus interface, a driver sends an [**IRP\_MN\_QUERY\_INTERFACE**](irp-mn-query-interface.md) request to its parent bus driver. The driver then calls the appropriate routine returned in the interface.

For example, to write configuration space from DISPATCH\_LEVEL a driver can call **IRP\_MN\_QUERY\_INTERFACE** during driver initialization to get the [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707) interface from the parent bus driver. The driver sends the query IRP from IRQL PASSIVE\_LEVEL. Later, from code at IRQL DISPATCH\_LEVEL, the driver calls the appropriate routine returned in the interface, such as the **Interface.SetBusData** routine.

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


[**IRP\_MN\_QUERY\_INTERFACE**](irp-mn-query-interface.md)

[**IRP\_MN\_READ\_CONFIG**](irp-mn-read-config.md)

 

 




