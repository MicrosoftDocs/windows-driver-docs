---
title: Storage Class Driver's BuildRequest Routine
author: windows-driver-content
description: Storage Class Driver's BuildRequest Routine
ms.assetid: 2ba26628-4862-440c-b8f1-dd983cf9923b
keywords: ["BuildRequest", "I/O stack locations WDK storage", "retrying requests WDK storage", "SCSI request sense WDK storage", "request sense WDK storage"]
---

# Storage Class Driver's BuildRequest Routine


## <span id="ddk_storage_class_drivers_buildrequest_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_BUILDREQUEST_ROUTINE_KG"></span>


Like all higher-level kernel-mode drivers, a storage class driver must set up the IRP's I/O stack location for the next-lower driver when [Handling Requests to Storage Peripherals](handling-requests-to-storage-peripherals.md). In IRPs that the class driver sets up with SRBs for the system-supplied port driver, the port driver's I/O stack location is set with the following:

-   **MajorFunction** contains IRP\_MJ\_SCSI

-   **Parameters.Scsi.Srb** contains a pointer to the SRB

Each class driver is responsible for allocating memory for SRBs as well as for setting them up with CDBs for the underlying storage port driver. The class driver can either set up a lookaside list for its SRBs with **ExInitializeNPageLookasideList** or call **ExAllocatePool** for nonpaged memory. See [Using Lookaside Lists](https://msdn.microsoft.com/library/windows/hardware/ff565416) for more information about using lookaside lists and nonpaged pool.

Whether it allocates memory from pool or from a driver-created lookaside list, every storage class driver is responsible for freeing the memory it allocates for SRBs. Storage class drivers' *IoCompletion* routines, described in [Storage Class Driver's IoCompletion Routines](storage-class-driver-s-iocompletion-routines.md), usually release the memory allocated for SRBs back to a lookaside list.

A class driver's *BuildRequest* routine must set appropriate values in the SRB members, including the length of the CDB it has set up to communicate with its device. For requests that return request-sense information and/or that the driver might need to retry, it sets an *IoCompletion* routine in the IRP. For read or write requests, it ORs the **SrbFlags** with the appropriate transfer direction, SRB\_FLAGS\_DATA\_IN or SRB\_FLAGS\_DATA\_OUT, respectively.

A *BuildRequest* routine might share the responsibility for setting up an SRB with a pair of *SendSrbSynchronous* and *SendSrbAsynchronous* routines. That is, the *BuildRequest* routine could set up the SRB members that are commonly set up for all requests, while the *SendSrbXxx* routines each set SRB values pertinent only to each type of request. When an IRP is passed down to the port driver from a *SendSrbAsynchronous* routine, the IRP must be set up with a driver-supplied *IoCompletion* routine.

After the class driver has loaded, it sets up most SRBs with the **Function** member set to SRB\_FUNCTION\_EXECUTE\_SCSI, indicating a device I/O request to be sent over the bus.

For more information about the system-defined SRB members and their values, see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393).

### <span id="Setting_Up_SRBs_for_Request_Sense"></span><span id="setting_up_srbs_for_request_sense"></span><span id="SETTING_UP_SRBS_FOR_REQUEST_SENSE"></span>Setting Up SRBs for Request Sense

A class driver can request that the port driver return SCSI request-sense or equivalent information when the target controller returns a check condition. To do this, the class driver sets up the **SenseInfoBuffer** pointer and **SenseInfoBufferLength** in the SRB, so the port driver can return the request-sense information if a check condition occurs. The port driver indicates that it returned request-sense information by setting the **SrbStatus** member with SRB\_STATUS\_AUTOSENSE\_VALID when it returns the IRP. For more information about *InterpretSenseInfo* routines, see [Storage Class Driver's InterpretRequestSense Routine](storage-class-driver-s-interpretrequestsense-routine.md).

### <span id="Retries"></span><span id="retries"></span><span id="RETRIES"></span>Retries

Storage class drivers are responsible for retrying requests that fail due to target/controller errors, bus resets, or request time-outs. Consequently, many class drivers maintain a retry count in their own I/O stack location of the IRP. Such a class driver's *BuildRequest* routine also might initialize the retry limit for a given request before it sets up its *IoCompletion* routine and sends the IRP to the port driver. For more information about *RetryRequest* routines, see [Storage Class Driver's RetryRequest Routine](storage-class-driver-s-retryrequest-routine.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20BuildRequest%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


