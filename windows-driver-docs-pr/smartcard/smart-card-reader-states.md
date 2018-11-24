---
title: Smart Card Reader States
description: Smart Card Reader States
ms.assetid: 7596ba27-206a-4590-aec0-c9009e7a12b6
keywords:
- smart card drivers WDK , reader states
- reader states WDK smart card
- states WDK smart card
- vendor-supplied drivers WDK smart card , reader states
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





