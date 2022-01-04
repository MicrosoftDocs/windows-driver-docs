---
title: Threading and Synchronization First Level
description: Threading and Synchronization First Level
keywords:
- threading WDK display , first level
- synchronization WDK display , first level
ms.date: 08/05/2020
---

# Threading and Synchronization First Level

The Windows Display Driver Model (WDDM) categorizes calls into the display miniport driver that are made under the first level of threading and synchronization into the following nonreentrancy classes. No reentrancy is permitted within a particular class; that is, only one thread can enter the driver within a particular class. However, calls from multiple first-level classes and [zero-level](threading-and-synchronization-zero-level.md) calls can be entered simultaneously.

> [!NOTE]
>
> Although two or more threads from different first-level classes and threads from [zero-level](threading-and-synchronization-zero-level.md) calls can be running in the driver at the same time, no two threads can belong to a single process.

## Pointer Class

The Windows Display Driver Model (WDDM) does not permit a call into one of the pointer class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

* [*DxgkDdiSetPointerPosition*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setpointerposition)
* [*DxgkDdiSetPointerShape*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setpointershape)

## GPU Scheduler Class

The Windows Display Driver Model (WDDM) does not permit a call into one of the GPU scheduler loader class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

* [*DxgkDdiBuildPagingBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer)
* [*DxgkDdiPatch*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_patch)
* [*DxgkDdiPreemptCommand*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_preemptcommand)
* [*DxgkDdiQueryDependentEngineGroup*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_querydependentenginegroup)
* [*DxgkDdiQueryEngineStatus*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryenginestatus)
* [*DxgkDdiResetEngine*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetengine)
* [*DxgkDdiSubmitCommand*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand)

## Swizzling Range Class

The Windows Display Driver Model (WDDM) does not permit a call into one of the swizzling range class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

* [*DxgkDdiAcquireSwizzlingRange*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_acquireswizzlingrange)
* [*DxgkDdiReleaseSwizzlingRange*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_releaseswizzlingrange)

## Overlay Class

The Windows Display Driver Model (WDDM) does not permit a call into one of the overlay class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

* [*DxgkDdiCreateOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createoverlay)
* [*DxgkDdiDestroyOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyoverlay)
* [*DxgkDdiFlipOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_flipoverlay)
* [*DxgkDdiUpdateOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updateoverlay)

## Child I/O Class

The Windows Display Driver Model (WDDM) does not permit a call into one of the child I/O class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions per child device at a given time:

> [!NOTE]
>
> The child I/O class functions are synchronized per child device (that is, simultaneous calls to multiple child devices are allowed). However, if internal dependencies exist between child devices, the display miniport driver must block calls as required.

* [*DxgkDdiQueryChildStatus*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_status)
* [DxgkDdiQueryConnectionChange](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange)
* [*DxgkDdiQueryDeviceDescriptor*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_device_descriptor)
* [*DxgkDdiDisplayDetectControl*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_displaydetectcontrol)
* [*DxgkDdiI2CReceiveDataFromDisplay*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_i2c_receive_data_from_display)
* [*DxgkDdiI2CTransmitDataToDisplay*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_i2c_transmit_data_to_display)
* [*DxgkDdiOPMConfigureProtectedOutput*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output)
* [*DxgkDdiOPMCreateProtectedOutput*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_create_protected_output)
* [*DxgkDdiOPMDestroyProtectedOutput*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_destroy_protected_output)
* [*DxgkDdiOPMGetCertificate*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_certificate)
* [*DxgkDdiOPMGetCertificateSize*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_certificate_size)
* [*DxgkDdiOPMGetCOPPCompatibleInformation*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information)
* [*DxgkDdiOPMGetInformation*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information)
* [*DxgkDdiOPMGetRandomNumber*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_random_number)
* [*DxgkDdiOPMSetSigningKeyAndSequenceNumbers*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_set_signing_key_and_sequence_numbers)

## Display Class

The Windows Display Driver Model (WDDM) does not permit a call into one of the display class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

* [*DxgkDdiSetTargetGamma*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settargetgamma)
* [*DxgkDdiSetTargetContentType*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settargetcontenttype)
* [*DxgkDdiSetTargetAnalogCopyProtection*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settargetanalogcopyprotection)
* [*DxgkDdiSetTargetAdjustedColorimetry*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_settargetadjustedcolorimetry)
