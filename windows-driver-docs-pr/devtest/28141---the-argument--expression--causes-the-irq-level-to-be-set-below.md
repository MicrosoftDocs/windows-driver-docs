---
title: C28141
description: Warning C28141 The argument causes the IRQ Level to be set below the current IRQL, and this function cannot be used for that purpose.
ms.assetid: 5cf30e4b-beef-42e0-9d1c-85418b601acb
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28141%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




