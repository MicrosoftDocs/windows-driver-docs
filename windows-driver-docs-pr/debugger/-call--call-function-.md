---
title: .call (Call Function)
description: The .call command causes the target process to execute a function.
ms.assetid: 93265c2a-ea4d-4523-928c-1bb75a9356b1
keywords: [".call (Call Function) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .call (Call Function)
api_type:
- NA
ms.localizationpriority: medium
---

# .call (Call Function)


The **.call** command causes the target process to execute a function.

```dbgsyntax
.call [/v] Function( Arguments ) 
.call /s Prototype Function( Arguments ) 
.call /c 
.call /C 
```

## <span id="ddk_meta_call_function_dbg"></span><span id="DDK_META_CALL_FUNCTION_DBG"></span>Parameters


<span id="________v______"></span><span id="________V______"></span> **/v**   
Verbose information about the call and its arguments is displayed.

<span id="________s________Prototype______"></span><span id="________s________prototype______"></span><span id="________S________PROTOTYPE______"></span> **/s** *Prototype*   
Allows you to call the function that is specified by *Function* even though you do not have the correct symbols. In this case, you must have symbols for another function that has the same calling prototype as the function you are trying to call. The *Prototype* parameter is the name of this prototype function.

<span id="_______Function______"></span><span id="_______function______"></span><span id="_______FUNCTION______"></span> *Function*   
Specifies the function being called. This can be the name of the function (preferably qualified with a module name), or any other expression that evaluates to the function address. If you need to call a constructor or destructor, you must supply the address -- or else use a C++ expression to evaluate named syntax for the operators (see [Numerical Expression Syntax](numerical-expression-syntax.md) for details).

<span id="_______Arguments______"></span><span id="_______arguments______"></span><span id="_______ARGUMENTS______"></span> *Arguments*   
Specifies the arguments passed to the function. If you are calling a method, the first argument must be **this**, and all other arguments follow it. Arguments should be separated with commas and should match the usual argument syntax. Variable-length argument lists are supported. Expressions within an argument are parsed by the C++ expression evaluator; see [C++ Numbers and Operators](c---numbers-and-operators.md) for details. You cannot enter a literal string as an argument, but you can use a pointer to a string, or any other memory accessible to the target process.

<span id="________c______"></span><span id="________C______"></span> **/c**   
Clears any existing call on the current thread.

<span id="________C______"></span><span id="________c______"></span> **/C**   
Clears any existing call on the current thread, and resets the context of the current thread to the context stored by the outstanding call.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86 and x64 only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The specified function is called by the current thread of the current process.

Only the **cdecl**, **stdcall**, **fastcall**, and **thiscall** calling conventions are supported. Managed code cannot be called by this command.

After **.call** is used, the debugger will update the stack, change the instruction pointer to point to the beginning of the called function, and then stop. Use [**g (Go)**](g--go-.md) to resume execution, or **~. g** to execute just the thread making the call.

When the function returns, a break occurs and the debugger displays the return value of the function. The return value is also stored in the **$callret** pseudo-register, which acquires the type of the return value.

If you have broken into the target using CTRL+C or CTRL+BREAK, the current thread is an additional thread created to handle the breakin. If you issue a **.call** command at this point, the extra thread will be used for the called function.

If you have reached a predefined breakpoint, there is no extra breakin thread. If you use **.call** while at a breakpoint in user mode, you could use [**g**](g--go-.md) to execute the entire process, or **~. g** to execute just the current thread. Using **g** may distort your program's behavior, since you have taken one thread and diverted it to this new function. On the other hand, this thread will still have its locks and other attributes, and thus **~. g** may risk deadlocks.

The safest way to use **.call** is to set a breakpoint in your code at a location where a certain function could be safely called. When that breakpoint is hit, you can use **.call** if you desire that function to run. If you use **.call** at a point where this function could not normally be called, a deadlock or target corruption could result.

It may be useful to add extra functions to your source code that are not called by the existing code, but are intended to be called by the debugger. For example, you could add functions that are used to investigate the current state of your code and its environment and store information about the state in a known memory location. Be sure not to optimize your code, or these functions may be removed by the compiler. Use this technique only as a last resort, because if your application crashes **.call** will not be available when debugging the dump file.

The **.call /c** and **.call /C** commands should only be used if an attempt to use **.call** has failed, or if you changed your mind before entering the [**g**](g--go-.md) command. These should not be used casually, since abandoning an uncompleted call can lead to a corrupted target state.

The following code example shows how the **.call /s** command is used.

```dbgcmd
.call /s KnownFunction UnknownFunction( 1 )
```

In this example, you have private symbols for **KnownFunction**, which takes an integer as its only argument and returns, for example, a pointer to an array. You do not have symbols, or possibly you only have public symbols for **UnknownFunction**, but you do know that it takes an integer as its only argument and returns a pointer to an array. By using the **/s** option, you can specify that **UnknownFunction** will work the same way that **KnownFunction** does. Thus, you can successfully generate a call to **UnknownFunction**.

 

 





