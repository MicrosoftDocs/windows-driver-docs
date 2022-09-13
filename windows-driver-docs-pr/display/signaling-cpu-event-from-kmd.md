---
title: Signaling a CPU event from KMD
description: How to signal a CPU event from KMD
ms.date: 09/12/2022
keywords:
- Signal a CPU event from KMD
- Signal a CPU event from kernel-mode driver
---

# Signaling a CPU event from a kernel-mode driver

There are cases when the kernel-mode driver (KMD) needs to signal a CPU event to notify the user-mode driver (UMD) about something. Typically, UMD can create a CPU event and pass its NT handle to KMD in an escape private data. This method does not work in the GPU paravirtualization (GPU-PV) scenario because NT handles cannot be used across virtual machine boundaries.

Starting in Windows 11 version 21H2 (WDDM 3.0), the WDDM API was extended to allow UMD to create a CPU event object that can be signaled by KMD. This feature works both when UMD is running on the host or in a virtual machine using GPU-PV.

## Feature flow

* UMD creates a CPU event.

* UMD [creates a GPU synchronization object](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_createsynchronizationobject2cb) with the [**D3DDDI_CPU_NOTIFICATION**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddi_synchronizationobject_type) type. The created object is made visible to KMD by setting the [**SignalByKmd**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_synchronizationobject_flags) flag when calling [**D3DKMTCreateSynchronizationObject**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatesynchronizationobject2).

* *Dxgkrnl* calls [**DXGKDDI_CREATECPUEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcpuevent) to allow the driver to create its own object.

* UMD calls [**D3DKMTEscape**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtescape) with the **D3DDDI_DRIVERESCAPETYPE_CPUEVENTUSAGE** known escape type to notify KMD about intended usage of the synchronization object.

* *Dxgkrnl* calls [**DXGKDDI_ESCAPE**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_escape) to pass the private data to KMD.

* At some point KMD calls [**DXGKCB_SIGNALEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_signalevent) with the **CpuEventObject** flag to signal the CPU event object.

* UMD calls [**D3DKMTDestroySynchronizationObject**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtdestroysynchronizationobject) to destroy the CPU event object.

* *Dxgkrnl* calls [**DXGKDDI_DESTROYCPUEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroycpuevent) to destroy the CPU event object. [**DXGKCB_SIGNALEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_signalevent) should be called after this point.

The synchronization object cannot be inserted to a context queue. It can only be signaled by KMD using [**DXGKCB_SIGNALEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_signalevent).

## User-mode APIs to handle CPU event sync objects

### Creation of the KMD CPU event object

The KMD CPU event object is created as a GPU synchronization object by calling [**D3D12DDICB_CREATESYNCHRONIZATIONOBJECT2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddicb_createsynchronizationobject2) with:

* [**Type**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddi_synchronizationobject_type) set to **D3DDDI_CPU_NOTIFICATION**.

* [**Flags**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_synchronizationobject_flags) set to **SignalByKmd** to specify that the object will be signaled by KMD. This flag can be set only when the [**Type**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddi_synchronizationobject_type) member of[**D3DDDI_SYNCHRONIZATIONOBJECTINFO2**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_synchronizationobjectinfo2) is **D3DDDI_CPU_NOTIFICATION**.

When the **SignalByKmd** flag is set, [**DXGKDDI_CREATECPUEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcpuevent) will be called to create the KMD CPU event object. Note that the device handle must be specified when creating the synchronization object.

The synchronization object cannot be used in signal and wait APIs (**D3DKMTSignalSynchronizationObject**, **D3DKMTWaitForSynchronizatioObject**). It can be signaled only by KMD, and UMD can wait on the corresponding CPU event.

### UMD escape to define the usage for a KMD CPU event sync object

A known escape was added to [**D3DDDI_DRIVERESCAPETYPE**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddi_driverescapetype). **D3DDDI_DRIVERESCAPETYPE_CPUEVENTUSAGE** is used to notify KMD about the intended usage of a KMD CPU event object. A known escape is defined by setting [**DXGKARG_ESCAPE::Flags.DriverKnownEscape**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_escape) = 1. Known escapes are sent to the host even from secure virtual machines.

The following snippet is a usage example.

``` C++
D3DDDI_DRIVERESCAPE_CPUEVENTUSAGE Command = {};
Command.EscapeType = D3DDDI_DRIVERESCAPETYPE_CPUEVENTUSAGE;
Command.hSyncObject = SyncObjectHandle;
Command.Usage[0] = 1;

D3DKMT_ESCAPE Args = {};
Args.hAdapter = AdapterHandle;
Args.Type = D3DKMT_ESCAPE_DRIVERPRIVATE;
Args.Flags.DriverKnownEscape = 1;
Args.Flags.NoAdapterSynchronization = 1; // Prevent waking up the device from D3
Args.pPrivateDriverData = &Command;
Args.PrivateDriverDataSize = sizeof(Command);

NTSTATUS Status = D3DKMTEscape(&Args);
```

*Dxgkrnl* will call [**DXGKDDI_ESCAPE**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_escape) with the following:

* **hDevice** set to the miniport device handle that was used to create the sync object
* [**pPrivateDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_escape) pointing to a **D3DDDI_DRIVERESCAPE_CPUEVENTUSAGE** structure
* **PrivateDriverDataSize** set to ```sizeof(D3DDDI_DRIVERESCAPE_CPUEVENTUSAGE)```

## Creating and destroying a KMD CPU event object

The following DDIs are used to create and destroy KMD CPU event sync objects:

* [**DXGKDDI_CREATECPUEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcpuevent)
* [**DXGKDDI_DESTROYCPUEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroycpuevent)

## Signalling a CPU event object from KMD

To signal a CPU event object, KMD calls [**DXGKCB_SIGNALEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_signalevent) at IRQL <= DISPATCH_LEVEL and with the [**DXGKARGCB_SIGNALEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_signalevent) structure values set as follows:

* **hDxgkProcess** equals 0.

* **hEvent** equal to the *Dxgkrnl* CPU event object handle passed in to [**DXGKDDI_CREATECPUEVENT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcpuevent).

* **CpuEventObject** must be 1.

* **Reserved** must be 0.
