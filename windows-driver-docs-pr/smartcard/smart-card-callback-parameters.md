---
title: Smart Card Callback Parameters
description: Smart Card Callback Parameters
ms.assetid: 6fd1590b-0600-4065-b1cc-71d8aed3f98a
keywords:
- IOCTLs WDK smart card
- callback parameters WDK smart card
- vendor-supplied drivers WDK smart card , IOCTL request management
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Smart Card Callback Parameters


## <span id="_ntovr_smart_card_callback_parameters"></span><span id="_NTOVR_SMART_CARD_CALLBACK_PARAMETERS"></span>


For all IOCTL requests except [**IOCTL\_SMARTCARD\_IS\_ABSENT**](https://msdn.microsoft.com/library/windows/hardware/ff548905) and [**IOCTL\_SMARTCARD\_IS\_PRESENT**](https://msdn.microsoft.com/library/windows/hardware/ff548906), [**SmartcardDeviceControl (WDM)**](https://msdn.microsoft.com/library/windows/hardware/ff548939) initializes the **IoRequest** member of the [**SMARTCARD\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff548974) structure before it calls a callback routine. The following table indicates the sorts of initialization that **SmartcardDeviceControl** performs.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member of IoRequest</th>
<th align="left">Initialization performed by SmartcardDeviceControl</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>IoRequest.RequestBuffer</strong></p></td>
<td align="left"><p>Stores the user data to be sent to the card in the buffer that this member points to.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IoRequest.RequestBufferLength</strong></p></td>
<td align="left"><p>Stores the length of the user buffer in this member.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IoRequest.ReplyBuffer</strong></p></td>
<td align="left"><p>Stores the data returned by the smart card in the buffer that this member points to.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IoRequest.ReplyBufferLength</strong></p></td>
<td align="left"><p>Stores the size of the reply buffer in this member.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IoRequest.Information</strong></p></td>
<td align="left"><p>Stores the number of bytes that were actually received from the card in the variable that this member points to.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MajorIoControlCode</strong></p></td>
<td align="left"><p>Stores the major I/O control code of the IOCTL request in this member.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MinorIoControlCode</strong></p></td>
<td align="left"><p>Stores the minor I/O control code (if any) of the IOCTL request in this member.</p></td>
</tr>
</tbody>
</table>

 

The structure pointed to by **SmartcardExtension-&gt;OsData** is set up as described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>CurrentIrp</strong></p></td>
<td align="left"><p>Receives a pointer to the requesting IRP for every control request except [<strong>IOCTL_SMARTCARD_IS_ABSENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548905) and [<strong>IOCTL_SMARTCARD_IS_PRESENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548906).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NotificationIrp</strong></p></td>
<td align="left"><p>Receives a pointer to the requesting IRP for the IOCTL_SMARTCARD_IS_ABSENT or IOCTL_SMARTCARD_IS_PRESENT control request.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Smart%20Card%20Callback%20Parameters%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




