---
title: ZwRegistryOpen rule (storport)
description: This rule verifies that the handle to the registry key opened via ZwOpenKey is subsequently used correctly by other ZwXxx routines.
ms.assetid: E423616B-C990-4D26-ABB4-6061BF3B6A21
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ZwRegistryOpen rule (storport)"]
topic_type:
- apiref
api_name:
- ZwRegistryOpen
api_type:
- NA
---

# ZwRegistryOpen rule (storport)


This rule verifies that the handle to the registry key opened via **ZwOpenKey** is subsequently used correctly by other ZwXxx routines. The routines **ZwEnumerateKey**, **ZwEnumerateValueKey**, **ZwFlushKey**, **ZwQueryKey**, **ZwQueryValueKey**, **ZwSetValueKey**, **ZwClose**, and **ZwDeleteKey** must not be called on a handle that isn't open. The handle must also be closed before returning.

|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ZwRegistryOpen</strong> rule.</p>
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
[**ZwDeleteKey**](https://msdn.microsoft.com/library/windows/hardware/ff566437)
[**ZwEnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566447)
[**ZwEnumerateValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff566453)
[**ZwFlushKey**](https://msdn.microsoft.com/library/windows/hardware/ff566457)
[**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014)
[**ZwQueryKey**](https://msdn.microsoft.com/library/windows/hardware/ff567060)
[**ZwQueryValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567069)
[**ZwSetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567109)
 

 





