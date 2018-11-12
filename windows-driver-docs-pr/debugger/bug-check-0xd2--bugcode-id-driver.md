---
title: Bug Check 0xD2 BUGCODE_ID_DRIVER
description: The BUGCODE_ID_DRIVER bug check has a value of 0x000000D2. This indicates that a problem occurred with an NDIS driver.
ms.assetid: 697d128c-c79d-454a-a3e7-e9b85e3ab4bc
keywords: ["Bug Check 0xD2 BUGCODE_ID_DRIVER", "BUGCODE_ID_DRIVER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BUGCODE_ID_DRIVER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xD2: BUGCODE\_ID\_DRIVER


The BUGCODE\_ID\_DRIVER bug check has a value of 0x000000D2. This indicates that a problem occurred with an NDIS driver.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BUGCODE\_ID\_DRIVER Parameters


<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Message and Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Number of bytes requested</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p><strong>Allocating shared memory at raised IRQL.</strong> A driver called <strong>NdisMAllocateSharedMemory</strong> with IRQL &gt;= DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>The <em>Status</em> value submitted to <strong>NdisMResetComplete</strong></p></td>
<td align="left"><p>The <em>AddressingReset</em> value submitted to <strong>NdisMResetComplete</strong></p></td>
<td align="left"><p>0</p></td>
<td align="left"><p><strong>Completing reset when one is not pending.</strong> A driver called <strong>NdisMResetComplete</strong>, but no reset was pending.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Memory page containing address being freed</p></td>
<td align="left"><p>Address of shared memory signature</p></td>
<td align="left"><p>Virtual address being freed</p></td>
<td align="left"><p><strong>Freeing shared memory not allocated.</strong> A driver called <strong>NdisMFreeSharedMemory</strong> or <strong>NdisMFreeSharedMemoryAsync</strong> with an address that is not located in NDIS shared memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Address of the packet that is incorrectly included in the packet array</p></td>
<td align="left"><p>Address of the packet array</p></td>
<td align="left"><p>Number of packets in the array</p></td>
<td align="left"><p><strong>Indicating packet not owned by it.</strong> The miniport&#39;s packet array is corrupt.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address of the MiniBlock</p></td>
<td align="left"><p>Address of the driver object</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p><strong>NdisAddDevice: AddDevice</strong> called with a <strong>MiniBlock</strong> that is not on the <strong>NdisMiniDriverList</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address of the MiniBlock</p></td>
<td align="left"><p>The MiniBlock&#39;s reference count</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p><strong>NdisMUnload: MiniBlock</strong> is getting unloaded but it is still on <strong>NdisMiniDriverList</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Memory page</p></td>
<td align="left"><p>Wrapper context</p></td>
<td align="left"><p>Address of shared memory signature</p></td>
<td align="left"><p><strong>Overwrote past allocated shared memory.</strong> The address being written to is not located in NDIS shared memory.</p></td>
</tr>
</tbody>
</table>

 

In the following instances of this bug check, the meaning of the parameters depends on the message and on the value of Parameter 4.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Message and Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Address of the miniport interrupt</p></td>
<td align="left"><p>Address of the miniport timer queue</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p><strong>Unloading without deregistering interrupt.</strong> A miniport driver failed its initialization without deregistering its interrupt.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Address of the miniport timer queue</p></td>
<td align="left"><p>Address of the miniport interrupt</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p><strong>Unloading without deregistering interrupt.</strong> A miniport driver did not deregister its interrupt during the halt process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Address of the miniport interrupt</p></td>
<td align="left"><p>Address of the miniport timer queue</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p><strong>Unloading without deregistering timer.</strong> A miniport driver failed its initialization without successfully canceling all its timers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Address of the miniport block</p></td>
<td align="left"><p>Address of the miniport timer queue</p></td>
<td align="left"><p>Address of the miniport interrupt</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p><strong>Unloading without deregistering timer.</strong> A miniport driver halted without successfully canceling all its timers.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This bug check code only occurs on Windows 2000 and Windows XP. In Windows Server 2003 and later, the corresponding code is [**bug check 0x7C**](bug-check-0x7c--bugcode-ndis-driver.md) (BUGCODE\_NDIS\_DRIVER).

On the checked build of Windows, only the **Allocating Shared Memory at Raised IRQL** and **Completing Reset When One is Not Pending** instances of this bug check can occur. All the other instances of bug check 0xD2 are replaced with ASSERTs. See [Breaking Into the Debugger](breaking-into-the-debugger.md) for details.

 

 




