---
title: C28114 Warning
description: Warning C28114 Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28114"
---

# C28114


warning: C28114: Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Use <strong>IoCopyCurrentIrpStackLocationToNext</strong> to accomplish this</p></td>
</tr>
</tbody>
</table>

 

The driver is copying an IRP improperly. Improperly copying an IRP can cause serious problems with a driver, including loss of data and system crashes. If an IRP must be copied and [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext) does not suffice, then certain members of the IRP should not be copied or should be zeroed after copying.

 

