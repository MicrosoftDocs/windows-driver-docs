---
title: DBH Command-Line Options
description: The DBH command line uses the following syntax.
ms.assetid: fd333c2d-1f07-4a47-8653-e10cf58417a5
keywords: ["DBH Command-Line Options Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- DBH Command-Line Options
api_type:
- NA
---

# DBH Command-Line Options


The DBH command line uses the following syntax.

```
    dbh [Options] -p:PID [Command] 

dbh [Options] ExecutableName [Command] 

dbh [Options] SymbolFileName [Command] 

dbh -? 

dbh -??  

   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="-p_PID"></span><span id="-p_pid"></span><span id="-P_PID"></span>**-p:***PID*  
Specifies the process ID of the process whose symbols are to be loaded.

<span id="_______ExecutableName______"></span><span id="_______executablename______"></span><span id="_______EXECUTABLENAME______"></span> *ExecutableName*   
Specifies the executable file whose symbols are to be loaded, including the file name extension (usually .exe or .sys). You should include a relative or absolute directory path; if no path is included, the current working directory is assumed. If the specified file is not found in this location, DBH searches for it using **SymLoadModuleEx**.

<span id="_______SymbolFileName______"></span><span id="_______symbolfilename______"></span><span id="_______SYMBOLFILENAME______"></span> *SymbolFileName*   
Specifies the symbol file whose symbols are to be loaded, including the file name extension (.pdb or .dbg). You should include a relative or absolute directory path; if no path is included, the current working directory is assumed.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any combination of the following options.

<span id="-d"></span><span id="-D"></span>**-d**  
Causes decorated names to be used when displaying symbols and searching for symbols. When this option is used, [SYMOPT\_PUBLICS\_ONLY](symbol-options.md#symopt-publics-only) is turned on, and both SYMOPT\_UNDNAME and SYMOPT\_AUTO\_PUBLICS are turned off. This is equivalent to issuing the command symopt +4000 followed by symopt -10002 after DBH is running.

<span id="-s_Path"></span><span id="-s_path"></span><span id="-S_PATH"></span>**-s:***Path*  
Sets the symbol path to the specified *Path* value.

<span id="-n_"></span><span id="-N_"></span>**-n**   
Turns on *noisy symbol loading*. Additional information is displayed about the search for symbols. The name of each symbol file is displayed as it is loaded. If the debugger cannot load a symbol file, it displays an error message. Error messages for .pdb files are displayed in text. Error messages for .dbg files are in the form of an error code, explained in the winerror.h file. Not all of these messages are useful, but some of them may be helpful to analyze why a symbol file cannot be found or matched. If an image file is loaded solely to recover symbolic header information, this is displayed as well.

<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Causes DBH to run, execute the specified *Command*, and then exit. For a list of possible commands, see [DBH Commands](dbh-commands.md).

<span id="_______-_______"></span> **-?**   
Displays help text for the DBH command line.

<span id="_______-________"></span> **-??**   
Displays help text for the DBH command line, and displays a list of all DBH commands.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the DBH tool, see [Using DBH](using-dbh.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DBH%20Command-Line%20Options%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




