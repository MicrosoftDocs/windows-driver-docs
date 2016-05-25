---
title: Negotiating Claim and Release Device Requests with SCSI Port
author: windows-driver-content
description: Negotiating Claim and Release Device Requests with SCSI Port
ms.assetid: 0eb00955-127c-4ef7-a18f-69448b5fd105
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Negotiating%20Claim%20and%20Release%20Device%20Requests%20with%20SCSI%20Port%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


