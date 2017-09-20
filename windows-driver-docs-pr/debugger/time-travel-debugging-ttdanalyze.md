---
title: Time Travel Debugging - Data and Utility objects
description: This section describes how to use the Data and utility objects to look at heap data in time travel traces.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Data and Utility objects

This section describes how to use the Data and utility objects to look at heap data in time travel traces.


The Data and Utility objects are childern of the TTD object. Use the dx command as shown to display information about the TTD childern object.

```
0:000> dx @$cursession.TTD
@$cursession.TTD : [object Object]
    Data             : Use 'dx -v' to see the data sources contained in TTD.Data
    Utility          : Use 'dx -v' to see the utility methods contained in TTD.Utility

```

Use the dx command -v and -d options to display addtional information about the objects. For more information about the dx command, see [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).

??? TBD - Ken I can paste in the updated help strings now if you can email the rc (?) file...


## TTD Data

The TTD Data object contains these two childern objects.   

   **capturedSession** - Captured session data. Supports the internal implementation of the data object.    
   **Heap** - Normalized head data    

### Remarks

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

Use the -g option to display the results in a grid

??? TBD Need to have a better example with better TimeEnd 

```
0:000> dx -r2 -g @$cursession.TTD.Data.Heap()
==========================================================================================================================================
=                          = Action   = Heap   = Address         = Size          = Flags  = (+) TimeStart = (+) TimeEnd         = Result =
==========================================================================================================================================
= [0x0] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - B2:3BF        - Invalid Position    -        =
= [0x1] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - 1C:78         - Invalid Position    -        =
= [0x2] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - B7:77         - Invalid Position    -        =
= [0x3] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - CC:77         - Invalid Position    -        =
= [0x4] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - D2:214        - Invalid Position    -        =
= [0x5] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - D3:1FE        - Invalid Position    -        =
= [0x6] : [object Object]  - Alloc    - 0x0    - 0x0             - 0x77722dc0    - 0x0    - DF:1CF        - Invalid Position    -        =
```


Note that clicking on TimeStart or TimeEnd will navigate you to that point in the trace.  

It is called “normalized data” because there is a chosen set of APIs that represent heap operations, extracted the data from the appropriate parameters that is presented in a uniform manner.


## TTD Utility

**capturedSession** - Captured session data. Supports the internal implementation of the data object.    

**GetHeapAddress** -  Filters HeapAPICalls() to just the entries that impact the specified address. The address can point anywhere inside a memory block, it is not required to point to  the start of a block.  
```dx @$cursession.TTDUtils.GetHeapAddress(address) ```

### GetHeapAddress example use 

Use this dx command with the GetHeapAddress method to locate heap entries that impact the specified address.

??? TBD - need better example then 0x0
??? TBD - is 0x0 non heap - stack memory?

```
0:000> dx -r4 -g @$cursession.TTD.Utility.GetHeapAddress(0x0)
=========================================================================================================================
=                          = Action   = Heap   = Address = Size          = Flags  = (+) TimeStart = (+) TimeEnd         =
=========================================================================================================================
= [0x0] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - B2:3BF        - Invalid Position    =
= [0x1] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - 1C:78         - Invalid Position    =
= [0x2] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - B7:77         - Invalid Position    =
= [0x3] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - CC:77         - Invalid Position    =
= [0x4] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - D2:214        - Invalid Position    =
= [0x5] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - D3:1FE        - Invalid Position    =
= [0x6] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - DF:1CF        - Invalid Position    =
= [0x7] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - E0:1FE        - Invalid Position    =
= [0x8] : [object Object]  - Alloc    - 0x0    - 0x0     - 0x77722dc0    - 0x0    - 22:B2         - Invalid Position    =
```



## TTD Methods

**Calls** - Returns call information from the trace for the specified set of methods:  

```
 dx @$cursession.TTD.Calls("module!method1", "module!method2", ...)
```


Calls returns an indexable list of heap API operations that change the address space in some way. For example alloc, realloc, free and a few others. It does not return heap API operations that are just queries (e.g. getting size of allocated block.) The data that is presented is specific to Heap APIs and hides Windows implementation details.


### Example use: Viewing Calls

Use the Calls method to see the areas of the trace that contain a specificed set of method calls. 

```
0:000> dx -r2 @$cursession.TTD.Calls("user32!SendMessageW")
@$cursession.TTD.Calls("user32!SendMessageW")
    [0x0]
        Function         : USER32!SendMessageW
        FunctionAddress  : 0x7ff98afc08b0
        ReturnValue      : 2
        Parameter[1]       : 0x307b0
        Parameter[2]       : 0x429
        Parameter[3]       : 0x2
        Parameter[4]       : 0
        TimeStart          : 14AE3:9A
        TimeEnd            : 14B4F:95

```

??? TBD - need updated output to show param[] array - zero based or one based?
??? TBD Parameter1..4 are being replaced with a Parameters[] array, indexed by 0 .. n-1 where n is number of parameters

Clicking on [Time Travel] will take you to that position in the trace.

If you click on a TimeRange you will see the extent of the call:

```
 0:000> dx @$cursession.TTDUtils.HeapAPICalls()[5]
 @$cursession.TTDUtils.HeapAPICalls()[5]                
    Action           : Alloc
    Heap             : 0x1a3f7430000
    Address          : 0x1a3f744bc40
    Size             : 0x10
    Flags            : 0x0
    TimeRange        : [50:167, 52:36]
 0:000> dx -r1 @$cursession.TTDUtils.HeapAPICalls()[5].@"TimeRange"
 @$cursession.TTDUtils.HeapAPICalls()[5].@"TimeRange"                 : [50:167, 52:36]
     MinPosition      : 50:167 [Time Travel]
     MaxPosition      : 52:36 [Time Travel]
```


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



### Example scenario use - Debugging exception

 Start by ensuring trace is indexed:

```
 0:000> !index
 Indexed 1/1 keyframes
 Successfully created the index in 29ms.
```

Use !events to navigate to the spot where the critical error is raised (which gives example queries to use in place of !events):

```
 0:000> dx @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)
 @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)                
     [0x0]            : Exception of type Software at PC: 0X7FF83B92BF60
 0:000> dx -r1 @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)[0]
 @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)[0]                 : Exception of type Software at PC: 0X7FF83B92BF60
     Position         : 74:0
     Type             : Software
     ProgramCounter   : 0x7ff83b92bf60
     Code             : 0xc0000374
     Flags            : 0x1
     RecordAddress    : 0x0
```

 0xc0000374 is the exception code for a heap error. Travel to that position and dump the start of the stack with parameters. The 4th parameter is the
 heap address that has a problem:

```
 0:000> !tt  74:0
 Setting position: 74:0
 (2420.4100): Break instruction exception - code 80000003 (first/second chance not available)
 Time Travel Position: 74:0
 ntdll!RtlRaiseException:
 00007ff8`3b92bf60 4055            push    rbp
 0:000> kP
  # Child-SP          RetAddr           Call Site
 00 000000b8`c811f6f8 00007ff8`3b9e166b ntdll!RtlRaiseException(
 			struct _EXCEPTION_RECORD * ExceptionRecord = 0x000000b8`c811f750) [minkernel\ntos\rtl\amd64\raise.c @ 52] 
 01 000000b8`c811f700 00007ff8`3b9e8b7e ntdll!RtlReportCriticalFailure(
 			long StatusCode = 0n-1073740940, 
 			void * FailureInfo = 0x00007ff8`3ba46700, 
 			unsigned long BreakIfDbgPresent = 1)+0x97 [minkernel\ntos\rtl\rtlutil.c @ 202] 
 02 000000b8`c811f810 00007ff8`3b98ce0e ntdll!RtlpHeapHandleError(
 			long ErrorLevel = 0n-938346672)+0x12 [minkernel\ntos\rtl\heaplog.c @ 374] 
 03 000000b8`c811f840 00007ff8`3b99e2ab ntdll!RtlpLogHeapFailure(
 			_HEAP_FAILURE_TYPE FailureType = 0n-938346672 (No matching enumerant), 
 			void * HeapAddress = 0x00000235`79330000, 
 			void * Address = 0x00000235`7942f850, 
 			void * Param1 = 0x00000235`7942f860, 
 			void * Param2 = 0x00000000`00000000, 
 			void * Param3 = 0x00000000`00000000)+0x96 [minkernel\ntos\rtl\heaplog.c @ 714] 
```

Ask TTD to locate all of the operations that impacted the address:

 ```
 0:000> dx -g @$cursession.TTD.GetHeapAddress(0x00000235`7942f860)
 =====================================================================================================================
 =          = Action   = Heap             = Address          = Size    = Flags  = (+) TimeRange      = Result        =
 =====================================================================================================================
 = [0x0]    - Alloc    - 0x23579330000    - 0x2357942f860    - 0x32    - 0x0    - [59:12, 5B:36]     -               =
 = [0x1]    - Free     - 0x23579330000    - 0x2357942f860    -         - 0x0    - [63:13, 65:2B]     - 0x1           =
 = [0x2]    - Free     - 0x23579330000    - 0x2357942f860    -         - 0x0    - [6D:13, 6D:B13]    - 0x6917108b    =
 =====================================================================================================================
```

 From this it is can be observed that the last two entries show the same address is freed twice. So the problem is a double free. The time positions for both the first and second free can be navigated to in order to understand the root cause.



## JavaScript Support

You can also use these queries from JavaScript as shown below.

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



---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




