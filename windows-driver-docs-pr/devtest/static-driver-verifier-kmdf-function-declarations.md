---
title: Static Driver Verifier KMDF Function Declarations
description: Static Driver Verifier KMDF Function Declarations
ms.assetid: 1623f3a4-e318-41b3-bbcf-d443202f31e6
---

# Static Driver Verifier KMDF Function Declarations


To enable SDV to verify your KMDF driver, you must declare each callback function, using a callback function role type. The callback function role types are defined in the various WDF header files and are included when you build your driver with the Wdf.h header file. The following table shows the function role types and the event callback functions that they are associated with.

You must declare the driver's callback functions before the callback function definitions. The following example shows the function role type declaration for the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. In this example, the callback function is called *EvtDriverDeviceAdd*.

```
#include <NTDDK.h>  
#include <wdf.h>
EVT_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd
```

If a callback function has a function prototype declaration, you must replace the function prototype with the function role type declaration. For more information about the function role type declarations, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

The following table shows the callback function types and the event callback functions that they are associated with.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function role type</th>
<th align="left">Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP</p></td>
<td align="left"><p>[<em>EvtChildListAddressDescriptionCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff540823)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY</p></td>
<td align="left"><p>[<em>EvtChildListAddressDescriptionCopy</em>](https://msdn.microsoft.com/library/windows/hardware/ff540824)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_DUPLICATE</p></td>
<td align="left"><p>[<em>EvtChildListIdentificationDescriptionDuplicate</em>](https://msdn.microsoft.com/library/windows/hardware/ff540836)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_CHILD_LIST_CREATE_DEVICE</p></td>
<td align="left"><p>[<em>EvtChildListCreateDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff540828)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</p></td>
<td align="left"><p>[<em>EvtChildListDeviceReenumerated</em>](https://msdn.microsoft.com/library/windows/hardware/ff540830)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_CLEANUP</p></td>
<td align="left"><p>[<em>EvtChildListIdentificationDescriptionCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff540832)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COMPARE</p></td>
<td align="left"><p>[<em>EvtChildListIdentificationDescriptionCompare</em>](https://msdn.microsoft.com/library/windows/hardware/ff540833)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COPY</p></td>
<td align="left"><p>[<em>EvtChildListIdentificationDescriptionCopy</em>](https://msdn.microsoft.com/library/windows/hardware/ff540834)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE</p></td>
<td align="left"><p>[<em>EvtChildListIdentificationDescriptionDuplicate</em>](https://msdn.microsoft.com/library/windows/hardware/ff540836)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_CHILD_LIST_SCAN_FOR_CHILDREN</p></td>
<td align="left"><p>[<em>EvtChildListScanForChildren</em>](https://msdn.microsoft.com/library/windows/hardware/ff540838)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_ARM_WAKE_FROM_S0</p></td>
<td align="left"><p>[<em>EvtDeviceArmWakeFromS0</em>](https://msdn.microsoft.com/library/windows/hardware/ff540843)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_ARM_WAKE_FROM_SX</p></td>
<td align="left"><p>[<em>EvtDeviceArmWakeFromSx</em>](https://msdn.microsoft.com/library/windows/hardware/ff540844)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_CONTEXT_CLEANUP</p></td>
<td align="left"><p>[<em>EvtCleanupCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540840)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_CONTEXT_DESTROY</p></td>
<td align="left"><p>[<em>EvtDestroyCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540841)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_D0_ENTRY</p></td>
<td align="left"><p>[<em>EvtDeviceD0Entry</em>](https://msdn.microsoft.com/library/windows/hardware/ff540848)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_D0_ENTRY_POST_INTERRUPTS_ENABLED</p></td>
<td align="left"><p>[<em>EvtDeviceD0EntryPostInterruptsEnabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540853)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_D0_EXIT</p></td>
<td align="left"><p>[<em>EvtDeviceD0Exit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540855)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_D0_EXIT_PRE_INTERRUPTS_DISABLED</p></td>
<td align="left"><p>[<em>EvtDeviceD0ExitPreInterruptsDisabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540856)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_DISABLE_WAKE_AT_BUS</p></td>
<td align="left"><p>[<em>EvtDeviceDisableWakeAtBus</em>](https://msdn.microsoft.com/library/windows/hardware/ff540858)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_DISARM_WAKE_FROM_S0</p></td>
<td align="left"><p>[<em>EvtDeviceDisarmWakeFromS0</em>](https://msdn.microsoft.com/library/windows/hardware/ff540860)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_DISARM_WAKE_FROM_SX</p></td>
<td align="left"><p>[<em>EvtDeviceDisarmWakeFromSx</em>](https://msdn.microsoft.com/library/windows/hardware/ff540862)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_EJECT</p></td>
<td align="left"><p>[<em>EvtDeviceEject</em>](https://msdn.microsoft.com/library/windows/hardware/ff540863)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</p></td>
<td align="left"><p>[<em>EvtDeviceEnableWakeAtBus</em>](https://msdn.microsoft.com/library/windows/hardware/ff540866)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_FILE_CREATE</p></td>
<td align="left"><p>[<em>EvtDeviceFileCreate</em>](https://msdn.microsoft.com/library/windows/hardware/ff540868)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_FILTER_RESOURCE_REQUIREMENTS</p></td>
<td align="left"><p>[<em>EvtDeviceFilterAddResourceRequirements</em>](https://msdn.microsoft.com/library/windows/hardware/ff540870)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</p></td>
<td align="left"><p>[<em>EvtDevicePnpStateChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff540874)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_POWER_POLICY_STATE_CHANGE_NOTIFICATION</p></td>
<td align="left"><p>[<em>EvtDevicePnpStateChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff540874)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_POWER_STATE_CHANGE_NOTIFICATION</p></td>
<td align="left"><p>[<em>EvtDevicePowerStateChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff540878)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_PREPARE_HARDWARE</p></td>
<td align="left"><p>[<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_PROCESS_QUERY_INTERFACE_REQUEST</p></td>
<td align="left"><p>[<em>EvtDeviceProcessQueryInterfaceRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff540882)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_QUERY_REMOVE</p></td>
<td align="left"><p>[<em>EvtDeviceQueryRemove</em>](https://msdn.microsoft.com/library/windows/hardware/ff540883)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_QUERY_STOP</p></td>
<td align="left"><p>[<em>EvtDeviceQueryStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff540885)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_RELATIONS_QUERY</p></td>
<td align="left"><p>[<em>EvtDeviceRelationsQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540886)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_RELEASE_HARDWARE</p></td>
<td align="left"><p>[<em>EvtDeviceReleaseHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540890)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES</p></td>
<td align="left"><p>[<em>EvtDeviceRemoveAddedResources</em>](https://msdn.microsoft.com/library/windows/hardware/ff540892)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_RESOURCE_REQUIREMENTS_QUERY</p></td>
<td align="left"><p>[<em>EvtDeviceResourceRequirementsQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540894)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_RESOURCES_QUERY</p></td>
<td align="left"><p>[<em>EvtDeviceResourcesQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540895)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_SELF_MANAGED_IO_CLEANUP</p></td>
<td align="left"><p>[<em>EvtDeviceSelfManagedIoCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff540898)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_SELF_MANAGED_IO_FLUSH</p></td>
<td align="left"><p>[<em>EvtDeviceSelfManagedIoFlush</em>](https://msdn.microsoft.com/library/windows/hardware/ff540901)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_SELF_MANAGED_IO_INIT</p></td>
<td align="left"><p>[<em>EvtDeviceSelfManagedIoInit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540902)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_SELF_MANAGED_IO_RESTART</p></td>
<td align="left"><p>[<em>EvtDeviceSelfManagedIoRestart</em>](https://msdn.microsoft.com/library/windows/hardware/ff540905)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_SELF_MANAGED_IO_SUSPEND</p></td>
<td align="left"><p>[<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_SET_LOCK</p></td>
<td align="left"><p>[<em>EvtDeviceSetLock</em>](https://msdn.microsoft.com/library/windows/hardware/ff540909)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_SHUTDOWN_NOTIFICATION</p></td>
<td align="left"><p>[<em>EvtDeviceShutdownNotification</em>](https://msdn.microsoft.com/library/windows/hardware/ff540911)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_SURPRISE_REMOVAL</p></td>
<td align="left"><p>[<em>EvtDeviceSurpriseRemoval</em>](https://msdn.microsoft.com/library/windows/hardware/ff540913)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_USAGE_NOTIFICATION</p></td>
<td align="left"><p>[<em>EvtDeviceUsageNotification</em>](https://msdn.microsoft.com/library/windows/hardware/ff540915)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DEVICE_WAKE_FROM_S0_TRIGGERED</p></td>
<td align="left"><p>[<em>EvtDeviceWakeFromS0Triggered</em>](https://msdn.microsoft.com/library/windows/hardware/ff540919)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DEVICE_WAKE_FROM_SX_TRIGGERED</p></td>
<td align="left"><p>[<em>EvtDeviceWakeFromSxTriggered</em>](https://msdn.microsoft.com/library/windows/hardware/ff540923)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DMA_ENABLER_DISABLE</p></td>
<td align="left"><p>[<em>EvtDmaEnablerDisable</em>](https://msdn.microsoft.com/library/windows/hardware/ff540927)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DMA_ENABLER_ENABLE</p></td>
<td align="left"><p>[<em>EvtDmaEnablerEnable</em>](https://msdn.microsoft.com/library/windows/hardware/ff540929)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DMA_ENABLER_FILL</p></td>
<td align="left"><p>[<em>EvtDmaEnablerFill</em>](https://msdn.microsoft.com/library/windows/hardware/ff540932)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DMA_ENABLER_FLUSH</p></td>
<td align="left"><p>[<em>EvtDmaEnablerFlush</em>](https://msdn.microsoft.com/library/windows/hardware/ff541655)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DMA_ENABLER_SELFMANAGED_IO_START</p></td>
<td align="left"><p>[<em>EvtDmaEnablerSelfManagedIoStart</em>](https://msdn.microsoft.com/library/windows/hardware/ff541663)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DMA_ENABLER_SELFMANAGED_IO_STOP</p></td>
<td align="left"><p>[<em>EvtDmaEnablerSelfManagedIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541677)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DPC</p></td>
<td align="left"><p>[<em>EvtDpcFunc</em>](https://msdn.microsoft.com/library/windows/hardware/ff541683)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_DRIVER_DEVICE_ADD</p></td>
<td align="left"><p>[<em>EvtDriverDeviceAdd</em>](https://msdn.microsoft.com/library/windows/hardware/ff541693)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_DRIVER_UNLOAD</p></td>
<td align="left"><p>[<em>EvtDriverUnload</em>](https://msdn.microsoft.com/library/windows/hardware/ff541694)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_FILE_CLEANUP</p></td>
<td align="left"><p>[<em>EvtFileCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff541700)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_FILE_CLOSE</p></td>
<td align="left"><p>[<em>EvtFileClose</em>](https://msdn.microsoft.com/library/windows/hardware/ff541702)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_FILE_CONTEXT_CLEANUP_CALLBACK</p></td>
<td align="left"><p>[<em>EvtCleanupCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540840)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_FILE_CONTEXT_DESTROY_CALLBACK</p></td>
<td align="left"><p>[<em>EvtDestroyCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540841)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_INTERRUPT_DISABLE</p></td>
<td align="left"><p>[<em>EvtInterruptDisable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541714)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_INTERRUPT_DPC</p></td>
<td align="left"><p>[<em>EvtInterruptDpc</em>](https://msdn.microsoft.com/library/windows/hardware/ff541721)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_INTERRUPT_ENABLE</p></td>
<td align="left"><p>[<em>EvtInterruptEnable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541730)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_INTERRUPT_ISR</p></td>
<td align="left"><p>[<em>EvtInterruptIsr</em>](https://msdn.microsoft.com/library/windows/hardware/ff541735)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_INTERRUPT_SYNCHRONIZE</p></td>
<td align="left"><p>[<em>EvtInterruptSynchronize</em>](https://msdn.microsoft.com/library/windows/hardware/ff541742)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_IN_CALLER_CONTEXT</p></td>
<td align="left"><p>[<em>EvtIoInCallerContext</em>](https://msdn.microsoft.com/library/windows/hardware/ff541764)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_CONTEXT_CLEANUP_CALLBACK</p></td>
<td align="left"><p>[<em>EvtCleanupCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540840)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_CONTEXT_DESTROY_CALLBACK</p></td>
<td align="left"><p>[<em>EvtDestroyCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540841)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_CANCELED_ON_QUEUE</p></td>
<td align="left"><p>[<em>EvtIoCanceledOnQueue</em>](https://msdn.microsoft.com/library/windows/hardware/ff541756)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_DEFAULT</p></td>
<td align="left"><p>[<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_DEVICE_CONTROL</p></td>
<td align="left"><p>[<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL</p></td>
<td align="left"><p>[<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_READ</p></td>
<td align="left"><p>[<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_RESUME</p></td>
<td align="left"><p>[<em>EvtIoResume</em>](https://msdn.microsoft.com/library/windows/hardware/ff541779)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_STOP</p></td>
<td align="left"><p>[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_WRITE</p></td>
<td align="left"><p>[<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_STATE</p></td>
<td align="left"><p>[<em>EvtIoQueueState</em>](https://msdn.microsoft.com/library/windows/hardware/ff541771)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_TARGET_QUERY_REMOVE</p></td>
<td align="left"><p>[<em>EvtIoTargetQueryRemove</em>](https://msdn.microsoft.com/library/windows/hardware/ff541793)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_TARGET_REMOVE_CANCELED</p></td>
<td align="left"><p>[<em>EvtIoTargetRemoveCanceled</em>](https://msdn.microsoft.com/library/windows/hardware/ff541800)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_TARGET_REMOVE_COMPLETE</p></td>
<td align="left"><p>[<em>EvtIoTargetRemoveComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff541806)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_OBJECT_CONTEXT_CLEANUP</p></td>
<td align="left"><p>[<em>EvtCleanupCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540840)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_OBJECT_CONTEXT_DESTROY</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_PROGRAM_DMA</p></td>
<td align="left"><p>[<em>EvtProgramDma</em>](https://msdn.microsoft.com/library/windows/hardware/ff541816)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_REQUEST_CANCEL</p></td>
<td align="left"><p>[<em>EvtRequestCancel</em>](https://msdn.microsoft.com/library/windows/hardware/ff541817)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_REQUEST_COMPLETION_ROUTINE</p></td>
<td align="left"><p>[<em>CompletionRoutine</em>](https://msdn.microsoft.com/library/windows/hardware/ff540745)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_TIMER</p></td>
<td align="left"><p>[<em>EvtTimerFunc</em>](https://msdn.microsoft.com/library/windows/hardware/ff541823)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_TRACE_CALLBACK</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_EXECUTE_METHOD</p></td>
<td align="left"><p>[<em>EvtWmiInstanceExecuteMethod</em>](https://msdn.microsoft.com/library/windows/hardware/ff541836)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_QUERY_INSTANCE</p></td>
<td align="left"><p>[<em>EvtWmiInstanceQueryInstance</em>](https://msdn.microsoft.com/library/windows/hardware/ff541843)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_SET_INSTANCE</p></td>
<td align="left"><p>[<em>EvtWmiInstanceSetInstance</em>](https://msdn.microsoft.com/library/windows/hardware/ff541847)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_SET_ITEM</p></td>
<td align="left"><p>[<em>EvtWmiInstanceSetItem</em>](https://msdn.microsoft.com/library/windows/hardware/ff541852)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_WMI_PROVIDER_FUNCTION_CONTROL</p></td>
<td align="left"><p>[<em>EvtWmiProviderFunctionControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541855)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_WORKITEM</p></td>
<td align="left"><p>[<em>EvtWorkItem</em>](https://msdn.microsoft.com/library/windows/hardware/ff541859)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDFDEVICE_WDM_IRP_PREPROCESS</p></td>
<td align="left"><p>[<em>EvtDeviceWdmIrpPreprocess</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</p></td>
</tr>
</tbody>
</table>

 

### <span id="function_role_types_that_allow_multiple_callback_functions"></span><span id="FUNCTION_ROLE_TYPES_THAT_ALLOW_MULTIPLE_CALLBACK_FUNCTIONS"></span>Function role types that allow multiple callback functions

There are some function role types that can have multiple event callback functions associated with them. For example, a driver might have multiple [*EvtTimerFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541823) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions. The following table show the maximum number of callbacks that SDV supports for each function role type. While it is not incorrect for a driver to have more than the maximum number of callback functions listed in the table, it does complicate the verification process when using SDV. For information about changes you might need to make to the Sdv-map.h file to accommodate the additional callback functions, see [Duplicate entry points for a function role type](duplicate-entry-points-for-a-function-role-type.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function role type</th>
<th align="left">Maximum number of callback functions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>EVT_WDF_DPC</p></td>
<td align="left"><p>7</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_INTERRUPT_SYNCHRONIZE</p></td>
<td align="left"><p>11</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_TIMER</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_EXECUTE_METHOD</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_QUERY_INSTANCE</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_SET_INSTANCE</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_WMI_INSTANCE_SET_ITEM</p></td>
<td align="left"><p>5</p></td>
</tr>
</tbody>
</table>

 

### <span id="function_role_types_and_i_o_queues"></span><span id="FUNCTION_ROLE_TYPES_AND_I_O_QUEUES"></span>Function role types and I/O queues

Use the following function role types when you declare the [Request Handlers](http://go.microsoft.com/fwlink/p/?linkid=153345) and callback functions that rely on the KMDF framework to deliver the I/O requests to the driver (for sequential or parallel dispatching). Do not use these function role types for the functions that manually forward requests from the default queue to other queues (manual dispatching). SDV does not support a memory model that allows it to track requests from one queue to another.

For more information about I/O queues, see [Creating I/O Queues](http://go.microsoft.com/fwlink/p/?linkid=153346).

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function role types used for I/O queue configured for manual dispatching</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_CONTEXT_CLEANUP_CALLBACK</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_CONTEXT_DESTROY_CALLBACK</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_CANCELED_ON_QUEUE</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_DEFAULT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_DEVICE_CONTROL</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_READ</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_RESUME</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_STOP</p></td>
</tr>
<tr class="even">
<td align="left"><p>EVT_WDF_IO_QUEUE_IO_WRITE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EVT_WDF_IO_QUEUE_STATE</p></td>
</tr>
</tbody>
</table>

 

### <span id="function_role_types_for_the_evtcleanupcallback_and_evtdestroycallback_"></span><span id="FUNCTION_ROLE_TYPES_FOR_THE_EVTCLEANUPCALLBACK_AND_EVTDESTROYCALLBACK_"></span>Function role types for the EvtCleanupCallback and EvtDestroyCallback functions

You must declare the [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) and [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) function with object-specific, function role types. SDV requires these object-specific role types to determine whether the driver is properly using the callback function. Use the following tables to determine which function type to use.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object type</th>
<th align="left">Function role type for EvtCleanupCallback</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Device object</p></td>
<td align="left"><p>EVT_WDF_DEVICE_CONTEXT_CLEANUP</p></td>
</tr>
<tr class="even">
<td align="left"><p>I/O queue object</p></td>
<td align="left"><p>EVT_WDF_IO_QUEUE_CONTEXT_CLEANUP_CALLBACK</p></td>
</tr>
<tr class="odd">
<td align="left"><p>File object</p></td>
<td align="left"><p>EVT_WDF_FILE_CONTEXT_CLEANUP_CALLBACK</p></td>
</tr>
<tr class="even">
<td align="left"><p>All other objects</p></td>
<td align="left"><p>EVT_WDF_OBJECT_CONTEXT_CLEANUP</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object type</th>
<th align="left">Function role type for EvDestroyCallback</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Device object</p></td>
<td align="left"><p>EVT_WDF_DEVICE_CONTEXT_DESTROY</p></td>
</tr>
<tr class="even">
<td align="left"><p>I/O queue object</p></td>
<td align="left"><p>EVT_WDF_IO_QUEUE_CONTEXT_DESTROY_CALLBACK</p></td>
</tr>
<tr class="odd">
<td align="left"><p>File object</p></td>
<td align="left"><p>EVT_WDF_FILE_CONTEXT_DESTROY_CALLBACK</p></td>
</tr>
<tr class="even">
<td align="left"><p>All other objects</p></td>
<td align="left"><p>EVT_WDF_OBJECT_CONTEXT_DESTROY</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20Driver%20Verifier%20KMDF%20Function%20Declarations%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




