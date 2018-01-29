---
title: SafeStrings rule (wdm)
description: The SafeStrings rule specifies that the driver calls only those string manipulations functions that protect the system from unintentional or malicious intrusion. These safe string functions for drivers are defined in Ntstrsafe.h.
ms.assetid: 77e949cf-b184-4235-80c4-4718d4808d11
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20SafeStrings%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




