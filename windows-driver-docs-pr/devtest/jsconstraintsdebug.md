---
title: JSConstraintsDebug
description: JSConstraintsDebug (JSConstraintsDebug.exe) is a command-line tool that provides debugging support for JavaScript Constraints while developing a V4 printer driver.
ms.assetid: 48C39A2C-7EA6-4BAA-B5E8-3B426C9697B3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# JSConstraintsDebug


JSConstraintsDebug (JSConstraintsDebug.exe) is a command-line tool that provides debugging support for [JavaScript Constraints](https://msdn.microsoft.com/library/windows/hardware/jj218731) while developing a [V4 printer driver](https://msdn.microsoft.com/library/windows/hardware/hh706306).

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Where can I download JSConstraintsDebug?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>JSConstraintsDebug.exe is included in the Microsoft Windows Driver Kit (WDK). For information about getting the WDK, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=808351" data-raw-source="[Windows Driver Kit downloads](http://go.microsoft.com/fwlink/p/?LinkId=808351)">Windows Driver Kit downloads</a>.</p></td>
</tr>
</tbody>
</table>

 

The tool executes each of the following relevant entry point APIs on the JavaScript constraints of the targeted driver against the user provided print ticket:

[**PTGetPrintCapabilities**](https://msdn.microsoft.com/library/windows/desktop/dd162881)

[**PTConvertDevModeToPrintTicket**](https://msdn.microsoft.com/library/windows/desktop/dd162879)

[**TConvertPrintTicketToDevMode**](https://msdn.microsoft.com/library/windows/desktop/dd162880)

[**PTMergeAndValidatePrintTicket**](https://msdn.microsoft.com/library/windows/desktop/dd162884)

During execution the tool will prompt for an appropriate IDE debugger such as Visual Studio. Upon selection, the constraints source code will be opened and stopped at a JavaScript debugger statement.

To debug JS constraints files, follow these steps:

1.  Open a Command Prompt window.

2.  Run the JSConstraintsDebug.exe tool and specify, at minimum, the printer name and the path to a test print ticket.

3.  Choose the debugging tool you wish to use.

## <span id="Running_JSConstraintsDebug_in_user_mode"></span><span id="running_jsconstraintsdebug_in_user_mode"></span><span id="RUNNING_JSCONSTRAINTSDEBUG_IN_USER_MODE"></span>Running JSConstraintsDebug in user mode


Elevated privileges are required to enable debugging of JS functions. To run in user mode, the following registry key must be set prior to executing JSConstraintsDebug.exe:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Key name</p></td>
<td align="left"><p>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print</p></td>
</tr>
<tr class="even">
<td align="left"><p>Value name</p></td>
<td align="left"><p>EnableJavaScriptDebugging</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Type</p></td>
<td align="left"><p>DWORD</p></td>
</tr>
<tr class="even">
<td align="left"><p>Value</p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

## <span id="JavaScript_debugger_statements"></span><span id="javascript_debugger_statements"></span><span id="JAVASCRIPT_DEBUGGER_STATEMENTS"></span>JavaScript debugger statements


Breakpoints can be created in JavaScript source by using the debugger statement. This will pause operation in Visual Studio all allow for step-by-step debugging. These statements can be inserted in any of the [JavaScript Constraint APIs](http://go.microsoft.com/fwlink/p/?LinkId=808350).

For example:

```JavaScript
function validatePrintTicket(PrintTicket, scriptContext)
{
    debugger; // debug tool will pause at this breakpoint
    ...
}
```

## <span id="JSConstraintsDebug_Command_Syntax"></span><span id="jsconstraintsdebug_command_syntax"></span><span id="JSCONSTRAINTSDEBUG_COMMAND_SYNTAX"></span>JSConstraintsDebug Command Syntax


```
JSConstraintsDebug <PrinterName> <PrintTicket> [MergePrintTicket] [Constraints]
```

## <span id="Command_parameters"></span><span id="command_parameters"></span><span id="COMMAND_PARAMETERS"></span>Command parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameters</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="PrinterName"></span><span id="printername"></span><span id="PRINTERNAME"></span>PrinterName</p></td>
<td align="left"><p>Required. Specifies the string name of a print driver which contains JS constraints source file. This driver will be used for all debugging operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PrintTicket"></span><span id="printticket"></span><span id="PRINTTICKET"></span>PrintTicket</p></td>
<td align="left"><p>Required. Specifies the path and name of a print ticket XML file to be validated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MergePrintTicket"></span><span id="mergeprintticket"></span><span id="MERGEPRINTTICKET"></span>MergePrintTicket</p></td>
<td align="left"><p>Optional. Specifies the path and name of a print ticket XML file which will be used to validate a merge operation.</p>
<p>If this parameter is not set the default DevMode will be converted to a Print Ticket and will be passed to the Merge and Validate API.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Constraints"></span><span id="constraints"></span><span id="CONSTRAINTS"></span>Constraints</p></td>
<td align="left"><p>Optional. Specifies the path and name of a JavaScript constraints file which will replace the existing constraints source file found in targeted printer driver before debugging.</p></td>
</tr>
</tbody>
</table>

 

**Note**  Specifying a constraints file with the Constraints parameter will overwrite existing source code in the targeted driver.

 

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


Debug a print driver against a known test print ticket.

```
JSConstraintsDebug “Contoso Printer” PrintTicket.xml
```

Debug a print driver with a new constraints source file against a known test print ticket.

```
JSConstraintsDebug “Contoso Printer” PrintTicket.xml Constraints.js
```

Test merge and validate operations between two custom print tickets.

```
JSConstraintsDebug “Contoso Printer” PrintTicket.xml PrintTicket2.xml
```

 

 





