---
title: C28147
description: Warning C28147 The use of a default pool tag (' kdD' or ' mdW') for calls to this function defeats the purpose of pool tagging.
ms.assetid: 4838b006-349e-45d1-8ac3-42cbf0d880b7
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





