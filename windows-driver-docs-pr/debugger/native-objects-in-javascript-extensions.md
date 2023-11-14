---
title: Native Debugger Objects in JavaScript Extensions
description: Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions.
ms.date: 02/02/2021
---

# Native Debugger Objects in JavaScript Extensions

Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions to manipulate the state of the debugger.

Example debugger objects include the following.

- Session
- Threads / Thread
- Processes / Process
- Stack Frames / Stack Frame
- Local Variables
- Modules / Module
- Utility
- State
- Settings

For example the host.namespace.Debugger.Utility.Control.ExecuteCommand object can be used to send the u command to the debugger with following two lines of JavaScript code.

```dbgcmd
var ctl = host.namespace.Debugger.Utility.Control;   
var outputLines = ctl.ExecuteCommand("u");
```

This topic describes how to work with common objects and provides reference information on their attributes and behaviors.

For general information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md). For JavaScript examples that use the debugger objects, see [JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md). For information about working with the settings objects, see [**.settings (Set Debug Settings)**](../debuggercmds/-settings--set-debug-settings-.md).

To explore the objects available in a debugger session, use the [**dx (Display NatVis Expression)**](../debuggercmds/dx--display-visualizer-variables-.md) command. For example, you can display some of the top level debugger objects with this dx command.

```dbgcmd
0: kd> dx -r2 Debugger
Debugger                
    Sessions         : [object Object]
        [0x0]            : Remote KD: KdSrv:Server=@{<Local>},Trans=@{NET:Port=50000,Key=1.2.3.4,Target}
    Settings        
        Debug           
        Display         
        EngineInitialization
        Extensions      
        Input           
        Sources         
        Symbols         
        AutoSaveSettings : false
    State           
        DebuggerVariables
        PseudoRegisters 
        Scripts         
        UserVariables   
    Utility         
        Collections     
        Control         
        Objects   
```

All of the items listed above are clickable DML and can be recursed further down to view the debugger object structure.

## Extending the Debugger via the Data Model

The debugger data model allows for the creation of an interface to information about applications and drivers in Windows that has the following attributes.

- Is discoverable and organized- a logically structured name space can be queried using the dx command.
- Can be queried using LINQ- This allows for extraction and sorting of data using a standard query language.
- Can be logically and consistently extended - Extensible using techniques described in this topic with debugger scripting providers such as Natvis and JavaScript.

## Extending a Debugger Object in JavaScript

In addition to being able to create a visualizer in JavaScript, script extensions can also modify the core concepts of the debugger - sessions, processes, threads, stacks, stack frames, local variables - and even publish themselves as extension points that other extensions can consume.

This section describes how to extend a core concept within the debugger. Extensions which are built to be shared should conform to the guidelines presented in [Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations](native-objects-in-javascript-extensions-design-considerations.md).

**Registering an Extension**

A script can register the fact that it provides an extension through an entry in the array returned from the initializeScript method.

```dbgcmd
function initializeScript()
{
    return [new host.namedModelParent(comProcessExtension, "Debugger.Models.Process")];
}
```

The presence of a host.namedModelParent object within the returned array indicates to the debugger that a given prototype object or ES6 class (comProcessExtension in this case) is going to be a parent data model to the model which is registered under the name Debugger.Models.Process.

**Debugger Object Extension Points**

The following debugger extension points are integral to the debugger and available to be used by script providers such as JavaScript.

**Debugger.Models.Sessions**: The list of sessions (targets) that the debugger is attached to

**Debugger.Models.Session**: An individual session (target) that the debugger is attached to (live user mode, KD, etc...)

**Debugger.Models.Processes**: The list of processes within a session

**Debugger.Models.Threads**: The list of threads within a process

**Debugger.Models.Thread**: An individual thread within a process (regardless of whether user or kernel mode)

**Debugger.Models.Stack**: The stack of a thread

**Debugger.Models.StackFrames**: The collection of frames which make up a stack

**Debugger.Models.StackFrame**: An individual stack frame within a stack

**Debugger.Models.LocalVariables**: The local variables within a stack frame

**Debugger.Models.Parameters**: The parameters for a call within a stack frame

**Debugger.Models.Module**: An individual module within the address space of a process

 
**Additional Data Model Objects**

In addition, there are some additional data model objects that are defined by the core data model.

**DataModel.Models.Intrinsic**: An intrinsic value (ordinals, floats, etc...)

**DataModel.Models.String**: A string

**DataModel.Models.Array**: A native array

**DataModel.Models.Guid**: A GUID

**DataModel.Models.Error**: An error object

**DataModel.Models.Concepts.Iterable**: Applied to every object which is iterable

**DataModel.Models.Concepts.StringDisplayable**: Applied to every object which has a display string conversion

**Example COM Debugger Object Extension Overview**

Let's consider an example. Imagine that you want to create a debugger extension to display information specific to COM, such as the global interface table (GIT).

In the past, there might be an existing debugger extension with a number of commands which provide a means to access things about COM. One command might display process centric information (the global interface table for instance). Another command might provide thread centric information such as what apartment code is executing within. You might need to know about and load a second debugger extension to explore other aspects of COM.

Instead of having a set of hard to discover commands, a JavaScript extension can modify the debugger's concept of what a process and a thread is, to add this information in a way that's natural, explorable, and composable with other debugger extensions.

**User or Kernel Mode Debugger Object Extension**

The debugger and the debugger objects have different behavior in user and kernel mode. When you create your debugger model objects you need to decide which environments you will be working in. Because we will be working with COM in user mode, we will create and test this com extension in user mode. In other situations, you may be able to create a debugger JavaScript that will work in both user and kernel mode debugging.

**Creating a Sub-Namespace**

Going back to our example, we can define a prototype or ES6 class, *comProcessExtension* which contains the set of things we want to add to a process object.

**Important**   The intent with the sub-namespace is to create a logically structured and naturally explorable paradigm. For example, avoid dumping unrelated items into the same sub-namespace. Carefully review the information discussed in [Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations](native-objects-in-javascript-extensions-design-considerations.md) before creating a sub-namespace.

In this code snippet, we create add a sub-namespace called 'COM' on to the existing process debugger object.

```javascript
var comProcessExtension =
{
    //
    // Add a sub-namespace called 'COM' on process.
    //
    get COM()
    {
        //
        // What is 'this' below...?  It's the debugger's process object.  Yes -- this means that there is a cross-language
        // object hierarchy here.  A C++ object implemented in the debugger has a parent model (prototype) which is
        // implemented in JavaScript.
        //
        return new comNamespace(this);
    }
}
```

**Namespace Implementation**

Next, create the object which implements the sub-namespace COM on a process.

**Important**  
There can be multiple processes (whether attached to such in user mode or under KD). This extension cannot assume that the present state of the debugger is the what the user intended. Someone can capture &lt;someProcess&gt;.COM in a variable and modify it, which can lead to presenting information from the wrong process context. The solution is to add code in the extension so that each instantiation will keep track of what process it is attached to. For this code sample, this information is passed via the 'this' pointer of the property.

`this.__process = process;`

```javascript
class comNamespace
{
    constructor(process)
    {
        //
        // This is an entirely JavaScript object.  Each instantiation of a comNamespace will keep track
        // of what process it is attached to (passed via the ''this'' pointer of the property getter
        // we authored above.
        //
        this.__process = process;
    }
    
    get GlobalObjects()
    {
        return new globalObjects(this.__process);
    }
}
```

**Implementation logic for the COM global interface table**

To separate this out the implementation logic for the COM global interface table more clearly, we'll define one ES6 class, *gipTable* which abstracts away the COM GIP table and another, *globalObjects*, which is what will get returned from the GlobalObjects() getter defined in the Namespace Implementation code snip shown above. All of these details can be hidden inside the closure of initializeScript to avoid publishing any of these internal details out into the debugger namespace.

```javascript
// gipTable:
//
// Internal class which abstracts away the GIP Table.  It iterates objects of the form
// {entry : GIPEntry, cookie : GIT cookie}
//
class gipTable
{
    constructor(gipProcess)
    {
        //
        // Windows 8 through certain builds of Windows 10, it's in CGIPTable::_palloc.  In certain builds
        // of Windows 10 and later, this has been moved to GIPEntry::_palloc.  We need to check which.
        //
        var gipAllocator = undefined;
        try
        {
            gipAllocator = host.getModuleSymbol("combase.dll", "CGIPTable::_palloc", "CPageAllocator", gipProcess)._pgalloc;
        }
        catch(err)
        {
        }

        if (gipAllocator == undefined)
        {
            gipAllocator = host.getModuleSymbol("combase.dll", "GIPEntry::_palloc", "CPageAllocator", gipProcess)._pgalloc;
        }

        this.__data = {
            process : gipProcess,
            allocator : gipAllocator,
            pageList : gipAllocator._pPageListStart,
            pageCount : gipAllocator._cPages,
            entriesPerPage : gipAllocator._cEntriesPerPage,
            bytesPerEntry : gipAllocator._cbPerEntry,
            PAGESHIFT : 16,
            PAGEMASK : 0x0000FFFF,
            SEQNOMASK : 0xFF00
        };
    }

    *[Symbol.iterator]()
    {
        for (var pageNum = 0; pageNum < this.__data.pageCount; ++pageNum)
        {
            var page = this.__data.pageList[pageNum];
            for (var entryNum = 0; entryNum < this.__data.entriesPerPage; ++entryNum)
            {
                var entryAddress = page.address.add(this.__data.bytesPerEntry * entryNum);
                var gipEntry = host.createPointerObject(entryAddress, "combase.dll", "GIPEntry *", this.__data.process);
                if (gipEntry.cUsage != -1 && gipEntry.dwType != 0)
                {
                    yield {entry : gipEntry, cookie : (gipEntry.dwSeqNo | (pageNum << this.__data.PAGESHIFT) | entryNum)};
                }
            }
        }
    }

    entryFromCookie(cookie)
    {
        var sequenceNo = (cookie & this.__data.SEQNOMASK);
        cookie = cookie & ~sequenceNo;
        var pageNum = (cookie >> this.__data.PAGESHIFT);
        if (pageNum < this.__data.pageCount)
        {
            var page = this.__data.pageList[pageNum];
            var entryNum = (cookie & this.__data.PAGEMASK);
            if (entryNum < this.__data.entriesPerPage)
            {
                var entryAddress = page.address.add(this.__data.bytesPerEntry * entryNum);
                var gipEntry = host.createPointerObject(entryAddress, "combase.dll", "GIPEntry *", this.__data.process);
                if (gipEntry.cUsage != -1 && gipEntry.dwType != 0 && gipEntry.dwSeqNo == sequenceNo)
                {
                    return {entry : gipEntry, cookie : (gipEntry.dwSeqNo | (pageNum << this.__data.PAGESHIFT) | entryNum)};
                }
            }
        }

        //
        // If this exception flows back to C/C++, it will be a failed HRESULT (according to the type of error -- here E_BOUNDS)
        // with the message being encapsulated by an error object.
        //
        throw new RangeError("Unable to find specified value");
    }
}
// globalObjects:
//
// The class which presents how we want the GIP table to look to the data model.  It iterates the actual objects
// in the GIP table indexed by their cookie.
//
class globalObjects
{
    constructor(process)
    {
        this.__gipTable = new gipTable(process);
    }

    *[Symbol.iterator]()
    {
        for (var gipCombo of this.__gipTable)
        {
            yield new host.indexedValue(gipCombo.entry.pUnk, [gipCombo.cookie]);
        }
    }

    getDimensionality()
    {
        return 1;
    }

    getValueAt(cookie)
    {
        return this.__gipTable.entryFromCookie(cookie).entry.pUnk;
    }
}
```

Lastly, use host.namedModelRegistration to register the new COM functionality.

```javascript
function initializeScript()
{
    return [new host.namedModelParent(comProcessExtension, "Debugger.Models.Process"),
            new host.namedModelRegistration(comNamespace, "Debugger.Models.ComProcess")];
}
```

Save the code to GipTableAbstractor.js using an application such as notepad.

Here is the process information available in user mode before loading this extension.

```dbgcmd
0:000:x86> dx @$curprocess
@$curprocess                 : DataBinding.exe
    Name             : DataBinding.exe
    Id               : 0x1b9c
    Threads         
    Modules  
```

Load the JavaScript extension.

```dbgcmd
0:000:x86> .scriptload C:\JSExtensions\GipTableAbstractor.js
JavaScript script successfully loaded from 'C:\JSExtensions\GipTableAbstractor.js'
```

Then use the dx command to display information about the process using the predefined @$curprocess.

```dbgcmd
0:000:x86> dx @$curprocess
@$curprocess                 : DataBinding.exe
    Name             : DataBinding.exe
    Id               : 0x1b9c
    Threads         
    Modules         
    COM              : [object Object]
```

```dbgcmd
0:000:x86> dx @$curprocess.COM
@$curprocess.COM                 : [object Object]
    GlobalObjects    : [object Object]
0:000:x86> dx @$curprocess.COM.GlobalObjects
@$curprocess.COM.GlobalObjects                 : [object Object]
    [0x100]          : 0x12f4fb0 [Type: IUnknown *]
    [0x201]          : 0x37cfc50 [Type: IUnknown *]
    [0x302]          : 0x37ea910 [Type: IUnknown *]
    [0x403]          : 0x37fcfe0 [Type: IUnknown *]
    [0x504]          : 0x12fe1d0 [Type: IUnknown *]
    [0x605]          : 0x59f04e8 [Type: IUnknown *]
    [0x706]          : 0x59f0eb8 [Type: IUnknown *]
    [0x807]          : 0x59f5550 [Type: IUnknown *]
    [0x908]          : 0x12fe340 [Type: IUnknown *]
    [0xa09]          : 0x5afcb58 [Type: IUnknown *]
```

This table is also programmatically accessible via GIT cookie.

```dbgcmd
0:000:x86> dx @$curprocess.COM.GlobalObjects[0xa09]
@$curprocess.COM.GlobalObjects[0xa09]                 : 0x5afcb58 [Type: IUnknown *]
    [+0x00c] __abi_reference_count [Type: __abi_FTMWeakRefData]
    [+0x014] __capture        [Type: Platform::Details::__abi_CapturePtr]
```

**Extending Debugger Object Concepts with LINQ**

In addition to being able to extend objects like process and thread, JavaScript can extend concepts associated with the data model as well. For example, it is possible to add a new LINQ method to every iterable. Consider an example extension, "DuplicateDataModel" which duplicates every entry in an iterable N times. The following code shows how this could be implemented.

```javascript
function initializeScript()
{
    var newLinqMethod =
    {
        Duplicate : function *(n)
        {
            for (var val of this)
            {
                for (var i = 0; i < n; ++i)
                {
                    yield val;
                }
            };
        }
    };

    return [new host.namedModelParent(newLinqMethod, "DataModel.Models.Concepts.Iterable")];
}
```

Save the code to DuplicateDataModel.js using an application such as notepad.

Load the JavaScript scripting provider if necessary and then load the DuplicateDataModel.js extension.

```dbgcmd
0:000:x86> !load jsprovider.dll
0:000:x86> .scriptload C:\JSExtensions\DuplicateDataModel.js
JavaScript script successfully loaded from 'C:\JSExtensions\DuplicateDataModel.js'
```

Use the dx command to test the new Duplicate function.

```dbgcmd
0: kd> dx -r1 Debugger.Sessions.First().Processes.First().Threads.Duplicate(2),d
Debugger.Sessions.First().Processes.First().Threads.Duplicate(2),d                 : [object Generator]
    [0]              : nt!DbgBreakPointWithStatus (fffff800`9696ca60) 
    [1]              : nt!DbgBreakPointWithStatus (fffff800`9696ca60) 
    [2]              : intelppm!MWaitIdle+0x18 (fffff805`0e351348) 
    [3]              : intelppm!MWaitIdle+0x18 (fffff805`0e351348) 
…
```

## See also

[Native Debugger Objects in JavaScript Extensions - Debugger Object Details](native-objects-in-javascript-extensions-debugger-objects.md)

[Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations](native-objects-in-javascript-extensions-design-considerations.md)

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)
