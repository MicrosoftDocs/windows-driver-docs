---
title: C28132
description: Warning C28132 Taking the size of pointer.
ms.assetid: 9047cfb5-220f-42ad-ba1d-3c1bd43a3423
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28132


warning C28132: Taking the size of pointer

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>This will yield the size of a pointer (4 or 8), not the size of the object pointed to. Dereference the pointer, or if the size of a pointer was intended, use the pointer type or (void *) instead.</p></td>
</tr>
</tbody>
</table>

 

The driver is taking the size of a pointer variable, not the size of the value that is pointed to. If the driver needs the size of the pointed-to value, change the code so that it references the value. If the driver actually needs the size of the pointer, take the size of the pointer type (for example, LPSTR, **char\*** or even **void\***) to clarify that this is the intent.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
memset(b, 0, sizeof(b));
```

The following code example avoids this warning.

```
memset(b, 0, sizeof(*b));
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28132%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




