---
title: token
description: The token extension displays a formatted view of a security token object.
ms.assetid: 3df89255-5e8c-4a09-9fe9-6977b26f5631
keywords: ["token", "security token", "token Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- token
api_type:
- NA
ms.localizationpriority: medium
---

# !token


The **!token** extension displays a formatted view of a security token object.

Kernel-Mode Syntax:

```dbgcmd
!token [-n] [Address] 
!token -?
```

User-Mode Syntax:

```dbgcmd
!token [-n] [Handle] 
!token -?
```

## <span id="ddk__token_dbg"></span><span id="DDK__TOKEN_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
(Kernel mode only) Specifies the address of the token to be displayed. If this is 0 or omitted, the token for the active thread is displayed.

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
(User mode only) Specifies the handle of the token to be displayed. If this is 0 or omitted, the token associated with the target thread is displayed.

<span id="_______-n______"></span><span id="_______-N______"></span> **-n**   
(User mode only) Causes the display to include the friendly name. This includes the security identifier (SID) type, as well as the domain and user name for the SID. This option cannot be used when you are debugging LSASS.

<span id="_______-_______"></span> **-?**   
Displays help text for this extension.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

The **!token** command is available in kernel-mode and live user-mode debugging. It cannot be used on user-mode dump files.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about the kernel-mode TOKEN structure, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. For information about the user-mode TOKEN structure, see the Microsoft Windows SDK documentation.

Remarks
-------

The TOKEN structure is a security object type that represents an authenticated user process. Every process has an assigned token, which becomes the default token for each thread of that process. However, an individual thread can be assigned a token that overrides this default.

You can get the token address from the output of [**!process**](-process.md). To display a list of the individual fields of the TOKEN structure, use the **dt nt!\_TOKEN** command.

Here is an example:

```dbgcmd
kd> !process 81464da8 1
PROCESS 81464da8  SessionId: 0  Cid: 03bc    Peb: 7ffdf000  ParentCid: 0124
    DirBase: 0dec2000  ObjectTable: e1a31198  TableSize: 275.
    Image: MSMSGS.EXE
    VadRoot 81468cc0 Vads 170 Clone 0 Private 455. Modified 413. Locked 0.
    DeviceMap e1958438
    Token                             e1bed030
    ElapsedTime                       0:44:15.0142
    UserTime                          0:00:00.0290
    KernelTime                        0:00:00.0300
    QuotaPoolUsage[PagedPool]         49552
    QuotaPoolUsage[NonPagedPool]      10872
    Working Set Sizes (now,min,max)  (781, 50, 345) (3124KB, 200KB, 1380KB)
    PeakWorkingSetSize                1550
    VirtualSize                       57 Mb
    PeakVirtualSize                   57 Mb
    PageFaultCount                    2481
    MemoryPriority                    BACKGROUND
    BasePriority                      8
    CommitCharge                      2497
kd> !exts.token -n e1bed030
_TOKEN e1bed030
TS Session ID: 0
User: S-1-5-21-518066528-515770016-299552555-2981724 (User: MYDOMAIN\myuser)
Groups:
 00 S-1-5-21-518066528-515770016-299552555-513 (Group: MYDOMAIN\Domain Users)
    Attributes - Mandatory Default Enabled
 01 S-1-1-0 (Well Known Group: localhost\Everyone)
    Attributes - Mandatory Default Enabled
 02 S-1-5-32-544 (Alias: BUILTIN\Administrators)
    Attributes - Mandatory Default Enabled Owner
 03 S-1-5-32-545 (Alias: BUILTIN\Users)
    Attributes - Mandatory Default Enabled
 04 S-1-5-21-518066528-515770016-299552555-2999049 (Group: MYDOMAIN\AllUsers)
    Attributes - Mandatory Default Enabled
 05 S-1-5-21-518066528-515770016-299552555-2931095 (Group: MYDOMAIN\SomeGroup1)
    Attributes - Mandatory Default Enabled
 06 S-1-5-21-518066528-515770016-299552555-2931096 (Group: MYDOMAIN\SomeGroup2)
    Attributes - Mandatory Default Enabled
 07 S-1-5-21-518066528-515770016-299552555-3014318 (Group: MYDOMAIN\SomeGroup3)
    Attributes - Mandatory Default Enabled
 08 S-1-5-21-518066528-515770016-299552555-3053352 (Group: MYDOMAIN\Another Group)
    Attributes - Mandatory Default Enabled
 09 S-1-5-21-518066528-515770016-299552555-2966661 (Group: MYDOMAIN\TestGroup)
    Attributes - Mandatory Default Enabled
 10 S-1-5-21-2117033040-537160606-1609722162-17637 (Group: MYOTHERDOMAIN\someusers)
    Attributes - Mandatory Default Enabled
 11 S-1-5-21-518066528-515770016-299552555-3018354 (Group: MYDOMAIN\TestGroup2)
    Attributes - Mandatory Default Enabled
 12 S-1-5-21-518066528-515770016-299552555-3026602 (Group: MYDOMAIN\SomeGroup4)
    Attributes - Mandatory Default Enabled
 13 S-1-5-21-518066528-515770016-299552555-2926570 (Group: MYDOMAIN\YetAnotherGroup)
    Attributes - Mandatory Default Enabled
 14 S-1-5-21-661411660-2927047998-133698966-513 (Group: MYDOMAIN\Domain Users)
    Attributes - Mandatory Default Enabled
 15 S-1-5-21-518066528-515770016-299552555-2986081 (Alias: MYDOMAIN\an_alias)
    Attributes - Mandatory Default Enabled GroupResource
 16 S-1-5-21-518066528-515770016-299552555-3037986 (Alias: MYDOMAIN\AReallyLongGroupName1)
    Attributes - Mandatory Default Enabled GroupResource
 17 S-1-5-21-518066528-515770016-299552555-3038991 (Alias: MYDOMAIN\AReallyLongGroupName2)
    Attributes - Mandatory Default Enabled GroupResource
 18 S-1-5-21-518066528-515770016-299552555-3037999 (Alias: MYDOMAIN\AReallyLongGroupName3)
    Attributes - Mandatory Default Enabled GroupResource
 19 S-1-5-21-518066528-515770016-299552555-3038983 (Alias: MYDOMAIN\AReallyReallyLongGroupName)
    Attributes - Mandatory Default Enabled GroupResource
 20 S-1-5-5-0-71188 (no name mapped)
    Attributes - Mandatory Default Enabled LogonId
 21 S-1-2-0 (Well Known Group: localhost\LOCAL)
    Attributes - Mandatory Default Enabled
 22 S-1-5-4 (Well Known Group: NT AUTHORITY\INTERACTIVE)
    Attributes - Mandatory Default Enabled
 23 S-1-5-11 (Well Known Group: NT AUTHORITY\Authenticated Users)
    Attributes - Mandatory Default Enabled
Primary Group: S-1-5-21-518066528-515770016-299552555-513 (Group: MYDOMAIN\Domain Users)
Privs:
 00 0x000000017 SeChangeNotifyPrivilege           Attributes - Enabled Default
 01 0x000000008 SeSecurityPrivilege               Attributes -
 02 0x000000011 SeBackupPrivilege                 Attributes -
 03 0x000000012 SeRestorePrivilege                Attributes -
 04 0x00000000c SeSystemtimePrivilege             Attributes -
 05 0x000000013 SeShutdownPrivilege               Attributes -
 06 0x000000018 SeRemoteShutdownPrivilege         Attributes -
 07 0x000000009 SeTakeOwnershipPrivilege          Attributes -
 08 0x000000014 SeDebugPrivilege                  Attributes -
 09 0x000000016 SeSystemEnvironmentPrivilege      Attributes -
 10 0x00000000b SeSystemProfilePrivilege          Attributes -
 11 0x00000000d SeProfileSingleProcessPrivilege   Attributes -
 12 0x00000000e SeIncreaseBasePriorityPrivilege   Attributes -
 13 0x00000000a SeLoadDriverPrivilege             Attributes - Enabled
 14 0x00000000f SeCreatePagefilePrivilege         Attributes -
 15 0x000000005 SeIncreaseQuotaPrivilege          Attributes -
 16 0x000000019 SeUndockPrivilege                 Attributes - Enabled
 17 0x00000001c SeManageVolumePrivilege           Attributes -
Authentication ID:         (0,11691)
Impersonation Level:       Anonymous
TokenType:                 Primary
Source: User32             TokenFlags: 0x9 ( Token in use )
Token ID: 18296            ParentToken ID: 0
Modified ID:               (0, 18298)
RestrictedSidCount: 0      RestrictedSids: 00000000
```

 

 





