---
title: Property Sheet Pages for Still Image Devices
author: windows-driver-content
description: Property Sheet Pages for Still Image Devices
ms.assetid: ef77e57d-f791-4afa-8d51-67e78b60cf57
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Property Sheet Pages for Still Image Devices


## <a href="" id="ddk-property-sheet-pages-for-still-image-devices-si"></a>


You can provide a DLL that creates device-specific property sheet pages. The Scanners and Cameras Control Panel calls the DLL's entry point when a user attempts to view the device's property sheet.

To cause this DLL to be installed and used, you must include a **PropertyPages** entry in your setup information (INF) file. This entry contains the DLL's file name and entry point name. For more information, see [INF Files for Still Image Devices](inf-files-for-still-image-devices.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Property%20Sheet%20Pages%20for%20Still%20Image%20Devices%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


