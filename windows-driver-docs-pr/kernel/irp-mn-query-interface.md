---
title: IRP_MN_QUERY_INTERFACE
description: The IRP_MN_QUERY_INTERFACE request enables a driver to export a direct-call interface to other drivers.A bus driver that exports an interface must handle this request for its child devices (child PDOs).
ms.date: 08/12/2017
ms.assetid: ae1dab46-c387-4e5f-9368-451e625ddbc1
keywords:
 - IRP_MN_QUERY_INTERFACE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_INTERFACE


The **IRP\_MN\_QUERY\_INTERFACE** request enables a driver to export a direct-call interface to other drivers.

A bus driver that exports an interface must handle this request for its child devices (child PDOs). Function and filter can optionally handle this request.

An "interface" in this context consists of one or more routines, and possibly data, exported by a driver or set of drivers. An interface has a structure that describes its contents and a GUID that identifies its type.

For example, the PCMCIA bus driver exports an interface of type GUID\_PCMCIA\_INTERFACE\_STANDARD that contains routines for operations such as getting the write-protect condition of a PCMCIA memory card. The function driver for such a memory card can send an **IRP\_MN\_QUERY\_INTERFACE** request to the parent PCMCIA bus driver to get pointers to the PCMCIA interface routines.

This section describes the query-interface IRP as a general mechanism. Drivers that expose an interface should provide additional information about their specific interface.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

A driver or system component sends this IRP to get information about an interface exported by a driver for a device.

A driver or system component sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

A driver can receive this IRP at any time after the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine has been called for the device. The device might or might not be started when this IRP is sent (that is, you cannot assume that the driver has successfully completed an [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md) request for the device).

## Input Parameters


The **Parameters.QueryInterface** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure is itself a structure, which describes the interface being requested. The structure contains the following information:

```cpp
CONST GUID *InterfaceType;
USHORT Size;
USHORT Version;
PINTERFACE Interface;
PVOID InterfaceSpecificData
```

The members of the structure are defined as follows:

<a href="" id="interfacetype"></a>**InterfaceType**  
Points to a GUID that identifies the interface being requested. The GUID can be for a system-defined interface, such as GUID\_BUS\_INTERFACE\_STANDARD, or a custom interface. The GUIDs for system-defined interfaces are listed in Wdmguid.h. GUIDs for custom interfaces should be generated with Uuidgen.

<a href="" id="size"></a>**Size**  
Specifies the size of the interface being requested. Drivers that handle this IRP must not return an [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure larger than **Size** bytes.

<a href="" id="version"></a>**Version**  
Specifies the version of the interface being requested.

If a driver supports more than one version of an interface, the driver returns the closest supported version without exceeding the requested version. The component that sent the IRP should examine the returned **Interface.Version** field and determine what to do based on that value.

<a href="" id="interface"></a>**Interface**  
Points to a structure in which to return the requested interface. This structure must contain an [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure as its first member. The component sending the IRP allocates this structure from paged memory.

A driver that exports an interface defines a new structure type containing the **INTERFACE** structure, plus members for routines and/or data in the interface. (The driver also defines a GUID for the interface, as described in the **InterfaceType** member, above.)

A driver that exports an interface defines the execution environment for each routine in the interface, including the IRQL at which the routine can be called, and so forth.

<a href="" id="interfacespecificdata"></a>**InterfaceSpecificData**  
Specifies additional information about the interface being requested.

For some interfaces, the component sending the IRP specifies additional information in this field. Typically, this field is **NULL** and the **InterfaceType** and **Version** are sufficient to identify the interface being requested.

## Output Parameters


On success, a driver fills in the members of the **Parameters.QueryInterface.Interface** structure.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a bus driver sets **Irp-&gt;IoStatus.Information** to zero.

If a function or filter driver does not handle this IRP, it calls [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and passes the IRP down to the next driver. Such a driver must not modify **Irp-&gt;IoStatus.Status** and must not complete the IRP.

If a bus driver does not export the requested interface and therefore does not handle this IRP for a child PDO, the bus driver leaves **Irp-&gt;IoStatus.Status** as is and completes the IRP.

Operation
---------

A driver handles this IRP if the parameters specify an interface the driver supports.

A driver must not queue this IRP if the IRP requests an interface that the driver does not support. A driver must check **Parameters.QueryInterface.InterfaceType** in its [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure. If the interface is not one the driver supports, the driver must pass the IRP to the next lower driver in the device stack without blocking.

Each interface must provide **InterfaceReference** and **InterfaceDereference** routines, and the driver that exports the interface must supply the addresses of these routines in the [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure. Before a driver returns an interface in response to the IRP, it must increment the interface's reference count by calling its **InterfaceReference** routine. When the driver that requested the interface has finished using it, that driver must decrement the reference count by calling the interface's **InterfaceDereference** routine.

If the driver that sends the IRP (driver *x*) later passes the interface to another driver (driver *y*) then driver *x* must increment the interface's reference count and driver *y* must decrement it.

A driver that handles this IRP should avoid passing the IRP to another device stack to get the requested interface. Such a design would create dependencies between the device stacks that are difficult to manage. For example, the device represented by the second device stack cannot be removed until the appropriate driver in the first stack dereferences the interface.

Interfaces can be bus-specific or bus-independent. Bus-specific interfaces are defined in the header files for those buses. The system defines a bus-independent interface, [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707), for exporting standard bus interfaces.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

This IRP is used specifically to pass routine entry points between layered kernel-mode drivers for a device. Do not confuse the interfaces exposed by this IRP with [*device interfaces*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interface). A device interface is used primarily for exposing a path to a device for use by user-mode components or other kernel components. For more information about device interfaces, see [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339).

**Sending This IRP**

See [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847) for information about sending IRPs. The following steps apply specifically to this IRP:

-   Allocate an [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure from paged pool and initialize it to zeros. If the interface will be called at IRQL &gt;= DISPATCH\_LEVEL, based on the interface contract, the caller can copy the contents to memory that is allocated from nonpaged pool.

-   Set the values in the next I/O stack location of the IRP: set **MajorFunction** to [**IRP\_MJ\_PNP**](irp-mj-pnp.md), set **MinorFunction** to **IRP\_MN\_QUERY\_INTERFACE**, and set the appropriate values in **Parameters.QueryInterface**.

-   Initialize **IoStatus.Status** to STATUS\_NOT\_SUPPORTED.

-   Deallocate the IRP and the **INTERFACE** structure when they are no longer needed.

-   Use the interface routines and context parameter as described in the specification for the interface.

-   Decrement the reference count using the [*InterfaceDereference*](https://msdn.microsoft.com/library/windows/hardware/ff547829) routine when the interface is no longer needed. Do not call any interface routines after dereferencing the interface.

A driver typically sends this IRP to the top of the device stack in which the driver is attached. If a driver sends this IRP to a different device stack, the driver must register for target device notification on the other device if the other device is not an ancestor of the device that the driver is servicing. Such a driver calls [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526) with an *EventCategory* of **EventCategoryTargetDeviceChange**. When the driver receives notification of type GUID\_TARGET\_DEVICE\_QUERY\_REMOVE, the driver must dereference the interface. The driver can requery for the interface if it receives a subsequent GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED notification.

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


[**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707)

[**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825)

[**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526)

 

 




