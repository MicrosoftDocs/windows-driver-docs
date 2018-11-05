---
title: amli set
description: The amli set extension sets or displays the AMLI Debugger options.
ms.assetid: 521fa305-8073-4d94-bc28-fdb35cbc2acd
keywords: ["amli set Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli set
api_type:
- NA
ms.localizationpriority: medium
---

# !amli set


The **!amli set** extension sets or displays the AMLI Debugger options.

```dbgcmd
    !amli set Options
```

## <span id="ddk__amli_set_dbg"></span><span id="DDK__AMLI_SET_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies one or more options to be set. Separate multiple options with spaces. Possible values include:

<span id="spewon"></span><span id="SPEWON"></span>**spewon**  
Causes full debug output to be sent from the target computer. This option should be left on at all times for effective AML debugging. See the Remarks section for details.

<span id="spewoff"></span><span id="SPEWOFF"></span>**spewoff**  
Suppresses debug output.

<span id="verboseon"></span><span id="VERBOSEON"></span>**verboseon**  
Turns on verbose mode. This causes the AMLI Debugger to display the names of AML methods as they are evaluated.

<span id="verboseoff"></span><span id="VERBOSEOFF"></span>**verboseoff**  
Turns off verbose mode.

<span id="traceon"></span><span id="TRACEON"></span>**traceon**  
Activates ACPI tracing. This produces much more output than the **verboseon** option. This option is very useful for tracking SMI-related hard hangs.

<span id="traceoff"></span><span id="TRACEOFF"></span>**traceoff**  
Deactivates ACPI tracing.

<span id="nesttraceon"></span><span id="NESTTRACEON"></span>**nesttraceon**  
Activates nest tracing. This option is only effective if the **traceon** option is also selected.

<span id="dbgbrkon"></span><span id="DBGBRKON"></span>**dbgbrkon**  
Enables breaking into the AMLI Debugger.

<span id="dbgbrkoff"></span><span id="DBGBRKOFF"></span>**dbgbrkoff**  
Deactivates the dbgbrkon option.

<span id="nesttraceoff"></span><span id="NESTTRACEOFF"></span>**nesttraceoff**  
Deactivates nest tracing.

<span id="lbrkon"></span><span id="LBRKON"></span>**lbrkon**  
Breaks into the AMLI Debugger when DDB loading is completed.

<span id="lbrkoff"></span><span id="LBRKOFF"></span>**lbrkoff**  
Deactivates the **lbrkon** option.

<span id="errbrkon"></span><span id="ERRBRKON"></span>**errbrkon**  
Breaks into the AMLI Debugger whenever the interpreter has a problem evaluating AML code.

<span id="errbrkoff"></span><span id="ERRBRKOFF"></span>**errbrkoff**  
Deactivates the **errbrkon** option.

<span id="logon"></span><span id="LOGON"></span>**logon**  
Enables event logging.

<span id="logoff"></span><span id="LOGOFF"></span>**logoff**  
Disables event logging.

<span id="logmuton"></span><span id="LOGMUTON"></span>**logmuton**  
Enables mutex event logging.

<span id="logmutoff"></span><span id="LOGMUTOFF"></span>**logmutoff**  
Disables mutex event logging.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

If no options are specified, the current status of all options is displayed.

By default, many messages are filtered out, you may need to turn this output on with **!amli set spewon**. Otherwise, numerous AMLI Debugger messages will be lost.

If the AML interpreter breaks into the AMLI Debugger, this output will be automatically turned on.

For more details on this output filtering, see **DbgPrintEx** and **KdPrintEx** in the Windows Driver Kit (WDK) documentation.

 

 





