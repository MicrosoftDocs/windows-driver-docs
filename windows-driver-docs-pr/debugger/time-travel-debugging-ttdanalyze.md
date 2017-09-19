---
title: Time Travel Debugging - TTDAnalyze
description: This section describes how to use the TTDAnalyze to analyze time travel traces.
ms.author: windowsdriverdev
ms.date: 09/19/2017
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
TBD TBD TBD 
TBD TBD TBD 

**This topic contains random notes and is not ready for review**

TBD TBD TBD 
TBD TBD TBD 
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

## Using TTDAnalyze

Follow these steps to use TTDAnalyze.

1. Load the TTDAnalyze.dll debugger extension. Note that the path to the extension repository is added autmatically, so no path is required ??? TBD.

```
load C:\TTDAnalyze.dll
```

2. Optionally load the associated JavaScripts.

```

```
3. Load the 

```

```

## JavaScripts

Two JavaScripts:
TTDAnalyze.js

which might call...

HeapAnalysis.js

## TTD Data
   capturedSession 
   Heap     

## TTD Utility

    capturedSession 
    GetHeapAddress  


##  capturedSession 
 
 
##  Heap    


## TBD

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

```


 Prerequisite: ttdanalyze.dll debugger extension has been loaded in the debugger

 This extension projects raw call data from ttdanalyze (provided by @$cursession.TTD.Calls())
 into friendlier data that is specific to Heap APIs and hides Windows implementation details.

 The following extensions to the datamodel are provided:

 dx @$cursession.TTDUtils.HeapAPICalls()
 --------------------------------
 Returns an indexable list of heap API operations that change the address space in some way:
 alloc, realloc, free and a few others. It does not return heap API operations that are just
 queries (e.g. getting size of allocated block.)

 0:000> dx -g @$cursession.TTDUtils.HeapAPICalls()
 ===================================================================================================================
 =           = Action   = Heap             = Address          = Size     = Flags  = (+) TimeRange         = Result =
 ===================================================================================================================
 = [0x0]     - Alloc    - 0x1a3f7430000    - 0x1a3f7459b40    - 0x208    - 0x0    - [10:EE, 12:36]        -        =
 = [0x1]     - Free     - 0x1a3f7430000    - 0x1a3f7459b40    -          - 0x0    - [12:472, 14:2B]       - 0x1    =
 = [0x2]     - Alloc    - 0x1a3f7430000    - 0x1a3f744bb90    - 0x7b     - 0x8    - [14:23A8, 16:36]      -        =
 = [0x3]     - Alloc    - 0x1a3f7430000    - 0x1a3f744bc40    - 0x46     - 0x0    - [17:79D, 19:36]       -        =
 = [0x4]     - Free     - 0x1a3f7430000    - 0x1a3f744bc40    -          - 0x0    - [1D:32, 1F:2B]        - 0x1    =
 = [0x5]     - Alloc    - 0x1a3f7430000    - 0x1a3f744bc40    - 0x10     - 0x0    - [50:167, 52:36]       -        =
 = [0x6]     - Alloc    - 0x1a3f7430000    - 0x1a3f7439ff0    - 0x38     - 0x0    - [AD:6F, AF:36]        -        =
 = [0x7]     - Alloc    - 0x1a3f7430000    - 0x1a3f744bc80    - 0x2      - 0x0    - [AF:FD, B1:36]        -        =
 = [0x8]     - Free     - 0x1a3f7430000    - 0x1a3f744bc80    -          - 0x0    - [B3:76, B5:2B]        - 0x1    =
 = [0x9]     - Alloc    - 0x1a3f7430000    - 0x1a3f744bc80    - 0x2      - 0x0    - [B5:CF, B7:36]        -        =
 ===================================================================================================================

 Most fields should be self explanatory. If you click on a TimeRange you will see the extent of the call:

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

 Clicking on [Time Travel] will take you to that position in the trace.

 [ Note: As of 6/5/2017 there is a bug that prevents clicking on that link from working (#12139327.) There are
  three workarounds:
     1. Enter a !tt <position> command manually (e.g. !tt 50:167)
     2. Point dx to the MinPosition / MaxPosition directly and *then* click the link
        (e.g. dx @$cursession.TTDUtils.HeapAPICalls()[5].TimeRange.MinPosition)
     3. Invoke the .SeekTo() method directly 
        (e.g.  dx @$cursession.TTDUtils.HeapAPICalls()[5].TimeRange.MinPosition.SeekTo())
 ]

 dx @$cursession.TTDUtils.GetHeapAddress(address)
 --------------------------------------------
 Filters HeapAPICalls() to just the entries that impact the specified address. The address can point anywhere inside a memory block, it is not required to point to
 the start of a block.

 Example use: Debugging a critical heap error (but see HeapAnalyze() below for the easier way...)

 Start by ensuring trace is indexed:

 0:000> !index
 Indexed 1/1 keyframes
 Successfully created the index in 29ms.

 Use !events to navigate to the spot where the critical error is raised (which gives example queries to use in place of !events):

 0:000> !events
 This command is not supported. You can now use the Data Model to explore events in the trace.
 Use dx to query for what you are looking for. Examples:
 - Querying for exceptions:
    dx @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception) 
 - Querying for the load event(s) of a particular module
    dx @$curprocess.TTD.Events.Where(t => t.Type == "ModuleLoaded").Where(t => t.Module.Name.Contains("ntdll.dll")) 
 - Querying for the threads that get created
    dx -g @$curprocess.TTD.Events.Where(t => t.Type == "ThreadCreated").Select(t => t.Thread) 
 
 To learn more visit https:aka.ms/ttddatamodel 

 Click on the first query to get the list of exceptions and click on the exception to get details:

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

 0xc0000374 is the exception code for a heap error. Travel to that position and dump the start of the stack with parameters. The 4th parameter is the
 heap address that has a problem:

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

 Ask TTD to locate all of the operations that impacted the address:

 0:000> dx -g @$cursession.TTDUtils.GetHeapAddress(0x00000235`7942f860)
 =====================================================================================================================
 =          = Action   = Heap             = Address          = Size    = Flags  = (+) TimeRange      = Result        =
 =====================================================================================================================
 = [0x0]    - Alloc    - 0x23579330000    - 0x2357942f860    - 0x32    - 0x0    - [59:12, 5B:36]     -               =
 = [0x1]    - Free     - 0x23579330000    - 0x2357942f860    -         - 0x0    - [63:13, 65:2B]     - 0x1           =
 = [0x2]    - Free     - 0x23579330000    - 0x2357942f860    -         - 0x0    - [6D:13, 6D:B13]    - 0x6917108b    =
 =====================================================================================================================

 From this it is easy to see that the problem is a double free. The time positions for both the first and second free can be navigated to in order to understand the root cause.

 dx -g @$cursession.TTDUtils.HeapAnalyze()
 -----------------------------------------
 .GetHeapAddress() is a useful generic function but that was alot of manual steps with specific domain knowledge to get the answer.
 As a demonstration of checkers, HeapAnalyze() automates the above analysis. Simply run HeapAnalyze() and it will determine if a 
 heap error is in the trace and display the relevant heap operation information:

 0:000> dx -g @$cursession.TTDUtils.HeapAnalyze()
 Heap failure detected!
     error: heap_failure_block_not_busy
      heap: 0x23579330000
   address: 0x2357942f860
 =====================================================================================================================
 =          = Action   = Heap             = Address          = Size    = Flags  = (+) TimeRange      = Result        =
 =====================================================================================================================
 = [0x0]    - Alloc    - 0x23579330000    - 0x2357942f860    - 0x32    - 0x0    - [59:12, 5B:36]     -               =
 = [0x1]    - Free     - 0x23579330000    - 0x2357942f860    -         - 0x0    - [63:13, 65:2B]     - 0x1           =
 = [0x2]    - Free     - 0x23579330000    - 0x2357942f860    -         - 0x0    - [6D:13, 6D:B13]    - 0x6917108b    =
 =====================================================================================================================


```



> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




