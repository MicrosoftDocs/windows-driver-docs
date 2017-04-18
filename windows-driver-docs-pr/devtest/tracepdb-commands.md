---
title: Tracepdb Commands
description: To use Tracepdb, type the commands in a Command Prompt window. The following syntax displays the elements of a Tracepdb command.
ms.assetid: c6502f26-d50e-48dc-85b4-978a83abff33
keywords: ["Tracepdb Commands Driver Development Tools"]
topic_type:
- apiref
api_name:
- Tracepdb Commands
api_type:
- NA
---

# Tracepdb Commands


To use Tracepdb, type the commands in a Command Prompt window. The following syntax displays the elements of a Tracepdb command.

Use the following parameters to specify the location of the PDB files.

``` syntax
    tracepdb [-f PDBFiles] [-s] [-p TMFDirectory] [-v] [-c]

   
```

Use the following parameters to specify an image file for the [trace provider](trace-provider.md).

``` syntax
    tracepdb -i ImageFiles [-r SymbolPaths] [-p TMFDiretory]  [-v]

   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-f_______PDBfiles______"></span><span id="_______-f_______pdbfiles______"></span><span id="_______-F_______PDBFILES______"></span> **-f** *PDBfiles*   
Specifies the location of the PDB symbol files that are the input to Tracepdb. The default is \*.pdb in the local directory.

*PDBFiles* are the path and file names of one or more PDB files. The file names can include wildcard characters, such as an asterisk (\*) to represent multiple characters and a question mark (?) to represent a single character. Use a semicolon (;) to separate file names.

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Searches recursively. Creates TMF files for all PDB files that match the value of the **-f** parameter in the directory and all subdirectories of the path specified by the **-f** parameter. If **-f** is omitted, **-s** creates TMF files for all PDB files in the local directory and its subdirectories.

<span id="_______-p_______TMFDirectory______"></span><span id="_______-p_______tmfdirectory______"></span><span id="_______-P_______TMFDIRECTORY______"></span> **-p** *TMFDirectory*   
Specifies a location for the TMF files that Tracepdb creates. The default is the local directory.

The TMF file is the Tracepdb output file. You cannot specify the name of the TMF file. The file name is the [message GUID](message-guid.md) of the [trace provider](trace-provider.md).

<span id="_______-i_______ImageFiles______"></span><span id="_______-i_______imagefiles______"></span><span id="_______-I_______IMAGEFILES______"></span> **-i** *ImageFiles*   
Specifies the location of the image files of [trace providers](trace-provider.md) on the local computer. When you use the **-i** parameter, Tracepdb uses the name and version of the image file to locate its PDB symbol file.

*ImageFiles* are the paths and file names of one or more binary files (.exe, .dll, .sys) of trace providers. The file names in *ImageFiles* can include wildcard characters, such as \* (to represent multiple characters) and ? (to represent a single character). Use a semicolon (**;**) to separate image file names.

<span id="_______-r_______SymbolPaths______"></span><span id="_______-r_______symbolpaths______"></span><span id="_______-R_______SYMBOLPATHS______"></span> **-r** *SymbolPaths*   
Specifies the location of the PDB symbol files.

*SymbolPaths* represents one or more paths to directories that store private symbols or to directories on a symbol server. The path names in *SymbolPaths* can include wildcard characters, such as \* (to represent multiple characters) and ? (to represent a single character).

If you include the **-i** parameter, but omit **-r**, Tracepdb searches for the PDB files for the specified images in the paths specified by the %\_NT\_SYMBOL\_PATH% environment variable. If the environment variable is not set, Tracepdb searches in the default symbol path, **srv\*\\\\\\\\symbols\\\\symbols**.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Displays verbose output.

<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Generates [TMC](trace-message-control-file.md) files.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

```
tracepdb -v
tracepdb -f tracedrv.pdb
tracepdb -f c:\tracing\ndis*.pdb -s
tracepdb -f d:\tools\trace*.pdb -p d:\tracing
tracepdb -i d:\winddk\7060\src\general\tracing\tracedrv\objfre_wnet_x86_vh\tracedrv.sys -r 
tracepdb -i trace*.exe;flpy*.dll -p d:\tracing
tracepdb -i tracedrv.exe -r srv*\\\\symbolstore\\symbols\\new
```

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The name of the TMF file is the [message GUID](message-guid.md) of the source file. The message GUID represents a source file and the trace entries in the file. Windows uses the message GUID to associate a trace message with the TMF file that contains formatting instructions for the message.

If you submit a PDB symbol file that does not include trace formatting instructions, Tracepdb displays an information message and does not create any files.

If Tracefmt cannot find any PDB files in the path specified, it returns to the command prompt without comment. To get processing details, resubmit the command with the **-v** parameter.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tracepdb%20Commands%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




