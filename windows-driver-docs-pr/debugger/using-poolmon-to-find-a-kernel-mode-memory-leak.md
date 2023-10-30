---
title: Use PoolMon to find a kernel-mode memory leak
description: Learn how to use PoolMon to find a kernel-mode memory leak by determining which pool tag is associated with the leak.
keywords: ["memory leak, kernel-mode, PoolMon", "PoolMon", "PoolMon, finding a memory leak"]
ms.date: 12/30/2022
---

# Use PoolMon to find a kernel-mode memory leak

If you suspect there's a kernel-mode memory leak, you can use the PoolMon tool to determine which pool tag is associated with the leak.

PoolMon (Poolmon.exe) monitors pool memory usage by pool tag name. This tool is included in the Windows Driver Kit (WDK). For more information, see [PoolMon](../devtest/poolmon.md).

## GFlags pool settings

Some GFlags settings such as Special Pool, will impact how memory pools are used. For more information, see [GFlags](gflags.md) and [Configuring Special Pool](configuring-special-pool.md).

## Use PoolMon

The PoolMon header displays the total paged and non-paged pool bytes. The columns show pool use for each pool tag. The display is updated automatically every few seconds. For example:

```dbgcmd
Memory: 16224K Avail: 4564K PageFlts: 31 InRam Krnl: 684K P: 680K
Commit: 24140K Limit: 24952K Peak: 24932K Pool N: 744K P: 2180K

## Tag   Type  Allocs       Frees        Diff    Bytes       Per Alloc


CM    Paged   1283  ( 0)  1002  ( 0)   281  1377312   ( 0)  4901
Strg  Paged  10385 ( 10)  6658  ( 4)  3727   317952 ( 512)    85
Fat   Paged   6662  ( 8)  4971  ( 6)  1691   174560 ( 128)   103
MmSt  Paged    614  ( 0)   441  ( 0)   173    83456   ( 0)   482 
```

PoolMon has command keys that sort the output according to various criteria. Select the letter associated with each command in order to resort the data. It takes a few seconds for each command to work.

The sort commands include:

| Command key | Operation |
|---|---|
| **P** | Limits the tags shown to non-paged pool bytes, paged pool bytes, or both. Repeatedly pressing **P** cycles through each of these options, in that order.|
| **B** | Sorts tags by maximum byte usage. |
| **M** | Sorts tags by maximum byte allocations. |
| **T** | Sorts tags alphabetically by tag name. |
| **E** | Causes the display to include the paged and non-paged totals across the bottom. |
| **A** | Sorts tags by allocation size. |
| **F** | Sorts tags by free operations. |
| **S** | Sorts tags by the difference between allocations and frees. |
| **Q** | Quits PoolMon. |

### Display driver names in PoolMon

You can use the PoolMon /g parameter to display the names of Windows components and commonly used drivers that assign each pool tag. If you find a problem in allocations with a particular tag, this feature helps you identify the offending component or driver.

The components and drivers are listed in the Mapped_Driver column, the right-most column in the display. The data for the Mapped_Driver column comes from pooltag.txt, a file installed with the WDK.

The following command shows the use of the /g parameter to add the Mapped_Driver column.

`poolmon /g "C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\triage\pooltag.txt"`

### Display specific pools

Use the /i parameter to show pool tags that start with a specific string, for example *Hid*.

`poolmon /iHid? /g "C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\triage\pooltag.txt"`

```dbgcmd
 Memory:33473120K Avail:20055132K  PageFlts:     5   InRam Krnl:10444K P:1843072K
 Commit:15035764K Limit:67027552K Peak:16677444K            Pool N:1023400K P:1955448K
 System pool information
 Tag  Type     Allocs            Frees            Diff       Bytes                 Per Alloc Mapped_Driver

 HidC Paged      1667 (   0)      1659 (   0)        8         896 (          0)         112 [hidclass.sys - HID Class d 
 HidC Nonp      17375 (   0)     17256 (   0)      119       19808 (          0)         166 [hidclass.sys - HID Class d 
 HidP Nonp       1014 (   0)       998 (   0)       16        6704 (          0)         419 [hidparse.sys - HID Parser]
```
### Use the PoolMon utility to find a memory leak

Here is one approach to find a memory leak with the PoolMon utility:

1. Start PoolMon.

2. If you've determined that the leak is occurring in a non-paged pool, select P once. If you've determined that it's occurring in a paged pool, select P twice. If you don't know, don't select P, so both kinds of pool are included.

3. Select B to sort the display by maximum byte use.

4. Start your test. Copy the output from the screen, for example by taking a screenshot and saving it.

5. Take a new screenshot every half hour. By comparing screenshots, determine which tag's bytes are increasing.

6. Stop your test and wait a few hours. Determine how much of the tag was freed up in this time.

Typically, after an application reaches a stable running state, it allocates memory and free memory at the same rate. If it allocates memory faster than it frees it, its memory use grows over time. This often indicates a memory leak.

## Address the leak

After you've determined which pool tag is associated with the leak, you might have all you need to know about the leak. If you need to determine which specific instance of the allocation routine is causing the leak, see [Using the kernel debugger to find kernel-mode memory leaks](using-the-kernel-debugger-to-find-a-kernel-mode-memory-leak.md).
