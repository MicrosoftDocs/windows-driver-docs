---
title: Init\_NdisAllocateIoWorkItem rule (ndis)
description: The Init\_NdisAllocateIoWorkItem rule specifies that if NdisAllocateIoWorkItem is called at least once during MiniportInitializeEx, the NdisFreeIoWorkItem function should - be called at least once in MPHaltEx, if MiniportInitializeEx succeeds.
ms.assetid: B7889948-741C-4C54-B27F-3175ED4EA7BA
ms.date: 05/21/2018
keywords: ["Init_NdisAllocateIoWorkItem rule (ndis)"]
topic_type:
- apiref
api_name:
- Init_NdisAllocateIoWorkItem
api_type:
- NA
ms.localizationpriority: medium
---

# Init\_NdisAllocateIoWorkItem rule (ndis)


The **Init\_NdisAllocateIoWorkItem** rule specifies that if [**NdisAllocateIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocateioworkitem) is called at least once during [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_initialize), the [**NdisFreeIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreeioworkitem) function should:

-   - be called at least once in MPHaltEx, if [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_initialize) succeeds.
-   - be called in [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_initialize), if *MiniportInitializeEx* fails.

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>Init_NdisAllocateIoWorkItem</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisAllocateIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocateioworkitem)
[**NdisFreeIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreeioworkitem)
[**RemoveHeadList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-removeheadlist)
 

 





