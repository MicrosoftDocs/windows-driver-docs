---
title: C28147
description: Warning C28147 The use of a default pool tag (' kdD' or ' mdW') for calls to this function defeats the purpose of pool tagging.
ms.assetid: 4838b006-349e-45d1-8ac3-42cbf0d880b7
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28147


warning C28147: The use of a default pool tag (' kdD' or ' mdW') for calls to this function defeats the purpose of pool tagging

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>This may be caused by using ExAllocatePool directly, or the tag may have been copied from that macro. In any case, ExAllocatePoolWithTag (etc.) should be used with a unique tag.</p></td>
</tr>
</tbody>
</table>

 

The driver is specifying a default pool tag. Because the system tracks pool use by pool tag, only those drivers that use a unique pool tag can identify and distinguish their pool use.

**ExAllocatePool** and **ExAllocatePoolWithQuota** are obsolete and should be replaced by [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) and [**ExAllocatePoolWithQuotaTag**](https://msdn.microsoft.com/library/windows/hardware/ff544513), which let you specify a unique pool tag.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28147%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




