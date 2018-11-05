---
title: Native Debugger Objects in JavaScript Extensions
description: Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions.
ms.assetid: A8E12564-D083-43A7-920E-22C4D627FEE8
ms.author: domars
ms.date: 12/22/2017
ms.localizationpriority: medium
---

# Native Debugger Objects in JavaScript Extensions


Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions to manipulate the state of the debugger.

Example debugger objects include the following.

-   Session
-   Threads / Thread
-   Processes / Process
-   Stack Frames / Stack Frame
-   Local Variables
-   Modules / Module
-   Utility
-   State
-   Settings

For example the host.namespace.Debugger.Utility.Control.ExecuteCommand object can be used to send the u command to the debugger with following two lines of JavaScript code.

```dbgcmd
var ctl = host.namespace.Debugger.Utility.Control;   
var outputLines = ctl.ExecuteCommand("u");
```

This topic describes how to work with common objects and provides reference information on their attributes and behaviors.

[Extending the Debugger via the Data Model](#extending)

[Extending a Debugger Object in JavaScript](#extending-debugger-object)

[Debugger Objects in JavaScript Extensions](#debugger-objects)

[Host APIs for JavaScript Extensions](#host-apis)

[Data Model Concepts in JavaScript](#data-model)

[Debugger Data Model Design Considerations](#design-considerations)

For general information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md). For JavaScript examples that use the debugger objects, see [JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md). For information about working with the settings objects, see [**.settings (Set Debug Settings)**](-settings--set-debug-settings-.md).

To explore the objects available in a debugger session, use the [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md) command. For example, you can display some of the top level debugger objects with this dx command.

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

## <span id="Extending"></span><span id="extending"></span><span id="EXTENDING"></span>Extending the Debugger via the Data Model


The debugger data model allows for the creation of an interface to information about applications and drivers in Windows that has the following attributes.

-   Is discoverable and organized- a logically structured name space can be queried using the dx command.
-   Can be queried using LINQ- This allows for extraction and sorting of data using a standard query language.
-   Can be logically and consistently extended - Extensible using techniques described in this topic with debugger scripting providers such as Natvis and JavaScript.

## <span id="Extending-Debugger-Object"></span><span id="extending-debugger-object"></span><span id="EXTENDING-DEBUGGER-OBJECT"></span>Extending a Debugger Object in JavaScript


In addition to being able to create a visualizer in JavaScript, script extensions can also modify the core concepts of the debugger - sessions, processes, threads, stacks, stack frames, local variables - and even publish themselves as extension points that other extensions can consume.

This section describes how to extend a core concept within the debugger. Extensions which are built to be shared should conform to the guidelines presented in [Debugger Data Model Design Considerations](#design-considerations).

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

|                                |                                                                                              |
|--------------------------------|----------------------------------------------------------------------------------------------|
| Debugger.Models.Sessions       | The list of sessions (targets) that the debugger is attached to                              |
| Debugger.Models.Session        | An individual session (target) that the debugger is attached to (live user mode, KD, etc...) |
| Debugger.Models.Processes      | The list of processes within a session                                                       |
| Debugger.Models.Threads        | The list of threads within a process                                                         |
| Debugger.Models.Thread         | An individual thread within a process (regardless of whether user or kernel mode)            |
| Debugger.Models.Stack          | The stack of a thread                                                                        |
| Debugger.Models.StackFrames    | The collection of frames which make up a stack                                               |
| Debugger.Models.StackFrame     | An individual stack frame within a stack                                                     |
| Debugger.Models.LocalVariables | The local variables within a stack frame                                                     |
| Debugger.Models.Parameters     | The parameters for a call within a stack frame                                               |
| Debugger.Models.Module         | An individual module within the address space of a process                                   |

 

**Addtional Data Model Objects**

In addition, there are some additional data model objects that are defined by the core data model.

|                                             |                                                               |
|---------------------------------------------|---------------------------------------------------------------|
| DataModel.Models.Intrinsic                  | An intrinsic value (ordinals, floats, etc...)                 |
| DataModel.Models.String                     | A string                                                      |
| DataModel.Models.Array                      | A native array                                                |
| DataModel.Models.Guid                       | A GUID                                                        |
| DataModel.Models.Error                      | An error object                                               |
| DataModel.Models.Concepts.Iterable          | Applied to every object which is iterable                     |
| DataModel.Models.Concepts.StringDisplayable | Applied to every object which has a display string conversion |

 

**Example COM Debugger Object Extension Overview**

Let's consider an example. Imagine that you want to create a debugger extension to display information specific to COM, such as the global interface table (GIT).

In the past, there might be an existing debugger extension with a number of commands which provide a means to access things about COM. One command might display process centric information (the global interface table for instance). Another command might provide thread centric information such as what apartment code is executing within. You might need to know about and load a second debugger extension to explore other aspects of COM.

Instead of having a set of hard to discover commands, a JavaScript extension can modify the debugger's concept of what a process and a thread is, to add this information in a way that's natural, explorable, and composable with other debugger extensions.

**User or Kernel Mode Debugger Object Extension**

The debugger and the debugger objects have different behavior in user and kernel mode. When you create your debugger model objects you need to decide which environments you will be working in. Because we will be working with COM in user mode, we will create and test this com extension in user mode. In other situations, you may be able to create a debugger JavaScript that will work in both user and kernel mode debugging.

**Creating a Sub-Namespace**

Going back to our example, we can define a prototype or ES6 class, *comProcessExtension* which contains the set of things we want to add to a process object.

**Important**   The intent with the sub-namespace is to create a logically structured and naturally explorable paradigm. For example, avoid dumping unrelated items into the same sub-namespace. Carefully review the information discussed in [Debugger Data Model Design Considerations](#design-considerations) before creating a sub-namespace.

 

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

Load the JavaScript scripting provider and the extension.

```dbgcmd
0:000:x86> !load jsprovider.dll
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

## <span id="Debugger-Objects"></span><span id="debugger-objects"></span><span id="DEBUGGER-OBJECTS"></span>Debugger Objects in JavaScript Extensions


**Passing Native Objects**

Debugger objects can be passed into or acquired in JavaScript extensions in a variety of ways.

-   They can be passed to JavaScript functions or methods
-   They can be the instance object for a JavaScript prototype (as a visualizer, for instance)
-   They can be returned from host methods designed to create native debugger objects
-   They can be returned from host methods designed to create debugger native objects

Debugger objects that are passed to a JavaScript extension have a set of functionality that is described in this section.

-   Property Access
-   Projected Names
-   Special Types Pertaining to Native Debugger Objects
-   Additional Attributes

**Property Access**

While there are some properties on objects which are placed there by the JavaScript provider itself, the majority of properties on a native object which enters JavaScript are provided by the data model. This means that for a property access --- object.propertyName or object\[propertyName\], the following will occur.

-   If *propertyName* is the name of a property projected onto the object by the JavaScript provider itself, it will resolve to this first; otherwise
-   If *propertyName* is the name of a key projected onto the object by the data model (another Visualizer), it will resolve to this name second; otherwise
-   If *propertyName* is the name of a field of the native object, it will resolve to this name third; otherwise
-   If object is a pointer, the pointer will be dereferenced, and the cycle above will continue (a projected property of the dereferenced object followed by a key followed by a native field)

The normal means of property access in JavaScript -- object.propertyName and object\[propertyName\] -- will access the underlying native fields of an object, much as the 'dx' command would within the debugger.

**Projected Names**

The following properties (and methods) are projected onto native objects which enter JavaScript.

| Method             | Signature                  | Description                                                                                                                                |
|--------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| hostContext        | Property                   | Returns an object which represents the context the object is within (the address space, debug target, etc...)                              |
| targetLocation     | Property                   | Returns an object which is an abstraction of where the object is within an address space (virtual address, register, sub-register, etc...) |
| targetSize         | Property                   | Returns the size of the object (effectively: sizeof(&lt;TYPE OF OBJECT&gt;)                                                                |
| addParentModel     | .addParentModel(object)    | Adds a new parent model (akin to a JavaScript prototype but on the data mdoel side) to the object                                          |
| removeParentModel  | .removeParentModel(object) | Removes a given parent model from the object                                                                                               |
| runtimeTypedObject | Property                   | Performs analysis on the object and tries to convert it to the runtime (most derived) type                                                 |

 

If the object is a pointer, the following properties (and methods) are projected onto the pointer which enters JavaScript:

| Property Name | Signature      | Description                                                                    |
|---------------|----------------|--------------------------------------------------------------------------------|
| add           | .add(value)    | Performs pointer math addition between the pointer and the specified value     |
| address       | Property       | Returns the address of the pointer as a 64-bit ordinal object (a library type) |
| dereference   | .dereference() | Dereferences the pointer and returns the underlying object                     |
| isNull        | Property       | Returns whether or not the pointer value is nullptr (0)                        |

 

**Special Types Pertaining to Native Debugger Objects**

**Location Objects**

The location object which is returned from the targetLocation property of a native object contains the following properties (and methods).

| Property Name | Signature        | Description                                          |
|---------------|------------------|------------------------------------------------------|
| add           | .add(value)      | Adds an absolute byte offset to the location.        |
| subtract      | .subtract(value) | Subtracts an absolute byte offset from the location. |

 

**Additional Attributes**

**Iterability**

Any object which is understood as iterable by the data model (it is a native array or it has a visualizer (NatVis or otherwise) which makes it iterable) will have an iterator function (indexed via the ES6 standard Symbol.iterator) placed upon it. This means that you can iterate a native object in JavaScript as follows.

```javascript
function iterateNative(nativeObject)
{
    for (var val of nativeObject)
    {
        // 
        // val will contain each element iterated from the native object.  This would be each element of an array,
        // each element of an STL structure which is made iterable through NatVis, each element of a data structure
        // which has a JavaScript iterator accessible via [Symbol.iterator], or each element of something
        // which is made iterable via support of IIterableConcept in C/C++.
        //
    }
}
```

**Indexability**

Objects which are understood as indexable in one dimension via ordinals (e.g.: native arrays) will be indexable in JavaScript via the standard property access operator -- object\[index\]. If an object is indexable by name or is indexable in more than one dimension, the getValueAt and setValueAt methods will be projected onto the object so that JavaScript code can utilize the indexer.

```javascript
function indexNative(nativeArray)
{
    var first = nativeArray[0];
}
```

**String Conversion**

Any native object which has a display string conversion via support of IStringDisplayableConcept or a NatVis DisplayString element will have that string conversion accessible via the standard JavaScript toString method.

```javascript
function stringifyNative(nativeObject)
{
    var myString = nativeObject.toString();
}
```

## <span id="Creating_Native_Debugger_Objects"></span><span id="creating_native_debugger_objects"></span><span id="CREATING_NATIVE_DEBUGGER_OBJECTS"></span>Creating Native Debugger Objects


As mentioned, a JavaScript script can get access to native objects by having them passed into JavaScript in one of several ways or it can create them through calls to the host library. Use the following functions to create native debugger objects.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Signature</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>host.getModuleSymbol</p></td>
<td align="left"><p>getModuleSymbol(moduleName, symbolName, [contextInheritor])</p>
<p>getModuleSymbol(moduleName, symbolName, [typeName], [contextInheritor])</p></td>
<td align="left"><p>Returns an object for a global symbol within a particular module. The module name and symbol name are strings.</p>
<p>If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger&#39;s current context. A JavaScript extension which is not a one-off test script should always supply an explicit context.</p>
<p>If the optional <em>typeName</em> argument is supplied, the symbol will be assumed to be of the passed type and the type indicated in symbol(s) will be ignored. Note that any caller which expects to operate on public symbols for a module should always supply an explicit type name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>host.createPointerObject</p></td>
<td align="left"><p>createPointerObject(address, moduleName, typeName, [contextInheritor])</p></td>
<td align="left"><p>Creates a pointer object at the specified address or location. The module name and type name are strings.</p>
<p>If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger&#39;s current context. A JavaScript extension which is not a one-off test script should always supply an explicit context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>host.createTypedObject</p></td>
<td align="left"><p>createTypedObject(location, moduleName, typeName, [contextInheritor])</p></td>
<td align="left"><p>Creates a object which represents a native typed object within the address space of a debug target at the specified location. The module name and type name are strings.</p>
<p>If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger&#39;s current context. A JavaScript extension which is not a one-off test script should always supply an explicit context.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Host-APIs"></span><span id="host-apis"></span><span id="HOST-APIS"></span>Host APIs for JavaScript Extensions


The JavaScript provider inserts an object called host into the global namespace of every script which it loads. This object provides access to critical functionality for the script as well as access to the namespace of the debugger. It is set up in two phases.

-   **Phase 1**: Before any script executes, the host object only contains the minimal set of functionality necessary for a script to initialize itself and register its extensibility points (both as producer and consumer). The root and initialization code is not intended to manipulate the state of a debug target or perform complex operations and, as such, the host is not fully populated until after the initializeScript method returns.

-   **Phase 2**: After initializeScript returns, the host object is populated with everything necessary to manipulate the state of debug targets.

**Host Object Level**

A few key pieces of functionality are directly under the host object. The remainder are sub-namespaced. Namespaces include the following.

| Namespace   | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| diagnostics | Functionality to assist in the diagnosis and debugging of script code    |
| memory      | Functionality to enable memory reading and writing within a debug target |

 

**Root Level**

Directly within the host object, the following properties, methods, and constructors can be found.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Signature</th>
<th align="left">Phase Present</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">createPointerObject</td>
<td align="left"><p>createPointerObject(address, moduleName, typeName, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">Creates a pointer object at the specified address or location. The module name and type name are strings. The optional <strong>contextInheritor</strong> argument works as with getModuleSymbol.</td>
</tr>
<tr class="even">
<td align="left">createTypedObject</td>
<td align="left"><p>createTypedObject(location, moduleName, typeName, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">Creates a object which represents a native typed object within the address space of a debug target at the specified location. The module name and type name are strings. The optional contextInheritor argument works as with getModuleSymbol.</td>
</tr>
<tr class="odd">
<td align="left">currentProcess</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Returns the object representing the current process of the debugger</td>
</tr>
<tr class="even">
<td align="left">currentSession</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Returns the object representing the current session of the debugger (which target, dump, etc...) is being debugged</td>
</tr>
<tr class="odd">
<td align="left">currentThread</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Returns the object representing the current thread of the debugger</td>
</tr>
<tr class="even">
<td align="left">evaluateExpression</td>
<td align="left"><p>evaluateExpression(expression, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This calls into the debug host to evaluate an expression using the language of the debug target only. If the optional <em>contextInheritor</em> argument is supplied, the expression will be evaluated in the context (e.g.: address space and debug target) of the argument; otherwise, it will be evaluated in the current context of the debugger</td>
</tr>
<tr class="odd">
<td align="left">evaluateExpressionInContext</td>
<td align="left"><p>evaluateExpressionInContext(context, expression)</p></td>
<td align="left">2</td>
<td align="left">This calls into the debug host to evaluate an expression using the language of the debug target only. The context argument indicates the implicit this pointer to utilize for the evaluation. The expression will be evaluated in the context (e.g.: address space and debug target) indicated by the <em>context</em> argument.</td>
</tr>
<tr class="even">
<td align="left">getModuleSymbol</td>
<td align="left"><p>getModuleSymbol(moduleName, symbolName, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">Returns an object for a global symbol within a particular module. The module name and symbol name are strings. If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger&#39;s current context. A JavaScript extension which is not a one-off script should always supply an explicit context</td>
</tr>
<tr class="odd">
<td align="left">getNamedModel</td>
<td align="left"><p>getNamedModel(modelName)</p></td>
<td align="left">2</td>
<td align="left">Returns the data model which was registered against a given name. Note that it is perfectly legal to call this against a name which is not yet registered. Doing so will create a stub for that name and manipulations of the stub will be made to the actual object upon registration</td>
</tr>
<tr class="even">
<td align="left">indexedValue</td>
<td align="left"><p>new indexedValue(value, indicies)</p></td>
<td align="left">2</td>
<td align="left">A constructor for an object which can be returned from a JavaScript iterator in order to assign a default set of indicies to the iterated value. The set of indicies must be expressed as a JavaScript array.</td>
</tr>
<tr class="odd">
<td align="left">Int64</td>
<td align="left"><p>new Int64(value, [highValue])</p></td>
<td align="left">1</td>
<td align="left">This constructs a library Int64 type. The single argument version will take any value which can pack into an Int64 (without conversion) and place it into such. If an optional second argument is supplied, a conversion of the first argument is packed into the lower 32-bits and a conversion of the second argument is packed into the upper 32 bits.</td>
</tr>
<tr class="even">
<td align="left">namedModelParent</td>
<td align="left"><p>new namedModelParent(object, name)</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents using a JavaScript prototype or ES6 class as a data model parent extension of a data model with the given name</td>
</tr>
<tr class="odd">
<td align="left">namedModelRegistration</td>
<td align="left"><p>new namedModelRegistration(object, name)</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents the registration of a JavaScript prototype or ES6 class as a data model via a known name so that other extensions can find and extend</td>
</tr>
<tr class="even">
<td align="left">namespace</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Gives direct access to the root namespace of the debugger. One could, for example, access the process list of the first debug target via host.namespace.Debugger.Sessions.First().Processes using this property</td>
</tr>
<tr class="odd">
<td align="left">registerNamedModel</td>
<td align="left"><p>registerNamedModel(object, modelName)</p></td>
<td align="left">2</td>
<td align="left">This registers a JavaScript prototype or ES6 class as a data model under the given name. Such a registration allows the prototype or class to be located and extended by other scripts or other debugger extensions. Note that a script should prefer to return a <strong>namedModelRegistration</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>initializeScript</strong> method in order to clean up.</td>
</tr>
<tr class="even">
<td align="left">registerExtensionForTypeSignature</td>
<td align="left"><p>registerExtensionForTypeSignature(object, typeSignature)</p></td>
<td align="left">2</td>
<td align="left">This registers a JavaScript prototype or ES6 class as an extension data model for a native type as given by the supplied type signature. Note that a script should prefer to return a <strong>typeSignatureExtension</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>initializeScript</strong> method in order to clean up.</td>
</tr>
<tr class="odd">
<td align="left">registerPrototypeForTypeSignature</td>
<td align="left"><p>registerPrototypeForTypeSignature(object, typeSignature)</p></td>
<td align="left">2</td>
<td align="left">This registers a JavaScript prototype or ES6 class as the canonical data model (e.g.: visualizer) for a native type as given by the supplied type signature. Note that a script should prefer to return a <strong>typeSignatureExtension</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>uninitializeScript</strong>method in order to clean up.</td>
</tr>
<tr class="even">
<td align="left">parseInt64</td>
<td align="left"><p>parseInt64(string, [radix])</p></td>
<td align="left">1</td>
<td align="left">This method acts similarly to the standard JavaScript parseInt method except that it returns a library Int64 type instead. If a radix is supplied, the parse will occur in either base 2, 8, 10, or 16 as indicated.</td>
</tr>
<tr class="odd">
<td align="left">typeSignatureExtension</td>
<td align="left"><p>new typeSignatureExtension(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents an extension of a native type described via a type signature by a JavaScript prototype or ES6 class. Such a registration &quot;adds fields&quot; to the debugger&#39;s visualization of any type which matches the signature rather than taking it over entirely. An optional module name and version can restrict the registration. Versions are specified as &quot;1.2.3.4&quot; style strings.</td>
</tr>
<tr class="even">
<td align="left">typeSignatureRegistration</td>
<td align="left"><p>new typeSignatureRegistration(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents a canonical registration of a JavaScript prototype or ES6 class against a native type signature. Such a registration &quot;takes over&quot; the debugger&#39;s visualization of any type which matches the signature rather than merely than extending it. An optional module name and version can restrict the registration. Versions are specified as &quot;1.2.3.4&quot; style strings.</td>
</tr>
<tr class="odd">
<td align="left">unregisterNamedModel</td>
<td align="left"><p>unregisterNamedModel(modelName)</p></td>
<td align="left">2</td>
<td align="left">This unregisters a data model from lookup by the given name undoing any operation performed by <strong>registerNamedModel</strong></td>
</tr>
<tr class="even">
<td align="left">unregisterExtensionForTypeSignature</td>
<td align="left"><p>unregisterExtensionForTypeSignature(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">2</td>
<td align="left">This unregisters a JavaScript prototype or ES6 class from being an extension data model for a native type as given by the supplied type signature. It is the logical undo of registerExtensionForTypeSignature. Note that a script should prefer to return a <strong>typeSignatureExtension</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>initializeScript</strong> method in order to clean up. An optional module name and version can restrict the registration. Versions are specified as &quot;1.2.3.4&quot; style strings.</td>
</tr>
<tr class="odd">
<td align="left">unregisterPrototypeForTypeSignature</td>
<td align="left"><p>unregisterPrototypeForTypeSignature(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">2</td>
<td align="left">This unregisters a JavaScript prototype or ES6 class from being the canonical data model (e.g.: visualizer) for a native type as given by the supplied type signature. It is the logical undo of registerPrototypeForTypeSignature. Note that a script should prefer to return a <strong>typeSignatureRegistration</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>uninitializeScript</strong> method in order to clean up. An optional module name and version can restrict the registration. Versions are specified as &quot;1.2.3.4&quot; style strings.</td>
</tr>
</tbody>
</table>

 

**Diagnostics Functionality**

The diagnostics sub-namespace of the host object contains the following.

| Name     | Signature           | Phase Present | Description                                                                                                                                                                                                                                                                                                                                                   |
|----------|---------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| debugLog | debugLog(object...) | 1             | This provides printf style debugging to a script extension. At present, output from debugLog is routed to the output console of the debugger. At a later point in time, there are plans to provide flexibility on routing this output. NOTE: This should not be used as a means of printing user output to console. It may not be routed there in the future. |

 

**Memory Functionality**

The memory sub-namespace of the host object contains the following.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Signature</th>
<th align="left">Phase Present</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">readMemoryValues</td>
<td align="left"><p>readMemoryValues(location, numElements, [elementSize], [isSigned], [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This reads a raw array of values from the address space of the debug target and places a typed array on top of the view of this memory. The supplied location can be an address (a 64-bit value), a location object, or a native pointer. The size of the array is indicated by the <em>numElements</em> argument. The size (and type) of each element of the array is given by the optional <em>elementSize</em> and <em>isSigned</em> arguments. If no such arguments are supplied, the default is byte (unsigned / 1 byte). If the optional <em>contextInheritor</em> argument is supplied, memory will be read in the context (e.g.: address space and debug target) indicated by the argument; otherwise, it will be read from the debugger&#39;s current context. Note that using this method on 8, 16, and 32-bit values results in a fast typed view being placed over the read memory. Using this method on 64-bit values results in an array of 64-bit library types being constructed which is significantly more expensive!</td>
</tr>
<tr class="even">
<td align="left">readString</td>
<td align="left"><p>readString(location, [contextInheritor])</p>
<p>readString(location, [length], [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This reads a narrow (current code page) string from the address space of a debug target, converts it to UTF-16, and returns the result as a JavaScript string. It may throw an exception if the memory could not be read. The supplied location can be an address (a 64-bit value), a location object, or a native char<em>. If the optional <em>contextInheritor</em> argument is supplied, memory will be read in the context (e.g.: address space and debug target) indicated by the argument; otherwise, it will be read from the debugger&#39;s current context. If the optional <em>length</em> argument is supplied, the read string will be of the specified length.</td>
</tr>
<tr class="odd">
<td align="left">readWideString</td>
<td align="left"><p>readWideString(location, [contextInheritor])</p>
<p>readWideString(location, [length], [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This reads a wide(UTF-16) string from the address space of a debug target and returns the result as a JavaScript string. It may throw an exception if the memory could not be read. The supplied location can be an address (a 64-bit value), a location object, or a native wchar_t</em>. If the optional <em>contextInheritor</em> argument is supplied, memory will be read in the context (e.g.: address space and debug target) indicated by the argument; otherwise, it will be read from the debugger&#39;s current context. If the optional <em>length</em> argument is supplied, the read string will be of the specified length.</td>
</tr>
</tbody>
</table>

 

## <span id="Data-Model"></span><span id="data-model"></span><span id="DATA-MODEL"></span>Data Model Concepts in JavaScript


**Data Model Mapping**

The following data model concepts map to JavaScript.

| Concept                 | Native Interface             | JavaScript Equivalent                                                |
|-------------------------|------------------------------|----------------------------------------------------------------------|
| String Conversion       | IStringDisplayableConcept    | standard: toString(...){...}                                         |
| Iterability             | IIterableConcept             | standard: \[Symbol.iterator\](){...}                                 |
| Indexability            | IIndexableConcept            | protocol: getDimensionality(...) / getValueAt(...) / setValueAt(...) |
| Runtime Type Conversion | IPreferredRuntimeTypeConcept | protocol: getPreferredRuntimeTypedObject(...)                        |

 

**String Conversion**

The string conversion concept (IStringDisplayableConcept) directly translates to the standard JavaScript **toString** method. As all JavaScript objects have a string conversion (provided by Object.prototype if not provided elsewhere), every JavaScript object returned to the data model can be converted to a display string. Overriding the string conversion simply requires implementing your own toString.

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IStringDisplayableConcept::ToDisplayString(...)
    //
    toString()
    { 
        return "This is my own string conversion!";
    }
}
```

**Iterability**

The data model's concept of whether an object is iterable or not maps directly to the ES6 protocol of whether an object is iterable. Any object which has a \[Symbol.iterator\] method is considered iterable. Implementation of such will make the object iterable.

An object which is only iterable can have an implementation such as follows.

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IIterableConcept::GetIterator
    //
    *[Symbol.iterator]()
    {
        yield "First Value";
        yield "Second Value";
        yield "Third Value";
    }
}
```

Special consideration must be given for objects which are both iterable and indexable as the objects returned from the iterator must include the index as well as the value via a special return type.

**Iterable and Indexable**

An object which is iterable and indexable requires a special return value from the iterator. Instead of yielding the values, the iterator yields instances of indexedValue. The indicies are passed as an array in the second argument to the indexedValue constructor. They can be multi-dimensional but must match the dimensionality returned in the indexer protocol.

This code shows an example implementaion.

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IIterableConcept::GetIterator
    //
    *[Symbol.iterator]()
    {
        //
        // Consider this a map which mapped 42->"First Value", 99->"Second Value", and 107->"Third Value"
        //
        yield new host.indexedValue("First Value", [42]);
        yield new host.indexedValue("Second Value", [99]);
        yield new host.indexedValue("Third Value", [107]);
    }
}
```

**Indexability**

Unlike JavaScript, the data model makes a very explicit differentiation between property access and indexing. Any JavaScript object which wishes to present itself as indexable in the data model must implement a protocol consisting of a getDimensionality method which returns the dimensionality of the indexer and an optional pair of getValueAt and setValueAt methods which perform reads and writes of the object at supplied indicies. It is acceptable to omit either the getValueAt or setValueAt methods if the object is read-only or write-only

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IIndexableConcept::GetDimensionality or IIterableConcept::GetDefaultIndexDimensionality
    //
    getDimensionality()
    {
        //
        // Pretend we are a two dimensional array.
        //
        return 2;
    } 

    //
    // This method will be called whenever any native code calls IIndexableConcept::GetAt
    //
    getValueAt(row, column)
    {
        return this.__values[row * this.__columnCount + column];
    }

    //
    // This method will be called whenever any native code calls IIndexableConcept::SetAt
    //
    setValueAt(value, row, column)
    {
        this.__values[row * this.__columnCount + column] = value;
    }
}
```

**Runtime Type Conversion**

This is only relevant for JavaScript prototypes/classes which are registered against type system (native) types. The debugger is often capable of performing analysis (e.g. Run-Time Type Information (RTTI) / v-table analysis) to determine the true runtime type of an object from a static type expressed in code. A data model registered against a native type can override this behavior via an implementation of the IPreferredRuntimeTypeConcept. Likewise, a JavaScript class or prototype registered against a native object can provide its own implementation via implementation of a protocol consisting of the getPreferredRuntimeTypedObject method.

Note that while this method can technically return anything, it is considered bad form for it to return something which isn't really the runtime type or a derived type. Such can result in significant confusion for users of the debugger. Overriding this method can, however, be valuable for things such as C-style header+object styles of implementation, etc...

```javascript
class myNativeModel
{
    //
    // This method will be called whenever the data model calls IPreferredRuntimeTypeConcept::CastToPreferredRuntimeType
    //
    getPreferredRuntimeTypedObject()
    {
        var loc = this.targetLocation;

        //
        // Perform analysis...
        //
        var runtimeLoc = loc.Add(runtimeObjectOffset);
  
        return host.createTypedObject(runtimeLoc, runtimeModule, runtimeTypeName);
    }
}
```

## <span id="Design-Considerations"></span><span id="design-considerations"></span><span id="DESIGN-CONSIDERATIONS"></span>Debugger Data Model Design Considerations


**Design Principles**

Consider the following principles to make your debugger extensions present information that is discoverable, queryable, and scriptable.

-   Information is close to where it is needed. For example, information on a registry key should be displayed as part of a local variable that contains a registry key handle.
-   Information is structured. For example, information about a registry key is presented in separate fields such as key type, key ACL, key name, and value. This means that the individual fields can be accessed without parsing text.
-   Information is consistent. Information about registry key handles is presented in as similar a way as possible to information about file handles.

Avoid these approaches that do not support these principles.

-   Do not structure your items into a single flat "Kitchen sink". An organized hierarchy allows users to browse for the information they are looking for without prior knowledge of what they are looking for and supports discoverability.
-   Do not convert a classic dbgeng extension by simply moving it to the model while still outputting screens of raw text. This is not composable with other extensions and cannot be queried with LINQ expressions. Instead break the data into separate, queryable fields.

**Naming Guidelines**

-   Capitalization of fields should be PascalCase. An exception could be considered for names that are widely known in another casing, such as jQuery.
-   Avoid using special characters that would not normally be used in a C++ identifier. For example, avoid using names such as "Total Length" (that contains a space), or "\[size\]" (that contains square brackets). This convention allows for easier consumption from scripting languages where these characters are not allowed as part of identifiers, and also allows easier consumption from the command window.

**Organization and Hierarchy Guidelines**

-   Do not extend the top level of the debugger namespace. Instead, you should extend an existing node in the debugger so that the information is displayed where it is most relevant.
-   Do not duplicate concepts. If you are creating a data model extension that lists additional information about a concept that already exists in the debugger, extend the existing information rather than trying to replace it with new information. In other words, an extension that displays details about a module should extend the existing *Module* object rather than creating a new list of modules.
-   Free floating utility commands must be part of the *Debugger.Utility* namespace. They should also be sub-namespaced appropriately (e.g. *Debugger.Utility.Collections.FromListEntry*)

**Backwards Compatibility and Breaking Changes**

A script that is published should not break compatibility with other scripts that depend on it. For example, if a function is published to the model, it should remain in the same location and with the same parameters, whenever possible.

**No Use of Outside Resources**

-   Extensions must not spawn external processes. External processes can interfere with the behavior of the debugger, and will misbehave in various remote debugger scenarios (e.g. dbgsrv remotes, ntsd remotes, and "ntsd -d remotes")
-   Extensions must not display any user interface. Displaying user interface elements will behave incorrectly on remote debugging scenarios, and can break console debugging scenarios.
-   Extensions must not manipulate the debugger engine or debugger UI through undocumented methods. This causes compatibility problems and will behave incorrectly on debugger clients with different UI.
-   Extensions must access target information only through the documented debugger APIs. Trying to access information about a target through win32 APIs will fail for many remote scenarios, and even some local debugging scenarios across security boundaries.

**No Use of Dbgeng Specific Features**

Scripts that are intended to be used as extensions must not rely on dbgeng-specific features whenever possible (such as executing "classic" debugger extensions). Scripts should be usable on top of any debugger that hosts the data model.

## <span id="Testing-Debugger-Extensions"></span><span id="testing-debugger-extensions"></span><span id="TESTING-DEBUGGER-EXTENSIONS"></span>Testing Debugger Extensions


Extensions are expected to work in a wide range of scenarios. While some extensions may be specific to a scenario (such as a kernel debugging scenario), most extensions should be expected to work in all scenarios, or have metadata indicating the supported scenarios.

Kernel Mode

-   Live kernel debugging
-   Kernel dump debugging

User Mode

-   Live user mode debugging
-   User mode dump debugging

In addition, consider these debugger usage scenarios

-   Multi-process debugging
-   Multi-session debugging (e.g. dump + live user within a single session)

**Remote Debugger Usage**

Test for proper operation with the remote debugger usage scenarios.

-   dbgsrv remotes
-   ntsd remotes
-   ntsd -d remotes

For more information, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md) and [**Activating a Process Server**](activating-a-process-server.md).

**Regression testing**

Investigate the use of test automation that can verify the functionality of your extensions, as new versions of the debugger are released.

## <span id="related_topics"></span>Related topics


[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

 

 






