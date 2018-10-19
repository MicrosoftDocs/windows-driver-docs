---
title: WriteErrorLog rule (ndis)
description: The WriteErrorLog rule specifies that if the NdisMAllocateSharedMemory function is called in the MiniportInitializeEx function, the driver should also call NdisWriteErrorLogEntry if the allocation fails.
ms.assetid: b626f25a-3101-4c0a-b0a9-fef6ce964055
ms.date: 05/21/2018
keywords: ["WriteErrorLog rule (ndis)"]
topic_type:
- apiref
api_name:
- WriteErrorLog
api_type:
- NA
ms.localizationpriority: medium
---

# WriteErrorLog rule (ndis)


The WriteErrorLog rule specifies that if the **NdisMAllocateSharedMemory** function is called in the *MiniportInitializeEx* function, the driver should also call **NdisWriteErrorLogEntry** if the allocation fails.

Generally, it is a good practice to log an error entry in the log whenever an allocation memory operation fails. Most of the allocation operations occur in the *MiniportInitializeEx* callback function. See the following code example for more information about how to log an error.

|              |      |
|--------------|------|
| Driver model | NDIS |

Example
-------

```
// an example of how to log an error if memory allocation fails PVOID p;
NdisMAllocateSharedMemory(par1, par2, par3, &amp;p, ...);
if (p == NULL)
{
 NdisWriteErrorLogEntry("Memory allocation failed");
}
```

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WriteErrorLog</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

 

 





