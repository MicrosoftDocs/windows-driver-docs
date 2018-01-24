---
title: KsProcessingMutex rule ()
ms.assetid: AD73B241-7B08-4E48-94A1-B6BDE78590E6
description: 
keywords: ["KsProcessingMutex rule ()"]
topic_type:
- apiref
api_name:
- KsProcessingMutex
api_type:
- NA
---

# KsProcessingMutex rule ()


The KsProcessingMutex rule specifies that a KS miniport driver uses the processing mutex in the correct sequence:

-   The processing mutex cannot be obtained recursively.
-   A thread that has acquired the processing mutex should not subsequently attempt to acquire the filter control mutex.
-   A thread should not release the processing mutex without acquiring it first.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0008100B) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).</p></td>
</tr>
</tbody>
</table>

 

See also
--------

[Processing Mutex in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff567790)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20KsProcessingMutex%20rule%20%28%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




