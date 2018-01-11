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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20SeStopImpersonatingClient%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





