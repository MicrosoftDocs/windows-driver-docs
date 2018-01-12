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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20RxDbgBreakPoint%20function%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





