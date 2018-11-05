---
title: Bug Check 0x3F NO_MORE_SYSTEM_PTES
description: The NO_MORE_SYSTEM_PTES bug check has a value of 0x0000003F. This is the result of a system which has performed too many I/O actions.
ms.assetid: b8164ec3-87c3-4629-ab70-6addbf368b76
keywords: ["Bug Check 0x3F NO_MORE_SYSTEM_PTES", "NO_MORE_SYSTEM_PTES"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NO_MORE_SYSTEM_PTES
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x3F: NO\_MORE\_SYSTEM\_PTES


The NO\_MORE\_SYSTEM\_PTES bug check has a value of 0x0000003F. This is the result of a system which has performed too many I/O actions. This has resulted in fragmented system page table entries (PTE).

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NO\_MORE\_SYSTEM\_PTES Parameters


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
<td align="left"><p><strong>0:</strong> system expansion PTE type</p>
<p><strong>1:</strong> nonpaged pool expansion PTE type</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Size of memory request</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Total free system PTEs</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Total system PTEs</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

In almost all cases, the system is not actually out of PTEs. Rather, a driver has requested a large block of memory, but there is no contiguous block of sufficient size to satisfy this request.

Often video drivers will allocate large amounts of kernel memory that must succeed. Some backup programs do the same.

Resolution
----------

**A possible work-around:** Modify the registry to increase the total number of system PTEs. If this does not help, remove any recently-installed software, especially backup utilities or disk-intensive applications.

**Debugging the problem:** The following method can be used to debug bug check 0x3F.

First, get a stack trace, and use the [**!sysptes 3**](-sysptes.md) extension command.

Then set **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\TrackPtes** equal to DWORD 1, and reboot. This will cause the system to save stack traces.

This allows you to display more detailed information about the PTE owners. For example:

```dbgcmd
0: kd> !sysptes 4

0x2c47 System PTEs allocated to mapping locked pages

VA       MDL     PageCount  Caller/CallersCaller
f0e5db48 eb6ceef0        1 ntkrpamp!MmMapLockedPages+0x15/ntkrpamp!IopfCallDriver+0x35
f0c3fe48 eb634bf0        1 netbt!NbtTdiAssociateConnection+0x1f/netbt!DelayedNbtProcessConnect+0x17c
f0db38e8 eb65b880        1 mrxsmb!SmbMmAllocateSessionEntry+0x89/mrxsmb!SmbCepInitializeExchange+0xda
f8312568 eb6df880        1 rdbss!RxCreateFromNetRoot+0x3d7/rdbss!RxCreateFromNetRoot+0x93
f8363908 eb685880        1 mrxsmb!SmbMmAllocateSessionEntry+0x89/mrxsmb!SmbCepInitializeExchange+0xda
f0c54248 eb640880        1 rdbss!RxCreateFromNetRoot+0x3d7/rdbss!RxCreateFromNetRoot+0x93
f0ddf448 eb5f3160        1 mrxsmb!MrxSmbUnalignedDirEntryCopyTail+0x387/mrxsmb!MRxSmbCoreInformation+0x36
f150bc08 eb6367b0        1 mrxsmb!MrxSmbUnalignedDirEntryCopyTail+0x387/mrxsmb!MRxSmbCoreInformation+0x36
f1392308 eb6fba70        1 netbt!NbtTdiOpenAddress+0x1fb/netbt!DelayedNbtProcessConnect+0x17c
eb1bee64 edac5000      200 VIDEOPRT!pVideoPortGetDeviceBase+0x118/VIDEOPRT!VideoPortMapMemory+0x45
f139b5a8 edd4b000       12 rdbss!FsRtlCopyWrite2+0x34/rdbss!RxDriverEntry+0x149
eb41f400 ede92000       20 VIDEOPRT!pVideoPortGetDeviceBase+0x139/VIDEOPRT!VideoPortGetDeviceBase+0x1b
eb41f198 edf2a000       20 NDIS!NdisReadNetworkAddress+0x3a/NDIS!NdisFreeSharedMemory+0x58
eb41f1e4 eb110000       10 VIDEOPRT!pVideoPortGetDeviceBase+0x139/VIDEOPRT!VideoPortGetDeviceBase+0x1b
......
```

If the system runs out of PTEs again after the **TrackPtes** registry value has been set, [**bug check 0xD8**](bug-check-0xd8--driver-used-excessive-ptes.md) (DRIVER\_USED\_EXCESSIVE\_PTES) will be issued instead of 0x3F. The name of the driver causing this error will be displayed as well.

 

 




