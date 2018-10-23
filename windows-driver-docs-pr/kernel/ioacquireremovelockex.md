---
title: Windows kernel routines reserved for system use
author: windows-driver-content
description: Windows kernel routines reserved for system use
ms.assetid: 78b0562a-903a-467d-9bf0-f5499ae47063
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows kernel routines reserved for system use


The following routines are reserved for system use:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>IoAcquireRemoveLockEx</strong></td>
<td><p>See [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204).</p></td>
</tr>
<tr class="even">
<td><strong>IoInitializeRemoveLockEx</strong></td>
<td><p>Use [<strong>IoInitializeRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549324) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoReleaseRemoveLockAndWaitEx</strong></td>
<td><p>See [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567).</p></td>
</tr>
<tr class="even">
<td><strong>IoReleaseRemoveLockEx</strong></td>
<td><p>See [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560).</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)  
[**IoInitializeRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549324)  
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)  
[**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567)  



