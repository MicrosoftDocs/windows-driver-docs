---
title: SeStopImpersonatingClient routine
description: The SeStopImpersonatingClient routine ends the calling thread's impersonation of a user.
ms.assetid: 1aab384b-919c-4709-9ceb-66616c622714
keywords: ["SeStopImpersonatingClient routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- SeStopImpersonatingClient
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SeStopImpersonatingClient routine


The **SeStopImpersonatingClient** routine ends the calling thread's impersonation of a user.

Syntax
------

```ManagedCPlusPlus
VOID SeStopImpersonatingClient(void);
```

Parameters
----------

This routine has no parameters.

Return value
------------

None

Remarks
-------

A server thread can impersonate a user by calling the [**SeImpersonateClientEx**](https://msdn.microsoft.com/library/windows/hardware/ff556659) routine. When the thread is done impersonating the user, it calls the **SeStopImpersonatingClient** routine to end the impersonation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows XP and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**SeImpersonateClientEx**](https://msdn.microsoft.com/library/windows/hardware/ff556659)

 

 






