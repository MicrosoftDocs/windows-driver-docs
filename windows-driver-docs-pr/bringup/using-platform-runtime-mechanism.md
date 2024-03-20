---
title: Using Platform Runtime Mechanism (PRM)
description: Describes the steps required to use the PRM interface
ms.author: tedhudek
ms.date: 03/19/2024
---

# Using Platform Runtime Mechanism (PRM)

PRM is an architectural UEFI (Unified Extensible Firmware Interface) interface callable by any kernel-mode component during OS runtime. PRM replaces SMM (Secure Management Mode) calls with a GUID-defined interface.

Before you get started, you should have a working knowledge of Extensible Firmware Interface (EFI) in general.

To use Platform Runtime Mechanism (PRM), your driver should follow the steps described in the following list.

You can also find working sample code at [PrmFunc](https://github.com/microsoft/Windows-driver-samples/tree/develop/prm/PrmFunc).

For more information about the routines in this interface, see [**PRM_INTERFACE**](/windows-hardware/drivers/ddi/prminterface/ns-prminterface-prm_interface).

## Step 1: Obtain a PRM interface object

First the driver calls the [**ExGetPrmInterface**](/windows-hardware/drivers/ddi/prminterface/nf-prminterface-exgetprminterface) routine to obtain a PRM interface object. This object contains the PRM operations interface.

## Step 2:

The driver calls the [*PRM_LOCK_MODULE*](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_lock_module) routine to synchronize against any potential runtime update to the PRM module. The lock and unlock calls are only required if a series of PRM handlers need to be called transactionally but using them is recommended.

The GUID provided in this call comes from the UEFI specification and is the same GUID that is used to define the PRM interface. The driver should have a GUID defined in its code that matches the GUID defined in the UEFI specification. The driver should use this GUID to call the PRM_LOCK_MODULE routine.

## Step 3:

The driver calls the [*PRM_QUERY_HANDLER*](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_query_handler) routine.

This call queries for the presence of the PRM handler for the given GUID. If the handler is present, the driver can call the PRM_INVOKE_HANDLER routine to invoke the handler. If the handler is not present, the driver should not call the PRM_INVOKE_HANDLER routine.

## Step 4:

The driver calls the [*PRM_INVOKE_HANDLER*](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_invoke_handler) routine.

This call invokes the PRM handler for the given GUID. The driver should pass the GUID and the parameter buffer to the PRM_INVOKE_HANDLER routine. The parameter buffer should contain the parameters that the driver wants to pass to the PRM handler. The *EfiStatus* parameter is an output parameter that contains the status of the PRM handler invocation. (EFI stands for Extensible Firmware Interface.)

```c
        Status = PrmInterface.InvokeHandler(
                (LPGUID)&TestParameters->Guid,
                TestParameters->ParameterBuffer,
                0,
                &EfiStatus);
```

## Step 5:

The driver calls the [*PRM_UNLOCK_MODULE*](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_unlock_module) routine to release the PRM interface object.
