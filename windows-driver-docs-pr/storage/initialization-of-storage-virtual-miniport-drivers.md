---
title: Implementing a Storport virtual miniport driver
description: Implementing a Storport virtual miniport driver
keywords:
- storage virtual miniport drivers WDK , initialization
- storage virtual miniport drivers , implementing
- miniport drivers WDK storage
- initializing WDK storage , virtual miniport drivers
ms.date: 03/01/2022
---

# Implementing a Storport virtual miniport driver

This page provides high-level implementation information for a Storport virtual miniport driver (VMiniport). The VMiniport interface is defined in *storport.h*.

Design considerations are unique to various VMiniports, so implementation specifics are not included here.

## The VMiniport interface

This section lists the more prominent functions, callbacks, and structures that a VMiniport implements/uses. Some functions and callbacks are required; the optional callbacks are unique to a VMiniport's design.

* [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), which is the first routine that the operating system calls after the VMiniport is loaded. This routine is required.

* [**HW_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data-r1), which is a Vminiport-allocated and initialized structure that the VMiniport passes to Storport during [initialization](#vminiport-initialization). The VMiniport provides pointers to its callback functions in this structure.

  The following callback routines are required:

  * [**HwFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter)

  * [**HwInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize)

  * [**HwStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio)

  * [**HwAdapterControl**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_adapter_control)

  * [**HwResetBus**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_reset_bus). The meaning of "bus" can be defined by the VMiniport developer.

  * [**HwFreeAdapterResources**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_free_adapter_resources). This routine is called when the virtual adapter is being removed so that the VMiniport can free any resources that are allocated during initialization.

  The following callback routines are optional, though a VMiniport might have to implement some of them depending on its unique architecture:

  * [**HwInitializeTracing**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize_tracing)

  * [**HwCleanupTracing**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_cleanup_tracing). This routine is required when [**HwInitializeTracing**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize_tracing) points to a callback routine; otherwise, this routine is optional, and is unique to a VMiniport.

  * [**HwProcessServiceRequest**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_process_service_request). This routine receives a "reverse-callback" IRP, which will be completed when the VMiniport updates the caller (such as a user-mode application or kernel-mode driver) or requires the caller to do something on the VMiniport's behalf.

  * [**HwCompleteServiceIrp**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_complete_service_irp). This routine is required when [**HwProcessServiceRequest**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_process_service_request) points to a callback routine; otherwise, this routine is optional and is unique to a VMiniport.**HwCompleteServiceIrp** is called when the virtual adapter is being removed so that the VMiniport can complete any reverse-callback IRPs that might be pending.

  The VMiniport must also set the following members of the [**HW_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data-r1) structure:

  * Set **HwInitializationDataSize** to **sizeof**(HW_INITIALIZATION_DATA).

  * Set **AdapterInterfaceType** to **Internal**, which indicates to Storport that this is a virtual adapter.

  * Set [**HwBuildIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio) to NULL.

  The Vminiport driver sets other fields as needed. Unused fields must be set to zero.

* [**PORT_CONFIGURATION_INFORMATION**](/windows-hardware/drivers/ddi/storport/ns-storport-_port_configuration_information), which is a Storport-allocated structure. Storport initializes some **PORT_CONFIGURATION_INFORMATION** members and then passed it to the VMiniport's [**HwFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) callback, where the VMiniport completes the initialization. Since this structure is pre-initialized by Storport, **HWFindAdapter** must not zero out the structure. A VMiniport must set **VirtualDevice** to TRUE.

## VMiniport initialization

A VMiniport has three stages of initialization.

* In the first stage, the VMiniport's [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine calls [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize) with a pointer to its initialized [**HW_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data-r1) structure.

* Storport calls the VMiniport's [**HwFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) callback with a Storport-allocated and partially initialized [**PORT_CONFIGURATION_INFORMATION**](/windows-hardware/drivers/ddi/storport/ns-storport-_port_configuration_information) structure. The principal function of **HwFindAdapter** is to complete the initialization of **PORT_CONFIGURATION_INFORMATION**, including setting the **VirtualDevice** member to TRUE.

* After [**HwFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) successfully returns, Storport calls the VMiniport's [**HwInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize) callback to complete initialization of the VMiniport.

## VMiniport I/O

Storport calls a VMiniport's [**HwStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) callback to initiate an I/O request. In Storport, an I/O request is described using a [**SCSI_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/storport/ns-storport-_scsi_request_block) or [**STORAGE_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/storport/ns-storport-_storage_request_block) (standard or extended SRB, respectively).

Unlike a physical miniport driver, Storport does not call [**HwBuildIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio) in a Vminiport prior to calling [**HwStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio).

No locks are held prior to calling **HwStartIo**. The default queue depth for each logical unit that is exposed through the virtual miniport interface is 250.
