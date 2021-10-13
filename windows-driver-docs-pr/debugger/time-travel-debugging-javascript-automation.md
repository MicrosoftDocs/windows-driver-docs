---
title: Time Travel Debugging - JavaScript Automation
description: This section describes how to use JavaScript automation to work with TTD traces.
ms.date: 09/17/2020
ms.localizationpriority: medium
---

# Time Travel Debugging - JavaScript Automation

![Small time travel logo showing clock.](images/ttd-time-travel-debugging-logo.png)

You can use JavaScript automation to work with TTD traces in a number of ways, such as command automation or using queries to locate event data from the trace file.

For general information about working with JavaScript see [JavaScript Debugger Scripting](javascript-debugger-scripting.md). There are also [JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md).

## JavaScript TTD Command Automation

One way to use JavaScript for TTD automation, is to send commands to automate working with time travel trace files.

### Moving in a trace file

This JavaScript shows how to move to the start of a time travel trace using the [!tt](time-travel-debugging-extension-tt.md) command.

```javascript
var dbgControl = host.namespace.Debugger.Utility.Control;  
dbgControl.ExecuteCommand("!tt 0",false);
host.diagnostics.debugLog(">>> Sent command to move to the start of the TTD file \n");
```

We can make this into a ResetTrace function, and save it as ResetTrace.js, using the JavaScript UI in WinDbg Preview.

```javascript
// WinDbg TTD JavaScript ResetTraceCmd Sample

"use strict";

function ResetTraceCmd()
{
    var dbgControl = host.namespace.Debugger.Utility.Control;  
    dbgControl.ExecuteCommand("!tt 0",false);
    host.diagnostics.debugLog(">>> Sent command to move to the start of the TTD file \n");
}
```

After a TTD file is loaded in WinDbg Preview, call the function ResetTraceCmd() function using the dx command in the debugger command window.

```dbgcmd
0:000> dx Debugger.State.Scripts.ResetTrace.Contents.ResetTraceCmd()
>>> Sent command to move to the start of the TTD file
Debugger.State.Scripts.ResetTrace.Contents.ResetTrace()
```

## Limitations of sending commands

But for all but the simplest situations, the approach of sending commands has drawbacks. It relies on the use  of text output. And parsing that output leads to code that is brittle and hard to maintain. A better approach is to use the TTD objects directly.

The following example shows how to use the objects directly to complete the same task using the objects directly.

```javascript
// WinDbg TTD JavaScript ResetTrace Sample

"use strict";

function ResetTrace()
{
    host.currentProcess.TTD.SetPosition(0);
    host.diagnostics.debugLog(">>> Set position to the start of the TTD file \n");
}

```

Running this code shows that we are able to move to the start of the trace file.

```dbgcmd
0:000> dx Debugger.State.Scripts.ResetTrace.Contents.ResetTrace()
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: F:0
>>> Set position to the start of the TTD file
```

In this example ResetTraceEnd function, the position is set to the end of the trace and the current and new position is displayed using the [currentThread.TTD](time-travel-debugging-thread-objects.md) Position object.

```javascript

// WinDbg TTD JavaScript Sample to Reset Trace using objects directly
// and display current and new position

function ResetTraceEnd()
{
   var PositionOutputStart = host.currentThread.TTD.Position;
   host.diagnostics.debugLog(">>> Current position in trace file:  "+ PositionOutputStart +"\n");
   host.currentProcess.TTD.SetPosition(100);
   var PositionOutputNew = host.currentThread.TTD.Position;
   host.diagnostics.debugLog(">>> New position in trace file:  "+ PositionOutputNew +"\n");
}
```

Running this code displays the current and new position.


```dbgcmd
0:000> dx Debugger.State.Scripts.ResetTrace.Contents.ResetTraceEnd()
>>> Current position in trace file:  F:0
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: D3:1
>>> New position in trace file:  D3:1
```

In this expanded sample, the starting and ending position values are compared to see if the position in the trace changed.

```javascript
// WinDbg TTD JavaScript ResetTraceEx Sample

"use strict";

function ResetTraceEx()
{
    const PositionOutputStart = host.currentThread.TTD.Position;
    host.diagnostics.debugLog(">>> Current position in trace file:  "+ PositionOutputStart +"\n");
  
    host.currentProcess.TTD.SetPosition(0);

    const PositionOutputNew = host.currentThread.TTD.Position;
    host.diagnostics.debugLog(">>> New position in trace file:  "+ PositionOutputNew +"\n");

    if (parseInt(PositionOutputStart,16) != parseInt(PositionOutputNew,16))
    {
        host.diagnostics.debugLog(">>> Set position to the start of the TTD file  \n");
    }
    else
    {
        host.diagnostics.debugLog(">>> Position was already set to the start of the TTD file \n");
    }
}

```

In this example run, a message is displayed that we were all ready at the start of the trace file.

```dbgcmd
0:000> dx Debugger.State.Scripts.ResetTrace.Contents.ResetTraceEx()
>>> Current position in trace file:  F:0
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: F:0
>>> New position in trace file:  F:0
>>> Position was already set to the start of the TTD file
```

To test the script use the [!tt](time-travel-debugging-extension-tt.md) command to navigate half way in the trace file.

```dbgcmd
0:000> !tt 50
Setting position to 50% into the trace
Setting position: 71:0
```

Running the script now displays the proper message that indicates that the position was set to the start of the TTD trace.

```dbgcmd
0:000> dx Debugger.State.Scripts.ResetTrace.Contents.ResetTraceEx()
>>> Current position in trace file:  71:0
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: F:0
>>> New position in trace file:  F:0
>>> Set position to the start of the TTD file  
```

## Indexing a time travel trace file

If just a trace file is copied over to a different PC, it will need to be re-indexed. For more information, see [Time Travel Debugging - Working with Trace Files](time-travel-debugging-trace-file-information.md).

This code shows an example IndexTrace function that displays how long it takes to re-index a trace file.

```javascript
function IndexTrace()
{
    var timeS = (new Date()).getTime();
    var output = host.currentProcess.TTD.Index.ForceBuildIndex();
    var timeE = (new Date()).getTime();
    host.diagnostics.debugLog("\n>>> Trace was indexed in " + (timeE - timeS) + " ms\n");
}

```

Here is the output from a small trace file.

```dbgcmd
0:000> dx Debugger.State.Scripts.TTDUtils.Contents.IndexTrace()

>>> Trace was indexed in 2 ms
```

### Adding a try catch statement

To check to see if errors were raised when the indexing was run, enclose the indexing code in a try catch statement.

```javascript

function IndexTraceTry()
{
    var timeS = (new Date()).getTime();
    try
    {
         var IndexOutput =  host.currentProcess.TTD.Index.ForceBuildIndex();
         host.diagnostics.debugLog("\n>>> Index Return Value: " + IndexOutput + "\n");
         var timeE = (new Date()).getTime();
         host.diagnostics.debugLog("\n>>> Trace was successfully indexed in " + (timeE - timeS) + " ms\n");
     }

    catch(err)
    {
         host.diagnostics.debugLog("\n>>> Index Failed! \n");
         host.diagnostics.debugLog("\n>>> Index Return Value: " + IndexOutput + "\n");
         host.diagnostics.debugLog("\n>>> Returned error: " + err.name + "\n");
    }
}

```

Here is the script output if the indexing is successful.

```dbgcmd
0:000> dx Debugger.State.Scripts.TTDUtils.Contents.IndexTraceTry()

>>> Index Return Value: Loaded

>>> Trace was successfully indexed in 1 ms
```

If the trace can not be indexed, for example if the trace is not loaded in the debugger, the catch loop code is run.

```dbgcmd
0:007> dx Debugger.State.Scripts.TTDUtils.Contents.IndexTraceTry()

>>> Index Failed!

>>> Index Return Value: undefined

>>> Returned error: TypeError
```

## JavaScript TTD Objects Queries

A more advanced use of JavaScript and TTD is to query the time travel objects to locate specific calls or events that have occurred in the trace. For more information about the TTD objects see:

[Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Native Debugger Objects in JavaScript Extensions - Debugger Object Details](native-objects-in-javascript-extensions-debugger-objects.md)

The [dx](dx--display-visualizer-variables-.md) command displays information from the debugger data model and supports queries using LINQ syntax. Dx is very useful to query the objects in realtime. This allows for the prototyping of the desired query that can be then automated using JavaScript. The dx command provides tab completion, which can be helpful when exploring the object model. For general information on working with LINQ queries and debugger objects, see [Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md).

This dx command, counts all the calls to a certain API, in this example *GetLastError*.

```dbgcmd
0:000> dx @$cursession.TTD.Calls("kernelbase!GetLastError").Count()

@$cursession.TTD.Calls("kernelbase! GetLastError").Count() : 0x12
```

This command looks in the entire time travel trace to see when GetLastError was called.

```dbgcmd
0:000> dx @$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0)

@$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0)
    [0x0]
    [0x1]
    [0x2]
    [0x3]
```

### String comparisons for TTD.Calls Object to locate calls

This example command, shows how to use string comparisons to locate specific calls. In this example, the query looks for the string "OLE" in the *lpFileName* parameter of the [CreateFileW function](/windows/win32/api/fileapi/nf-fileapi-createfilew).

```dbgcmd
dx -r2 @$cursession.TTD.Calls("kernelbase!CreateFileW").Where(x => x.Parameters.lpFileName.ToDisplayString("su").Contains("OLE"))
```

Add a .Select statement to print Timestart and the value of the *lpFileName* parameter.

```dbgcmd
dx -r2 @$cursession.TTD.Calls("kernelbase!CreateFileW").Where(x => x.Parameters.lpFileName.ToDisplayString("su").Contains("OLE")).Select(x => new { TimeStart = x.TimeStart, lpFileName = x.Parameters.lpFileName })
```

This generates this output, if a [TTD.Calls](time-travel-debugging-calls-objects.md) object is found that contains the target information.

```dbgcmd
    [0x0]
        TimeStart        : 6E37:590
        lpFileName       : 0x346a78be90 : "C:\WINDOWS\SYSTEM32\OLEACCRC.DLL" [Type: wchar_t *]
```

## Displaying the number of calls in a trace

After you have used the dx command to explore objects you want to work with, you can automate their use with JavaScript. In this simple example, the [TTD.Calls](time-travel-debugging-calls-objects.md) object is used to count calls to *kernelbase!GetLastError*.

```javascript
function CountLastErrorCalls()
{
    var LastErrorCalls = host.currentSession.TTD.Calls("kernelbase!GetLastError");
    host.diagnostics.debugLog(">>> GetLastError calls in this TTD recording: " +  LastErrorCalls.Count() +" \n");
}
```

Save the script in a TTDUtils.js file and call it using the dx command to display a count of the number of kernelbase!GetLastError in the trace file.

```dbgcmd

0:000> dx Debugger.State.Scripts.TTDUtils.Contents.CountLastErrorCalls()
>>> GetLastError calls in this TTD recording: 18
```

## Displaying the frames in a stack

To display the frames in a stack, an array is used.

```javascript
function DisplayStack()
{
// Create an array of stack frames in the current thread
const Frames = Array.from(host.currentThread.Stack.Frames);
host.diagnostics.debugLog(">>> Printing stack \n");
// Print out all of the frame entries in the array
for(const [Idx, Frame] of Frames.entries())
    {
        host.diagnostics.debugLog(">>> Stack Entry -> " + Idx + ":  "+ Frame + " \n");
    }
}
```

In this sample trace, the one stack entry is displayed.

```dbgcmd
0:000> dx Debugger.State.Scripts.TTDUtils.Contents.DisplayStack()
>>> Printing stack
>>> Stack Entry -> 0:  ntdll!LdrInitializeThunk + 0x21
```

## Locating an event and displaying the stack

In this code all of the exceptions events are located and a loop is used to move to each one. Then the currentThread.ID of the [TTD Thread Objects](time-travel-debugging-thread-objects.md) is used to display the thread ID and currentThread.Stack is used to display all of the frames in the stack.

```javascript

function HardwareExceptionDisplayStack()
{
var exceptionEvents = host.currentProcess.TTD.Events.Where(t => t.Type == "Exception");
    for (var curEvent of exceptionEvents)
    {
        // Move to the current event position
        curEvent.Position.SeekTo();
        host.diagnostics.debugLog(">>> The Thread ID (TID) is : " + host.currentThread.Id + "\n");
        // Create an array of stack frames in the current thread
        const Frames = Array.from(host.currentThread.Stack.Frames);
        host.diagnostics.debugLog(">>> Printing stack \n");
        // Print out all of the frame entries in the array
        for(const [Idx, Frame] of Frames.entries()) {
            host.diagnostics.debugLog(">>> Stack Entry -> " + Idx + ":  "+ Frame + " \n");
        }
    host.diagnostics.debugLog("\n");
    }
}
```

The output shows the location of the exception event, the TID and the stack frames.  

```dbgcmd
0:000> dx Debugger.State.Scripts.TTDUtils.Contents.HardwareExceptionDisplayStack()
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 91:0
>>> The Thread ID (TID) is : 5260
>>> Printing stack
>>> Stack Entry -> 0:  0x540020
>>> Stack Entry -> 1:  0x4d0049
>>> Stack Entry -> 2:  DisplayGreeting!__CheckForDebuggerJustMyCode + 0x16d
>>> Stack Entry -> 3:  DisplayGreeting!mainCRTStartup + 0x8
>>> Stack Entry -> 4:  KERNEL32!BaseThreadInitThunk + 0x19
>>> Stack Entry -> 5:  ntdll!__RtlUserThreadStart + 0x2f
>>> Stack Entry -> 6:  ntdll!_RtlUserThreadStart + 0x1b

```

## Locating an event and sending two commands

Querying TTD objects and sending commands can be combined as necessary. This example locates each event in the TTD trace of type ThreadCreated, moves to that position, and sends the [~ Thread Status](---thread-status-.md) and the [!runaway](-runaway.md) commands to display the thread status.

```javascript
function ThreadCreateThreadStatus()
{
var threadEvents = host.currentProcess.TTD.Events.Where(t => t.Type == "ThreadCreated");
    for (var curEvent of threadEvents)
    {
        // Move to the current event position
       curEvent.Position.SeekTo();
        // Display Information about threads
       host.namespace.Debugger.Utility.Control.ExecuteCommand("~", false);
       host.namespace.Debugger.Utility.Control.ExecuteCommand("!runaway 7", false);
    }
}
```

Running the code displays the thread status at the moment in time that the exception occurred.

```dbgcmd
0:000> dx Debugger.State.Scripts.TTDUtils.Contents.ThreadCreateThreadStatus()
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: F:0
.  0  Id: 948.148c Suspend: 4096 Teb: 00a33000 Unfrozen
User Mode Time
  Thread       Time
    0:148c     0 days 0:00:00.000
Kernel Mode Time
  Thread       Time
    0:148c     0 days 0:00:00.000
Elapsed Time
  Thread       Time
    0:148c     3474 days 2:27:43.000
```

## Chaining utility functions together

In this final sample, we can call the utility functions that we created earlier. First we  index the trace using *IndexTraceTry* and then call *ThreadCreateThreadStatus*. We then use *ResetTrace* to move to the start of the trace and lastly call *HardwareExceptionDisplayStack*.

```JavaScript
function ProcessTTDFiles()
{
    try
    {
    IndexTraceTry()
    ThreadCreateThreadStatus()
    ResetTrace()
    HardwareExceptionDisplayStack()
    }

    catch(err)
    {
         host.diagnostics.debugLog("\n >>> Processing of TTD file failed \n");
    }

}
```

Running this script on a trace file that contains a hardware exception, generates this output.

```dbgcmd
0:000> dx Debugger.State.Scripts.TTDUtils.Contents.ProcessTTDFiles()

>>> Index Return Value: Loaded

>>> Trace was successfully indexed in 0 ms
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: F:0
.  0  Id: 948.148c Suspend: 4096 Teb: 00a33000 Unfrozen
User Mode Time
  Thread       Time
    0:148c     0 days 0:00:00.000
Kernel Mode Time
  Thread       Time
    0:148c     0 days 0:00:00.000
Elapsed Time
  Thread       Time
    0:148c     3474 days 2:27:43.000
>>> Printing stack
>>> Stack Entry -> 0:  ntdll!LdrInitializeThunk
>>> Current position in trace file:  F:0
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: F:0
>>> New position in trace file:  F:0
(948.148c): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 91:0
>>> The Thread ID (TID) is : 5260
>>> Printing stack
>>> Stack Entry -> 0:  0x540020
>>> Stack Entry -> 1:  0x4d0049
>>> Stack Entry -> 2:  DisplayGreeting!__CheckForDebuggerJustMyCode + 0x16d
>>> Stack Entry -> 3:  DisplayGreeting!mainCRTStartup + 0x8
>>> Stack Entry -> 4:  KERNEL32!BaseThreadInitThunk + 0x19
>>> Stack Entry -> 5:  ntdll!__RtlUserThreadStart + 0x2f
>>> Stack Entry -> 6:  ntdll!_RtlUserThreadStart + 0x1b

```

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Native Debugger Objects in JavaScript Extensions - Debugger Object Details](native-objects-in-javascript-extensions-debugger-objects.md)

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)