---
title: Calling WmiSystemControl to Handle WMI IRPs
description: Calling WmiSystemControl to Handle WMI IRPs
ms.assetid: a2fa53e2-6468-4c3c-8b41-9a97305abc43
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI", "WmiSystemControl"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling WmiSystemControl to Handle WMI IRPs





WMI library routines simplify handling of WMI requests because instead of processing each such request, a driver calls [**WmiSystemControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol). In the **WmiSystemControl** call, the driver passes an initialized [**WMILIB\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/ns-wmilib-_wmilib_context) structure that contains entry points to the driver's [WMI library callback routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/index) (*DpWmiXxx* routines) and information about the driver's data blocks and event blocks.

Because the WMI library provides no mechanism for passing dynamic instance names or a static instance name list, a driver can use the WMI library to handle requests involving only data blocks with static instance names based on a PDO or a single base name string. For more information about static and dynamic instance names, see [Defining WMI Instance Names](defining-wmi-instance-names.md). Nothing prevents a driver from using the WMI library to handle requests for such blocks and processing requests for other blocks in its [*DispatchSystemControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine. For more information, see [Processing WMI IRPs in a DispatchSystemControl Routine](processing-wmi-irps-in-a-dispatchsystemcontrol-routine.md).

To handle WMI IRPs by calling **WmiSystemControl**, a driver must implement certain required *DpWmiXxx* callback routines, and might implement additional optional *DpWmiXxx* callback routines:

-   [*DpWmiQueryReginfo*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_reginfo_callback)—(Required) Provides information about the data and event blocks being registered by the driver. WMI calls a driver's *DpWmiQueryReginfo* routine to process an [**IRP\_MN\_REGINFO**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-reginfo) or [**IRP\_MN\_REGINFO\_EX**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-reginfo-ex) request. For more information, see [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md).

-   [*DpWmiQueryDataBlock*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_datablock_callback)—(Required) Returns either a single instance or all instances of a data block. WMI calls a driver's *DpWmiQueryDataBlock* routine to process an [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-single-instance) or [**IRP\_MN\_QUERY\_ALL\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-all-data) request.

-   [*DpWmiSetDataBlock*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_set_datablock_callback)—(Optional) Changes all data items in a single instance of a data block. WMI calls a driver's *DpWmiSetDataBlock* routine to process an [**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-change-single-instance) request.

-   [*DpWmiSetDataItem*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_set_dataitem_callback)—(Optional) Changes a single data item in an instance of a data block. WMI calls a driver's *DpWmiSetDataItem* routine to process an [**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-change-single-item) request.

-   [*DpWmiFunctionControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_function_control_callback)—(Optional) Enables and disables event notification and data collection for blocks registered as expensive to collect. WMI calls a driver's *DpWmiFunctionControl* routine to process an [**IRP\_MN\_ENABLE\_COLLECTION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-enable-collection), [**IRP\_MN\_DISABLE\_COLLECTION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-disable-collection), [**IRP\_MN\_ENABLE\_EVENTS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-enable-events), or [**IRP\_MN\_DISABLE\_EVENTS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-disable-events) request.

-   [*DpWmiExecuteMethod*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_execute_method_callback)—(Optional) Executes a method associated with a data block. WMI calls a driver's *DpWmiExecuteMethod* routine to process an [**IRP\_MN\_EXECUTE\_METHOD**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-execute-method) request.

A driver's *DpWmiXxx* routines can have any names chosen by the driver writer.

Before calling [**WmiSystemControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol), the driver must initialize a [**WMILIB\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/ns-wmilib-_wmilib_context) structure with entry points to its *DpWmiXxx* routines and information about its data blocks and event blocks.

When the driver receives a WMI request:

1. The driver calls **WmiSystemControl** with a pointer to its initialized **WMILIB\_CONTEXT** structure, a pointer to its device object, and a pointer to the IRP.

2. WMI validates the IRP parameters and calls the driver's *DpWmiXxx* routine that processes the request. If the driver set no entry point in its **WMILIB\_CONTEXT** for an optional *DpWmiXxx* routine, WMI completes the IRP with default values and status.

3. In its *DpWmiXxx* routine, the driver processes the request and writes any output to the caller-supplied buffer. For example, a driver's [*DpWmiQueryDataBlock*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_datablock_callback) routine would write the requested instance(s) of the specified block to the buffer.

4. In all *DpWmiXxx* routines except [*DpWmiQueryReginfo*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_reginfo_callback), the driver calls [**WmiCompleteRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmicompleterequest) to complete the request, or returns STATUS\_PENDING to postpone completion, as for any IRP.

5. WMI performs any necessary postprocessing, packages any output in an appropriate **WNODE\_*XXX*** structure, and passes the output and status to the data consumer.

 

 




