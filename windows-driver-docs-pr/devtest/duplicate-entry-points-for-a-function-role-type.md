---
title: Duplicate Entry Points for a Function Role Type
description: Duplicate Entry Points for a Function Role Type
ms.assetid: cf6604da-bd79-4adf-a08f-9b903aa91133
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Duplicate Entry Points for a Function Role Type


For most function role types, SDV assumes that the driver has, at most, one callback function for each entry point. However, there are some function role types that can have multiple event callback functions associated with them. For example, a KMDF driver might have multiple [*EvtTimerFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541823) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions (that use the EVT\_WDF\_TIMER and EVT\_WDF\_DPC role type annotations). In this case, SDV appends an integer to the function type in Sdv-map.h. For example, if your driver has two DPC callback functions, SDV maps them to **fun\_WDF\_DPC\_1** and **fun\_WDF\_DPC\_2**.

If a driver exceeds the maximum number of callback functions for a role type, SDV displays the following message.

```
Static Driver Verifier found more than one entry point for '[role type]'
```

If a function role type has more entry points than SDV supports, there is not necessarily something wrong with the driver. However, to obtain accurate verification results, you must edit the Sdv.-map.h file to remove the duplicate entries.

For example, the following Sdv-map.h file shows that there are two [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) functions that were annotated using the EVT\_WDF\_REQUEST\_COMPLETION\_ROUTINE role type. In the Sdv-map.h file, SDV defines both **EvtRequestReadCompletionRoutine** and **EvtRequestWriteCompletionRoutine** as fun\_WDF\_REQUEST\_COMPLETION\_ROUTINE.

```
//Approved=false
#define fun_WDF_DRIVER_DEVICE_ADD OsrFxEvtDeviceAdd
#define fun_WDF_IO_QUEUE_IO_READ OsrFxEvtIoRead
#define fun_WDF_IO_QUEUE_IO_STOP OsrFxEvtIoStop
#define fun_WDF_DEVICE_D0_EXIT OsrFxEvtDeviceD0Exit
#define fun_WDF_REQUEST_COMPLETION_ROUTINE EvtRequestReadCompletionRoutine
#define fun_WDF_REQUEST_COMPLETION_ROUTINE EvtRequestWriteCompletionRoutine
#define fun_WDF_OBJECT_CONTEXT_CLEANUP OsrFxEvtDriverContextCleanup
#define fun_WDF_DEVICE_D0_ENTRY OsrFxEvtDeviceD0Entry
#define fun_WDF_DEVICE_PREPARE_HARDWARE OsrFxEvtDevicePrepareHardware
#define fun_WDF_IO_QUEUE_IO_WRITE OsrFxEvtIoWrite
#define fun_WDF_IO_QUEUE_IO_DEVICE_CONTROL OsrFxEvtIoDeviceControl
```

To remove the duplication, comment out the second completion routine (replace the **\#d** in \#define with two comment delimiters (**//**). Then set **Approved=true** and run a verification.

```
#define fun_WDF_REQUEST_COMPLETION_ROUTINE EvtRequestReadCompletionRoutine
//efine fun_WDF_REQUEST_COMPLETION_ROUTINE EvtRequestWriteCompletionRoutine
```

After you have viewed the results of the verification with the one completion routine, edit the Sdv-map.h file again, but this time comment out the completion routine that was just verified and remove the comment (replace the **//** with **\#d**) from the completion routine that was not verified. Then run SDV again.

### <span id="function_role_types_that_support_multiple_entry_points"></span><span id="FUNCTION_ROLE_TYPES_THAT_SUPPORT_MULTIPLE_ENTRY_POINTS"></span>Function role types that support multiple entry points

Some function role types support multiple entries. When the number of entries exceeds the supported maximum, SDV also reports these as duplicate entries. You can treat these additional entries the same way you handle duplicate entries, by selectively commenting out the **\#define** statements for the callback routines in the Sdv-map.h file and making separate verifications. For example, if your driver has eight DPC callback functions (that use the EVT\_WDF\_DPC role type), you could do the following:

-   Edit Sdv-map.h and comment out the define statements for fun\_WDF\_DPC\_5 through fun\_WDF\_DPC\_8.

-   Run SDV on the driver.

-   Then edit Sdv-map.h again to define fun\_WDF\_DPC\_5 through fun\_WDF\_DPC\_8 and comment out the define statements for fun\_WDF\_DPC\_1 through fun\_WDF\_DPC\_4.

-   Run SDV on the driver.

See [Static Driver Verifier KMDF Annotations](static-driver-verifier-kmdf-function-declarations.md) for a list of function role types that can have more than one callback function. The list shows the maximum number of callback functions that SDV supports for those role types.

 

 





