---
title: Using DBH
description: Using DBH
ms.assetid: c544013d-e925-40bf-b76d-bf9cefb9fd6d
keywords: ["DBH, using"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using DBH


DBH is a command-line tool that exposes many of the functions in the DbgHelp API (dbghelp.dll). It can display information about the contents of a symbol file, display specific details of the symbols in the file, and search through the file for symbols matching various criteria.

The functionality provided by DBH is similar to that provided within WinDbg, KD, and CDB by commands such as [**x (Examine Symbols)**](x--examine-symbols-.md).

### <span id="running_dbh_in_interactive_mode"></span><span id="RUNNING_DBH_IN_INTERACTIVE_MODE"></span>Running DBH in Interactive Mode

You start DBH with a simple command line, on which you specify the target module whose symbols you wish to investigate. A target module can be an EXE program or a PDB symbol file. You can also specify a process ID (PID) to investigate. See [**DBH Command-Line Options**](dbh-command-line-options.md) for the full syntax.

When DBH starts, it loads the symbols for the specified module, and then presents you with a prompt at which you can type a variety of commands. See [DBH Commands](dbh-commands.md) for a list of available commands.

For example, the following sequence starts DBH by specifying the target process with process ID 4672, then executes the **enum** command at the DBH prompt to display symbols matching a specific pattern, and then executes the **q** command to quit DBH:

```
C:\> dbh -p:4672 
            400000 : TimeTest
          77820000 : ntdll
          77740000 : kernel32

pid:4672 mod:TimeTest[400000]: enum TimeTest!ma* 

 index            address     name
     1             42cc56 :   main
     3             415810 :   malloc
     5             415450 :   mainCRTStartup

pid:4672 mod:TimeTest[400000]: q 

goodbye 
```

### <span id="running_dbh_in_batch_mode"></span><span id="RUNNING_DBH_IN_BATCH_MODE"></span>Running DBH in Batch Mode

If you wish to run only a single DBH command, you can specify it at the end of the command line. This causes DBH to start, load the specified module, run the specified command, and then exit.

For example, the previous example could be replaced with a single command line:

```
C:\> dbh -p:4672 enum TimeTest!ma* 
           400000 : TimeTest
         77820000 : ntdll
         77740000 : kernel32

index            address     name
    1             42cc56 :   main
    3             415810 :   malloc
    5             415450 :   mainCRTStartup 
```

This method of running DBH is called *batch mode*, because it can be easily used in batch files. This version of the command line can also be followed by a pipe ( **|** ) which redirects the DBH output to another program.

### <span id="specifying_the_target"></span><span id="SPECIFYING_THE_TARGET"></span>Specifying the Target

DBH can select a target in three ways: by the process ID of a running process, by the name of the executable, or by the name of the symbol file. For example, if there is exactly one instance of MyProg.exe currently running, with process ID 1234, then the following commands are almost equivalent:

```
C:\> dbh -v -p:1234 
C:\> dbh -v c:\mydir\myprog.exe 
C:\> dbh -v c:\mydir\myprog.pdb 
```

One difference between these commands is that when you start DBH by specifying the process ID, DBH uses the actual virtual addresses being used by this process. When you start DBH by specifying the executable name or the symbol file name, DBH assumes that the module's base address is a standard value (for example, 0x01000000). You can then use the **base** command to specify the actual base address, thus shifting the addresses of all the symbols in the module.

DBH does not attach to the target process in the way that a debugger does. DBH cannot cause a process to begin or end, nor can it alter how that process runs. For DBH to attach to a process by its process ID, the target process has to be running, but once DBH has been started the target process can be terminated and DBH will continue to access its symbols.

### <span id="decorated_and_undecorated_symbols"></span><span id="DECORATED_AND_UNDECORATED_SYMBOLS"></span>Decorated and Undecorated Symbols

By default, DBH uses undecorated symbol names when displaying and searching for symbols. If you turn off the [SYMOPT\_UNDNAME](symbol-options.md#symopt-undname) symbol option, or include the -d option on the DBH command line, decorations will be included.

For information on symbol decorations, see [Public and Private Symbols](public-and-private-symbols.md).

### <span id="exiting_dbh"></span><span id="EXITING_DBH"></span>Exiting DBH

To exit DBH, use the **q** command at the DBH prompt.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20DBH%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




