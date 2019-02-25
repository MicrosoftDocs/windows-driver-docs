---
title: Negotiating Claim and Release Device Requests with Storport
description: Negotiating Claim and Release Device Requests with Storport
ms.assetid: 9212f2b0-6319-47a6-8c61-02002ad81178
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Negotiating Claim and Release Device Requests with Storport


Storage class drivers must request permission from Storport to *claim* a device. For more information about how a class driver claims a device, see [Storage Class Driver's ClaimDevice Routine](storage-class-driver-s-claimdevice-routine.md).

The process by which new devices are discovered and enumerated differs depending on whether they are PnP devices or pre-PnP storage devices. The Storport driver mediates between pre-PNP and PnP drivers that attempt to control the same device. Therefore, a storage device driver must obtain permission from Storport before interacting with its device. Furthermore, the device in question may be either the HBA itself, or a LUN that is attached to a target that is controlled by the HBA. However, when referring to devices that are claimed by a storage class driver, it is always the LUN that is being claimed, not the HBA.

To obtain permission to use a device, the device driver sends a claim request to Storport. The claim request consists of an IRP with an I/O control code of IOCTL\_SCSI\_EXECUTE\_NONE and a pointer to an SRB at **Parameters.Scsi.Srb**. The SRB is of the function type SRB\_FUNCTION\_CLAIM\_DEVICE.

Storport maintains a flag for each device that indicates whether the device has been claimed. Storport sets this flag in response to a SRB\_FUNCTION\_CLAIM\_DEVICE request; Storport clears the flag in response to a SRB\_FUNCTION\_REMOVE\_DEVICE request.

If a higher-level driver attempts to claim a device that does not exist, Storport fails the claim request IRP and returns a status of STATUS\_DEVICE\_DOES\_NOT\_EXIST.

If a higher-level driver attempts to claim a device that has already been claimed, Storport fails the claim request IRP and returns status of STATUS\_DEVICE\_BUSY.

If the claim request succeeds, Storport returns the current device object for the device in the data buffer pointer of the SRB.

To release a previously claimed device, higher-level drivers must send a release device request to the Storport driver: The release device request consists of an SRB with a **Function** value of SRB\_FUNCTION\_RELEASE\_DEVICE.

For a discussion of claim device requests from the point of view of the storage class driver, see [Storage Class Driver's ClaimDevice Routine](storage-class-driver-s-claimdevice-routine.md).

 

 




