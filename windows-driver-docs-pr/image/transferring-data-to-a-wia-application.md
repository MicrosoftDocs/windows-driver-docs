---
title: Transferring Data to a WIA Application
description: Transferring Data to a WIA Application
ms.assetid: 3ad906c9-968f-43d7-ae17-fc570440883d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transferring Data to a WIA Application





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

 

 




