---
title: MiniportOnlyWdmDevice rule (kmdf)
description: The MiniportOnlyWdmDevice rule specifies that WDF drivers should not use IoCreateDevice and IoCreateDeviceSecure functions to create bare WDM device objects.
ms.assetid: 23B9431E-3932-42F3-B797-0820D9A43295
ms.date: 05/21/2018
keywords: ["MiniportOnlyWdmDevice rule (kmdf)"]
topic_type:
- apiref
api_name:
- MiniportOnlyWdmDevice
api_type:
- NA
ms.localizationpriority: medium
---

# MiniportOnlyWdmDevice rule (kmdf)


The **MiniportOnlyWdmDevice** rule specifies that WDF drivers should not use [**IoCreateDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatedevice) and [**IoCreateDeviceSecure**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) functions to create bare WDM device objects. This will cause a the computer to crash if someone tries to send an IRP to the WDM device. This is because IRP dispatch entries of the device are set to WDF-specific entries, but the framework hasn’t created a WDF device. However, miniport drivers can use the DDIs because driver dispatch entry points aren’t set for them.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>MiniportOnlyWdmDevice</strong> rule.</p>
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

[**WdfDriverCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdrivercreate)
[**IoCreateDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatedevice)
[**IoCreateDeviceSecure**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure)
 

 





