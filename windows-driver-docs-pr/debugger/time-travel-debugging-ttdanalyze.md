---
title: Time Travel Debugging - TTDAnalyze
description: This section describes how to use the TTDAnalyze to analyze time travel traces.
ms.author: windowsdriverdev
ms.date: 09/14/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - TTDAnalyze 

This section describes how to  section describes how to use the TTDAnalyze to analyze time travel traces.

TBD TBD TBD 

You interact with TTDAnalyze through the data model, under the current session:

```
0:000> dx @$cursession.TTD
@$cursession.TTD : [object Object]
    Data             : Use 'dx -v' to see the data sources contained in TTD.Data
    Utility          : Use 'dx -v' to see the utility methods contained in TTD.Utility

```

The Data namespace contains “normalized data” from the trace. There is one data source offered, heap allocations, which can be accessed using .Heap().


```
0:000> dx -r2 @$cursession.TTD.Data.Heap()
@$cursession.TTD.Data.Heap()
    [0x0]            : [object Object]
        Action           : Alloc
        Heap             : 0x172eabe0000
        Address          : 0x172eabf3e30
        Size             : 0x168
        Flags            : 0x100008
        TimeStart        : 29:38
        TimeEnd          : 2B:9C
    [0x1]            : [object Object]
        Action           : Alloc
        Heap             : 0x172eabe0000
        Address          : 0x172eabed6f0
        Size             : 0xd0
        Flags            : 0xc0000
        TimeStart        : 17B0:19
        TimeEnd          : 17BA:3C
…
    [0x19]           : [object Object]
        Action           : Free
        Heap             : 0x172eabe0000
        Address          : 0x172eabec380
        Flags            : 0x0
        Result           : 0x1
        TimeStart        : 47:269
        TimeEnd          : 49:1D
…
```

Note that clicking on TimeStart or TimeEnd will navigate you to that point in the trace.  

It is called “normalized data” because theere is a chosen set of APIs that represent heap operations, extracted the data from the appropriate parameters that is presented in a uniform manner.

There is support searching for arbitrary function calls using the .Calls() method as shown below.

```
0:000> dx -r2 @$cursession.TTD.Calls("user32!SendMessageW")
@$cursession.TTD.Calls("user32!SendMessageW")
    [0x0]
        Function         : USER32!SendMessageW
        FunctionAddress  : 0x7ff98afc08b0
        ReturnValue      : 2
        Parameter1       : 0x307b0
        Parameter2       : 0x429
        Parameter3       : 0x2
        Parameter4       : 0
        TimeStart        : 14AE3:9A
        TimeEnd          : 14B4F:95

```

Note: Parameter1..4 are being replaced with a Parameters[] array, indexed by 0 .. n-1 where n is number of parameters


All of the LINQ features of dx can be used to filter the query, for example searching for just message 0x429.

```
0:000> dx -r2 @$cursession.TTD.Calls("user32!SendMessageW").Where(c => c.Parameter2 == 0x429)
@$cursession.TTD.Calls("user32!SendMessageW").Where(c => c.Parameter2 == 0x429)
    [0x0]
        Function         : USER32!SendMessageW
        FunctionAddress  : 0x7ff98afc08b0
        ReturnValue      : 2
        Parameter1       : 0x307b0
        Parameter2       : 0x429
        Parameter3       : 0x2
        Parameter4       : 0
        TimeStart        : 14AE3:9A
        TimeEnd          : 14B4F:95
    [0x1]
        Function         : USER32!SendMessageW
        FunctionAddress  : 0x7ff98afc08b0
        ReturnValue      : 0
        Parameter1       : 0x307b0
        Parameter2       : 0x429
        Parameter3       : 0x2
        Parameter4       : 2
        TimeStart        : 149D0:57
        TimeEnd          : 14AE3:95

```

You can pass multiple functions to .Calls(“function1”, “function2”, “function3” …) and those functions can contain wildcards.  

You can also use these queries from JavaScript.

```
var localApis = host.currentSession
    .TTD.Calls("kernelbase!LocalReAlloc", "kernelbase!LocalFree")
    .Where(function(call) { return call.Parameter1 == handle; });

var locations = [];
for (var api of localApis)
{
    locations.push(api.TimeStart);
}
```

> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




