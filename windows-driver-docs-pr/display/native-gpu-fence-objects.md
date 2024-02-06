---
title: Native GPU Fence Object
description: Notification of Actual Heap Base Addresses
keywords:
- WDDM, native GPU fence object
- WDDM, GPU fence synchronization object
- WDDM, hardware scheduling
ms.date: 04/08/2024
---

# Native GPU fence object

This article describes the GPU fence synchronization object that can be used for true GPU-to-GPU synchronization in GPU hardware scheduling stage 2. This feature is available starting in WDDM 3.1. Graphics driver developers should be familiar with WDDM 2.0 and GPU hardware scheduling stage 1.

## Existing versus new fence synchronization objects

### Existing monitored fence synchronization object

WDDM 2.x's [monitored fence synchronization object](context-monitoring.md) supports the following operations:

* CPU wait on a monitored fence value, either by polling using a CPU virtual address (VA), or by queuing a blocking wait inside *Dxgkrnl* that's signaled when the CPU observes the new monitored fence value.
* CPU signal of a monitored value.
* GPU signal of a monitored value by writing to the monitored fence GPU VA and raising "monitored fence signaled" interrupt to notify the CPU of the value update.

What isn't supported is a native on-the-GPU wait for a monitored fence value. Instead, the operating system implements this functionality on the CPU by holding off GPU work that's dependent on the waited value, and only releasing it to the GPU when the value is signaled.

### GPU native fence synchronization object

This article introduces an extension to the monitored fence object that supports the following additional features:

* GPU wait on a monitored fence value, which allows for high performance engine-to-engine synchronization without requiring a CPU roundtrip.
* Conditional interrupt notification only for GPU fence signals that have CPU waiters. This feature enables substantial power savings by enabling the CPU to enter low power state when all GPU work has been queued.
* Fence value storage in the GPU local memory (as opposed to system memory).

## GPU native fence sync object design

The following diagram illustrates the basic architecture of the GPU native fence object, focusing on synchronization object state that's shared between the CPU and the GPU.

::::image type="content" source="images/NativeFenceStorage.png" alt-text="Diagram illustrating the architecture of the GPU native fence object and the synchronization object state shared between the CPU and GPU.":::

The diagram includes two main components:

* Current value. This memory location contains the currently signaled 64-bit fence value. It is mapped and accessible to both the CPU (writeable from kernel mode, readable from both user and kernel mode) and GPU (readable and writeable using GPU virtual address). Sixty-four (64) bit writes to this value are required to be atomic from both the CPU and the GPU point of view. That is, updates to the high and low 32 bits can't be torn and should be visible at the same time. This concept is already present in the existing monitored fence object.

* Monitored value. This memory location contains the least currently-waited-on value by the CPU subtracted by 1. It is mapped and accessible to both the CPU (readable and writeable from kernel mode, no user mode access) and GPU (readable using GPU VA, no write access). The OS maintains the list of outstanding CPU waiters for a given fence object, and it updates the monitored value as waiters are added and removed. When there are no outstanding waiters, the value is set to UINT64_MAX. This concept is new to the GPU native fence sync object.

The next diagram illustrates how *Dxgkrnl* tracks outstanding CPU waiters on a specific monitored fence value, and what the monitored fence value is set to at a given point in time. CurrentValue and MonitoredValue are both 41, which means that the GPU has completed all tasks up to the fence value of 41, and the CPU isn't waiting on any fence value less than or equal to 41.

::::image type="content" source="images/cpuwaiters.png" alt-text="Diagram illustrating a fence object's CurrentValue (41) and MonitoredValue (41) when the least waited on fence value is 42.":::

The following diagram illustrates that the context management processor (CMP) on the GPU conditionally raises a CPU interrupt only if the new fence value is greater than monitored value (which means there are outstanding CPU waiters that can be satisfied with the newly written value).

::::image type="content" source="images/conditionalinterrupt.png" alt-text="Diagram illustrating the GPU's context management processor raising a CPU interrupt when CurrentValue's new fence value equals 42 and MonitoredValue equals 41.":::

When the CPU processes this interrupt, *Dxgkrnl* performs the following actions as illustrated in the next diagram:

* It unblocks CPU waiters that have been satisfied with the newly written fence.
* It advances the monitored value to correspond to the least outstanding waited on value subtracted by 1.

::::image type="content" source="images/unblockingcpuwaiters.png" alt-text="Diagram illustrating that Wait for fence 42 is satisfied so the least waited on value (MonitoredValue) now equals 42.":::

## Physical memory storage for current and monitored fence values

For a given fence object, current value and monitored value storage are stored in separate locations.

* Fence objects that are non-shareable have fence value storage for different fence objects within the same process packed in the same memory page. The values are packed according to the stride values specified in the native fence KMD caps described later in this article.

* Fence objects that are shareable have their current and monitored values placed in memory pages that are not shared with other fence objects.

### Current value

Current value can reside either in system memory or GPU local memory.

For system memory fences, the OS allocates current value storage from internal system memory pool.

For local memory fences, the OS allocates current value storage from local memory segment set specified in DXGK_NATIVE_FENCE_CAPS as described in the DDI section of this document.

Segments included in PreferredSegment must be CPU accessible (either explicitly marked CPU visible or accessible through CPU host aperture mapping), and GPU updates of the current value must be done as write through.

### Monitored value

Monitored value can also reside either in system or GPU local memory.

For system memory fences, the OS allocates current value storage from internal system memory pool.

For local memory fences, the OS allocates current value storage from local memory segment set specified in [**DXGK_NATIVE_FENCE_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_native_fence_caps) as described in the DDI section of this document.

When the OS CPU wait conditions change, it instructs KMD to update monitored value to a specified value via DxgkDdiUpdateMonitoredValues callback described later.

## Synchronization issues

Note that the previously described mechanism has an inherent race condition between the CPU and GPU reads and writes of the current value and the monitored value. If special care isn't taken, it's possible for the GPU to read a stale MonitoredValue and not raise an interrupt as expected by the CPU, or for a GPU engine to write a newer CurrentValue while the context management processor is in the middle of deciding the interrupt condition, and for the newer CurrentValue to not raise the interrupt as expected, or not being visible to the CPU as it fetches the current value.

### Synchronization within the GPU between the engine and CMP

For efficiency, many discrete GPUs implement the monitored fence signal semantics using shadow state that resides in the GPU's local memory between:

* The GPU engine executing the command buffer stream and conditionally raising a hardware signal to the context management processor.

* The GPU context management processor that decides whether a CPU interrupt should be raised.

In this case, the context management processor needs to synchronize memory access with the GPU engine performing memory write to the fence value. In particular, the operation of updating a shadow MonitoredValue should be ordered from the context management processor point of view using the following steps:

1. Write a new MonitoredValue (shadow GPU storage)
2. Execute a memory barrier to synchronize memory access with the GPU engine
3. Read CurrentValue:
   * If CurrentValue > MonitoredValue, raise a CPU interrupt.
   * If CurrentValue <= MonitoredValue, don't raise the CPU interrupt.

For this race condition to resolve properly, it's imperative that the memory barrier in step 2 function properly. There must not be any pending memory write operation to CurrentValue in step 3 originating from a command which hasn't seen the MonitoredValue update in step 1 (and would thus generate an interrupt if the fence written in step 3 was greater than the value updated in step 1).

### Synchronization between GPU and CPU

The CPU has to perform updates of MonitoredValue and reads of CurrentValue in a way that doesn't lose interrupt notification for in flight signals.

* When a new CPU waiter is added to the system, or if an existing CPU waiter is retired, the OS has to modify MonitoredValue.
* The OS uses DxgkDdiUpdateMonitoredValue to notify the GPU of a new monitored value.
* DxgkDdiUpdateMonitoredValue executes at the device interrupt level and is thus synchronized with the monitored fence signaled ISR.
* DxgkDdiUpdateMonitoredValue guarantees that CurrentValue read by any processor core after DdiUpdateMonitoredValue returns was written by the GPU context management processor after having observed the new MonitoredValue.
* Upon DxgkDdiUpdateMonitoredValue return, the OS re-samples CurrentValue and satisfies any waiters that are unblocked by the new CurrentValue.
Note that it's perfectly acceptable for the CPU to observe a newer CurrentValue than the one used by the GPU to decide whether to raise the interrupt. This would occasionally result in an interrupt notification that doesn't unblock any waiters.

What isn't acceptable is for the CPU to not receive an interrupt notification for the most recent CurrentValue update that was monitored (i.e., CurrentValue > MonitoredValue.)

## Querying native fence feature enablement in OS

The following interfaces are introduced for a KMD to query whether the OS has enabled the native fence feature:

* [**DXGKCB_FEATURE_NATIVEFENCE_CAPS_1**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_feature_nativefence_caps_1)
* [**DXGKARGCB_FEATURE_NATIVEFENCE_CAPS_1**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_feature_nativefence_caps_1)
* [**DXGKCBINT_FEATURE_NATIVEFENCE_1**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkcbint_feature_nativefence_1)

Like the hardware scheduling stage 1 and hardware flip queue features, drivers must query whether the native fence feature is enabled in the OS during driver initialization. However, unlike before, the OS leverages the added [**IsFeatureEnabled**]() interface to control whether the feature is enabled. As a result, drivers must implement this interface. For more information, see [Detecting whether a feature is enabled]().

Before KMD advertises native fence support in [**DXGK_VIDSCHCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps), KMD is expected to implement the **IsFeatureEnabled** interface and query whether the OS has enabled the [**DXGK_FEATURE_NATIVE_FENCE**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_id) feature. The OS fails adapter initialization if KMD advertises native fence support if the feature isn't enabled by the OS.

The OS implements the added [**DXGKCB_FEATURE_NATIVEFENCE_CAPS_1**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_feature_nativefence_caps_1) interface table dedicated to version 1 of **DXGK_FEATURE_NATIVE_FENCE**. KMD must query this feature interface table to determine the OS's capabilities. In future OS releases, the OS might introduce future versions of this interface table, detailing support for new capabilities.

### Sample driver code for querying support

``` C++

DXGK_FEATURE_INTERFACE      FeatureInterface;

struct FEATURE_RESULT
{
    bool Enabled;
    DXGK_FEATURE_VERSION Version;
};

// Driver internal cache for state & version of queried features
struct FEATURE_STATE
{
    struct
    {
        UINT NativeFenceEnabled             : 1;
    };

    DXGK_FEATURE_VERSION NativeFenceVersion = 0;

    // Interfaces
    DXGKCBINT_FEATURE_NATIVEFENCE_1 NativeFenceInterface = {};

    // Interface queried values
    DXGKARGCB_FEATURE_NATIVEFENCE_CAPS_1 NativeFenceOSCaps1 = {};
};

// Helper function to query OS's feature enabled interface
FEATURE_RESULT IsFeatureEnabled(
    DXGK_FEATURE_ID FeatureId
    )
{
    FEATURE_RESULT Result = {};

    //
    // If the feature interface functionality is available (e.g. supported by the OS)
    //
    DXGKARGCB_ISFEATUREENABLED2 Args = {};
    Args.FeatureId = FeatureId;

    if(NT_SUCCESS(FeatureInterface.IsFeatureEnabled(DxgkInterface.DeviceHandle, &Args)))
    {
        Result.Enabled = Args.Result.Enabled;
        Result.Version = Args.Result.Version;
    }

    return Result;
}

// Actual code to query whether OS has enabled Native Fence support and corresponding OS caps
FEATURE_RESULT FeatureResult = IsFeatureEnabled(DXGK_FEATURE_NATIVE_FENCE);
FEATURE_STATE FeatureState = {};
FeatureState.NativeFenceEnabled = !!FeatureResult.Enabled;

if (FeatureResult.Enabled)
{
    // Query OS caps for native fence feature, using the feature interface
    DXGKARGCB_QUERYFEATUREINTERFACE QFIArgs = {};
    QFIArgs.FeatureId = DXGK_FEATURE_NATIVE_FENCE;
    QFIArgs.Interface = &FeatureState.NativeFenceInterface;
    QFIArgs.InterfaceSize = sizeof(FeatureState.NativeFenceInterface);
    QFIArgs.Version = FeatureResult.Version;

    Status = FeatureInterface.QueryFeatureInterface(DxgkInterface.DeviceHandle, &QFIArgs);
    if(NT_SUCCESS(Status))
    {
        FeatureState.NativeFenceVersion = FeatureResult.Version;
        Status = FeatureState.NativeFenceInterface.GetOSCaps(&FeatureState.NativeFenceOSCaps1);
        NT_ASSERT(NT_SUCCESS(Status));
    }
    else
    {
        // We should always succeed getting an interface from a successfully
        // negotiated feature + version.
        NT_ASSERT(FALSE);
    }
}
```


7. Native fence caps

The following interfaces are updated or introduced to query native fence caps:

* The **NativeGpuFence** field is added to [**DXGK_VIDSCHCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps)

  If the OS has enabled the [**DXGK_FEATURE_NATIVE_FENCE**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_id) feature, the driver can declare support for native GPU fence functionality during adapter initialization by setting the [**DXGK_VIDSCHCAPS::NativeGpuFence**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps) bit to 1.

* *Dxgkrnl* exposes this feature to user mode via the added corresponding [**D3DKMT_WDDM_3_1_CAPS::NativeGpuFenceSupported**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmt_wddm_3_1_caps) structure/bit. **KMTQAITYPE_WDDM_3_1_CAPS** is added to [**KMTQUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype).

* **DXGKQAITYPE_NATIVE_FENCE_CAPS** is added to [**DXGK_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype).

* **KMTQAITYPE_WDDM_3_1_CAPS** is added to [**KMTQUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype).

* The following entities are added for a KMD to use to indicate its support capabilities for the native GPU fence feature:

  * The [**DXGK_NATIVE_FENCE_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi/ns-d3dkmddi-dxgk_native_fence_caps) structure describes the GPU's native fence capabilities.
  * KMD returns its populated **DXGK_NATIVE_FENCE_CAPS** structure when its [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) function is called with the added [**DXGKQAITYPE_NATIVE_FENCE_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) query adapter info type.

## KMD DDIs to create, open, close, and destroy a native fence object

The following DDIs are introduced to create, open, close, and destroy a native fence object. *Dxgkrnl* calls these DDIs on behalf of user-mode components. *Dxgkrnl* calls them only if the OS has enabled the DXGK_FEATURE_NATIVE_FENCE feature.

* [**DxgkDdiCreateNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createnativefence)/[**DXGKARG_CREATENATIVEFENCE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_createnativefence)
* [**Dxgk**DxgkDdiCreateNativeFence****](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_opennativefence)/[**DXGKARG_OPENNATIVEFENCE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_opennativefence)
* [**Dxgk**DxgkDdiCloseNativeFence****](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_closenativefence)/[**DXGKARG_CLOSENATIVEFENCE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_closenativefence)
* [**Dxgk**DxgkDdiDestroyNativeFence****](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroynativefence)/[**DXGKARG_DESTROYNATIVEFENCE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_destroynativefence)

The following DDIs were updated to support native fence objects:

* The following members were added to [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data). Drivers that support native GPU fence objects should implement the functions and provide *Dxgkrnl* with pointers to them via this structure.

  * PDXGKDDI_CREATENATIVEFENCE    DxgkDdiCreateNativeFence;  // added in WDDM 3.1
  * PDXGKDDI_DESTROYNATIVEFENCE   DxgkDdiDestroyNativeFence; // added in WDDM 3.1
  * PDXGKDDI_OPENNATIVEFENCE      DxgkDdiCreateNativeFence;  // added in WDDM 3.2
  * PDXGKDDI_CLOSENATIVEFENCE     DxgkDdiCloseNativeFence;   // added in WDDM 3.2

### Global and local handles for shared fences

Imagine process A creates a shared native fence and process B later opens this fence.

* When process A creates the shared native fence, *Dxgkrnl* calls [**DxgkDdiCreateNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createnativefence) with the adapter driver handle on which this fence is created. The fence handle created and returned in **hGlobalNativeFence** is the global fence handle.

* *Dxgkrnl* subsequently follows up with a call to [**DxgkDdiOpenNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_opennativefence) to open a process A-specific local handle (**hLocalNativeFence*A***).

* When process B opens the same shared native fence, *Dxgkrnl* calls **DxgkDdiOpenNativeFence** to open a process B-specific local handle (**hLocalNativeFence*B***)

* If process A destroys its shared native fence instance, *Dxgkrnl* sees that there is still a pending reference to this global fence, so only calls [**DxgkDdiCloseNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_closenativefence)(**hLocalNativeFence*A***) for the driver to cleanup process A-specific structures. The **hGlobalNativeFence** handle still exists.

* When process B destroys its fence instance, *Dxgkrnl* calls **DxgkDdiCloseNativeFence**(**hLocalNativeFence*B***) and subsequently [**DxgkDdiDestroyNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroynativefence)(**hGlobalNativeFence**) to allow KMD to destroy its global fence data.

### GPU VA mappings in paging process address space for CMP use

The KMD sets the [**DXGK_NATIVE_FENCE_CAPS::MapToGpuSystemProcess**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_native_fence_caps) cap on hardware that requires native fence GPU VAs to be also mapped into the GPU paging process address space. A set **MapToGpuSystemProcess** bit instructs the OS to create GPU VA mappings in the paging process address space for the native fence's CurrentValue and MonitoredValue for use by the context management processor. These GPU VAs are subsequently passed to [**DxgkDdiCreateNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createnativefence) as [**DXGKARG_CREATENATIVEFENCE::CurrentValueSystemProcessGpuVa**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_createnativefence) and **MonitoredValueSystemProcessGpuVa**.

9. D3DKMT kernel APIs for native fences

The following D3DKMT kernel APIs are introduced to create, open, close and destroy a native fence object.

* [**D3DKMTCreateNativeFence**](/windows-hardware/drivers/ddi/d3dkmthk/nc-d3dkmthk-d3dkmtcreatenativefence)
9.1. D3DKMTCreateNativeFence

typedef enum _D3DDDI_NATIVEFENCE_TYPE
{
    D3DDDI_NATIVEFENCE_TYPE_DEFAULT = 0,   // Full CPU and GPU interoperability.
    D3DDDI_NATIVEFENCE_TYPE_INTRA_GPU = 1, // Special fence type for engine-engine synchronization, which
                                           // doesn't support any CPU access or CPU wait/signal operations
} D3DDDI_NATIVEFENCE_TYPE;

typedef struct _D3DDDI_NATIVEFENCEMAPPING
{
    D3DKMT_PTR(VOID*,                       CurrentValueCpuVa);  // Read-only mapping of the current value for the CPU
    D3DKMT_ALIGN64 D3DGPU_VIRTUAL_ADDRESS   CurrentValueGpuVa;   // Read/write mapping of the current value for the GPU in the current process address space
    D3DKMT_ALIGN64 D3DGPU_VIRTUAL_ADDRESS   MonitoredValueGpuVa; // Read/write mapping of the monitored value for the GPU in the current process address space
    D3DKMT_ALIGN64 BYTE                     Reserved[32];
} D3DDDI_NATIVEFENCEMAPPING;

typedef struct _D3DDDI_NATIVEFENCEINFO
{
    D3DKMT_ALIGN64 UINT64                   InitialFenceValue;  // in: initial fence value.
    UINT                                    EngineAffinity;     // in: Defines physical adapters where the GPU VA is mapped
    D3DDDI_NATIVEFENCE_TYPE                 Type;               // in: Type of the fence
    D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS      Flags;              // in: Flags.
    D3DDDI_NATIVEFENCEMAPPING               NativeFenceMapping; // out: process mapping information for the native fence
    D3DKMT_ALIGN64 BYTE                     Reserved[28];
} D3DDDI_NATIVEFENCEINFO;

#define D3DDDI_NATIVE_FENCE_PDD_SIZE 64

typedef struct _D3DKMT_CREATENATIVEFENCE_FLAGS 
{
    union
    {
        struct 
        {
            UINT Reserved : 32;
        };
        UINT Value;
    };
}D3DKMT_CREATENATIVEFENCE_FLAGS;

typedef struct _D3DKMT_CREATENATIVEFENCE
{
    D3DKMT_HANDLE                  hDevice;                                         // in:  Handle to the device.
    D3DKMT_HANDLE                  hSyncObject;                                     // out: Handle to sync object in this process.
    BYTE                           PrivateDriverData[D3DDDI_NATIVE_FENCE_PDD_SIZE]; // in/out: Private driver data to pass to KMD CreateNativeFence call,
                                                                                    //         and copy back to UMD
    D3DDDI_NATIVEFENCEINFO         Info;                                            // in/out: Attributes of the synchronization object.
    D3DKMT_CREATENATIVEFENCE_FLAGS Flags;
    BYTE                           Reserved[28];
} D3DKMT_CREATENATIVEFENCE;

EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTCreateNativeFence(_Inout_ D3DKMT_CREATENATIVEFENCE*);

D3DKMTCreateNativeFence is used by runtime to create a native GPU fence object on a particular device.

D3DDDI_NATIVEFENCEMAPPING contains native GPU fence address mappings in the caller process address space

CurrentValueCpuVa is CPU read-only and used by user mode components to poll the native fence CurrentValue.
CurrentValueGpuVa is GPU read/write and used by the GPU engine to read or write to the native fence CurrentValue as a fence signal operation.
MonitoredValueGpuVa is GPU read/write and used by GPU engine to check whether conditional CPU interrupt should be raised

9.2. D3DDDI_NATIVEFENCE_TYPE

D3DDDI_NATIVEFENCE_TYPE dictates the type of native fence that the OS creates. They differ in functionality, performance characteristics and storage requirements for **CurrentValue** and **MonitoredValue**:

| Type | CurrentValue | MonitoredValue | Supports Cross-process Sharing on CPU? | Supports Cross-Adapter Sharing | UM CPUVA CurrentValue | KM CPUVA CurrentValue | GPU VA CurrentValue | CMPVA CurrentValue | UM MonitoredValue | KM MonitoredValue | GPU VA MonitoredValue | Use-Case |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D3DDDI_NATIVEFENCE_TYPE_DEFAULT | Sysmem | Sysmem | Yes | Yes | ReadOnly | Read/Write | Read/Write | Read/Write | NA | Write | ReadOnly (or Read/Write) | Read/Write | Application fences with reduced CPU interrupts. GPU waiter is unblocked without waking up CPU |
| D3DDDI_NATIVEFENCE_TYPE_DEFAULT (OPTIMIZED) | Sysmem | VRAM | Yes | Yes | ReadOnly | Read/Write | Read/Write | Read/Write | NA | Write | ReadOnly (or Read/Write) | Read/Write | Same as Type 0 but with reduced PCI bus traffic as MV reads are local to GPU. GPU signal command completes faster because of this reduced latency (throughput++). |
| D3DDDI_NATIVEFENCE_TYPE_INTRA_GPU | VRAM | VRAM | Yes | No | NA | NA | Read/Write | Read/Write | NA | NA | ReadOnly (or Read/Write) | Read/Write | Command buffer level (not application visible) synchronization within same gpu. Read/Write to fence value (CV) is local and so signal/unblock operations are fast |


9.2.1. D3DDDI_NATIVEFENCE_TYPE_DEFAULT
Supported in Win2024 RTM

This fence type supports all existing D3DKMT sync object Wait/Signal from CPU/GPU operations.

Both CurrentValue and MonitoredValue storage for this fence type will be allocated in system memory segment

9.2.2. D3DDDI_NATIVEFENCE_TYPE_DEFAULT (Optimized)
Optimized version of D3DDDI_NATIVEFENCE_TYPE_DEFAULT, in which the MonitoredValue storage can be allocated in VRAM, which will speed up reads of MonitoredValue from the GPU engine

This optimization is not exposed to UMD, but rather *Dxgkrnl* and KMD will decide whether the default fence type can be optimized by allocating MonitoredValue storage in VRAM

MonitoredValue storage allocated in VRAM may still be demoted to system memory if the system is under local memory pressure

If OS supports this fence type, it will set SupportOptimizedDefaultFenceType to TRUE in DXGKARGCB_FEATURE_NATIVEFENCE_CAPS_1 feature interface table. KMD is expected to query the feature interface table during driver initialization to determine this OS capability

This capability will not be supported by OS in Win 2024 RTM

More details on how KMD can choose whether to allocate MonitoredValue in sysmem or VRAM for D3DDDI_NATIVEFENCE_TYPE_DEFAULT fences will be added soon. (todo: This will tie in with the concept of allocating fence storage using vidmm standard allocations).

9.2.3. D3DDDI_NATIVEFENCE_TYPE_INTRA_GPU
D3DDDI_NATIVEFENCE_TYPE_INTRA_GPU fence doesn't support any CPU operations i.e OS will not allow user mode to queue wait and signals to this fence object

Hence, this type can't be used for DX application fences which must support CPU wait and signal semantics. This type is mainly used for internal UMD fences for synchronization between GPU engines and creating this as a D3DKMT native fence object provides visibility into these fences for tools such as gpuview and debugging

Supported segment for this fence must be a non-CPU visible local memory segment

Storage allocated in local memory may still be demoted to system memory if the system is under local memory pressure

If OS supports this fence type, it will set SupportIntraGpuFenceType to TRUE in DXGKARGCB_FEATURE_NATIVEFENCE_CAPS_1 feature interface table. KMD is expected to query the feature interface table during driver initialization to determine this OS capability

This capability will not be supported by OS in Win 2024 RTM

9.3. D3DKMTOpenNativeFenceFromNTHandle
typedef struct _D3DKMT_OPENNATIVEFENCEFROMNTHANDLE
{
    D3DKMT_PTR(HANDLE,                  hNtHandle);         // in : NT handle for the shared fence object.
    D3DKMT_HANDLE                       hDevice;            // in : Device handle to open this fence object on.
    UINT                                EngineAffinity;     // in: Defines physical adapters where the GPU VA is mapped
    D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS  Flags;              // in: Flags.
    D3DKMT_HANDLE                       hSyncObject;        // out: Handle to the opened fence object
    D3DDDI_NATIVEFENCEMAPPING           NativeFenceMapping; // out: process mapping information for the fence object
    BYTE                                Reserved[32];
} D3DKMT_OPENNATIVEFENCEFROMNTHANDLE;

EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTOpenNativeFenceFromNtHandle(_Inout_ D3DKMT_OPENNATIVEFENCEFROMNTHANDLE*);
D3DKMTOpenNativeFenceFromNTHandle is used by runtime to open an existing shared native fence on a different device or process.

If the native fence is being opened on a different device of the same process, then the NativeFenceMapping will contain the same VAs as the original native fence. If it is being opened on a different process, then the NativeFenceMapping will contain new VAs mapped in the new process address space.

9.4. D3DKMTDestroySynchronizationObject
Runtime will use the exiting D3DKMTDestroySynchronizationObject API to free an existing native fence object.


10. Native HWQueueProgressFence
typedef struct _D3DDDI_CREATEHWQUEUEFLAGS
{
    union
    {
        struct
        {
            UINT    DisableGpuTimeout   : 1;      // 0x00000001
            UINT    NoBroadcastSignal   : 1;      // 0x00000002
            UINT    NoBroadcastWait     : 1;      // 0x00000004
            UINT    NoKmdAccess         : 1;      // 0x00000008
            UINT    UserModeSubmission  : 1;      // 0x00000010
            UINT    NativeProgressFence : 1;      // 0x00000020
            UINT    Reserved            :26;      // 0xFFFFFFD0
        };
        UINT Value;
    };
} D3DDDI_CREATEHWQUEUEFLAGS;

On supported systems, OS will update the HWQueueProgressFence to a native fence. A new NativeProgressFence flag is added in DxgkDdiCreateHwQueue to indicate to KMD that the handle DXGKARG_CREATEHWQUEUE::hHwQueueProgressFence points to the driver handle of a native GPU fence object previously created using [**DxgkDdiCreateNativeFence**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createnativefence).

11. Native fence signaled interrupt

The following changes are made to the interrupt mechanism to support native fence signaled interrupt:

* The [**DXGK_INTERRUPT_TYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_interrupt_type) enum is updated to include a **DXGK_INTERRUPT_NATIVE_FENCE_SIGNALED** interrupt type.
* The [**DXGKARGCB_NOTIFY_INTERRUPT_DATA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data) structure is updated to include a **NativeFenceSignaled** member.

The native fence signaled interrupt ([**DXGKARGCB_NOTIFY_INTERRUPT_DATA.NativeFenceSignaled**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_notify_interrupt_data)) is used to inform the OS that a set of native fence GPU objects monitored by the CPU were signaled on a GPU engine. If the GPU is able to determine the exact subset of objects with active CPU waiters, it passes this subset via **pSignaledNativeFenceArray**. The handles in this array must be valid **hGlobalNativeFence** handles that *Dxgkrnl* passed to KMD in **DxgkDdiCreateNativeFence**. Passing a handle to a destroyed native fence object causes a bugcheck.

The GPU can pass a NULL **pSignaledNativeFenceArray** under the following conditions:

* The GPU is unable to determine the exact subset of objects with active CPU waiters.
* Multiple signal interrupts are collapsed together making it hard to determine the signaled set with active waiters.

A NULL value instructs the OS to scan all outstanding native GPU fence object waiters.

The contract between the OS and the driver here is as follows. If the OS has an active CPU waiter (as expressed by **MonitoredValue**), and the GPU engine signaled the object to the value that requires a CPU interrupt, the GPU must react by taking either of the following actions:

* Including this native fence handle in the **pSignaledNativeFenceArray**.
* Raising a **NativeFenceSignaled** interrupt with a NULL **pSignaledNativeFenceArray**.

By default, when KMD [raises this interrupt](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_notify_interrupt) with a NULL **pSignaledNativeFenceArray**, *Dxgkrnl* only scans all pending native fence waiters and doesn't scan legacy monitored fence waiters. On hardware that can't distinguish between legacy DXGK_INTERRUPT_MONITORED_FENCE_SIGNALED and DXGK_INTERRUPT_NATIVE_FENCE_SIGNALED, the KMD can always raise only the introduced DXGK_INTERRUPT_NATIVE_FENCE_SIGNALED interrupt with **pSignaledNativeFenceArray** = NULL and **EvaluateLegacyMonitoredFences** = 1, which indicates to the OS to scan all waiters (legacy monitored fence waiter & native fence waiters).



typedef struct _DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS
{
    union
    {
        struct
        {
            UINT            ValidPhysicalAdapterMask : 1; // 0x00000001
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
            UINT            HsyncFlipCompletion      : 1; // 0x00000002
            UINT            EvaluateLegacyMonitoredFences  : 1; // 0x00000003
            UINT            Reserved                 :29; // 0xFFFFFFFB
#else
            UINT            Reserved                 :31; // 0xFFFFFFFE
#endif
        };
        UINT                Value;
    };
} DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS;



12. DdiUpdateMonitoredValues: Instructing KMD to update a batch of MonitoredValues
typedef struct _DXGKARG_UPDATEMONITOREDVALUES
{
    _Field_size_(NumFences)
    HANDLE*                             NativeFenceArray;          // in: Native fence handles.
    _Field_size_(NumFences)
    UINT64*                             UpdatedValueArray;         // in: New monitored values.
    _Field_size_(NumFences)
    void**                              MonitoredValueKernelCpuVa; // in: Read/write kernel mode CPU VA of the monitored value.
    UINT                                NumFences;                 // in: Number of native fences that OS updates monitored values of.
    DXGKARG_UPDATEMONITOREDVALUES_FLAGS Flags;
    BYTE                                Reserved[28];
} DXGKARG_UPDATEMONITOREDVALUES;

typedef _In_ CONST DXGKARG_UPDATEMONITOREDVALUES*   IN_CONST_PDXGKARG_UPDATEMONITOREDVALUES;

typedef
    _Check_return_
    _Function_class_DXGK_(DXGKDDI_UPDATEMONITOREDVALUES)
    _IRQL_requires_max_(PROFILE_LEVEL - 1)
NTSTATUS
APIENTRY
DXGKDDI_UPDATEMONITOREDVALUES(
    IN_CONST_PDXGKARG_UPDATEMONITOREDVALUES pUpdateMonitoredValues
    );

typedef struct _DRIVER_INITIALIZATION_DATA {
...
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
    PDXGKDDI_UPDATEMONITOREDVALUES          DxgkDdiUpdateMonitoredValues;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
} DRIVER_INITIALIZATION_DATA, *PDRIVER_INITIALIZATION_DATA;
DxgkDdiUpdateMonitoredValues executes at the device interrupt level and is thus synchronized with the monitored fence signaled ISR. DxgkDdiUpdateMonitoredValues implementation must guarantee that CurrentValue read by any processor core after the call returns was written by the GPU context management processor after having observed NewMonitoredValue. DxgkDdiUpdateMonitoredValues is expected to write the UpdatedValueArray values to the location specified by MonitoredValueGpuVa while honoring the synchronization contract.

OS only guarantees that the MonitoredValueKernelCpuVa pointer is valid for the duration of this DDI call, and not before or after it. Hence, KMD must never cache this pointer for use elsewhere.

13. DdiUpdateCurrentValuesFromCpu: Instructing KMD to update a batch of CurrentValues

typedef struct _DXGK_UPDATECURRENTVALUESFROMCPU_FLAGS
{
    union
    {
        struct
        {
            UINT AlwaysSignaled   : 1;
            UINT NotificationOnly : 1;
            UINT Reserved         : 30;
        };
        UINT Value;
    };
} DXGK_UPDATECURRENTVALUESFROMCPU_FLAGS;

typedef struct _DXGKARG_UPDATECURRENTVALUESFROMCPU
{
    DXGK_UPDATECURRENTVALUESFROMCPU_FLAGS Flags;
    UINT                                  NumFences;               // in: Number of native fences that OS updates current values of.
    _Field_size_(NumFences)
    HANDLE*                               NativeFenceArray;        // in: Native fence handles.
    _Field_size_(NumFences)
    UINT64*                               UpdatedValueArray;       // in: New current values.
    _Field_size_(NumFences)
    void**                                CurrentValueKernelCpuVa; // in: Read/write kernel mode CPU VA of the current value.
    BYTE                                  Reserved[28];
} DXGKARG_UPDATECURRENTVALUESFROMCPU;

typedef _In_ CONST DXGKARG_UPDATECURRENTVALUESFROMCPU*   IN_CONST_PDXGKARG_UPDATECURRENTVALUESFROMCPU;

typedef
    _Check_return_
    _Function_class_DXGK_(DXGKDDI_UPDATECURRENTVALUESFROMCPU)
    _IRQL_requires_(DISPATCH_LEVEL)
NTSTATUS
APIENTRY
DXGKDDI_UPDATECURRENTVALUESFROMCPU(
    IN_CONST_PDXGKARG_UPDATECURRENTVALUES pUpdateCurrentValuesFromCpu
    );

typedef struct _DRIVER_INITIALIZATION_DATA {
...
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
    PDXGKDDI_UPDATECURRENTVALUESFROMCPU      DxgkDdiUpdateCurrentValuesFromCpu;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
} DRIVER_INITIALIZATION_DATA, *PDRIVER_INITIALIZATION_DATA;
DxgkDdiUpdateCurrentValuesFromCpu is invoked by the OS to update the CurrentValue of a batch of native fences from the CPU. This DDI is used to support existing "signal fence from CPU" API semantics. Instead of Dxgkrnl writing a new CurrentValue, we ask the driver to write to CurrentValue in order to give drivers an opportunity to insert any required pre-write synchronization/barriers. The OS synchronizes CPU side updates and guarantees that the most up to date value is available to the DxgkDdiUpdateCurrentValuesFromCpu callback. After updating CurrentValue, driver must trigger the GPU to unblock hardware queues which were waiting on this fence and got unblocked with the update to CurrentValue. In a nutshell the steps to be followed by the driver are:

for i = 1 : NumFences
  1. Insert pre-write memory barrier if required
  2. write new value to CurrentValueCpuVa
  3. trigger GPU to unblock any HwQueues that got unblocked by the updated CurrentValue
end
OS only guarantees that the CurrentValueKernelCpuVa pointer is valid for the duration of this DDI call, and not before or after it. Hence, KMD must never cache this pointer for use elsewhere.

AlwaysSignaled

To handle special cases such as parent device of fence being put in error, *Dxgkrnl* will provide new CurrentValue as 0xFFFFFFFF and call DxgkDdiUpdateCurrentValuesFromCpu with AlwaysSignaled flag set. This flag indicates to the driver that the fence object CurrentValue can't be relied upon to be updated as before. Driver/CMP must ensure that when it sees a GPU wait of this fence, it must be unblocked immediately without actually queuing a wait and similarly when it sees a signal of this fence it should be a no-op and not touch the fence storage.

NotificationOnly

OS sets this flag to inform KMD that it should not actually write a new value to CurrentValue location, and instead this call is just a notification that CurrentValue was updated and KMD should re-scan its runlist to unblock any GPU waiters that are now signaled. This flag is used to handle cross-adapter native fences, as described in the dedicated section below.

14. Cross-adapter native fences

* The OS must support creating cross-adapter native fences because existing DX12 apps create and use cross-adapter monitored fences. If underlying queues and scheduling for these apps is switched to user-mode submission, then their monitored fences must also be switched to native fences (user-mode queues can't support monitored fences).

* A cross-adapter fence must be created with type D3DDDI_NATIVEFENCE_TYPE_DEFAULT, otherwise [**D3DKMTCreateNativeFence**]() fails.

* All GPUs share the same copy of **CurrentValue** storage, which is always allocated in system memory. When the runtime creates a cross-adapter native fence on GPU1 and opens it on GPU2, the GPU VA mappings on both GPUs point to the same **CurrentValue** physical storage.

* Each GPU gets its own copy of **MonitoredValue**. Hence, **MonitoredValue** storage can be allocated in system memory or local memory.

* Cross-adapter native fences must resolve the condition where GPU1 is waiting on a native fence, which is signaled by GPU2. Today, there is no concept of GPU to GPU signals; hence, the OS explicitly resolves this condition by signaling GPU1 from the CPU. This is done by setting **MonitoredValue** for the cross-adapter fence to 0 for its lifetime. Then, when GPU2 signals the native fence, it also raises a CPU interrupt, allowing *Dxgkrnl* to update **CurrentValue** on GPU1 (using DdiUpdateCurrentValueFromCpu and NotificationOnly == TRUE) and unblock any pending CPU/GPU waiters of that GPU

* Note, although MV will always be 0 for cross-adapter native fences, wait and signals submitted on the same GPU still benefit from faster on GPU synchronization. However, the power benefit of reduced CPU interrupts is lost because CPU interrupts will be raised unconditionally, even if there were no CPU waiters or waiters on the other GPU. This is a trade-off we make to keep the design and implementation cost of cross-adapter native fence simple

* OS supports scenario where a native fence object is created on GPU1 (which supports the feature) and opened GPU2 which doesn't support the feature. The fence object will be opened as a regular MonitoredFence on GPU2.

* OS supports scenario where a regular monitored fence object is created on GPU1 and opened as a NativeFence on GPU2 (which supports the feature). The fence object will be opened as a NativeFence on GPU2.

14.1. Cross-adapter wait/signal combinations
Below tables takes an example of an iGPU and dGPU system, and list the various configurations which are possible for native fence Wait/Signal from CPU/GPU. We also consider two cases:

both GPUs support native fences
iGPU doesn't support native fences, dGPU supports native fences.
Note: Second scenario is also similar to the case where both GPUs support native fences, but native fence wait/signal is submitted to a kernel mode queue on iGPU

The tables should be read by selecting a pair of wait and signal from the columns, for example WaitFromGPU - SignalFromGPU or WaitFromGPU - SignalFromCPU etc.

14.1.1. Both dGPU and iGPU Support NF
iGPU		dGPU	
WaitFromGPU (hFence, 10)	WaitFromCPU (hFence, 10)	SignalFromGpu (hFence, 10)	SignalFromCpu(hFence, 10)
UMD insert a wait for hfence CurrentValue == 10 instruction in command buffer	Runtime calls D3DKMTWaitForSyncObjectFromCpu		
VidSch tracks this sync object in a new NativeFenceCpuWaiterList		
UMD inserts a write hFence CurrentValue = 10 signal instruction in command buffer	Runtime calls D3DKMTSignalSyncObjectFromCpu
VidSch receives NativeFenceSignaledISR when CurrentValue is written (because MV == 0 always)	VidSch calls DdiUpdateCurrentValueFromCpu(hFence, 10)
VidSch propogates the signal (hFence, 10) to iGPU	VidSch propogates the signal (hFence,10) to iGPU
VidSch receives the propogated signal and calls DdiUpdateCurrentValueFromCpu(hFence, NotificationOnly==TRUE)	VidSch receives the propogated signal and calls DdiUpdateCurrentValueFromCpu(hFence, NotificationOnly==TRUE)		
KMD re-scans the runlist to unblock HW channel that was waiting on hFence	VidSch unblocks the CPU wait condition by signalling the KEVENT		
14.1.2. iGPU doesn't support, dGPU supports NF: Wait submitted on iGPU, Signal submitted on dGPU
iGPU		dGPU	
WaitFromGPU (hFence, 10)	WaitFromCPU (hFence, 10)	SignalFromGpu (hFence, 10)	SignalFromCpu(hFence, 10)
Runtime calls D3DKMTWaitForSyncObjectFromGpu	Runtime calls D3DKMTWaitForSyncObjectFromCpu		
VidSch tracks this sync object in the MonitoredFenceWaitingList	VidSch tracks this sync object in the MonitoredFenceCpuWaiterListHead		
UMD inserts a write hFence CurrentValue = 10 signal instruction in command buffer	Runtime calls D3DKMTSignalSyncObjectFromCpu
VidSch receives NativeFenceSignaledISR when CurrentValue is written (because MV == 0 always)	VidSch calls DdiUpdateCurrentValueFromCpu(hFence, 10)
VidSch propagates the signal (hFence, 10) to iGPU	VidSch propagates the signal (hFence,10) to iGPU
VidSch receives the propagated signal and observes new fence value	VidSch receives the propagated signal and observes new fence value		
VidSch scans the MonitoredFenceWaitingList and unblocks SWContexts	VidSch scans the MonitoredFenceCpuWaiterListHead and unblocks CPU wait by signalled the KEVENT		
14.1.3. iGPU doesn't support, dGPU supports NF: Signal submitted on iGPU, Wait submitted on dGPU
iGPU		dGPU	
SignalFromGpu (hFence, 10)	SignalFromCpu (hFence, 10)	WaitFromGpu (hFence, 10)	WaitFromCpu (hFence, 10)
UMD insert a wait for hfence CurrentValue == 10 instruction in command buffer	Runtime calls D3DKMTWaitForSyncObjectFromCpu
VidSch tracks this sync object in a new NativeFenceCpuWaiterList
UMD calls D3DKMTSignalSyncObjectFromGpu	UMD calls D3DKMTSignalSyncObjectFromCpu		
When packet is at head of SWContext, vidsch updates fence value directly from CPU	vidsch updates fence value directly from CPU		
VidSch propogates the signal (hFence, 10) to dGPU	VidSch propogates the signal (hFence, 10) to dGPU		
VidSch receives the propogated signal and calls DdiUpdateCurrentValueFromCpu(hFence, NotificationOnly == TRUE)	VidSch receives the propogated signal and calls DdiUpdateCurrentValueFromCpu(hFence, NotificationOnly == TRUE)
KMD re-scans the runlist to unblock HW channel that was waiting on hFence	VidSch unblocks the CPU wait condition by signalling the KEVENT
14.2. Future GPU-GPU cross-adapter signal
As described in #5 above, for cross-adapter native fences, we lose power savings because a CPU interrupt is raised unconditionally

In a future release, OS will design and develop an infrastructure using which a GPU signal on one GPU can interrupt other GPUs by writing to a common doorbell memory, allowing other GPUs to wake up, process its run-list and unblock ready HW queues.

The challenge for this work will be to design the common doorbell memory as well as an intelligent payload or handle which a GPU can write to the doorbell which allows other GPUs to determine which fence was signalled so that it can only scan a subset of HWQueues

With such a cross-adapter signal, it might even be possible for GPUs to share the same copy of native fence storage (a linear format cross-adapter allocation, similar to cross-adapter scanout allocations) from which all GPUs read and write to

15. Native fence log buffer design
With native fences and user mode submission, Dxgkrnl will not have visibility of when native GPU Waits and Signals enqueued from UMD and are unblocked on GPU for a particular HWQueue (With native fences, monitored fence signalled interrupt could be suppressed for a given fence).

GpuView Fences

We need a way to recreate the fence operations as shown above in GPUVIEW. The dark pink boxes are Signals and light pink are Waits. Where each box begins is when the operation was submitted on CPU to *Dxgkrnl* and where the box ends is when the operation was completed by *Dxgkrnl* on CPU. This way we are able to study entire lifetime of a command

So, at a high level, the per HWQueue conditions which require to be logged are:

FENCE_WAIT_QUEUED

CPU Timestamp of when the UMD inserts a GPU Wait instruction in the command queue

FENCE_SIGNAL_QUEUED

CPU Timestamp of when the UMD inserts a GPU Signal instruction in the command queue

FENCE_SIGNAL_EXECUTED

GPU timestamp of when a signal command is executed on GPU for a HWQueue

FENCE_WAIT_UNBLOCKED

GPU timestamp of when a wait condition is satisfied on GPU and the HWQueue is unblocked

15.1. Mechanism
Dxgkrnl will allocate two dedicated 4 KB log buffer per HWQueue - one for logging waits and other for logging signals. These log buffers have mappings for KernelCPUVA, ContextManagementProcessor VA and a GPU VA in process address space so that it can be read/write by KMD, CMP and GPU engine.

Immediately after UMD inserts a native fence wait or signal instruction to the command list, it also inserts a command instructing the GPU to write a payload at a particular entry into the log buffer. The payload is described in the DXGK_FENCE_LOG_ENTRY struct

After the GPU engine executes the fence operation, it sees the UMD instruction to write a payload to a given entry into the log buffer. In addition, GPU also writes the current GPUTimestamp into this log buffer entry

While the UMD can't access the GPU accessible log buffer, it controls the progression of the log buffer i.e determines the next free entry to write to if any and programs the GPU with this information. When the GPU writes to the log buffer, it increments the NextFreeIndex value in the log header UMD must ensure that writes to log entries are monotonically increasing


typedef enum _DXGK_NATIVE_FENCE_LOG_TYPE {
    DXGK_NATIVE_FENCE_LOG_TYPE_WAITS   = 1,
    DXGK_NATIVE_FENCE_LOG_TYPE_SIGNALS = 2
} DXGK_NATIVE_FENCE_LOG_TYPE;

struct DXGK_NATIVE_FENCE_LOG_HEADER
{
    union
    {
        struct
        {
            UINT32          FirstFreeEntryIndex;    // same as LowPart of AtomicWraparoundAndEntryIndex
            UINT32          WraparoundCount;        // same as HighPart of AtomicWraparoundAndEntryIndex
        };

        ULARGE_INTEGER      AtomicWraparoundAndEntryIndex;
    };

    DXGK_NATIVE_FENCE_LOG_TYPE Type;
    UINT64          NumberOfEntries;
    UINT64          Reserved[2];
};

enum DXGK_NATIVE_FENCE_LOG_OPERATION
{
    DXGK_NATIVE_FENCE_LOG_OPERATION_SIGNAL_EXECUTED = 0,
    DXGK_NATIVE_FENCE_LOG_OPERATION_WAIT_UNBLOCKED = 1
};

typedef struct _DXGK_NATIVE_FENCE_LOG_ENTRY
{
    UINT64 FenceValue;                // UMD payload: Newly signaled/unblocked fence value 
    D3DKMT_HANDLE hNativeFence;       // UMD payload: user mode D3DKMT_HANDLE of native fence to which this operation belongs
    UINT OperationType;               // UMD payload: DXGK_FENCE_LOG_OPERATION type
    UINT64 Reserved0;                 // Reserved for alignment
    UINT64 FenceObservedGpuTimestamp; // GPU Payload: OPERATION_WAIT_UNBLOCKED only: GPU Time at which an unresolved wait command was seen by engine and stalled the HWQueue
    UINT64 Reserved1;                 // Reserved for alignment
    UINT64 FenceEndGpuTimestamp;      // GPU Payload: GPU Time at which the fence operation completed on GPU    
}DXGK_NATIVE_FENCE_LOG_ENTRY;

struct DXGK_NATIVE_FENCE_LOG_BUFFER
{
    DXGK_NATIVE_FENCE_LOG_HEADER  Header;

    _Field_size_(Header.NumberOfEntries)
    DXGK_NATIVE_FENCE_LOG_ENTRY   Entries[1];
};

struct DXGKARG_SETNATIVEFENCELOGBUFFER
{
    HANDLE                      hAdapter;                   // in: driver handle of adapter
    HANDLE                      hHwQueue;                   // in: HWQueue this log belongs to
    UINT                        NumberOfEntries;            // in: number of entries in the log entries array

    _Field_size_bytes_(32 + 32 * NumberOfEntries)
    DXGK_FENCE_LOG_BUFFER* LogBufferCpuVa;                  // in: read/write kernel mode CPU VA of the fence log buffer
    D3DGPU_VIRTUAL_ADDRESS LogBufferGpuVa;                  // in: read/write GPU VA of the log buffer
    D3DGPU_VIRTUAL_ADDRESS LogBufferCmpVa;                  // in: read/write VA of log buffer in context management processor address space
};

typedef _In_ CONST DXGKARG_SETNATIVEFENCELOGBUFFER*   IN_CONST_PDXGKARG_SETNATIVEFENCELOGBUFFER;

typedef
_Check_return_
_Function_class_DXGK_(DXGKDDI_SETNATIVEFENCELOGBUFFER)
_IRQL_requires_(DISPATCH_LEVEL)
NTSTATUS
APIENTRY
DXGKDDI_SETNATIVEFENCELOGBUFFER(
    IN_CONST_PDXGKARG_SETNATIVEFENCELOGBUFFER pSetNativeFenceLogBuffer
);

typedef struct _D3DKMT_CREATEHWQUEUE
{
    -----
    -----
    UINT NativeFenceWaitLogBufferGpuVa;          // Opaque 64 bit GPU VA of used for programming GPU writes into native fence wait log buffer 
    UINT NativeFenceSignalLogBufferGpuVa;        // Opaque 64 bit GPU VA of used for programming GPU writes into native fence signal log buffer
    UINT NativeFenceLogBufferNumberOfEntries;    // Size of Entries array in DXGK_FENCE_LOG_BUFFER
} D3DKMT_CREATEHWQUEUE;
Consider,

we have 2 HWQueues HWQueueA and HWQueueB with corresponding fence log buffers with GPU VA FenceLogA and FenceLogB
we have a native fence object with user mode D3DKMT_HANDLE: FenceF
GPUWait on FenceF for Value V1 is queued to HWQueueA at time CPUT1. When building the command buffer, UMD will insert a command instructing GPU to log payload: LOG(FenceF, V1, DXGK_FENCE_LOG_OPERATION_WAIT_UNBLOCKED)
GPUSignal to FenceF with Value V1 is queued to HWQueueB at time CPUT2. When building the command buffer, UMD will insert a command instructing GPU to log payload: LOG(FenceF, V1, DXGK_FENCE_LOG_OPERATION_SIGNAL_EXECUTED)
After GPU scheduler executes the GPUSignal on HWQueueB at GPU Time GPUT1, it reads the UMD payload and logs the event in the OS provided fence log for HWQueueB:

DXGK_FENCE_LOG_ENTRY LogEntry = {};
LogEntry.hNativeFence = FenceF;
LogEntry.FenceValue = V1;
LogEntry.OperationType = DXGK_FENCE_LOG_OPERATION_SIGNAL_EXECUTED;
LogEntry.FenceEndGpuTimestamp = GPUT1;
After GPU scheduler observes HWQueueA is unblocked at GPU Time GPUT2, it reads the UMD payload and logs the event in the OS provided fence log for HWQueueA:

DXGK_FENCE_LOG_ENTRY LogEntry = {};
LogEntry.hNativeFence = FenceF;
LogEntry.FenceValue = V1;
LogEntry.OperationType = DXGK_FENCE_LOG_OPERATION_WAIT_UNBLOCKED;
LogEntry.FenceObservedGpuTimestamp = GPUTo
LogEntry.FenceEndGpuTimestamp = GPUT2;
15.2. CPU Timestamps of fence queued operations
Given that a command list can be recorded several minutes before GPU execution of a command buffer that includes the command list, and that this several minutes can be out-of-order with other sync objects that are in the same command buffer, there is little benefit of making the UMD log these CPU timestamps. There is a cost to including the CPU timestamps in UMDs instructions to GPU-written log buffer so we do not include CPUTimestamps in the log entry payload.

Instead, the runtime or UMD can emit a native fence queued ETW event with the CPUTimestamp, at the time a command list is being recorded. This way tools can build a timeline of fence queued and completed events by combining the CPUTimestamp from this new event and GPUTimestamp from the log buffer entry.

15.3. Order of Operations on GPU when signaling or unblocking a fence
The UMD must ensure that it maintains the following order when it builds a command list instructing GPU to signal/unblock a fence:

Write new fence value to fence GPU VA/CMPVA
Write log payload to corresponding log buffer GPU VA/CMPVA
Raise native fence signaled interrupt if required
This ensures that when interrupt is raised to OS, *Dxgkrnl* sees the most up to date log entries.

15.4. Log buffer overrun is permitted
It is not necessary for UMD to implement back pressure support while progressing the log buffer entries and GPU can overrun the log buffer by overwriting to entries no yet seen by OS by incrementing the WraparoundCount. When OS eventually reads the log, it can detect that an overrun has occurred by comparing the new WraparoundCount value in log header with its cached value. In case of an overrun, OS has fallback options as follows: - To unblock fences in case of an overrun, OS will scan all the fences and determine which waiters were unblocked - If tracing was enabled then OS can emit a flag in the trace which notifies a user that events were lost. Also, when tracing is enabled, OS will first increase the size of the log buffer to prevent overruns in the first place

15.5. Empty or repeated log buffer timestamps
In common cases, *Dxgkrnl* expects that timestamps in log entries are monotonically increasing. However, there are scenarios when timestamp of subsequent log entries are zero or same as previous log entries. For example, in LDA case, one of the chained adapter in LDA can skip the fence write operation in which case its log buffer entry will have a zero timestamp. Dxgkrnl will handle such cases. However, for a given log entry, *Dxgkrnl* never expects its timestamp to be lesser than previous log entry, i.e timestamps can never go backwards.

15.6. Synchronously updating native fence Log
GPU writes to update fence value and corresponding log buffer must ensure that writes have fully propagated before CPU reads, which necessitate the use of memory barriers. For example:

    Signal Fence(N): write N as a new current value
    Write LOG entry including GPU timestamp
    MemoryBarrier
    Increment FirstFreeEntryIndex
    MemoryBarrier
    Monitored fence interrupt (N): read Address “M”, compare the value with N to decide delivering the CPU interrupt
It would prove too expensive to insert two barriers on every GPU signal, especially, when its likely that the conditional interrupt check is not satisfied and no CPU interrupt is necessary. As a result, we propose to move the cost of inserting one of the memory barrier from GPU (producer) to CPU (consumer). Hence, we are introducing a DDI to synchronously flush pending native fence log writes on demand (similar to how we introduced DdiUpdateFlipQueueLogBuffer for HW flip queue log flush).

GPU operations:

- Signal Fence(N): write N as a new current value
- Write LOG entry including GPU timestamp
- Increment FirstFreeEntryIndex
- MemoryBarrier => Ensures FirstFreeEntryIndex is fully propogated
- Monitored fence interrupt (N): read Address “M”, compare the value with N to decide delivering the interrupt
CPU Operations:

In *Dxgkrnl*’s Native Fence Signaled interrupt handler (DISPATCH_IRQL):

- For each HWQueue Log: Read FirstFreeEntryIndex and determine if new entries are written 
- For each HWQueue log with new entries: Call DdiUpdateNativeFenceLog and provide kernel handle of HWQueue 
    In this DDI, KMD inserts a MemoryBarrier to the given HWQueue which ensures that all log entry writes are commited
- Dxgkrnl reads log entries to extract timestamp payload
So, as long as HW inserts a MemoryBarrier after writes to FirstFreeEntryIndex, *Dxgkrnl* will always call KMD DDI, allowing KMD to insert a memory barrier, before *Dxgkrnl* reads any log entries.

This DDI executes at the DISPATCH_LEVEL.

struct DXGKARG_UPDATENATIVEFENCELOGS
{
    UINT    NumberOfQueues; // Number of elements in below array
    HANDLE* hHWQueue;       // Array of KMD Handles to HWQueues whose pending native fence log writes must be flushed to OS log buffer
};

_Check_return_
_Function_class_DXGK_(DXGKDDI_UPDATENATIVEFENCELOGS)
_IRQL_requires_(DISPATCH_LEVEL)
NTSTATUS
APIENTRY
DXGKDDI_UPDATENATIVEFENCELOGS(
    DXGKARG_UPDATENATIVEFENCELOGS* pUpdateNativeFenceLog
    );
15.7. Future Hardware Requirements
Most current generation hardware might only support writing the kernel handle of the fence object it signaled in the native fence signaled interrupt. This is the design described before in Section 12 DXGKARGCB_NOTIFY_INTERRUPT_DATA::NativeFenceSignaled. In this case, *Dxgkrnl* handles the interrupt payload, as follows:

OS performs a read (potentially across PCI) of the fence value
Knowing which fence has been signaled and the fence value, the OS awakens CPU waiters that are waiting on that fence/value.
Separately, for the parent device of this fence, the OS scans the log buffers of all its HWQueues, and then reads the last written log buffer entries to determine which HWQueue did the signal and extract the corresponding timestamp payload. This might redundantly read some fence values across PCI.
On future platforms, *Dxgkrnl* prefers to obtain an array of kernel HwQueue handles in the native fence signaled interrupt. This enables the OS to do the following:

Read the latest log buffer entries for that HwQueue. The user device is not known to the interrupt handler, therefore this HwQueue handle needs to be a kernel handle.
Scan the log buffer for log entries that indicate what fences have been signaled, and to what values. Reading only the log buffer ensures a single read over PCI instead of having to redundantly read fence values and the log buffer. This is an optimization that succeeds as long as the log buffer has not been overrun (dropping entries that were never read by *Dxgkrnl*.)
If the OS detects that log buffer overrun has occurred, then the OS falls back to the not-optimized path that reads the live value of every fence owned by the same device. Performance is proportional to the number of fences owned by the device. If the fence value is in video memory, then these are cache-coherent reads across PCI.
Knowing which fences have been signaled and the fence values, the OS awakens CPU waiters that are waiting on those fences/values.
15.7.1. Optimized Native Fence Signaled Interrupt
If supported by HW, then instead of filling out an array of fence handles which got signaled, GPU should only mention the KMD handle of the HWQueue which was running. Dxgkrnl will scan the fence log buffer for this HWQueue and read all the fences operations which were completed by GPU since last update and unblock any corresponding CPU waiters. If GPU could not determine which subset of fences were signaled, then it should specify a NULL HWQueue handle. When *Dxgkrnl* sees a NULL HWQueue handle, it falls back to re-scan log buffer of all HWQueues on this engine to determine which fences got signaled.

Support for this optimization will be optional and KMD should set the OptimizedNativeFenceSignaledInterrupt cap if supported by HW. If OptimizedNativeFenceSignaledInterrupt cap is not set, then GPU/KMD should follow the behavior of native fence signaled interrupt as described earlier in section 12.

typedef struct _DXGK_VIDSCHCAPS
{
    union
    {
        struct
        {
        ---
        ---

#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)

            UINT    NativeGpuFence         :1;  // Specifies whether the GPU supports native GPU fence
            UINT    OptimizedNativeFenceSignaledInterrupt : 1; // TRUE if GPU can specify HWQueue handle in DXGKARGCB_NOTIFY_INTERRUPT_DATA::NativeFenceSignaled
            UINT    Reserved               :20;

#else

            UINT    Reserved               :21;

#endif // !(DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)

        ---
        ---
        };
        UINT        Value;
    };
} DXGK_VIDSCHCAPS;

typedef enum _DXGK_INTERRUPT_TYPE
{
...
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
    DXGK_INTERRUPT_NATIVE_FENCE_SIGNALED = 19
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)

} DXGK_INTERRUPT_TYPE;

typedef struct _DXGKARGCB_NOTIFY_INTERRUPT_DATA
{
    DXGK_INTERRUPT_TYPE  InterruptType;        // in: interrupt type
...
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
        struct
        {
            UINT    NodeOrdinal;    // in: Node ordinal of engine generating the notification.
            UINT    EngineOrdinal;  // in: Engine ordinal of engine generating the notification.
                                                // Signaled native fence array specifies all fences that were signaled and require waiters to be unblocked.
                                                // If this array is empty, the OS will re-scan all pending native fence waiters instead of the subset specified by the signaled native fence array.
            UINT    SignaledNativeFenceCount;   // in: size of the signaled native fence array.
            _Field_size_(SignaledNativeFenceCount)
            HANDLE* pSignaledNativeFenceArray;  // in: OS kernel mode handles of objects in the signaled native fence array.

            HANDLE  hHWQueue;       // Dxgkrnl reads this value only if OptimizedNativeFenceInterrupt is TRUE. 
                                    // KMD Handle of the HWQueue which was running on the engine which raised the 
                                    // interrupt. If this handle is NULL then *Dxgkrnl* will re-scan log buffer of 
                                    // all HWQueues on this engine
        }; NativeFenceSignaled;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM3_1)
...
} DXGKARGCB_NOTIFY_INTERRUPT_DATA;

HWQueue A: GPU Signal to Fence F1, Value V1 -> Write to log buffer Entry E1 -> no interrupt required

HWQueue A: GPU Signal to Fence F1, Value V2 -> Write to log buffer Entry E2 -> no interrupt required

HWQueue A: GPU Signal to Fence F2, Value V3 -> Write to log buffer Entry E3 -> no interrupt required

HWQueue A: GPU Signal to Fence F2, Value V3 -> Write to log buffer Entry E4 -> interrupt raised

DXGKARGCB_NOTIFY_INTERRUPT_DATA FenceSignalISR = {};
FenceSignalISR.NodeOrdinal = 0;
FenceSignalISR.EngineOrdinal = 0;
FenceSignalISR.hHWQueue = A;
Dxgkrnl reads log buffer for HWQueue A -> reads log buffer entries E1, E2, E3, E4 to observe signaled fences F1 @ Value V1, F1 @ Value V2, F2 @ Value V3, F2 @ Value V3 -> unblock any waiters waiting on those fences and values.

15.8. Optional and Mandatory Logging
Above native fence logging for DXGK_NATIVE_FENCE_LOG_TYPE_WAITS and DXGK_NATIVE_FENCE_LOG_TYPE_SIGNALS is mandatory.

In the future, additional logging types might be added for only when verbose ETW logging is enabled in the OS by a tool such as gpuview. OS must inform both UMD and KMD of when verbose logging is enabled and disabled so that logging of those verbose events are selectively enabled.

15.8.1. New KMD DDI to inform when verbose logging is enabled/disabled
enum D3DDDI_LOGGING_LEVEL
{
    D3DDDI_LOGGING_LEVEL_DEFAULT = 0,
    D3DDDI_LOGGING_LEVEL_ALL = 1
};

typedef struct _DXGKARG_UPDATELOGGINGLEVEL
{
    D3DDDI_LOGGING_LEVEL LoggingLevel;
} DXGKARG_UPDATELOGGINGLEVEL;

typedef _In_ CONST DXGKARG_UPDATELOGGINGLEVEL*   IN_CONST_PDXGKARG_UPDATELOGGINGLEVEL;

typedef
    _Check_return_
    _Function_class_DXGK_(DXGKDDI_UPDATELOGGINGLEVEL)
    _IRQL_requires_(PASSIVE_LEVEL)
NTSTATUS
APIENTRY
DXGKDDI_UPDATELOGGINGLEVEL(
    IN_CONST_PDXGKARG_UPDATELOGGINGLEVEL pUpdateLoggingLevel
    );
15.8.2. UMD payload generation controlled by disconnecting doorbell to force UMD to query verbosity level from *Dxgkrnl*
Each time verbose logging is toggled, *Dxgkrnl* will disconnect the doorbell of all HWQueues which forces the UMD to call into *Dxgkrnl* to reconnect the doorbell. As part of this reconnect, *Dxgkrnl* will also return the new verbosity level to UMD based on which it can start/stop verbose logging of native fence operations.

enum _D3DDDI_DOORBELLSTATUS
{
    D3DDDI_DOORBELLSTATUS_CONNECTED = 0,
    D3DDDI_DOORBELLSTATUS_CONNECTED_NOTIFY_KMD = 1,
    D3DDDI_DOORBELLSTATUS_DISCONNECTED_RETRY = 2,
    D3DDDI_DOORBELLSTATUS_DISCONNECTED_ABORT = 3,
}D3DDDI_DOORBELLSTATUS;

// Doorbell status is a 64 Byte memory allocation
struct D3DDDI_DOORBELLSTATUS_STORAGE
{
    UINT32 ConnectionStatus;
    UINT32 LoggingLevel;
};
