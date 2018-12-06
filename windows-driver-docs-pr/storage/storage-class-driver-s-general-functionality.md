---
title: Storage Class Driver's General Functionality
description: Storage Class Driver's General Functionality
ms.assetid: 4fc92d20-5570-4680-bc7b-f6e84524a672
keywords:
- storage class drivers WDK , functionality
- class drivers WDK storage , functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's General Functionality


## <span id="ddk_storage_class_drivers_general_functionality_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_GENERAL_FUNCTIONALITY_KG"></span>


To a storage port driver, a storage class driver is a higher-level driver with built-in, device-type-specific functionality. In general, every storage class driver is responsible for the following:

-   Claiming each device represented by a physical device object (PDO) passed to its *AddDevice* routine by the PnP manager

-   For each such PDO, creating a functional device object (FDO) and attaching it to the device stack

-   If the driver controls a partitionable device, creating physical device objects (PDOs) to represent each partition and responding to enumeration requests

-   Interpreting system I/O requests (IRPs)

-   Mapping IRPs to SCSI class/port interface requests (SRBs with SCSI CDBs)

-   Establishing time-out values for requests

-   Limiting the size of data transfers to suit the limits of the underlying HBA

-   Handling error conditions that are not already handled by the storage port driver, such as check-condition status or bus resets

 

 




