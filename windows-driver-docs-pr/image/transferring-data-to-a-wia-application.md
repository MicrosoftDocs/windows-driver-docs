---
title: Transferring Data to a WIA Application
description: Transferring Data to a WIA Application
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transferring Data to a WIA Application





When an application initiates a data transfer, the WIA service calls the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method to perform the transfer. This method is responsible for acquiring data from the device and sending that data back to the application using the [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback) method.

In Microsoft Windows Millennium Edition (Me) and Windows XP, the WIA minidriver should be able to handle two types of data transfers: file and memory. To determine which type of transfer the application initiated, the minidriver should read the [**WIA\_IPA\_TYMED**](./wia-ipa-tymed.md) property value or check the **tymed** member of the [**MINIDRV\_TRANSFER\_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_minidrv_transfer_context) structure. The second option is valid only if the WIA minidriver called the [**wiasGetImageInformation**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetimageinformation) service function first. The **wiasGetImageInformation** service function automatically reads the WIA\_IPA\_TYMED property and assigns the value to the **tymed** member of the MINIDRV\_TRANSFER\_CONTEXT structure.

The preferred way is for the WIA minidriver to read the WIA\_IPA\_TYMED property value. This guarantees that the minidriver is performing the proper type of acquisition.

Beginning with Windows Vista, a simplified stream-based transfer method is introduced. For more information on this data transfer method see [IStream Data Transfers](istream-data-transfers.md).

This section covers the following topics:

[Understanding TYMED](understanding-tymed.md)

[Allocating Memory for Data](allocating-memory-for-data.md)

[Canceling a Data Transfer](canceling-a-data-transfer.md)

[Canceling Pending I/O Operations](canceling-pending-i-o-operations.md)

[RAW Format Data Transfer](raw-format-data-transfer.md)

For basic information about data transfers using TYMED( in-memory and file transfers) and stream-based transfers see [Data Transfers](data-transfers.md).

 

