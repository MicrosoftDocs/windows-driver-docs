---
title: User-Mode Work Submission
description: Describes user-mode work submission in the Windows OS, which enables applications to submit work to the GPU directly from user mode with very low latency.
keywords:
- WDDM, UMD work submission to GPU
- WDDM, hardware scheduling
ms.date: 04/08/2024
---

# User-mode work submission

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This article describes the user-mode (UM) work submission feature that is still under development as of Windows 11, version 24H2 (WDDM 3.2). UM work submission enables applications to submit work to the GPU directly from user mode with very low latency. The goal is to improve performance of applications that submit small workloads frequently to the GPU. In addition, user-mode submission is expected to significantly benefit such applications if they're running inside a container or virtual machine (VM). This benefit is because the user-mode driver (UMD) running in the VM can directly submit work to the GPU without having to send a message to the host.

IHV drivers and hardware that support UM work submission must continue to support the traditional kernel-mode work submission model simultaneously. This support is necessary for scenarios such as an older guest that supports only traditional KM queues running on a latest host.

This article doesn't discuss UM submission interoperability with Flip/FlipEx. UM submission described in this article is limited to render only/compute class of scenarios. The presentation pipeline continues to be based on kernel-mode submission for now as it has a dependency on native monitored fences. The design and implementation of UM submission based presentation can be considered once native monitored fences and UM submission for compute/render only are fully implemented. Hence, drivers should support user mode submission on a per queue basis.

## Doorbells

Most current or upcoming generations of GPUs that support hardware scheduling also support the concept of a GPU *doorbell*. A doorbell is a mechanism to indicate to a GPU engine that new work is queued in its work queue. Doorbells are typically registered in the PCIe BAR (base address bar) or system memory. Each GPU IHV has their own architecture that determines the number of doorbells, where they're located in the system, and so forth. The Windows OS uses doorbells as part of its design to implement UM work submission.

At a high level there are two different models of doorbells implemented by different IHV and GPUs:

* Global doorbells

  In the Global Doorbells model, all the hardware queues across contexts and processes share a single global doorbell. The value written into the doorbell informs the GPU scheduler about which particular hardware queue and engine has new work. The GPU hardware uses a form of a polling mechanism to fetch work if multiple hardware queues are actively submitting work and ringing the same global doorbell.

* Dedicated doorbells

  In the dedicated doorbell model, each hardware queue is assigned its own doorbell that is rung whenever there's new work to be submitted to the GPU. When a doorbell is rung, the GPU scheduler knows exactly which hardware queue submitted new work. There are limited doorbells that are shared across all hardware queues created on the GPU. If the number of hardware queues created exceeds the number of available doorbells, the driver needs to disconnect the doorbell of an older or least recently used hardware queue and assign its doorbell to a newly created queue, effectively "virtualizing" doorbells.

## Discovering user-mode work submission support

### DXGK_NODEMETADATA_FLAGS::UserModeSubmissionSupported

For GPU nodes that support the UM work submission feature, KMD's [**DxgkDdiGetNodeMetadata**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata) sets the **UserModeSubmissionSupported** node metadata flag that is added to [**DXGK_NODEMETADATA_FLAGS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_nodemetadata_flags). The OS then allows UMD to create user-mode submission HWQueues and doorbells only on nodes for which this flag is set.

### DXGK_QUERYADAPTERINFOTYPE::DXGKQAITYPE_USERMODESUBMISSION_CAPS

To query doorbell-specific information, the OS calls KMD's [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) function with the [**DXGKQAITYPE_USERMODESUBMISSION_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) query adapter info type. KMD responds by populating a [**DXGK_USERMODESUBMISSION_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_usermodesubmission_caps) structure with its support details for user-mode work submission.

Currently, the only cap required is the doorbell memory size (in bytes). *Dxgkrnl* needs the doorbell memory size for a couple of reasons:

* During doorbell creation ([**D3DKMTCreateDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatedoorbell)), *Dxgkrnl* returns a **DoorbellCpuVirtualAddress** to UMD. Before doing so, *Dxgkrnl* first needs to internally map to a dummy page because the doorbell isn't yet assigned and connected. The size of the doorbell is needed to allocate the dummy page.
* During doorbell connect ([**D3DKMTConnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-d3dkmt_connect_doorbell)), *Dxgkrnl* needs to rotate the **DoorbellCpuVirtualAddress** to a **DoorbellPhysicalAddress** provided by KMD. Again, *Dxgkrnl* needs to know the doorbell size.

### D3DDDI_CREATEHWQUEUEFLAGS::UserModeSubmission in D3DKMTCreateHwQueue

UMD sets the added **UserModeSubmission** flag added to [**D3DDDI_CREATEHWQUEUEFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_createhwqueueflags) for creating HWQueues that use the user-mode submission model. HWQueues created using this flag can't use the regular kernel-mode work submission path and must rely on the doorbell mechanism for work submission on the queue.

## User-mode work submission APIs

The following user-mode APIs are added to support user-mode work submission.

* [**D3DKMTCreateDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatedoorbell) creates a doorbell for a D3D HWQueue for user-mode work submission.

* [**D3DKMTConnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtconnectdoorbell) connects a previously created doorbell to a D3D HWQueue for user-mode work submission.

* [**D3DKMTDestroyDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtdestroydoorbell) destroys a previously created doorbell.

* [**D3DKMTNotifyWorkSubmission**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtnotifyworksubmission) notifies the KMD that new work was submitted on a HWQueue. The point of this feature is a low latency work submission path, where KMD isn't involved or aware when work is submitted. This API is useful in scenarios where the KMD needs to be notified whenever work is submitted on a HWQueue. Drivers should use this mechanism in specific and infrequent scenarios because it involves a round trip from UMD to KMD on every work submission, thus defeating the purpose of a low latency user-mode submission model.

## Residency model of doorbell memory and ring buffer allocations

* UMD is responsible for making the ring buffer and ring buffer control allocations resident before creating a doorbell.
* UMD manages the lifetime of the ring buffer and ring buffer control allocations. *Dxgkrnl* won't destroy these allocations implicitly even if the corresponding doorbell is destroyed. UMD is responsible for allocating and destroying these allocations. However, to prevent a malicious user-mode program from destroying these allocations while the doorbell is alive, *Dxgkrnl* does take a reference on them during the lifetime of the doorbell.
* The only scenario in which *Dxgkrnl* destroys ring buffer allocations is during device termination. *Dxgkrnl* destroys all HWQueues, doorbells, and ring buffer allocations associated with the device.
* As long as the ring buffer allocations are alive, the ring buffer CPUVA is always valid and available for UMD to access, irrespective of the doorbell connections status. That is, ring buffer residency isn't tied to the doorbell.
* When KMD makes the DXG callback to disconnect a doorbell (that is, calls [**DxgkCbDisconnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_disconnectdoorbell.md) with status D3DDDI_DOORBELL_STATUS_DISCONNECTED_RETRY), *Dxgkrnl* rotates the doorbell CPUVA to a dummy page. It doesn't evict or unmap the ring buffer allocations.
* In the event of any device-lost scenarios (TDR/GPU Stop/Page, etc.), *Dxgkrnl* disconnects the doorbell and marks the status as D3DDDI_DOORBELL_STATUS_DISCONNECTED_ABORT. User mode is responsible for destroying the HWQueue, doorbell, ring buffer, and for re-creating them. This requirement is similar to how other device resources are destroyed and re-created in this scenario.

## Hardware context suspension

When the OS suspends a hardware context, *Dxgkrnl* keeps the doorbell connection active and ring buffer (work queue) allocation resident. In this way, UMD can continue queuing work to the context; this work just doesn’t get scheduled while the context is suspended. Once the context is resumed and scheduled, the GPU's context management processor (CMP) observes the new write pointer and work submission.

This logic is similar to current kernel-mode submission logic, where UMD can call [**D3DKMTSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtsubmitcommand) with a suspended context. *Dxgkrnl* enqueues this new command to the HwQueue but it just doesn’t get scheduled until a later time.

The following sequence of events occurs during hardware context suspend and resume.

* Suspending a hardware context:

  1. *Dxgkrnl* calls [**DxgkddiSuspendContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_suspendcontext).
  2. KMD removes all HWQueues of the context from the HW scheduler’s list.
  3. Doorbells are still connected and ring buffer/ring buffer control allocations are still resident.  The UMD can write new commands to the HWQueue of this context, but the GPU won’t process them, which is similar to today’s kernel-mode command submission to a suspended context.
  4. If KMD chooses to victimize the doorbell of a suspended HWQueue, then UMD loses its connection. UMD can attempt to reconnect the doorbell and KMD will assign a new doorbell to this queue. The intention is to not stall the UMD, but rather to allow it to continue submitting work that the HW engine can eventually process once the context is resumed.

* Resuming a hardware Context:

  1. *Dxgkrnl* calls [**DxgkddiResumeContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resumecontext).
  2. KMD adds all HWQueues of the context to HW scheduler’s list.

## Engine F-state transitions

In traditional kernel-mode work submission, *Dxgkrnl* is in charge of submitting new commands to the HWQueue and monitoring completion interrupts from KMD. For this reason, *Dxgkrnl* has a complete view of when an engine is active and idle.

In user-mode work submission, *Dxgkrnl* monitors whether a GPU engine is making progress using TDR timeout cadence, so if it's worthwhile to initiate a transition to F1 state sooner than in the two-second TDR timeout, the KMD can request the OS to do so.

The following changes were made to facilitate this approach:

* The **DXGK_INTERRUPT_GPU_ENGINE_STATE_CHANGE** interrupt type is added to [**DXGK_INTERRUPT_TYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_interrupt_type). KMD uses this interrupt to notify *Dxgkrnl* of engine state transitions that require a GPU power action or timeout recovery such as *Active -> TransitionToF1* and *Active -> Hung*.

* The **EngineStateChange** interrupt data structure is added to [**DXGKARGCB_NOTIFY_INTERRUPT_DATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data).

* The [**DXGK_ENGINE_STATE**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_dxgk_engine_state) enum is added to represent the engine state transitions for **EngineStateChange**.

When KMD raises a **DXGK_INTERRUPT_GPU_ENGINE_STATE_CHANGE** interrupt with **EngineStateChange.NewState** set to **DXGK_ENGINE_STATE_TRANSITION_TO_F1**, *Dxgkrnl* disconnects all doorbells of HWQueues on this engine and then initiates an F0 to F1 power component transition.

When the UMD attempts to submit new work to the GPU engine in F1 state, it needs to reconnect the doorbell, which in turn causes *Dxgkrnl* to initiate a transition back to the F0 power state.

## Engine D-state transitions

During a D0 to D3 device power state transition, *Dxgkrnl* suspends the HWQueue, disconnects the doorbell (rotating the doorbell CPUVA to a dummy page), and updates the **DoorbellStatusCpuVirtualAddress** doorbell status to D3DDDI_DOORBELL_STATUS_DISCONNECTED_RETRY.

If UMD calls [**D3DKMTConnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtconnectdoorbell) when the GPU is in D3, it forces *Dxgkrnl* to wake up the GPU to D0. *Dxgkrnl* is also responsible for resuming the HWQueue and rotating the doorbell CPUVA to a physical doorbell location.

The following sequence of events takes place.

* A D0 to D3 GPU power down occurs:

  1. *Dxgkrnl* calls [**DxgkddiSuspendContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_suspendcontext) for all HW contexts on the GPU. KMD removes these contexts from the HW scheduler list.
  2. *Dxgkrnl* disconnects all doorbells.
  3. *Dxgkrnl* possibly evicts all Ring Buffer/Ring Buffer Control allocations from VRAM if necessary. It does so once all contexts are suspended and removed from the hardware scheduler's list so that hardware doesn’t reference any evicted memory.

* UMD writes a new command to a HWQueue when the GPU is in D3 state:

  1. UMD sees doorbell is disconnected, so calls [**D3DKMTConnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtconnectdoorbell).
  2. *Dxgkrnl* initiates a D0 transition.
  3. *Dxgkrnl* makes all Ring Buffer/Ring Buffer Control allocations resident if they were evicted.
  4. *Dxgkrnl* calls KMD's [**DxgkddiCreateDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdoorbell) function to request that KMD make a doorbell connection for this HWQueue.
  5. *Dxgkrnl* calls [**DxgkddiResumeContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resumecontext) for all HWContexts. KMD adds the corresponding queues to the HW scheduler’s list.

## DDIs for user-mode work submission

### KMD-implemented DDIs

The following kernel-mode DDIs are added for KMD to implement user-mode work submission support.

* [**DxgkDdiCreateDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdoorbell). When UMD calls [**D3DKMTCreateDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatedoorbell) to create a doorbell for a HWQueue, *Dxgkrnl* makes a corresponding call to this function so that KMD can initialize its doorbell structures.

* [**DxgkDdiConnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_connectdoorbell). When UMD calls [**D3DKMTConnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtconnectdoorbell), *Dxgkrnl* makes a corresponding call to this function so that KMD can provide a CPUVA mapped to the physical doorbell location, and also make the required connections between the HWQueue object, doorbell object, doorbell physical address, GPU scheduler, and so forth.

* [**DxgkDdiDisconnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_disconnectdoorbell). When the OS wants to disconnect a particular doorbell, it calls KMD with this DDI.

* [**DxgkDdiDestroyDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroydoorbell). When UMD calls [**D3DKMTDestroyDoorbell**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtdestroydoorbell), *Dxgkrnl* makes a corresponding call to this function so that KMD can destroy its doorbell structures.

* [**DxgkDdiNotifyWorkSubmission**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_notifyworksubmission). When UMD calls [**D3DKMTNotifyWorkSubmission**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtnotifyworksubmission), *Dxgkrnl* makes a corresponding call to this function so that KMD can be notified of new work submissions.

### *Dxgkrnl*-implemented DDI

The [**DxgkCbDisconnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_disconnectdoorbell) callback is implemented by *Dxgkrnl*. KMD can call this function to notify *Dxgkrnl* that KMD needs to disconnect a particular doorbell.

## HW queue progress fence changes

Hardware queues running in the UM work submission model still have a concept of a monotonically increasing progress fence value that UMD generates and writes when a command buffer is completed. In order for *Dxgkrnl* to know whether a particular hardware queue has pending work, the UMD needs to update the queued progress fence value just before appending a new command buffer to the ring buffer and making it visible to the GPU. [**CreateDoorbell.HwQueueProgressFenceLastQueuedValueCPUVirtualAddress**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-d3dkmt_create_doorbell) is a read/write user-mode process mapping of the latest queued value.

It's essential for the UMD to ensure the queued value is updated right before the new submission is made visible to the GPU. The following steps are the recommended sequence of operations. They assume the HW queue is idle and the last finished buffer had a progress fence value of *N*.

* Generate a new progress fence value *N+1*.
* Fill out the command buffer. The last instruction of the command buffer is a progress fence value write to *N+1*.
* Inform the OS of the newly queued value by setting *(**HwQueueProgressFenceLastQueuedValueCPUVirtualAddress**) equal to *N+1*.
* Make the command buffer visible to the GPU by adding it to the ring buffer.
* Ring the doorbell.

## Normal and abnormal process termination

The following sequence of events takes place during normal process termination.

For each HWQueue of the device/context:

1. *Dxgkrnl* calls [**DxgkDdiDisconnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_disconnectdoorbell) to disconnect the doorbell.
2. *Dxgkrnl* waits for the last queued **HwQueueProgressFenceLastQueuedValueCPUVirtualAddress** to be completed on the GPU. Ring Buffer/Ring Buffer Control allocations remain resident.
3. *Dxgkrnl*’s wait is satisfied, and it can now destroy the Ring Buffer/Ring Buffer Control allocations, and doorbell and HWQueue objects.

The following sequence of events takes place during abnormal process termination.

1. *Dxgkrnl* marks the device in error.

2. For each device context, *Dxgkrnl* calls [**DxgkddiSuspendContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_suspendcontext) to suspend the context. The Ring Buffer/Ring Buffer Control allocations are still resident. KMD preempts the context and removes it from its HW run list.

3. For each HWQueue of context, *Dxglrnl*:

   a. Calls [**DxgkDdiDisconnectDoorbell**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_disconnectdoorbell) to disconnect the doorbell.

   b. Destroys the Ring Buffer/Ring Buffer Control allocations, and the doorbell and HWQueue objects.

## Pseudocode examples

### Work submission pseudocode in UMD

The following pseudocode is a basic example of the model that UMD should use for creating and submitting work to HWQueues using the doorbell APIs. Consider ```hHWqueue1``` is the handle to a HWQueue created with the ```UserModeSubmission``` flag using the existing D3DKMTCreateHwQueue API.

``` C
// Create a doorbell for the HWQueue
D3DKMT_CREATE_DOORBELL CreateDoorbell = {};
CreateDoorbell.hHwQueue = hHwQueue1;
CreateDoorbell.hRingBuffer = hRingBufferAlloc;
CreateDoorbell.hRingBufferControl = hRingBufferControlAlloc;
CreateDoorbell.Flags.Value = 0;

NTSTATUS ApiStatus =  D3DKMTCreateDoorbell(&CreateDoorbell);
if(!NT_SUCCESS(ApiStatus))
  goto cleanup;

assert(CreateDoorbell.DoorbellCPUVirtualAddress!=NULL && 
      CreateDoorbell.DoorbellStatusCPUVirtualAddress!=NULL);

// Get a CPUVA of Ring buffer control alloc to obtain write pointer.
// Assume the write pointer is at offset 0 in this alloc
D3DKMT_LOCK2 Lock = {};
Lock.hAllocation = hRingBufferControlAlloc;
ApiStatus = D3DKMTLock2(&Lock);
if(!NT_SUCCESS(ApiStatus))
  goto cleanup;

UINT64* WritePointerCPUVirtualAddress = (UINT64*)Lock.pData;

// Doorbell created successfully. Submit command to this HWQueue

UINT64 DoorbellStatus = 0;
do
{
  // first connect the doorbell and read status
  ApiStatus = D3DKMTConnectDoorbell(hHwQueue1);
  D3DDDI_DOORBELL_STATUS DoorbellStatus = *(UINT64*(CreateDoorbell.DoorbellStatusCPUVirtualAddress));

  if(!NT_SUCCESS(ApiStatus) ||  DoorbellStatus == D3DDDI_DOORBELL_STATUS_DISCONNECTED_ABORT)
  {
    // fatal error in connecting doorbell, destroy this HWQueue and re-create using traditional kernel mode submission.
    goto cleanup_fallback;
  }

  // update the last queue progress fence value
  *(CreateDoorbell.HwQueueProgressFenceLastQueuedValueCPUVirtualAddress) = new_command_buffer_progress_fence_value;

  // write command to ring buffer of this HWQueue
  *(WritePointerCPUVirtualAddress) = address_location_of_command_buffer;

  // Ring doorbell by writing the write pointer value into doorbell address. 
  *(CreateDoorbell.DoorbellCPUVirtualAddress) = *WritePointerCPUVirtualAddress;

  // Check if submission succeeded by reading doorbell status
  DoorbellStatus = *(UINT64*(CreateDoorbell.DoorbellStatusCPUVirtualAddress));
  if(DoorbellStatus == D3DDDI_DOORBELL_STATUS_CONNECTED_NOTIFY)
  {
      D3DKMTNotifyWorkSubmission(CreateDoorbell.hDoorbell);
  }

} while (DoorbellStatus == D3DDDI_DOORBELL_STATUS_DISCONNECTED_RETRY);
```

### Victimizing doorbell pseudocode in KMD

The following example illustrates how KMD might need to "virtualize" and share the available doorbells between the HWQueues on GPUs that use dedicated doorbells.

KMD's ```VictimizeDoorbell()``` function's pseudocode:

* KMD decides that logical doorbell ```hDoorbell1``` connected to ```PhysicalDoorbell1``` needs to be victimized and disconnected.
* KMD calls *Dxgkrnl*'s ```DxgkCbDisconnectDoorbellCB(hDoorbell1->hHwQueue)```.
  * *Dxgkrnl* rotates the UMD-visible CPUVA of this doorbell to a dummy page and updates the status value to D3DDDI_DOORBELL_STATUS_DISCONNECTED_RETRY.
* KMD gets back control and does the actual victimization/disconnection.
  * KMD victimizes ```hDoorbell1``` and disconnects it from ```PhysicalDoorbell1```.
  * ```PhysicalDoorbell1``` is available for use

Now, consider the following scenario:

1. There's a single physical doorbell in the PCI BAR with a kernel-mode CPUVA equal to ```0xfeedfeee```. A doorbell object created for a HWQueue is assigned this physical doorbell value.

   ``` pseudocode
   HWQueue KMD Handle: hHwQueue1
   Doorbell KMD Handle: hDoorbell1
   Doorbell CPU Virtual Address: CpuVirtualAddressDoorbell1 =>  0xfeedfeee // hDoorbell1 is mapped to 0xfeedfeee
   Doorbell Status CPU Virtual Address: StatusCpuVirtualAddressDoorbell1 => D3DDDI_DOORBELL_STATUS_CONNECTED
   ```

2. The OS calls ```DxgkDdiCreateDoorbell``` for a different ```HWQueue2```:

   ``` pseudocode
   HWQueue KMD Handle: hHwQueue2
   Doorbell KMD Handle: hDoorbell2
   Doorbell CPU Virtual Address: CpuVirtualAddressDoorbell2 => 0 // this doorbell object isn't yet assigned to a physical doorbell  
   Doorbell Status CPU Virtual Address: StatusCpuVirtualAddressDoorbell2 => D3DDDI_DOORBELL_STATUS_DISCONNECTED_RETRY

   // In the create doorbell DDI, KMD doesn't need to assign a physical doorbell yet, 
   // so the 0xfeedfeee doorbell is still connected to hDoorbell1
   ```

3. The OS calls ```DxgkDdiConnectDoorbell``` on ```hDoorbell2```:

   ``` pseudocode
   // KMD needs to victimize hDoorbell1 and assign 0xfeedfeee to hDoorbell2. 
   VictimizeDoorbell(hDoorbell1);

   // Physical doorbell 0xfeedfeee is now free and can be used vfor hDoorbell2.
   // KMD makes required connections for hDoorbell2 with HW
   ConnectPhysicalDoorbell(hDoorbell2, 0xfeedfeee)
  
   return 0xfeedfeee

   // On return from this DDI, *Dxgkrnl* maps 0xfeedfeee to process address space CPUVA i.e:
   // CpuVirtualAddressDoorbell2 => 0xfeedfeee

   // *Dxgkrnl* updates hDoorbell2 status to connected i.e:
   // StatusCpuVirtualAddressDoorbell2 => D3DDDI_DOORBELL_STATUS_CONNECTED
   ``

This mechanism isn't required if a GPU uses global doorbells. Instead, in this example, both ```hDoorbell1``` and ```hDoorbell2``` would be assigned the same ```0xfeedfeee``` physical doorbell.
