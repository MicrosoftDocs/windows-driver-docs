---
title: Windows Kernel-Mode Platform Runtime Mechanism (PRM) Library
description: Describes the steps required to use the PRM interface
ms.author: tedhudek
ms.date: 03/22/2024
---

# Windows Kernel-Mode Platform Runtime Mechanism (PRM) Library

PRM (Platform Runtime Mechanism) is a GUID-based interface that a driver can use to run handlers that have been preloaded in UEFI (Unified Extensible Firmware Interface) firmware. PRM provides similar functionality to SMI (System Management Interrupt) calls that operate in SMM (System Management Mode), but with improved security.

At system runtime, there may be multiple PRM modules in the firmware, each with its own set of handlers.

A driver might call PRM handlers to perform low-level operations such as controlling hardware components, managing thermal states, or advanced power management.

Use the following procedure to query for the availability of a specific handler and then to run it. You can find an implementation of this sequence in the [PrmFunc sample](https://github.com/microsoft/Windows-driver-samples/tree/develop/prm/PrmFunc).

1. Call the [**ExGetPrmInterface**](/windows-hardware/drivers/ddi/prminterface/nf-prminterface-exgetprminterface) routine to obtain a pointer to a [PRM_INTERFACE](/windows-hardware/drivers/ddi/prminterface/ns-prminterface-prm_interface) structure, which contains pointers to the individual PRM operations routines.

1. Use the provided function pointer to call the [**PRM_LOCK_MODULE**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_lock_module) routine to synchronize against any potential runtime update to the PRM module. The lock and unlock calls are only required if a series of PRM handlers need to be called transactionally but using them is recommended.

1. Call the [**PRM_QUERY_HANDLER**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_query_handler) routine to query for the presence of the specified PRM handler.

1. If the query was successful, the driver can now call the [**PRM_INVOKE_HANDLER**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_invoke_handler) routine.

    This call invokes the PRM handler for the given GUID. The driver should pass the GUID and the parameter buffer to the PRM_INVOKE_HANDLER routine. The parameter buffer should contain the parameters that the driver wants to pass to the PRM handler. The *EfiStatus* (Extensible Firmware Interface) parameter is an output parameter that contains the status of the PRM handler invocation.

1. If it called **PRM_LOCK_MODULE**, the driver calls the [**PRM_UNLOCK_MODULE**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_unlock_module) routine to release the PRM interface object.

## See also

[PRM specification](https://uefi.org/sites/default/files/resources/Platform%20Runtime%20Mechanism%20-%20with%20legal%20notice.pdf)
