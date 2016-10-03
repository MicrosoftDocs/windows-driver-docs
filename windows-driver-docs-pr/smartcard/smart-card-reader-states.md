---
title: Smart Card Reader States
description: Smart Card Reader States
ms.assetid: 7596ba27-206a-4590-aec0-c9009e7a12b6
keywords: ["smart card drivers WDK , reader states", "reader states WDK smart card", "states WDK smart card", "vendor-supplied drivers WDK smart card , reader states"]
---

# Smart Card Reader States


## <span id="_ntovr_smart_card_reader_states"></span><span id="_NTOVR_SMART_CARD_READER_STATES"></span>


The following table defines the smart card reader states.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">State</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>SCARD_UNKNOWN</p></td>
<td align="left"><p>Indicates that the reader driver has no information concerning the current state of the reader.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SCARD_ABSENT</p></td>
<td align="left"><p>Indicates that there is no card in the reader.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCARD_PRESENT</p></td>
<td align="left"><p>Indicates that a card is present in the reader, but it has not been moved into position for use.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SCARD_SWALLOWED</p></td>
<td align="left"><p>Indicates that a card is in the reader and in position for use. The card is not powered.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCARD_POWERED</p></td>
<td align="left"><p>Indicates that the card is powered, but the reader driver has no additional information concerning the state of the card.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SCARD_NEGOTIABLE</p></td>
<td align="left"><p>Indicates that the card has been reset and is awaiting PTS negotiation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCARD_SPECIFIC</p></td>
<td align="left"><p>Indicates that the card has been reset, and specific communication protocols have been established.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Smart%20Card%20Reader%20States%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




