---
title: BinPlace Command-Line Syntax
description: BinPlace uses the following syntax at the command line
ms.assetid: 8489b7ae-3e3b-41d5-b9a6-0b69aa92087e
keywords:
- BinPlace Command-Line Syntax Driver Development Tools
topic_type:
- apiref
api_name:
- BinPlace Command-Line Syntax
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# BinPlace Command-Line Syntax


BinPlace uses the following syntax at the command line:

```
    binplace [Options] File [ [Options] [@PlaceFile] File [...] ]
```

## <span id="ddk_binplace_command_line_syntax_tools"></span><span id="DDK_BINPLACE_COMMAND_LINE_SYNTAX_TOOLS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
This can include any of the following switches. The switches should be preceded by a hyphen (-) or a slash (/). It is possible to combine several options after one hyphen or slash, but options that take additional parameters should be followed by a space. Thus, the following two commands are equivalent:

```
binplace -q -k -g LCFile -v -s SymbolRoot File 
binplace -qkg LCFile -vs SymbolRoot File 
```

The following switches are available:

<span id="-a"></span><span id="-A"></span>**-a**  
Causes BinPlace to strip private symbols out of the symbol files when they are being placed. This creates stripped symbol files that contain public symbols but not private symbols. When using the **-a** switch, you must use **-s** and **-x** as well. When **-a** is used, stripped symbol files will be placed in the path specified by **-s***SymbolRoot*. If **-n***FullSymbolRoot* is also present, the full symbol files will be placed in *FullSymbolRoot*. Otherwise, they will not be placed anywhere.

<span id="-b_ExtraSubdirectory"></span><span id="-b_extrasubdirectory"></span><span id="-B_EXTRASUBDIRECTORY"></span>**-b** *ExtraSubdirectory*  
Causes BinPlace to place files in a different location than usual. After concatenating the root destination directory, the class subdirectory, and the file-type subdirectory as usual, BinPlace will then append *ExtraSubdirectory* to this path to create the final destination directory. *ExtraSubdirectory* should neither begin with nor end with a backslash. See [BinPlace Destination Directories](binplace-destination-directories.md) for more details.

<span id="-e"></span><span id="-E"></span>**-e**  
Causes BinPlace to continue execution if a file cannot be placed. By default, BinPlace will exit when this error occurs.

<span id="-f"></span><span id="-F"></span>**-f**  
Forces BinPlace to place a file even if it is overwriting a more recent file. By default, when BinPlace attempts to place a file, it will overwrite an older version but will not overwrite a more recent version.

<span id="-g_LCFile"></span><span id="-g_lcfile"></span><span id="-G_LCFILE"></span>**-g** *LCFile*  
Causes BinPlace to verify the executable file. *LCFile* specifies the localization constraint file to be used for this verification.

<span id="-h"></span><span id="-H"></span>**-h**  
Causes BinPlace to create hard links instead of copying the file when placing files. This option is only available on the NTFS file system.

<span id="-j"></span><span id="-J"></span>**-j**  
Causes BinPlace to verify that the proper symbols exist before copying any executable files. For this option to be used, the SymChk tool must be in your path. (SymChk is part of the Debugging Tools for Windows package. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) for details.)

<span id="-k"></span><span id="-K"></span>**-k**  
Causes BinPlace to preserve file attributes. By default, BinPlace will turn off the archive attribute.

<span id="-n_FullSymbolRoot"></span><span id="-n_fullsymbolroot"></span><span id="-N_FULLSYMBOLROOT"></span>**-n** *FullSymbolRoot*  
Specifies the root directory for full symbol files (symbol files that contain both public and private symbols). This requires the **-a**, **-x**, and **-s** switches as well. See [BinPlace Destination Directories](binplace-destination-directories.md) for more details.

<span id="-o_RootSubdirectory"></span><span id="-o_rootsubdirectory"></span><span id="-O_ROOTSUBDIRECTORY"></span>**-o** *RootSubdirectory*  
Specifies a subdirectory of the root destination directory to be used. When the destination directory is created, *RootSubdirectory* will be inserted after the root destination directory and before the class subdirectory. See [BinPlace Destination Directories](binplace-destination-directories.md) for more details.

<span id="-p_PlaceFile"></span><span id="-p_placefile"></span><span id="-P_PLACEFILE"></span>**-p** *PlaceFile*  
Specifies the path and file name of the place file. If the **-p** switch is not used, BinPlace uses a place named *\\tools\\placefil.txt*. See [**Place File Syntax**](place-file-syntax.md) for an explanation of a place file's contents.

**Note**  The **-p** switch and place files are now obsolete and should not be used.



<span id="-q"></span><span id="-Q"></span>**-q**  
Prevents BinPlace from using a log file. If the **-q** switch is omitted, the file specified by the BINPLACE\_LOG environment variable is used as the log file.

<span id="-r_RootDestinationPath"></span><span id="-r_rootdestinationpath"></span><span id="-R_ROOTDESTINATIONPATH"></span>**-r** *RootDestinationPath*  
Specifies the root destination directory. If this is omitted, the default is determined by the \_NT386TREE, \_NTIA64TREE, or \_NTAMD64TREE environment variable on an x86-based, Itanium-based, or x64-based computer, respectively. See [BinPlace Destination Directories](binplace-destination-directories.md) for details.

<span id="-s_SymbolRoot"></span><span id="-s_symbolroot"></span><span id="-S_SYMBOLROOT"></span>**-s** *SymbolRoot*  
Specifies the root directory for symbol files. If the **-a** and **-x** switches are also used, private symbols will be stripped out of the symbol files, and the stripped symbol files will be placed in the directory specified by *SymbolRoot*. If you want to place both stripped and full symbol files, you should use -a -x -s SymbolRoot -n FullSymbolRoot. See [BinPlace Destination Directories](binplace-destination-directories.md) for more details.

<span id="-t"></span><span id="-T"></span>**-t**  
*Test mode*. When this switch is used, no files will be copied, but BinPlace will display warning and error messages as if it were placing files. You may want to use the **-v** switch as well to increase the number of messages.

<span id="-u"></span><span id="-U"></span>**-u**  
Causes BinPlace to append \\up to the class subdirectory. This is useful for separating out uniprocessor (UP) drivers. In addition, whenever this switch is used, BinPlace will not split executable files containing symbols. See [BinPlace Destination Directories](binplace-destination-directories.md) for more details.

<span id="-v"></span><span id="-V"></span>**-v**  
*Verbose mode*. Causes BinPlace to display more detailed error, warning, and progress messages.

<span id="-w"></span><span id="-W"></span>**-w**  
Causes BinPlace to add Windows 95 symbol files (.sym) to the symbol tree.

<span id="-x"></span><span id="-X"></span>**-x**  
If BinPlace encounters files that use the *old symbol system*, this switch causes it to remove all symbols from the executable files and move this information to separate symbol files. See [Symbol File Systems](symbol-file-systems.md) for details. When using the **-x** switch, you must use **-s** and **-a** as well.

<span id="-y"></span><span id="-Y"></span>**-y**  
Prevents BinPlace from using any class subdirectories. The destination directory will be created solely from the root destination directory plus the file-type subdirectory. See [BinPlace Destination Directories](binplace-destination-directories.md) for details.

<span id="-z"></span><span id="-Z"></span>**-z**  
Cancels the **-x** switch. This can be useful if you are using BinPlace on several targets -- you can use a command of the form **binplace** *argumentsTarget1argumentsTarget2*, and since the command line is parsed from left to right, *Target1* and *Target2* will be affected by different arguments. (See the Parsing Order section following). If a **-z** switch is encountered, this cancels the effect of any previous **-x** switch.

<span id="-ci_ReturnCode_Application_Argument_Argument__..._"></span><span id="-ci_returncode_application_argument_argument__..._"></span><span id="-CI_RETURNCODE_APPLICATION_ARGUMENT_ARGUMENT__..._"></span>**-ci** <em>ReturnCode</em>**,**<em>Application</em>**,**<em>Argument</em>**,**<em>Argument</em>**,** ...   
Causes BinPlace to use a custom application to validate all executable files. You can use the **-ci** switch if you want BinPlace to use some other application to do its validation.

*ReturnCode* should be the value that will be returned by this application if it finds an error in an executable file. The additional parameters are used to launch this application. These must all be separated by commas. *Application* specifies the name of the program. This can be followed by any number of command-line arguments. The program will be started with a command line that includes *Application* followed by all the arguments (separated by spaces rather than commas), and finally ending with the name of the executable file to be checked.

<span id="-_ARC"></span><span id="-_arc"></span>**-:ARC**  
Causes BinPlace to only place files whose archive attributes are set.

<span id="-_DBG"></span><span id="-_dbg"></span>**-:DBG**  
Prevents BinPlace from placing .dbg files. If the **-j** switch is also used, this will prevent BinPlace from placing binaries that point to .dbg files. For this option to be used, the SymChk tool must be in your path. (SymChk is part of the Debugging Tools for Windows package. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) for details.)

<span id="-_DEST_ClassPath"></span><span id="-_dest_classpath"></span><span id="-_DEST_CLASSPATH"></span>**-:DEST** *ClassPath*  
Causes BinPlace to ignore the place file and use the specified *ClassPath* as the class subdirectory. See [BinPlace Destination Directories](binplace-destination-directories.md) for details.

<span id="-_LOGPDB"></span><span id="-_logpdb"></span>**-:LOGPDB**  
Causes BinPlace to include the full .pdb paths in the log file.

<span id="-_REN_NewName"></span><span id="-_ren_newname"></span><span id="-_REN_NEWNAME"></span>**-:REN** *NewName*  
Causes BinPlace to rename the files being placed. The original file name, including the extension, will be replaced by *NewName*. (If the original file is an executable file that is being split, the new symbol file will be given the original file name plus the extension .dbg.)

<span id="-_TMF"></span><span id="-_tmf"></span>**-:TMF**  
Causes BinPlace to create a [trace message format (.tmf) file](trace-message-format-file.md) by extracting trace message formatting instructions from the PDB symbol file. The TMF file will be placed in the directory specified by the BinPlace TRACE\_FORMAT\_PATH environment variable. See [BinPlace Macros and Environment Variables](binplace-macros-and-environment-variables.md).

<span id="-ChangeAsmsToRetailForSymbols"></span><span id="-changeasmstoretailforsymbols"></span><span id="-CHANGEASMSTORETAILFORSYMBOLS"></span>**-ChangeAsmsToRetailForSymbols**  
Causes BinPlace to replace the string "asms" with the string "retail" if it occurs in the destination directory for symbol files. See [BinPlace Destination Directories](binplace-destination-directories.md) for more details.

<span id="_______File______"></span><span id="_______file______"></span><span id="_______FILE______"></span> *File*   
Specifies the full path and file name of a file that BinPlace will act on. You can list any number of files, separated by spaces. If a path and file name contains a space, you must enclose the path and file name in quotation marks.

<span id="________PlaceFile______"></span><span id="________placefile______"></span><span id="________PLACEFILE______"></span> **@**<em>PlaceFile</em>   
If any file name is preceded by an at sign ( **@** ), the file name represents the name of a place file. For more information, see the Supplying Parameters in a File section following.

### <span id="parsing_order"></span><span id="PARSING_ORDER"></span>Parsing Order

BinPlace parses the command line from left to right. You can specify several options, then a *File* parameter, then new options, then another *File* parameter, and so forth. Each time BinPlace encounters a new option, it will be adopted, overriding any previously seen contradictory options. Whenever it encounters a *File* specifier, it will act on that file using the accumulated options it has already encountered on the command line.

### <span id="supplying_parameters_in_a_file"></span><span id="SUPPLYING_PARAMETERS_IN_A_FILE"></span>Supplying Parameters in a File

It is possible to pass parameters to BinPlace from a text file. There are two ways to do this:

-   You can specify a file name in the BINPLACE\_OVERRIDE\_FLAGS environment variable. This file will be read and its contents used as parameters whenever BinPlace is run. The parameters in this file will be parsed before the parameters that actually appear on the BinPlace command line.

-   You can specify a file name on the BinPlace command line by prefixing it with an at sign ( **@** ). When BinPlace sees a string beginning with this sign on its command line, it will take the string, remove the at sign, and then look for a file with this name. If it finds this file, it will insert its text into the command line at exactly the place where the original parameter beginning with the at sign had been. Because BinPlace parses parameters from left to right, you can use this technique along with multiple instances of *File* to use BinPlace on several files with different options for each, without having to type all the options each time. (If this file is not found, BinPlace will treat the original string, including the at sign, as a *File* parameter.)









