---
title: Using LINQ With the debugger objects
description: Using LINQ With the debugger objects. LINQ syntax can be used with the debugger objects to search and manipulate data.
keywords: ["Using LINQ With the debugger objects"]
ms.author: domars
ms.date: 08/10/2017
ms.localizationpriority: medium
---

# Using LINQ With the debugger objects

LINQ syntax can be used with the debugger objects to search and manipulate data. LINQ is conceptually similar to the Structured Query Language (SQL) that is used to query databases. You can use a number of LINQ methods to search, filter and parse debug data. The LINQ C# method syntax is used. For more information on LINQ and the LINQ C# syntax, see the following topics:

[LINQ (Language-Integrated Query)](https://msdn.microsoft.com/library/bb397926.aspx)

[Getting Started with LINQ in C#](https://msdn.microsoft.com/library/bb397933.aspx)

## Native debugger objects

Native debugger objects represent various constructs and behaviors of the debugger environment. Example debugger objects include the following.

-   Session
-   Threads / Thread
-   Processes / Process
-   Stack Frames / Stack Frame
-   Local Variables
-   Modules / Module
-   Utility
-   State
-   Settings

You can work with the debugger objects with NatVis. For more information see [Native Debugger Objects in NatVis](native-debugger-objects-in-natvis.md). For information about using debugger objects with JavaScript, see [Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

## Dx command

The examples shown here use the dx command, for more information about working with the dx command, see [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).


## Function Objects (Lambda Expressions)

Many of the methods that are used to query data are based on the concept of repeatedly running a user provided function across objects in a collection. To support the ability to query and manipulate data in the debugger, the dx command supports lambda expressions using the equivalent C# syntax. A lambda expression is defined by usage of the =&gt; operator as follows:

(arguments) =&gt; (result)

To see how LINQ is used with dx, try this simple example to add together 5 and 7.

```dbgcmd
kd> dx ((x, y) => (x + y))(5, 7) 
```

The dx command echos back the lambda expression and displays the result of 12.

```dbgcmd
((x, y) => (x + y))(5, 7)  : 12
```

This example lambda expression combines the strings "Hello" and "World".

```dbgcmd
kd> dx ((x, y) => (x + y))("Hello", "World")
((x, y) => (x + y))("Hello", "World") : HelloWorld
```

## Debugger Objects Examples

Debugger objects are projected into a namespace rooted at "Debugger". Processes, modules, threads, stacks, stack frames, and local variables are all available to be used in a LINQ query.

LINQ commands such as the following can be used .All, .Any, .Count, .First, .Flatten, .GroupBy, .Last, .OrderBy, .OrderByDescending, .Select, and .Where. These methods follow (as closely as possible) the C# LINQ method form.

This example shows the top 5 processes running the most threads:

```dbgcmd
0: kd> dx -r2 Debugger.Sessions.First().Processes.Select(p => new { Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.ThreadCount),5
Debugger.Sessions.First().Processes.Select(p => new { Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.ThreadCount),5 

: 
    [0x4]            : 
        Name             : <Unknown Image>
        ThreadCount      : 0x73
    [0x708]          : 
        Name             : explorer.exe
        ThreadCount      : 0x2d
    [0x37c]          : 
        Name             : svchost.exe
        ThreadCount      : 0x2c
    [0x6b0]          : 
        Name             : MsMpEng.exe
        ThreadCount      : 0x22
    [0x57c]          : 
        Name             : svchost.exe
        ThreadCount      : 0x15
    [...]       
```

This example shows the devices in the plug and play device tree grouped by the name of the physical device object's driver. Not all of the output is shown.

```dbgcmd
kd> dx -r2 Debugger.Sessions.First().Devices.DeviceTree.Flatten(n => n.Children).GroupBy(n => n.PhysicalDeviceObject->Driver->DriverName.ToDisplayString())
Debugger.Sessions.First().Devices.DeviceTree.Flatten(n => n.Children).GroupBy(n => n.PhysicalDeviceObject->Driver->DriverName.ToDisplayString()) 

: 
    ["\"\\Driver\\PnpManager\""] : 
        [0x0]            : HTREE\ROOT\0
        [0x1]            : ROOT\volmgr\0000 (volmgr)
        [0x2]            : ROOT\BasicDisplay\0000 (BasicDisplay)
        [0x3]            : ROOT\CompositeBus\0000 (CompositeBus)
        [0x4]            : ROOT\vdrvroot\0000 (vdrvroot)
         ...  
```

## Dx Command Tab Auto Completion

Contextual TAB key auto completion is aware of the LINQ query methods and will work for parameters of lambdas.

As an example, type (or copy and paste) the following text into the debugger. Then hit the TAB key several times to cycle through potential completions.

```dbgcmd
dx -r2 Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.
```

Press the TAB key until ".Name" appears. Add a closing parenthesis ")" and press enter to execute the command.

```dbgcmd
kd> dx -r2 Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.Name)
Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.Name) : 
    [0x274]          : 
        Name             : winlogon.exe
        ThreadCount      : 0x4
    [0x204]          : 
        Name             : wininit.exe
        ThreadCount      : 0x2
    [0x6c4]          : 
        Name             : taskhostex.exe
        ThreadCount      : 0x8
         ...  
```

This example shows completion with a key comparator method. The substitution will show string methods, since the key is a string.

```dbgcmd
dx -r2 Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.Name, (a, b) => a.
```

Press the TAB key until ".Length" appears. Add a closing parenthesis ")" and press enter to execute the command.

```dbgcmd
kd> dx -r2 Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.Name, (a, b) => a.Length)
Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.Name, (a, b) => a.Length) : 
    [0x544]          : 
        Name             : spoolsv.exe
        ThreadCount      : 0xc
    [0x4d4]          : 
        Name             : svchost.exe
        ThreadCount      : 0xa
    [0x438]          : 
        Name             : svchost.exe
```

## User Defined Variables

A user defined variable can be defined by prefixing the variable name with @$. A user defined variable can be assigned to anything dx can utilize, for example, lambdas, the results of LINQ queries, etc.

You can create and set the value of a user variable like this.

```dbgcmd
kd> dx @$String1="Test String"
```

You can display the defined user variables using *Debugger.State.UserVariables* or *@$vars*.

```dbgcmd
kd> dx Debugger.State.UserVariables
Debugger.State.UserVariables : 
    mySessionVar     : 
    String1          : Test String
```

You can remove a variable using .Remove.

```dbgcmd
kd> dx @$vars.Remove("String1")
```

This example shows how to define a user variable to reference Debugger.Sesssions.

```dbgcmd
kd> dx @$mySessionVar = Debugger.Sessions
```

The user defined variable can then be used as shown below.

```dbgcmd
kd> dx -r2 @$mySessionVar 
@$mySessionVar   : 
    [0x0]            : Remote KD: KdSrv:Server=@{<Local>},Trans=@{COM:Port=\\.\com3,Baud=115200,Timeout=4000}
        Processes        : 
        Devices     
```

**User Defined Variables - Anonymous Types**

This creation of dynamic objects is done using the C# anonymous type syntax (new { ... }). For more information see about anonymous types, see [Anonymous Types (C# Programming Guide)](https://msdn.microsoft.com/library/bb397696.aspx). This example create an anonymous type with an integer and string value.

```dbgcmd
kd> dx -r1 new { MyInt = 42, MyString = "Hello World" }
new { MyInt = 42, MyString = "Hello World" } : 
    MyInt            : 42
    MyString         : Hello World
```

## System Defined Variables

The following system defined variables can be used in any LINQ dx query.

-   @$cursession - The current session

-   @$curprocess - The current process

-   @$curthread - The current thread

This example show the use of the system defined variables.

```dbgcmd
kd> dx @$curprocess.Threads.Count()
@$curprocess.Threads.Count() : 0x4
```

```dbgcmd
kd> dx -r1 @$curprocess.Threads
@$curprocess.Threads : 
    [0x4adc]         : 
    [0x1ee8]         : 
    [0x51c8]         : 
    [0x62d8]         : 
     ...
```

## Supported LINQ Syntax - Query Methods

Any object which dx defines as iterable (be that a native array, a type which has NatVis written describing it as a container, or a debugger extension object) has a series of LINQ (or LINQ equivalent) methods projected onto it. Those query methods are described below. The signatures of the arguments to the query methods are listed after all of the query methods.

Filtering Methods

|                            |                                                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| .Where ( PredicateMethod ) | Returns a new collection of objects containing every object in the input collection for which the predicate method returned true. |



Projection Methods

|                                     |                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .Flatten ( \[KeyProjectorMethod\] ) | Takes an input container of containers (a tree) and flattens it into a single container which has every element in the tree. If the optional key projector method is supplied, the tree is considered a container of keys which are themselves containers and those keys are determined by a call to the projection method. |
| .Select ( KeyProjectorMethod )      | Returns a new collection of objects containing the result of calling the projector method on every object in the input collection.                                                                                                                                                                                          |



Grouping Methods

|                                                                                                                            |                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .GroupBy ( KeyProjectorMethod, \[KeyComparatorMethod\] )                                                                   | Returns a new collection of collections by grouping all objects in the input collection having the same key as determined by calling the key projector method. An optional comparator method can be provided. |
| Join (InnerCollection, Outer key selector method, Inner key selector method, Result selector method, \[ComparatorMethod\]) | Joins two sequences based on key selector functions and extracts pairs of values. An optional comparator method can also be specified.                                                                        |
| Intersect (InnerCollection, \[ComparatorMethod\])                                                                          | Returns the set intersection, which means elements that appear in each of two collections. An optional comparator method can also be specified.                                                               |
| Union (InnerCollection, \[ComparatorMethod\])                                                                              | Returns the set union, which means unique elements that appear in either of two collections. An optional comparator method can also be specified.                                                             |



Data Set Methods

|                                                |                                                                                                                                                                                                   |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contains (Object, \[ComparatorMethod\])        | Determines whether a sequence contains a specified element. An optional comparator method can be provided that will be called each time the element is compared against an entry in the sequence. |
| Distinct (\[ComparatorMethod\])                | Removes duplicate values from a collection. An optional comparator method can be provided to be called each time objects in the collection must be compared.                                      |
| Except (InnerCollection, \[ComparatorMethod\]) | Returns the set difference, which means the elements of one collection that do not appear in a second collection. An optional comparator method can be specified.                                 |
| Concat (InnerCollection)                       | Concatenates two sequences to form one sequence.                                                                                                                                                  |



Ordering Methods

|                                                                    |                                                                                                                                                                                                      |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .OrderBy ( KeyProjectorMethod, \[KeyComparatorMethod\] )           | Sorts the collection in ascending order according to a key as provided by calling the key projection method on every object in the input collection. An optional comparator method can be provided.  |
| .OrderByDescending ( KeyProjectorMethod, \[KeyComparatorMethod\] ) | Sorts the collection in descending order according to a key as provided by calling the key projection method on every object in the input collection. An optional comparator method can be provided. |



Aggregating Methods

|                            |                                                                                                                                                |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Count ()                   | A method that returns the number of elements in the collection.                                                                                |
| Sum (\[ProjectionMethod\]) | Calculates the sum of the values in a collection. Can optionally specify a projector method to transform the elements before summation occurs. |



Skip Methods

|                             |                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------|
| Skip (Count)                | Skips elements up to a specified position in a sequence.                                      |
| SkipWhile (PredicateMethod) | Skips elements based on a predicate function until an element does not satisfy the condition. |



Take Methods

|                             |                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------|
| Take (Count)                | Takes elements up to a specified position in a sequence.                                      |
| TakeWhile (PredicateMethod) | Takes elements based on a predicate function until an element does not satisfy the condition. |



Comparison Methods

|                                                       |                                                                                                                                  |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| SequenceEqual (InnerCollection, \[ComparatorMethod\]) | Determines whether two sequences are equal by comparing elements in a pair-wise manner. An optional comparator can be specified. |



Error Handling Methods

|                                     |                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------|
| AllNonError (PredicateMethod)       | Returns whether all non-error elements of a collection satisfy a given condition. |
| FirstNonError (\[PredicateMethod\]) | Returns the first element of a collection that isn’t an error.                    |
| LastNonError (\[PredicateMethod\])  | Returns the last element of a collection that isn’t an error.                     |



Other Methods

|                                |                                                                                                                                                                                                                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .All ( PredicateMethod )       | Returns whether the result of calling the specified predicate method on every element in the input collection is true.                                                                                                                                                       |
| .Any ( PredicateMethod )       | Returns whether the result of calling the specified predicate method on any element in the input collection is true.                                                                                                                                                         |
| .First ( \[PredicateMethod\] ) | Returns the first element in the collection. If the optional predicate is passed, returns the first element in the collection for which a call to the predicate returns true.                                                                                                |
| .Last ( \[PredicateMethod\] )  | Returns the last element in the collection. If the optional predicate is passed, returns the last element in the collection for which a call to the predicate returns true.                                                                                                  |
| Min(\[KeyProjectorMethod\])    | Returns the minimum element of the collection. An optional projector method can be specified to project each method before it is compared to others.                                                                                                                         |
| Max(\[KeyProjectorMethod\])    | Returns the maximum element of the collection. An optional projector method can be specified to project each method before it is compared to others.                                                                                                                         |
| Single(\[PredicateMethod\])    | Returns the only element from the list (or an error if the collection contains more than one element). If a predicate is specified, returns the single element that satisfies that predicate (if more than one element satisfies it, the function returns an error instead). |



**Signatures of the Arguments**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">KeyProjectorMethod : ( obj =&gt; arbitrary key )</td>
<td align="left">Takes an object of the collection and returns a key from that object.</td>
</tr>
<tr class="even">
<td align="left">KeyComparatorMethod: ( (a, b) =&gt; integer value )</td>
<td align="left">Takes two keys and compares them returning:
<p>-1 if ( a &lt; b )</p>
<p>0 if ( a == b)</p>
<p>1 if ( a &gt; b )</p></td>
</tr>
<tr class="odd">
<td align="left">PredicateMethod: ( obj =&gt; boolean value )</td>
<td align="left">Takes an object of the collection and returns true or false based on whether that object meets certain criteria.</td>
</tr>
</tbody>
</table>



## Supported LINQ Syntax - String Manipulation

All string objects have the following methods projected into them, so that they are available for use:

Query Relevant Methods & Properties

|                                     |                                                                                                                                                                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .Contains ( OtherString )           | Returns a boolean value indicating whether the input string contains OtherString.                                                                                                                                                 |
| .EndsWith ( OtherString )           | Returns a boolean value indicating whether the input string ends with OtherString.                                                                                                                                                |
| Length                              | A property which returns the length of the string.                                                                                                                                                                                |
| .StartsWith ( OtherString )         | Returns a boolean value indicating whether the input string starts with OtherString.                                                                                                                                              |
| .Substring ( StartPos, \[Length\] ) | Returns a substring within the input string starting at the given starting position. If the optional length is supplied, the returned substring will be of the specified length; otherwise – it will go to the end of the string. |



Miscellaneous Methods

|                              |                                                                                   |
|------------------------------|-----------------------------------------------------------------------------------|
| .IndexOf ( OtherString )     | Returns the index of the first occurrence of OtherString within the input string. |
| .LastIndexOf ( OtherString ) | Returns the index of the last occurrence of OtherString within the input string.  |



Formatting Methods

|                                          |                                                                                                                                                                                                                                                     |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .PadLeft ( TotalWidth )                  | Adds spaces as necessary to the left side of the string in order to bring the total length of the string to the specified width.                                                                                                                    |
| .PadRight ( TotalWidth )                 | Adds spaces as necessary to the right side of the string in order to bring the total length of the string to the specified width.                                                                                                                   |
| .Remove ( StartPos, \[Length\] )         | Removes characters from the input string starting as the specified starting position. If the optional length parameter is supplied, that number of characters will be removed; otherwise – all characters to the end of the string will be removed. |
| .Replace ( SearchString, ReplaceString ) | Replaces every occurrence of SearchString within the input string with the specified ReplaceString.                                                                                                                                                 |



String Object Projections

In addition to the methods which are projected directly onto string objects, any object which itself has a string conversion has the following method projected onto it, making it method available for use:

|                      |                                                                                                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .ToDisplayString ( ) | Returns a string conversion of the object. This is the string conversion which would be shown in a dx invocation for the object. You can provide a formatting specifier to format the output of ToDisplayString. |



The following examples illustrate the use of format specifiers.

```dbgcmd
kd> dx (10).ToDisplayString("d")
(10).ToDisplayString("d") : 10

kd> dx (10).ToDisplayString("x")
(10).ToDisplayString("x") : 0xa

kd> dx (10).ToDisplayString("o")
(10).ToDisplayString("o") : 012

kd> dx (10).ToDisplayString("b") 
(10).ToDisplayString("b")  : 0y1010
```

## <span id="Debugging_Plug_and_Play"></span><span id="debugging_plug_and_play"></span><span id="DEBUGGING_PLUG_AND_PLAY"></span>Debugging Plug and Play Example


This section illustrates how the built in debugger objects used with LINQ queries, can be used to debug plug and play objects.

**View all devices**

Use *Flatten* on the device tree to view all devices. 

```dbgcmd
 1: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ROOT\volmgr\0000 (volmgr)
    [0x2]            : ROOT\BasicDisplay\0000 (BasicDisplay)
    [0x3]            : ROOT\CompositeBus\0000 (CompositeBus)
    [0x4]            : ROOT\vdrvroot\0000 (vdrvroot)
    [0x5]            : ROOT\spaceport\0000 (spaceport)
    [0x6]            : ROOT\KDNIC\0000 (kdnic)
    [0x7]            : ROOT\UMBUS\0000 (umbus)
    [0x8]            : ROOT\ACPI_HAL\0000
...
```

**Grid Display**

As with other dx commands, you can right click on a command after it was executed and click "Display as grid" or add "-g" to the command to get a grid view of the results.

```dbgcmd
# 0: kd> dx -g @$cursession.Devices.DeviceTree.Flatten(n => n.Children)
=====================================================================================================================================================================================================================================================================================================================
# =                                                              = (+) DeviceNodeObject = InstancePath                                                 = ServiceName               = (+) PhysicalDeviceObject                                    = State                          = (+) Resoures = (+) Children       =
=====================================================================================================================================================================================================================================================================================================================
= [0x0] : HTREE\ROOT\0                                         - {...}                - HTREE\ROOT\0                                                 -                           - 0xffffb6075614be40 : Device for "\Driver\PnpManager"        - DeviceNodeStarted (776)        - {...}        - [object Object]    =
= [0x1] : ROOT\volmgr\0000 (volmgr)                            - {...}                - ROOT\volmgr\0000                                             - volmgr                    - 0xffffb607561fbe40 : Device for "\Driver\PnpManager"        - DeviceNodeStarted (776)        - {...}        - [object Object]    =
= [0x2] : ROOT\BasicDisplay\0000 (BasicDisplay)                - {...}                - ROOT\BasicDisplay\0000                                       - BasicDisplay              - 0xffffb607560739b0 : Device for "\Driver\PnpManager"        - DeviceNodeStarted (776)        - {...}        - [object Object]    =
= [0x3] : ROOT\CompositeBus\0000 (CompositeBus)                - {...}                - ROOT\CompositeBus\0000                                       - CompositeBus              - 0xffffb607561f9060 : Device for "\Driver\PnpManager"        - DeviceNodeStarted (776)        - {...}        - [object Object]    =
...
```

**View Devices by State**

Use *Where* to specify a specific device state.

```dbgcmd
dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.State <operator> <state number>)
```

For example to view devices in state DeviceNodeStarted use this command.

```dbgcmd
1: kd>  dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.State == 776)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.State == 776)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ROOT\volmgr\0000 (volmgr)
    [0x2]            : ROOT\BasicDisplay\0000 (BasicDisplay)
    [0x3]            : ROOT\CompositeBus\0000 (CompositeBus)
    [0x4]            : ROOT\vdrvroot\0000 (vdrvroot)
...
```

**View Not Started Devices**

Use this command to view devices not in state DeviceNodeStarted.

```dbgcmd
1: kd>  dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.State != 776)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.State != 776)                
    [0x0]            : ACPI\PNP0C01\1
    [0x1]            : ACPI\PNP0000\4&215d0f95&0
    [0x2]            : ACPI\PNP0200\4&215d0f95&0
    [0x3]            : ACPI\PNP0100\4&215d0f95&0
    [0x4]            : ACPI\PNP0800\4&215d0f95&0
    [0x5]            : ACPI\PNP0C04\4&215d0f95&0
    [0x6]            : ACPI\PNP0700\4&215d0f95&0 (fdc)
    [0x7]            : ACPI\PNP0C02\1
    [0x8]            : ACPI\PNP0C02\2
```

**View Devices by Problem Code**

Use the *DeviceNodeObject.Problem* object to view devices that have specific problem codes.

```dbgcmd
dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem <operator> <problemCode>)
```

For example, to view devices that have a non zero problem code use this command. This provides similar information to "[**!devnode**](-devnode.md) 0 21".

```dbgcmd
1: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem != 0)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem != 0)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ACPI\PNP0700\4&215d0f95&0 (fdc)
```

**View All Devices Without a Problem**

Use this command to view all devices without a problem

```dbgcmd
1: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem == 0)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem == 0)                
    [0x0]            : ROOT\volmgr\0000 (volmgr)
    [0x1]            : ROOT\BasicDisplay\0000 (BasicDisplay)
    [0x2]            : ROOT\CompositeBus\0000 (CompositeBus)
    [0x3]            : ROOT\vdrvroot\0000 (vdrvroot)
...
```

**View All Devices With a Specific Problem**

Use this command to view devices with a problem state of 0x16.

```dbgcmd
1: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem == 0x16)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem == 0x16)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ACPI\PNP0700\4&215d0f95&0 (fdc)
```

**View Devices by Function Driver**

Use this command to view devices by function driver.

```dbgcmd
dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.ServiceName <operator> <service name>)
```

To view devices using a certain function driver, such as atapi, use this command.

```dbgcmd
1: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.ServiceName == "atapi")
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.ServiceName == "atapi")                
    [0x0]            : PCIIDE\IDEChannel\4&10bf2f88&0&0 (atapi)
    [0x1]            : PCIIDE\IDEChannel\4&10bf2f88&0&1 (atapi)
```

**Viewing a List of Boot Start Drivers**

To view the list of what winload loaded as boot start drivers, you need to be in a context where you have access to the LoaderBlock and early enough the LoaderBlock is still around. For example, during nt!IopInitializeBootDrivers. A breakpoint can be set to stop in this context.

```dbgcmd
1: kd> g
Breakpoint 0 hit
nt!IopInitializeBootDrivers:
8225c634 8bff            mov     edi,edi
```

Use the ?? command to display the boot driver structure.

```dbgcmd
1: kd> ?? LoaderBlock->BootDriverListHead
struct _LIST_ENTRY
 [ 0x808c9960 - 0x808c8728 ]
   +0x000 Flink            : 0x808c9960 _LIST_ENTRY [ 0x808c93e8 - 0x808a2e18 ]
   +0x004 Blink            : 0x808c8728 _LIST_ENTRY [ 0x808a2e18 - 0x808c8de0 ]
```

Use the Debugger.Utility.Collections.FromListEntry debugger object to view of the data, using the starting address of the nt!\_LIST\_ENTRY structure.

```dbgcmd
1: kd> dx Debugger.Utility.Collections.FromListEntry(*(nt!_LIST_ENTRY *)0x808c9960, "nt!_BOOT_DRIVER_LIST_ENTRY", "Link")
Debugger.Utility.Collections.FromListEntry(*(nt!_LIST_ENTRY *)0x808c9960, "nt!_BOOT_DRIVER_LIST_ENTRY", "Link")                
    [0x0]            [Type: _BOOT_DRIVER_LIST_ENTRY]
    [0x1]            [Type: _BOOT_DRIVER_LIST_ENTRY]
    [0x2]            [Type: _BOOT_DRIVER_LIST_ENTRY]
    [0x3]            [Type: _BOOT_DRIVER_LIST_ENTRY]
    [0x4]            [Type: _BOOT_DRIVER_LIST_ENTRY]
    [0x5]            [Type: _BOOT_DRIVER_LIST_ENTRY]
...
```

Use the -g option to create a grid view of the data.

```dbgcmd
dx -r1 -g Debugger.Utility.Collections.FromListEntry(*(nt!_LIST_ENTRY *)0x808c9960, "nt!_BOOT_DRIVER_LIST_ENTRY", "Link")
```

**View devices by Capability**

View devices by capability using the DeviceNodeObject.CapabilityFlags object.

```dbgcmd
dx -r1 @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => (n.DeviceNodeObject.CapabilityFlags & <flag>) != 0)
```

This table summarizes the use of the dx command with common device capability flags.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Removable</td>
<td align="left"><div class="code">

<code>dbgcmd
0: kd&gt; dx -r1 @$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x10) != 0)
@$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x10) != 0)                
    [0x0]            : SWD\PRINTENUM\{2F8DBBB6-F246-4D84-BB1D-AA8761353885}
    [0x1]            : SWD\PRINTENUM\{F210BC77-55A1-4FCA-AA80-013E2B408378}
    [0x2]            : SWD\PRINTENUM\{07940A8E-11F4-46C3-B714-7FF9B87738F8}
    [0x3]            : DISPLAY\Default_Monitor\6&amp;1a097cd8&amp;0&amp;UID5527112 (monitor)</code>

</div></td>
</tr>
<tr class="even">
<td align="left">UniqueID</td>
<td align="left"><div class="code">

<code>dbgcmd
0: kd&gt; dx -r1 @$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x40) != 0)
@$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x40) != 0)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ROOT\volmgr\0000 (volmgr)
    [0x2]            : ROOT\spaceport\0000 (spaceport)
...</code>

</div></td>
</tr>
<tr class="odd">
<td align="left">SilentInstall</td>
<td align="left"><div class="code">

<code>dbgcmd
0: kd&gt; dx -r1 @$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x80) != 0)
@$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x80) != 0)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ROOT\volmgr\0000 (volmgr)
    [0x2]            : ROOT\spaceport\0000 (spaceport)
...</code>

</div></td>
</tr>
<tr class="even">
<td align="left">RawDeviceOk</td>
<td align="left"><div class="code">

<code>dbgcmd
0: kd&gt; dx -r1 @$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x100) != 0)
@$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x100) != 0)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : SWD\MMDEVAPI\MicrosoftGSWavetableSynth
    [0x2]            : SWD\IP_TUNNEL_VBUS\IP_TUNNEL_DEVICE_ROOT
...</code>

</div></td>
</tr>
<tr class="odd">
<td align="left">SurpriseRemovalOK</td>
<td align="left"><div class="code">

<code>dbgcmd
0: kd&gt; dx -r1 @$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x200) != 0)
@$cursession.Devices.DeviceTree.Flatten(n =&gt; n.Children).Where(n =&gt; (n.DeviceNodeObject.CapabilityFlags &amp; 0x200) != 0)                
    [0x0]            : SWD\MMDEVAPI\MicrosoftGSWavetableSynth
    [0x1]            : SWD\IP_TUNNEL_VBUS\IP_TUNNEL_DEVICE_ROOT
    [0x2]            : SWD\PRINTENUM\PrintQueues
...</code>

</div></td>
</tr>
</tbody>
</table>


For more information about the CapabilityFlags, see [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095).


## <span id="see_also"></span>See also

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

[Native Debugger Objects in NatVis](native-debugger-objects-in-natvis.md)

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md) 

---







