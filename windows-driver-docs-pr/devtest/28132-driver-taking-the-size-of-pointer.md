---
title: C28132
description: Warning C28132 Taking the size of pointer.
ms.assetid: 9047cfb5-220f-42ad-ba1d-3c1bd43a3423
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

The driver is taking the size of a pointer variable, not the size of the value that is pointed to. If the driver needs the size of the pointed-to value, change the code so that it references the value. If the driver actually needs the size of the pointer, take the size of the pointer type (for example, LPSTR, **char\\*** or even **void\\***) to clarify that this is the intent.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
memset(b, 0, sizeof(b));
```

The following code example avoids this warning.

```
memset(b, 0, sizeof(*b));
```

 

 





