---
title: .kdfiles (Set Driver Replacement Map)
description: The .kdfiles command reads a file and uses its contents as the driver replacement map.
keywords: ["Set Driver Replacement Map (.kdfiles) command", "driver replacement map, Set Driver Replacement Map (.kdfiles) command", ".kdfiles (Set Driver Replacement Map) Windows Debugging"]
ms.date: 08/11/2020
topic_type:
- apiref
api_name:
- .kdfiles (Set Driver Replacement Map)
api_type:
- NA
ms.localizationpriority: medium
---

# .kdfiles (Set Driver Replacement Map)

The **.kdfiles** command reads a file and uses its contents as the driver replacement map.

```dbgcmd
.kdfiles MapFile
.kdfiles -m OldDriver NewDriver
.kdfiles -s SaveFile
.kdfiles -c
.kdfiles
```

## Parameters


<span id="_______MapFile______"></span><span id="_______mapfile______"></span><span id="_______MAPFILE______"></span> *MapFile*   
Specifies the driver replacement map file to read.

<span id="_______-m______"></span><span id="_______-M______"></span> **-m**   
Adds a driver replacement association to the current association list.

<span id="_______OldDriver______"></span><span id="_______olddriver______"></span><span id="_______OLDDRIVER______"></span> *OldDriver*   
Specifies the path and file name of the previous driver on the target computer. The syntax for *OldDriver* is the same as that of the first line after **map** in a driver replacement file. For more information about this syntax, see [Mapping Driver Files](mapping-driver-files.md).

<span id="_______NewDriver______"></span><span id="_______newdriver______"></span><span id="_______NEWDRIVER______"></span> *NewDriver*   
Specifies the path and file name of the new driver. This driver can be on the host computer or at some other network location. The syntax for *NewDriver* is the same as that of the second line after **map** in a driver replacement file. For more information about this syntax, see [Mapping Driver Files](mapping-driver-files.md).

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Creates a file and writes the current driver replacement associations to that file.

<span id="_______SaveFile______"></span><span id="_______savefile______"></span><span id="_______SAVEFILE______"></span> *SaveFile*   
Specifies the name of the file to create.

<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Deletes the existing driver replacement map. (This option does not alter the map file itself. Instead, this option clears the debugger's current map settings.)

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86-based processors</p></td>
</tr>
</tbody>
</table>

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about and examples of driver replacement and the replacement of other kernel-mode modules, a description of the format for driver replacement map files, and restrictions for using this feature, see [Mapping Driver Files](mapping-driver-files.md).

## Remarks

If you use the **.kdfiles** command without parameters, the debugger displays the path and name of the current driver replacement map file and the current set of replacement associations.

When you run this command, the specified *MapFile*file is read. If the file is not found or if it does not contain text in the proper format, the debugger displays a message that states, "Unable to load file associations".

If the specified file is in the correct driver replacement map file format, the debugger loads the file's contents and uses them as the driver replacement map. This map remains until you exit the debugger, or until you issue another **.kdfiles** command.

After the file has been read, the driver replacement map is not affected by subsequent changes to the file (unless these changes are followed by another **.kdfiles** command).

### User Mode File Replacement


User Mode File Replacement was added in version 2004 of Windows. This support enables the following user mode files to be replaced with .kdfiles.

- User mode DLLs (also including NTDLL and KnownDlls)
- User mode EXEs that are a main process image for CreateProcess

To use user mode .kdfiles support, you need to first enable kernel symbol loading using the `!gflag +ksl` debugger command or configure the ksl global flags in the registry. For more information about gflag, see [!gflag](-gflag.md).

The following examples illustrate common usage.

```dbgcmd
.kdfiles -m system32\userdll C:\myfiles\my_native_userdll.dll
.kdfiles -m system32\userdll \\server\share\my_native_userdll.dll
.kdfiles -m syswow64\ntdll.dll \\server\share\my_x86_wow64_ntdll.dll
.kdfiles -m system32\userbase.dll \\server\share\my_native_userbase.dll
```

User mode .kdfiles ignores any failures to match a file and does not display an error message when a failure occurs.

Be careful to appropriately qualify the .kdfiles paths for user mode .kdfiles. It is a bad idea to just match ntdll.dll (instead of system32\ntdll.dll) as otherwise the Wow64 NTDLL will get replaced with the native one. Similar situations can arise with other ambiguous substring matches.

After build 20172, the user mode .kdfiles mechanism will attempt to pull files from the debugger until one attempt fails; then, the file name that failed to be pulled will not be tried again for the boot session, without manual intervention from the debugger to modify the target system state. On earlier builds, the user mode .kdfiles mechanism will make one attempt (whether successful or not) to pull a given file name per boot session. These policies reduce the overhead of communicating with the debugger for files that are not in the kdfiles list, or that are inaccessible for replacement, such as due to sharing violations from processes that may have already loaded a given file. Because of this behavior, it is generally advisable to configure any files to pull in the .kdfiles list up front, before they would first be referenced.

Be aware of limitations with being unable to replace already in use disk files, etc. As many system DLLs are won’t be easily hot swappable after they have been loaded up initially, preset the gflags +ksl option and use .kdfiles to replace any user mode binaries right at boot.

For more information about enabling boot debugging, see [BCDEdit /bootdebug](../devtest/bcdedit--bootdebug.md).

The use of the high speed/low latency KD transport KDNET is recommended to minimize system performance impacts.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Supported in Windows XP and later versions of the Windows operating system.</p></td>
</tr>
</tbody>
</table>

 

