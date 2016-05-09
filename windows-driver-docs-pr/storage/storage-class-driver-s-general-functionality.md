---
title: Storage Class Driver's General Functionality
description: Storage Class Driver's General Functionality
ms.assetid: 4fc92d20-5570-4680-bc7b-f6e84524a672
keywords: ["storage class drivers WDK , functionality", "class drivers WDK storage , functionality"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20General%20Functionality%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




