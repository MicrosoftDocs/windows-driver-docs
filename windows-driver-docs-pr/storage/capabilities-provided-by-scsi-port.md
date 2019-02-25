---
title: Capabilities Provided by SCSI Port
description: Capabilities Provided by SCSI Port
ms.assetid: 549dc3f1-b62f-4047-bdc0-7e24d5bc6ad5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capabilities Provided by SCSI Port


## <span id="ddk_capabilities_provided_by_scsi_port_kg"></span><span id="DDK_CAPABILITIES_PROVIDED_BY_SCSI_PORT_KG"></span>


The SCSI Port driver provides the following capabilities:

-   Microsoft Windows supports systems that contain different types of I/O buses and/or several I/O buses of the same type. A common addressing scheme is needed to handle this variety.

-   PCI devices can have both I/O port and memory register resources. Logical addresses help to make this distinction transparent to the port driver.

-   Some systems contain HBAs that are connected to more than one bus; such an HBA might require several sets of address translations.

-   Logical addresses are needed for portability across CISC-based and RISC-based machines.

<!-- -->

-   Retrying IRPs when a device is too busy to process them.

    Storage class drivers do not have to implement algorithms for retrying IRPs when devices are too busy to process them. The SCSI Port driver implements this functionality.

-   Enforcing time-out values for requests.

    The class driver sets a time-out value for requests, and SCSI Port is responsible for enforcing it. However, the SCSI Port driver can enforce the class driver's time-out values flexibly, taking the state of the bus into consideration. For example, if a fibre channel link managed by SCSI Port drops for 20 seconds, SCSI Port might suspend the time-out counter during the down time, so that, for instance, requests with a time out of 10 seconds will not fail until 10 seconds after the link comes back up. SCSI Port increases the time-out values that are assigned to requests in response to an increase in I/O traffic, because with heavier I/O traffic, the devices will require more time to complete requests.

-   Handling target and controller-busy errors, as well as transport error conditions (in other words, errors that are related to the actual transmission of data on the bus). For example:

-   1.  bus-parity errors
    2.  selection time outs

<!-- -->

-   Providing class drivers with information about host adapter limitations.

    It is the responsibility of the class driver to regulate the size of data transfers to suit the limits of the host bus adapters (HBA). However, SCSI Port provides the class driver with the information it needs to accomplish this task. SCSI Port furnishes this information in an adapter descriptor ([**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346)) in response to an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) IOCTL request. The class driver is responsible for breaking requests up into chunks of the appropriate size based on the information reported in this descriptor.

-   Translating bus relative addresses to logical addresses.

    When queried, adapters furnish bus-relative addresses for I/O ports, command registers, and control status registers. However, a miniport driver cannot use bus-relative addresses to communicate with its host bus adapter (HBA). SCSI Port translates bus relative addresses to logical addresses, so that miniport drivers can access bus addresses in a transparent manner. There are several reasons for this:

-   Ensuring that a device and all its underlying devices are powered up (at the D0 device power state) before the device is started.

    When a device is not ready to be powered up, SCSI Port queues a D0 request for that device until the device is ready.

-   Queuing asynchronous requests from class drivers and forwarding them synchronously to the target device.

    Class drivers do not have to wait for a request to complete before sending the next request. SCSI Port assumes the responsibility of queuing these requests to avoid overwhelming the processing power of the underlying hardware.

-   Supporting both internal and external management of internal I/O request queues.

    Most queue management operations are initiated by SCSI Port itself. For instance, SCSI Port freezes its queue when an error occurs and reports the error condition to the class driver, so that the class driver can respond before further requests are processed. However, SCSI Port also responds to requests from the class driver or other higher-level drivers to lock, unlock, freeze or unfreeze its internal request queue. Higher-level drivers can force SCSI Port to unfreeze its internal queue using the SRB\_FUNCTION\_RELEASE\_QUEUE request. For an explanation of what it means to "freeze," "lock" or "unlock" a queue, see [SCSI Port Driver's Queue Management](scsi-port-driver-s-queue-management.md).

-   Translating errors that are reported by the device into SCSI-2 sense data format for processing by the class driver.

SCSI Port provides services to the miniport driver by means of the SCSI Port library routines. Miniport driver writers can call these routines rather than coding the functionality that they provide into a single monolithic port driver. Some of the most important services afforded by using these routines are as follows:

-   A SCSI Port miniport driver can delegate many OS-dependent initialization operations to SCSI Port's [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) library routine. This makes a SCSI Port miniport driver more portable across different versions of the operating system. For an explanation of the initialization duties of a SCSI Port miniport driver, see [SCSI Miniport Driver's DriverEntry Routine](scsi-miniport-driver-s-driverentry-routine.md).

-   SCSI Port miniport drivers for non-PnP devices are spared the task of locating adapters and reporting their resources to the PnP manager. This is done in [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645).

-   SCSI Port miniport drivers do not initialize dispatch entry points in the driver object. The SCSI Port driver does this on behalf of the miniport driver when the miniport driver calls [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645).

-   SCSI Port miniport drivers do not convert bus-relative addresses to logical addresses using [**HalTranslateBusAddress**](https://msdn.microsoft.com/library/windows/hardware/ff546637). SCSI Port miniport drivers do this by a call to [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629).

For a complete list of the library routines that SCSI Port makes available to SCSI Port miniport drivers, see [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375).

 

 




