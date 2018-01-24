---
title: ParentObjectCheck rule (kmdf)
description: The ParentObjectCheck rule specifies that driver should call WdfMemoryCreate specifying a parent object using a WDF\_OBJECT\_ATTRIBUTES structure.
ms.assetid: E0597996-9067-40C3-8DE9-1048B2227F07
keywords: ["ParentObjectCheck rule (kmdf)"]
topic_type:
- apiref
api_name:
- ParentObjectCheck
api_type:
- NA
---

# ParentObjectCheck rule (kmdf)


The **ParentObjectCheck** rule specifies that driver should call [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706) specifying a parent object using a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. If driver doesn’t set a parent object for the framework memory object then the framework sets the driver as the default parent, so that unless the driver deletes the framework memory object explicitly it’ll remain in the memory until the driver object unloads.

|              |      |
|--------------|------|
| Driver model | KMDF |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ParentObjectCheck</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20ParentObjectCheck%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




