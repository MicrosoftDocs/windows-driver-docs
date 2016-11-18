---
title: ChkINF Command Syntax
description: The ChkINF scripts are located in the WindowSdkDir \\Tools\\x86\\Chkinf subdirectory.
ms.assetid: 62919c28-73f1-4401-95de-59ac45e4a8e7
keywords: ["ChkINF Command Syntax Driver Development Tools"]
topic_type:
- apiref
api_name:
- ChkINF Command Syntax
api_type:
- NA
---

# ChkINF Command Syntax


The ChkINF scripts are located in the %WindowSdkDir%\\Tools\\x86\\Chkinf subdirectory. To run ChkINF, open a Command Prompt window and navigate to the ChkINF directory. Type **chkinf** to run the ChkINF.bat file.

Use the following command syntax:

``` syntax
    chkinf {INFFile [INFFile...] | Directory} [/L TextFile] [/B] [/LO] [/DC Options]

   
```

## <span id="ddk_chkinf_command_syntax_tools"></span><span id="DDK_CHKINF_COMMAND_SYNTAX_TOOLS"></span>Parameters


<span id="_______INFFile______"></span><span id="_______inffile______"></span><span id="_______INFFILE______"></span> *INFFile*   
Specifies the fully qualified path and file names of one or more INF files. ChkINF verifies the specified files. You can use the wildcard character (\*) to specify multiple files, for example, \*net.inf.

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies a directory that contain INF Files. ChkINF examines all INF files in the directory. You cannot use the wildcard character (\*) in a directory name.

<span id="________L_______TextFile______"></span><span id="________l_______textfile______"></span><span id="________L_______TEXTFILE______"></span> **/L** *TextFile*   
Creates a results file in text format, in addition to the HTML files. The text file includes results for all INF files that were validated.

*TextFile* specifies a path and file name for the resulting file. There is no default name or location. If you do not specify a file name, ChkINF does not create a text file.If you do not specify a path, ChkINF creates the text file in the current directory, not in the htm subdirectory with its other output files.

<span id="________B______"></span><span id="________b______"></span> **/B**   
Displays the results when command completes. If ChkINF is validating one INF file, ChkINF displays the results for that INF file. If ChkINF is validating more than one file, it displays the summary of results.

<span id="________LO______"></span><span id="________lo______"></span> **/LO**   
Determines whether the INF file conforms to the layout rules defined in the layout.inf file. This test is designed for printer INF files and files that are included in Windows.

<span id="________DC________Options______"></span><span id="________dc________options______"></span><span id="________DC________OPTIONS______"></span> **/DC** *Options*   
Specifies the device class-specific options that ChkINF should use when checking INF files. At present, the only supported option is **NOFAX**, which instructs ChkINF not to check any Fax keys present in modem INF files.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

```
chkinf c:\windows\inf\ntprint.inf /L d:\dev\ntprint.txt /b
```

```
chkinf c:\windows\inf\ntprint.inf c:\windows\inf\flpydisk.inf
```

```
chkinf d:\myinfs /b /lo
```

```
chkinf c:\windows\inf\*net* /L netinfs.txt /b
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20ChkINF%20Command%20Syntax%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




