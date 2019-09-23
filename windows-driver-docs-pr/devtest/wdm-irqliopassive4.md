---
title: IrqlIoPassive4 rule (wdm)
ms.assetid: 2bdfa09d-0777-4eaf-85ff-d5accc0f31de
ms.date: 05/21/2018
description: 
keywords: ["IrqlIoPassive4 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive4
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlIoPassive4 rule (wdm)


The **IrqlIoPassive4** rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE\_LEVEL:

-   [**IoCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatefile)

-   [**IoCreateNotificationEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatenotificationevent)

-   [**IoCreateSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatesymboliclink)

-   [**IoCreateSynchronizationEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatesynchronizationevent)

-   [**IoCreateUnprotectedSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreateunprotectedsymboliclink)

-   [**IoDeassignArcName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-iodeassignarcname)

-   [**IoDeleteController**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-iodeletecontroller)

-   [**IoDeleteSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iodeletesymboliclink)

-   [**IoDisconnectInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iodisconnectinterrupt)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x0002000D) |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>IrqlIoPassive4</strong> rule.</p>
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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a> and select the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**IoCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatefile)
[**IoCreateNotificationEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatenotificationevent)
[**IoCreateSynchronizationEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreatesynchronizationevent)
[**IoCreateUnprotectedSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocreateunprotectedsymboliclink)
[**IoDeleteController**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-iodeletecontroller)
[**IoDeleteSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iodeletesymboliclink)
[**IoDisconnectInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iodisconnectinterrupt)
 

 





