---
title: IrqlKeWaitForMultipleObjects rule (wdm)
description: The IrqlKeWaitForMultipleObjects rule specifies that callers of the KeWaitForMultipleObjects routine must be running at proper IRQL based upon the Timeout parameter.
ms.date: 05/21/2018
keywords: ["IrqlKeWaitForMultipleObjects rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeWaitForMultipleObjects
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlKeWaitForMultipleObjects rule (wdm)


The **IrqlKeWaitForMultipleObjects** rule specifies that callers of the [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) routine must be running at proper IRQL based upon the *Timeout* parameter.

Callers of **IrqlKeWaitForMultipleObjects** routine can be running at IRQL &lt;= DISPATCH\_LEVEL, except in the following situations:

-   If *Timeout* &lt;&gt; 0, the caller of the [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) routine must be running at IRQL &lt;= APC\_LEVEL.
-   If *Timeout* != NULL and \**Timeout* = 0, the caller of the [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) routine must be running at IRQL = DISPATCH\_LEVEL.

-   If *Timeout* = **NULL**, or \**Timeout* != 0, the caller of the [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) routine must running at IRQL &lt;= APC\_LEVEL.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>IrqlKeWaitForMultipleObjects</strong> rule.</p>
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

## Applies to

[**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects)
