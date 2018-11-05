---
title: KDbgCtrl Command-Line Options
description: The KDbgCtrl command line uses the following syntax
ms.assetid: 0367a09d-c475-4aeb-8f88-47d51ec7e9d5
keywords: ["KDbgCtrl Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KDbgCtrl Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# KDbgCtrl Command-Line Options


The KDbgCtrl command line uses the following syntax:

```dbgcmd
kdbgctrl [-e|-d|-c] [-ea|-da|-ca] [-eu|-du|-cu] [-eb|-db|-cb] [-sdb Size | -cdb] 

kdbgctrl -cx 

kdbgctrl -td ProcessID File 

kdbgctrl -? 
```

## <span id="ddk_kdbgctrl_command_line_options_dbg"></span><span id="DDK_KDBGCTRL_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-e______"></span><span id="_______-E______"></span> **-e**   
Enables Full Kernel Debugging.

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
Disables Full Kernel Debugging.

<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Checks whether Full Kernel Debugging is enabled. Displays true if Full Kernel Deubugging is enabled, and displays false if Full Kernel Debugging is disabled.

<span id="_______-ea______"></span><span id="_______-EA______"></span> **-ea**   
Enables Automatic Kernel Debugging.

<span id="_______-da______"></span><span id="_______-DA______"></span> **-da**   
Disables Automatic Kernel Debugging.

<span id="_______-ca______"></span><span id="_______-CA______"></span> **-ca**   
Checks whether Automatic Kernel Debugging is enabled. Displays true if Automatic Kernel Deubugging is enabled, and displays false if Automatic Kernel Debugging is disabled.

<span id="_______-eu______"></span><span id="_______-EU______"></span> **-eu**   
Enables User-Mode Error Handling.

<span id="_______-du______"></span><span id="_______-DU______"></span> **-du**   
Disables User-Mode Error Handling.

<span id="_______-cu______"></span><span id="_______-CU______"></span> **-cu**   
Checks whether User-Mode Error Handling is enabled. Displays true if User-Mode Error Handling is enabled, and displays false if User-Mode Error Handling is disabled.

<span id="-eb"></span><span id="-EB"></span>**-eb**  
Enables blocking of kernel debugging.

<span id="-db"></span><span id="-DB"></span>**-db**  
Disables blocking of kernel debugging

<span id="-cb"></span><span id="-CB"></span>**-cb**  
Checks whether kernel debugging is blocked. Displays true if kernel debugging is blocked, and displays false if kernel debugging is not blocked.

<span id="_______-sdb_______Size______"></span><span id="_______-sdb_______size______"></span><span id="_______-SDB_______SIZE______"></span> **-sdb** *Size*   
Sets the size of the DbgPrint buffer. If *Size* is prefixed with **0x** it will be interpreted as a hexadecimal number. If it is prefixed with **0** (zero), it will be interpreted as octal. Otherwise, it will be interpreted as decimal.

<span id="_______-cdb______"></span><span id="_______-CDB______"></span> **-cdb**   
Displays the current size, in bytes, of the DbgPrint buffer.

<span id="_______-cx______"></span><span id="_______-CX______"></span> **-cx**   
Determines the current Full Kernel Debugging setting and returns an appropriate value. This option cannot be combined with other options, and it does not display any output. It is designed for use in a batch file where the return value of the KDbgCtrl program can be tested. Possible return values are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>0x10001</strong></p></td>
<td align="left"><p>Full Kernel Debugging is enabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>0x10002</strong></p></td>
<td align="left"><p>Full Kernel Debugging is disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Any other value</p></td>
<td align="left"><p>An error occurred. KDbgCtrl was unable to determine the current status of Full Kernel Debugging.</p></td>
</tr>
</tbody>
</table>

 

<span id="-td_ProcessID_File"></span><span id="-td_processid_file"></span><span id="-TD_PROCESSID_FILE"></span>**-td** *ProcessID* *File*  
Obtains a kernel triage dump file. Enter the process ID and a name for the dump file.

<span id="_______-_______"></span> **-?**   
Displays command-line help for KDbgCtrl.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a description of all the KDbgCtrl settings, see [Using KDbgCtrl](using-kdbgctrl.md).

 

 





