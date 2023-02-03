---
title: Sharing the backing store with KMD
description:  UMD and KMD can share the graphics allocation backing store
ms.date: 09/08/2022
keywords:
- UMD access to graphics allocation backing store from KMD
- Sharing graphics allocation backing store
---

# Sharing the backing store with KMD

Starting in Windows 11 version 22H2, the WDDM API was extended to allow access to a graphics allocation backing store from the kernel-mode driver (KMD). Using this API, both the user-mode driver (UMD) and KMD can access the same allocation memory. This feature can be used when UMD is running on the host or in a virtual machine using GPU paravirtualization (GPU-PV).

This feature has been back-ported to Windows 10 version 20H1. The DDI is available for WDDM 3.1 drivers or newer.

## WDDM graphics allocations and backing stores

Each graphics allocation in the WDDM model has a backing store, which is a committed memory buffer that holds the allocation content when it is not in video memory.

A graphics allocation is created by calling [**D3DKMTCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreateallocation). UMD passes private data for this allocation, which *Dxgkrnl* passes to KMD through a call to [**DXGKDDI_CREATEALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation). KMD returns the desired allocation flags to *Dxgkrnl*.

## Checking for feature availability

To check whether the backing store sharing feature is available, KMD must first call one of the following callbacks with [**FeatureId**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_feature_id) set to **DXGK_FEATURE_SHARE_BACKING_STORE_WITH_KMD**:

* [**DXGKCB_QUERYFEATURESUPPORT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_queryfeaturesupport) (available starting in WDDM 2.9)
* [**DXGKCB_ISFEATUREENABLED**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_isfeatureenabled)

The feature can only be used if the callback succeeds and **Enable** is set to TRUE.

## Feature flow

Once KMD has successfully determined that the feature is enabled, UMD calls [**D3DKMTCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreateallocation) to create a shared CPU-visible allocation and instructs KMD via private data that the allocation has to be shared with KMD. In the course of this call, the following occurs:

* KMD sets [**DXGK_ALLOCATIONINFOFLAGS2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_allocationinfoflags2)'s **ShareBackingStoreWithKmd** flag when the OS calls KMD's [**DXGKDDI_CREATEALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) callback. If the feature is not enabled, KMD must not set the **ShareBackingStoreWithKmd** flag.

* *Dxgkrnl* calls the [**DXGKDDI_SETALLOCATIONBACKINGSTORE**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setallocationbackingstore) DDI to give KMD a kernel-mode address to the allocation backing store.

* UMD calls [**D3DKMTLock2**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtlock2) to get the allocation's user-mode address.

## Properties of the allocation

The allocation created in this way must have the following properties:

* The allocation is allowed to be only in the system memory segment.
* The allocation must be created as shared.
* The allocation cannot use existing system memory as backing store.
* UMD can do any operation as for a regular allocation.
  * UMD can call [**D3DKMTLock2**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtlock2) to get a pointer to the allocation.
  * UMD can call [**D3DKMTMakeResident**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtmakeresident) to make the allocation accessible by the GPU.
