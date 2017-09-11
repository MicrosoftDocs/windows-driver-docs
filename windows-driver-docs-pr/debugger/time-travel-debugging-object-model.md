---
title: Time Travel Debugging - Object Model
description: This section describes how to use the data model to query time travel traces. 
ms.author: windowsdriverdev
ms.date: 09/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Object Model

TBD TBD TBD 

This section describes how to use the data model to query time travel traces. This can be a powerful tool to 

For more information about objects see these topics:

[Debugger Object model reference - Time Travel Debugging](debugger-object-model-reference-time-travel-debugging.md)

T1

T2

## Querying a Time Travel Trace – dx namespaces and commands


The Lifetime, Threads and Events TTD objects are associated with the current process (curprocess). Use the dx command to view these TTD Objects.

```
0:000> dx @$curprocess.TTD 
@$curprocess.TTD  
    Lifetime         : [97:0, 113:0]
    Threads         
    Events          
```


Use dx to query for what you are looking for. 

Examples:
- Querying for exceptions:

```
dx @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception) 

```

- Querying for the load event(s) of a particular module
```

```
dx @$curprocess.TTD.Events.Where(t => t.Type == "ModuleLoaded").Where(t => t.Module.Name.Contains("ntdll.dll")) 
```
- Querying for the threads that get created

```
dx -g @$curprocess.TTD.Events.Where(t => t.Type == "ThreadCreated").Select(t => t.Thread) 

```

##	Overview of namespaces and querying call-outs

TBD

For addtional information, see [Debugger Object model reference - Time Travel Debugging](debugger-object-model-reference-time-travel-debugging.md).


> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




