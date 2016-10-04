---
title: Mapping for a Legacy Application and Windows Vista Driver
author: windows-driver-content
description: Mapping for a Legacy Application and Windows Vista Driver
MS-HAID:
- 'WIA\_Fundamentals\_95bd6242-b967-4336-a104-775404739b55.xml'
- 'image.mapping\_for\_a\_legacy\_application\_and\_windows\_vista\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6f4ebcc7-ecf0-4e0b-bcef-e5b72dc472dc
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
<td><p>Ignored. This message always goes along with a call to [<strong>IWiaTransferCallback::GetNextStream</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545039). Not duplicate any messages, this is implemented in the <strong>GetNextStream</strong> implementation instead.</p></td>
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
<td><p>Ignored. This message always goes along with a call to [<strong>IWiaTransferCallback::GetNextStream</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545039). To avoid duplicate messages, this message is implemented in the <strong>GetNextStream</strong> implementation instead.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20for%20a%20Legacy%20Application%20and%20Windows%20Vista%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


