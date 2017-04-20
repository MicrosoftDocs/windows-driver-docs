---
title: Mapping for a Vista Application and Legacy Driver
author: windows-driver-content
description: Mapping for a Vista Application and Legacy Driver
ms.assetid: 176157b0-cc30-467b-95ec-2d25a40c43ab
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20for%20a%20Vista%20Application%20and%20Legacy%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


