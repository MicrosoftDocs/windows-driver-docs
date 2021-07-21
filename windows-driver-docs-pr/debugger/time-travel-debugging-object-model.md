---
title: Time Travel Debugging - Introduction to Time Travel Debugging objects
description: This section describes how to use the data model to query time travel traces. 
ms.date: 04/17/2019
ms.localizationpriority: medium
---

# Introduction to Time Travel Debugging objects

![Small time travel logo showing clock.](images/ttd-time-travel-debugging-logo.png)

This section describes how to use the data model to query time travel traces. This can be a powerful tool to answer questions like these about the code that is captured in a time travel trace.
* What exceptions are in the trace?
* At what point in time in the trace did a specific code module load?
* When were threads created/terminated in the trace?
* What are the longest running threads in the trace?

There are TTD extensions that add data to the *Session* and *Process* data model objects. The TTD data model objects can be accessed through  the [dx  (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) command, WinDbg Preview's model windows, JavaScript and C++. The TTD extensions are automatically loaded when debugging a time travel trace.

## Process Objects

The primary objects added to *Process* objects can be found in the *TTD* namespace off of any *Process* object. For example, `@$curprocess.TTD`.

```dbgcmd
:000> dx @$curprocess.TTD
@$curprocess.TTD                
    Threads         
    Events          
    Lifetime         : [26:0, 464232:0]
    SetPosition      [Sets the debugger to point to the given position on this process.]
```

For general information on working with LINQ queries and debugger objects, see [Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md).

### Properties

| Object | Description |
| --- | --- |
| Lifetime | A [TTD range object](time-travel-debugging-range-objects.md) describing the lifetime of the entire trace. |
| Threads | Contains a collection of [TTD thread objects](time-travel-debugging-thread-objects.md), one for every thread throughout the lifetime of the trace. |
| Events | Contains a collection of [TTD event objects](time-travel-debugging-event-objects.md), one for every event in the trace. |

### Methods

| Method | Description |
| --- | --- |
| SetPosition() | Takes an integer between 0 and 100 or string in N:N form as input and jumps the trace to that location. See [!tt](time-travel-debugging-extension-tt.md) for more information.|

## Session Objects
The primary objects added to *Session* objects can be found in the *TTD* namespace off of any *Session* object. For example, `@$cursession.TTD`.

```dbgcmd
0:000> dx @$cursession.TTD
@$cursession.TTD                 : [object Object]
    Calls            [Returns call information from the trace for the specified set of methods: TTD.Calls("module!method1", "module!method2", ...) For example: dx @$cursession.TTD.Calls("user32!SendMessageA")]
    Memory           [Returns memory access information for specified address range: TTD.Memory(startAddress, endAddress [, "rwec"])]
    DefaultParameterCount : 0x4
    AsyncQueryEnabled : false
    Resources       
    Data             : Normalized data sources based on the contents of the time travel trace
    Utility          : Methods that can be useful when analyzing time travel traces
```


> [!NOTE]
> There are some objects and methods added by TTDAnalyze that are used for internal functions of the extension. Not all namespaces are documented, and the current namespaces will evolve over time.
>

### Methods

| Method | Description |
| --- | --- |
| Data.Heap() | A collection of [heap objects](time-travel-debugging-heap-objects.md) that were allocated during the trace. Note that this is a function that does computation, so it takes a while to run.|
| Calls() | Returns a collection of [calls objects](time-travel-debugging-calls-objects.md) that match the input string. The input string can contain wildcards. Note that this is a function that does computation, so it takes a while to run.  |
| Memory() | This is a method that takes beginAddress, endAddress and dataAccessMask parameters and returns a collection of [memory objects](time-travel-debugging-memory-objects.md). Note that this is a function that does computation, so it takes a while to run.  |


## Sorting query output

Use the OrderBy() method to sort the rows returned from the query by one or more columns. This example sorts by TimeStart in ascending order.

```dbgcmd
0:000> dx -r2 @$cursession.TTD.Calls("kernelbase!GetLastError").OrderBy(c => c.TimeStart)
@$cursession.TTD.Calls("kernelbase!GetLastError").OrderBy(c => c.TimeStart)                
    [0xb]           
        EventType        : Call
        ThreadId         : 0x3a10
        UniqueThreadId   : 0x2
        TimeStart        : 39:2DC [Time Travel]
        TimeEnd          : 39:2DF [Time Travel]
        Function         : UnknownOrMissingSymbols
        FunctionAddress  : 0x7561ccc0
        ReturnAddress    : 0x7593d24c
        ReturnValue      : 0x0
        Parameters      
    [0xe]           
        EventType        : Call
        ThreadId         : 0x3a10
        UniqueThreadId   : 0x2
        TimeStart        : AF:36 [Time Travel]
        TimeEnd          : AF:39 [Time Travel]
        Function         : UnknownOrMissingSymbols
        FunctionAddress  : 0x7561ccc0
        ReturnAddress    : 0x4723ef
        ReturnValue      : 0x0
        Parameters  
```

To display additional depth of the data model objects the -r2 recursion level option is used. For more information about the dx command options, see [dx  (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).

This example sorts by TimeStart in descending order.

```dbgcmd
0:000> dx -r2 @$cursession.TTD.Calls("kernelbase!GetLastError").OrderByDescending(c => c.TimeStart)
@$cursession.TTD.Calls("kernelbase!GetLastError").OrderByDescending(c => c.TimeStart)                
    [0x1896]        
        EventType        : Call
        ThreadId         : 0x3a10
        UniqueThreadId   : 0x2
        TimeStart        : 464224:34 [Time Travel]
        TimeEnd          : 464224:37 [Time Travel]
        Function         : UnknownOrMissingSymbols
        FunctionAddress  : 0x7561ccc0
        ReturnAddress    : 0x7594781c
        ReturnValue      : 0x0
        Parameters      
    [0x18a0]        
        EventType        : Call
        ThreadId         : 0x3a10
        UniqueThreadId   : 0x2
        TimeStart        : 464223:21 [Time Travel]
        TimeEnd          : 464223:24 [Time Travel]
        Function         : UnknownOrMissingSymbols
        FunctionAddress  : 0x7561ccc0
        ReturnAddress    : 0x7594781c
        ReturnValue      : 0x0
        Parameters    
```

## Specifying elements in a query

To select a specific element a variety of qualifiers can be appended to the query. For example, the query displays the first call that contains  "kernelbase!GetLastError".

```dbgcmd
0:000> dx @$cursession.TTD.Calls("kernelbase!GetLastError").First()
@$cursession.TTD.Calls("kernelbase!GetLastError").First()                
    EventType        : Call
    ThreadId         : 0x3a10
    UniqueThreadId   : 0x2
    TimeStart        : 77A:9 [Time Travel]
    TimeEnd          : 77A:C [Time Travel]
    Function         : UnknownOrMissingSymbols
    FunctionAddress  : 0x7561ccc0
    ReturnAddress    : 0x6cf12406
    ReturnValue      : 0x0
    Parameters    
```

## Filtering in a query

Use the Select() method to choose which columns to see and modify the column display name.

This example returns rows where ReturnValue is not zero and selects to display the TimeStart and ReturnValue columns with custom display names of Time and Error.

```dbgcmd
0:000> dx -r2 @$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0).Select(c => new { Time = c.TimeStart, Error = c.ReturnValue })
@$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0).Select(c => new { Time = c.TimeStart, Error = c.ReturnValue })                
    [0x13]          
        Time             : 3C64A:834 [Time Travel]
        Error            : 0x36b7
    [0x1c]          
        Time             : 3B3E7:D6 [Time Travel]
        Error            : 0x3f0
    [0x1d]          
        Time             : 3C666:857 [Time Travel]
        Error            : 0x36b7
    [0x20]          
        Time             : 3C67E:12D [Time Travel]
```

## Grouping

Use the GroupBy() method to group data returned by the query to do perform analysis using structured results
This example groups the time locations by error number.

```dbgcmd
0:000> dx -r2 @$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0).Select(c => new { Time = c.TimeStart, Error = c.ReturnValue }).GroupBy(x => x.Error)
@$s = @$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0).Select(c => new { Time = c.TimeStart, Error = c.ReturnValue }).GroupBy(x => x.Error)                
    [0x36b7]        
        [0x0]           
        [0x1]           
        [0x2]           
        [0x3]           
        [...]           
    [0x3f0]         
        [0x0]           
        [0x1]           
        [0x2]           
        [0x3]           
...
```

## Assigning result of a query to a variable

Use this syntax to assigning result of a query to a variable `dx @$var = <expression>`

This example assigns the results of a query to myResults

```dbgcmd
dx -r2 @$myResults = @$cursession.TTD.Calls("kernelbase!GetLastError").Where(c => c.ReturnValue != 0).Select(c => new { Time = c.TimeStart, Error = c.ReturnValue })
```

Use the dx command to display the newly created variable using the -g grid option. For more information on the dx command options, see [dx  (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).

```dbgcmd
0:000> dx -g @$myResults
========================================
=           = (+) Time     = (+) Error =
========================================
= [0x13]    - 3C64A:834    - 0x36b7    =
= [0x1c]    - 3B3E7:D6     - 0x3f0     =
= [0x1d]    - 3C666:857    - 0x36b7    =
= [0x20]    - 3C67E:12D    - 0x2       =
= [0x21]    - 3C6F1:127    - 0x2       =
= [0x23]    - 3A547:D6     - 0x3f0     =
= [0x24]    - 3A59B:D0     - 0x3f0     =
```


## Examples

### Querying for exceptions

This LINQ query uses the [TTD.Event object](time-travel-debugging-event-objects.md) to display all of the exceptions in the trace.

```dbgcmd
0:000> dx @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)
@$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)
    [0x0]            : Exception 0x000006BA of type Software at PC: 0X777F51D0
    [0x1]            : Exception 0x000006BA of type Software at PC: 0X777F51D0
    [0x2]            : Exception 0xE06D7363 of type CPlusPlus at PC: 0X777F51D0
```

### Querying for specific API calls

Use [TTD.Calls object](time-travel-debugging-calls-objects.md) to query for specific API calls. In this example, an error has occurred when calling *user32!MessageBoxW*, the Windows API to show a message box. We list all calls to MessageBoxW , order it by the start time of the function, and then pick the last call.

```dbgcmd
0:000> dx @$cursession.TTD.Calls("user32!MessageBoxW").OrderBy(c => c.TimeStart).Last()
@$cursession.TTD.Calls("user32!MessageBoxW").OrderBy(c => c.TimeStart).Last()                
    EventType        : Call
    ThreadId         : 0x3a10
    UniqueThreadId   : 0x2
    TimeStart        : 458310:539 [Time Travel]
    TimeEnd          : 45C648:61 [Time Travel]
    Function         : UnknownOrMissingSymbols
    FunctionAddress  : 0x750823a0
    ReturnAddress    : 0x40cb93
    ReturnValue      : 0x10a7000000000001
    Parameters

```

### Querying for the load event of a specific module

First, use the [lm (List Loaded Modules)](lm--list-loaded-modules-.md) command to display the loaded modules.

```dbgcmd
0:000> lm
start    end        module name
012b0000 012cf000   CDog_Console   (deferred)             
11570000 1158c000   VCRUNTIME140D   (deferred)             
11860000 119d1000   ucrtbased   (deferred)             
119e0000 11b63000   TTDRecordCPU   (deferred)             
11b70000 11cb1000   TTDWriter   (deferred)             
73770000 73803000   apphelp    (deferred)             
73ea0000 74062000   KERNELBASE   (deferred)             
75900000 759d0000   KERNEL32   (deferred)             
77070000 771fe000   ntdll      (private pdb symbols)
```

Then use the following dx command to see at what position in the trace a specific module was loaded, such as ntdll.

```dbgcmd
dx @$curprocess.TTD.Events.Where(t => t.Type == "ModuleLoaded").Where(t => t.Module.Name.Contains("ntdll.dll")) 
@$curprocess.TTD.Events.Where(t => t.Type == "ModuleLoaded").Where(t => t.Module.Name.Contains("ntdll.dll"))                 
    [0x0]            : Module Loaded at position: A:0 
```

This LINQ query displays the load event(s) of a particular module.

```dbgcmd
0:000> dx @$curprocess.TTD.Events.Where(t => t.Type == "ModuleUnloaded").Where(t => t.Module.Name.Contains("ntdll.dll")) 
@$curprocess.TTD.Events.Where(t => t.Type == "ModuleUnloaded").Where(t => t.Module.Name.Contains("ntdll.dll"))                 
    [0x0]            : Module Unloaded at position: FFFFFFFFFFFFFFFE:0
```
The address of FFFFFFFFFFFFFFFE:0 indicates the end of the trace. 



### Querying for all of the error checks in the trace

Use this command to sort by all of the error checks in the trace by error count.

```dbgcmd
0:000> dx -g @$cursession.TTD.Calls("kernelbase!GetLastError").Where( x=> x.ReturnValue != 0).GroupBy(x => x.ReturnValue).Select(x => new { ErrorNumber = x.First().ReturnValue, ErrorCount = x.Count()}).OrderByDescending(p => p.ErrorCount),d
==================================================
=                 = (+) ErrorNumber = ErrorCount =
==================================================
= [1008]          - 1008            - 8668       =
= [14007]         - 14007           - 4304       =
= [2]             - 2               - 1710       =
= [6]             - 6               - 1151       =
= [1400]          - 1400            - 385        =
= [87]            - 87              - 383        =
```

### Querying for the time position in the trace when threads were created

Use this dx command to display all of the events in the trace in grid format (-g).

```dbgcmd
0:000> dx -g @$curprocess.TTD.Events
==================================================================================================================================================================================================
=                                                          = (+) Type            = (+) Position          = (+) Module                                                   = (+) Thread             =
==================================================================================================================================================================================================
= [0x0] : Module Loaded at position: 2:0                   - ModuleLoaded        - 2:0                   - Module C:\Users\USER1\Documents\Visual Studio 2015\Proje... -                        =
= [0x1] : Module Loaded at position: 3:0                   - ModuleLoaded        - 3:0                   - Module C:\WINDOWS\SYSTEM32\VCRUNTIME140D.dll at address 0... -                        =
= [0x2] : Module Loaded at position: 4:0                   - ModuleLoaded        - 4:0                   - Module C:\WINDOWS\SYSTEM32\ucrtbased.dll at address 0X118... -                        =
= [0x3] : Module Loaded at position: 5:0                   - ModuleLoaded        - 5:0                   - Module C:\Users\USER1\AppData\Local\Dbg\UI\Fast.20170907... -                        =
= [0x4] : Module Loaded at position: 6:0                   - ModuleLoaded        - 6:0                   - Module C:\Users\USER1\AppData\Local\Dbg\UI\Fast.20170907... -                        =
= [0x5] : Module Loaded at position: 7:0                   - ModuleLoaded        - 7:0                   - Module C:\WINDOWS\SYSTEM32\apphelp.dll at address 0X73770... -                        =
= [0x6] : Module Loaded at position: 8:0                   - ModuleLoaded        - 8:0                   - Module C:\WINDOWS\System32\KERNELBASE.dll at address 0X73... -                        =
= [0x7] : Module Loaded at position: 9:0                   - ModuleLoaded        - 9:0                   - Module C:\WINDOWS\System32\KERNEL32.DLL at address 0X7590... -                        =
= [0x8] : Module Loaded at position: A:0                   - ModuleLoaded        - A:0                   - Module C:\WINDOWS\SYSTEM32\ntdll.dll at address 0X7707000... -                        =
= [0x9] : Thread created at D:0                            - ThreadCreated       - D:0                   -                                                              - UID: 2, TID: 0x4C2C    =
= [0xa] : Thread terminated at 64:0                        - ThreadTerminated    - 64:0                  -                                                              - UID: 2, TID: 0x4C2C    =
= [0xb] : Thread created at 69:0                           - ThreadCreated       - 69:0                  -                                                              - UID: 3, TID: 0x4CFC    =
= [0xc] : Thread created at 6A:0                           - ThreadCreated       - 6A:0                  -                                                              - UID: 4, TID: 0x27B0    =
= [0xd] : Thread terminated at 89:0                        - ThreadTerminated    - 89:0                  -                                                              - UID: 4, TID: 0x27B0    =
= [0xe] : Thread terminated at 8A:0                        - ThreadTerminated    - 8A:0                  -                                                              - UID: 3, TID: 0x4CFC    =
= [0xf] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0  - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\Users\USER1\Documents\Visual Studio 2015\Proje... -                        =
= [0x10] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\Users\USER1\AppData\Local\Dbg\UI\Fast.20170907... -                        =
= [0x11] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\WINDOWS\SYSTEM32\VCRUNTIME140D.dll at address 0... -                        =
= [0x12] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\Users\USER1\AppData\Local\Dbg\UI\Fast.20170907... -                        =
= [0x13] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\WINDOWS\SYSTEM32\ucrtbased.dll at address 0X118... -                        =
= [0x14] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\WINDOWS\SYSTEM32\apphelp.dll at address 0X73770... -                        =
= [0x15] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\WINDOWS\System32\KERNELBASE.dll at address 0X73... -                        =
= [0x16] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\WINDOWS\System32\KERNEL32.DLL at address 0X7590... -                        =
= [0x17] : Module Unloaded at position: FFFFFFFFFFFFFFFE:0 - ModuleUnloaded      - FFFFFFFFFFFFFFFE:0    - Module C:\WINDOWS\SYSTEM32\ntdll.dll at address 0X7707000... -                        =
==================================================================================================================================================================================================
```

Select any of the columns with a + sign to sort the output.

Use this LINQ query to display in grid format, the time position in the trace when threads were created (Type == "ThreadCreated").

```dbgcmd
dx -g @$curprocess.TTD.Events.Where(t => t.Type == "ThreadCreated").Select(t => t.Thread) 
===========================================================================================================
=                             = (+) UniqueId = (+) Id    = (+) Lifetime                 = (+) ActiveTime  =
===========================================================================================================
= [0x0] : UID: 2, TID: 0x4C2C - 0x2          - 0x4c2c    - [0:0, FFFFFFFFFFFFFFFE:0]    - [D:0, 64:0]     =
= [0x1] : UID: 3, TID: 0x4CFC - 0x3          - 0x4cfc    - [0:0, 8A:0]                  - [69:0, 8A:0]    =
= [0x2] : UID: 4, TID: 0x27B0 - 0x4          - 0x27b0    - [0:0, 89:0]                  - [6A:0, 89:0]    =
===========================================================================================================
```

Use this LINQ query to display in grid format, the time positions in the trace when threads were terminated (Type == "ThreadTerminated").

```dbgcmd
0:000> dx -g @$curprocess.TTD.Events.Where(t => t.Type == "ThreadTerminated").Select(t => t.Thread) 
===========================================================================================================
=                             = (+) UniqueId = (+) Id    = (+) Lifetime                 = (+) ActiveTime  =
===========================================================================================================
= [0x0] : UID: 2, TID: 0x4C2C - 0x2          - 0x4c2c    - [0:0, FFFFFFFFFFFFFFFE:0]    - [D:0, 64:0]     =
= [0x1] : UID: 4, TID: 0x27B0 - 0x4          - 0x27b0    - [0:0, 89:0]                  - [6A:0, 89:0]    =
= [0x2] : UID: 3, TID: 0x4CFC - 0x3          - 0x4cfc    - [0:0, 8A:0]                  - [69:0, 8A:0]    =
===========================================================================================================
```

### Sorting output to determine the longest running threads

Use this LINQ query to display in grid format, the approximate longest running threads in the trace.

```dbgcmd
0:000> dx -g @$curprocess.TTD.Events.Where(e => e.Type == "ThreadTerminated").Select(e => new { Thread = e.Thread, ActiveTimeLength = e.Thread.ActiveTime.MaxPosition.Sequence - e.Thread.ActiveTime.MinPosition.Sequence }).OrderByDescending(t => t.ActiveTimeLength)
=========================================================
=          = (+) Thread              = ActiveTimeLength =
=========================================================
= [0x0]    - UID: 2, TID: 0x1750     - 0x364030         =
= [0x1]    - UID: 3, TID: 0x420C     - 0x360fd4         =
= [0x2]    - UID: 7, TID: 0x352C     - 0x35da46         =
= [0x3]    - UID: 9, TID: 0x39F4     - 0x34a5b5         =
= [0x4]    - UID: 11, TID: 0x4288    - 0x326199         =
= [0x5]    - UID: 13, TID: 0x21C8    - 0x2fa8d8         =
= [0x6]    - UID: 14, TID: 0x2188    - 0x2a03e3         =
= [0x7]    - UID: 15, TID: 0x40E8    - 0x29e7d0         =
= [0x8]    - UID: 16, TID: 0x124     - 0x299677         =
= [0x9]    - UID: 4, TID: 0x2D74     - 0x250f43         =
= [0xa]    - UID: 5, TID: 0x2DC8     - 0x24f921         =
= [0xb]    - UID: 6, TID: 0x3B1C     - 0x24ec8e         =
= [0xc]    - UID: 10, TID: 0x3808    - 0xf916f          =
= [0xd]    - UID: 12, TID: 0x26B8    - 0x1ed3a          =
= [0xe]    - UID: 17, TID: 0x37D8    - 0xc65            =
= [0xf]    - UID: 8, TID: 0x45F8     - 0x1a2            =
=========================================================
```

### Querying for read accesses to a memory range 

Use the [TTD.Memory object](time-travel-debugging-memory-objects.md) to query for to query for read accesses to a memory range.

The Thread Environment Block (TEB) is a structure that contains all the information regarding the state of a thread, including the result returned by GetLastError(). You can query this data structure by running `dx @$teb` for the current thread. One of TEB's members is a LastErrorValue variable, 4 bytes in size. We can reference the LastErrorValue member in the TEB using this syntax. `dx &@$teb->LastErrorValue`.

The example query shows how to find every read operation done in that range in memory, select all the reads that happen before the a dialog was created and then sort the result to find the last read operation.

```dbgcmd
0:000> dx @$cursession.TTD.Memory(&@$teb->LastErrorValue, &@$teb->LastErrorValue + 0x4, "r")
@$cursession.TTD.Memory(&@$teb->LastErrorValue, &@$teb->LastErrorValue + 0x4, "r")
    [0x0]           
    [0x1]           
    [0x2]           
    [0x3]     
```

If in our trace a "dialog" event has taken place we can run a query to find every read operation done in that range in memory, select all the reads that happen before the dialog got created and then sort the result to find the last read operation. Then time travel to that point in time by calling SeekTo() on the resulting time position.

```dbgcmd

:000> dx @$cursession.TTD.Memory(&@$teb->LastErrorValue, &@$teb->LastErrorValue + 0x4, "r").Where(m => m.TimeStart < @$dialog).OrderBy(m => m.TimeStart).Last().TimeEnd.SeekTo()
Setting position: 458300:37
ModLoad: 6cee0000 6cf5b000   C:\WINDOWS\system32\uxtheme.dll
ModLoad: 75250000 752e6000   C:\WINDOWS\System32\OLEAUT32.dll
ModLoad: 76320000 7645d000   C:\WINDOWS\System32\MSCTF.dll
ModLoad: 76cc0000 76cce000   C:\WINDOWS\System32\MSASN1.dll
```

## GitHub TTD Query Lab

For a tutorial on how to debug C++ code using a Time Travel Debugging recording using queries to find information about the execution of the problematic code in question, see https://github.com/Microsoft/WinDbg-Samples/blob/master/TTDQueries/tutorial-instructions.md.

All of the code used in the lab is available here: https://github.com/Microsoft/WinDbg-Samples/tree/master/TTDQueries/app-sample.


## Troubleshooting TTD Queries

### "UnknownOrMissingSymbols" as the function names

The data model extension needs full symbol information in order to provide function names, parameter values, etc. When full symbol information is not available the debugger uses "UnknownOrMissingSymbols" as the function name.

- If you have private symbols you will get the function name and the correct list of parameters.
- If you have public symbols you will get the function name and a default set of parameters - four unsigned 64-bit ints.
- If you have no symbol information for the module you are querying, then “UnknownOrMissingSymbols” is used as the name.

### TTD Queries for calls

There can be a several reasons that a query does not return anything for calls to a DLL.

- The syntax for the call isn't quite right.  Try verifying the call syntax by using the x command: "x <call>". If the module name returned by x is in uppercase, use that.
- The DLL is not loaded yet and is loaded later in the trace. To work around this travel to a point in time after the DLL is loaded and redo the query.
- The call is inlined which the query engine is unable to track.
- The query pattern uses wildcards which returns too many functions.  Try to make the query pattern more specific so that the number of matched functions is small enough.

## See Also

[Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md)

[dx  (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[Time Travel Debugging - JavaScript Automation](time-travel-debugging-javascript-automation.md)

---
