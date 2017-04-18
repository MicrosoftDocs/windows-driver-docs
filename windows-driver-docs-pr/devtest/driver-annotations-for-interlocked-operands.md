---
title: Driver annotations for interlocked operands
description: Driver annotations for interlocked operands
ms.assetid: 33C85016-765B-42BF-9F38-BB682951B20C
---

# Driver annotations for interlocked operands


A large family of functions takes as one of their parameters the address of a variable that should be accessed by using an interlocked processor instruction. These are cache read-through atomic instructions, and if the operands are used incorrectly, very subtle bugs result.

Use the following annotation for function parameters to identify it as an interlocked operand.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Interlocked operand annotation</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="_Interlocked_operand_"></span><span id="_interlocked_operand_"></span><span id="_INTERLOCKED_OPERAND_"></span>_Interlocked_operand_</p></td>
<td align="left"><p>The annotated function parameter is the target operand of one of the interlocked functions. Those operands must have specific additional properties.</p></td>
</tr>
</tbody>
</table>

 

Function parameters annotated with the \_Interlocked\_operand\_ are expected to be shared between processes. Variables used with this annotation must:

-   Be declared **volatile.**

-   Not be a local variable. Use of a local variable usually indicates a misunderstanding of the function's intent. Even if a local variable is somehow shared, system paging requirements make addressing variables in another process problematic.

-   Not be accessed except by an interlocked function. Without the explicit use of an interlocked function, the operation might access stale data, might occur only in a single processor’s cache, or might be delayed in reaching the rest of the system.

System-supplied functions are already annotated for interlocked operands.

The following example shows the annotation for the [**InterlockedExchange**](https://msdn.microsoft.com/library/windows/hardware/ff547892) function. This annotation specifies that the Target parameter must always be accessed by using an interlocked operation.

```
LONG  
InterlockedExchange (  
    _Inout_ _Interlocked_operand_ LONG volatile *Target,  
    _In_ LONG Value  
    );  

```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Drivers](sal-2-annotations-for-windows-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20annotations%20for%20interlocked%20operands%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





