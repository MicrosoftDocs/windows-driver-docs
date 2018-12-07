---
title: Dispatch Routine IRQL and Thread Context
description: Dispatch Routine IRQL and Thread Context
ms.assetid: 95f3a976-c97a-4c8a-979b-14a0ddd823a2
keywords:
- IRP dispatch routines WDK file system , IRQL
- IRP dispatch routines WDK file system , thread context
- nonarbitrary thread context WDK file system
- thread context WDK file system
- arbitrary thread context WDK file system
- IRQLs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dispatch Routine IRQL and Thread Context


## <span id="ddk_dispatch_routine_irql_and_thread_context_if"></span><span id="DDK_DISPATCH_ROUTINE_IRQL_AND_THREAD_CONTEXT_IF"></span>


The following table summarizes the IRQL and thread context requirements for file system filter driver dispatch routines.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Dispatch routine</th>
<th align="left">Caller&#39;s IRQL:</th>
<th align="left">Caller&#39;s thread context:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Cleanup</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>Close</p></td>
<td align="left"><p>APC_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Create</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>DeviceControl (except paging I/O)</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DeviceControl (paging I/O path)</p></td>
<td align="left"><p>APC_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectoryControl</p></td>
<td align="left"><p>APC_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FlushBuffers</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>FsControl (except paging I/O)</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FsControl (paging I/O path)</p></td>
<td align="left"><p>APC_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>LockControl</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PnP</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>QueryEa</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>QueryInformation</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>QueryQuota</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>QuerySecurity</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>QueryVolumeInfo</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Read (except paging I/O)</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>Read (paging I/O path)</p></td>
<td align="left"><p>APC_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SetEa</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>SetInformation</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SetQuota</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>SetSecurity</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SetVolumeInfo</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>Shutdown</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Write (except paging I/O)</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
<td align="left"><p>Nonarbitrary</p></td>
</tr>
<tr class="even">
<td align="left"><p>Write (paging I/O path)</p></td>
<td align="left"><p>APC_LEVEL</p></td>
<td align="left"><p>Arbitrary</p></td>
</tr>
</tbody>
</table>

 

 

 




