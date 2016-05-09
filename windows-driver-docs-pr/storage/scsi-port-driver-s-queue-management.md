---
title: SCSI Port Driver's Queue Management
description: SCSI Port Driver's Queue Management
ms.assetid: ddcbd016-8d8b-4bbc-9c71-b7a5eaa61205
---

# SCSI Port Driver's Queue Management


## <span id="ddk_scsi_port_driver_s_queue_management_kg"></span><span id="DDK_SCSI_PORT_DRIVER_S_QUEUE_MANAGEMENT_KG"></span>


SCSI host adapters vary greatly in the volume of I/O requests that they can handle. In order to avoid overwhelming the capability of any particular host adapter, either the storage class driver or the storage port driver must be able to control the flow of I/O requests.

In the Microsoft Windows storage architecture, the SCSI Port driver handles most aspects of I/O flow control. Storage class drivers can therefore forward any number of I/O requests to SCSI Port without testing the limits of particular adapters. SCSI Port also accepts explicit requests from storage class drivers to halt queue processing.

The SCSI Port driver is said to "freeze" its I/O request queue whenever it halts the processing of queued requests in response to an error condition reported by the underlying hardware. SCSI Port is said to "lock" its I/O request queue whenever it halts processing in response to an explicit request from the class driver or some other higher-level driver.

The following sections describe the conditions that cause SCSI Port to change the status of its queue. They also describe the SRBs that higher-level drivers can use to exert control over SCSI Port's internal I/O request queue.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Port%20Driver's%20Queue%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




