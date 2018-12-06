---
title: Mapping for a Legacy Application and Windows Vista Driver
description: Mapping for a Legacy Application and Windows Vista Driver
ms.assetid: 6f4ebcc7-ecf0-4e0b-bcef-e5b72dc472dc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping for a Legacy Application and Windows Vista Driver


This section explains how Windows Vista transfer messages and data flow are mapped to legacy transfer messages and data flow when a legacy application needs to work with a Windows Vista driver.

### Callback Transfers

This table shows the mapping of a Windows Vista driver's callback transfer messages to the message sent to a legacy application.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Windows Vista driver message</strong></p></td>
<td><p><strong>Legacy application message (after compatibility layer conversion)</strong></p></td>
</tr>
<tr class="even">
<td><p>WIA_TRANSFER_MSG_STATUS</p></td>
<td><p>IT_MSG_STATUS</p></td>
</tr>
<tr class="odd">
<td><p>WIA_TRANSFER_MSG_ERROR</p></td>
<td><p>Ignored.</p></td>
</tr>
<tr class="even">
<td><p>WIA_TRANSFER_MSG_END_OF_STREAM</p></td>
<td><p>Ignored. This message always goes along with a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545039" data-raw-source="[&lt;strong&gt;IWiaTransferCallback::GetNextStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545039)"><strong>IWiaTransferCallback::GetNextStream</strong></a>. Not duplicate any messages, this is implemented in the <strong>GetNextStream</strong> implementation instead.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_TRANSFER_MSG_END_OF_TRANSFER</p></td>
<td><p>IT_MSG_TERMINATION (note WIA_TRANSFER_MSG_END_OF_TRANSFER is not sent by the driver).</p></td>
</tr>
<tr class="even">
<td><p>WIA_TRANSFER_MSG_DEVICE_STATUS</p></td>
<td><p>If hrErrorStatus == WIA_STATUS_WARMING_UP, the compatibility layer sends IT_MSG_STATUS with IT_STATUS_TRANSFER_FROM_DEVICE in order to provide some status to an application as well as giving a Windows Vista application the possibility to cancel the transfer.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_TRANSFER_MSG_NEW_PAGE</p></td>
<td><p>Ignored. Should never be sent by a Windows Vista driver in this case, since we call into the Windows Vista driver with TYMED_FILE.</p></td>
</tr>
<tr class="even">
<td><p><strong>IWiaTransferCallback::GetNextStream</strong></p></td>
<td><p>First page: IT_MSG_DATA_HEADER</p>
<p>Subsequent pages: IT_MSG_NEW_PAGE</p></td>
</tr>
<tr class="odd">
<td><p><strong>IStream::Write</strong></p></td>
<td><p>IT_MSG_DATA</p></td>
</tr>
</tbody>
</table>

 

### File Transfers

This table shows the mapping of a Windows Vista driver's file transfer messages to the message sent to a legacy application.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Windows Vista driver message</strong></p></td>
<td><p><strong>Legacy application message (after compatibility layer conversion)</strong></p></td>
</tr>
<tr class="even">
<td><p>WIA_TRANSFER_MSG_STATUS</p></td>
<td><p>IT_MSG_STATUS</p></td>
</tr>
<tr class="odd">
<td><p>WIA_TRANSFER_MSG_ERROR</p></td>
<td><p>Ignored.</p></td>
</tr>
<tr class="even">
<td><p>WIA_TRANSFER_MSG_END_OF_STREAM</p></td>
<td><p>Ignored. This message always goes along with a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545039" data-raw-source="[&lt;strong&gt;IWiaTransferCallback::GetNextStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545039)"><strong>IWiaTransferCallback::GetNextStream</strong></a>. To avoid duplicate messages, this message is implemented in the <strong>GetNextStream</strong> implementation instead.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_TRANSFER_MSG_END_OF_TRANSFER</p></td>
<td><p>IT_MSG_TERMINATION (note WIA_TRANSFER_MSG_END_OF_TRANSFER is not sent by the driver).</p></td>
</tr>
<tr class="even">
<td><p>WIA_TRANSFER_MSG_DEVICE_STATUS</p></td>
<td><p>If hrErrorStatus == WIA_STATUS_WARMING_UP, IT_MSG_STATUS is sent with IT_STATUS_TRANSFER_FROM_DEVICE in order to provide some status to an application as well as giving a Windows Vista application the possibility to cancel the transfer.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_TRANSFER_MSG_NEW_PAGE</p></td>
<td><p>IT_MSG_NEW_PAGE</p>
<p>Note: this behavior is somewhat different from a multi-page file transfer today because <em>wiasWritePageBufToFile</em> never sends IT_MSG_NEW_PAGE.</p></td>
</tr>
<tr class="even">
<td><p><strong>IWiaTransferCallback::GetNextStream</strong></p></td>
<td><p>First page: IT_MSG_FILE_PREVIEW_DATA_HEADER</p>
<p>Subsequent pages: Error (the WIA_ERROR_GENERAL_ERROR is passed back to driver). <strong>IWiaTransferCallback::GetNextStream</strong> should only be called once because you can only transfer one page with TYMED_FILE and during a TYMED_MULTIPAGE_FILE transfer, the Windows Vista driver should only call <strong>GetNextStream</strong> once because all the pages should go into the same stream.</p></td>
</tr>
<tr class="odd">
<td><p><strong>IStream::Write</strong></p></td>
<td><p>No message sent. In case of file transfers, the compatibility layer does not convert any of the data that the driver (image processing filter) writes into legacy transfer messages. Rather, the data is simply written into a file that is returned to the user at the end of the transfer.</p></td>
</tr>
</tbody>
</table>

 

For more information on the legacy transfer messages see the [IWiaMiniDrvCallBack Interface](https://msdn.microsoft.com/library/windows/hardware/ff543943).

For more information on the TYMED constants, see [Understanding TYMED](understanding-tymed.md).

The **IStream** interface is described in the Microsoft Windows SDK documentation.

 

 




