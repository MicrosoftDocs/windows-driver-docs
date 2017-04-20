---
title: Single Driver for Windows Vista and Windows XP
author: windows-driver-content
description: Single Driver for Windows Vista and Windows XP
ms.assetid: 3fa9c044-ab9d-4bed-b5fc-89396e1269ce
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Single Driver for Windows Vista and Windows XP


You might want to have a single driver for both Windows Vista and Windows XP. In such situations, the driver handles data transfers by checking the flags. When [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) is called for stream-based transfers, the *lFlags* parameter is set to either WIA\_MINIDRV\_TRANSFER\_DOWNLOAD or WIA\_MINIDRV\_TRANSFER\_UPLOAD. If neither of these bits is set, the transfer is a *legacy* transfer and the driver should follow the behavior that is outlined for Windows XP data transfers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Single%20Driver%20for%20Windows%20Vista%20and%20Windows%20XP%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


