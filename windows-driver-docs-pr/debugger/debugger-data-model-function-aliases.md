---
title: Debugger Data Model Function Aliases
description: Function aliases are a quick unique short name by which a user of the debugger can access functionality defined in a debugger extension.
keywords: ["Debugger Data Model Function Aliases"]
ms.author: domars
ms.date: 01/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugger Data Model Function Aliases

Function aliases are a quick unique short name by which a user of the debugger can access functionality defined in a debugger extension (whether written in C++ or some scripting environment such as JavaScript). This name gets associated with a data model function object (an object which implements IModelMethod). That function takes an arbitrary number of arguments and returns a single value. The effect of invoking a function alias and what is done with that value depend on how the function alias is invoked and what host debugger it is invoked within. 

This topic assumes the reader is familar with the debugger oject model and and JavaScript. For information about using debugger objects with JavaScript, see [Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

Some of the examples shown here use the dx command, for more information about working with the dx command, see [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).


## Using function alias as extension commands

All function aliases created in WinDbg Preview can be invoked as if they were debug extension **!** "bang" commands. If the function takes no arguments, simply invoking !aliasName will cause the function to be called and the result value to be displayed. As an example (created with JavaScript extensibility)

As an example this function provides two constant values, *pi* and *e*.

```
function __constants()
{
    return { math_constants : { pi :  3.1415926535 , e :  2.7182818284}, description : "Archimedes' pi and Euler's number e" };
}

function initializeScript()
{
    return [new host.functionAlias(__constants, "constants")];
}

```

The results of calling the function alias are shown here. 

```
0:000> !constants
@$constants()                 : [object Object]
    math_constants   : [object Object]
    description      : Archimedes' pi and Euler's number e
```

DML links to complex objects will be generated automatically. Clicking the math_constants shown above will result in the following. 


```
0:000> dx -r1 @$constants().math_constants
@$constants().math_constants                 : [object Object]
    pi               : 3.141593
    e                : 2.718282

```


If the function has arguments, they can be supplied after the function alias command itself. Note that whatever comes after the function alias command is considered an expression and is evaluated as such. The text string is not passed directly to the function. For a single argument expression, it can come after the function alias command itself. For multiple arguments, they should be parenthesized as if it were a function call as illustrated in this next example.


```
function __oneArgument(x)
{
    return -x;
}

function __twoArguments(x, y)
{
    return x + y;
}

function initializeScript()
{
    return [new host.functionAlias(__oneArgument, "neg"),
            new host.functionAlias(__twoArguments, "add")];
}
```


```

```





## Examples

Debugger objects are projected into a namespace rooted at "Debugger". Processes, modules, threads, stacks, stack frames, and local variables are all available to be used in a LINQ query.

LINQ commands such as the following can be used .All, .Any, .Count, .First, .Flatten, .GroupBy, .Last, .OrderBy, .OrderByDescending, .Select, and .Where. These methods follow (as closely as possible) the C# LINQ method form.

This example shows the top 5 processes running the most threads:

```
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

```
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

```
dx -r2 Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.
```

Press the TAB key until ".Name" appears. Add a closing parenthesis ")" and press enter to execute the command.

```
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

```
dx -r2 Debugger.Sessions.First().Processes.Select(p => new {Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.Name, (a, b) => a.
```

You can display the defined user variables using *Debugger.State.UserVariables* or *@$vars*.

```
kd> dx Debugger.State.UserVariables
Debugger.State.UserVariables : 
    mySessionVar     : 
    String1          : Test String
```

You can remove a variable using .Remove.

```
kd> dx @$vars.Remove("String1")
```


## <span id="Debugging_Plug_and_Play"></span><span id="debugging_plug_and_play"></span><span id="DEBUGGING_PLUG_AND_PLAY"></span>Debugging Plug and Play Example


This section illustrates how the built in debugger objects used with LINQ queries, can be used to debug plug and play objects.

**View all devices**

Use *Flatten* on the device tree to view all devices. 

```
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

```
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

```
dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.State <operator> <state number>)
```

For example to view devices in state DeviceNodeStarted use this command.

```
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

```
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

```
dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem <operator> <problemCode>)
```

For example, to view devices that have a non zero problem code use this command. This provides similar information to "[**!devnode**](-devnode.md) 0 21".

```
1: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem != 0)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.DeviceNodeObject.Problem != 0)                
    [0x0]            : HTREE\ROOT\0
    [0x1]            : ACPI\PNP0700\4&215d0f95&0 (fdc)
```


## <span id="see_also"></span>See also

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

[Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md)

[Native Debugger Objects in NatVis](native-debugger-objects-in-natvis.md)

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md) 

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20dx%20%28Display%20Debugger%20Object%20Model%20Expression%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





