---
title: Bug Check 0x74 BAD_SYSTEM_CONFIG_INFO
description: The BAD_SYSTEM_CONFIG_INFO bug check has a value of 0x00000074. This bug check indicates that there is an error in the registry.
ms.assetid: c59ddc44-d860-4fbb-a975-ae7226fdce86
keywords: ["Bug Check 0x74 BAD_SYSTEM_CONFIG_INFO", "BAD_SYSTEM_CONFIG_INFO"]
ms.author: domars
ms.date: 08/17/2018
topic_type:
- apiref
api_name:
- BAD_SYSTEM_CONFIG_INFO
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x74: BAD\_SYSTEM\_CONFIG\_INFO


The BAD\_SYSTEM\_CONFIG\_INFO bug check has a value of 0x00000074. This bug check indicates that there is an error in the registry.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BAD\_SYSTEM\_CONFIG\_INFO Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The NT status value/code (if it is available)</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The BAD\_SYSTEM\_CONFIG\_INFO bug check occurs if the SYSTEM hive is corrupt. However, this corruption is unlikely, because the boot loader, checks a hive for corruption when it loads the hive.

This bug check can also occur if some critical registry keys and values are missing. The keys and values might be missing if a user manually edited the registry or if an application or service corrupted the registry.

Looking up the NT status value returned in parameter 4 can provide additional information, see [NTSTATUS Values](https://msdn.microsoft.com/library/cc704588.aspx) for a listing. 

Resolution
----------

Try booting into safe mode and then restart the OS normally. If the restart does not fix the problem, the registry damage is too extensive. Try the following steps.

-   If you have a system restore point, try restoring to an earlier restore point.
-   Reset your PC.
-   Use installation media to restore or reset your PC.
-   Use installation media to reinstall Windows.

For more information, see [Recovery options in Windows 10](https://windows.microsoft.com/windows-10/windows-10-recovery-options#).

 

 




