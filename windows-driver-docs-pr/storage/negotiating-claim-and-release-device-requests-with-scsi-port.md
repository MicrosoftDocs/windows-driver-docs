---
title: Negotiating Claim and Release Device Requests with SCSI Port
description: Negotiating Claim and Release Device Requests with SCSI Port
ms.assetid: 0eb00955-127c-4ef7-a18f-69448b5fd105
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Negotiating Claim and Release Device Requests with SCSI Port


## <span id="ddk_negotiating_claim_and_release_device_requests_with_scsi_port_kg"></span><span id="DDK_NEGOTIATING_CLAIM_AND_RELEASE_DEVICE_REQUESTS_WITH_SCSI_PORT_KG"></span>


Storage class drivers must request permission from SCSI Port to *claim* a device. For more information about how a class driver claims a device, see [Storage Class Driver's ClaimDevice Routine](storage-class-driver-s-claimdevice-routine.md).

The process by which new devices are discovered and enumerated differs depending on whether they are PnP devices or pre-PnP storage devices. The SCSI Port driver mediates between pre-PNP and PnP drivers that attempt to control the same device. Therefore, a storage device driver must obtain permission from SCSI Port before interacting with its device.

To obtain permission to use a device, the device driver sends a claim request to SCSI Port, usually in its *AddDevice* routine. The claim request consists of an IRP with an I/O control code of IOCTL\_SCSI\_EXECUTE\_NONE and a pointer to an SRB at **Parameters.Scsi.Srb**. The SRB is of the function type SRB\_FUNCTION\_CLAIM\_DEVICE.

SCSI Port maintains a flag for each device that indicates whether the device has been claimed. SCSI Port sets this flag in response to a SRB\_FUNCTION\_CLAIM\_DEVICE request; SCSI Port clears the flag in response to a SRB\_FUNCTION\_REMOVE\_DEVICE request.

If a higher-level driver attempts to claim a device that does not exist, SCSI Port fails the claim request IRP and returns a status of STATUS\_DEVICE\_DOES\_NOT\_EXIST.

If a higher-level driver attempts to claim a device that has already been claimed, SCSI Port fails the claim request IRP and returns status of STATUS\_DEVICE\_BUSY.

If the claim request succeeds, SCSI Port returns the current device object for the device in the data buffer pointer of the SRB.

To release a previously claimed device, higher-level drivers must send a release device request to the SCSI Port driver: The release device request consists of an SRB with a **Function** value of SRB\_FUNCTION\_RELEASE\_DEVICE.

For a discussion of claim device requests from the point of view of the storage class driver, see [Storage Class Driver's ClaimDevice Routine](storage-class-driver-s-claimdevice-routine.md).

 

 




