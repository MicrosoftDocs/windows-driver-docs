---
title: Data Transfer Between Windows Vista Application and Legacy Driver
author: windows-driver-content
description: Data Transfer Between Windows Vista Application and Legacy Driver
ms.assetid: 0acb2ca3-6ac6-441d-a12d-446ae5b70295
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data Transfer Between Windows Vista Application and Legacy Driver


The compatibility layer makes it possible for a Windows Vista application to call **IWiaTransfer::Download** (described in the Microsoft Windows SDK documentation) on a legacy driver. The compatibility layer has to implement folder-transfer code as well as format conversions. The compatibility layer implements special code for feeder transfers to ensure that it is always possible to transfer multiple pages from a legacy driver. A Windows Vista application should always be able to request multiple pages during a scan from the feeder item, even with a TYMED\_FILE transfer. The following diagram illustrates a legacy driver with a Windows Vista application.

![diagram illustrating data transfer between a windows vista application and a legacy driver](images/vistaapp-legacydrv.png)

The legacy callback object within the WIA service converts legacy transfer messages and data into Windows Vista transfer messages and writes data into provided stream.

A Windows Vista application only expects TYMED\_FILE and TYMED\_MULTIPAGE\_FILE so the compatibility layer is responsible for ensuring that TYMED\_CALLBACK and TYMED\_MULTIPAGE\_CALLBACK are not exposed to a Windows Vista application from a legacy driver.

The simplest way to implement this part of the compatibility layer have been to always call into the legacy driver with TYMED\_FILE and TYMED\_MULTIPAGE\_FILE set. The drawback of doing this is that the driver would have always had to scan the entire image, before data could be written back into the application's stream. Therefore, the compatibility layer uses TYMED\_CALLBACK when a Windows Vista application requests a scan of format **WiaImgFmt\_BMP** (the [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property set to **WiaImgFmt\_BMP)**. This makes it possible for the compatibility layer to write the data back band by band.

However, a legacy driver does not support **WiaImgFmt\_BMP**, but **WiaImgFmt\_MEMORYBMP** for TYMED\_CALLBACK. Therefore, the conversion callback object has to create the BMP file header and write this file header back to the application as well. Sometimes this is easy, such as when the BMP file header can be directly constructed from the BMP info header. There are cases however when the height of the BMP info header is set to 0. In this case, the WIA compatibility layer must wait until all the data has been transferred before it can write the BMP file header and update the BMP info header.

The reason TYMED transfers, other than just TYMED\_CALLBACK, are preformed from a legacy driver is that multi-page formats are typically only supported by TYMED\_MULTIPAGE\_FILE, and drivers typically support more formats for TYMED\_FILE than for TYMED\_CALLBACK..

During a TYMED\_FILE transfer the compatibility layer waits until the transfer is finished before it writes the data back to the application's stream. This is done by mapping the file to memory and writing all the data in the memory back in one single write request.

During a TYMED\_CALLBACK transfer, the compatibility layer writes back to the application's stream each time it receives an IT\_MSG\_DATA transfer message from the legacy driver.

The compatibility layer also contains a special code for FEEDER transfers. This code ensures that the compatibility layer can transfer multiple pages from the ADF even though the TYMED is not TYMED\_MULTIPAGE\_FILE. The way this is done is by having the compatibility layer call into the driver multiple times, each time requesting only one page. This solution ensures that every legacy driver will be able to handle transfers of multiple pages from the feeder when invoked by a Windows Vista application.

A legacy driver can send "out-of-band" messages during transfers (for example for previewing). These messages will be ignored as they do not fit into the stream-based transfer model.

For more information on the TYMED constants, please see [Understanding TYMED](understanding-tymed.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Data%20Transfer%20Between%20Windows%20Vista%20Application%20and%20Legacy%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


