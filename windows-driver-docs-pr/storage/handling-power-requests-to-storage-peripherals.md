---
title: Handling Power Requests to Storage Peripherals
description: Handling Power Requests to Storage Peripherals
ms.assetid: 3cc7b885-27ad-4384-aeec-4d76f9ad4f1c
keywords:
- peripherals WDK storage , power requests
- storage peripherals WDK , power requests
- power requests WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Power Requests to Storage Peripherals


## <span id="ddk_handling_power_requests_to_storage_peripherals_kg"></span><span id="DDK_HANDLING_POWER_REQUESTS_TO_STORAGE_PERIPHERALS_KG"></span>


A storage class driver is responsible for issuing device-specific commands to handle power requests. Most commonly, a storage class driver:

-   Blocks I/O to its device in response to a query-power request (IRP\_MJ\_POWER with [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)) if handling such I/O might prevent the driver from succeeding a set-power request in a reasonable amount of time

-   Sets the power state of its device in response to a set-power request (IRP\_MJ\_POWER with [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744))

-   Restarts I/O to its device in response to a set-power request to power up the device

-   Forwards power requests to the next-lower driver.

Note that a driver must call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) and [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654), not **IoCallDriver**, to send power requests.

Unless the storage class driver has a [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, it should lock the storage port driver's LU-specific queue (IRP\_MJ\_SCSI with SRB\_FUNCTION\_LOCK\_QUEUE) before setting the device's power state, to block unsynchronized operations until the power operation (which may involve several steps) is complete. Any SRBs issued to handle the power operation should set SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE to make sure they reach the port driver. After the driver finishes setting the power state, it should unlock the queue (IRP\_MJ\_SCSI with SRB\_FUNCTION\_UNLOCK\_QUEUE and SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE) so that the port driver can resume sending queued IRPs to the device once it has been powered up.

If a storage class driver has a *StartIo* routine, that routine handles synchronization so the class driver does not have to explicitly lock and unlock the port driver's LU-specific queue.

A class driver should not attempt to bypass a queue locked by another driver.

 

 




