---
title: XpsConverter
description: XPS Converter (XpsConverter.exe) is a command-line tool for converting XML Paper Specification (XPS) documents from Microsoft XPS (MSXPS) to standardized OpenXPS.
ms.assetid: A51F818E-AECD-4EBD-99AC-F3BD026C19D6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XpsConverter


XPS Converter (XpsConverter.exe) is a command-line tool for converting XML Paper Specification (XPS) documents from Microsoft XPS (MSXPS) to standardized OpenXPS, and from OpenXPS to Microsoft XPS (MSXPS). This tool is intended to aide in the conversion of XPS test collateral from one XPS format to the other.

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Where can I download XpsConverter?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>XpsConverter.exe is included in the Microsoft Windows Driver Kit (WDK). For information about getting the WDK, see <a href="http://go.microsoft.com/fwlink/p/?linkid=290798" data-raw-source="[Windows Driver Kit Downloads]( http://go.microsoft.com/fwlink/p/?linkid=290798)">Windows Driver Kit Downloads</a>.</p></td>
</tr>
</tbody>
</table>

 

The XpsConverter is not intended to be used in any other capacity than as a stand-alone tool. It is not supported for any other use. It may not be used in part or whole in any application or driver, and de-compiling or modifying the tool is strictly prohibited. Microsoft retains all rights and holds copyright on XpsConverter.exe and all its supporting documentation.

**To convert XPS documents**

1.  Open a Visual Studio Command Prompt window.

2.  Run the **XpsConverter.exe** tool and specify the names of the source and destination files or folders and specify the format to convert the file(s) to.

    For example, the following command converts the MSXPS file called text.xps to OpenXPS format.

    ```
    XpsConverter /OpenXPS /InputFile=Text.xps /OutputFile=Test.oxps
    ```

    When you install the WDK, the XpsConverter.exe file is placed in the %programfiles%\\Windows Kits\\8.1\\bin\\*&lt;arch&gt;* or %programfiles(86)%\\Windows Kits\\8.1\\bin\\*&lt;arch&gt;* directories.

## <span id="XpsConverter_Command_Syntax"></span><span id="xpsconverter_command_syntax"></span><span id="XPSCONVERTER_COMMAND_SYNTAX"></span>XpsConverter Command Syntax


```
  XpsConverter  <format>  
  [/InputFile=<inputfile> /OutputFile=<outputfile>  | /InputFolder=<inputfolder> /OutputFolder=<outputfolder>]  

  [-logger:<LoggerType>]
  [-logfile:<LogFile>  ]
  [ -device:<DeviceString> ]
  [ /? ]
```

## <span id="Command_parameters"></span><span id="command_parameters"></span><span id="COMMAND_PARAMETERS"></span>Command parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="_format_"></span><span id="_FORMAT_"></span><em>&lt;format&gt;</em></p></td>
<td align="left"><p>Specifies the format to convert the source file(s) to. The <em>&lt;format&gt;</em> is required. Specify <strong>/OpenXPS</strong> to convert the document(s) to OpenXPS or <strong>/XPS</strong> to convert the document(s) to Microsoft XPS (MSXPS).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_InputFile__inputfile___OutputFile__outputfile_"></span><span id="_inputfile__inputfile___outputfile__outputfile_"></span><span id="_INPUTFILE__INPUTFILE___OUTPUTFILE__OUTPUTFILE_"></span><strong>/InputFile=</strong><em>&lt;inputfile&gt;</em> <strong>/OutputFile=</strong><em>&lt;outputfile&gt;</em></p></td>
<td align="left"><p>Use this option to convert <em>&lt;inputfile&gt;</em> and save it to <em>&lt;outputfile&gt;</em>. The <em>&lt;inputfile&gt;</em> must have the .xps or .oxps file name extension.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_InputFolder__inputfolder____OutputFolder__outputfolder_"></span><span id="_inputfolder__inputfolder____outputfolder__outputfolder_"></span><span id="_INPUTFOLDER__INPUTFOLDER____OUTPUTFOLDER__OUTPUTFOLDER_"></span><strong>/InputFolder=</strong><em>&lt;inputfolder&gt;</em> <strong>/OutputFolder=</strong><em>&lt;outputfolder&gt;</em></p></td>
<td align="left"><p>Use this option to convert all the files in <em>&lt;inputfolder&gt;</em> and save them to the <em>&lt;outputfolder&gt;</em>. Files in <em>&lt;inputfolder&gt;</em> must have .xps or .oxps file name extensions.</p>
<div class="alert">
<strong>Note</strong>   Converting a folder is a recursive operation. The tool converts all files in the specified s<em>&lt;inputfolder&gt;</em> and all subdirectories.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p><span id="__-logger__LoggerType_"></span><span id="__-logger__loggertype_"></span><span id="__-LOGGER__LOGGERTYPE_"></span> <strong>-logger:</strong><em>&lt;LoggerType&gt;</em></p></td>
<td align="left"><p>Optional. <em>&lt;LoggerType&gt;</em> indicates the type of log to generate (<strong>File</strong>, <strong>Console</strong> or <strong>WTT</strong>) to use during the conversion. The default logger is <strong>Console</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="-logfile__LogFile_"></span><span id="-logfile__logfile_"></span><span id="-LOGFILE__LOGFILE_"></span><strong>-logfile:</strong><em>&lt;LogFile&gt;</em></p></td>
<td align="left"><p>Optional. Specifies the <em>&lt;LogFile&gt;</em> to use when the <strong>-logger</strong> option is <strong>FILE</strong>. If you do not specify a <em>&lt;LogFile&gt;</em>, the default log file is XpsConverter.txt.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="-device__DeviceString_"></span><span id="-device__devicestring_"></span><span id="-DEVICE__DEVICESTRING_"></span><strong>-device:</strong><em>&lt;DeviceString&gt;</em></p></td>
<td align="left"><p>Optional. Specifies the<em>&lt;DeviceString&gt;</em> to use when the <strong>-logger</strong> option is <strong>WTT</strong>. The default device is <strong>$LogFile:file=XpsConverter.wtl,WriteMode=append</strong>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


You can use the **isXPS.exe (isXPS Conformance Tool)** to tests a file's conformity to the XPS and the Open Packaging Conventions (OPC) specifications.

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


```
XpsConverter /OpenXPS /InputFile=Text.xps /OutputFile=Test.oxps
XpsConverter /XPS /InputFolder=c:\OpenXPS /OutputFolder=c:\MSXPS
XpsConverter /OpenXPS /InputFile=MyDoc.xps /OutputFile=ConvertedMyDoc.oxps  logger:file  logfile:MyLog.txt
```

## <span id="related_topics"></span>Related topics


**isXPS.exe (isXPS Conformance Tool)**

 

 






