---
title: Using AMLI Debugger Commands
description: Using AMLI Debugger Commands
ms.assetid: 8efa6f13-67db-417a-83ec-8219afc9874c
keywords: ["AMLI Debugger, AMLI Debugger commands"]
ms.author: domars
ms.date: 11/07/2018
ms.localizationpriority: medium
---

# Using AMLI Debugger Commands


## <span id="ddk_using_amli_debugger_commands_dbg"></span><span id="DDK_USING_AMLI_DEBUGGER_COMMANDS_DBG"></span>


The following commands can be issued from the AMLI Debugger prompt.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">General Category</th>
<th align="left">Specific Action</th>
<th align="left">AMLI Debugger Commands</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Controlling the Debugger</p></td>
<td align="left"><p></p>
Continue Execution
Break to Kernel Debugger</td>
<td align="left"><p></p>
<strong>g</strong>
<strong>q</strong></td>
</tr>
<tr class="even">
<td align="left"><p>Controlling AML Execution</p></td>
<td align="left"><p></p>
Run Method
Step Over AML Code
Trace Into AML Code</td>
<td align="left"><p></p>
<strong>run</strong>
<strong>p</strong>
<strong>t</strong></td>
</tr>
<tr class="odd">
<td align="left"><p>Controlling Trace Mode Settings</p></td>
<td align="left"><p>Configure Trace Mode</p></td>
<td align="left"><p><strong>trace</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Notifying a Namespace Object</p></td>
<td align="left"><p>Notify Namespace Object</p></td>
<td align="left"><p><strong>notify</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Displaying the Object Count Table</p></td>
<td align="left"><p>Display Object Count Table</p></td>
<td align="left"><p><strong>dc</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Accessing Memory</p></td>
<td align="left"><p></p>
Display Data
Display Data Bytes
Display Data Words
Display Data DWORDs
Display Data String
Edit Memory</td>
<td align="left"><p></p>
<strong>d</strong>
<strong>db</strong>
<strong>dw</strong>
<strong>dd</strong>
<strong>da</strong>
<strong>e</strong></td>
</tr>
<tr class="odd">
<td align="left"><p>Accessing Ports</p></td>
<td align="left"><p></p>
Read Byte from Port
Read Word from Port
Read DWORD from Port
Write Byte to Port
Write Word to Port
Write DWORD to Port</td>
<td align="left"><p></p>
<strong>i</strong>
<strong>iw</strong>
<strong>id</strong>
<strong>o</strong>
<strong>ow</strong>
<strong>od</strong></td>
</tr>
<tr class="even">
<td align="left"><p>Displaying Help</p></td>
<td align="left"><p>Display Help</p></td>
<td align="left"><p><strong>?</strong></p></td>
</tr>
</tbody>
</table>

 

### <span id="controlling_the_debugger"></span><span id="CONTROLLING_THE_DEBUGGER"></span>Controlling the Debugger

These commands exit the AMLI Debugger. The **g** command will resume normal execution of the target computer, and the **q** command will freeze the target computer and break into the kernel debugger.

**g**

**q**

### <span id="controlling_aml_execution"></span><span id="CONTROLLING_AML_EXECUTION"></span>Controlling AML Execution

These commands allow you to run or step through AML methods. The **run** command begins execution at a specified point. The **p** and **t** commands allow you to step through one instruction at a time. If a function call is encountered, the **p** command treats the function as a single step, while the **t** command traces into the new function one instruction at a time.


**run** *MethodName* **\[***ArgumentList***\]**

**run** *CodeAddress* **\[***ArgumentList***\]**

**p**

**t**

<span id="MethodName"></span><span id="methodname"></span><span id="METHODNAME"></span>*MethodName*  
Specifies the full path and name of a method. Execution will start at the beginning of this method's memory location.

<span id="CodeAddress"></span><span id="codeaddress"></span><span id="CODEADDRESS"></span>*CodeAddress*  
Specifies the address where execution is to begin.

<span id="ArgumentList"></span><span id="argumentlist"></span><span id="ARGUMENTLIST"></span>*ArgumentList*  
Specifies a list of arguments to be passed to the method. Each argument must be an integer. Multiple arguments should be separated with spaces.

### <span id="controlling_trace_mode_settings"></span><span id="CONTROLLING_TRACE_MODE_SETTINGS"></span>Controlling Trace Mode Settings

The **trace** command controls the AML interpreter's trace mode settings. If this command is used with no parameters, the current trace mode settings are displayed.

**trace \[trigon|trigoff\] \[level=**<em>Level</em>**\] \[add=**<em>TPStrings</em>**\] \[zap=**<em>TPNumbers</em>**\]**

<span id="trigon"></span><span id="TRIGON"></span>**trigon**  
Activates trace trigger mode.

<span id="trigoff"></span><span id="TRIGOFF"></span>**trigoff**  
Deactivates trace trigger mode.

<span id="Level"></span><span id="level"></span><span id="LEVEL"></span>*Level*  
Specifies the new setting for the trace level.

<span id="TPStrings"></span><span id="tpstrings"></span><span id="TPSTRINGS"></span>*TPStrings*  
Specifies one or more trigger points to be added. Each trigger point is specified by name. Multiple trigger point strings should be separated by commas.

<span id="TPNumbers"></span><span id="tpnumbers"></span><span id="TPNUMBERS"></span>*TPNumbers*  
Specifies one or more trigger points to be deleted. Each trigger point is specified by number. Multiple trigger point numbers should be separated by commas. To see a list of trigger point numbers, use the **trace** command with no parameters.

### <span id="notifying_a_namespace_object"></span><span id="NOTIFYING_A_NAMESPACE_OBJECT"></span>Notifying a Namespace Object

The **notify** command sends a notification to an ACPI namespace object. The notification will be placed in the specified object's queue.

**notify** *ObjectName Value*

**notify** *ObjectAddress Value*

<span id="ObjectName"></span><span id="objectname"></span><span id="OBJECTNAME"></span>*ObjectName*  
Specifies the full namespace path of the object to be notified.

<span id="ObjectAddress"></span><span id="objectaddress"></span><span id="OBJECTADDRESS"></span>*ObjectAddress*  
Specifies the address of the object to be notified.

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>*Value*  
Specifies the notification value.

### <span id="displaying_the_object_count_table"></span><span id="DISPLAYING_THE_OBJECT_COUNT_TABLE"></span>Displaying the Object Count Table

The **dc** command displays the memory object count table.

**dc**

### <span id="accessing_memory"></span><span id="ACCESSING_MEMORY"></span>Accessing Memory

The memory access commands allow you to read and write to memory. When reading memory, you can choose the size of the memory units with the **db**, **dw**, **dd** or **da** command. A simple **d** command displays memory in the most recently-chosen units. If this is the first display command used, byte units are used.

If no address or method is specified, display will begin where the previous display command ended.

These commands have the same effect as the standard kernel debugger memory commands; they are duplicated within the AMLI Debugger for easy access.

**d\[b|w|d|a\] \[ \[l=**<em>Length</em>**\] \[** *Method* **| \[%%\]**<em>Address</em> **\] \]**

**e \[%%\]**<em>Address Datalist</em>

<span id="b"></span><span id="B"></span>**b**  
Specifies that the data should be displayed in byte units.

<span id="w"></span><span id="W"></span>**w**  
Specifies that the data should be displayed in word (16-bit) units.

<span id="d"></span><span id="D"></span>**d**  
Specifies that the data should be displayed in DWORD (32-bit) units.

<span id="a"></span><span id="A"></span>**a**  
Specifies that the data should be displayed as a string. The data is displayed as ASCII characters. The display terminates when a NULL character is read, or when *Length* characters have been displayed.

<span id="Length"></span><span id="length"></span><span id="LENGTH"></span>*Length*  
Specifies the number of bytes to be displayed. *Length* must be a hexadecimal number (without an **0x** prefix). If *Length* is omitted, the default display size is 0x80 bytes.

<span id="Method"></span><span id="method"></span><span id="METHOD"></span>*Method*  
Specifies the full path and name of a method. The display will start at the beginning of this method's memory location.

<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>*Address*  
Specifies the memory address where reading or writing will begin. If the address is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address.

<span id="DataList"></span><span id="datalist"></span><span id="DATALIST"></span>*DataList*  
Specifies the data to be written to memory. Each item in the list can be either a hexadecimal byte or a string. When a string is used, it must be enclosed in quotation marks. Multiple items should be separated by spaces.

### <span id="accessing_ports"></span><span id="ACCESSING_PORTS"></span>Accessing Ports

The port commands allow you to send output or receive input from a data port. The **i** and **o** commands transfer single bytes, the **iw** and **ow** commands transfer words (16 bits), and the **id** and **od** commands transfer DWORDS (32 bits).

These commands have the same effect as the standard kernel debugger port commands; they are duplicated within the AMLI Debugger for easy access.

**i** *Port*

**iw** *Port*

**id** *Port*

**o** *Port* *DataForPort*

**ow** *Port* *DataForPort*

**od** *Port* *DataForPort*

<span id="Port"></span><span id="port"></span><span id="PORT"></span>*Port*  
Specifies the address of the port to be accessed. The port size must match the command chosen.

<span id="DataForPort"></span><span id="dataforport"></span><span id="DATAFORPORT"></span>*DataForPort*  
Specifies the data to be written to the port. The size of this data must match the command chosen.

### <span id="displaying_help"></span><span id="DISPLAYING_HELP"></span>Displaying Help

This command displays help text for the AMLI Debugger commands.

**? \[**<em>Command</em>**\]**

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*  
Specifies the command for which to display help. If this is omitted, a list of all AMLI Debugger commands and AMLI Debugger extensions is displayed.

## See Also

[The AMLI Debugger](the-amli-debugger.md) 
