---
title: C28173
description: Warning C28173 The current function appears to incorrectly adapt to physical memory above 4 GB.
ms.assetid: 9332c35e-9d04-4286-9eff-3a639589607e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28173


warning C28173: The current function appears to incorrectly adapt to physical memory above 4 GB

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The code does not appear to recover from a call to <strong>IoGetDmaAdapter</strong> that returns a small number of map registers. See the documentation for details.</p></td>
</tr>
</tbody>
</table>

 

On systems that have more than 4 GB of memory, the **IoGetDmaAdapter** function might return fewer map registers than requested; this becomes more likely when the value requested becomes large (approaching 64).This is because of the need to map physical memory above 4 GB into the space below 4 GB.

This warning message appears when code does not adapt to getting fewer registers than it asked for. When a function makes a call to **IoGetDmaAdapter**, the Code Analysis tool simulates that the **IoGetDmaAdapter** function returns a smaller number of registers than requested. The calling function must handle this condition and return successfully.

Note that there are other ways that a driver can fail on systems with more than 4 GB. You should inspect your code for these possible failure modes. For more information about the 4 GB memory issues and the map registers, see [**NdisMAllocateMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff552300).

 

 





