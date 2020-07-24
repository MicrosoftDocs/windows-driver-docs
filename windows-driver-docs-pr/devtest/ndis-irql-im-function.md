---
title: Irql\_IM\_Function rule (ndis)
description: The Irql\_IM\_Function rule specifies that the NDIS functions for Intermediate (IM) drivers must be called at correct IRQL levels.
ms.assetid: f13ee05d-41d5-48e1-aa53-8904d99f94da
ms.date: 05/21/2018
keywords: ["Irql_IM_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_IM_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_IM\_Function rule (ndis)


The Irql\_IM\_Function rule specifies that the NDIS functions for Intermediate (IM) drivers must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisIMAssociateMiniport**
**NdisIMCancelInitializeDeviceInstance**
**NdisIMDeInitializeDeviceInstance**
**NdisIMGetBindingContext**
**NdisIMInitializeDeviceInstanceEx**

**Driver model: NDIS**

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>Irql_IM_Function</strong> rule.</p>
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

[**NdisIMAssociateMiniport**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimassociateminiport)
[**NdisIMCancelInitializeDeviceInstance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimcancelinitializedeviceinstance)
[**NdisIMDeInitializeDeviceInstance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimdeinitializedeviceinstance)
[**NdisIMGetBindingContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimgetbindingcontext)
[**NdisIMInitializeDeviceInstanceEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex)








