---
title: Mapping for a Vista Application and Legacy Driver
description: Mapping for a Vista Application and Legacy Driver
ms.assetid: 176157b0-cc30-467b-95ec-2d25a40c43ab
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping for a Vista Application and Legacy Driver


This section shows the mapping used when a Windows Vista application needs to work with a legacy driver. The following tables describe how the WIA compatibility layer maps legacy transfer messages and data flow to Windows Vista transfer messages and data flow.

### Callback Transfers

This table shows the mapping of a legacy driver's callback transfer messages to the messages sent to a Windows Vista application.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Legacy driver transfer message</strong></p></td>
<td><p><strong>Windows Vista Application message (after compatibility layer conversion)</strong></p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_DATA</p></td>
<td><p><strong>IStream::Seek,IStream::Write</strong>, and WIA_TRANSFER_MSG_STATUS all ORed together.</p></td>
</tr>
<tr class="odd">
<td><p>IT_MSG_STATUS</p></td>
<td><p>WIA_TRANSFER_MSG_STATUS</p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_DATA_HEADER</p></td>
<td><p>Ignored. This message is only sent by the service, not by the driver, and will never be sent during this type of transfer.</p></td>
</tr>
<tr class="odd">
<td><p>IT_MSG_NEW_PAGE</p></td>
<td><p>Ignored. This message should never be received during this type of transfer. A legacy driver would only send this during a multi-page transfer with TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK that are not exposed to a Windows Vista application. The compatibility layer only does multi-page transfers with TYMED_MULTIPAGE_FILE. For TYMED_FILE transfers, the application will always receive one page at a time.</p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_TERMINATION</p></td>
<td><p>This message is only sent by the service, not by the driver. The compatibility layer will send WIA_TRANSFER_MSG_END_OF_STREAM and WIA_TRANSFER_MSG_END_OF_TRANSFER instead.</p></td>
</tr>
<tr class="odd">
<td><p>IT_MSG_FILE_PREVIEW_DATA</p></td>
<td><p>Ignored. The <strong>IStream</strong> transfer model does not support out-of-band data.</p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_FILE_PREVIEW_DATA_HEADER</p></td>
<td><p>Ignored. The <strong>IStream</strong> transfer model does not support out-of-band data.</p></td>
</tr>
</tbody>
</table>

 

### File Transfers

This table shows the mapping of a legacy driver's file transfer messages to the messages sent to a Windows Vista application.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Legacy driver transfer message</strong></p></td>
<td><p><strong>Windows Vista Application message (after compatibility layer conversion)</strong></p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_DATA</p></td>
<td><p>Ignored. This message should never be sent during a file transfer.</p></td>
</tr>
<tr class="odd">
<td><p>IT_MSG_STATUS</p></td>
<td><p>WIA_TRANSFER_MSG_STATUS</p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_DATA_HEADER</p></td>
<td><p>Ignored. This message is only sent by the service (not by the driver) and will never be sent during this type of transfer.</p></td>
</tr>
<tr class="odd">
<td><p>IT_MSG_NEW_PAGE</p></td>
<td><p>Ignored. This message should never be received during this type of transfer. A legacy driver would only send this during a multi-page transfer with TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK that are not exposed to a Windows Vista application. The compatibility layer, however, only does multi-page transfers with TYMED_MULTIPAGE_FILE. For TYMED_FILE transfers, the driver will always receive one page at a time.</p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_TERMINATION</p></td>
<td><p>This message is only sent by the service ( not by the driver). The compatibility layer will instead send WIA_TRANSFER_MSG_END_OF_STREAM and WIA_TRANSFER_MSG_END_OF_TRANSFER.</p></td>
</tr>
<tr class="odd">
<td><p>IT_MSG_FILE_PREVIEW_DATA</p></td>
<td><p>Ignored. The new transfer model does not support for out-of-band data.</p></td>
</tr>
<tr class="even">
<td><p>IT_MSG_FILE_PREVIEW_DATA_HEADER</p></td>
<td><p>Ignored. The new transfer model does not support for out-of-band data.</p></td>
</tr>
</tbody>
</table>

 

For more information on the legacy transfer messages, see the [IWiaMiniDrvCallBack Interface](https://msdn.microsoft.com/library/windows/hardware/ff543943).

For more information on the TYMED constants, see [Understanding TYMED](understanding-tymed.md).

The **IStream** interface is described in the Microsoft Windows SDK documentation.

 

 




