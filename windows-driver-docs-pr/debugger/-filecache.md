---
title: filecache
description: The filecache extension displays information regarding the system file cache memory and PTE use.
ms.assetid: 38dbff14-5144-455c-a9b8-1ac6292f4200
keywords: ["file cache", "filecache Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- filecache
api_type:
- NA
ms.localizationpriority: medium
---

# !filecache


The **!filecache** extension displays information regarding the system file cache memory and PTE use.

```dbgcmd
!filecache [Flags]
```

## <span id="ddk__filelock_dbg"></span><span id="DDK__FILELOCK_DBG"></span>Parameters


<span id="_______Flags"></span><span id="_______flags"></span><span id="_______FLAGS"></span> *Flags*  
Optional. Default value is 0x0. Set *Flags* to 0x1 to sort the output by shared cache map. This way you can locate all the system cache views for a given control area.

## <span id="ddk__filecache_dbg"></span><span id="DDK__FILECACHE_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about file system drivers, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Each line of this extension's output represents a virtual address control block (VACB). When named files are mapped into the VACB, the names of these files are displayed. If "no name for file" is specified, this means that this VACB is being used to cache metadata.

Here is an example of the output from this extension from a Windows XP system:

```dbgcmd
kd> !filecache
***** Dump file cache******
  Reading and sorting VACBs ...
  Removed 1811 nonactive VACBs, processing 235 active VACBs ...
File Cache Information
  Current size 28256 kb
  Peak size    30624 kb
  235 Control Areas
Skipping view @ c1040000 - no VACB, but PTE is valid!
  Loading file cache database (100% of 131072 PTEs)
  SkippedPageTableReads = 44
  File cache has 4056 valid pages
 

  Usage Summary (in Kb):
Control Valid Standby/Dirty Shared Locked Name
817da668     4      0     0     0  $MftMirr
8177ae68   304    920     0     0  $LogFile
81776160   188      0     0     0  $BitMap
817cf370     4      0     0     0  $Mft
81776a00     8      0     0     0  $Directory
817cfdd0     4      0     0     0  $Directory
81776740    36      0     0     0    No Name for File
817cf7c8    20      0     0     0  $Directory
817cfb98   304      0     0     0  $Directory
8177be40    16      0     0     0  $Directory
817dadc0  2128     68     0     0  $Mft
817cf008     4      0     0     0  $Directory
817d0258     8      4     0     0  $Directory
817763f8     4      0     0     0  $Directory
...
8173f058     4      0     0     0  $Directory
8173e628    32      0     0     0  $Directory
8173e4c8    32      0     0     0  $Directory
8173da38     4      0     0     0  $Directory
817761f8     4      0     0     0  $Directory
81740530    32      0     0     0  $Directory
8173d518     4      0     0     0  $Directory
817d9560     8      0     0     0  $Directory
8173f868     4      0     0     0  $Directory
8173fc00     4      0     0     0  $Directory
81737278     4      0     0     0  $MftMirr
81737c88    44      0     0     0  $LogFile
81735fa0    48      0     0     0  $Mft
81737e88   188      0     0     0  $BitMap
817380b0     4      0     0     0  $Mft
817399e0     4      0     0     0  $Directory
817382b8     4      0     0     0  $Directory
817388d8    12      0     0     0    No Name for File
81735500     8      0     0     0  $Directory
81718e38   232      0     0     0  default
81735d40    48     20     0     0  SECURITY
81723008  8632      0     0     0  software
816da3a0    24     44     0     0  SAM
8173dfa0     4      0     0     0  $Directory
...
8173ba90     4      0     0     0  $Directory
8170ee30     4     36     4     0  AppEvent.Evt
816223f8     4      0     0     0  $Directory
8170ec28     8     28     4     0  SecEvent.Evt
816220a8     4      0     0     0  $Directory
8170ea20     4     32     4     0  SysEvent.Evt
8170d188   232      0     0     0  NTUSER.DAT
81709f10     8      0     0     0  UsrClass.dat
81708918   232      0     0     0  NTUSER.DAT
81708748     8      0     0     0  UsrClass.dat
816c58f8    12      0     0     0  change.log
815c3880     4      0     0     0  $Directory
81706aa8     4      0     0     0  SchedLgU.Txt
815ba2d8     4      0     0     0  $Directory
815aa5f8     8      0     0     0  $Directory
8166d728    44      0     0     0  Netlogon.log
81701120     8     16     4     0  es.dll
816ff0a8     4      8     4     0  stdole2.tlb
8159a358     4      0     0     0  $Directory
8159da70     4      0     0     0  $Directory
8159c158     4      0     0     0  $Directory
815cb9b0     4      0     0     0  00000001
81779b20     4      0     0     0  $Directory
8159ac20     4      0     0     0  $Directory
815683f8     4      0     0     0  $Directory
81566978   580      0     0     0  NTUSER.DAT
81568460     4      0     0     0  $Directory
815675d8    68      0     0     0  UsrClass.dat
81567640     4      0     0     0  $Directory
...
81515878     4      0     0     0  $Directory
81516870     8      0     0     0  $Directory
8150df60     4      0     0     0  $Directory
...
816e5300     4      0     0     0  $Directory
8152afa0    16    212     0     0  msmsgs.exe
8153bbd8     4     32     0     0  stdole32.tlb
8172f950   488    392     0     0  OBJECTS.DATA
8173e9c0     4      0     0     0  $Directory
814f4538     4      0     0     0  $Directory
81650790   344     48     0     0  INDEX.BTR
814f55f8     4      0     0     0  $Directory
...
814caef8     4      0     0     0  $Directory
8171cd90  1392     36     0     0  system
815f07f0     4      0     0     0  $Directory
814a2298     4      0     0     0  $Directory
81541538     4      0     0     0  $Directory
81585288    28      0     0     0  $Directory
8173f708     4      0     0     0  $Directory
...
8158cf10     4      0     0     0  $Directory
```

 

 





