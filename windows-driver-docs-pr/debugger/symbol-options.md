---
title: Symbol Options
description: Symbol Options
ms.assetid: 4a501ea3-431c-4c11-8826-154eb8799a64
keywords: ["symbols, setting symbol options", "symbols, SYMOPT_XXXX", "noisy symbol loading", "CV record"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbol Options


## <span id="ddk_setting_symbol_options_dbg"></span><span id="DDK_SETTING_SYMBOL_OPTIONS_DBG"></span>


A number of options are available to control how symbols are loaded and used. These options can be set in a variety of ways.

The following table lists these symbol options:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Option Name</th>
<th align="left">Default in debugger</th>
<th align="left">Default in DBH</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p><a href="#symopt-case-insensitive" data-raw-source="[SYMOPT_CASE_INSENSITIVE](#symopt-case-insensitive)">SYMOPT_CASE_INSENSITIVE</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p><a href="#symopt-undname" data-raw-source="[SYMOPT_UNDNAME](#symopt-undname)">SYMOPT_UNDNAME</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p><a href="#symopt-deferred-loads" data-raw-source="[SYMOPT_DEFERRED_LOADS](#symopt-deferred-loads)">SYMOPT_DEFERRED_LOADS</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p><a href="#symopt-no-cpp" data-raw-source="[SYMOPT_NO_CPP](#symopt-no-cpp)">SYMOPT_NO_CPP</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p><a href="#symopt-load-lines" data-raw-source="[SYMOPT_LOAD_LINES](#symopt-load-lines)">SYMOPT_LOAD_LINES</a></p></td>
<td align="left"><p>Off in KD and CDB</p>
<p>On in WinDbg</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20</p></td>
<td align="left"><p><a href="#symopt-omap-find-nearest" data-raw-source="[SYMOPT_OMAP_FIND_NEAREST](#symopt-omap-find-nearest)">SYMOPT_OMAP_FIND_NEAREST</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40</p></td>
<td align="left"><p><a href="#symopt-load-anything" data-raw-source="[SYMOPT_LOAD_ANYTHING](#symopt-load-anything)">SYMOPT_LOAD_ANYTHING</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x80</p></td>
<td align="left"><p><a href="#symopt-ignore-cvrec" data-raw-source="[SYMOPT_IGNORE_CVREC](#symopt-ignore-cvrec)">SYMOPT_IGNORE_CVREC</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x100</p></td>
<td align="left"><p><a href="#symopt-no-unqualified-loads" data-raw-source="[SYMOPT_NO_UNQUALIFIED_LOADS](#symopt-no-unqualified-loads)">SYMOPT_NO_UNQUALIFIED_LOADS</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x200</p></td>
<td align="left"><p><a href="#symopt-fail-critical-errors" data-raw-source="[SYMOPT_FAIL_CRITICAL_ERRORS](#symopt-fail-critical-errors)">SYMOPT_FAIL_CRITICAL_ERRORS</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x400</p></td>
<td align="left"><p><a href="#symopt-exact-symbols" data-raw-source="[SYMOPT_EXACT_SYMBOLS](#symopt-exact-symbols)">SYMOPT_EXACT_SYMBOLS</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x800</p></td>
<td align="left"><p><a href="#symopt-allow-absolute-symbols" data-raw-source="[SYMOPT_ALLOW_ABSOLUTE_SYMBOLS](#symopt-allow-absolute-symbols)">SYMOPT_ALLOW_ABSOLUTE_SYMBOLS</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1000</p></td>
<td align="left"><p><a href="#symopt-ignore-nt-sympath" data-raw-source="[SYMOPT_IGNORE_NT_SYMPATH](#symopt-ignore-nt-sympath)">SYMOPT_IGNORE_NT_SYMPATH</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2000</p></td>
<td align="left"><p>SYMOPT_INCLUDE_32BIT_MODULES</p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4000</p></td>
<td align="left"><p><a href="#symopt-publics-only" data-raw-source="[SYMOPT_PUBLICS_ONLY](#symopt-publics-only)">SYMOPT_PUBLICS_ONLY</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8000</p></td>
<td align="left"><p><a href="#symopt-no-publics" data-raw-source="[SYMOPT_NO_PUBLICS](#symopt-no-publics)">SYMOPT_NO_PUBLICS</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10000</p></td>
<td align="left"><p><a href="#symopt-auto-publics" data-raw-source="[SYMOPT_AUTO_PUBLICS](#symopt-auto-publics)">SYMOPT_AUTO_PUBLICS</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20000</p></td>
<td align="left"><p><a href="#symopt-no-image-search" data-raw-source="[SYMOPT_NO_IMAGE_SEARCH](#symopt-no-image-search)">SYMOPT_NO_IMAGE_SEARCH</a></p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40000</p></td>
<td align="left"><p><a href="#symopt-secure" data-raw-source="[SYMOPT_SECURE](#symopt-secure)">SYMOPT_SECURE</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x80000</p></td>
<td align="left"><p><a href="#symopt-no-prompts" data-raw-source="[SYMOPT_NO_PROMPTS](#symopt-no-prompts)">SYMOPT_NO_PROMPTS</a></p></td>
<td align="left"><p>On in KD and CDB</p>
<p>Off in WinDbg</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x80000000</p></td>
<td align="left"><p><a href="#symopt-debug" data-raw-source="[SYMOPT_DEBUG](#symopt-debug)">SYMOPT_DEBUG</a></p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Off</p></td>
</tr>
</tbody>
</table>

 

### <span id="changing-the-symbol-option-settings"></span><span id="CHANGING_THE_SYMBOL_OPTION_SETTINGS"></span>Changing the Symbol Option Settings

The [**.symopt (Set Symbol Options)**](-symopt--set-symbol-options-.md) command can be used to change or display the symbol option settings. In addition, a number of command-line parameters and commands are available to change these settings; these are listed in the individual SYMOPT\_*XXX* sections.

You can also control all the settings at once with the **-sflags**[command-line option](command-line-options.md). This option can be followed with a decimal number, or with a hexadecimal number prefixed by **0x**. It is recommended that you use hexadecimal, since the symbol flags are aligned properly that way. Be cautious in using this method, since it sets the entire bitfield and will override all the symbol handler defaults. For example, **-sflags 0x401** will not only turn on SYMOPT\_EXACT\_SYMBOLS and SYMOPT\_CASE\_INSENSITIVE, but will also turn off all the other options that normally are on by default!

The default value for the total flag bits is 0x30237 in WinDbg, 0xB0227 in CDB and KD, and 0x10C13 in [the DBH tool](dbh.md), when these programs are launched without any symbol-related command line options.

### <span id="symopt-case-insensitive"></span><span id="SYMOPT_CASE_INSENSITIVE"></span>SYMOPT\_CASE\_INSENSITIVE

This symbol option causes all searches for symbol names to be case-insensitive.

This option is on by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x1** or .symopt-0x1, respectively.

This option is on by default in DBH. Once DBH is running, it can be turned on or off by using symopt +1 or symopt -1, respectively.

### <span id="symopt-undname"></span><span id="SYMOPT_UNDNAME"></span>SYMOPT\_UNDNAME

This symbol option causes public symbol names to be undecorated when they are displayed, and causes searches for symbol names to ignore symbol decorations. Private symbol names are never decorated, regardless of whether this option is active. For information on symbol name decorations, see [Public and Private Symbols](public-and-private-symbols.md).

This option is on by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x2** or .symopt-0x2, respectively.

This option is on by default in DBH. It is turned off if the -d command-line option is used. Once DBH is running, it can be turned on or off by using symopt +2 or symopt -2, respectively.

### <span id="symopt-deferred-loads"></span><span id="SYMOPT_DEFERRED_LOADS"></span>SYMOPT\_DEFERRED\_LOADS

This symbol option is called *deferred symbol loading* or *lazy symbol loading*. When it is active, symbols are not actually loaded when the target modules are loaded. Instead, symbols are loaded by the debugger as they are needed. See [Deferred Symbol Loading](deferred-symbol-loading.md) for details.

This option is on by default in all debuggers. In CDB and KD, the -s command-line option will turn this option off. It can also be turned off in CDB by using the **LazyLoad** variable in the [tools.ini](configuring-tools-ini.md) file. Once the debugger is running, this option can be turned on or off by using **.symopt+0x4** or .symopt-0x4, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +4 or symopt -4, respectively.

### <span id="symopt-no-cpp"></span><span id="SYMOPT_NO_CPP"></span>SYMOPT\_NO\_CPP

This symbol option turns off C++ translation. When this symbol option is set, **::** is replaced by **\_\_** in all symbols.

This option is off by default in all debuggers. It can be activated by using the -snc command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x8** or .symopt-0x8, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +8 or symopt -8, respectively.

### <span id="symopt-load-lines"></span><span id="SYMOPT_LOAD_LINES"></span>SYMOPT\_LOAD\_LINES

This symbol option allows line number information to be read from source files. This option must be on for source debugging to work correctly.

In KD and CDB, this option is off by default; in WinDbg, this option is on by default. In CDB and KD, the -lines command-line option will turn this option on. Once the debugger is running, it can be turned on or off by using **.symopt+0x10** or .symopt-0x10, respectively. It can also be toggled on and off by using the [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command.

This option is on by default in DBH. Once DBH is running, it can be turned on or off by using symopt +10 or symopt -10, respectively.

### <span id="symopt-omap-find-nearest"></span><span id="SYMOPT_OMAP_FIND_NEAREST"></span>SYMOPT\_OMAP\_FIND\_NEAREST

When code has been optimized and there is no symbol at the expected location, this option causes the nearest symbol to be used instead.

This option is on by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x20** or .symopt-0x20, respectively.

This option is on by default in DBH. Once DBH is running, it can be turned on or off by using symopt +20 or symopt -20, respectively.

### <span id="symopt-load-anything"></span><span id="SYMOPT_LOAD_ANYTHING"></span>SYMOPT\_LOAD\_ANYTHING

This symbol option reduces the pickiness of the symbol handler when it is attempting to match symbols.

This option is off by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x40** or .symopt-0x40, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +40 or symopt -40, respectively.

### <span id="symopt-ignore-cvrec"></span><span id="SYMOPT_IGNORE_CVREC"></span>SYMOPT\_IGNORE\_CVREC

This symbol option causes the symbol handler to ignore the CV record in the loaded image header when searching for symbols.

This option is off by default in all debuggers. It can be activated by using the -sicv command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x80** or .symopt-0x80, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +80 or symopt -80, respectively.

### <span id="symopt-no-unqualified-loads"></span><span id="SYMOPT_NO_UNQUALIFIED_LOADS"></span>SYMOPT\_NO\_UNQUALIFIED\_LOADS

This symbol option disables the symbol handler's automatic loading of modules. When this option is set and the debugger attempts to match a symbol, it will only search modules which have already been loaded.

This option can be used as a defense against mistyping a symbol name. Normally, a mistyped symbol will cause the debugger to pause while it searches all unloaded symbol files. When this option is active, a mistyped symbol will not be found in the loaded modules, and then the search will terminate.

This option is off by default in all debuggers. It can be activated by using the -snul command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x100** or .symopt-0x100, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +100 or symopt -100, respectively.

### <span id="symopt-fail-critical-errors"></span><span id="SYMOPT_FAIL_CRITICAL_ERRORS"></span>SYMOPT\_FAIL\_CRITICAL\_ERRORS

This symbol option causes file access error dialog boxes to be suppressed.

If this option is off, file access errors, such as "drive not ready", encountered during symbol loading, will result in dialog boxes appearing. If this option is on, these boxes are suppressed and all access errors receive a "fail" response.

This option is on by default in all debuggers. It can be deactivated by using the -sdce command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x200** or .symopt-0x200, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +200 or symopt -200, respectively.

### <span id="symopt-exact-symbols"></span><span id="SYMOPT_EXACT_SYMBOLS"></span>SYMOPT\_EXACT\_SYMBOLS

This symbol option causes the debugger to perform a strict evaluation of all symbol files.

When this option is on, even the slightest discrepancy between the symbol files and the symbol handler's expectations will cause the symbols to be ignored.

This option is off by default in all debuggers. It can be activated by using the -ses command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x400** or .symopt-0x400, respectively.

The -failinc command-line option also turns on SYMOPT\_EXACT\_SYMBOLS. In addition, if you are debugging a user-mode minidump or a kernel-mode minidump, -failinc will prevent the debugger from loading any modules whose images can't be mapped.

This option is on by default in DBH. Once DBH is running, it can be turned on or off by using symopt +400 or symopt -400, respectively.

### <span id="symopt-allow-absolute-symbols"></span><span id="SYMOPT_ALLOW_ABSOLUTE_SYMBOLS"></span>SYMOPT\_ALLOW\_ABSOLUTE\_SYMBOLS

This symbol option allows DbgHelp to read symbols that are stored at an absolute address in memory. This option is not needed in the vast majority of cases.

This option is off by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x800** or .symopt-0x800, respectively.

This option is on by default in DBH. Once DBH is running, it can be turned on or off by using symopt +800 or symopt -800, respectively.

### <span id="symopt-ignore-nt-sympath"></span><span id="SYMOPT_IGNORE_NT_SYMPATH"></span>SYMOPT\_IGNORE\_NT\_SYMPATH

This symbol option causes the debugger to ignore the environment variable settings for the symbol path and the executable image path.

This option is off by default in all debuggers. It can be activated by using the -sins command-line option. However, it cannot be controlled by **.symopt** once the debugger is running, because the environment variables are only read at startup.

This option is off by default in DBH, and is ignored by DBH in all cases.

### <span id="symopt-publics-only"></span><span id="SYMOPT_PUBLICS_ONLY"></span>SYMOPT\_PUBLICS\_ONLY

This symbol option causes DbgHelp to ignore private symbol data, and search only the public symbol table for symbol information. This emulates the behavior of DbgHelp before support for these types was added. see [Public and Private Symbols](public-and-private-symbols.md).

This option is off by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x4000** or .symopt-0x4000, respectively.

This option is off by default in DBH. It is turned on if the -d command-line option is used. Once DBH is running, it can be turned on or off by using symopt +4000 or symopt -4000, respectively.

### <span id="symopt-no-publics"></span><span id="SYMOPT_NO_PUBLICS"></span>SYMOPT\_NO\_PUBLICS

This symbol option prevents DbgHelp from searching the public symbol table. This can make symbol enumeration and symbol searches much faster. If you are concerned solely with search speed, the SYMOPT\_AUTO\_PUBLICS option is generally preferable to this one. For information on the public symbol table, see [Public and Private Symbols](public-and-private-symbols.md).

This option is off by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x8000** or .symopt-0x8000, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +8000 or symopt -8000, respectively.

### <span id="symopt-auto-publics"></span><span id="SYMOPT-AUTO-PUBLICS"></span>SYMOPT\_AUTO\_PUBLICS

This symbol option causes DbgHelp to search the public symbol table in a .pdb file only as a last resort. If any matches are found when searching the private symbol data, the public symbols will not be searched. This improves symbol search speed.

This option is on by default in all debuggers. It can be deactivated by using the -sup command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x10000** or .symopt-0x10000, respectively.

This option is on by default in DBH. It is turned off if the -d command-line option is used. Once DBH is running, it can be turned on or off by using symopt +10000 or symopt -10000, respectively.

### <span id="symopt-no-image-search"></span><span id="SYMOPT-NO-IMAGE-SEARCH"></span>SYMOPT\_NO\_IMAGE\_SEARCH

This symbol option prevents DbgHelp from searching the disk for a copy of the image when symbols are loaded.

This option is on by default in all debuggers. Once the debugger is running, it can be turned on or off by using **.symopt+0x20000** or .symopt-0x20000, respectively.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +20000 or symopt -20000, respectively.

### <span id="symopt-secure"></span><span id="SYMOPT_SECURE"></span>SYMOPT\_SECURE

(Kernel mode only) This symbol option indicates whether [Secure Mode](secure-mode.md) is active.

Secure Mode is off by default in all debuggers. It can be activated by using the -secure command-line option. If the debugger is running, is in dormant mode, and has not established any Debugging Servers, Secure Mode can be turned on by using **.symopt+0x40000** or [**.secure (Activate Secure Mode)**](-secure--activate-secure-mode-.md).

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +40000 or symopt -40000, respectively.

Secure mode can never be turned off once it has been activated.

### <span id="symopt-no-prompts"></span><span id="SYMOPT_NO_PROMPTS"></span>SYMOPT\_NO\_PROMPTS

This symbol option suppresses authentication dialog boxes from the proxy server. This may result in SymSrv being unable to access a symbol store on the internet.

For details, see [Firewalls and Proxy Servers](firewalls-and-proxy-servers.md).

In KD and CDB, this option is on by default; in WinDbg, this option is off by default. Once the debugger is running, it can be turned on or off by using **.symopt+0x80000** or .symopt-0x80000, respectively, followed by the [**.reload (Reload Module)**](-reload--reload-module-.md) command. It can also be turned on and off by using the [**!sym prompts off**](-sym.md) and **!sym prompts** extension commands, followed by the **.reload (Reload Module)** command.

This option is off by default in DBH. Once DBH is running, it can be turned on or off by using symopt +80000 or symopt -80000, respectively.

### <span id="symopt-disable-fast-symbols"></span>

### <span id="symopt_disable_symsrv_timeout"></span>

### <span id="symopt-debug"></span>-SYMOPT\_DEBUG

This symbol option turns on *noisy symbol loading*. This instructs the debugger to display information about its search for symbols.

The name of each symbol file will be displayed as it is loaded. If the debugger cannot load a symbol file, it will display an error message. Error messages for .pdb files will be displayed in text. Error messages for .dbg files will be in the form of an error code; these codes are explained in the winerror.h file.

If an image file is loaded solely to recover symbolic header information, this will be displayed as well.

This option is off by default in all debuggers. It can be activated by using the -n command-line option. Once the debugger is running, it can be turned on or off by using **.symopt+0x80000000** or .symopt-0x80000000, respectively. It can also be turned on and off by using the [**!sym noisy**](-sym.md) and **!sym quiet** extension commands.

**Note**   This option should not be confused with noisy *source* loading -- that is controlled by the [**.srcnoisy (Noisy Source Loading)**](-srcnoisy--noisy-source-loading-.md) command.

 

This option is off by default in DBH. It can be activated by using the -n command-line option. Once DBH is running, it can be turned on or off by using symopt +80000000 or symopt -80000000, respectively. It can also be turned on and off by using the verbose on and verbose off commands.

 

 





