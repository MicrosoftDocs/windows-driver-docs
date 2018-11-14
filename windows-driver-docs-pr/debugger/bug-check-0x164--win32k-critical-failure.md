---
title: Bug Check 0x164 WIN32K_CRITICAL_FAILURE
description: The WIN32K_CRITICAL_FAILURE bug check has a value of 0x00000164. This indicates that Win32k has encountered a critical failure.
ms.assetid: 6274C852-53DA-4E01-B2A6-D7485501BE50
keywords: ["Bug Check 0x164 WIN32K_CRITICAL_FAILURE", "WIN32K_CRITICAL_FAILURE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WIN32K_CRITICAL_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x164: WIN32K\_CRITICAL\_FAILURE


The WIN32K\_CRITICAL\_FAILURE bug check has a value of 0x00000164. This indicates that Win32k has encountered a critical failure.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WIN32K\_CRITICAL\_FAILURE Parameters


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
<td align="left">1</td>
<td align="left"><p>1 - Type of the failure.</p>
0x1 : REGION_VALIDATION_FAILURE- Region is out of surface bounds.
<p>2 - Pointer to DC</p>
<p>3 - Pointer to SURFACE</p>
<p>4 - Pointer to REGION</p>
0x2 : OPERATOR_NEW_USED - Operator &quot;new&quot; is used to allocate memory.
<p>2 - Reserved</p>
<p>3 - Reserved</p>
<p>4 - Reserved</p>
<p></p>
0x3 : CRITICAL_APISET_EXTENSIONS_MISSING - Critical extension APISET API is missing.
<p>2 - wchar_t* to the name of the missing function</p>
<p>3 - Reserved</p>
<p>4 - Reserved</p>
0x4 : GDI_SPRITE_SURFACE_INVALID_DELETE - GDI sprite&#39;s shape is being deleted without deleting the sprite.
<p>2 - Handle to the SURFACE</p>
<p>3 - Reference count to the SURFACE</p>
<p>4 - PID of the SURFACE owner</p>
0x5 : POINTER_DEVICE_EXCLUSIVE_OPEN_FAILED - Failed to open Pointer device.
<p></p>
<p>2 - UNICODE_STRING of the device</p>
<p>3 - Reserved</p>
<p>4 - Reserved</p>
0x8 : PUBLIC_DC_INVALID_PRIVATE_MEMBER - A public DC has a pointer to an object owned by a specific process.
<p>2 - Pointer to DC</p>
<p>3 - Process id that owns the object</p>
<p>4 - Reserved</p>
0xA : TTFD_INVOKE_ILLEGAL_ID - Invalid function table index is being used in TTFD.
<p>2 - Reserved</p>
<p>3 - Reserved</p>
<p>4 - Reserved</p>
0xB : OTFD_INVOKE_ILLEGAL_ID - Invalid function table index is being used in ATMFD.
<p>2 - Reserved</p>
<p>3 - Reserved</p>
<p>4 - Reserved</p>
0xC : GFPE_INVOKE_ILLEGAL_ID - Invalid function table index is being used in a PALETTE.
<p>2 - Pointer to the PALETTE</p>
<p>3 - The invalid index</p>
<p>4 - Maximum valid index + 1</p>
0x10 : USER_SAS_REGISTRATION_FAILED - SAS key registration has failed.
<p>2 - vkey</p>
<p>3 - modifiers</p>
<p>4 - flags</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>

 

 

 




