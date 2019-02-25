---
title: TDR changes in Windows 8
description: Starting with Windows 8, GPU timeout detection and recovery (TDR) behavior has changed to allow parts of individual physical adapters to be reset, instead of requiring an adapter-wide reset.
ms.assetid: 5BC4F94C-2B45-44E2-8BBF-B455BB864A29
keywords:
- TDR (timeout detection and recovery) WDK display , changes in Windows 8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TDR changes in Windows 8


Starting with Windows 8, GPU timeout detection and recovery (TDR) behavior has changed to allow parts of individual physical adapters to be reset, instead of requiring an adapter-wide reset.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Minimum Windows Display Driver Model (WDDM) version</td>
<td align="left">1.2</td>
</tr>
<tr class="even">
<td align="left">Minimum Windows version</td>
<td align="left">8</td>
</tr>
<tr class="odd">
<td align="left">Driver implementation—Full graphics and Render only</td>
<td align="left">Mandatory</td>
</tr>
<tr class="even">
<td align="left"><a href="https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit" data-raw-source="[WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit)">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>Device.Graphics…TDRResiliency</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="TDR_device_driver_interface__DDI_"></span><span id="tdr_device_driver_interface__ddi_"></span><span id="TDR_DEVICE_DRIVER_INTERFACE__DDI_"></span>TDR device driver interface (DDI)


To accommodate this behavior change, display miniport drivers should implement these functions:

-   [*DxgkDdiQueryDependentEngineGroup*](https://msdn.microsoft.com/library/windows/hardware/hh451407)
-   [*DxgkDdiQueryEngineStatus*](https://msdn.microsoft.com/library/windows/hardware/hh451411)
-   [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418)

**Note**  A driver that supports these functions must also support level zero synchronization for the [*DxgkDdiCollectDbgInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559595) function. This is to ensure that level zero miniport calls not affected be the reset operation can continue. See Remarks of *DxgkDdiCollectDbgInfo*.

 

These structures are associated with the new functions:

-   [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062) (new **SupportPerEngineTDR** member)
-   [**DXGK\_ENGINESTATUS**](https://msdn.microsoft.com/library/windows/hardware/hh464023)
-   [**DXGKARG\_QUERYDEPENDENTENGINEGROUP**](https://msdn.microsoft.com/library/windows/hardware/hh451294)
-   [**DXGKARG\_QUERYENGINESTATUS**](https://msdn.microsoft.com/library/windows/hardware/hh451299)
-   [**DXGKARG\_RESETENGINE**](https://msdn.microsoft.com/library/windows/hardware/hh451303)

A display miniport driver indicates support for these functions by setting the [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**SupportPerEngineTDR** member, in which case it must implement the [*DxgkDdiQueryDependentEngineGroup*](https://msdn.microsoft.com/library/windows/hardware/hh451407), [*DxgkDdiQueryEngineStatus*](https://msdn.microsoft.com/library/windows/hardware/hh451411), and [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418) functions.

## <span id="TDR_process_description"></span><span id="tdr_process_description"></span><span id="TDR_PROCESS_DESCRIPTION"></span>TDR process description


A common stability problem in graphics occurs when the system appears completely frozen or hung while processing an end-user command or operation. Usually the GPU is busy processing intensive graphics operations, typically during game-play. No screen updates occur, and users assume that their system is frozen. Users usually wait a few seconds and then reboot the system by pressing the power button.

Both Windows Vista and Windows 7 try to detect these problematic hang situations and dynamically recover a responsive desktop. The system does not reboot, but in most cases the screen flickers as it is redrawn. However, some older Microsoft DirectX applications render a black screen at the end of recovery, and users must restart these applications. These GPU hangs are referred to as time-out detection and recovery errors (TDRs).

The figure shows the timeout detection and recovery process. For more details about this process, see [Timeout Detection and Recovery (TDR)](timeout-detection-and-recovery.md).

![timeout detection and recovery (tdr) of gpus through wddm](images/timeoutdetectionrecoverygpusthroughwddm.jpg)

TDRs happen when a GPU command has taken too long to complete or the hardware is hung. TDRs enable the operating system to detect that the UI is not responsive.

## <span id="Nodes"></span><span id="nodes"></span><span id="NODES"></span>Nodes


As used in the above TDR functions, a *node* is one of multiple parts of a single physical adapter that can be scheduled independently. For example, a 3-D node, a video decoding node, and a copy node can all exist in the same physical adapter, and each can be assigned a separate node ordinal value in the [**DXGKARG\_QUERYDEPENDENTENGINEGROUP**](https://msdn.microsoft.com/library/windows/hardware/hh451294).**NodeOrdinal** member in a call to [*DxgkDdiQueryDependentEngineGroup*](https://msdn.microsoft.com/library/windows/hardware/hh451407).

The number of nodes in the physical adapter is reported by the display miniport driver in the **NbAsymetricProcessingNodes** member of [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**GpuEngineTopology**.

The node ordinal value is passed in the **NodeOrdinal** member of the [**DXGKARG\_CREATECONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff557567) structure when a context is created.

## <span id="Engines"></span><span id="engines"></span><span id="ENGINES"></span>Engines


As used in the above TDR functions, an *engine* is one of multiple physical adapters (or GPUs) that together act as one logical adapter. The DirectX graphics kernel subsystem supports such configurations but requires that each engine must have the same number of nodes.

As an example, the GPU scheduler considers engine 0 to correspond to physical adapter 0. Engine 0 must have the same number of nodes as engine 1, which corresponds to adapter 1.

## <span id="Engine_ordinal_value_at_context_creation"></span><span id="engine_ordinal_value_at_context_creation"></span><span id="ENGINE_ORDINAL_VALUE_AT_CONTEXT_CREATION"></span>Engine ordinal value at context creation


When a context is created, a single bit corresponding to the engine ordinal value is set in the **EngineAffinity** member of the [**DXGKARG\_CREATECONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff557567) structure. The **EngineOrdinal** member of this and other scheduler-related structures is a zero-based index. The value of **EngineAffinity** is 1 &lt;&lt; **EngineOrdinal**, and **EngineOrdinal** is the highest bit position in **EngineAffinity**.

## <span id="Packets_unaffected_by_engine_reset"></span><span id="packets_unaffected_by_engine_reset"></span><span id="PACKETS_UNAFFECTED_BY_ENGINE_RESET"></span>Packets unaffected by engine reset


The driver might be asked by the GPU scheduler to resubmit packets that were submitted too late to the engine hardware queue to be fully processed before the engine reset completed. The driver must follow these guidelines to resubmit such packets:

-   *Paging packets*: The driver will be asked by the GPU scheduler to resubmit paging packets with their original fence IDs, and in the same order as they were originally submitted. Any such packets will be resubmitted before new packets are added to the hardware queue.
-   *Render packets*: The GPU scheduler will assign render packets new fence IDs and then resubmit them.

## <span id="Calling_sequence_to_reset_an_engine"></span><span id="calling_sequence_to_reset_an_engine"></span><span id="CALLING_SEQUENCE_TO_RESET_AN_ENGINE"></span>Calling sequence to reset an engine


When [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418) succeeds, the GPU scheduler ensures that the **LastAbortedFenceId** value returned from the engine reset call corresponds either to an existing fence ID in the hardware queue, or to the last completed fence ID on the GPU. The latter situation can happen when the hardware queue empties after the GPU timeout is detected, but before the engine reset callback is invoked.

The last completed fence ID value on the GPU must be maintained by the driver at all times because it is also needed to set the **DmaPreempted**.**LastCompletedFenceId** member of a [**DXGKARGCB\_NOTIFY\_INTERRUPT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff557538) preemption interrupt notification structure. The last completed fence ID should be advanced only in these situations:

-   When a packet is completed (not preempted), the last completed fence ID should be set to the fence ID of the completed packet.
-   When [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418) succeeds, the last completed fence ID should be set to the value of the **LastCompletedFenceId** member returned by the engine reset call.
-   For adapter-wide reset, the last completed fence ID on all nodes should be advanced to the last submitted fence ID at the time of the reset.

Here's a chronological sequence of a successful engine reset, as seen by the GPU scheduler:

1.  A preemption attempt is issued.
2.  A GPU timeout is detected.
3.  A snapshot of the last submitted and completed fence IDs is taken by the GPU scheduler, and interrupts from the timed-out engine are ignored. This is one atomic operation at the device interrupt level.
4.  If there are no packets in the hardware queue at this point, exit. This can happen if a packet was completed in the time window between steps 2 and 3.
5.  All queued DPCs are flushed.
6.  Prepare for engine reset.
7.  Call [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418).
8.  If the **LastAbortedFenceId** member is less than the last completed fence ID or is greater than the last submitted fence ID, the DirectX graphics kernel subsystem causes a system bugcheck to occur. In a crash dump file, the error is noted by the message **BugCheck 0x119**, which has these four parameters:
    -   0xA, meaning the driver has reported an invalid aborted fence ID
    -   **LastAbortedFenceId** value returned by the driver
    -   Last completed fence ID
    -   An internal operating system parameter

9.  If the **LastAbortedFenceId** value is valid, proceed with engine reset recovery as follows. If a paging packet was affected by the engine reset, the GPU scheduler follows the engine reset with an adapter-wide reset. All devices that own allocations referenced by that paging packet are put in the error state as well. However, the system device itself is not put into the error state, and it resumes execution after the reset is complete.

## <span id="Special_cases"></span><span id="special_cases"></span><span id="SPECIAL_CASES"></span>Special cases


A special situation can occur when a packet is completed on the GPU between steps 3 and 7 described above. In this case, **LastAbortedFenceId** should be set by the driver to the fence ID of the last completed packet if there are no packets in the hardware queue from the driver's point of view. From the scheduler's point of view, it will appear that such a packet was aborted, and the corresponding device will be put into an error state even though the packet eventually completed.

If the driver cannot perform a reset operation because the hardware is in an invalid state, or because the hardware is incapable of resetting the nodes, the driver should return a failure status code. If the GPU scheduler receives a failure status code, it performs an adapter-wide reset and restart operation following the [TDR behavior](timeout-detection-and-recovery.md) prior to Windows 8.

Even if a driver has opted into the Windows 8 TDR behavior, there will be cases when the GPU scheduler requests a reset and restart of the entire logical adapter. Therefore the driver must still implement the [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815) and [*DxgkDdiRestartFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559820) functions, and their semantics remain the same as prior to Windows 8. When an attempt to reset a physical adapter with [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418) leads to a reset of the logical adapter, the **!analyze** command of the Windows debugger shows that the **TdrReason** value of the TDR recovery context is set to a new value of **TdrEngineTimeoutPromotedToAdapterReset** = 9.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…TDRResiliency**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





