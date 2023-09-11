---
title: lm (List Loaded Modules)
description: The lm command displays the specified loaded modules. The output includes the status and the path of the module.
keywords: ["lm (List Loaded Modules) Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- lm (List Loaded Modules)
api_type:
- NA
---

# lm (List Loaded Modules)


The **lm** command displays the specified loaded modules. The output includes the status and the path of the module.

```dbgcmd
lm Options [a Address] [m Pattern | M Pattern]
```

## Parameters

*Options*

Any combination of the following options:

D  

Displays output using [Debugger Markup Language](debugger-markup-language-commands.md).

o  

Displays only loaded modules.

l  

Displays only modules whose symbol information has been loaded.

v  

Causes the display to be verbose. The display includes the symbol file name, the image file name, checksum information, version information, date stamps, time stamps, and information about whether the module is managed code (CLR). This information is not displayed if the relevant headers are missing or paged out.

u  

(Kernel mode only) Displays only user-mode symbol information.

k  

(Kernel mode only) Displays only kernel-mode symbol information.

e  

Displays only modules that have a symbol problem. These symbols include modules that have no symbols and modules whose symbol status is C, T, \#, M, or Export. For more information about these notations, see [Symbol Status Abbreviations](symbol-status-abbreviations.md).

c  

Displays checksum data.

1m  

Reduces the output so that nothing is included except the names of the modules. This option is useful if you are using the [**.foreach**](-foreach.md) token to pipe the command output into another command's input.

sm  

Sorts the display by module name instead of by the start address.

In addition, you can include only one of the following options. If you do not include any of these options, the display includes the symbol file name.

i  

Displays the image file name.

f  
Displays the full image path. (This path always matches the path that is displayed in the initial load notification, unless you issued a [**.reload -s**](-reload--reload-module-.md) command.) When you use f, symbol type information is not displayed.

n  

Displays the image name. When you use n, symbol type information is not displayed.

p  
Displays the mapped image name. When you use p, symbol type information is not displayed.

t  

Displays the file time stamps. When you use t, symbol type information is not displayed.

a *Address*

Specifies an address that is contained in this module. Only the module that contains this address is displayed. If Address contains an expression, it must be enclosed in parentheses.

m *Pattern*

Specifies a pattern that the module name must match. Pattern can contain a variety of wildcard characters and specifiers. For more information about the syntax of this information, see [String Wildcard Syntax](string-wildcard-syntax.md).

In most cases, the module name is the file name without the file name extension. For example, if you want to display information about the Flpydisk.sys driver, use the lm mflpydisk command, not lm mflpydisk.sys. In some cases, the module name differs significantly from the file name.

M *Pattern*

Specifies a pattern that the image path must match. Pattern can contain a variety of wildcard characters and specifiers. For more information about the syntax of this information, see [String Wildcard Syntax](string-wildcard-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode, kernel mode|
|Targets|Live, crash dump|
|Platforms|All|

## Remarks

The **lm** command lists all of the modules and the status of symbols for each module.

Windows maintains an unloaded module list for user-mode processes. When you are debugging a user-mode process or dump file, the **lm** command also shows these unloaded modules.

The modules displayed depends on how you are debugging, for example user or kernel mode, and the specific context you are looking at. For more information about the process context and other context settings, see [Changing Contexts](changing-contexts.md) and [Controlling Processes and Threads](controlling-processes-and-threads.md).

This command shows several columns or fields, each with a different title. Some of these titles have specific meanings:

- *module name* is typically the file name without the file name extension. In some cases, the module name differs significantly from the file name.

- The symbol type immediately follows the module name. This column is not labeled. For more information about the various status values, see [Symbol Status Abbreviations](symbol-status-abbreviations.md). If you have loaded symbols, the symbol file name follows this column.

- The first address in the module is shown as start. The first address after the end of the module is shown as end. For example, if start is "faab4000" and end is "faab8000", the module extends from 0xFAAB4000 to 0xFAAB7FFF, inclusive.

- **lmv** only: The image path column shows the name of the executable file, including the file name extension. Typically, the full path is included in user mode but not in kernel mode.

- **lmv** only: The loaded symbol image file value is the same as the image name, unless Microsoft CodeView symbols are present.

- **lmv** only: The mapped memory image file value is typically not used. If the debugger is mapping an image file (for example, during minidump debugging), this value is the name of the mapped image.

The following code example shows the **lm** command using the m and s\* options, so only modules that begin with "s" are displayed.

```dbgcmd
kd> lm m s*
start    end        module name
f9f73000 f9f7fd80   sysaudio     (deferred)                 
fa04b000 fa09b400   srv          (deferred)                 
faab7000 faac8500   sr           (deferred)                 
facac000 facbae00   serial       (deferred)                 
fb008000 fb00ba80   serenum      e:\mysymbols\SereEnum.pdb\.......
fb24f000 fb250000   swenum       (deferred)                 

Unloaded modules:
f9f53000 f9f61000   swmidi.sys
fb0ae000 fb0b0000   splitter.sys
fb040000 fb043000   Sfloppy.SYS
```

## Examples

The following two examples show the **lm** command once without any options and once with the sm option. Compare the sort order in the two examples.

Example 1:

```dbgcmd
0:000> lm
start    end        module name
01000000 0100d000   stst       (deferred)
77c10000 77c68000   msvcrt     (deferred)
77dd0000 77e6b000   ADVAPI32   (deferred)
77e70000 77f01000   RPCRT4     (deferred)
7c800000 7c8f4000   kernel32   (deferred)
7c900000 7c9b0000   ntdll      (private pdb symbols) c:\db20sym\ntdll.pdb
```

Example 2:

```dbgcmd
0:000> lm sm
start    end        module name
77dd0000 77e6b000   ADVAPI32   (deferred)
7c800000 7c8f4000   kernel32   (deferred)
77c10000 77c68000   msvcrt     (deferred)
7c900000 7c9b0000   ntdll      (private pdb symbols)  c:\db20sym\ntdll.pdb
77e70000 77f01000   RPCRT4     (deferred)
01000000 0100d000   stst       (deferred)
```

## See also

- [Changing Contexts](changing-contexts.md)
- [Controlling Processes and Threads](controlling-processes-and-threads.md).
- [Standard debugging techniques](standard-debugging-techniques.md)
- [Get started with Windows Debugging](getting-started-with-windows-debugging.md)
