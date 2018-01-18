---
title: Enable heap validation on call
description: Enable heap validation on call
ms.assetid: 779871e0-f8b9-4eb5-9869-8df67586ffab
keywords: ["Enable heap validation on call (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enable heap validation on call


## <span id="ddk_enable_heap_validation_on_call_dtools"></span><span id="DDK_ENABLE_HEAP_VALIDATION_ON_CALL_DTOOLS"></span>


The **Enable heap validation on call** flag validates the entire heap each time a heap function is called.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>hvc</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x80</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_VALIDATE_ALL</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To avoid the high overhead associated with this flag, use the **HeapValidate** function instead of setting this flag, especially at critical junctures, such as when the heap is destroyed. However, this flag is useful for detecting random corruption in a pool.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Enable heap parameter checking](enable-heap-parameter-checking.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Enable%20heap%20validation%20on%20call%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




