---
title: SafeStrings rule (wdm)
description: The SafeStrings rule specifies that the driver calls only those string manipulations functions that protect the system from unintentional or malicious intrusion. These safe string functions for drivers are defined in Ntstrsafe.h.
ms.assetid: 77e949cf-b184-4235-80c4-4718d4808d11
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SafeStrings rule (wdm)"]
topic_type:
- apiref
api_name:
- SafeStrings
api_type:
- NA
---

# SafeStrings rule (wdm)


The **SafeStrings** rule specifies that the driver calls only those string manipulations functions that protect the system from unintentional or malicious intrusion. These safe string functions for drivers are defined in Ntstrsafe.h.

To comply with this rule, use the string functions that are considered to be safe for kernel-mode drivers. The safe string functions and the unsafe functions that they replace are listed in [**Using Safe String Functions**](https://msdn.microsoft.com/library/windows/hardware/ff565508). There are two sets of safe string functions. One set of safe string functions are for use in kernel-mode code (defined in the Ntstrsafe.h). The other set of safe string functions are for use in user-mode applications, and they are defined in Strsafe.h.

If a kernel-mode driver uses the user-mode safe string functions, the driver violates this rule.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SafeStrings</strong> rule.</p>
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

See also
--------

[**Using Safe String Functions**](https://msdn.microsoft.com/library/windows/hardware/ff565508)
 

 





