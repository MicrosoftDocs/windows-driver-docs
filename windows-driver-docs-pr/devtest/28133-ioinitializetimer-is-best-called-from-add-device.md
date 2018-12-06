---
title: C28133
description: Warning C28133 IoInitializeTimer is best called from AddDevice.
ms.assetid: c832cf67-1fc2-491b-a9e3-d35c5d9f6b73
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28133


warning C28133: IoInitializeTimer is best called from AddDevice

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>IoInitializeTimer can only be called once per device object. Calling it from the AddDevice routine helps assure that it is not unexpectedly called more than once.</p></td>
</tr>
</tbody>
</table>

 

The driver is calling [**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344) in a routine other than its **AddDevice** routine. The Code Analysis tool is using this opportunity to suggest a best practice recommendation that can prevent errors and make the driver code more reliable.

 

 





