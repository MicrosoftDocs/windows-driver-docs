---
title: wmitrace.setprefix
description: The wmitrace.setprefix extension specifies the trace message prefix that is prepended to the trace messages from this session. 
ms.assetid: 8712af44-f231-48f6-97ac-56a1d737cd6b
keywords: ["wmitrace.setprefix Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.setprefix
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.setprefix


The **!wmitrace.setprefix** extension specifies the trace message prefix that is prepended to the trace messages from this session. This extension allows you to change the prefix during the debugging session.

```dbgcmd
!wmitrace.setprefix [+] PrefixVariables 
!wmitrace.setprefix 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="______________"></span> **+**   
Causes *PrefixVariables* to be apended to the trace message prefix. If the **+** token is not used, *PrefixVariables* replaces the existing trace message prefix.

<span id="_______PrefixVariables______"></span><span id="_______prefixvariables______"></span><span id="_______PREFIXVARIABLES______"></span> *PrefixVariables*   
A set of variables that specifies the format and data in the trace message prefix.

The variables have the format %n!x!, where %n represents a data field and !x! represents the data type. You can also include separation characters, such as colons (:), semicolons (;), parentheses ( ( ) ), braces ( { } ), and brackets ( \[ \] ) to separate the fields.

Each %n variable represents a parameter that is described in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Prefix variable identifier</th>
<th align="left">Variable type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>%1</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The friendly name of the message GUID of the trace message. By default, the friendly name of a message GUID is the name of the directory in which the trace provider was built.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%2</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Source file and line number.</p>
<p>This variable represents the friendly name of the trace message. By default, the friendly name of a trace message is the name of the source file and the line number of the code that generated the trace message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%3</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>Thread ID.</p>
<p>Identifies the thread that generated the trace message.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%4</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Time stamp of the time that the trace message was generated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%5</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Kernel time.</p>
<p>Displays the elapsed execution time for kernel-mode instruction, in CPU ticks, at the time that the trace message was generated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%6</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>User time.</p>
<p>Displays the elapsed execution time for user-mode instruction, in CPU ticks, at the time that the trace message was generated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%7</p></td>
<td align="left"><p>LONG</p></td>
<td align="left"><p>Sequence number.</p>
<p>Displays the local or global sequence number of the trace message. Local sequence numbers, which are unique only to this trace session, are the default.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%8</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>Process ID.</p>
<p>Identifies the process that generated the trace message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%9</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>CPU number.</p>
<p>Identifies the CPU on which the trace message was generated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!FUNC!</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Function name.</p>
<p>Displays the name of the function that generated the trace message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!FLAGS%</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Displays the name of the trace flags that enable the trace message.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!LEVEL!</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Displays the value of the trace level that enables the trace message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%!COMPNAME!</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Component name.</p>
<p>Displays the name of the component of the provider that generated the trace message. The component name appears only if it is specified in the tracing code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%!SUBCOMP!</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Subcomponent name.</p>
<p>Displays the name of the subcomponent of the provider that generated the trace message. The subcomponent name appears only if it is specified in the tracing code.</p></td>
</tr>
</tbody>
</table>

 

The symbol within exclamation marks is a conversion character that specifies the format and precision of the variable. For example, %8!04X! specifies the process ID formatted as a four-digit, unsigned, hexadecimal number.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

### <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example

The following command changes the trace message prefix in the debugger output to the following format:

**!wmitrace.setprefix %2!s!: %!FUNC!: %8!04x!.%3!04x!: %4!s!:**

This extension command sets the trace message prefix to the following format:

*SourceFile\_LineNumber: FunctionName: ProcessID.ThreadID: SystemTime:*

As a result, the trace messages are prepended with the specified information in the specified format. The following code example is taken from a trace of the Tracedrv sample driver in the WDK.

```dbgcmd
tracedrv_c258: TracedrvDispatchDeviceControl: 0af4.0c64: 07/25/2003-13:55:39.998:  IOCTL = 1
```

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK documentation. For information about trace message format files, see the "Trace Message Prefix" topic in the WDK documentation.

Remarks
-------

When used with no parameters, **!wmitrace.setprefix** displays the current value of the trace message prefix.

The *trace message prefix* consists of data about the trace message that is prepended to each trace message during Windows software trace preprocessor (WPP) software tracing. This data originates in the trace log (.etl) file and the trace message format (.tmf) file. You can customize the format and data in trace message prefix.

The default trace message prefix is as follows:

```dbgcmd
[%9!d!]%8!04X!.%3!04X!::%4!s! [%1!s!]
```

and produces the following prefix:

```dbgcmd
[CPUNumber]ProcessID.ThreadID::SystemTime [ProviderDirectory] 
```

You can change the format and data in the trace message prefix outside of the debugger by setting the %TRACE\_FORMAT\_PREFIX% environment variable. For an example that illustrates how to set the trace message prefix outside of the debugger, see "Example 7: Customizing the Trace Message Prefix" in the Windows Driver Kit (WDK) documentation. If the trace message prefix of your messages varies from the default, this environment variable might be set on your computer.

The prefix that you set by using this extension command affects only the debugger output. The trace message prefix that appears in the trace log is determined by the default value and the value of the %TRACE\_FORMAT\_PREFIX% environment variable.

This extension is only useful during WPP software tracing, and earlier (legacy) methods of Event Tracing for Windows. Trace events that are produced by other manifested providers do not use trace message format (TMF) files, and therefore this extension does not affect them.

 

 





