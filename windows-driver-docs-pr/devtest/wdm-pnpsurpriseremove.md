---
title: PnpSurpriseRemove rule (wdm)
description: The PnpSurpriseRemove rule specifies that the driver does not call IoDeleteDevice or IoDetachDevice while processing an IRP\_MN\_SURPRISE\_REMOVAL request.
ms.assetid: 58553c78-04c3-423c-bf68-69d5a8fbfa9b
ms.date: 05/21/2018
keywords: ["PnpSurpriseRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpSurpriseRemove
api_type:
- NA
ms.localizationpriority: medium
---

# PnpSurpriseRemove rule (wdm)


The **PnpSurpriseRemove** rule specifies that the driver does not call IoDeleteDevice or IoDetachDevice while processing an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request.

The PnP manager sends the [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request to notify drivers that a device is no longer available for I/O operations and that it has probably been unexpectedly removed from the computer.

-   All PnP drivers must handle [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request.
-   The driver must not call [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) or [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087) on device objects until the IRP\_MN\_SURPRISE\_REMOVAL IRP succeeds and all open handles to the device are closed.
-   The PnP manager then sends an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to the device stack. In response to the remove IRP, drivers detach their device objects from the stack and delete them.

For more information about how a driver should respond to [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request, see [**Handling an IRP\_MN\_SURPRISE\_REMOVAL Request**](https://msdn.microsoft.com/library/windows/hardware/ff546699)

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>PnpSurpriseRemove</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)
[**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087)
See also
--------

[**Handling an IRP\_MN\_SURPRISE\_REMOVAL Request**](https://msdn.microsoft.com/library/windows/hardware/ff546699)
[Analyzing a Driver Using Verification and Code Analysis Tools](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver)
[**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760)
[**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)
 

 





