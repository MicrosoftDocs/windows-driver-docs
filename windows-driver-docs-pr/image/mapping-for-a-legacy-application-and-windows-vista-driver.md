---
title: Mapping for a legacy application and Windows Vista driver
description: Mapping for a legacy application and Windows Vista driver
ms.date: 05/01/2023
---

# Mapping for a legacy application and Windows Vista driver

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

This section explains how Windows Vista transfer messages and data flow are mapped to legacy transfer messages and data flow when a legacy application needs to work with a Windows Vista driver.

## Callback Transfers

This table shows the mapping of a Windows Vista driver's callback transfer messages to the message sent to a legacy application.

| Windows Vista driver message | Legacy application message (after compatibility layer conversion) |
|--|--|
| WIA_TRANSFER_MSG_STATUS | IT_MSG_STATUS |
| WIA_TRANSFER_MSG_ERROR | Ignored. |
| WIA_TRANSFER_MSG_END_OF_STREAM | Ignored. This message always goes along with a call to [**IWiaTransferCallback::GetNextStream**](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwiatransfercallback-getnextstream). To avoid duplicate messages, this message is implemented in the **GetNextStream** implementation instead. |
| WIA_TRANSFER_MSG_END_OF_TRANSFER | IT_MSG_TERMINATION (WIA_TRANSFER_MSG_END_OF_TRANSFER is not sent by the driver). |
| WIA_TRANSFER_MSG_DEVICE_STATUS | If hrErrorStatus == WIA_STATUS_WARMING_UP, the compatibility layer sends IT_MSG_STATUS with IT_STATUS_TRANSFER_FROM_DEVICE in order to provide some status to an application as well as giving a Windows Vista application the possibility to cancel the transfer. |
| WIA_TRANSFER_MSG_NEW_PAGE | Ignored. Should never be sent by a Windows Vista driver in this case, since we call into the Windows Vista driver with TYMED_FILE. |
| **IWiaTransferCallback::GetNextStream** | First page: IT_MSG_DATA_HEADER<br><br>Subsequent pages: IT_MSG_NEW_PAGE |
| **IStream::Write** | IT_MSG_DATA |

## File Transfers

This table shows the mapping of a Windows Vista driver's file transfer messages to the message sent to a legacy application.

| Windows Vista driver message | Legacy application message (after compatibility layer conversion) |
|--|--|
| WIA_TRANSFER_MSG_STATUS | IT_MSG_STATUS |
| WIA_TRANSFER_MSG_ERROR | Ignored. |
| WIA_TRANSFER_MSG_END_OF_STREAM | Ignored. This message always goes along with a call to [**IWiaTransferCallback::GetNextStream**](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwiatransfercallback-getnextstream). To avoid duplicate messages, this message is implemented in the **GetNextStream** implementation instead. |
| WIA_TRANSFER_MSG_END_OF_TRANSFER | IT_MSG_TERMINATION (WIA_TRANSFER_MSG_END_OF_TRANSFER is not sent by the driver). |
| WIA_TRANSFER_MSG_DEVICE_STATUS | If hrErrorStatus == WIA_STATUS_WARMING_UP, IT_MSG_STATUS is sent with IT_STATUS_TRANSFER_FROM_DEVICE in order to provide some status to an application as well as giving a Windows Vista application the possibility to cancel the transfer. |
| WIA_TRANSFER_MSG_NEW_PAGE | This behavior is somewhat different from a multi-page file transfer today because <em>wiasWritePageBufToFile</em> never sends IT_MSG_NEW_PAGE. |
| **IWiaTransferCallback::GetNextStream** | First page: IT_MSG_FILE_PREVIEW_DATA_HEADER<br><br>Subsequent pages: Error (the WIA_ERROR_GENERAL_ERROR is passed back to driver). **IWiaTransferCallback::GetNextStream** should only be called once because you can only transfer one page with TYMED_FILE and during a TYMED_MULTIPAGE_FILE transfer, the Windows Vista driver should only call **GetNextStream** once because all the pages should go into the same stream. |
| **IStream::Write** | No message sent. In case of file transfers, the compatibility layer does not convert any of the data that the driver (image processing filter) writes into legacy transfer messages. Rather, the data is simply written into a file that is returned to the user at the end of the transfer. |

For more information on the legacy transfer messages see the [IWiaMiniDrvCallBack Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback).

For more information on the TYMED constants, see [Understanding TYMED](understanding-tymed.md).
