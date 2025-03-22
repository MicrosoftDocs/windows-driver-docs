---
title: Windows Kernel-Mode Platform Runtime Mechanism (PRM) Library
description: Describes the steps required to use the PRM interface
ms.date: 03/22/2024
---

# Windows Kernel-Mode Platform Runtime Mechanism (PRM) Library

The Platform Runtime Mechanism (PRM) is a GUID-based interface that enables drivers to run handlers preloaded in Unified Extensible Firmware Interface (UEFI) firmware. PRM offers functionality similar to System Management Interrupt (SMI) calls in System Management Mode (SMM), but it's more secure.

During system runtime, the firmware may contain several PRM modules, each with a unique set of handlers.

Drivers can call PRM handlers for low-level operations such as controlling hardware components, managing thermal states, or advanced power management.

Follow these steps to check for the availability of a specific handler and to run it. You can find a sample implementation of this process in the [PrmFunc sample](https://github.com/microsoft/Windows-driver-samples/tree/develop/prm/PrmFunc).

1. Obtain a pointer to a [PRM_INTERFACE](/windows-hardware/drivers/ddi/prminterface/ns-prminterface-prm_interface) structure by calling the [**ExGetPrmInterface**](/windows-hardware/drivers/ddi/prminterface/nf-prminterface-exgetprminterface) routine. This structure contains pointers to the PRM operation routines.

1. Synchronize against potential runtime updates to the PRM module by calling the [**PRM_LOCK_MODULE**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_lock_module) routine. Lock and unlock calls are necessary for transactional series of PRM handler calls, but it's generally recommended to use them.

1. Check the presence of the specified PRM handler using the [**PRM_QUERY_HANDLER**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_query_handler) routine.

1. If the query succeeds, invoke the PRM handler by calling the [**PRM_INVOKE_HANDLER**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_invoke_handler) routine. Provide the GUID and the parameter buffer, which should contain the parameters for the PRM handler. The *EfiStatus* output parameter will indicate the status of the handler invocation.

1. If you previously called **PRM_LOCK_MODULE**, release the PRM interface object by calling the [**PRM_UNLOCK_MODULE**](/windows-hardware/drivers/ddi/prminterface/nc-prminterface-prm_unlock_module) routine.

## See also

For more information, refer to the [PRM specification](https://uefi.org/sites/default/files/resources/Platform%20Runtime%20Mechanism%20-%20with%20legal%20notice.pdf).
