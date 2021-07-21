---
title: StorPortMSILock rule (storport)
description: Miniport drivers are required to acquire the MSI spin lock for a message if, and only if, the InterruptSynchronizationMode member of the PORT\_CONFIGURATION\_INFORMATION (Storport) structure is set to InterruptSynchronizePerMessage.
ms.date: 05/21/2018
keywords: ["StorPortMSILock rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortMSILock
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortMSILock rule (storport)


Miniport drivers are required to acquire the MSI spin lock for a message if, and only if, the **InterruptSynchronizationMode** member of the [**PORT\_CONFIGURATION\_INFORMATION (Storport)**](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)) structure is set to **InterruptSynchronizePerMessage**. This rule verifies that calls to [**StorPortAcquireMSISpinLock**](/windows-hardware/drivers/ddi/storport/nf-storport-storportacquiremsispinlock) are only made if the synchronization mode is **InterruptSynchronizePerMessage**.

**Driver model: Storport**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>StorPortMSILock</strong> rule.</p>
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

