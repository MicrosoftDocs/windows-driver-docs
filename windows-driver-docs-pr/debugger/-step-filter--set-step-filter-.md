---
title: .step_filter (Set Step Filter)
description: The .step_filter command creates a list of functions that are skipped (stepped over) when tracing.
ms.assetid: 9ce2bed4-fac0-4537-a129-7cb9f1e8725e
keywords: [".step_filter (Set Step Filter) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .step_filter (Set Step Filter)
api_type:
- NA
ms.localizationpriority: medium
---

# .step\_filter (Set Step Filter)


The **.step\_filter** command creates a list of functions that are skipped (stepped over) when tracing. This allows you to trace through code and skip only certain functions. It can also be used in source mode to control stepping when there are multiple function calls on one line.

```dbgcmd
.step_filter "FilterList" 
.step_filter /c 
.step_filter 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_FilterList_"></span><span id="_filterlist_"></span><span id="_FILTERLIST_"></span>**"**<em>FilterList</em>**"**  
Specifies the symbols associated with functions to be stepped over. *FilterList* can contain any number of text patterns separated by semicolons. Each of these patterns may contain a variety of wildcards and specifiers; see [String Wildcard Syntax](string-wildcard-syntax.md) for details. A function whose symbol matches at least one of these patterns will be stepped over during tracing. Each time **"**<em>FilterList</em>**"** is used, any previous filter list is discarded and completely replaced with the new list.

<span id="________c______"></span><span id="________C______"></span> **/c**   
Clears the filter list.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Without any parameters, **.step\_filter** displays the current filter list.

Typically, a trace command (for example, [**t**](t--trace-.md) or the windbg [debug | step into](debug---step-into.md) button ![screen shot of the step into button](images/tbinto.png)) traces into a function call. However, if the symbol associated with the function being called matches a pattern specified by *FilterList*, the function will be stepped over -- as if a step command (for example, [**p**](p--step-.md)) had been used.

If the instruction pointer is located within code that is listed in the filter list, any trace or step commands will step out of this function, like the [**gu**](gu--go-up-.md) command or the WinDbg **Step Out** button. Of course, this filter would prevent such code from having been traced into in the first place, so this will only happen if you have changed the filter or hit a breakpoint.

For example, the following command will cause trace commands to skip over all CRT calls:

```dbgcmd
.step_filter "msvcrt!*" 
```

The **.step\_filter** command is most useful when you are debugging in source mode, because there can be multiple function calls on a single source line. The [**p**](p--step-.md) and [**t**](t--trace-.md) commands cannot be used to separate these function calls.

For example, in the following line, the [**t**](t--trace-.md) command will step into both GetTickCount and printf, while the [**p**](p--step-.md) command will step over both function calls:

```dbgcmd
printf( "%x\n", GetTickCount() );
```

The **.step\_filter** command allows you to filter out one of these calls while still tracing into the other.

Because the functions are identified by symbol, a single filter can include an entire module. This lets you filter out framework functions -- for example, Microsoft Foundation Classes (MFC) or Active Template Library (ATL) calls.

When debugging in assembly mode, each call is on a different line, so you can choose whether to step or trace line-by-line. So **.step\_filter** is not very useful in assembly mode.

 

 





