---
title: ZwRegistryCreate rule (wdm)
ms.assetid: 7855d9f0-c8f2-42a3-941b-623038c03840
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
description: 
keywords: ["ZwRegistryCreate rule (wdm)"]
topic_type:
- apiref
api_name:
- ZwRegistryCreate
api_type:
- NA
---

# ZwRegistryCreate rule (wdm)


The **ZwRegistryCreate** rule specifies that after calling [**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425), the driver can call the following registry functions only while holding an open handle to the registry key (that is, before any calls to [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) or [**ZwDeleteKey**](https://msdn.microsoft.com/library/windows/hardware/ff566437) to close or delete the handle to the registry key):

-   [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)

-   [**ZwDeleteKey**](https://msdn.microsoft.com/library/windows/hardware/ff566437)

-   [**ZwEnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566447)

-   [**ZwEnumerateValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff566453)

-   [**ZwFlushKey**](https://msdn.microsoft.com/library/windows/hardware/ff566457)

-   [**ZwQueryKey**](https://msdn.microsoft.com/library/windows/hardware/ff567060)

-   [**ZwQueryValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567069)

-   [**ZwSetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567109)

This rule also specifies that the driver must not call [**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425) or [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014) if it is already holding an open handle to that registry key.

Finally, this rule specifies that the driver must not return from the dispatch routine or cancel routine while holding an open handle to a registry key.

This rule does not verify that the driver has called [**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425) or [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014) to acquire handle to the registry key before closing or deleting it.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ZwRegistryCreate</strong> rule.</p>
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

Applies to
----------

[**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)
[**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425)
[**ZwDeleteKey**](https://msdn.microsoft.com/library/windows/hardware/ff566437)
[**ZwEnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566447)
[**ZwEnumerateValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff566453)
[**ZwFlushKey**](https://msdn.microsoft.com/library/windows/hardware/ff566457)
[**ZwQueryKey**](https://msdn.microsoft.com/library/windows/hardware/ff567060)
[**ZwQueryValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567069)
[**ZwSetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567109)
 

 





