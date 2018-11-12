---
title: Bug Check 0xC0000218 STATUS_CANNOT_LOAD_REGISTRY_FILE
description: The STATUS_CANNOT_LOAD_REGISTRY_FILE bug check has a value of 0xC0000218. This indicates that a registry file could not be loaded.
ms.assetid: cdcf68fa-8beb-4e21-bc6b-7a9f4c6e9e80
keywords: ["Bug Check 0xC0000218 STATUS_CANNOT_LOAD_REGISTRY_FILE", "STATUS_CANNOT_LOAD_REGISTRY_FILE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- STATUS_CANNOT_LOAD_REGISTRY_FILE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC0000218: STATUS\_CANNOT\_LOAD\_REGISTRY\_FILE


The STATUS\_CANNOT\_LOAD\_REGISTRY\_FILE bug check has a value of 0xC0000218. This indicates that a registry file could not be loaded.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## STATUS\_CANNOT\_LOAD\_REGISTRY\_FILE Parameters


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
<td align="left"><p>Address of the name of the registry hive that could not be loaded.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Zero (Reserved)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Zero (Reserved)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Zero (Reserved)</p></td>
</tr>
</tbody>
</table>

 

This bug check displays a descriptive text message. The name of the damaged file is displayed as part of the message.

Cause
-----

This error occurs if a necessary registry hive file cannot be loaded. Usually this means the file is corrupt or is missing.

In rare instances, this error can be caused by a driver that has corrupted the registry image in memory, or by a memory error in this region.

Resolution
----------

Try using the startup recovery mechanism (for example Startup Repair, Recovery Console, or Emergency Recovery Disk) provided by the operating system. If the problem is a missing or corrupt registry file, that usually fixes the problem.

 

 




