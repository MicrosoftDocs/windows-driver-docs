---
title: Debugger Object model reference - Time Travel Debugging
description: This section describes the debugger model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Debugger Object model reference - Time Travel Debugging

This section describes the debugger model objects associated with time travel debugging.

The Lifetime, Threads and Events TTD objects are associated with the current process (curprocess). Use the dx command to view these TTD Objects.

```
0:000> dx @$curprocess.TTD 
@$curprocess.TTD  
    Lifetime         : [97:0, 113:0]
    Threads         
    Events          
```

## TTD Lifetime Object 

The TTD Lifetime Object contains information on the contents of the time travel trace.

**MinPostion** 

MinPosition Contains:
  *Sequence* - The sequence position in the TTD trace. TBD
  *Steps* - The number of steps in the TTD trace. TBD
 
**MaxPosition**
MaxPosition Contains:
  *Sequence* - The sequence position in the TTD trace. TBD
  *Steps* - The number of steps in the TTD trace. TBD
  

Use the dx command to display all of the childern objects to the TTD Lifetime object.

```
0:000> dx -r2 @$curprocess.TTD .@"Lifetime"
@$curprocess.TTD .@"Lifetime"                 : [97:0, 113:0]
    MinPosition      : 97:0 [Time Travel]
        Sequence         : 0x97
        Steps            : 0x0
    MaxPosition      : 113:0 [Time Travel]
        Sequence         : 0x113
        Steps            : 0x0
```



## TTD Threads Object 

The TTD Threads Object contains and array of the threads in the TTD trace. Each thread in the array contains the following objects.

**UniqueId** 
The uniqueId is an assigned Unique ID TBD TBD.

**Id**

**LifeTime**

The TTD Lifetime Object contains information on the contents of the time travel trace.


**MinPostion** 

MinPosition Contains:
  *Sequence* - The sequence position in the TTD trace. TBD
  *Steps* -    The number of steps in the TTD trace. TBD
 
**MaxPosition**
MaxPosition Contains:
  *Sequence* - The sequence position in the TTD trace. TBD
  *Steps* -    The number of steps in the TTD trace. TBD
 
**ActiveTime**

The TTD Lifetime Object contains information on the contents of the time travel trace.

The active lifetime of a thread is the closest approximation to when the thread was present during record.
[FirstPosition..LastPosition] is the portion of the timeline that contains instructions executed by the thread.

### TTD Threads Object Examples

Use the dx command to display all of the children objects to the first TTD threads object.

```
0:000> dx -r3 @$curprocess.TTD .@"Threads"[0]
@$curprocess.TTD .@"Threads"[0]                 : UID: 2, TID: 0x4164
    UniqueId         : 0x2
    Id               : 0x4164
    Lifetime         : [0:0, FFFFFFFFFFFFFFFE:0]
        MinPosition      : Min Position [Time Travel]
            Sequence         : 0x0
            Steps            : 0x0
        MaxPosition      : FFFFFFFFFFFFFFFE:0 [Time Travel]
            Sequence         : 0xfffffffffffffffe
            Steps            : 0x0
    ActiveTime       : [97:0, ED:0]
        MinPosition      : 97:0 [Time Travel]
            Sequence         : 0x97
            Steps            : 0x0
        MaxPosition      : ED:0 [Time Travel]
            Sequence         : 0xed
            Steps            : 0x0
```

The [Time Travel] links provide a link to a 

```
dx @$curprocess.TTD .@"Threads"[2].@"ActiveTime".@"MinPosition".SeekTo()
```

## TTD Events Object 

The TTD Events Object contains an array of events in the TTD trace.
Events are the TBD... in the TTD trace

**Type** - The type of module that is loaded, for example *ModuleLoaded* indicates TBD.
Contains:
 *Length* - Length of the TBD in TBD, for example 0xc
 
**Position**
The position is an offset to the current event from the TBD of the TTD trace, for example 8C:0 [Time Travel] indicates TBD.

Contains:
  *Sequence* - The sequence is TBD, for example  0x8c
  *Steps* - Steps, for example 0x0 indicates, that TBD.
 
**Module**

 The module references a specific code element, for example
 ```
 Module C:\Data1\Redstone\Debugger\TTD\CDog_Console\Debug\CDog_Console.exe at address 0XBF0000 with size 126976
 ```
Contains:
  *Name* - The module name, for example C:\Data1\Redstone\Debugger\TTD\CDog_Console\Debug\CDog_Console.exe
  *Address* - The address of the module -  for example 0xbf0000
  *Size* -   The size of the module - for example, 0x1f000
  *Checksum* -   The computed checksum of the module - for example, 0x0 TBD - Need to confirm value
  *Timestamp* -   The timestamp of the module - for example,  0x59b1e18f. The timestamp is relative to the TBD of the TBD. 
        

### TTD Events Object Examples

Use the dx command to display all of the childern objects to the TTD Events object.

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


> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




