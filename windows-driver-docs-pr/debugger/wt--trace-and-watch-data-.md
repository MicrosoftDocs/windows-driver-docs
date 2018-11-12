---
title: wt (Trace and Watch Data)
description: The wt command runs through the whole function and then displays statistics, when you execute this command at the beginning of a function call.
ms.assetid: 2dd62a7f-67d9-4b13-b04e-5cd02e6ef9f0
keywords: ["wt (Trace and Watch Data) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wt (Trace and Watch Data)
api_type:
- NA
ms.localizationpriority: medium
---

# wt (Trace and Watch Data)


The **wt** command runs through the whole function and then displays statistics, when you execute this command at the beginning of a function call.

```dbgcmd
wt [WatchOptions] [= StartAddress] [EndAddress] 
```

## <span id="ddk_cmd_trace_and_watch_data_dbg"></span><span id="DDK_CMD_TRACE_AND_WATCH_DATA_DBG"></span>Parameters


<span id="_______WatchOptions______"></span><span id="_______watchoptions______"></span><span id="_______WATCHOPTIONS______"></span> *WatchOptions*   
Specifies how to modify the display. You can use any of the following options.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>-l</strong> <em>Depth</em></p></td>
<td align="left"><p>(User mode only) Specifies the maximum depth of the calls to display. Any calls that are at least <em>Depth</em> levels deeper than the starting point are executed silently.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-m</strong> <em>Module</em></p></td>
<td align="left"><p>(User mode only) Restricts the display to code inside the specified module, plus the first level of calls made from that module. You can include multiple -m options to display code from multiple modules and no other modules.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-i</strong> <em>Module</em></p></td>
<td align="left"><p>(User mode only) Ignores any code within the specified module. You can include multiple -i options to ignore code from multiple modules. If you use a -m option, the debugger ignores all -i options.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-ni</strong></p></td>
<td align="left"><p>(User mode only) Does not display any entry into code that is being ignored because of an -m or -i option.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-nc</strong></p></td>
<td align="left"><p>Does not display individual call information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-ns</strong></p></td>
<td align="left"><p>Does not display summary information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-nw</strong></p></td>
<td align="left"><p>Does not display warnings during the trace.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-oa</strong></p></td>
<td align="left"><p>(User mode only) Displays the actual address of call sites.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>-or</strong></p></td>
<td align="left"><p>(User mode only) Displays the return register values of the called function, using the default radix as the base.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-oR</strong></p></td>
<td align="left"><p>(User mode only) Displays the return register values of the called function, in the appropriate type for each return value.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger begins execution. If you do not use *StartAddress*, execution begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______EndAddress______"></span><span id="_______endaddress______"></span><span id="_______ENDADDRESS______"></span> *EndAddress*   
Specifies the address where tracing ends. If you do not use *EndAddress*, a single instruction or function call is executed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p></p>
<strong>User mode:</strong> all
<strong>Kernel mode:</strong> x86-based only</td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about issuing the **wt** command and an overview of related commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

The **wt** command is useful if you want information about the behavior of a specific function, but you do not want to step through the function. Instead, go to the beginning of that function and then issue the **wt** command.

If the program counter is at a point that corresponds to a symbol (such as the beginning of a function or entry point into a module), the **wt** command traces until it reaches the current return address. If the program counter is on a **call** instruction, the **wt** command traces until it returns to the current location. This tracing is profiled in the [Debugger Command window](debugger-command-window.md) together with output that describes the various calls that the command encounters.

If the **wt** command is issued somewhere other than the beginning of a function, the command behaves like the [**p (Step)**](p--step-.md) command. However, if you specify *EndAddress*, execution continues until that address is reached, even if this execution involves many program steps and function calls.

When you are debugging in source mode, you should trace into the function only to the point where you see the opening bracket of the function body. Then, you can use the **wt** command. (It is typically easier to insert a breakpoint at the first line of the function, or use [Debug | Run to Cursor](debug---run-to-cursor.md), and then use the **wt** command.)

Because the output from **wt** can be long, you might want to use a log file to record your output.

The following example shows a typical log file.

```dbgcmd
0:000> l+                  Source options set to show source lines
Source options are f:
     1/t - Step/trace by source line
     2/l - List source line for LN and prompt
     4/s - List source code at prompt
     8/o - Only show source code at prompt
0:000> p                   Not yet at the function call: use "p"
>  44:       minorVariableOne = 12;
0:000> p
>  45:       variableOne = myFunction(2, minorVariable);
0:000> t                   At the function call: now use "t"
MyModule!ILT+10(_myFunction):
0040100f e9cce60000      jmp     MyModule!myFunction (0040f6e0)
0:000> t
>  231:    { 
0:000> wt                  At the function beginning:  now use "wt"
Tracing MyModule!myFunction to return address 00401137

  105     0 [  0] MyModule!myFunction
    1     0 [  1]   MyModule!ILT+1555(_printf)
    9     0 [  1]   MyModule!printf
    1     0 [  2]     MyModule!ILT+370(__stbuf)
   11     0 [  2]     MyModule!_stbuf
    1     0 [  3]       MyModule!ILT+1440(__isatty)
   14     0 [  3]       MyModule!_isatty
   50    15 [  2]     MyModule!_stbuf
   17    66 [  1]   MyModule!printf
    1     0 [  2]     MyModule!ILT+980(__output)
   59     0 [  2]     MyModule!_output
   39     0 [  3]       MyModule!write_char
  111    39 [  2]     MyModule!_output
   39     0 [  3]       MyModule!write_char

....

   11     0 [  5]           kernel32!__SEH_epilog4
   54 11675 [  4]         kernel32!ReadFile
  165 11729 [  3]       MyModule!_read
  100 11895 [  2]     MyModule!_filbuf
   91 11996 [  1]   MyModule!fgets
54545 83789 [  0] MyModule!myFunction
    1     0 [  1]   MyModule!ILT+1265(__RTC_CheckEsp)
    2     0 [  1]   MyModule!_RTC_CheckEsp
54547 83782 [  0] MyModule!myFunction

112379 instructions were executed in 112378 events (0 from other threads)

Function Name                               Invocations MinInst MaxInst AvgInst
MyModule!ILT+1265(__RTC_CheckEsp)                     1       1       1       1
MyModule!ILT+1440(__isatty)                          21       1       1       1
MyModule!ILT+1540(__ftbuf)                           21       1       1       1
....
ntdll!memcpy                                         24       1      40      19
ntdll!memset                                          2      29      29      29

23 system calls were executed

Calls  System Call
   23  ntdll!KiFastSystemCall
```

In the listing of the trace, the first number specifies the number of instructions that were executed, the second number specifies the number of instructions executed by child processes of the function, and the third number (in brackets) specifies the depth of the function in the stack (taking the initial function as zero). The indentation of the function name shows the call depth.

In the preceding example, **MyModule!myFunction** executes 105 instructions before it calls several subroutines, including **printf** and **fgets**, and then executes 54545 additional instructions after calling those functions, but before issuing a few more calls. However, in the final count, the display shows that **myFunction** executes 112,379 instructions, because this count includes all of the instructions that **myFunction** and its children execute. (The *children* of **myFunction** are functions that are called from **myFunction**, either directly or indirectly.)

In the preceding example, note also that **ILT+1440 (\_\_isatty)** is called 21 times. In the final count, the summary of this function's behavior shows the number of times that it was called, the smallest number of instructions in any single execution, the largest number of instructions in any single execution, and the average number of instructions per execution.

If any system calls are made, they appear in the counter and are listed again at the end of the command output.

 

 





