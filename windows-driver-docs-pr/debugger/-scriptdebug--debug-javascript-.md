---
title: .scriptdebug (Debug JavaScript)
description: Use the .scriptdebug command to debug JavaScript scripts.
keywords: [".scriptdebug Debug JavaScript Windows Debugging"]
ms.date: 02/02/2021
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .scriptdebug (Debug JavaScript)
api_type:
- NA
---

# .scriptdebug (Debug JavaScript)

Use the **.scriptdebug** command to debug JavaScript scripts.

```dbgcmd
.scriptdebug FileName
```

### Parameters

*FileName*

Specifies the name of the debugger JavaScript script to debug.

### <span id="Environment"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>



## <span id="Additional_Information"></span>Additional Information

For an overview of JavaScript debugging, see  [JavaScript Debugger Scripting - JavaScript Debugging](javascript-debugger-scripting.md#DEBUGGING).

>[!NOTE] 
> To use JavaScript Debugging with WinDbg Preview, run the debugger as Administrator.
>


## Remarks

Before you debug a JavaScript completed the following steps.

1. Load the sample script.

    ```dbgcmd
    0:000> .scriptload C:\MyScripts\DebuggableSample.js
    ```

To start actively debugging the script use the **.scriptdebug** command.

```dbgcmd
0:000> .scriptdebug C:\MyScripts\DebuggableSample.js
>>> ****** DEBUGGER ENTRY DebuggableSample ******
           No active debug event!

>>> Debug [DebuggableSample <No Position>] >
```

Once you see the prompt *>>> Debug [DebuggableSample <No Position>] >* and a request for input, you are
inside the script debugger.  

Use the **.help** command or **?** to display a list of commands in the JavaScript debugging environment.

```dbgcmd
>>> Debug [DebuggableSample <No Position>] >.help
Script Debugger Commands (*NOTE* IDs are **PER SCRIPT**):
    ? .................................. Get help
    ? <expr>  .......................... Evaluate expression <expr> and display result
    ?? <expr>  ......................... Evaluate expression <expr> and display result
    |  ................................. List available scripts
    |<scriptid>s  ...................... Switch context to the given script
    bc <bpid>  ......................... Clear breakpoint by specified <bpid>
    bd <bpid>  ......................... Disable breakpoint by specified <bpid>
    be <bpid>  ......................... Enable breakpoint by specified <bpid>
    bl  ................................ List breakpoints
    bp <line>:<column>  ................ Set breakpoint at the specified line and column
    bp <function-name>  ................ Set breakpoint at the (global) function specified by the given name
    bpc  ............................... Set breakpoint at current location
    dv  ................................ Display local variables of current frame
    g  ................................. Continue script
    gu   ............................... Step out
    k  ................................. Get stack trace
    p  ................................. Step over
    q  ................................. Exit script debugger (resume execution)
    sx  ................................ Display available events/exceptions to break on
    sxe <event>  ....................... Enable break on <event>
    sxd <event>  ....................... Disable break on <event>
    t  ................................. Step in
    .attach <scriptId>  ................ Attach debugger to the script specified by <scriptId>
    .detach [<scriptId>]  .............. Detach debugger from the script specified by <scriptId>
    .frame <index>  .................... Switch to frame number <index>
    .f+  ............................... Switch to next stack frame
    .f-  ............................... Switch to previous stack frame
    .help  ............................. Get help
```


### Events

Use the **sx** script debugger command to see the list of events that can be trapped.

```dbgcmd
>>> Debug [DebuggableSample <No Position>] >sx              
sx                                                          
    ab  [   inactive] .... Break on script abort            
    eh  [   inactive] .... Break on any thrown exception    
    en  [   inactive] .... Break on entry to the script     
    uh  [     active] .... Break on unhandled exception     
```

Use the **sxe** script debugger command to enable any of the break behaviors. For example to turn on break on entry so that the script will trap into the script debugger as soon as any code within it executes, use this command.

```dbgcmd
>>> Debug [DebuggableSample <No Position>] >sxe en          
sxe en                                                      
Event filter 'en' is now active                             
```

Use the **sxd** script debugger command to disable any of the breakpoint behaviors.

```dbgcmd                                                                                                                      
>>> Debug [DebuggableSample 34:5] >sxd en                                                                              
sxd en                                                                                                                 
Event filter 'en' is now inactive                                                                                      
```

### Stack trace

Use the **k** command to display a stack trace.

```dbgcmd
>>> Debug [DebuggableSample 34:5] >k                                                  
k                                                                                     
    ##  Function                         Pos    Source Snippet                        
-> [00] throwAndCatch                    034:05 (var curProc = host.currentProcess)   
   [01] outer                            066:05 (var foo = throwAndCatch())           
   [02] outermost                        074:05 (var result = outer())                
```

### Enumerating variables

Use **??** to enumerate the values of JavaScript variables.

```dbgcmd
>>> Debug [DebuggableSample 34:5] >??someObj                
??someObj                                                   
someObj          : {...}                                    
    __proto__        : {...}                                
    a                : 0x63                                 
    b                : {...}                                
```


### Breakpoints

Use the following breakpoint commands to work with additional breakpoints.


**bp <bpid>**: Set a breakpoint

**bd <bpid>**: Disable the breakpoint

**be <bpid>**: Enable the breakpoint

**bc <bpid>**: Clear the breakpoint

**bpc**: Set breakpoint on current line

**bl**: List the breakpoint(s)


### Flow control - navigation

Use the following commands to move forward in the script.

**p**: Step over

**t**: Step in

**g**: Continue script

**gu**: Step out




### Frames

Use the following commands to work with frames.


**.frame <index>**: Switch to frame number <index>

**.f+**: Switch to next stack frame

**.f+**: Switch to previous stack frame


### Quiting

Use the **.detach** command to detach the JavaScript debugger. 

```dbgcmd
>>> Debug [DebuggableSample 34:5] >.detach                  
.detach                                                     
Debugger has been detached from script!                     
```

Use the **q** command to quit the JavaScript debugger. 

```dbgcmd
>>> Debug [<NONE> ] >q                                      
q                                                           
```

