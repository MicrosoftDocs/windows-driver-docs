---
title: C28121
description: Warning C28121 The function is not permitted to be called at the current IRQ level. The current level is too high.
ms.assetid: f0ab65ee-e160-4118-b001-7a8ba83d9671
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28121


warning C28121: The function is not permitted to be called at the current IRQ level. The current level is too high.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>IRQL was last set to &lt;<em>IRQL</em>&gt; at line &lt;<em>line-number</em>&gt;.The level might have been inferred from the function signature.</p></td>
</tr>
</tbody>
</table>

 

The driver is executing at an IRQL that is too high for the function that it is calling.

When the Code Analysis tool reports this warning, consult the WDK documentation for the function and verify the IRQL at which the function can be called.

The Code Analysis tool infers the current IRQL and reports this warning only when it has inferred enough about the IRQL to detect the error. This inference might be based on the *function signature* (the arguments and result type) of the function being analyzed, or from prior calls along the current path.

If the Code Analysis tool cannot determine the IRQL at which the driver is running, it will not report this warning, even if the function is being called at the wrong IRQL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28121%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




