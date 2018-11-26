---
title: IRP_MN_QUERY_BUS_INFORMATION
description: The PnP manager uses this IRP to request the type and instance number of a device's parent bus.Bus drivers should handle this request for their child devices (PDOs). Function and filter drivers do not handle this IRP.
ms.date: 08/12/2017
ms.assetid: a7ea1a81-7f03-41c7-8861-a2e1813c15cf
keywords:
 - IRP_MN_QUERY_BUS_INFORMATION Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_BUS\_INFORMATION


The PnP manager uses this IRP to request the type and instance number of a device's parent bus.

Bus drivers should handle this request for their child devices (PDOs). Function and filter drivers do not handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP when a device is enumerated.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


None

## Output Parameters


Returned in the I/O status block.

## I/O Status Block


A bus driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a bus driver sets **Irp-&gt;IoStatus.Information** to a pointer to a completed [**PNP\_BUS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559608) structure. (See the "Operation" section for more information.) On an error, the bus driver sets **Irp-&gt;IoStatus.Information** to zero.

Function and filter drivers do not handle this IRP.

Operation
---------

The information returned in response to this IRP is available to the function and filter drivers for devices on the bus. Function and filter drivers can call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) to request a **DevicePropertyBusTypeGuid**, **DevicePropertyLegacyBusType**, or **DevicePropertyBusNumber**. Function and filter drivers that support devices on more than one bus can use this information to determine on which bus a particular device resides.

If a bus driver returns information in response to this IRP, it allocates a **PNP\_BUS\_INFORMATION** structure from paged memory. The PnP manager frees the structure when it is no longer needed.

A **PNP\_BUS\_INFORMATION** structure has the following format:

```cpp
typedef struct _PNP_BUS_INFORMATION {
    GUID BusTypeGuid;
    INTERFACE_TYPE LegacyBusType;
    ULONG BusNumber;
} PNP_BUS_INFORMATION, *PPNP_BUS_INFORMATION;
```

The members of the structure are defined as follows:

<a href="" id="bustypeguid"></a>**BusTypeGuid**  
A bus driver sets **BusTypeGuid** to the GUID for the type of the bus on which the device resides. GUIDs for standard bus types are listed in Wdmguid.h. Driver writers should generate GUIDs for other bus types using Uuidgen.

<a href="" id="legacybustype"></a>**LegacyBusType**  
A PnP bus driver sets **LegacyBusType** to the [**INTERFACE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff547839) of the parent bus. The interface types are defined in Wdm.h. Some buses have a specific **INTERFACE\_TYPE** value, such as **PCMCIABus**, **PCIBus**, or **PNPISABus**. For other buses, especially newer buses like USB, the bus driver sets this member to **PNPBus**.

The **LegacyBusType** specifies the interface used to communicate with the device. This may or may not correspond to the type of the parent bus. For example, the interface for a CardBus card that is plugged into a PCI CardBus controller is **PCIBus**. However, the interface for a PCMCIA card on a PCI CardBus controller is **PCMCIABus**.

<a href="" id="busnumber"></a>**BusNumber**  
A bus driver sets **BusNumber** to a number distinguishing the bus from other buses of the same type on the computer. The bus-numbering scheme is bus-specific. Bus numbers may be virtual, but must match any numbering used by legacy interfaces such as [**IoReportResourceUsage**](https://msdn.microsoft.com/library/windows/hardware/ff549616).

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

Call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) to get information about the bus to which a device is attached.

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


[**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203)

 

 




