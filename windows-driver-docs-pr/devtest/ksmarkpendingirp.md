---
title: KsMarkPendingIrp rule ()
description: The KsMarkPendingIrp rule specifies that a kernel-stream (KS) miniport driver should mark IRPs as pending when returning with STATUS\_PENDING from the following callback functions AVStrMiniFilterCloseAVStrMiniPinCloseAVStrMiniPinCreate.
ms.assetid: 88612656-0068-41B8-9A0D-4DDC98AD2435
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["KsMarkPendingIrp rule ()"]
topic_type:
- apiref
api_name:
- KsMarkPendingIrp
api_type:
- NA
---

# KsMarkPendingIrp rule ()


The KsMarkPendingIrp rule specifies that a kernel-stream (KS) miniport driver should mark IRPs as pending when returning with STATUS\_PENDING from the following callback functions:

-   AVStrMiniFilterClose
-   AVStrMiniPinClose
-   AVStrMiniPinCreate

To mark the IRP as pending, use the [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) routine.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00081008) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>KsMarkPendingIrp</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).</p></td>
</tr>
</tbody>
</table>

 

See also
--------

[*AVStrMiniFilterClose*](https://msdn.microsoft.com/library/windows/hardware/ff556307)
[*AVStrMiniPinClose*](https://msdn.microsoft.com/library/windows/hardware/ff556329)
[*AVStrMiniPinCreate*](https://msdn.microsoft.com/library/windows/hardware/ff556334)
 

 





