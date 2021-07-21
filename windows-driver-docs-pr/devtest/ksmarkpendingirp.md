---
title: KsMarkPendingIrp rule ()
description: The KsMarkPendingIrp rule specifies that a kernel-stream (KS) miniport driver should mark IRPs as pending when returning with STATUS\_PENDING from the following callback functions AVStrMiniFilterCloseAVStrMiniPinCloseAVStrMiniPinCreate.
ms.date: 05/21/2018
keywords: ["KsMarkPendingIrp rule ()"]
topic_type:
- apiref
api_name:
- KsMarkPendingIrp
api_type:
- NA
ms.localizationpriority: medium
---

# KsMarkPendingIrp rule ()


The KsMarkPendingIrp rule specifies that a kernel-stream (KS) miniport driver should mark IRPs as pending when returning with STATUS\_PENDING from the following callback functions:

-   AVStrMiniFilterClose
-   AVStrMiniPinClose
-   AVStrMiniPinCreate

To mark the IRP as pending, use the [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) routine.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00081008)


## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>KsMarkPendingIrp</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
<p>For more information, see <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

## See also

[*AVStrMiniFilterClose*](/previous-versions/ff556307(v=vs.85))
[*AVStrMiniPinClose*](/previous-versions/ff556329(v=vs.85))
[*AVStrMiniPinCreate*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinirp)
