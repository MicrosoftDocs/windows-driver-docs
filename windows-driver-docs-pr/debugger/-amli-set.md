---
title: amli set
description: The amli set extension sets or displays the AMLI Debugger options.
ms.assetid: 521fa305-8073-4d94-bc28-fdb35cbc2acd
keywords: ["amli set Windows Debugging"]
topic_type:
- apiref
api_name:
- amli set
api_type:
- NA
---

# !amli set


The **!amli set** extension sets or displays the AMLI Debugger options.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20set%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




