---
title: C28153
description: Warning C28153 The value for an IRQL from annotation could not be evaluated in this context.
ms.assetid: 384d0925-b23b-4ba7-b5fb-34bb7106ca3f
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28153


warning C28153: The value for an IRQL from annotation could not be evaluated in this context.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Probable annotation error.</p>
<p>The following was computed: &lt;<em>val</em>&gt;</p></td>
</tr>
</tbody>
</table>

 

This warning indicates that the Code Analysis tool cannot interpret the function annotation because the annotation is not coded correctly. As a result, the Code Analysis tool cannot determine the specified IRQL value.

This warning can occur with any of the driver-specific annotations that mention an IRQL when the Code Analysis tool cannot evaluate the expression for the IRQL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28153%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




