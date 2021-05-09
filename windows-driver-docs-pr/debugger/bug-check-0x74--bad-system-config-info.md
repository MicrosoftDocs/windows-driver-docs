---
title: Bug Check 0x74 BAD_SYSTEM_CONFIG_INFO
description: The BAD_SYSTEM_CONFIG_INFO bug check has a value of 0x00000074. This bug check indicates that there is an error in the registry.
keywords: ["Bug Check 0x74 BAD_SYSTEM_CONFIG_INFO", "BAD_SYSTEM_CONFIG_INFO"]
ms.date: 01/29/2021
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

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

## Cause

The BAD\_SYSTEM\_CONFIG\_INFO bug check occurs if the SYSTEM hive is corrupt. However, this corruption is unlikely, because the boot loader, checks a hive for corruption when it loads the hive.

This bug check can also occur if some critical registry keys and values are missing. The keys and values might be missing if a user manually edited the registry or if an application or service corrupted the registry.

Looking up the NT status value returned in parameter 4 can provide additional information, see [NTSTATUS Values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) for a listing. 

## Resolution

Check in the Windows system eventlog to see if there are any registry related error events. If there are see if the event lists a hive or specific key that the error occurred in.

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

```dbgcmd
BAD_SYSTEM_CONFIG_INFO (74)
Can indicate that the SYSTEM hive loaded by the osloader/NTLDR
was corrupt.  This is unlikely, since the osloader will check
a hive to make sure it isn't corrupt after loading it.
It can also indicate that some critical registry keys and values
are not present.  (i.e. somebody used regedt32 to delete something
that they shouldn't have)  Booting from LastKnownGood may fix
the problem, but if someone is persistent enough in mucking with
the registry they will need to reinstall or use the Emergency
Repair Disk.
Arguments:
Arg1: 0000000000000002, (reserved)
Arg2: ffffd481054b49f0, (reserved)
Arg3: 0000000000000004, (reserved)
Arg4: ffffffffc000014c, usually the NT status code.

```

Review all of the information returned by the !analyze to learn about the failure.

Use the [!error](-error.md) extension to display information about the NTSTATUS value in parameter 4.

```dbgcmd
2: kd> !ERROR ffffffffc000014c
Error code: (NTSTATUS) 0xc000014c (3221225804) - {The Registry Is Corrupt}  The structure of one of the files that contains Registry data is corrupt, or the image of the file in memory is corrupt, or the file could not be recovered because the alternate copy or log was absent or corrupt.
```

Use the [!reg](-reg.md) extenstion to display information about the registry, for example the hives present in the registry.

```dbgcmd
!reg hivelist

-------------------------------------------------------------------------------------------------------------------------------------------------------
|     HiveAddr     |Stable Length|    Stable Map    |Volatile Length|    Volatile Map    |MappedViews|PinnedViews|U(Cnt)|     BaseBlock     | FileName 
-------------------------------------------------------------------------------------------------------------------------------------------------------
| ffff95077ea24000 |       1000  | ffff95077ea24588 |          0    |  0000000000000000  |     0| ffff95077ea31000  | <NONAME>
| ffff95077ea3e000 |    12d3000  | ffff95077ea49000 |      21000    |  ffff95077ea3e800  |     0| ffff95077ea40000  | SYSTEM
| ffff95077ea8f000 |      53000  | ffff95077ea8f588 |       9000    |  ffff95077ea8f800  |     0| ffff95077ea91000  | <NONAME>
| ffff9507821c8000 |       7000  | ffff9507821c8588 |          0    |  0000000000000000  |     0| ffff9507821cc000  | kVolume2\EFI\Microsoft\Boot\BCD
| ffff95077f6ae000 |    685c000  | ffff95077f737000 |       6000    |  ffff95077f6ae800  |     0| ffff95077f6b6000  | emRoot\System32\Config\SOFTWARE
-------------------------------------------------------------------------------------------------------------------------------------------------------
```

Use the !reg openkeys command to see which registry keys were open.

```dbgcmd
2: kd> !reg openkeys

Hive: \REGISTRY\MACHINE\SYSTEM
===========================================================================================
Index 0: 	 00000000 kcb=ffffd805e303c728 cell=00000020 f=002c0100 \REGISTRY\MACHINE\SYSTEM
Index 1: 	 db67f96d kcb=ffffd805e416ed18 cell=00bd0b40 f=00200080 \REGISTRY\MACHINE\SYSTEM\WPA\8DEC0AF1-0341-4B93-85CD-72606C2DF94C-7P-374
Index 3: 	 db67ee93 kcb=ffffd805e30c5ab8 cell=00bc1550 f=00200080 \REGISTRY\MACHINE\SYSTEM\WPA\8DEC0AF1-0341-4B93-85CD-72606C2DF94C-7P-161
Index 4: 	 f9909d96 kcb=ffffd805e44bd268 cell=00bf8f50 f=00200000 \REGISTRY\MACHINE\SYSTEM\CONTROLSET001\CONTROL\POWER\PROFILE\EVENTS\{54533251-82BE-4824-96C1-47B60B740D00}\{8BC6262C-C026-411D-AE3B-7E2F70811A13}
Index 5: 	 e9dd6ce5 kcb=ffffd805e4180e48 cell=00812970 f=00200000 \REGISTRY\MACHINE\SYSTEM\DRIVERDATABASE

...

```

## Remarks

For general information on determining the cause of a blue screen, refer to [Blue Screen Data](blue-screen-data.md).

It is always a good idea to confirm that there is sufficient hard drive or SSD storage available to allow the OS to function normally.

The system file checker tool can look for corruptions in Windows. For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files-79aa86cb-ca52-166a-92a3-966e85d4094e).

Try booting into safe mode and then restart the OS normally. If the restart does not fix the problem, the registry damage is too extensive. Try the following steps.

- If you have a system restore point, try restoring to an earlier restore point.
- Reset your PC.
- Use installation media to restore or reset your PC.
- Use installation media to reinstall Windows.

For more information, see [Recovery options in Windows 10](https://support.microsoft.com/help/12415/windows-10-recovery-options#).

This support article discusses this bug check code: [Error 0x74: Bad_system_config_info](https://support.microsoft.com/help/4028653/windows-error-0x74-badsystemconfiginfo)
