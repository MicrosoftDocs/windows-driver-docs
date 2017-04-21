---
title: Transfer Contexts
author: windows-driver-content
description: Transfer Contexts
ms.assetid: b4eadccd-afb6-4cb5-bf52-704f64d45e40
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transfer Contexts


## <a href="" id="ddk-transfer-contexts-si"></a>


A transfer context is a collection of information that describes a data transfer from the minidriver to an application. Information about the transfer is stored in a [**MINIDRV\_TRANSFER\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff545250) structure. A transfer context includes members that contain information about the image that is to be transferred: its size, resolution, color depth (number of bytes per pixel), type of compression, and image format. The WIA service obtains these values from the relevant WIA item properties before it calls the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method. The values are then stored in a MINIDRV\_TRANSFER\_CONTEXT structure and handed down to the driver for convenient access. This process eliminates the need for the driver to use the WIA service library routines to read these values from the application item context (that is, the WIA service context).

A transfer context also includes information about the type of transfer: whether it is a file data transfer or a memory-callback transfer. For file data transfers, one member contains a handle to the file that will be written. It is recommended that minidrivers not touch this handle. The WIA service opens the handle before the transfer occurs and closes it upon completion of the transfer. For memory-callback data transfers (and for file data transfers where the application is to receive updates from the minidriver), a member contains the address of the minidriver's callback routine.

Other members contain information such as the total size of all of the buffers that are used in the transfer, and whether the minidriver or the WIA service allocated them. See [**MINIDRV\_TRANSFER\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff545250) for a complete list of the members for this structure.

The minidriver, together with the [**wiasGetImageInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549249) function, sets many of the transfer context items that describe the image itself, such as its width in pixels, and the number of lines. The WIA service sets many of the transfer context items that are concerned with the data transfer, such as the file handle (when applicable), the type of transfer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Transfer%20Contexts%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


