---
title: RxDbgBreakPoint function
description: RxDbgBreakPoint breaks into the kernel debugger if one is installed.
ms.assetid: 981256a4-2faf-4f9e-acfc-7488230bb62e
keywords: ["RxDbgBreakPoint function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- RxDbgBreakPoint
api_location:
- rxassert.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RxDbgBreakPoint function


**RxDbgBreakPoint** breaks into the kernel debugger if one is installed.

Syntax
------

```ManagedCPlusPlus
VOID RxDbgBreakPoint(
   ULONG LineNumber
);
```

Parameters
----------

*LineNumber*   
The line number in the source file where **RxDbgBreakPoint** was called.

Return value
------------

None

Remarks
-------

This routine calls the kernel **DbgBreakPoint** routine.

This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise it is handled by the debug system. If no debugger is connected to the system, the exception can be handled in the standard way.

In kernel mode, a break exception that is not handled will cause a blue screen (bug check) to result. You can, however, connect a kernel-mode debugger to the target computer that has kernel debugging enabled. For more information, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

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


[**RxAssert**](rxassert.md)

[Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063)

 

 






