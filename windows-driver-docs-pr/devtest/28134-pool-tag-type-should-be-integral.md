---
title: C28134
description: Warning C28134 The type of a pool tag should be integral, not a string or string pointer.
ms.assetid: f61aec4c-4072-421f-aa6d-d9399d0c439c
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p>A pool tag name should be a character literal using single quotation marks (&#39;gaT_&#39;), not a string in double quotation marks. It is normally in reverse byte order.</p></td>
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

 

 





