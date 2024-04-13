---
title: WIA Transfer Constants
description: WIA transfer constants
ms.date: 05/11/2023
---

# WIA transfer constants

This topic contains a list of the constants that are used for WIA **IStream**-based transfers.

These constants are divided into three subgroups:

- Item type

- Callback messages

- Transfer flags

## Item type

The following table shows which WIA item type bits relate to stream-based data transfer.

| Name | Description |
|--|--|
| [**WiaItemTypeTransfer**](/windows/win32/wia/-wia-iwiatransfer) | This [**WIA_IPA_ITEM_FLAGS**](./wia-ipa-item-flags.md) bit should be set on all items that are capable of transferring data; that is, an application can initiate a download or upload on items that have this bit set. |

## Callback messages

The following table shows possible values for the *lFlags* parameter of [**IWiaTransferCallback::TransferCallback**](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwiatransfercallback-transfercallback).

| Name | Description |
|--|--|
| WIA_TRANSFER_MSG_STATUS | Notifies the application of the progress of the transfer.<br><br>*pWiaTransferParams*-\>*lPercentComplete* contains the percent complete for this item and the page that is being transferred. |
| WIA_TRANSFER_MSG_END_OF_STREAM | Notifies the application that there is no more data to be transferred to the current data stream and that the stream may be closed.<br><br>A new stream may subsequently be requested in a multi-item or multipage transfer.<br><br>Drivers do not send this message manually. The WIA service will automatically send this message when the driver asks for the next stream. |
| WIA_TRANSFER_MSG_END_OF_TRANSFER | Received by the application at the end of the transfer.<br><br>The driver does not send this message. The WIA service will send this message automatically after the transfer has ended (that is, the call to **IWiaMiniDrv::drvAcquireItemData** returns). |
| WIA_TRANSFER_MSG_ERROR | Reserved by Microsoft for future use. |
| WIA_TRANSFER_MSG_DEVICE_STATUS | Indicates an error during the transfer (for example, a paper jam).<br><br>*pWiaTransferParams*-\>*hrErrorStatus* contains the error status code. |
| WIA_TRANSFER_MSG_NEW_PAGE | Indicates that a new page is being transferred during a multipage transfer when a format that supports multiple pages in one file (such as multifile TIFF) is being used. |

## Transfer flags

The following table shows the flags that may be passed into [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata).

| Name | Description |
|--|--|
| WIA_MINIDRV_TRANSFER_DOWNLOAD | Indicates that the transfer is a stream-based download operation (that is, a data transfer from a device to an application).<br><br>Applications do not set this bit directly. The WIA service sets this bit if the application calls **IWiaTransfer::Download**. |
| WIA_MINIDRV_TRANSFER_UPLOAD | Indicates that the transfer is a stream-based upload operation (that is, a data transfer from an application to a device).<br><br>Applications do not set this bit directly. The WIA service sets this bit if the application calls **IWiaTransfer::Upload**. |
| WIA_MINIDRV_TRANSFER_ACQUIRE_CHILDREN | Indicates that the driver should perform a folder transfer. If this value is called on a folder item, the application requests to transfer the children of that folder.<br><br>This value will be set if an application requests a folder transfer by setting the *lFlags* parameter of **IWiaTransfer::Download** to WIA_TRANSFER_ACQUIRE_CHILDREN *and* the driver has specified that it can transfer multiple children in one scan. If the driver cannot perform this type of transfer, the WIA service will make multiple calls into the driver and WIA_MINIDRV_TRANSFER_ACQUIRE_CHILDREN will *not* be set. |
