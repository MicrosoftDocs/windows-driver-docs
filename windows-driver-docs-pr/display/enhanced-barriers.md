---
title: D3D12 enhanced barriers
description: Learn about D3D12 enhanced barriers
keywords:
- D3D12 enhanced barriers
- Windows 11 , enhanced barriers
- WDDM 3.0 , enhanced barriers
- Agility SDK Preview , enhanced barriers
ms.date: 10/19/2022
ms.localizationpriority: medium
prerelease: true
---

# D3D12 enhanced barriers

The DDI interface for enhanced barriers is available in the [Windows 11, version 22H2 WDK](/windows-hardware/drivers/download-the-wdk) (WDDM 3.0). To use enhanced barriers on 22H2 (or earlier OS releases), you must install the [1.706.4-preview Agility SDK](https://devblogs.microsoft.com/directx/directx12agility/).

D3D12 enhanced barriers give developers independent control over GPU work synchronization, texture layout transitions, and cache flushing (“resource memory access”). This feature offers a set of Direct3D APIs and DDIs that give developers independent control over GPU work synchronization, texture layout transitions, and cache flushing (resource memory access).

Enhanced barriers replace [legacy resource barriers](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_resourcebarrier_0022) with more expressive barrier types. Features include the following:

* Less synchronization latency.
* A reduction in excessive cache flushes.
* No mysterious Promotion and Decay rules.
* Fast, flexible resource aliasing (diverse aliasing topologies).
* Discard during barrier transition.
* Support for concurrent read/write, including same-resource copy (self-copy).
* Support for Asynchronous Discard, Copy, Resolve, and Clear commands.

Enhanced barriers aren't simpler than legacy resource barriers, but they're far less ambiguous and therefore easier for developers to use.

## Reporting enhanced barrier support

The enhanced barriers feature isn't currently a hardware or driver requirement. A driver indicates support by setting the **EnhancedBarriersSupported** member of [**D3D12DDI_D3D12_OPTIONS_DATA_0089**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_d3d12_options_data_0089) to TRUE.

* **D3D12DDI_FEATURE_VERSION_VIDEO_0088_0** is the version number that defines the preliminary implementation of D3D12 enhanced barrier milestones introduced in Windows 11.

## D3D12 enhanced barrier callback functions

Drivers that indicate support for enhanced barriers implement the following callback functions:

* [**PFND3D12DDI_BARRIER_0088**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_barrier_0088)
* [**PFND3D12DDI_CREATEHEAPANDRESOURCE_0088**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_createheapandresource_0088)
* [**PFND3D12DDI_CALCPRIVATEHEAPANDRESOURCESIZES_0088**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_calcprivateheapandresourcesizes_0088)
* [**PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0088**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_checkresourceallocationinfo_0088)

## Design details

Drivers typically handle legacy resource barriers using three separate operations:

1. Synchronize GPU work.
2. Perform any necessary cache flush operations.
3. Perform any necessary layout changes.

Enhanced barriers give developers the ability to control each of these operations separately.

### Types of enhanced barriers

There are three types of *enhanced* barriers:

* [Texture barriers](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_texture_barrier_0088)
* [Buffer barriers](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_buffer_barrier_0088)
* [Global barriers](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_global_barrier_0088)

[Ranged barriers](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_ranged_barrier_0088) replace [legacy resource barriers](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_resource_ranged_barrier_0022). Ranged barriers are provided so that legacy resource barriers can be fully implemented with no noticeable performance loss.

* All barrier types control GPU work synchronization and read or write access types before and after the barrier.

* Texture barriers additionally manage layout of texture subresources. Subresource selection can be expressed as a range of mip, array, and plane slices, in addition to the familiar one-or-all option used by legacy resource barriers.

* Buffer barriers and global barriers control only synchronization and resource access and have no impact on resource layout (buffers don’t have a layout). Global barriers affect all cached memory so they can be expensive and should only be used when a more scoped barrier is insufficient.

#### Texture barriers

* Control cache flush, memory layout, and synchronization for texture subresources.
* Must only be used with texture resources.
* Allow selection of a single subresource, all subresources, or a coherent range of subresources (that is, mip range and array range).
* Must provide a valid, non-NULL resource pointer.

#### Buffer barriers

* Control cache flush and synchronization for buffer resources.
* Must only be used with buffer resources.
* Unlike textures, buffers have only a single subresource and don't have a layout that can be transitioned.
* Must provide a valid, non-NULL resource pointer.

#### Global barriers

* Control cache flush and synchronization for all indicated resource access types in a single command queue.
* Have no effect on texture layout.
* Are needed to provide functionality similar to legacy NULL UAV barriers and NULL/NULL aliasing barriers.

Since global barriers don't transition texture layout, global barriers can't be used in transitions that otherwise would require a layout change. For example, a global barrier can't be used to transition a non-simultaneous-access texture from D3D12DDI_BARRIER_ACCESS_RENDER_TARGET to D3D12DDI_BARRIER_ACCESS_SHADER_RESOURCE, since that would also require a change from D3D12DDI_BARRIER_LAYOUT_RENDER_TARGET to D3D12DDI_BARRIER_LAYOUT_SHADER_RESOURCE.

### Synchronization

Graphics processors are designed to execute as much work in parallel as possible. Any GPU work that depends on previous GPU work must be synchronized before accessing dependent data.

The enhanced barrier interface uses explicit **SyncBefore** and **SyncAfter** values as logical bit field masks. A barrier must wait for all preceding command **SyncBefore** scopes to complete before executing the barrier. Similarly, a barrier must block all subsequent **SyncAfter** scopes until the barrier completes. [**D3D12DDI_BARRIER_SYNC**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_barrier_sync) specifies the synchronization scope of GPU work with respect to the barrier.

For more information see the [Enhanced Barriers specification](https://microsoft.github.io/DirectX-Specs/d3d/D3D12EnhancedBarriers.html#synchronization).

### Layout transitions

Texture subresources can use different layouts for various access methods. For example, textures are often compressed when used as a render target or depth stencil and are often uncompressed for shader read or copy commands. Texture barriers use **LayoutBefore** and **LayoutAfter** [**D3D12DDI_BARRIER_LAYOUT**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_barrier_layout) values to describe layout transitions.

Layout transitions are only needed for textures, so they're expressed only in the [**D3D12DDI_TEXTURE_BARRIER**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_texture_barrier_0088) data structure.

Both **LayoutBefore** and **LayoutAfter** must be compatible with the type of queue performing the barrier. For example, a compute queue can't transition a subresource into or out of **D3D12DDI_BARRIER_LAYOUT_RENDER_TARGET**.

To provide well-defined barrier ordering, the layout of a subresource after completing a sequence of barriers is the final **LayoutAfter** in the sequence.

### Access transitions

Since many GPU-write operations are cached, any barrier from a write access to another write access, or a read-only access might require a cache flush. The enhanced barrier API’s use access transitions to indicate that a subresource’s memory needs to be made visible for a specific new access type. Like the layout transitions, some access transitions might not be needed if it's known that the memory of the associated subresource is already accessible for the desired use.

Access transitions are expressed as follows:

* For textures, as part of the D3D12DDI_TEXTURE_BARRIER structure.
* For buffers, as part of the D3D12DDI_BUFFER_BARRIER structure.

Access transitions don't perform synchronization. It's expected that synchronization between dependent accesses is handled using appropriate **SyncBefore** and **SyncAfter** values in the barrier.

An **AccessBefore** made visible to a specified **AccessAfter** doesn't guarantee that the resource memory is also visible for a different access type. For example:

``` cpp
MyTexBarrier.AccessBefore=D3D12DDI_BARRIER_ACCESS_UNORDERED_ACCESS;
MyTexBarrier.AccessAfter=D3D12DDI_BARRIER_ACCESS_SHADER_RESOURCE;
```

This access transition indicates that a subsequent shader-read access depends on a preceding unordered-access-write. However, if the hardware is capable of reading shader resources directly from the UAV cache, the driver might not actually flush the UAV cache.

#### D3D12DDI_BARRIER_ACCESS_COMMON

**D3D12DDI_BARRIER_ACCESS_COMMON** is a special access type that indicates any layout-compatible access. Transitioning to **D3D12DDI_BARRIER_ACCESS_COMMON** means that subresource data must be available for any layout-compatible access after a barrier. Since buffers have no layout, **D3D12DDI_BARRIER_ACCESS_COMMON** simply means any buffer-compatible access.

Specifying **D3D12DDI_BARRIER_ACCESS_COMMON** as **AccessBefore** in a barrier implies the set of all write-access types. Using **D3D12DDI_BARRIER_ACCESS_COMMON** as **AccessBefore** is discouraged since it could result in costly, unintended cache flushes. Instead, developers are encouraged to use only the most narrowly required write-access bits to properly constrain barrier overhead. A debug layer warning is issued when **AccessBefore** is set to **D3D12DDI_BARRIER_ACCESS_COMMON**.

#### Single-queue simultaneous access

Enhanced barriers allow concurrent read/write operations on the same buffer or simultaneous-access texture in the same command queue.

Buffers and simultaneous-access resources have always supported write access from one queue with concurrent, non-dependent read accesses from one or more other queues. This support is because such resources always use the COMMON layout and have no read/write hazards since reads must not depend on concurrent writes. (Legacy resource barrier rules disallow combining write state bits with any other state bits. As such, resources can't be concurrently read-from and written-to in the same queue using legacy resource barriers.)

The one-writer-at-a-time policy still applies since two seemingly non-overlapping write regions might still have overlapping cache lines.

### Subresource Ranges

It's common for developers to want to transition a range of subresources; for example, transition a full mip-chain for a given texture array or a single mip-level for all array slices. Enhanced barriers allow developers to transition logically adjacent ranges of subresources using the [**D3D12DDI_BARRIER_SUBRESOURCE_RANGE**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_barrier_subresource_range_0088) structure. (Legacy resource state transition barriers only provide developers the option of transitioning *all* subresource states or a single subresource state atomically.)

### Compute and direct queue layouts

The following [enhanced barrier layouts](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_barrier_layout) are guaranteed to be the same for both direct and compute queues:

* D3D12DDI_BARRIER_LAYOUT_GENERIC_READ
* D3D12DDI_BARRIER_LAYOUT_UNORDERED_ACCESS
* D3D12DDI_BARRIER_LAYOUT_SHADER_RESOURCE
* D3D12DDI_BARRIER_LAYOUT_COPY_SOURCE
* D3D12DDI_BARRIER_LAYOUT_COPY_DEST

A subresource in one of these layouts can be used in either direct queues or compute queues without a layout transition.

On some hardware, layout transition barriers on direct queues can be significantly faster if both preceding or subsequent accesses are also on direct queues. It's strongly recommended to access resources on direct queues use the following layouts:

* D3D12DDI_BARRIER_LAYOUT_DIRECT_QUEUE_GENERIC_READ
* D3D12DDI_BARRIER_LAYOUT_DIRECT_QUEUE_UNORDERED_ACCESS
* D3D12DDI_BARRIER_LAYOUT_DIRECT_QUEUE_SHADER_RESOURCE
* D3D12DDI_BARRIER_LAYOUT_DIRECT_QUEUE_COPY_SOURCE
* D3D12DDI_BARRIER_LAYOUT_DIRECT_QUEUE_COPY_DEST

The DIRECT_QUEUE layout variants are not compatible with compute queues and can't be used in compute command list barriers. However, they're compatible with compute operations in direct queues.

### Barrier-free access

Since there must be no pending commands or cache flush operations between ExecuteCommandLists boundaries, buffers might be initially accessed in an ExecuteCommandLists scope without a barrier. Likewise, texture subresources might also be initially accessed without a barrier under the following conditions:

* The subresource layout is compatible with the access type.
* Any necessary compression metadata has been initialized.

Texture subresources in layout D3D12DDI_BARRIER_LAYOUT_COMMON (or a queue-specific common layout such as D3D12DDI_BARRIER_LAYOUT_DIRECT_QUEUE_COMMON) that have no potentially outstanding read or write operations can be accessed in an ExecuteCommandLists command stream without a barrier using any of the following access types:

* D3D12DDI_BARRIER_ACCESS_SHADER_RESOURCE
* D3D12DDI_BARRIER_ACCESS_COPY_SOURCE
* D3D12DDI_BARRIER_ACCESS_COPY_DEST

Additionally, a buffer or texture using a queue-specific common layout can use D3D12DDI_BARRIER_ACCESS_UNORDERED_ACCESS without a barrier.

Buffers and simultaneous-access textures (textures created with the D3D12DDI_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS flag) can be initially accessed in an ExecuteCommandLists command stream without a barrier using any of the following access types:

* D3D12DDI_BARRIER_ACCESS_VERTEX_BUFFER
* D3D12DDI_BARRIER_ACCESS_CONSTANT_BUFFER
* D3D12DDI_BARRIER_ACCESS_INDEX_BUFFER
* D3D12DDI_BARRIER_ACCESS_RENDER_TARGET
* D3D12DDI_BARRIER_ACCESS_UNORDERED_ACCESS
* D3D12DDI_BARRIER_ACCESS_SHADER_RESOURCE
* D3D12DDI_BARRIER_ACCESS_STREAM_OUTPUT
* D3D12DDI_BARRIER_ACCESS_INDIRECT_ARGUMENT
* D3D12DDI_BARRIER_ACCESS_COPY_DEST
* D3D12DDI_BARRIER_ACCESS_COPY_SOURCE
* D3D12DDI_BARRIER_ACCESS_RESOLVE_DEST
* D3D12DDI_BARRIER_ACCESS_RESOLVE_SOURCE
* D3D12DDI_BARRIER_ACCESS_PREDICATION

Subsequent accesses can also be made without a barrier with no more than one write access type. However, except for D3D12DDI_BARRIER_ACCESS_RENDER_TARGET, barriers must be used to flush sequential writes to the same resource.

### Self Resource Copy

Though not exclusively related to the enhanced barriers, the ability to allow copies from one region of a subresource to another non-intersecting region is a highly requested feature. With enhanced barriers, a subresource with a common layout can be used as both a source and destination in the same CopyBufferRegion or CopyTextureRegion call. Copies between intersecting source and destination memory regions produce undefined results. The Debug Layer MUST validate against such results. (The legacy resource barrier design doesn't allow a subresource to be in both the D3D12DDI_RESOURCE_STATE_COPY_SOURCE and D3D12DDI_RESOURCE_STATE_COPY_DEST state at the same time, and thus can't copy to itself.)

### Placed resource metadata initialization

The legacy resource barrier design requires newly placed and activated aliased texture resources to be initialized by Clear, Copy, or Discard before being used as a Render Target or Depth Stencil resource. This requirement is because Render Target and Depth Stencil resources typically use compression metadata that must be initialized for the data to be valid. The same goes for reserved textures with newly updated tile mapping.

Enhanced barriers support an option to Discard as part of a barrier. Barrier layout transitions from D3D12DDI_BARRIER_LAYOUT_UNDEFINED to any potentially compressed layout (for example, D3D12DDI_BARRIER_LAYOUT_RENDER_TARGET, D3D12DDI_BARRIER_LAYOUT_DEPTH_STENCIL, D3D12DDI_BARRIER_LAYOUT_UNORDERED_ACCESS) MUST initialize compression metadata when D3D12DDI_TEXTURE_BARRIER_FLAG_DISCARD is present in the D3D12DDI_TEXTURE_BARRIER::Flags member.

In addition to render target and depth/stencil resources, there are similar UAV texture compression optimizations that the legacy barrier model didn't support.

### Barrier Ordering

Barriers are queued in forward order (API-call order, barrier-group-index, barrier-array-index). Multiple barriers on the same subresource must function as though the barriers complete in queued order.

Queued barriers with matching **SyncAfter** scopes that potentially write to the same memory must complete all writes in queued order. This requirement avoids data races on barriers that support resource aliasing. For example, a barrier that ‘deactivates’ a resource must flush any caches before another barrier that ‘activates a different resource on the same memory, possible clearing metadata.
