---
title: C28134
description: Warning C28134 The type of a pool tag should be integral, not a string or string pointer.
ms.assetid: f61aec4c-4072-421f-aa6d-d9399d0c439c
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28134


warning C28134: The type of a pool tag should be integral, not a string or string pointer

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>A pool tag name should be a character literal using single quotation marks ('gaT_'), not a string in double quotation marks. It is normally in reverse byte order.</p></td>
</tr>
</tbody>
</table>

 

The driver is calling a function that assigns a pool tag, such as [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520), but it is using a value other than a literal in single quotation marks to specify the value of the pool tag. Do not use a quoted string in a pool tag.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
p = ExAllocatePoolWithTag(NonPagedPool, 30, "_Tag");
```

The following code example avoids this warning.

```
p = ExAllocatePoolWithTag(NonPagedPool, 30, &#39;gaT_&#39;);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28134%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




