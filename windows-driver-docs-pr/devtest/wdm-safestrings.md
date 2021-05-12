---
title: SafeStrings rule (wdm)
description: The SafeStrings rule specifies that the driver calls only those string manipulations functions that protect the system from unintentional or malicious intrusion. These safe string functions for drivers are defined in Ntstrsafe.h.
ms.date: 05/21/2018
keywords: ["SafeStrings rule (wdm)"]
topic_type:
- apiref
api_name:
- SafeStrings
api_type:
- NA
ms.localizationpriority: medium
---

# SafeStrings rule (wdm)


The **SafeStrings** rule specifies that the driver calls only those string manipulations functions that protect the system from unintentional or malicious intrusion. These safe string functions for drivers are defined in Ntstrsafe.h.

To comply with this rule, use the string functions that are considered to be safe for kernel-mode drivers. The safe string functions and the unsafe functions that they replace are listed in [**Using Safe String Functions**](../kernel/using-safe-string-functions.md). There are two sets of safe string functions. One set of safe string functions are for use in kernel-mode code (defined in the Ntstrsafe.h). The other set of safe string functions are for use in user-mode applications, and they are defined in Strsafe.h.

If a kernel-mode driver uses the user-mode safe string functions, the driver violates this rule.

**Driver model: WDM**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>SafeStrings</strong> rule.</p>
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

## See also

[**Using Safe String Functions**](../kernel/using-safe-string-functions.md)
