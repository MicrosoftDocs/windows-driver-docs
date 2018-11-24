---
title: Declaring Functions Using Function Role Types for WDM Drivers
description: Declaring Functions Using Function Role Types for WDM Drivers
ms.assetid: 3260b53e-82be-4dbc-8ac5-d0e52de77f9d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Declaring Functions Using Function Role Types for WDM Drivers


To inform SDV about the driver's entry points when you analyze a WDM driver, you must declare functions using function role type declarations. The function role types are defined in Wdm.h. Each entry point in the *DriverEntry* routine in your WDM driver must be declared by specifying the corresponding role type. The role types are predefined typedefs that correspond to the recognized entry points in a WDM driver.

For example, to create a function role type declaration for a driver's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine called *CsampUnload*, use the predefined typedef DRIVER\_UNLOAD role type declaration. The function role type declaration must appear before the function definition.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544113" data-raw-source="[&lt;em&gt;DriverEntry&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544113)"><em>DriverEntry</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>DRIVER_STARTIO</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563858" data-raw-source="[&lt;em&gt;StartIO&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563858)"><em>StartIO</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>DRIVER_UNLOAD</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564886" data-raw-source="[&lt;em&gt;Unload&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564886)"><em>Unload</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>DRIVER_ADD_DEVICE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540521" data-raw-source="[&lt;em&gt;AddDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540521)"><em>AddDevice</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<strong><em>Dispatch_type</em>(</strong> <em>type</em> <strong>)</strong>
DRIVER_DISPATCH</td>
<td align="left"><p>The dispatch routine(s) used by the driver. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566407" data-raw-source="[Writing Dispatch Routines](https://msdn.microsoft.com/library/windows/hardware/ff566407)">Writing Dispatch Routines</a>. The <strong><em>Dispatch_type</em>(</strong><em>type</em><strong>)</strong> annotation must be combined with the DRIVER_DISPATCH role type declaration to specify the driver entry points.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IO_COMPLETION_ROUTINE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548354" data-raw-source="[&lt;em&gt;IoCompletion&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548354)"><em>IoCompletion</em></a></p>
<p>The <em>IoCompletion</em> routine is set by calling <em>IoSetCompletionRoutine</em> or <em>IoSetCompletionRoutineEx</em> and passing the function pointer to the <em>IoCompletion</em> routine as the second parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DRIVER_CANCEL</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540742" data-raw-source="[&lt;em&gt;Cancel&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540742)"><em>Cancel</em></a></p>
<p>The <strong>Cancel</strong> routine is set by calling <strong>IoSetCancelRoutine</strong> and passing the function pointer to the cancellation routine for the IRP as the second parameter to the function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IO_DPC_ROUTINE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544079" data-raw-source="[&lt;em&gt;DpcForIsr&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544079)"><em>DpcForIsr</em></a></p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff544079" data-raw-source="[&lt;em&gt;DpcForIsr&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544079)"><em>DpcForIsr</em></a> routine is registered by calling <em>IoInitializeDpcRequest</em> and passing the function pointer to the <em>DpcForIsr</em> routine as the second parameter. To queue the DPC, call <em>IoQueueDpc</em> from the ISR routine by using the same DPC object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KDEFERRED_ROUTINE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542972" data-raw-source="[&lt;em&gt;CustomDpc&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542972)"><em>CustomDpc</em></a></p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff542972" data-raw-source="[&lt;em&gt;CustomDpc&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542972)"><em>CustomDpc</em></a> routine is set by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552130" data-raw-source="[&lt;strong&gt;KeInitializeDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552130)"><strong>KeInitializeDpc</strong></a> and passing the function pointer to the <em>CustomDpc</em> as the second parameter. To queue the <em>CustomDpc</em> for the driver, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff552185" data-raw-source="[&lt;strong&gt;KeInsertQueueDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552185)"><strong>KeInsertQueueDpc</strong></a> from the ISR routine by using the same DPC object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSERVICE_ROUTINE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547958" data-raw-source="[&lt;em&gt;InterruptService&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547958)"><em>InterruptService</em></a></p>
<p>The InterruptService routine (ISR) services a device interrupt and schedules post-interrupt processing of received data, if necessary.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>REQUEST_POWER_COMPLETE</p></td>
<td align="left"><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff961906" data-raw-source="[&lt;em&gt;PowerCompletion&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff961906)"><em>PowerCompletion</em></a> callback routine completes the processing of a power IRP. If the driver needs to perform additional tasks after all other drivers have completed the IRP, the driver registers a <em>PowerCompletion</em> callback routine during the call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559734" data-raw-source="[&lt;strong&gt;PoRequestPowerIrp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559734)"><strong>PoRequestPowerIrp</strong></a> routine that allocates the IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>WORKER_THREAD_ROUTINE</p></td>
<td align="left"><p><em>Routine</em></p>
<p><em>Routine</em> is the callback routine that is specified in the second parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545327" data-raw-source="[&lt;strong&gt;ExInitializeWorkItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545327)"><strong>ExInitializeWorkItem</strong></a> function.</p>
<p>The <em>Routine</em> should only be declared this way if the driver calls <strong>ExQueueWorkItem</strong> to add the work item to a system queue.</p></td>
</tr>
</tbody>
</table>

 

### <span id="annotating_driver_dispatch_routines"></span><span id="ANNOTATING_DRIVER_DISPATCH_ROUTINES"></span>Declaring Driver Dispatch Routines

The function role type declarations for dispatch routines require additional information. Use the annotation **\_Dispatch\_type\_(**<em>type</em>**)** in the declarations for dispatch routines that serve major IRP function codes. The *type* is the major I/O function code (for example, IRP\_MJ\_CREATE, IRP\_MJ\_CLOSE, IRP\_MJ\_SYSTEM\_CONTROL).

For an example of how to declare driver dispatch routines, see the source code for the Cancel sample driver (Cancel.sys). In the header file for the driver (Cancel.h) there is a function role type declaration for *CsampCleanup*, a driver dispatch routine that handles the IRP\_MJ\_CLEANUP I/O function code. The **\_Dispatch\_type\_ (**<em>type</em>**)** annotation precedes the DRIVER\_DISPATCH role type declaration.

The *CsampCleanup* routine is declared as follows:

```
_Dispatch_type_(IRP_MJ_CLEANUP)
DRIVER_DISPATCH CsampCleanup;
```

The Cancel sample driver also has a driver dispatch routine, *CsampCreateClose*, that handles both IRP\_MJ\_CREATE and IRP\_MJ\_CLOSE I/O function codes. The *CsampCreateClose* routine is declared in Cancel.h. Because this routine handles two I/O function codes, it requires two **\_Dispatch\_type\_** annotations in addition to the DRIVER\_DISPATCH role type declaration.

```
_Dispatch_type_(IRP_MJ_CREATE)
_Dispatch_type_(IRP_MJ_CLOSE)
DRIVER_DISPATCH CsampCreateClose;
```

Suppose that a filter driver has a driver dispatch routine called *FilterDispatchIo* that handles the IRP\_MJ\_CREATE, IRP\_MJ\_CLOSE, IRP\_MJ\_CLEANUP, and IRP\_MJ\_DEVICE\_CONTROL I/O function codes.

The *FilterDispatchIo* routine is declared in Filter.h as follows.

```
_Dispatch_type_(IRP_MJ_CREATE)
_Dispatch_type_(IRP_MJ_CLOSE)
_Dispatch_type_(IRP_MJ_CLEANUP)
_Dispatch_type_(IRP_MJ_DEVICE_CONTROL)
DRIVER_DISPATCH FilterDispatchIo;
```

### <span id="quick_steps__how_to_annotate_a_wdm_driver"></span><span id="QUICK_STEPS__HOW_TO_ANNOTATE_A_WDM_DRIVER"></span>Quick Steps: How to Annotate a WDM Driver

The procedure for declaring functions using the function role types is as follows:

1.  Locate the source code for the *DriverEntry* routine.

2.  Ensure that routines that are assigned to the following pointers are declared using function role types.

    ```
    DriverObject->DriverStartIo
    DriverObject->Unload
    DriverObject->DriverExtension->AddDevice 
    ```

    For example, the following code example shows the function role type declarations for routines that correspond to these pointers (*myDriverStartIO*, *myUnload*, and *myAddDevice*).

    ```
    DRIVER_STARTIO myDriverStartIo;
    DRIVER_UNLOAD myUnload;
    DRIVER_ADD_DEVICE myAddDevice 
    ```

3.  Ensure that routines that are assigned to the following pointers are declared using the DRIVER\_DISPATCH role type and that they have the **\_Dispatch\_type\_** annotations.

    ```
    DriverObject->MajorFunction[IRP_MJ_xxx]
    ```

    For example:

    ```
    _Dispatch_type_(IRP_MJ_CLEANUP)
    DRIVER_DISPATCH CsampCleanup;
    ```

### <span id="function_parameters_and_function_role_types"></span><span id="FUNCTION_PARAMETERS_AND_FUNCTION_ROLE_TYPES"></span>Function Parameters and Function Role Types

As required in the C programming language, the parameter types that you use in the function definition must match the parameter types of the function prototype, or in this case, the function role type. SDV depends upon the function signatures for analysis and ignores functions whose signatures do not match.

For example, you should declare an [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine using the IO\_COMPLETION\_ROUTINE function role type:

```
IO_COMPLETION_ROUTINE myCompletionRoutine;
```

When you implement *myCompletionRoutine*, the parameter types must match those used by IO\_COMPLETION\_ROUTINE, namely, PDEVICE\_OBJECT, PIRP, and PVOID (see [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for syntax).

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

 

 





