---
title: Declaring Functions Using Function Role Types for WDM Drivers
description: Declaring Functions Using Function Role Types for WDM Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Declaring Functions Using Function Role Types for WDM Drivers

> [!NOTE]
> Starting in Windows 10 Version 2004, [Static Driver Verifier](/windows-hardware/drivers/devtest/static-driver-verifier) (SDV) no longer requires annotations to identify role types of dispatch routines for WDM drivers.  Please follow the guidance in the *Basic and Advanced Initializations* section of this page.

To inform SDV about the driver's entry points when you analyze a WDM driver, you must declare functions using function role type declarations. The function role types are defined in Wdm.h. Each entry point in the *DriverEntry* routine in your WDM driver must be declared by specifying the corresponding role type. The role types are predefined typedefs that correspond to the recognized entry points in a WDM driver.

For example, to create a function role type declaration for a driver's [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine called *CsampUnload*, use the predefined typedef DRIVER\_UNLOAD role type declaration. The function role type declaration must appear before the function definition.

```
DRIVER_UNLOAD CsampUnload;
```

The definition of the *CsampUnload* function remains unchanged:

```
VOID
CsampUnload(
    IN PDRIVER_OBJECT DriverObject
    )
{
    ...
}
```

SDV recognizes the types of entry points shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WDM function role type</th>
<th align="left">WDM routine</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DRIVER_INITIALIZE</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize" data-raw-source="[&lt;em&gt;DriverEntry&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)"><em>DriverEntry</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>DRIVER_STARTIO</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio" data-raw-source="[&lt;em&gt;StartIO&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio)"><em>StartIO</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>DRIVER_UNLOAD</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload" data-raw-source="[&lt;em&gt;Unload&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)"><em>Unload</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>DRIVER_ADD_DEVICE</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device" data-raw-source="[&lt;em&gt;AddDevice&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)"><em>AddDevice</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<strong><em>Dispatch_type</em>(</strong> <em>type</em> <strong>)</strong>
DRIVER_DISPATCH</td>
<td align="left"><p>The dispatch routine(s) used by the driver. See <a href="/windows-hardware/drivers/kernel/writing-dispatch-routines" data-raw-source="[Writing Dispatch Routines](../kernel/writing-dispatch-routines.md)">Writing Dispatch Routines</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IO_COMPLETION_ROUTINE</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine" data-raw-source="[&lt;em&gt;IoCompletion&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine)"><em>IoCompletion</em></a></p>
<p>The <em>IoCompletion</em> routine is set by calling <em>IoSetCompletionRoutine</em> or <em>IoSetCompletionRoutineEx</em> and passing the function pointer to the <em>IoCompletion</em> routine as the second parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DRIVER_CANCEL</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel" data-raw-source="[&lt;em&gt;Cancel&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel)"><em>Cancel</em></a></p>
<p>The <strong>Cancel</strong> routine is set by calling <strong>IoSetCancelRoutine</strong> and passing the function pointer to the cancellation routine for the IRP as the second parameter to the function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IO_DPC_ROUTINE</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine" data-raw-source="[&lt;em&gt;DpcForIsr&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine)"><em>DpcForIsr</em></a></p>
<p>The <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine" data-raw-source="[&lt;em&gt;DpcForIsr&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine)"><em>DpcForIsr</em></a> routine is registered by calling <em>IoInitializeDpcRequest</em> and passing the function pointer to the <em>DpcForIsr</em> routine as the second parameter. To queue the DPC, call <em>IoQueueDpc</em> from the ISR routine by using the same DPC object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KDEFERRED_ROUTINE</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine" data-raw-source="[&lt;em&gt;CustomDpc&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine)"><em>CustomDpc</em></a></p>
<p>The <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine" data-raw-source="[&lt;em&gt;CustomDpc&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine)"><em>CustomDpc</em></a> routine is set by calling <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializedpc" data-raw-source="[&lt;strong&gt;KeInitializeDpc&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializedpc)"><strong>KeInitializeDpc</strong></a> and passing the function pointer to the <em>CustomDpc</em> as the second parameter. To queue the <em>CustomDpc</em> for the driver, call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc" data-raw-source="[&lt;strong&gt;KeInsertQueueDpc&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc)"><strong>KeInsertQueueDpc</strong></a> from the ISR routine by using the same DPC object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSERVICE_ROUTINE</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine" data-raw-source="[&lt;em&gt;InterruptService&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine)"><em>InterruptService</em></a></p>
<p>The InterruptService routine (ISR) services a device interrupt and schedules post-interrupt processing of received data, if necessary.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>REQUEST_POWER_COMPLETE</p></td>
<td align="left"><p>The <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-request_power_complete" data-raw-source="[&lt;em&gt;PowerCompletion&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-request_power_complete)"><em>PowerCompletion</em></a> callback routine completes the processing of a power IRP. If the driver needs to perform additional tasks after all other drivers have completed the IRP, the driver registers a <em>PowerCompletion</em> callback routine during the call to the <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp" data-raw-source="[&lt;strong&gt;PoRequestPowerIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp)"><strong>PoRequestPowerIrp</strong></a> routine that allocates the IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>WORKER_THREAD_ROUTINE</p></td>
<td align="left"><p><em>Routine</em></p>
<p><em>Routine</em> is the callback routine that is specified in the second parameter to the <a href="/windows-hardware/drivers/kernel/mmcreatemdl" data-raw-source="[&lt;strong&gt;ExInitializeWorkItem&lt;/strong&gt;](../kernel/mmcreatemdl.md)"><strong>ExInitializeWorkItem</strong></a> function.</p>
<p>The <em>Routine</em> should only be declared this way if the driver calls <strong>ExQueueWorkItem</strong> to add the work item to a system queue.</p></td>
</tr>
</tbody>
</table>

 

### <span id="annotating_driver_dispatch_routines"></span><span id="ANNOTATING_DRIVER_DISPATCH_ROUTINES"></span>Declaring Driver Dispatch Routines

Starting in Windows 10 Version 2004, the function role type declarations for dispatch routines are refined with their IRP category automatically based on the initialization of the DriverObject->MajorFunction table in the DriverEntry routine of a WDM driver.  

A driver Foo must accomplish role declarations by using either the basic or advanced style of declaration in order to be compliant with SDV.  

#### Basic and Advanced Initializations

The basic style can be seen in the example below (note the dispatch routine names FooCreate and FooCleanup are just examples, any appropriate name can be used):

```
DriverObject->MajorFunction[IRP_MJ_CREATE] = FooCreate; //Basic style
DriverObject->MajorFunction[IRP_MJ_CLEANUP] = FooCleanup;
```

A more advanced approach can be taken to shorten the list required.  While the same dispatch routine is used for more than one IRP category, a driver may encode two initializations this way:

```
DriverObject->MajorFunction[IRP_MJ_CREATE] = 
DriverObject->MajorFunction[IRP_MJ_CLEANUP] = FooCreateCleanup; // Advanced style for a multi-role dispatch routine 
```

In order for a driver to be able to run SDV properly, **the driver must only use either the *basic* or *advanced* style shown above**.  SDV verficiation on the driver **will not work as expected** if one of these two methods is not used.

### <span id="function_parameters_and_function_role_types"></span><span id="FUNCTION_PARAMETERS_AND_FUNCTION_ROLE_TYPES"></span>Function Parameters and Function Role Types

As required in the C programming language, the parameter types that you use in the function definition must match the parameter types of the function prototype, or in this case, the function role type. SDV depends upon the function signatures for analysis and ignores functions whose signatures do not match.

For example, you should declare an [**IoCompletion**](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine using the IO\_COMPLETION\_ROUTINE function role type:

```
IO_COMPLETION_ROUTINE myCompletionRoutine;
```

When you implement *myCompletionRoutine*, the parameter types must match those used by IO\_COMPLETION\_ROUTINE, namely, PDEVICE\_OBJECT, PIRP, and PVOID (see [**IoCompletion**](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for syntax).

```
NTSTATUS
myCompletionRoutine(
 PDEVICE_OBJECT  DeviceObject,
 PIRP  Irp,
 PVOID  Context
 )
{
}
```

## <span id="running_code_analysis_for_drivers_to_verify_the_function_declarations"></span><span id="RUNNING_CODE_ANALYSIS_FOR_DRIVERS_TO_VERIFY_THE_FUNCTION_DECLARATIONS"></span> Running Code Analysis for Drivers to verify the function declarations


To help you determine whether the source code is prepared, run [Code Analysis for Drivers](code-analysis-for-drivers.md). Code Analysis for Drivers checks for function role type declarations and can help identify function declarations that might have been missed or warn you when the parameters of the function definition do not match those in the function role type.
