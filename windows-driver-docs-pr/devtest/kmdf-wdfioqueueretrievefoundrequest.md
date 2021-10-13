---
title: WdfIoQueueRetrieveFoundRequest rule (kmdf)
description: The WdfIoQueueRetrieveFoundRequest rule specifies that WdfIoQueueRetrieveFoundRequest method is called only after WdfIoQueueFindRequest is called and returned STATUS\_SUCCESS and no WdfObjectDereference is called on the same request.
ms.date: 05/21/2018
keywords: ["WdfIoQueueRetrieveFoundRequest rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfIoQueueRetrieveFoundRequest
api_type:
- NA
ms.localizationpriority: medium
---

# WdfIoQueueRetrieveFoundRequest rule (kmdf)


The **WdfIoQueueRetrieveFoundRequest** rule specifies that [**WdfIoQueueRetrieveFoundRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievefoundrequest) method is called only after [**WdfIoQueueFindRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest) is called and returned STATUS\_SUCCESS and no [**WdfObjectDereference**](../wdf/wdfobjectdereference.md) is called on the same request.

If [**WdfIoQueueFindRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest) returns STATUS\_SUCCESS it increments the reference count of the output request object, the driver must call [**WdfObjectDereference**](../wdf/wdfobjectdereference.md) after it has finished using this request handle.

**Driver model: KMDF**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>WdfIoQueueRetrieveFoundRequest</strong> rule.</p>
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

[**WdfIoQueueFindRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest)
[**WdfIoQueueRetrieveFoundRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievefoundrequest)
[**WdfObjectDereference**](../wdf/wdfobjectdereference.md)
