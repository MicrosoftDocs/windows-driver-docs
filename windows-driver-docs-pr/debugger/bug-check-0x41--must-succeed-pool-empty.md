---
title: Bug Check 0x41 MUST_SUCCEED_POOL_EMPTY
description: The MUST_SUCCEED_POOL_EMPTY bug check has a value of 0x00000041. This indicates that a kernel-mode thread has requested too much must-succeed pool.
ms.assetid: 10aafcf4-6af0-41b5-803c-578369bdd810
keywords: ["Bug Check 0x41 MUST_SUCCEED_POOL_EMPTY", "MUST_SUCCEED_POOL_EMPTY"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MUST_SUCCEED_POOL_EMPTY
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x41: MUST\_SUCCEED\_POOL\_EMPTY


The MUST\_SUCCEED\_POOL\_EMPTY bug check has a value of 0x00000041. This indicates that a kernel-mode thread has requested too much must-succeed pool.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MUST\_SUCCEED\_POOL\_EMPTY Parameters


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
<td align="left"><p>The size of the request that could not be satisfied</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The number of pages used from nonpaged pool</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The number of requests from nonpaged pool larger than PAGE_SIZE</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The number of pages available</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

In Microsoft Windows 2000, only a small amount of must-succeed pool is permitted. In Windows XP and later, no driver is permitted to request must-succeed pool.

If a must-succeed request cannot be filled, this bug check is issued.

Resolution
----------

Replace or rewrite the driver which is making the request. A driver should not request must-succeed pool. Instead, it should ask for normal pool and gracefully handle the scenario where the pool is temporarily empty.

The [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command will show the driver that caused the error.

Additionally, it is possible that a second component has depleted the must-succeed pool. To determine if this is the case, first use the **kb** command. Then use [**!vm 1**](-vm.md) to display total pool usage, [**!poolused 2**](-poolused.md) to display per-tag nonpaged pool usage, and **!poolused 4** to display per-tag paged pool usage. The component associated with the tag using the most pool is probably the source of the problem.

 

 




