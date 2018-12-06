---
title: RxAssert routine
description: RxAssert sends an ASSERT string on checked builds of RDBSS to a kernel debugger if one is installed. For retail builds of RDBSS, calls to this routine will bug check.
ms.assetid: 3ef01569-74ef-4f35-acaf-9c01f2b9d9a7
keywords: ["RxAssert routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- RxAssert
api_location:
- rxassert.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RxAssert routine


**RxAssert** sends an ASSERT string on checked builds of RDBSS to a kernel debugger if one is installed. For retail builds of RDBSS, calls to this routine will bug check.

Syntax
------

```ManagedCPlusPlus
VOID RxAssert(
  _In_     PVOID FailedAssertion,
  _In_     PVOID FileName,
  _In_     ULONG LineNumber,
  _In_opt_ PCHAR Message
);
```

Parameters
----------

*FailedAssertion* \[in\]  
The failed assertion.

*FileName* \[in\]  
The name of the source file where **RxAssert** or **RtlAssert** was called.

*LineNumber* \[in\]  
The line number in the source file where **RxAssert** or **RtlAssert** was called.

*Message* \[in, optional\]  
An optional message.

Return value
------------

None

Remarks
-------

When the *rxassert.h* include file is used, Windows kernel RtlAssert calls will be redefined to call this RxAssert routine as well.

On retail builds, **RxAssert** will call **KeBugCheckEx** passing in the value 0xa55a0000 ORed with the line number as BugCheckParamater1.

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
<td align="left"><p>Header</p></td>
<td align="left">Rxassert.h (include Rxassert.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**ASSERT**](https://msdn.microsoft.com/library/windows/hardware/ff542107)

[RtlAssert](https://msdn.microsoft.com/library/windows/hardware/ff563638)

[**RxDbgBreakPoint**](rxdbgbreakpoint.md)

 

 






