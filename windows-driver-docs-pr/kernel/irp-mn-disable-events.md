---
title: IRP_MN_DISABLE_EVENTS
description: Learn about the 'IRP_MN_DISABLE_EVENTS' kernel-mode driver architecture. Any WMI driver that registers one or more event blocks must handle this IRP.
ms.date: 08/12/2017
keywords:
 - IRP_MN_DISABLE_EVENTS Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_DISABLE\_EVENTS


Any WMI driver that registers one or more event blocks must handle this IRP. A driver can handle WMI IRPs either by calling [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) or by handling the IRP itself, as described in [Handling WMI Requests](./handling-wmi-requests.md).

If a driver calls [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) to handle an **IRP\_MN\_DISABLE\_EVENTS** request, WMI in turn calls that driver's [*DpWmiFunctionControl*](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_function_control_callback) routine.

## Major Code

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)

## When Sent

WMI sends this IRP to inform the driver that a data consumer has requested no further notification of an event.

WMI sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


**Parameters.WMI.ProviderId** points to the device object of the driver that should respond to the request. This pointer is located in the driver's I/O stack location in the IRP.

**Parameters.WMI.DataPath** points to a GUID that identifies the event block to disable.

## Output Parameters


None.

## I/O Status Block


If the driver handles the IRP by calling [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol), WMI sets **Irp-&gt;IoStatus.Status** and **Irp-&gt;IoStatus.Information** in the I/O status block.

Otherwise, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as the following:

STATUS\_WMI\_GUID\_NOT\_FOUND

STATUS\_INVALID\_DEVICE\_REQUEST

On success, a driver sets **Irp-&gt;IoStatus.Information** to zero.

## Operation

A driver can handle WMI IRPs either by calling [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) or by handling the IRP itself, as described in [Handling WMI Requests](./handling-wmi-requests.md).

If a driver handles WMI IRPs by calling [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol), that routine calls the driver's [*DpWmiFunctionControl*](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_function_control_callback) routine, or returns STATUS\_SUCCESS if the driver does not define the routine.

If a driver handles an **IRP\_MN\_DISABLE\_EVENTS** request itself, it should do so only if **Parameters.WMI.ProviderId** points to the same device object as the pointer that the driver passed to [**IoWMIRegistrationControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiregistrationcontrol). Otherwise, the driver must forward the request to the next-lower driver.

Before handling a request, the driver must determine whether **Parameters.WMI.DataPath** points to a GUID the driver supports. If not, the driver must fail the IRP and return STATUS\_WMI\_GUID\_NOT\_FOUND.

If the driver supports the event block, it disables the event for all instances of that block.

It is unnecessary for the driver to check whether events are already disabled for the event block because WMI sends a single disable request for that event block when the last data consumer disables the event. WMI will not send another disable request without an intervening request to enable.

For details about defining event blocks, see [Designing WMI Data and Event Blocks](./designing-wmi-data-and-event-blocks.md).

## Requirements

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


[*DpWmiFunctionControl*](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_function_control_callback)

[**IoWMIRegistrationControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiregistrationcontrol)

[**IRP\_MN\_ENABLE\_EVENTS**](irp-mn-enable-events.md)

[**WMILIB\_CONTEXT**](/windows-hardware/drivers/ddi/wmilib/ns-wmilib-_wmilib_context)

[**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol)

 

