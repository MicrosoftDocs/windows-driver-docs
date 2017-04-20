---
title: Transferring Data to a WIA Application
author: windows-driver-content
description: Transferring Data to a WIA Application
ms.assetid: 3ad906c9-968f-43d7-ae17-fc570440883d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transferring Data to a WIA Application


## <a href="" id="ddk-transferring-data-to-a-wia-application-si"></a>


When an application initiates a data transfer, the WIA service calls the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method to perform the transfer. This method is responsible for acquiring data from the device and sending that data back to the application using the [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946) method.

In Microsoft Windows Millennium Edition (Me) and Windows XP, the WIA minidriver should be able to handle two types of data transfers: file and memory. To determine which type of transfer the application initiated, the minidriver should read the [**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656) property value or check the **tymed** member of the [**MINIDRV\_TRANSFER\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff545250) structure. The second option is valid only if the WIA minidriver called the [**wiasGetImageInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549249) service function first. The **wiasGetImageInformation** service function automatically reads the WIA\_IPA\_TYMED property and assigns the value to the **tymed** member of the MINIDRV\_TRANSFER\_CONTEXT structure.

The preferred way is for the WIA minidriver to read the WIA\_IPA\_TYMED property value. This guarantees that the minidriver is performing the proper type of acquisition.

Beginning with Windows Vista, a simplified stream-based transfer method is introduced. For more information on this data transfer method see [IStream Data Transfers](istream-data-transfers.md).

This section covers the following topics:

[Understanding TYMED](understanding-tymed.md)

[Allocating Memory for Data](allocating-memory-for-data.md)

[Canceling a Data Transfer](canceling-a-data-transfer.md)

[Canceling Pending I/O Operations](canceling-pending-i-o-operations.md)

[RAW Format Data Transfer](raw-format-data-transfer.md)

For basic information about data transfers using TYMED( in-memory and file transfers) and stream-based transfers see [Data Transfers](data-transfers.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Transferring%20Data%20to%20a%20WIA%20Application%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


