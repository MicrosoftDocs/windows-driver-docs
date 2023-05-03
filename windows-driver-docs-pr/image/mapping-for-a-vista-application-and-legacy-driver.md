---
title: Mapping for a Vista application and legacy driver
description: Mapping for a Vista application and legacy driver
ms.date: 05/03/2023
---

# Mapping for a Vista application and legacy driver

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

This section shows the mapping used when a Windows Vista application needs to work with a legacy driver. The following tables describe how the WIA compatibility layer maps legacy transfer messages and data flow to Windows Vista transfer messages and data flow.

## Callback transfers

This table shows the mapping of a legacy driver's callback transfer messages to the messages sent to a Windows Vista application.

| Legacy driver transfer message | Windows Vista Application message (after compatibility layer conversion) |
|--|--|
| IT_MSG_DATA | **IStream::Seek,IStream::Write**, and WIA_TRANSFER_MSG_STATUS all ORed together. |
| IT_MSG_STATUS | WIA_TRANSFER_MSG_STATUS |
| IT_MSG_DATA_HEADER | Ignored. This message is only sent by the service, not by the driver, and will never be sent during this type of transfer. |
| IT_MSG_NEW_PAGE | Ignored. This message should never be received during this type of transfer. A legacy driver would only send this during a multi-page transfer with TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK that's not exposed to a Windows Vista application. The compatibility layer only does multi-page transfers with TYMED_MULTIPAGE_FILE. For TYMED_FILE transfers, the application will always receive one page at a time. |
| IT_MSG_TERMINATION | This message is only sent by the service, not by the driver. The compatibility layer sends WIA_TRANSFER_MSG_END_OF_STREAM and WIA_TRANSFER_MSG_END_OF_TRANSFER instead. |
| IT_MSG_FILE_PREVIEW_DATA | Ignored. The **IStream** transfer model doesn't support out-of-band data. |
| IT_MSG_FILE_PREVIEW_DATA_HEADER | Ignored. The **IStream** transfer model doesn't support out-of-band data. |

## File transfers

This table shows the mapping of a legacy driver's file transfer messages to the messages sent to a Windows Vista application.

| Legacy driver transfer message | Windows Vista Application message (after compatibility layer conversion) |
|--|--|
| IT_MSG_DATA | Ignored. This message should never be sent during a file transfer. |  
| IT_MSG_STATUS | WIA_TRANSFER_MSG_STATUS |  
| IT_MSG_DATA_HEADER | Ignored. This message is only sent by the service (not by the driver) and will never be sent during this type of transfer. |  
| IT_MSG_NEW_PAGE | Ignored. This message should never be received during this type of transfer. A legacy driver would only send this during a multi-page transfer with TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK that's not exposed to a Windows Vista application. The compatibility layer, however, only does multi-page transfers with TYMED_MULTIPAGE_FILE. For TYMED_FILE transfers, the driver will always receive one page at a time. |  
| IT_MSG_TERMINATION | This message is only sent by the service (not by the driver). The compatibility layer will instead send WIA_TRANSFER_MSG_END_OF_STREAM and WIA_TRANSFER_MSG_END_OF_TRANSFER. |  
| IT_MSG_FILE_PREVIEW_DATA | Ignored. The new transfer model doesn't support for out-of-band data. |  
| IT_MSG_FILE_PREVIEW_DATA_HEADER | Ignored. The new transfer model doesn't support for out-of-band data. |  

For more information on the legacy transfer messages, see the [**IWiaMiniDrvCallBack**](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback) interface.

For more information on the TYMED constants, see [Understanding TYMED](understanding-tymed.md).
