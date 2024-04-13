---
title: Capabilities Provided by Storport
description: Capabilities Provided by Storport
ms.date: 03/16/2021
---

# Capabilities Provided by Storport

The Storport driver provides the following capabilities:

- **Addressing**

  Microsoft Windows supports systems that contain different types of I/O buses and/or several I/O buses of the same type. A common addressing scheme is needed to handle this variety.

  PCI devices can have both I/O port and memory register resources. Logical addresses help to make this distinction transparent to the port driver.

  Some systems contain HBAs that are connected to more than one bus; such an HBA might require several sets of address translations.

  Logical addresses are needed for portability across CISC-based and RISC-based machines.

- **Retrys and Error Handling**

  - Storage class drivers do not have to implement algorithms for retrying IRPs when devices are too busy to process them. The Storport driver implements this functionality.

  - The class driver sets a time-out value for requests, and Storport is responsible for enforcing it. However, the Storport driver can enforce the class driver's time-out values flexibly, taking the state of the bus into consideration. For example, if a fibre channel link managed by Storport drops for 20 seconds, Storport might suspend the time-out counter during the down time, so that, for instance, requests with a time out of 10 seconds will not fail until 10 seconds after the link comes back up. Storport increases the time-out values that are assigned to requests in response to an increase in I/O traffic, because with heavier I/O traffic, the devices will require more time to complete requests.

  - Storport handles target and controller-busy errors, as well as transport error conditions (in other words, errors that are related to the actual transmission of data on the bus). For example:
    - bus-parity errors
    - selection time outs

- **Configuration, Queuing, and Power State Management**

  - Providing class drivers with information about host adapter limitations: It is the responsibility of the class driver to regulate the size of data transfers to suit the limits of the host bus adapters (HBAs). However, Storport provides the class driver with the information it needs to accomplish this task. Storport furnishes this information in an adapter descriptor ([STORAGE_ADAPTER_DESCRIPTOR](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_adapter_descriptor)) in response to an IOCTL request ([**IOCTL_STORAGE_QUERY_PROPERTY**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property)). The class driver is responsible for breaking requests up into chunks of the appropriate size based on the information reported in this descriptor.

  - Translating bus relative addresses to logical addresses: When queried, adapters furnish bus-relative addresses for I/O ports, command registers, and control status registers. However, a miniport driver cannot use bus-relative addresses to communicate with its host bus adapter (HBA). Storport translates bus-relative addresses to logical addresses, so that miniport drivers can access bus addresses in a transparent manner. There are several reasons for this:

  - Ensuring that a device and all its underlying devices are powered up (at the D0 device power state) before the device is started: When a device is not ready to be powered up, Storport queues a D0 request for that device until the device is ready.

  - Queuing asynchronous requests from class drivers and forwarding them asynchronously to the target device: Class drivers do not have to wait for a request to complete before sending the next request. Storport assumes the responsibility of queuing these requests to avoid overwhelming the processing power of the underlying hardware.

  - Supporting both internal and external management of internal I/O request queues: Most queue management operations are initiated by Storport itself. For instance, Storport freezes its queue when an error occurs and reports the error condition to the class driver, so that the class driver can respond before further requests are processed. However, Storport also responds to requests from the class driver or other higher-level drivers to lock, unlock, freeze or unfreeze its internal request queue. Higher-level drivers can force Storport to unfreeze its internal queue using the SRB_FUNCTION_RELEASE_QUEUE request. For an explanation of what it means to "freeze," "lock" or "unlock" a queue, see [Storport Queue Management](storport-queue-management.md).

  - Translating errors that are reported by the device into SCSI-3 sense data format for processing by the class driver.

Storport provides services to the miniport driver by means of the Storport library routines. Miniport driver writers can call these routines rather than coding the functionality that they provide into a single monolithic port driver. Some of the most important services afforded by using these routines are as follows:

- A Storport miniport driver can delegate many OS-dependent initialization operations to Storport's [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize) library routine. For example, the Storport driver handles the details related to PnP and DMA mapping. This reduces the amount of work a Storport miniport driver needs to do. For an explanation of the initialization duties of a Storport miniport driver, see [Hardware Initialization with Storport](hardware-initialization-with-storport.md).

- Storport miniport drivers for non-PnP devices are spared the task of locating adapters and reporting their resources to the PnP manager. This is done in [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize).

- Storport miniport drivers do not initialize dispatch entry points in the driver object. The Storport driver does this on behalf of the miniport driver when the miniport driver calls [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize).

- Storport miniport drivers do not convert bus-relative addresses to logical addresses using **HalTranslateBusAddress**. Storport miniport drivers do this by a call to [**StorPortGetDeviceBase**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetdevicebase).

For a complete list of the library routines that Storport makes available to Storport miniport drivers, see [Storport Driver Support Routines](storport-driver-support-routines.md).
