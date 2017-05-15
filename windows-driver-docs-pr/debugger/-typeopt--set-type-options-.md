---
title: .typeopt (Set Type Options)
description: The .typeopt command sets or displays the type options.
ms.assetid: 17842897-26e3-4b61-aa65-e5cfe8576324
keywords: [".typeopt (Set Type Options) Windows Debugging"]
topic_type:
- apiref
api_name:
- .typeopt (Set Type Options)
api_type:
- NA
---

# .typeopt (Set Type Options)


The **.typeopt** command sets or displays the type options.

``` syntax
.typeopt +Flags 
.typeopt -Flags 
.typeopt +FlagName 
.typeopt -FlagName 
.typeopt 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="______________"></span> **+**   
Causes the type options specified by *FlagName* to be set.

<span id="_______-______"></span> **-**   
Causes the type options specified by *FlagName* to be cleared.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the type options to be changed. *FlagName* can be a sum of any of the following values (there is no default):

<span id="0x1"></span><span id="0X1"></span>**0x1**  
Displays values in all Watch windows and the Locals window as having UNICODE data type.

<span id="0x2"></span><span id="0X2"></span>**0x2**  
Displays values in all Watch windows and the Locals window as having LONG data type.

<span id="0x4"></span><span id="0X4"></span>**0x4**  
Displays integers in all Watch windows and the Locals window in the default radix.

<span id="0x8"></span><span id="0X8"></span>**0x8**  
Causes the debugger to choose the matching symbol with the largest size when the Locals window or Watch window references a symbol by name but there is more than one symbol that matches this name. The size of a symbol is defined as follows: if the symbol is the name of a function, its size is the size of the function in memory. Otherwise, the size of the symbol is the size of the data type that it represents.

<span id="_______FlagName______"></span><span id="_______flagname______"></span><span id="_______FLAGNAME______"></span> *FlagName*   
Specifies the type options to be changed. *FlagName* can be any one of the following strings (there is no default):

<span id="uni"></span><span id="UNI"></span>**uni**  
Displays values in all Watch windows and the Locals window as having UNICODE data type. (This has the same effect as **0x1**.)

<span id="longst"></span><span id="LONGST"></span>**longst**  
Displays values in all Watch windows and the Locals window as having LONG data type. (This has the same effect as **0x2**.)

<span id="radix"></span><span id="RADIX"></span>**radix**  
Displays integers in all Watch windows and the Locals window in the default radix. (This has the same effect as **0x4**.)

<span id="size"></span><span id="SIZE"></span>**size**  
Causes the debugger to choose the matching symbol with the largest size when the Locals window or Watch window references a symbol by name but there is more than one symbol that matches this name. The size of a symbol is defined as follows: if the symbol is the name of a function, its size is the size of the function in memory. Otherwise, the size of the symbol is the size of the data type that it represents. (This has the same effect as **0x8**.)

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

Without any arguments, **.typeopt** displays the current symbol options.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.typeopt%20%28Set%20Type%20Options%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




