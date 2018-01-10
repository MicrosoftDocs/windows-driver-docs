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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20RxAssert%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





