---
title: Transfer Contexts
description: Transfer Contexts
ms.date: 04/20/2017
---

# Transfer Contexts





A transfer context is a collection of information that describes a data transfer from the minidriver to an application. Information about the transfer is stored in a [**MINIDRV\_TRANSFER\_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_minidrv_transfer_context) structure. A transfer context includes members that contain information about the image that is to be transferred: its size, resolution, color depth (number of bytes per pixel), type of compression, and image format. The WIA service obtains these values from the relevant WIA item properties before it calls the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method. The values are then stored in a MINIDRV\_TRANSFER\_CONTEXT structure and handed down to the driver for convenient access. This process eliminates the need for the driver to use the WIA service library routines to read these values from the application item context (that is, the WIA service context).

A transfer context also includes information about the type of transfer: whether it is a file data transfer or a memory-callback transfer. For file data transfers, one member contains a handle to the file that will be written. It is recommended that minidrivers not touch this handle. The WIA service opens the handle before the transfer occurs and closes it upon completion of the transfer. For memory-callback data transfers (and for file data transfers where the application is to receive updates from the minidriver), a member contains the address of the minidriver's callback routine.

Other members contain information such as the total size of all of the buffers that are used in the transfer, and whether the minidriver or the WIA service allocated them. See [**MINIDRV\_TRANSFER\_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_minidrv_transfer_context) for a complete list of the members for this structure.

The minidriver, together with the [**wiasGetImageInformation**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetimageinformation) function, sets many of the transfer context items that describe the image itself, such as its width in pixels, and the number of lines. The WIA service sets many of the transfer context items that are concerned with the data transfer, such as the file handle (when applicable), the type of transfer.

 

