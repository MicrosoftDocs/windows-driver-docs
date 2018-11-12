---
title: PDBCopy Command-Line Options
description: The PDBCopy command line uses the following syntax. The parameters can be included in any order.
ms.assetid: a793f860-db21-41fb-a0d2-931812400f0d
keywords: ["PDBCopy Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 04/10/2018
topic_type:
- apiref
api_name:
- PDBCopy Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# PDBCopy Command-Line Options


The PDBCopy command line uses the following syntax. The parameters can be included in any order.

```dbgcmd
pdbcopy OldPDB NewPDB [Options] 

pdbcopy OldPDB NewPDB -p [-f:Symbol] [-f:@TextFile] [Options] 

pdbcopy OldPDB NewPDB -p [-F:Symbol] [-F:@TextFile] [Options] 

pdbcopy InputPDB BackupPDB -CVE-2018-1037 [autofix|verbose]

pdbcopy /? 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______OldPDB______"></span><span id="_______oldpdb______"></span><span id="_______OLDPDB______"></span> *OldPDB*   
Specifies the path and file name of the original symbol file to be read, including the .pdb file name extension. *OldPDB* may contain the absolute or relative path of a directory on the local computer, or a UNC path. If no path is specified, the current working directory is used. If *OldPDB* contains spaces, it must be enclosed in quotation marks.

<span id="_______NewPDB______"></span><span id="_______newpdb______"></span><span id="_______NEWPDB______"></span> *NewPDB*   
Specifies the path and file name of the new symbol file to be created, including the .pdb file name extension. *NewPDB* may contain the absolute or relative path of a directory on the local computer, or a UNC path. This path must already exist; PDBCopy will not create a new directory. If no path is specified, the current working directory is used. If *NewPDB* contains spaces, you must enclose it in quotation marks. The specified file should not already exist; if it does, the new file may not be written, or may be written incorrectly.

<span id="_______-p______"></span><span id="_______-P______"></span> **-p**   
Causes PDBCopy to remove private symbol data from the new symbol file. If the old symbol file contains no private symbols, this option has no effect. If this option is omitted, PDBCopy creates a new file with identical symbol content as the original file.

<span id="-f_Symbol"></span><span id="-f_symbol"></span><span id="-F_SYMBOL"></span>**-f:**<em>Symbol</em>  
Causes PDBCopy to remove the specified public symbol from the new symbol file. *Symbol* must specify the name of the symbol to be removed, including any symbol name decorations (for example, initial underscores), but not including the module name. This option requires the -p option. If you use multiple **-f** or **-f:@** parameters, PDBCopy removes all the specified symbols from the new symbol file.

<span id="-f__TextFile"></span><span id="-f__textfile"></span><span id="-F__TEXTFILE"></span>**-f:@**<em>TextFile</em>  
Causes PDBCopy to remove the public symbols listed in the specified text file from the new symbol file. *TextFile* specifies the file name and path (absolute or relative) of this file. This file can list the names of any number of symbols, one on each line, including any symbol name decorations (for example, initial underscores), but not including module names. This option requires the -p option.

<span id="-F_Symbol"></span><span id="-f_symbol"></span><span id="-F_SYMBOL"></span>**-F:**<em>Symbol</em>  
Causes PDBCopy to remove all public and private symbols from the new symbol file, except for the specified public symbol. *Symbol* must specify the name of the symbol to be retained, including any symbol name decorations (for example, initial underscores), but not including the module name. This option requires the -p option. If multiple **-F** or **-F:@** parameters are used, all the specified symbols are retained in the new symbol file.

<span id="-F__TextFile"></span><span id="-f__textfile"></span><span id="-F__TEXTFILE"></span>**-F:@**<em>TextFile</em>  
Causes PDBCopy to remove all public and private symbols from the new symbol file, except for the public symbols listed in the specified text file. *TextFile* specifies the file name and path (absolute or relative) of this file. This file can list the names of any number of symbols, one on each line, including any symbol name decorations (for example, initial underscores), but not including module names. This option requires the -p option.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any combination of the following options. These options are case-sensitive.

<span id="-s"></span><span id="-S"></span>**-s**  
Causes the new symbol file to have a different signature than the old file. Normally you should not use the -s option, because a new signature may cause SymSrv to assign a different index value to the new file than to the old file, preventing new file from properly replacing the old one.

<span id="-vc6"></span><span id="-VC6"></span>**-vc6**  
Causes PDBCopy to use mspdb60.dll instead of mspdb80.dll. This option is never required, because PDBCopy automatically looks for the proper version of mspdb\*.dll. By default, PDBCopy uses mspdb80.dll, which is the version used by Visual Studio .NET 2002 and later versions of Visual Studio. If your symbols were built using Visual Studio 6.0 or an earlier version, you can specify this command-line option so that PDBCopy will use mspdb60.dll instead. However, this is not required, since PDBCopy looks for the appropriate file even if this option is not used. Whichever version of mspdb\*.dll you use must be in the executable path of the Command Prompt window from which you launch PDBCopy.


<span id="CVE-2018-1037"></span> **-CVE-2018-1037**   

Reports whether InputPDBFile has the issue described in CVE-2018-1037 and optionally remediates the problem. See [KB# 4131751 - PDBCopy tool](https://support.microsoft.com/help/4131751/pdbcopy-update-to-fix-pdb-security-issue) for more information and detailed usage information.


<span id="_______-_______"></span> **-?**   
Displays help text for the PDBCopy command line.



### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the PDBCopy tool, see [Using PDBCopy](using-pdbcopy.md).

 

 





