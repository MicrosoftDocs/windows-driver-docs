---
title: SCSI Port Driver's Queue Management
description: SCSI Port Driver's Queue Management
ms.assetid: ddcbd016-8d8b-4bbc-9c71-b7a5eaa61205
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Port Driver's Queue Management


## <span id="ddk_scsi_port_driver_s_queue_management_kg"></span><span id="DDK_SCSI_PORT_DRIVER_S_QUEUE_MANAGEMENT_KG"></span>


SCSI host adapters vary greatly in the volume of I/O requests that they can handle. In order to avoid overwhelming the capability of any particular host adapter, either the storage class driver or the storage port driver must be able to control the flow of I/O requests.

In the Microsoft Windows storage architecture, the SCSI Port driver handles most aspects of I/O flow control. Storage class drivers can therefore forward any number of I/O requests to SCSI Port without testing the limits of particular adapters. SCSI Port also accepts explicit requests from storage class drivers to halt queue processing.

The SCSI Port driver is said to "freeze" its I/O request queue whenever it halts the processing of queued requests in response to an error condition reported by the underlying hardware. SCSI Port is said to "lock" its I/O request queue whenever it halts processing in response to an explicit request from the class driver or some other higher-level driver.

The following sections describe the conditions that cause SCSI Port to change the status of its queue. They also describe the SRBs that higher-level drivers can use to exert control over SCSI Port's internal I/O request queue.

 

 




