---
title: Debugger object model reference - time travel debugging (TTD)
description: This section describes the debugger model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/21/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Debugger object model reference - time travel debugging (TTD)

This section describes the debugger model objects associated with time travel debugging - TTD. 

For general information about the debugger object model, see [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) and  [Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md). 

For information on working with the TTD objects see, [Time Travel Debugging - Object Model](time-travel-debugging-object-model.md).

## TTD Object

The TTD object contains time travel debugging properties available for each process in a trace file. The TTD object is associated with the curprocess debugger object. The following TTD objects are discussed in this topic. 

- *Lifetime*
- *Threads*
- *Events* 


### TTD Methods

**SetPosition()** - Sets the debugger to point to the given position on this process.    

### TTD dx command Example

Use the dx command with the help option (-h)  to view the TTD Objects with their descriptions.

```
0:000>  dx -h @$curprocess.TTD
@$curprocess.TTD                 [TTD-specific properties available for each process (for each trace file).]
    Lifetime         : [D:0, 8A:0] [The position range [smallest, largest] found in the trace file.]
    Threads          [This process' list of threads alive throughout the timeline.]
    Events           [This process' list of events.]         
```

Add the -v verbose option to view the methods associated with the TTD Objects, in this case the SetPostion method.

```
0:000> dx -h -v @$curprocess.TTD 
@$curprocess.TTD                  [TTD-specific properties available for each process (for each trace file).]
    Lifetime         : [D:0, 8A:0] [The position range [smallest, largest] found in the trace file.]
    Threads          [This process' list of threads alive throughout the timeline.]
    Events           [This process' list of events.]
    SetPosition      [Sets the debugger to point to the given position on this process.]      
```

## TTD Lifetime Object 

The TTD Lifetime Object contains the position range [smallest, largest] found in the time travel trace file. 

**MinPostion** - The minimum valid position for a position range. MinPosition Contains:

  *Sequence* - References the last position where this thread might have explicitly interacted with other threads.

  *Steps* - The steps (instructions) beyond the last thread sequencing event.
 
**MaxPosition** - The maximum valid position for a position range. MaxPosition Contains:

  *Sequence* - References the last position where this thread might have explicitly interacted with other threads.
  
  *Steps* - The steps (instructions) beyond the last thread sequencing event.
  
### TTD Lifetime Methods

**ToDisplayString([FormatSpecifier]** - Method which converts the object to its display string representation according to an optional format specifier. All of the TTD Lifetime object children support this method.

### TTD Object dx Command Example

Use the dx command to display information about all of the children objects of the TTD Lifetime object.

```
0:000> x -r2 -h -v @$curprocess.TTD.Lifetime
@$curprocess.TTD.Lifetime                 : [D:0, 8A:0] [The position range [smallest, largest] found in the trace file.]
    MinPosition      : D:0 [Time Travel] [The minimum valid position for a position range.]
        Sequence         : 0xd [References the last position where this thread might have explicitly interacted with other threads.]
        Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]
        SeekTo           [Method which seeks to time position]
        ToDisplayString  [ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier]
    MaxPosition      : 8A:0 [Time Travel] [The maximum valid position for a position range.]
        Sequence         : 0x8a [References the last position where this thread might have explicitly interacted with other threads.]
        Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]
        SeekTo           [Method which seeks to time position]
        ToDisplayString  [ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier]
    ToDisplayString  [ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier]
```

## TTD Threads Objects 

The TTD Threads Object contains an array of the threads in the TTD trace. Each thread in the array contains the following objects.

**UniqueId** - The uniqueId is the thread's unique ID within the process (TIDs can be reused over the life of the process).
 
**Id** - The thread's TID assigned by the OS.

**LifeTime** - The TTD Lifetime object contains information on the contents of the time travel trace, see above for information on the LifeTime object. In the Lifetime object, the MinPosition to MaxPosition range, is the portion of the timeline that contains instructions executed by the thread.
 
**ActiveTime** - The position range where execution of this thread is recorded. The active lifetime of a thread is the closest approximation to when the thread was present during recording of the trace.


## TTD Threads Methods 
 
 **SeekTo** - Method which seeks to time position. The MinPosition and MaxPosition TTD Threads objects, support this method.
 
 **ToDisplayString** - ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier. All of the TTD Threads object children support this method.
        
 
### TTD Threads Object Example

Use the dx command to display all of the children objects of the first TTD threads object in the array.

```
0:000> dx -r3 -h @$curprocess.TTD.Threads[0]
@$curprocess.TTD.Threads[0]                 : UID: 2, TID: 0x4C2C
    UniqueId         : 0x2 [The thread's unique ID within the process (TIDs can be reused over the life of the process).]
    Id               : 0x4c2c [The thread's TID assigned by the OS.]
    Lifetime         : [0:0, FFFFFFFFFFFFFFFE:0] [The position range where the thread appears in the timeline.]
        MinPosition      : Min Position [Time Travel] [The minimum valid position for a position range.]
            Sequence         : 0x0 [References the last position where this thread might have explicitly interacted with other threads.]
            Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]
        MaxPosition      : FFFFFFFFFFFFFFFE:0 [Time Travel] [The maximum valid position for a position range.]
            Sequence         : 0xfffffffffffffffe [References the last position where this thread might have explicitly interacted with other threads.]
            Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]
    ActiveTime       : [D:0, 64:0] [The position range where execution of this thread is recorded.]
        MinPosition      : D:0 [Time Travel] [The minimum valid position for a position range.]
            Sequence         : 0xd [References the last position where this thread might have explicitly interacted with other threads.]
            Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]
        MaxPosition      : 64:0 [Time Travel] [The maximum valid position for a position range.]
            Sequence         : 0x64 [References the last position where this thread might have explicitly interacted with other threads.]
            Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]
```

The [Time Travel] links provide a link to SeekTo() a specific event. 


```
0:0:000> dx -r1 @$curprocess.TTD .@"Threads"[2].@"ActiveTime"
@$curprocess.TTD .@"Threads"[2].@"ActiveTime"                 : [6A:0, 89:0]
   MinPosition      : 6A:0 [Time Travel]
   MaxPosition      : 89:0 [Time Travel]
0:0:000> dx @$curprocess.TTD .@"Threads"[2].@"ActiveTime".@"MinPosition".SeekTo()
@$curprocess.TTD .@"Threads"[2].@"ActiveTime".@"MinPosition".SeekTo()

```

## TTD Events Object 

The TTD Events Object contains an array of events in the TTD trace.

**Events** - This process list of events in the trace.
 
### TTD Events Type Object

**Type** - The type of event. For example, *ModuleLoaded* indicates that code module loaded. Contains:
*Length* - Property which returns the length of the string, for example 0xc.

### TTD Events Type Methods

**Contains(OtherString)** - Method which returns whether the string contains a given sub string.

**EndsWith(OtherString)** - Method which returns whether the string ends with a given string.

**IndexOf(OtherString)** - Method which returns the index of the first occurrence of a substring in the given string.  If no such occurrence exists, -1 is returned.

**LastIndexOf(OtherString)** -Method which returns the index of the last occurrence of a substring in the given string.  If no such occurrence exists, -1 is returned.

**Length** - Property which returns the length of the string.

**PadLeft(TotalWidth)** - Method which right aligns the string to the specified width by inserting spaces at the left of the string.

**PadRight(TotalWidth)** - Method which left aligns the string to the specified width by inserting spaces at the right of the string.

**Remove(StartPos, [Length])** - Method which removes all characters beginning at the specified position from the string.  If an optional length is supplied, only that many characters after the starting position are removed.

**Replace(SearchString, ReplaceString)** - Method which replaces every occurrence of a specified search string with a replacement string.

**StartsWith(OtherString)** - Method which returns whether the string starts with a given string.

**Substring(StartPos, [Length])** - Method which retrieves a substring from the given string.  The substring starts at a specified character position and continues to the end of the string or for the optionally specified length.

**ToLower()** - Returns a copy of this string converted to lowercase.

**ToUpper()** - Returns a copy of this string converted to uppercase.

**ToDisplayString** - ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier. All of the TTD Events object children support this method.
 
### TTD Events Position Objects

**Position** - The position where the event happened. The position is an offset to the current event from the start of the TTD trace. Position contains:

  *Sequence* - References the last position where this thread might have explicitly interacted with other threads.

  *Steps* - Counts the steps (instructions) beyond the last thread sequencing event.

   Position         : 2:0 [Time Travel] [The position where the event happened.]
        Sequence         : 0x2 [References the last position where this thread might have explicitly interacted with other threads.]
        Steps            : 0x0 [Counts the steps (instructions) beyond the last thread sequencing event.]

### TTD Events Position Methods
 
 **SeekTo** - Method which seeks to time position. The MinPosition and MaxPosition TTD Threads objects support this method.
 
 **ToDisplayString** - ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier. All of the TTD Lifetime object children support this method.
        

### TTD Events Module Objects

**Module** -  The module references a specific code element, for example:
 
 ```
 Module C:\Data1\Redstone\Debugger\TTD\CDog_Console\Debug\CDog_Console.exe 
 ```

The Module object contains:

  *Name* - The module name, for example C:\Data1\Redstone\Debugger\TTD\CDog_Console\Debug\CDog_Console.exe. *Name* contains: *Length* - Property which returns the length of the string, for example 0x59.

  *Address* - The address where the module was loaded, for example 0xbf0000

  *Size* -   The size of the module in bytes, for example, 0x1f000

  *Checksum* -   The computed checksum of the module, for example, 0x9c4e

  *Timestamp* -   The timestamp of the module, for example,  0x59b1e18f. The timestamp is relative to the ???TBD of the ???TBD or is when the module is loaded ??? TBD. 


### TTD Events Module Methods

 **ToDisplayString** - ToDisplayString([FormatSpecifier]) - Method which converts the object to its display string representation according to an optional format specifier. All of the TTD Lifetime object children support this method.


### TTD Events Module Name Methods

**Contains(OtherString)** -Method which returns whether the string contains a given sub string.

**EndsWith(OtherString)** -Method which returns whether the string ends with a given string.

**IndexOf(OtherString)** -Method which returns the index of the first occurrence of a substring in the given string.  If no such occurrence exists, -1 is returned.

**LastIndexOf(OtherString)** -Method which returns the index of the last occurrence of a substring in the given string.  If no such occurrence exists, -1 is returned.

**Length** - Property which returns the length of the string.

**PadLeft(TotalWidth)** - Method which right aligns the string to the specified width by inserting spaces at the left of the string.

**PadRight(TotalWidth)** - Method which left aligns the string to the specified width by inserting spaces at the right of the string.

**Remove(StartPos, [Length])** - Method which removes all characters beginning at the specified position from the string.  If an optional length is supplied, only that many characters after the starting position are removed.

**Replace(SearchString, ReplaceString)** - Method which replaces every occurrence of a specified search string with a replacement string.

**StartsWith(OtherString)** - Method which returns whether the string starts with a given string.

**Substring(StartPos, [Length])** - Method which retrieves a substring from the given string.  The substring starts at a specified character position and continues to the end of the string or for the optionally specified length.

**ToLower()** - Returns a copy of this string converted to lowercase.

**ToUpper()** - Returns a copy of this string converted to uppercase.


### TTD Events Object Examples

Use the dx command to display all of the children objects for the TTD Events object.

```
0:000> dx -r2 @$curprocess.TTD .@"Events"[0]
@$curprocess.TTD .@"Events"[0]                 : Module Loaded at position: 8C:0
    Type             : ModuleLoaded
        Length           : 0xc
    Position         : 8C:0 [Time Travel]
        Sequence         : 0x8c
        Steps            : 0x0
    Module           : Module C:\Data1\Redstone\Debugger\TTD\CDog_Console\Debug\CDog_Console.exe at address 0XBF0000 with size 126976
        Name             : C:\Data1\Redstone\Debugger\TTD\CDog_Console\Debug\CDog_Console.exe
        Address          : 0xbf0000
        Size             : 0x1f000
        Checksum         : 0x0
        Timestamp        : 0x59b1e18f
```

## See Also

[Time Travel Debugging - Trace File object model](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




