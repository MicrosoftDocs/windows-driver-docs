---
title: Processing WMI IRPs in a DispatchSystemControl Routine
description: Processing WMI IRPs in a DispatchSystemControl Routine
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI", "DispatchSystemControl routine"]
ms.date: 06/16/2017
---

# Processing WMI IRPs in a DispatchSystemControl Routine





A driver that handles WMI IRPs in its [*DispatchSystemControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine must handle such an IRP only if the device object pointer at **Parameters.WMI.ProviderId** matches the pointer passed by the driver in its call to [**IoWMIRegistrationControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiregistrationcontrol). Otherwise, the driver must forward the IRP to the next lower driver.

If the driver handles the request, it must:

Check the GUID at **Parameters.WMI.DataPath** to determine whether it represents a data block supported by the driver and, if not, fail the IRP with STATUS\_WMI\_GUID\_NOT\_FOUND.

A driver should check the input **WNODE\_*XXX*** structure at **Parameters.WMI.Buffer** for the instance name when handling any of the following requests:

[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](./irp-mn-query-single-instance.md)
[**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](./irp-mn-change-single-instance.md)
[**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](./irp-mn-change-single-item.md)
[**IRP\_MN\_EXECUTE\_METHOD**](./irp-mn-execute-method.md)
The driver should check for the instance name as follows:

- If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is set in **WnodeHeader.Flags**, use **InstanceIndex** as an index into the driver's list of static instance names for that block.

- If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is clear in **WnodeHeader.Flags**, use **OffsetInstanceName** as an offset to the instance name string in the input **WNODE\_*XXX*** structure. **OffsetInstanceName** is the offset in bytes from the beginning of the structure to a USHORT that indicates the length of the instance name string in bytes (not characters), including the NUL terminator if present, followed by the string itself in Unicode.

If the driver cannot locate the instance specified by **InstanceIndex** or **OffsetInstanceName**, it must fail the IRP with STATUS\_WMI\_INSTANCE\_NOT\_FOUND.

For an [**IRP\_MN\_EXECUTE\_METHOD**](./irp-mn-execute-method.md) request, check **MethodID** in the input [**WNODE\_METHOD\_ITEM**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-tagwnode_method_item) and, if the method is not valid for that data block, fail the IRP with STATUS\_WMI\_ITEMID\_NOT\_FOUND.

If the request generates output, a driver should check the size of the buffer at **Parameters.WMI.BufferSize** when handling any of the following requests:

[**IRP\_MN\_QUERY\_ALL\_DATA**](./irp-mn-query-all-data.md)
[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](./irp-mn-query-single-instance.md)
[**IRP\_MN\_EXECUTE\_METHOD**](./irp-mn-execute-method.md)
If the buffer is too small to receive the output, but at least **sizeof**(**WNODE\_TOO\_SMALL**), the driver should succeed the IRP and write a [**WNODE\_TOO\_SMALL**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-tagwnode_too_small) structure to the buffer at **Parameters.WMI.Buffer**. If the buffer is smaller than **sizeof**(**WNODE\_TOO\_SMALL**), the driver fails the IRP with an NTSTATUS code of STATUS\_BUFFER\_TOO\_SMALL.

If the request generates output and the buffer size is adequate, write the following output to the buffer at **Parameters.WMI.Buffer**:
-   For an **IRP\_MN\_QUERY\_ALL\_DATA** request, the driver writes a [**WNODE\_ALL\_DATA**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-tagwnode_all_data) structure that contains data for all instances of the specified data block.
-   For an **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** request, the driver writes a [**WNODE\_SINGLE\_INSTANCE**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-tagwnode_single_instance) structure that contains data for the specified instance of a data block.
-   For an **IRP\_MN\_EXECUTE\_METHOD** if the method generates output, the driver writes the method output in driver-determined format following the input [**WNODE\_METHOD\_ITEM**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-tagwnode_method_item) in the buffer (overwriting input data, if any).

Set **Irp-&gt;IoStatus.Information** to the number of bytes written to the buffer at **Parameters.WMI.Buffer** and **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

Call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to complete the IRP.

For more information, see [WMI WNODE\_*XXX* Structures](wmi-wnode-xxx-structures.md).

 

