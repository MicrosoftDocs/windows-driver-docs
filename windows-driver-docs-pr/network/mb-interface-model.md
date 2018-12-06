---
title: MB Interface Model
description: This section provides information for mobile broadband devices that are implemented based on the Mobile Broadband Interface Model (MBIM) specification.
ms.assetid: B1C6D5F4-63E2-4C46-8038-71B8144AB474
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Interface Model


This section provides information for mobile broadband devices that are implemented based on the Mobile Broadband Interface Model (MBIM) specification.

Starting with Windows 8, Microsoft provides an inbox class driver, referred to as MBCD, for MBIM functions. Microsoft already provides an inbox driver, USBCCGP, for composite devices. This section describes the requirements for mobile broadband devices to load USBCCGP and MBCD in Windows 8.

Mobile broadband composite devices that use WMC UFD for grouping interfaces into functions should implement Microsoft OS descriptors to load USBCCGP on Windows 8 and instruct USBCCGP to parse WMC UFD to create functions. Mobile broadband composite devices that use Interface Association Descriptors (IADs) for grouping interfaces into functions do not need to implement Microsoft OS descriptors to load USBCCGP.

MBIM functions that are backward compatible should implement Microsoft OS descriptors to load MBCD. MBIM functions that are not backward compatible do not need to implement Microsoft OS descriptors to load MBCD.

Mobile broadband devices that exhibit identity morphing should also implement Microsoft OS descriptors.

These scenarios are discussed in more detail throughout the MB Interface Model topics. The following table summarizes all of the Microsoft OS compatible IDs mentioned in these subtopics. For more information see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?linkid=308932).

*Microsoft OS compatible IDs*

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Microsoft OS Compatible ID</th>
<th align="left">Microsoft OS Sub Compatible ID</th>
<th align="left">Required for Scenario</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>&quot;CDC_WMC&quot;</p></td>
<td align="left"><p></p></td>
<td align="left"><p>Loading USBCCGP on composite devices that use WMC UFD for grouping interfaces into functions</p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;MBIM&quot;</p></td>
<td align="left"><p></p></td>
<td align="left"><p>Loading MBCD on MBIM backward-compatible function</p></td>
</tr>
<tr class="odd">
<td align="left"><p>&quot;ALTRCFG&quot;</p></td>
<td align="left"><p>Configuration number in ASCII</p></td>
<td align="left"><p>Identity morphing with IADs</p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;WMCALTR&quot;</p></td>
<td align="left"><p>Configuration number in ASCII</p></td>
<td align="left"><p>Identity morphing with WMC UFD</p></td>
</tr>
</tbody>
</table>

 

The MB Interface Model in described further in the following subtopics:

[MB Interface Terms](mb-interface-terms.md)
[MB Union Function Descriptors](mb-union-function-descriptors.md)
[MB Identity Morphing](mb-identity-morphing.md)
[MB Interface Model Supplement](mb-interface-model-supplement.md)
 

 





