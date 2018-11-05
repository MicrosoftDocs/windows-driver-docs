---
title: avrf
description: The avrf extension controls the settings of Application Verifier and displays a variety of output produced by Application Verifier.
ms.assetid: e9313954-a1fa-45a9-bc1a-78be2451f5aa
keywords: ["avrf Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- avrf
api_type:
- NA
ms.localizationpriority: medium
---

# !avrf


The **!avrf** extension controls the settings of [Application Verifier](application-verifier.md) and displays a variety of output produced by Application Verifier.

```dbgcmd
    !avrf
    !avrf -vs { Length | -a Address }
    !avrf -hp { Length | -a Address }
    !avrf -cs { Length | -a Address }
    !avrf -dlls [ Length ]
    !avrf -trm
    !avrf -ex [ Length ] 
    !avrf -threads [ ThreadID ]
    !avrf -tp [ ThreadID ]
    !avrf -srw  [ Address | Address Length ] [ -stats ]
    !avrf -leak  [ -m ModuleName] [ -r ResourceType] [ -a Address ] [ -t ]
    !avrf -trace TraceIndex 
    !avrf -cnt
    !avrf -brk [BreakEventType]  
    !avrf -flt [EventType Probability] 
    !avrf -flt break EventType 
    !avrf -flt stacks Length 
    !avrf -trg [ Start End | dll Module | all ] 
    !avrf -settings 
    !avrf -skp [ Start End | dll Module | all | Time ] 
```

## <span id="ddk__avrf_dbg"></span><span id="DDK__AVRF_DBG"></span>Parameters


<span id="-vs___Length___-a_Address__"></span><span id="-vs___length___-a_address__"></span><span id="-VS___LENGTH___-A_ADDRESS__"></span>**-vs {** *Length* **| -a** *Address* **}**  
Displays the virtual space operation log. *Length* specifies the number of records to display, starting with the most recent. *Address* specifies the virtual address. Records of the virtual operations that contain this virtual address are displayed.

<span id="-hp___Length___-a_Address__"></span><span id="-hp___length___-a_address__"></span><span id="-HP___LENGTH___-A_ADDRESS__"></span>**-hp {** *Length* **| -a** *Address* **}**  
Displays the heap operation log. *Address* specifies the heap address. Records of the heap operations that contain this heap address are displayed.

<span id="-cs___Length___-a_Address__"></span><span id="-cs___length___-a_address__"></span><span id="-CS___LENGTH___-A_ADDRESS__"></span>**-cs {** *Length* **| -a** *Address* **}**  
Displays the critical section delete log. *Length* specifies the number of records to display, starting with the most recent. *Address* specifies the critical section address. Records for the particular critical section are displayed when *Address* is specified.

<span id="-dlls___Length__"></span><span id="-dlls___length__"></span><span id="-DLLS___LENGTH__"></span>**-dlls \[** *Length* **\]**  
Displays the DLL load/unload log. *Length* specifies the number of records to display, starting with the most recent.

<span id="-trm"></span><span id="-TRM"></span>**-trm**  
Displays a log of all terminated and suspended threads.

<span id="-ex___Length__"></span><span id="-ex___length__"></span><span id="-EX___LENGTH__"></span>**-ex \[** *Length* **\]**  
Displays the exception log. Application Verifier tracks all the exceptions in the application.

<span id="-threads___ThreadID__"></span><span id="-threads___threadid__"></span><span id="-THREADS___THREADID__"></span>**-threads \[** *ThreadID* **\]**  
Displays information about threads in the target process. For child threads, the stack size and the **CreateThread** flags specified by the parent are also displayed. If you provide a thread ID, information for only that thread is displayed.

<span id="-tp___ThreadID___"></span><span id="-tp___threadid___"></span><span id="-TP___THREADID___"></span>**-tp \[** *ThreadID* **\]**   
Displays the threadpool log. This log contains stack traces for various operations such as changing the thread affinity mask, changing thread priority, posting thread messages, and initializing or uninitializing COM from within the threadpool callback. If you provide a thread ID, information for that thread only is displayed.

<span id="-srw____Address___Address_Length_____-stats___"></span><span id="-srw____address___address_length_____-stats___"></span><span id="-SRW____ADDRESS___ADDRESS_LENGTH_____-STATS___"></span>**-srw \[** *Address* **|** *Address Length* **\] \[ -stats \]**   
Displays the Slim Reader/Writer (SRW) log. If you specify *Address*, records for the SRW lock at that address are displayed. If you specify *Address* and *Length*, records for SRW locks in that address range are displayed. If you include the **-stats** option, the SRW lock statistics are displayed.

<span id="-leak___-m_ModuleName____-r_ResourceType____-a_Address_____-t___"></span><span id="-leak___-m_modulename____-r_resourcetype____-a_address_____-t___"></span><span id="-LEAK___-M_MODULENAME____-R_RESOURCETYPE____-A_ADDRESS_____-T___"></span>**-leak \[ -m** <em>ModuleName</em>**\] \[ -r** <em>ResourceType</em>**\] \[ -a** *Address* **\] \[ -t \]**   
Displays the outstanding resources log. These resources may or may not be leaks at any given point. If you specify *Modulename* (including the extension), all outstanding resources in the specified module are displayed. If you specify *ResourceType*, all outstanding resources of that resource type are displayed. If you specify *Address*, records of outstanding resources with that address are displayed. *ResourceType* can be one of the following:

Heap: Displays heap allocations using Win32 Heap APIs

Local: Displays Local/Global allocations

CRT: Displays allocations using CRT APIs

Virtual: Displays Virtual reservations

BSTR: Displays BSTR allocations

Registry: Displays Registry key opens

Power: Displays power notification objects

Handle: Displays thread, file, and event handle allocations

<span id="-trace_TraceIndex"></span><span id="-trace_traceindex"></span><span id="-TRACE_TRACEINDEX"></span>**-trace** *TraceIndex*
Displays a stack trace for the specified trace index. Some structures use this 16-bit index number to identify a stack trace. This index points to a location within the stack trace database.

<span id="-cnt"></span><span id="-CNT"></span>**-cnt**
Displays a list of global counters.

<span id="-brk___BreakEventType__"></span><span id="-brk___breakeventtype__"></span><span id="-BRK___BREAKEVENTTYPE__"></span>**-brk \[** *BreakEventType* **\]**
Specifies a break event. *BreakEventType* is the type number of the break event. For a list of possible types, and a list of the current break event settings, enter **!avrf -brk**.

<span id="-flt___EventType_Probability__"></span><span id="-flt___eventtype_probability__"></span><span id="-FLT___EVENTTYPE_PROBABILITY__"></span>**-flt \[** *EventType Probability* **\]**
Specifies a fault injection. *EventType* is the type number of the event. *Probability* is the frequency with which the event will fail. This can be any integer between 0 and 1,000,000 (0xF4240). If you enter **!avrf -flt** with no additional parameters, the current fault injection settings are displayed.

<span id="-flt_break_EventType"></span><span id="-flt_break_eventtype"></span><span id="-FLT_BREAK_EVENTTYPE"></span>-**flt break** *EventType*
Causes Application Verifier to break into the debugger each time this fault, specified by *EventType*, is injected.

<span id="-flt_stacks_Length"></span><span id="-flt_stacks_length"></span><span id="-FLT_STACKS_LENGTH"></span>**-flt stacks** *Length*
Displays *Length* number of stack traces for the most recent fault-injected operations.

<span id="-trg___Start_End___dll_Module___all____"></span><span id="-trg___start_end___dll_module___all____"></span><span id="-TRG___START_END___DLL_MODULE___ALL____"></span>**-trg \[** *Start End* **| dll** *Module* **| all \]**
Specifies a target range. *Start* is the beginning address of the target range. *End* is the ending address of the target range. *Module* specifies the name (including the .exe or .dll extension, but not including the path) of a module to be targeted. If you enter **-trg all**, all target ranges are reset. If you enter **-trg** with no additional parameters, the current target ranges are displayed.

<span id="-skp___Start_End___dll_Module___all___Time____"></span><span id="-skp___start_end___dll_module___all___time____"></span><span id="-SKP___START_END___DLL_MODULE___ALL___TIME____"></span>**-skp \[** *Start End* **| dll** *Module* **| all |** *Time* **\]**
Specifies an exclusion range. *Start* is the beginning address of the exclusion range. *End* is the ending address of the exclusion range. Module specifies the name of a module to be targeted or excluded. *Module* specifies the name (including the .exe or .dll extension, but not including the path) of a module to be excluded. If you enter **-skp all**, all target ranges or exclusion ranges are reset. If you enter a*Time* value, all faults are suppressed for *Time* milliseconds after execution resumes.

### <span id="DLL"></span><span id="dll"></span>DLL

exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about how to download and install Application Verifier and its documentation, see [Application Verifier](application-verifier.md).

Remarks
-------

When the **!avrf** extension is used with no parameters, it displays the current Application Verifier options. If the **Full page heap** or **Fast fill heap** option has been enabled, information about active page heaps is displayed as well. For some examples, see "Heap Operation Logs" in the Application Verifier documentation.

If an Application Verifier Stop has occurred, the **!avrf** extension with no parameters will reveal the nature of the stop and its cause. For some examples, see "Debugging Application Verifier Stops" in the Application Verifier documentation.

If symbols for ntdll.dll and verifier.dll are missing, the **!avrf** extension generates an error message. For information about how to address this problem, see "Setting Up a Debugger for Application Verifier" in the Application Verifier documentation.

 

 





