---
title: Conditional breakpoints in WinDbg and other Windows debuggers
description: Conditional breakpoints in WinDbg and other Windows debuggers are useful when you need to break in only if a specific condition is satisfied.
keywords: ["breakpoints, conditional", "conditional breakpoints"]
ms.date: 05/23/2017
---

# Conditional breakpoints in WinDbg and other Windows debuggers


Conditional breakpoints in WinDbg and other Windows debuggers are useful when you need to break in only if a specific condition is satisfied.

## <span id="ddk_setting_a_conditional_breakpoint_dbg"></span><span id="DDK_SETTING_A_CONDITIONAL_BREAKPOINT_DBG"></span>


A conditional breakpoint is created with the "/w" parameter to the [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) or other breakpoint command. The basic syntax of the command is:

```dbgcmd
0:000> bp /w "(Condition)" Address
```

The breakpoint will only cause a break into the debugger when the specified condition is true. The "w" is an abbreviation for "when". The condition expression can be anything that can be used with the [**dx (Display Debugger Object Model Expression)**](dx--display-visualizer-variables-.md) command. This includes most C++ style expressions including comparisons, arithmetic, pointer operations, and others. For instance, a basic conditional breakpoint that only breaks in when a variable is more than 20 could be written as:

```dbgcmd
0:000> bp /w "MyVar > 20" `mysource.cpp:143`
```

Since the condition is evaluated using the debugger object model, you can also take advantage of things like NatVis support. For instance, assuming myVec is a `std::vector<int>`, you could create a condition such as:

```dbgcmd
0:000> bp /w "myVec.Count() == 4" `mysource.cpp:143`
```

This will break in when line 143 of mysource.cpp is executed while the myVec variable has 4 elements.

Beyond natvis, you can also invoke a JavaScript function. If you load a script using the WinDbg script window or the [**.scriptload (Load Script)**](-scriptload--load-script-.md) command which contains a function called "myFunc", you could set a breakpoint like this:

```dbgcmd
0:000> bp /w "@$scriptContents.myFunc()" `mysource.cpp:143`
```

For more information about writing JavaScript functions and extensions in the debugger, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md)

While higher level expressions are typically the most useful, it's also possible to evaluate registers using these expresions. For instance, you could create a breakpoint that only triggers when the stack pointer reaches some threshold:

```dbgcmd
0:000> bp /w "@esp < 0x6ff9f8" `mysource.cpp:143`
```


### <span id="legacy_conditional_breakpoint_syntax"></span>Legacy conditional breakpoint syntax

Before the availability of the "/w" parameter to the breakpoint commands, the recommended way to set conditional breakpoints was to use the [**j (Execute If - Else)**](j--execute-if---else-.md) command or the [**.if**](-if.md) token, followed by the [**gc (Go from Conditional Breakpoint)**](gc--go-from-conditional-breakpoint-.md) command. While these methods of setting conditional breakpoints are no longer recommended, they do still function and you may see this syntax referenced in other sources.

The basic syntax for a conditional breakpoint using the **j** command is as follows:

```dbgcmd
0:000> bp Address "j (Condition) 'OptionalCommands'; 'gc' "
```

The basic syntax for a conditional breakpoint using the **.if** token is as follows:

```dbgcmd
0:000> bp Address ".if (Condition) {OptionalCommands} .else {gc}"
```
