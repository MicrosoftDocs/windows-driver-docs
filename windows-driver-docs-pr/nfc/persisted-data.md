---
title: Persisted data
author: windows-driver-content
description: Data persistence is.
ms.assetid: 61C3C55C-00DC-4A8C-B235-7C0391FB5119
---

# Persisted data


Data persistence for the registry location is described as follows.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Location</th>
<th align="left">Contents, Usage, Defaults</th>
<th align="left">Access (if not default)</th>
<th align="left">PII stored?</th>
<th align="left">Is this setting migrated?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Device node registry location</td>
<td align="left">NfcRadioTurnedOff, DWORD:
<p>TRUE: NFC RM is off</p>
<p>FALSE: NFC RM is on and subject to idle power management</p></td>
<td align="left">Inherit from the device enum tree, no special ACL set</td>
<td align="left">N/A</td>
<td align="left">No</td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Persisted%20data%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




