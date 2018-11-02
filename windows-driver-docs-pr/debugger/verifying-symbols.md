---
title: Verifying Symbols
description: Verifying Symbols
ms.assetid: 61b4fcce-960b-4091-b575-4dd53c39cff2
keywords: ["symbols, verifying"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Verifying Symbols


## <span id="ddk_verifying_symbols_dbg"></span><span id="DDK_VERIFYING_SYMBOLS_DBG"></span>


Symbol problems can show up in a variety of ways. Perhaps a stack trace shows incorrect information or fails to identify the names of the functions in the stack. Or perhaps a debugger command failed to understand the name of a module, function, variable, structure, or data type.

If you suspect that the debugger is not loading symbols correctly, there are several steps you can take to investigate this problem.

First, use the [**lm (List Loaded Modules)**](lm--list-loaded-modules-.md) command to display the list of loaded modules with symbol information. The most useful form of this command is the following:

```dbgcmd
0:000> lml 
```

If you are using WinDbg, the [Debug | Modules](debug---modules.md) menu command will let you see this information as well.

Pay particular attention to any notes or abbreviations you may see in these displays. For an interpretation of these, see [Symbol Status Abbreviations](symbol-status-abbreviations.md).

If you don't see the proper symbol files, the first thing to do is to check the symbol path:

```dbgcmd
0:000> .sympath
Current Symbol Path is: d:\MyInstallation\i386\symbols\retail
```

If your symbol path is wrong, fix it. If you are using the kernel debugger make sure your local %WINDIR% is not on your symbol path.

Then reload symbols using the [**.reload (Reload Module)**](-reload--reload-module-.md) command:

```dbgcmd
0:000> .reload ModuleName 
```

If your symbol path is correct, you should activate *noisy mode* so you can see which symbol files **dbghelp** is loading. Then reload your module. See [Setting Symbol Options](symbol-options.md) for information about how to activate noisy mode.

Here is an example of a "noisy" reload of the Microsoft Windows symbols:

```dbgcmd
kd> !sym noisy
kd> .reload nt
 1: Kernel Version 2081 MP Checked
 2: Kernel base = 0x80400000 PsLoadedModuleList = 0x80506fa0
 3: DBGHELP: FindExecutableImageEx-> Looking for D:\MyInstallation\i386\ntkrnlmp.exe...mismatched timestamp
 4: DBGHELP: No image file available for ntkrnlmp.exe
 5: DBGHELP: FindDebugInfoFileEx-> Looking for
 6: d:\MyInstallation\i386\symbols\retail\symbols\exe\ntkrnlmp.dbg... no file
 7: DBGHELP: FindDebugInfoFileEx-> Looking for
 8: d:\MyInstallation\i386\symbols\retail\symbols\exe\ntkrnlmp.pdb... no file
 9: DBGHELP: FindDebugInfoFileEx-> Looking for d:\MyInstallation\i386\symbols\retail\exe\ntkrnlmp.dbg... OK
10: DBGHELP: LocatePDB-> Looking for d:\MyInstallation\i386\symbols\retail\exe\ntkrnlmp.pdb... OK
11: *** WARNING: symbols checksum and timestamp is wrong 0x0036a4ea 0x00361a83 for ntkrnlmp.exe
```

The symbol handler first looks for an image that matches the module it is trying to load (lines three and four). The image itself is not always necessary, but if an incorrect one is present, the symbol handler will often fail. These lines show that the debugger found an image at **D:\\MyInstallation\\i386\\ntkrnlmp.exe**, but the time-date stamp didn't match. Because the time-date stamp didn't match, the search continues. Next, the debugger looks for a .dbg file and a .pdb file that match the loaded image. These are on lines 6 through 10. Line 11 indicates that even though symbols were loaded, the time-date stamp for the image did not match (that is, the symbols were wrong).

If the symbol-search encountered a catastrophic failure, you would see a message of the form:

```dbgcmd
ImgHlpFindDebugInfo(00000000, module.dll, c:\MyDir;c:\SomeDir, 0823345, 0) failed
```

This could be caused by items such as file system failures, network errors, and corrupt .dbg files.

### <span id="diagnosing_symbol_loading_errors"></span><span id="DIAGNOSING_SYMBOL_LOADING_ERRORS"></span>Diagnosing Symbol Loading Errors

When in noisy mode, the debugger may print out error codes when it cannot load a symbol file. The error codes for .dbg files are listed in winerror.h. The .pdb error codes come from another source and the most common errors are printed in plain English text.

Some common error codes for .dbg files from winerror.h are:

<span id="0xB"></span><span id="0xb"></span><span id="0XB"></span>0xB  
ERROR\_BAD\_FORMAT

<span id="0x3"></span><span id="0X3"></span>0x3  
ERROR\_PATH\_NOT\_FOUND

<span id="0x35"></span><span id="0X35"></span>0x35  
ERROR\_BAD\_NETPATH

It's possible that the symbol file cannot be loaded because of a networking error. If you see ERROR\_BAD\_FORMAT or ERROR\_BAD\_NETPATH and you are loading symbols from another machine on the network, try copying the symbol file to your host computer and put its path in your symbol path. Then try to reload the symbols.

### <span id="verifying_your_search_path_and_symbols"></span><span id="VERIFYING_YOUR_SEARCH_PATH_AND_SYMBOLS"></span>Verifying Your Search Path and Symbols

Let "c:\\MyDir;c:\\SomeDir" represent your symbol path. Where should you look for debug information?

In cases where the binary has been stripped of debug information, such as the free builds of Windows, first look for a .dbg file in the following locations:

```dbgcmd
c:\MyDir\symbols\exe\ntoskrnl.dbg
c:\SomeDir\symbols\exe\ntoskrnl.dbg
c:\MyDir\exe\ntoskrnl.dbg
c:\SomeDir\exe\ntoskrnl.dbg
c:\MyDir\ntoskrnl.dbg
c:\SomeDir\ntoskrnl.dbg
current-working-directory\ntoskrnl.dbg
```

Next, look for a .pdb file in the following locations:

```dbgcmd
c:\MyDir\symbols\exe\ntoskrnl.pdb
c:\MyDir\exe\ntoskrnl.pdb
c:\MyDir\ntoskrnl.pdb
c:\SomeDir\symbols\exe\ntoskrnl.pdb
c:\SomeDir\exe\ntoskrnl.pdb
c:\SomeDir\ntoskrnl.pdb
current-working-directory\ntoskrnl.pdb
```

Note that in the search for the .dbg file, the debugger interleaves searching through the MyDir and SomeDir directories, but in the .pdb search it does not.

Windows XP and later versions of Windows do not use any .dbg symbol files. See [Symbols and Symbol Files](symbols-and-symbol-files.md) for details.

### <span id="mismatched_builds"></span><span id="MISMATCHED_BUILDS"></span>Mismatched Builds

One of the most common problems in debugging failures on a machine that is often updated is mismatched symbols from different builds. Three common causes of this problem are: pointing at symbols for the wrong build, using a privately built binary without the corresponding symbols, and using the uniprocessor hardware abstraction level (HAL) and kernel symbols on a multiprocessor machine. The first two are simply a matter of matching your binaries and symbols; the third can be corrected by renaming your hal\*.dbg and ntkrnlmp.dbg to hal.dbg and ntoskrnl.dbg.

To find out what build of Windows is installed on the target computer, use the [**vertarget (Show Target Computer Version)**](vertarget--show-target-computer-version-.md) command:

```dbgcmd
kd> vertarget 
Windows XP Kernel Version 2505 UP Free x86 compatible
Built by: 2505.main.010626-1514
Kernel base = 0x804d0000 PsLoadedModuleList = 0x80548748
Debug session time: Mon Jul 02 14:41:11 2001
System Uptime: 0 days 0:04:53 
```

### <span id="testing_the_symbols"></span><span id="TESTING_THE_SYMBOLS"></span>Testing the Symbols

Testing the symbols is more difficult. It involves verifying a stack trace on the debugger and seeing if the debug output is correct. Here's one example to try:

```dbgcmd
kd> u videoprt!videoportfindadapter2
Loading symbols for 0xf2860000     videoprt.sys ->   videoprt.sys

VIDEOPRT!VideoPortFindAdapter2:
f2856f42 55               push    ebp
f2856f43 8bec             mov     ebp,esp
f2856f45 81ecb8010000     sub     esp,0x1b8
f2856f4b 8b4518           mov     eax,[ebp+0x18]
f2856f4e 53               push    ebx
f2856f4f 8365f400         and     dword ptr [ebp-0xc],0x
f2856f53 8065ff00         and     byte ptr [ebp-0x1],0x0
f2856f57 56               push    esi
```

The **u** command unassembles the videoportfindadapter string in videoprt.sys. The symbols are correct on the debugger because common stack commands like **push** and **mov** show up on the stack. Most functions begin with an add, sub, or push operation using either the base pointer (ebp) or the stack pointer (esp).

It's usually obvious when the symbols aren't working correctly. Glintmp.sys doesn't have symbols in this example because a function isn't listed next to **Glintmp**:

```dbgcmd
kd> kb
Loading symbols for 0xf28d0000     videoprt.sys ->   videoprt.sys
Loading symbols for 0xf9cdd000      glintmp.sys ->   glintmp.sys
*** ERROR: Symbols could not be loaded for glintmp.sys
ChildEBP RetAddr  Args to Child
f29bf1b0 8045b5fa 00000001 0000a100 00000030 ntoskrnl!RtlpBreakWithStatusInstruction
f29bf1b0 8044904e 00000001 0000a100 00000030 ntoskrnl!KeUpdateSystemTime+0x13e
f29bf234 f28d1955 f9b7d000 ffafb2dc f9b7d000 ntoskrnl!READ_REGISTER_ULONG+0x6
f29bf248 f9cde411 f9b7d000 f29bf2b0 f9ba0060 VIDEOPRT!VideoPortReadRegisterUlong+0x27
00000002 00000000 00000000 00000000 00000000 glintMP+0x1411 [No function listed.] 
```

The wrong build symbols were loaded for this stack trace. Notice how there are no functions listed for the first two calls. This stack trace looks like a problem with win32k.sys drawing rectangles:

```dbgcmd
1: kd> 
1: kd> kb                      [Local        9:50 AM]
Loading symbols for 0xf22b0000       agpcpq.sys ->   agpcpq.sys
*** WARNING: symbols checksum is wrong 0x0000735a 0x00000000 for agpcpq.sys
*** ERROR: Symbols could not be loaded for agpcpq.sys
Loading symbols for 0xa0000000       win32k.sys ->   win32k.sys
*** WARNING: symbols checksum is wrong 0x00191a41 0x001995a9 for win32k.sys
ChildEBP RetAddr  Args to Child
be682b18 f22b372b 82707128 f21c1ffc 826a70f8 agpCPQ+0x125b [No function listed.]
be682b4c a0140dd4 826a72f0 e11410a8 a0139605 agpCPQ+0x372b [No function listed.]
be682b80 a00f5646 e1145100 e1cee560 e1cee560 win32k!vPatCpyRect1_6x6+0x20b
00000001 00000000 00000000 00000000 00000000 win32k!RemoteRedrawRectangle+0x32 
```

Here's the correct stack trace. The problem is really with AGP440.sys. The first item appearing on a stack trace is usually at fault. Notice that the win32k.sys rectangle error is gone:

```dbgcmd
1: kd> kb                      [Local        9:49 AM]
ChildEBP RetAddr  Args to Child
be682b18 f22b372b 82707128 f21c1ffc 826a70f8 agpCPQ!AgpReleaseMemory+0x88
be682b30 f20a385c 82703638 e183ec68 00000000 agpCPQ!AgpInterfaceReleaseMemory+0x8b
be682b4c a0140dd4 826a72f0 e11410a8 a0139605 VIDEOPRT!AgpReleasePhysical+0x44
be682b58 a0139605 e1cee560 e11410a8 a00e5f0a win32k!OsAGPFree+0x14
be682b64 a00e5f0a e1cee560 e11410a8 e1cee560 win32k!AGPFree+0xd
be682b80 a00f5646 e1145100 e1cee560 e1cee560 win32k!HeapVidMemFini+0x49
be682b9c a00f5c20 e1cee008 e1cee008 be682c0c win32k!vDdDisableDriver+0x3a
be682bac a00da510 e1cee008 00000000 be682c0c win32k!vDdDisableDirectDraw+0x2d
be682bc4 a00da787 00000000 e1843df8 e1843de8 win32k!PDEVOBJ__vDisableSurface+0x27
be682bec a00d59fb 00000000 e1843de8 00000000 win32k!PDEVOBJ__vUnreferencePdev+0x204
be682c04 a00d7421 e1cee008 82566a98 00000001 win32k!DrvDestroyMDEV+0x30
be682ce0 a00a9e7f e1843e10 e184a008 00000000 win32k!DrvChangeDisplaySettings+0x8b3
be682d20 a008b543 00000000 00000000 00000000 win32k!xxxUserChangeDisplaySettings+0x106
be682d48 8045d119 00000000 00000000 00000000 win32k!NtUserChangeDisplaySettings+0x48
be682d48 77e63660 00000000 00000000 00000000 ntkrnlmp!KiSystemService+0xc9 
```

### <span id="useful_commands_and_extensions"></span><span id="USEFUL_COMMANDS_AND_EXTENSIONS"></span>Useful Commands and Extensions

The following commands and extensions may be useful in tracking down symbol problems:

<span id="lm__List_Loaded_Modules_"></span><span id="lm__list_loaded_modules_"></span><span id="LM__LIST_LOADED_MODULES_"></span>[**lm (List Loaded Modules)**](lm--list-loaded-modules-.md)  
Lists all modules and gives the loading status of all symbols in these modules.

<span id="_dh_image-header-base"></span><span id="_DH_IMAGE-HEADER-BASE"></span>[**!dh image-header-base**](-dh.md)  
Displays header information for a loaded image beginning at *image-header-base*.

<span id=".RELOAD__N"></span>[**.reload /n**](-reload--reload-module-.md)  
Reloads all kernel symbols.

<span id=".reload__image-name_"></span><span id=".RELOAD__IMAGE-NAME_"></span>[**.reload \[image-name\]**](-reload--reload-module-.md)  
(CDB or WinDbg only) Reloads symbols for the image *image-name*. If no *image-name* is specified, reloads symbols for all images. (It is necessary to reload symbols after the symbol path has been changed.)

<span id="_sym_noisy"></span><span id="_SYM_NOISY"></span>[**!sym noisy**](-sym.md)  
Turns on verbose mode for symbol loads. This can be used to get information about the module loads. See [Setting Symbol Options](symbol-options.md) for details.

<span id=".sympath__new-symbol-path_"></span><span id=".SYMPATH__NEW-SYMBOL-PATH_"></span>[**.sympath \[new-symbol-path\]**](-sympath--set-symbol-path-.md)  
Sets a new symbol path, or displays the current symbol path. See [Symbol Path](symbol-path.md) for details.

If the kernel symbols are correct, but you aren't getting a complete stack, the following commands may also be useful:

<span id="X___"></span><span id="x___"></span>[**X \*!**](x--examine-symbols-.md)  
This will list the modules which currently have symbols loaded. This is useful if the kernel symbols are correct.

<span id=".RELOAD__USER"></span>[**.reload /user**](-reload--reload-module-.md)  
This will attempt to reload all user-mode symbols. This is needed while performing kernel debugging if symbols were loaded while one process was running, and a break later occurred in another process. In this case, the user-mode symbols from the new process will not be loaded unless this command is executed.

<span id="X_wdmaud__start_"></span><span id="x_wdmaud__start_"></span><span id="X_WDMAUD__START_"></span>[**X wdmaud!\*start\\***](x--examine-symbols-.md)  
This will list only the symbols in the **wdmaud** module whose names contain the "start" string. This has the advantage that it forces the reloading of all the symbols in **wdmaud**, but only displays those with "start" in them. (This means a shorter listing, but since there are always some symbols with "start" in them, there will be some verification that the load has taken place.)

One other useful technique for verifying symbols is unassembling code. Most functions begin with an add, sub, or push operation using either the base pointer (**ebp**) or the stack pointer (**esp** or **sp**). Try unassembling ([**U Function**](u--unassemble-.md)) some of the functions on the stack (from offset zero) to verify the symbols.

### <span id="network_and_port_problems"></span><span id="NETWORK_AND_PORT_PROBLEMS"></span>Network and Port Problems

Problems will occur with the symbol files and while connecting to the debugger. Here are a few things to keep in mind if you encounter problems:

-   Determine which COM port the debug cable is connected to on the test system.

-   Check the boot.ini settings of the test system. Look for the **/debug** switch and check the baud rate and COM port settings.

-   Network problems can interfere with debugging if the symbols files are accessed through the network.

-   .dll and .sys files with the same name (for example − mga64.sys and mga64.dll) will confuse the debugger if they aren't separated into the proper directories of the symbol tree.

-   The kernel debugger doesn't always like replacing the build symbol files with private symbol files. Double check the symbol path and do a **.reload***FileName* on the misbehaving symbol. The [**!dlls**](-dlls.md) command is sometimes useful.

### <span id="questions_and_misconceptions"></span><span id="QUESTIONS_AND_MISCONCEPTIONS"></span>Questions and Misconceptions

**Q:** I've successfully loaded symbols, but the stack seems to be wrong. Is the debugger broken?

**A:** Not necessarily. The most likely cause of your problem is that you've got incorrect symbols. Go through the steps outlined in this section to determine whether you've loaded valid symbols or not. Do not assume that because some things work you have valid symbols. For example, you very well may be able to execute **dd nt!ntbuildnumber** or **u nt!KeInitializeProcess** with incorrect symbols. Verify that they are correct using the procedures outlined above.

**Q:** Will the debugger still work with incorrect symbols?

**A:** Yes and no. Often you can get away with symbols that don't strictly match. For example, symbols from a previous Windows build will often work in certain cases, but there is no rule as to when this will work and when it will not.

**Q:** I'm stopped in the kernel debugger and I want to view symbols for my user-mode process. Can I do it?

**A:** Mostly. The support for this scenario is poor because the kernel debugger doesn't keep enough information around to track the module loads for each process, but there's a reasonable workaround. To load symbols for a user-mode module, execute a **.reload -user** command. This will load the user-mode modules for the current context.

**Q:** What does the following message mean?

`*** WARNING: symbols checksum and timestamp is wrong 0x0036d6bf 0x0036ab55 for ntkrnlmp.exe`

**A:** It means your symbols for ntkrnlmp.exe are wrong.

 

 





