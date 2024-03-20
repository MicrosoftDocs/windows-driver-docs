---
title: Live Migration on GPU-P Devices
description: Describes live migration on GPU-P devices and how to implement it in a kernel-mode display driver.
keywords:
- WDDM, live migration
- WDDM, live migration support in kernel-mode driver
- WDDM, quick migration
- WDDM, GPU paravirtualization
- WDDM, GPUP
- WDDM, GPU-P
ms.date: 03/21/2024
---

# Live migration on GPU-P devices

This article describes the DDI design of the *live migration* of heterogenous compute devices (GPUs, NPUs, etc.) virtualized through SR-IOV (single root I/O virtualization) partitioning. Devices that support partitioning through the WDDM and MCDM driver models have become an integral part of our virtualization offerings. Thus, it's important to support live migration and help our virtualization abstractions become maximally reliable to reduce customer impact when resource assignments must change. This article also describes the *quick migration* of these devices as well.

Live migration is supported starting in Windows 11, version 24H2 (WDDM 3.2). It's more generally an extension of the GPU paravirtualization (GPU-P) DDIs for drivers that expose the capability. These interfaces can optionally be implemented by MCDM drivers that also implement the GPU-P virtualization interfaces, including their extension with triage events. Also note that the use of the term "GPU" in this article simply refers to devices that implement the GPU-P virtualization framework, whether WDDM or MCDM, and whether GPU, NPU, or other heterogenous compute device.

## Kinds and Purpose of Resource Migration

Resource migration is the ability to move a virtualization to new physical resources. There are a variety of ways in which virtualized execution can be moved, including:

* Hard power down. The virtual motherboard can be powered down directly, stopping execution of the virtual resources. Any applications that aren't powerhit-tolerant lose the data they are operating on, and all device state is wiped. The virtual hard disk (VHD) can then be virtualized on a different host machine, which results in a cold boot.

* Soft power down. This power down differs from the hard power down in that it simply sends the power request to the guest OS, and the guest OS distributes the power down mechanism to applications to cleanly shut down. Applications can use this notification to safely store all data and register to restart on boot, though it is dependent on each application’s programming. A soft power down requires a guest OS that supports this mechanism of clean shutdown and the appropriate services to store current state and restart on reboot.

* Hibernation. This other guest-originated technology allows the guest to transition to a fast-starting sleep power state where all application processes are frozen, the device state is purged to CPU memory, and all memory is then sent to storage to allow the hardware to power down. Then, the VM storage VHD can be restarted on a different machine, and the memory loaded, the device state restored, and the processes unfrozen. Hibernation is only available on guest OSes that support it. It's a fairly invasive process that depends on guest stability, but it provides a mechanism to restore application processes with state that the power down mechanisms don't provide.

* Quick Migration (also known as *VM Save and Restore*). With this technology, the VM is paused (vCPUs stop scheduling) and all state needed to restore state on the new physical resources is gathered inside the Host OS – including the memory of the VM and the state of all devices. This state is then transferred to the new Host, where a VM is created with all vCPU contexts loaded, the memory mapped to the VM space, and the device states restored. A PowerOnRestore then restarts execution of the vCPUs. This technology is independent of the Guest OS and doesn't depend on execution in the guest environment, so it's a more reliable way to maintain process and device state than Hibernation. The virtualization user might notice a significant down time as the VM memory can be many GBs and transfer times can be noticeable.

* Live Migration. If we have the ability to transfer content while the virtualized resources are still active and we can track content that gets dirtied, we have the ability to transfer significant content leaving the virtualization active. Then, when the VM is paused, far less content needs to be transferred and we can minimize the time the virtualization is not executing. The result is minimized end user impact, as all operations occurring during the migration continue unimpeded and the impact to resource consumption rate is reduced as far as is currently possible. In particular, outage deadlines (external time constraints to the virtualization outage, like TCP and other protocol timeouts with external endpoints) can be minimized or eliminated.

Each progression reduces or removes some (often major) customer awareness of the change in physical assignment of a virtualization, making the virtualization more and more complete and transparent to the user. Along with other technologies (like Host crash isolation) that separate out the customer dependencies on infrastructure, it moves our virtualization solution towards the ideal of assignment independence and true ephemeral compute.

## Large-Scale Design

Live migration transfers virtualization content from a Source Host to a Target Host. The virtualization consists of a variety of stateful devices, which can include memory, compute, and storage, each with data that must be transferred from the devices on the source over to the devices on the target. Executive Agents that manage virtualizations across clusters communicate to Hosts to let them know to setup orchestration for either Source Migration of an existing VM (when the content is leaving the Host) or for Target Migration to a new VM (to receive the content). The major players in this interaction are seen in the following diagram.

::::image type="content" source="images/DDIComponent.png" alt-text="Diagram illustrating the architectural components for live migration.":::

## Epochs of the Source Host

The following diagram illustrates source-side migration states.

::::image type="content" source="images/SourceState.png" alt-text="Diagram illustrating source-side migration state.":::

### Source-side boot

When a Host boots generally, the KMD reports device capabilities to the kernel through a variety of initialization calls.

When the KMD receives the [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call for [**DXGKQAITYPE_GPUPCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) data, a **LiveMigration** capability bit has been added to [**DXGK_GPUPCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gpupcaps). When KMD sets this bit, it indicates that the driver supports live migration.

A prerequisite to live migration support is to support for the tracking of modified VRAM pages on all GPU-local memory segments, as described in [Dirty bit tracking](dirty-bit-tracking.md). That support is reported through additional **DxgkDdiQueryAdapterInfo** calls for other specified information types. A driver that reports support for live migration must also report support for dirty bit tracking. Support for live migration but not dirty bit tracking is an invalid configuration and *Dxgkrnl* fails to start the adapter.

### VMs online

Once the host has booted and the management stacks have come online, virtual machine activity begins to come online. Requests for starting and stopping VMs begin to arrive and we start to see GPU-P vGPUs projected into these virtualizations.

Assuming performant dirty bit plane capability, *Dxgkrnl* calls [**DxgkDdiStartDirtyTracking**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_startdirtytracking) after reserving the VRAM resources for a VF (virtual function), which allows the system to track VRAM cleanliness in the case where the VF later participates in a migration scenario.

This VM startup begins to intercept interrupt table access to virtualize interrupt support, which proceeds for the lifetime of the VM.

### Live migration send preparation

The management stack sends the event to begin live migration when indicated by its controls, and the migration state machine management gathers all state from the virtual device that will be immutable for the lifetime of the virtualization (vGPU partition configuration metrics) in order to reconstruct the vGPU on the target. Once ready, the process of preparation of the transport buffers and initialization of the transport stack is started.

This epoch generates a call to the introduced [**DxgkDdiPrepareLiveMigration**]() DDI. The intent of this call is to establish the PF/VF scheduling policies that provide for the live migration’s ability to stream dirty content from the VRAM in the host while preserving fair performance for the VF. If the dirty tracking is reported as nonperformant, this is also where the dirty tracking is started.

### Live migration send

::::image type="content" source="images/SourceTransfer.png" alt-text="Diagram illustrating live migration send.":::

 We then enter the active phase of the dirty VRAM transfer. This phase involves making calls through the dirty bitplane DDI to get snapshots of the VF framebuffer and then paging those pages from the GPU to the CPU buffers prepared earlier.

There comes a stage in this transfer where the VM and all its virtual devices are paused. The VF can stop being scheduled for the guest, and at this time, any additional timeslice that can be given to the PF to finish the paging of content should be. Because both the VF and the vCPU are paused in the VM, it's expected that there should be no further changes to content being migrated (CPU or device-local memory) after this point.

### Paused migration send

The last iteration of dirty pages are transferred while paused. At this point, a call is made to gather any last pieces of device and driver state that was mutable while active and couldn’t be transferred in the earlier preparation. This state can be any state reconstruction needed on the other side, any tracking structures, or generally all information necessary to finalize the restoration of VF state on the target side.

### Live migration teardown

Finally, once the VM and all of its virtual devices have transferred their state to their new physical realizations, the source side can clean up the VM remnants. The buffers and other migration state are cleared up and the vGPU is destroyed.

## Epochs of the target host

The following diagram illustrates target-side migration states.

::::image type="content" source="images/TargetState.png" alt-text="Diagram illustrating target-side migration state.":::

### Target-side boot

Boot on the target looks the same as on the source. Boot is for the whole system, which can be a source and target on different VFs throughout its lifecycle. The driver just needs to specify support of live migration to participate.

### Live migration receive preparation

On the target side, the VM is constructed starting as if it were a new VM. The VM and the virtual devices are created. This creation process includes the virtual GPU, created using the same parameters it was created with on the source side. After creation, the validation data is received and passed to the driver to validate that the target side is compatible with the source to restore the VM. At that point, it should ensure anything that could affect such compatibility, including driver version, firmware version(s), and other ambient state of the target system and driver. The driver will configure to allow the PF access to all timeslice of paging that would normally be assigned to the VF while that VF is not yet active.

### Live migration receive

::::image type="content" source="images/TargetTransfer.png" alt-text="Diagram illustrating live migration send.":::

 The receive of dirty page data is similar to the stage on the source, except the paging direction is from CPU buffers to VRAM. All transfers are made while the VF is paused, so the entire transfer can be done within the VF budget.

### VM start and teardown

Once all of the VRAM migration has completed, the vGPU gets a chance to set up any additional state that needed to be transferred (the final mutable save data). Then we start the VM on the target and teardown the migration state, including the buffers used for the transfer.

## Performance Goals

An important part of live migration is its responsiveness. In particular, it minimizes the downtime of the virtualization where it won't respond externally (either to the user of the virtualization or any endpoints it might be further connected to). Many network stack protocols have timeouts across remote machines that are quite brief before retry/reestablish fails, and so can be disruptive to the user when dropped. As a common fixed goal, it's desired that the total pause time to transfer and start is under three quarters of a second (750 ms), which pushes the time out of contact to under many of the most common stack timeouts.

Additionally, the performance changes to the active system shouldn't trigger other end-user disruptions if at all possible. In the devices using these DDIs, that primarily means we shouldn't significantly increase the rate of TDRs by slowing down the timeslice scheduled. Now, we expect most TDRs aren't long packets but hung devices instead, and doubling or tripling the time to execute a packet shouldn't push most packets over the large timeouts of seconds. But we need to be aware of not triggering our timeouts in the general performance picture.

## Device driver interfaces

Generally, the live migration DDIs refer to the general concepts of WDDM and MCDM DDIs and the GPU-P virtualization DDIs in particular.

hAdapter: will generally refer to the handle token that represents a specific device that this driver manages. Systems with multiple physical devices enumerated by the system may have a driver manage multiple hAdapters, so this localizes to the specific device.

vfIndex: identifies which virtual function / vDEV is being referenced - so this localizes to the specific virtual device. This is sometimes also called the partition ID.

DeviceLuid: this also localizes the specific virtual device, but down in the language of the UMED interface with the virtual device management.

SegmentId: identifies specific VidMm segment exposure when referencing content stored on the device - like VRAM reserve.

### Note on interface definitions

This DDI document refers to dynamically sized structures. These structures are implemented through dynamically sized arrays, which the reference pages describe like:

``` cpp
    size_t       ArraySize;
    ElementType  Array[ArraySize];
```

where the interface passes an array size earlier in the structure and the parsing of the interface object then iterates over that many elements when the array is supplied. These declarations aren't valid C/C++ as those languages express statically sized fragments. Read in the static sized structure first and then dynamically parse in code.

### Device start and caps reporting

The 
KMD must fill out the following caps in response to the DXGKQAITYPE_GPUPCAPS [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) request. The OS queries caps during device initialization after DxgkDdiStartDevice is called and when the adapter supports GPU partitioning.

* 
``` cpp
//
// These caps must be filled out by the KMD in response to DXGKQAITYPE_GPUPCAPS QueryAdapterInfo request.
// These are queried by the OS during device initialization after DxgkDdiStartDevice is called and
// when the adapter supports GPU partitioning.
//
struct _DXGK_GPUPCAPS
{
    union
    {
        struct
        {
            UINT VirtualMachineHibernation  : 1;
            UINT HotDriverUpdate            : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_2)
            UINT LiveMigration              : 1;
            UINT ScatterMapReserve          : 1;
            UINT Reserved                   : 28;
#else
            UINT Reserved                   : 30;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_2)
        };
        UINT Value;
    } Caps;
} DXGK_GPUPCAPS;
The LiveMigration cap indicates support generally of the DDIs of this document except for the new SetVGPUResources DDI (v2) mentioned below. This SetVGPUResources is tied to the ScatterMapReserve flag.

If the driver returns the ScatterMapReserve cap, it will need to expose a new QueryAdapterInfo DXGKQAITYPE_SCATTER_RESERVE with interface types

struct DXGK_QUERYSCATTERRESERVEIN
{
    UINT  SegmentId;
};
struct DXGK_QUERYSCATTERRESERVEOUT
{
    UINT64  SetVGPUResourcesPageSize;
};
Here, SegmentId will only refer to local memory segments.

The SetVGPUResourcesPageSize field will describe the page size of the 2nd phase of GPUVA translation available on the hardware (in bytes). We expect the page size to align with the reserve physical assignments (partition VRAM sizes and offsets are multiples of this page size).

### Scatter-Paging Support
In order to support the transfer of noncontiguous dirty pages to/from the framebuffer, this project will be one of the first to exercise GPUVA mappings that are not backed by contiguous physical addresses. The paging interfaces do not need to be updated for this support as this has always been a possibility supported by the page tables generally, but any latent implementation details that made assumptions about contiguity will likely be exposed by this change. So it is important to understand this new OS mechanism, how it will execute the virtual paging interfaces, and ensure that the paging is robust to this change.

In particular, the TransferVirtual interface will now be passing VA ranges that are not mapped contiguously on the framebuffer.

### Live migration Start Send-Side
When we start the live component of the migration, we need to first notify the driver that this epoch has begun and allow it to configure the VF scheduling policy for the migration, which should apportion some of the free and migrating-VF budget for PF paging.

enum DXGK_GPUP_MIGRATIONTYPE
{
    DXGK_GPUP_MIGRATIONTYPE_SOURCE = 0,
    DXGK_GPUP_MIGRATIONTYPE_TARGET
};
struct DXGK_GPUP_PREPARE_LIVE_MIGRATION
{
    UINT                     vfIndex;
    DXGK_GPUP_MIGRATIONTYPE  MigrationType;
};
NTSTATUS DxgkDdiPrepareLiveMigration(
    HANDLE                              hAdapter,
    DXGK_GPUP_PREPARE_LIVE_MIGRATION *  pArgs
    );
MigrationType provides details as to the side of migration process to prepare for.

This interface call allows the driver to configure the virtual function, it's scheduling, it's own internal state, and anything else needed around managing the migration.

Then we need to grab the information about the device to restore on the target side. This is also an opportunity to validate the configuration of the remote, so we ask that the KMD package up enough information in this request to validate any hardware, firmware, or driver validation data that will detect the capability to move the VF over to the target configuration.

struct DXGK_GPUP_SAVE_IMMUTABLE_MIGRATION_DATA
{
	[in]     UINT      vfIndex;
	[in,out] UINT64 *  DataSize;
	[in,out] BYTE *    Data;
};
NTSTATUS DxgkDdiSaveImmutableMigrationData(
    HANDLE                                     hAdapter,
    DXGK_GPUP_SAVE_IMMUTABLE_MIGRATION_DATA *  pArgs
    );
DataSize is a size (in bytes) of a buffer. Data is that buffer.

This DDI is called in the classic dynamic buffer pattern:

First call has DataSize 0 in and Data pointer NULL. The DataSize value is changed to the total size needed to store the immutable data.
Then a buffer of the appropriate DataSize is created.
And a second call to the interface has DataSize set to the value used and the Data pointer points to the new buffer.
We will control the lifetime of this memory after the call.

The driver should use this to store data about the VF that will not change while it is alive that the KMD on the target can use to help initialize the new VF. This does not need to include the vGPU creation parameters, as those will be transferred in lower levels and used to create the vGPU using the normal DDI. This can include all data that is immutably tied to the VF, and does not all need to be restored on the target side. Data can be sent purely for validation purposes, and this is a critical part of this interface.

After the immutable data and the validation data is accumulated and sent, the main iterative loop of dirty send will begin.

### Iterative Save / Send
As described in the overview section, the iterated save operation will use the DxgkDdiQueryDirtyBitData to snapshot the current dirty bitplane for the VF at the start of each iteration and use the standard DXGK_OPERATION_VIRTUAL_TRANSFER to page the dirty pages reported. If this is on a device that has reported in it’s dirty tracking capabilities that it is not a negligible performance impact, the iteration control will first enable the dirty tracking, then transfer the entire framebuffer before the first call to query the dirty bitplane.

For the virtual transfer, the primary new behavior is that the mapping will not be contiguous VA to contiguous PA, but may have disconnected pages of PA under the mapping. Otherwise, behavior is as described in the original paging and dirty bitplane tracking documentation, and this project does not add to that.

### Live migration End Send-Side
At the end of the migration, we need to collect all device and driver state needed to finish rebuilding state and tracking that was not yet transferred. This is data that could not be transferred because it did not fit the immutability requirements of the earlier migration data and was not VRAM dirty content. A new DDI is available here, with the same usage as the similar earlier immutable transfer.

typedef struct DXGK_GPUP_SAVE_MUTABLE_MIGRATION_DATA
{
	[in]     UINT      vfIndex;
	[in,out] UINT64 *  DataSize;
	[in,out] BYTE *    Data;
};
NTSTATUS DxgkDdiSaveMutableMigrationData(
    HANDLE                                   hAdapter,
    DXGK_GPUP_SAVE_MUTABLE_MIGRATION_DATA *  pArgs
    );
Again, we expect a two-phase dynamic sizing usage, with the first call with NULL Data used to gather the size requirements, at which point a buffer can be created and used in a second call that would then fill the Data field.

This DDI should only ever be called for VFs that are currently paused.

Eventually, when there is no more need for migration configuration on this VF,

NTSTATUS DxgkDdiEndLiveMigration(
    HANDLE  hAdapter,
    UINT    vfIndex
    );
will be called. All scheduling and state should return to a non-migrating configuration.

### Live migration Start Receive-Side
On the receive side, the immutable data will come in and directly be passed to the driver through

typedef struct DXGK_GPUP_RESTORE_IMMUTABLE_MIGRATION_DATA
{
	[in]     UINT      vfIndex;
	[in]     UINT64    DataSize;
	[in]     BYTE *    Data;
};
NTSTATUS DxgkDdiRestoreImmutableMigrationData(
    HANDLE                                        hAdapter,
    DXGK_GPUP_RESTORE_IMMUTABLE_MIGRATION_DATA *  pArgs
    );
This DDI is only called once, unlike the save side, as it will have all the data needed to present to the KMD a full data buffer. The driver should take that data and apply it to the VF being constructed and any tracking for it, and the data invariants necessary for successful restore should be validated.

This buffer is the content that was filled on the source side in DxgkDdiSaveImmutableMigrationData, so that data should be tracked in a common type. There should also be a versioning scheme implemented in the content data if there is a potential that the data may need to change with new drivers, and this may be a part of the version checking done on the target.

If the data indicates that the target system is not configured properly to have the VF migrated from the source, it should first report through the DxgkCbLogEtwEvent with the GUID_DxgkAzureTriageEvent identifier specific details on what failed validation so the issue can be triaged and corrected. Then it should return from this DDI call with the error: STATUS_OBJECT_TYPE_MISMATCH.

This DDI should only ever be called for VFs that are currently paused.

### Iterative Restore / Receive
Again, the scatter paging will operate in an iterative manner, but this time without the calls to inspect the dirty bitplane associated to the framebuffer reserved by the VF (since the dirty bitplane on the target will be constructed by the paging) and the direction of paging is reversed. Content in the buffers received will be transferred to the VRAM, with the placement of the pages dictated

### Live migration End Receive-Side
Once the migration is coming to an end, the driver will be given the final package of state to restore. This should provide all the content that was left for the driver to transfer over for restoration of it's state and tracking and for the remaining restoration of the VF state.

typedef struct DXGK_GPUP_RESTORE_MUTABLE_MIGRATION_DATA
{
	[in]     UINT      vfIndex;
	[in]     UINT64    DataSize;
	[in]     BYTE *    Data;
};
NTSTATUS DxgkDdiRestoreMutableMigrationData(
    HANDLE                                      hAdapter,
    DXGK_GPUP_RESTORE_MUTABLE_MIGRATION_DATA *  pArgs
    );
This DDI should only ever be called for VFs that are currently paused.

After this call, there will be a call to EndLiveMigration to let the target side know to clean up any state around the live migration, including restoration of normal VF scheduling.

## Communications with the UMED
The UMED interface will be extended with the IGPUPMigration interface to expose additional ability to save and validate content during a live migration.

HRESULT SaveImmutableGpup(
    [in]     PLUID     DeviceLuid,
    [in,out] UINT64 *  Length,
    [in,out] BYTE *    SaveBuffer
    );

HRESULT RestoreImmutableGpup(
    [in] PLUID   DeviceLuid,
    [in] UINT64  Length,
    [in] BYTE *  RestoreBuffer
    );
During the live migration preparation actions where the KMD is called similarly, the UMED will have the opportunity to send over any information that may be useful to preparation of the UMED for the migration or validation that the environment supports the migration at the UMED level. It is an optional interface for UMEDs with the standard interface contracts for the UMED (threading and process context, restricted OS exposure, ...). It's calling pattern mimics the KMD DDIs, with the 2-phase save. There are no state flags in these calls, like other save/restore UMED interfaces) as these should be valid and constant throughout the life of the device and it's LUID.

The mutable state of the UMED is transferred in the existing Save/Restore interface. This interface has been blocked in the past from executing with GPU-P drivers, but will be unblocked when the KMD reports support for LiveMigration. This tying of UMED callout function and KMD capability is intentional. Live migration is how we implement quick migration for the virtualization of these devices. The same sequence of tasks will be done, and you can conceive of the quick migration (a.k.a. Save/Restore) as the special case of live migration where there is no active transfer. A UMED that supports Save/Restore will still need to have a KMD that supports the live migration DDIs, and similarly, the UMED must be aware of the IGPUPMigration interface and evaluate whether it is necessary in it's design before the KMD could live migrate.

## Virtualization of Interrupts
The physical addressing of the guest interrupt management has to be virtualized in order to properly service MSI-X table access as the underlying hardware changes. The MSI-X interrupt table must be intercepted by the UMED for all drivers that support live migration, and any reads or writes to the Message Upper Address and Message Address fields need to map to the actual HW values. DxgKrnl will maintain the mapping of the virtualized (or guest) address and perform the substitution where needed in the call stack.

The OS will manage the virtualization / mapping of the guest physical addresses that table reads or writes may refer to guest-side with the host physical addresses needed for actual interrupt servicing. This is a common path and will not need separate UMED implementation or kernel forwarding. The UMED will not be notified when the table is intercepted. The only requirement for the UMED is that the mitigations for the device need to be set for the BAR pages of the table.

In the kernel, though, we will want the KMD to service the actual writes. There should never be a need for a read because the writes will be tracked locally (in virtualized / guest-translated form) by the user-mode so they don't require the expensive kernel jump. This tracking will migrate with the virtual device.

typedef struct DXGK_INTERRUPT_TABLE_ENTRY
{
    UINT64  MessageAddress;
    UINT32  MessageData;
    UINT32  VectorControl;
};
typedef struct DXGK_GPUP_WRITE_VIRTUALIZED_MSIX
{
    [in] UINT                       vfIndex;
    [in] INT16                      InterruptTableIndex;
    [in] DXGKINTERRUPT_TABLE_ENTRY  WriteValue;
};
NTSTATUS DxgkDdiWriteVirtualizedInterrupt(
    HANDLE                              hAdapter,
    DXGK_GPUP_WRITE_VIRTUALIZED_MSIX *  pArgs
    );
For WriteValue, here MessageAddress, MessageData, and VectorControl refer to the standard MSI-X table structure, as described in section 6.8 of the PCI Local Bus Specification. InterruptTableIndex refers to the specific index of entry to reference.

## Heterogenous partitioning and same-GPU defrag or page-based reserve
An important benefit of live migration is the vast improvements of the cluster utilization it allows with intelligent management of virtualization residency. Partial residency hosts can be consolidated through migration and cluster resources repurposed for maximal availability.

When we create a vGPU, the current framebuffer mapping DDI SetVirtualGpuResources assumes that the framebuffer backing it is contiguous, which is how we have performed the allocation/reserve in the past. However, contiguous allocation of heterogenous sizes suffers fragmentation issues and utilization of the VRAM can be suboptimal.

In many ways, the defragmentation of clusters and the defragmentation on a given GPU are the same logical operation – moving of device virtualized content to merge unused physical resources for better allocation availability. But when you are looking to defragment on a single GPU around the specific constraint of memory reserve, some optimizations arise.

First, the hardware may perform a full two-phase translation of VRAM access of the guest, with page table mapping in the second phase. The contiguous reserve that has been used only ever required a second phase that could perform an offset increment and end validation, but if there is mapped addressing of sufficient granularity, then there is no fragmentation issue. In particular, if the page size of the machine satisfies:

::::image type="content" source="images/PageSize1.png" alt-text="Diagram illustrating ???????????????????.":::

so that:

::::image type="content" source="images/PageSize2.png" alt-text="Diagram illustrating ???????.":::

then any combination of partitions on the framebuffer will be evenly mappable in pages. To support this functionality, there is a new SetVirtualGpuResources2 DDI:

struct DXGK_GPU_PHYSICAL_RESERVE_DESCRIPTOR
{
    [In] HANDLE  DriverAllocationHandle;
    [in] HANDLE  MemoryBasis
};
struct DXGK_SETVIRTUALGPURESOURCES2
{
    [in] ULONG                                   vfIndex;
    [in] ULONG                                   SegmentCount;
    [in] DXGK_GPU_PHYSICAL_RESERVE_DESCRIPTOR *  SegmentDescriptors[SegmentCount];
};
NTSTATUS DxgkDdiSetVirtualGpuResources2(
    HANDLE                          hAdapter,
    DXGK_SETVIRTUALGPURESOURCES2 *  pArgs
    );
A Physical Reserve Descriptor describes the MemoryBasis and DriverAllocationHandle that represent the vGPU's VRAM for a specific SegmentId (which will always refer to a local memory segment here).

NOTE: the MemoryBasis here will have offset and sizes aligned to the SetVGPUResourcesPageSize reported by the driver above. This is in addition to any other alignement constraints that MemoryBasis be under through other DDIs.

This DDI may be used to configure multiple (SegmentCount many) segments at once, arrayed here under the SegmentDescriptors.

This will be called when the ScatterMapReserve cap is set, to allow the mapping of the 2nd phase of translation around the segments of this vGPU.

We will call this DDI prior to the first power on of the VF, after creation.

Also note that the allocations that represent the reserve will also have possibly-scatter-mapped GPUVA due to the noncontiguity, so this is another place where the scatter mapping will first execute (particularly in the fill-zero operation for reserve preparation) outside the migration transfers of dirty pages.

When a driver does not report support for the scatter mapping of reserve, there will be times when reserve must be defragmented. In these cases, multiple other VFs will need to be paused, have their content moved, and then the VF can be unpaused again to access the framebuffer. In order to support these devices, we expose the following support DDI:

struct DXGK_SETVIRTUALFUNCTIONPAUSESTATE
{
    [in] ULONG    vfIndex;
    [in] BOOLEAN  Pause;
};
NTSTATUS DxgkDdiSetVirtualFunctionPauseState(
    HANDLE                               hAdapter,
    DXGK_SETVIRTUALFUNCTIONPAUSESTATE *  pArgs
    );
Here, when Pause is not FALSE, the VF identified should be removed from VF scheduling. When Pause is FALSE, the VF should be scheduled according to the state of the VF as if this DDI had not been called. In other words, the DDI takes it’s effect when Pause is not FALSE, but when FALSE is passed, that effect is removed and the natural state of the VF should be honored from other interactions.

### DDI Sync and IRQL Contexts

| DDI | Sync Level | IRQL |
| --- | --- | --- |
| DxgkDdiPrepareLiveMigration | 0 | PASSIVE |
| DxgkDdiEndLiveMigration | 0 | PASSIVE |
| DxgkDdiSaveImmutableMigrationData | 0 | PASSIVE |
| DxgkDdiSaveMutableMigrationData | 0 | PASSIVE |
| DxgkDdiRestoreImmutableMigrationData | 0 | PASSIVE |
| DxgkDdiRestoreMutableMigrationData | 0 | PASSIVE |
| DxgkDdiWriteVirtualizedInterrupt | 0 | PASSIVE |
| DxgkDdiSetVirtualGpuResources2 | 0 | PASSIVE |
| DxgkDdiSetVirtualFunctionPauseState | 0 | PASSIVE |
| IGPUPMigration::SaveImmutableGpup | 0 | PASSIVE |
| IGPUPMigration::RestoreImmutableGpup | 0 | PASSIVE |

## Important Considerations for VF Scheduling
The efficiency of the transfer is strongly determined by the scheduling of the paging transfers on the PF. The more access to the paging engines of the device the PF can use to saturate the bus and get best throughput, the more performant the transfer in general and the paused transfer specifically. The more content that can be captured and sent over in a given time, the better - at least up to network saturation.

It would be preferrable to have the change in scheduling only affect the paging engine and no other device resource, but not all VF scheduling designs may allow this. At a minimum, it is desired that the scheduling:

only take budget from the VF being migrated or from unassigned VF schedule
not degrade performance for any other virtualizations on the machine
Note, on the target side these conditions can be much more easily met as the VF is paused the entire transfer and that whole budget is available. On the source side, it requires a balancing of the migration needs and the VM needs, with the ultimate need to meet the pause transfer goals

We want to work with partners to understand the capabilities of their VF scheduling better in this area and will look to validate responsiveness measures in the unrelated virtualizations.