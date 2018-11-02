---
title: C28141
description: Warning C28141 The argument causes the IRQ Level to be set below the current IRQL, and this function cannot be used for that purpose.
ms.assetid: 5cf30e4b-beef-42e0-9d1c-85418b601acb
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28141


warning C28141: The argument causes the IRQ Level to be set below the current IRQL, and this function cannot be used for that purpose

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>IRQL was last set to &lt;<em>IRQL</em>&gt; at line &lt;<em>line-number</em>&gt;&quot;</p></td>
</tr>
</tbody>
</table>

 

A function call that lowers the IRQL at which a caller is executing is being used inappropriately. Typically, the function call lowers the IRQL as part of a more general routine or is intended to raise the caller's IRQL.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
KeRaiseIrql(DISPATCH_LEVEL, &OldIrql);
KeRaiseIrql(PASSIVE_LEVEL, &OldIrql);
```

The following code example avoids this warning.

```
KeRaiseIrql(DISPATCH_LEVEL, &OldIrql);
KeLowerIrql(OldIrql);
```

 

 





