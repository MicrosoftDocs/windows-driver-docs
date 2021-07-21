---
title: Storage Filter Driver's Device-Type-Specific Functionality
description: Storage Filter Driver's Device-Type-Specific Functionality
keywords:
- storage filter drivers WDK , device-type-specific functionality
- filter drivers WDK storage , device-type-specific functionality
- SFD WDK storage , device-type-specific functionality
- device-type-specific functionality WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Driver's Device-Type-Specific Functionality

Depending on the nature of its device, an storage filter driver (SFD) might be responsible for the following device-type-specific functionality:

- Translating data from or into a device-specific format before or after sending a transfer request to lower drivers if the device processes data in a nonstandard format

- Setting up IRPs with SRBs for port-driver-supported I/O control requests, for driver-defined I/O control requests, or for pass-through requests, as necessary for its device, and sending those IRPs to the next-lower driver

- Modifying class driver-supplied SRBs as necessary for its device

- Establishing time-out values for requests

- Supplying one or more [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routines and, like the corresponding storage class driver, handling certain error conditions and retries for device-specific requests that require special handling

In general, an SFD has the same responsibilities as a storage class driver for those requests that require device-specific handling. For a discussion of the functionality required of storage class drivers, see [Storage Class Drivers](introduction-to-storage-class-drivers.md).
