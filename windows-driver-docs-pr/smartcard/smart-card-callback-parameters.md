---
title: Smart Card Callback Parameters
description: Smart Card Callback Parameters
keywords:
- IOCTLs WDK smart card
- callback parameters WDK smart card
- vendor-supplied drivers WDK smart card , IOCTL request management
ms.date: 04/20/2017
---

# Smart Card Callback Parameters


## <span id="_ntovr_smart_card_callback_parameters"></span><span id="_NTOVR_SMART_CARD_CALLBACK_PARAMETERS"></span>


For all IOCTL requests except [**IOCTL\_SMARTCARD\_IS\_ABSENT**](/previous-versions/windows/hardware/drivers/ff548905(v=vs.85)) and [**IOCTL\_SMARTCARD\_IS\_PRESENT**](/previous-versions/windows/hardware/drivers/ff548906(v=vs.85)), [**SmartcardDeviceControl (WDM)**](/previous-versions/ff548939(v=vs.85)) initializes the **IoRequest** member of the [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension) structure before it calls a callback routine. The following table indicates the sorts of initialization that **SmartcardDeviceControl** performs.

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
<td align="left"><p>Receives a pointer to the requesting IRP for every control request except <a href="/previous-versions/windows/hardware/drivers/ff548905(v=vs.85)" data-raw-source="[&lt;strong&gt;IOCTL_SMARTCARD_IS_ABSENT&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff548905(v=vs.85))"><strong>IOCTL_SMARTCARD_IS_ABSENT</strong></a> and <a href="/previous-versions/windows/hardware/drivers/ff548906(v=vs.85)" data-raw-source="[&lt;strong&gt;IOCTL_SMARTCARD_IS_PRESENT&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff548906(v=vs.85))"><strong>IOCTL_SMARTCARD_IS_PRESENT</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NotificationIrp</strong></p></td>
<td align="left"><p>Receives a pointer to the requesting IRP for the IOCTL_SMARTCARD_IS_ABSENT or IOCTL_SMARTCARD_IS_PRESENT control request.</p></td>
</tr>
</tbody>
</table>

 

