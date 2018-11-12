---
title: .scriptdebug (Debug JavaScript)
description: Use the .scriptdebug command to debug JavaScript scripts.
keywords: [".scriptdebug Debug JavaScript Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 12/28/2017
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

```
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


Remarks
-------

Before you debug a JavaScript completed the following steps.

1. Load the JavaScript scripting provider using the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command. 

    ```
    0:000> .load jsprovider.dll
    ```

2. Load the sample script.

    ```
    0:000> .scriptload C:\MyScripts\DebuggableSample.js
    ```

To start actively debugging the script use the **.scriptdebug** command.

```
0:000> .scriptdebug C:\MyScripts\DebuggableSample.js
>>> ****** DEBUGGER ENTRY DebuggableSample ******
           No active debug event!

>>> Debug [DebuggableSample <No Position>] >
```

Once you see the prompt *>>> Debug [DebuggableSample <No Position>] >* and a request for input, you are
inside the script debugger.  

Use the **.help** command or **?** to display a list of commands in the JavaScript debugging environment.

```
>>> Debug [DebuggableSample <No Position>] >.help
Script Debugger Commands (*NOTE* IDs are **PER SCRIPT**):
    ? .................................. Get help
    ? <expr>  .......................... Evaluate expression <expr> and display result
    ?? <expr>  ......................... Evaluate expression <expr> and display result
    |  ................................. List available scripts
    |<scriptid>s  ...................... Switch context to the given script
    bc <bpid>  ......................... Clear breakpoint by specifed <bpid>
    bd <bpid>  ......................... Disable breakpoint by specifed <bpid>
    be <bpid>  ......................... Enable breakpoint by specifed <bpid>
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

```
>>> Debug [DebuggableSample <No Position>] >sx              
sx                                                          
    ab  [   inactive] .... Break on script abort            
    eh  [   inactive] .... Break on any thrown exception    
    en  [   inactive] .... Break on entry to the script     
    uh  [     active] .... Break on unhandled exception     
```

Use the **sxe** script debugger command to enable any of the break beahaviors. For example to turn on break on entry so that the script will trap into the script debugger as soon as any code within it executes, use this command.

```
>>> Debug [DebuggableSample <No Position>] >sxe en          
sxe en                                                      
Event filter 'en' is now active                             
```

Use the **sxd** script debugger command to disable any of the breakpoint behaviors.

```                                                                                                                      
>>> Debug [DebuggableSample 34:5] >sxd en                                                                              
sxd en                                                                                                                 
Event filter 'en' is now inactive                                                                                      
```

### Stack trace

Use the **k** command to display a stack trace.

```
>>> Debug [DebuggableSample 34:5] >k                                                  
k                                                                                     
    ##  Function                         Pos    Source Snippet                        
-> [00] throwAndCatch                    034:05 (var curProc = host.currentProcess)   
   [01] outer                            066:05 (var foo = throwAndCatch())           
   [02] outermost                        074:05 (var result = outer())                
```

### Enumerating variables

Use **??** to enumerate the values of JavaScript variables.

```
>>> Debug [DebuggableSample 34:5] >??someObj                
??someObj                                                   
someObj          : {...}                                    
    __proto__        : {...}                                
    a                : 0x63                                 
    b                : {...}                                
```


### Breakpoints

Use the following breakpoint commands to work with additional breakpoints.


|           |                                |
|-----------|--------------------------------|
| bp <bpid> |        Set a breakpoint        |
| bd <bpid> |     Disable the breakpoint     |
| be <bpid> |     Enable the breakpoint      |
| bc <bpid> |      Clear the breakpoint      |
|    bpc    | Set breakpoint on current line |
|    bl     |     List the breakpoint(s)     |

### Flow control - navigation

Use the following commands to move forward in the script.

|   |                           |
|---|---------------------------|
|p  | Step over                 |
|t  | Step in                   |
|g  | Continue script           |
|gu | Step out                  |



### Frames

Use the following commands to work with frames.


|                |                                |
|----------------|--------------------------------|
| .frame <index> | Switch to frame number <index> |
|      .f+       |   Switch to next stack frame   |
|      .f+       | Switch to previous stack frame |

### Quiting

Use the **.detach** command to detach the JavaScript debugger. 

```
>>> Debug [DebuggableSample 34:5] >.detach                  
.detach                                                     
Debugger has been detached from script!                     
```

Use the **q** command to quit the JavaScript debugger. 

```
>>> Debug [<NONE> ] >q                                      
q                                                           
```




[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger/debugger]:%20.crash%20%28Force%20System%20Crash%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




