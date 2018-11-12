---
title: Conditional breakpoints in WinDbg and other Windows debuggers
description: Conditional breakpoints in WinDbg and other Windows debuggers are useful when you need to break in only if a specific condition is satisfied.
ms.assetid: 9fa5b417-8904-48bc-ad5c-62ba35d70b73
keywords: ["breakpoints, conditional", "conditional breakpoints"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Conditional breakpoints in WinDbg and other Windows debuggers


Conditional breakpoints in WinDbg and other Windows debuggers are useful when you need to break in only if a specific condition is satisfied.

## <span id="ddk_setting_a_conditional_breakpoint_dbg"></span><span id="DDK_SETTING_A_CONDITIONAL_BREAKPOINT_DBG"></span>


A conditional breakpoint is created by combining a breakpoint command with either the [**j (Execute If - Else)**](j--execute-if---else-.md) command or the [**.if**](-if.md) token, followed by the [**gc (Go from Conditional Breakpoint)**](gc--go-from-conditional-breakpoint-.md) command. This breakpoint causes a break to occur only if a specific condition is satisfied.

The basic syntax for a conditional breakpoint using the **j** command is as follows:

```dbgcmd
0:000> bp Address "j (Condition) 'OptionalCommands'; 'gc' "
```

The basic syntax for a conditional breakpoint using the **.if** token is as follows:

```dbgcmd
0:000> bp Address ".if (Condition) {OptionalCommands} .else {gc}"
```

Conditional breakpoints are best illustrated with an example. The following command sets a breakpoint at line 143 of the Mysource.cpp source file. When this breakpoint is hit, the variable **MyVar** is tested. If this variable is less than or equal to 20, execution continues; if it is greater than 20, execution stops.

```dbgcmd
0:000> bp `mysource.cpp:143` "j (poi(MyVar)>0n20) ''; 'gc' " 
0:000> bp `mysource.cpp:143` ".if (poi(MyVar)>0n20) {} .else {gc}"
```

The preceding command has a fairly complicated syntax that contains the following elements:

-   The [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command sets breakpoints. Although the preceding example uses the bp command, you could also use the **bu (Set Unresolved Breakpoint)** command. For more information about the differences between **bp** and **bu**, and for a basic introduction to breakpoints, see [Using Breakpoints](using-breakpoints.md).

-   Source line numbers are specified by using grave accents ( **\`** ). For details, see [Source Line Syntax](source-line-syntax.md).

-   When the breakpoint is hit, the command in straight quotation marks ( **"** ) is executed. In this example, this command is a [**j (Execute If - Else)**](j--execute-if---else-.md) command or an [**.if**](-if.md) token, which tests the expression in parentheses.

-   In the source program, **MyVar** is an integer. If you are using C++ expression syntax, **MyVar** is interpreted as an integer. However, in this example (and in the default debugger configuration), MASM expression syntax is used. In a MASM expression, **MyVar** is treated as an address. Thus, you need to use the **poi** operator to dereference it. (If your variable actually is a C pointer, you will need to dereference it twice--for example, **poi(poi(MyPtr))**.) The **0n** prefix specifies that this number is decimal. For syntax details, see [MASM Numbers and Operators](masm-numbers-and-operators.md).

-   The expression in parentheses is followed by two commands, surrounded by single quotation marks ( **'** ) for the **j** command and curly brackets ( {} ) for the **.if** token. If the expression is true, the first of these commands is executed. In this example, there is no first command, so command execution will end and control will remain with the debugger. If the expression in parentheses is false, the second command will execute. The second command should almost always be a [**gc (Go from Conditional Breakpoint)**](gc--go-from-conditional-breakpoint-.md) command, because this command causes execution to resume in the same manner that was occurring before the breakpoint was hit (stepping, tracing, or free execution).

If you want to see a message each time the breakpoint is passed or when it is finally hit, you can use additional commands in the single quotation marks or curly brackets. For example:

```dbgcmd
0:000> bp `:143` "j (poi(MyVar)>5) '.echo MyVar Too Big'; '.echo MyVar Acceptable; gc' " 
0:000> bp `:143` ".if (poi(MyVar)>5) {.echo MyVar Too Big} .else {.echo MyVar Acceptable; gc} " 
```

These comments are especially useful if you have several such breakpoints running at the same time, because the debugger does not display its standard "Breakpoint *n* Hit" messages when you are using a command string in the **bp** command.

### <span id="Conditional_Breakpoint_Based_on_String_Comparison"></span><span id="conditional_breakpoint_based_on_string_comparison"></span><span id="CONDITIONAL_BREAKPOINT_BASED_ON_STRING_COMPARISON"></span>Conditional Breakpoint Based on String Comparison

In some situations you might want to break into the debugger only if a string variable matches a pattern. For example, suppose you want to break at kernel32!CreateEventW only if the *lpName* argument points to a string that matches the pattern "Global\*". The following example shows how to create the conditional breakpoint.

```dbgcmd
bp kernel32!CreateEventW "$$<c:\\commands.txt"
```

The preceding [**bp**](bp--bu--bm--set-breakpoint-.md) command creates a breakpoint based on conditions and optional commands that are in a script file named commands.txt. The script file contains the following statements.

```dbgcmd
.if (@r9 != 0) { as /mu ${/v:EventName} @r9 } .else { ad /q ${/v:EventName} }
.if ($spat(@"${EventName}", "Global*") == 0)  { gc } .else { .echo EventName }
```

The *lpName* argument passed to the **CreateEventW** function is the fourth argument, so it is stored in the r9 register (x64 processor). The script performs the following steps:

1.  If *lpName* is not NULL, use [**as**](as--as--set-alias-.md) and [**${}**](-------alias-interpreter-.md) to create an alias named EventName. Assign to EventName the null-terminated Unicode string beginning at the address pointed to by *lpName*. On the other hand, if *lpName* is NULL, use [**ad**](ad--delete-alias-.md) to delete any existing alias named EventName.

2.  Use [**$spat**](masm-numbers-and-operators.md) to compare the string represented by EventName to the pattern "Global\*". If the string does not match the pattern, use [**gc**](gc--go-from-conditional-breakpoint-.md) to continue without breaking. If the string does match the pattern, break and display the string represented by EventName.

**Note**  [**$spat**](masm-numbers-and-operators.md) performs a case-insensitive match.

**Note**  The ampersand ( @ ) character in $spat(@"${EventName}" specifies that the string represented by EventName is to be interpreted literally; that is, a backslash ( \\ ) is treated as a backslash rather than an escape character.

### <span id="conditional_breakpoints_and_register_sign_extension"></span><span id="CONDITIONAL_BREAKPOINTS_AND_REGISTER_SIGN_EXTENSION"></span>Conditional Breakpoints and Register Sign Extension

You can set a breakpoint that is conditional on a register value.

The following command will break at the beginning of the **myFunction** function if the **eax** register is equal to 0xA3:

```dbgcmd
0:000> bp mydriver!myFunction "j @eax = 0xa3  '';'gc'" 
0:000> bp mydriver!myFunction ".if @eax = 0xa3  {} .else {gc}"
```

However, the following similar command will not necessarily break when **eax** equals 0xC0004321:

```dbgcmd
0:000> bp mydriver!myFunction "j @eax = 0xc0004321  '';'gc'" 
0:000> bp mydriver!myFunction ".if @eax = 0xc0004321  {} .else {gc}"
```

The reason the preceding command will fail is that the MASM expression evaluator sign-extends registers whose high bit equals one. When **eax** has the value 0xC0004321, it will be treated as 0xFFFFFFFF\`C0004321 in computations--even though **eax** will still be displayed as 0xC0004321. However, the numeral **0xc0004321** is sign-extended in kernel mode, but not in user mode. Therefore, the preceding command will not work properly in user mode. If you mask the high bits of **eax**, the command will work properly in kernel mode--but now it will fail in user mode.

You should formulate your commands defensively against sign extension in both modes. In the preceding command, you can make the command defensive by masking the high bits of a 32-bit register by using an AND operation to combine it with 0x00000000\`FFFFFFFF and by masking the high bits of a numeric constant by including a grave accent ( **\`** ) in its syntax.

The following command will work properly in user mode and kernel mode:

```dbgcmd
0:000> bp mydriver!myFunction "j (@eax & 0x0`ffffffff) = 0x0`c0004321  '';'gc'" 
0:000> bp mydriver!myFunction ".if (@eax & 0x0`ffffffff) = 0x0`c0004321  {} .else {gc}"
```

For more information about which numbers are sign-extended by the debugger, see [Sign Extension](sign-extension.md).

### <span id="conditional_breakpoints_in_windbg"></span><span id="CONDITIONAL_BREAKPOINTS_IN_WINDBG"></span>Conditional Breakpoints in WinDbg

In WinDbg, you can create a conditional breakpoint by clicking [Breakpoints](edit---breakpoints.md) from the **Edit** menu, entering a new breakpoint address into the **Command** box, and entering a condition into the **Condition** box.

For example, typing **mymod!myFunc+0x3A** into the **Command** box and **myVar &lt; 7** into the **Condition** box is equivalent to issuing the following command:

```dbgcmd
0:000> bu mymod!myFunc+0x3A "j(myVar<7) '.echo "Breakpoint hit, condition myVar<7"'; 'gc'" 
0:000> bu mymod!myFunc+0x3A ".if(myVar<7) {.echo "Breakpoint hit, condition myVar<7"} .else {gc}" 
```

### <span id="restrictions_on_conditional_breakpoints"></span><span id="RESTRICTIONS_ON_CONDITIONAL_BREAKPOINTS"></span>Restrictions on Conditional Breakpoints

If you are [controlling the user-mode debugger from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md), you cannot use conditional breakpoints or any other breakpoint command string that contains the [**gc (Go from Conditional Breakpoint)**](gc--go-from-conditional-breakpoint-.md) or [**g (Go)**](g--go-.md) commands. If you use these commands, the serial interface might not be able to keep up with the number of breakpoint passes, and you will be unable to break back into CDB.

 

 





