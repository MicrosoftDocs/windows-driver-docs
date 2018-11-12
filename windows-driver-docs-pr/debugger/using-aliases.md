---
title: Using Aliases
description: Using Aliases
ms.assetid: ee0540d0-5bfd-47ef-92b1-ec1d6954aec7
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Using Aliases


## <span id="ddk_using_aliases_dbg"></span><span id="DDK_USING_ALIASES_DBG"></span>


*Aliases* are character strings that are automatically replaced with other character strings. You can use them in debugger commands and to avoid retyping certain common phrases.

An alias consists of an *alias name* and an *alias equivalent*. When you use an alias name as part of a debugger command, the name is automatically replaced by the alias equivalent. This replacement occurs immediately, before the command is parsed or executed.

The debugger supports three kinds of aliases:

-   You can set and name *user-named aliases*.

-   You can set *fixed-name aliases*, but they are named **$u0**, **$u1**, ..., **$u9**.

-   The debugger sets and names *automatic aliases*.

### <span id="defining_a_user_named_alias"></span><span id="DEFINING_A_USER_NAMED_ALIAS"></span>Defining a User-Named Alias

When you define a user-named alias, you can choose the alias name and the alias equivalent:

-   The alias name can be any string that does not contain white space.

-   The alias equivalent can be any string. If you enter it at the keyboard, the alias equivalent cannot contain leading spaces or carriage returns. Alternatively, you can set it equal to a string in memory, the value of a numeric expression, the contents of a file, the value of an environment variable, or the output of one or more debugger commands.

Both the alias name and the alias equivalent are case sensitive.

To define or redefine a user-named alias, use the [**as (Set Alias)**](as--as--set-alias-.md) or **aS (Set Alias)** command.

To remove an alias, use the [**ad (Delete Alias)**](ad--delete-alias-.md) command.

To list all current user-named aliases, use the [**al (List Aliases)**](al--list-aliases-.md) command.

### <span id="defining_a_fixed_name_alias"></span><span id="DEFINING_A_FIXED_NAME_ALIAS"></span>Defining a Fixed-Name Alias

There are 10 fixed-name aliases. Their alias names are **$u0**, **$u1**, ..., **$u9**. Their alias equivalents can be any string that does not contain the ENTER keystroke.

Use the [**r (Registers)**](r--registers-.md) command to define the alias equivalents for fixed-name aliases. When you define a fixed-name alias, you must insert a period (**.**) before the letter "u". The text after the equal sign (=) is the alias equivalent. The alias equivalent can include spaces or semicolons, but leading and trailing spaces are ignored. You should not enclose the alias equivalent in quotation marks (unless you want quotation marks in the results).

**Note**   Do not be confused by using the **r (Registers)** command for fixed-name aliases. These aliases are not registers or pseudo-registers, even though you use the **r** command to set their alias equivalents. You do not have to add an at (**@**) sign before these aliases, and you cannot use the **r** command to *display* the value of one of these aliases.

 

By default, if you do not define a fixed-name alias, it is an empty string.

### <span id="automatic_aliases"></span><span id="AUTOMATIC_ALIASES"></span>Automatic Aliases

The debugger sets the following automatic aliases.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Alias name</th>
<th align="left">Alias equivalent</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>$ntnsym</strong></p></td>
<td align="left"><p>The most appropriate module for NT symbols on the computer&#39;s native architecture. This alias can equal either <strong>ntdll</strong> or <strong>nt</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$ntwsym</strong></p></td>
<td align="left"><p>The most appropriate module for NT symbols during 32-bit debugging that uses WOW64. This alias could be <strong>ntdll32</strong> or some other 32-bit version of Ntdll.dll.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$ntsym</strong></p></td>
<td align="left"><p>The most appropriate module for NT symbols that match the current machine mode. When you are debugging in native mode, this alias is the same as <strong>$ntnsym</strong>. When you are debugging in a non-native mode, the debugger tries to find a module that matches this mode. (For example, during 32-bit debugging that uses WOW64, this alias is the same as <strong>$ntwsym</strong>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$CurrentDumpFile</strong></p></td>
<td align="left"><p>The name of the last dump file that the debugger loaded.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$CurrentDumpPath</strong></p></td>
<td align="left"><p>The directory path of the last dump file that the debugger loaded.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$CurrentDumpArchiveFile</strong></p></td>
<td align="left"><p>The name of the last dump archive file (CAB file) that the debugger loaded.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$CurrentDumpArchivePath</strong></p></td>
<td align="left"><p>The directory path of the last dump archive file (CAB file) that the debugger loaded.</p></td>
</tr>
</tbody>
</table>

 

Automatic aliases are similar to [automatic pseudo-registers](pseudo-register-syntax.md), except that you can use automatic aliases with alias-related tokens (such as **${ }**), while you cannot use pseudo-registers with these tokens.

### <span id="using_an_alias_in_the_debugger_command_window"></span><span id="USING_AN_ALIAS_IN_THE_DEBUGGER_COMMAND_WINDOW"></span>Using an Alias in the Debugger Command Window

After you define an alias, you can use it in any command entry. The alias name is automatically replaced with the alias equivalent. Therefore, you can use the alias as an expression or as a macro.

An alias name expands correctly even if it is enclosed in quotation marks. Because the alias equivalent can include any number of quotation marks or semicolons, the alias equivalent can represent multiple commands.

A user-named alias is recognized only if its name is separated from other characters by white space. The first character of its alias name must begin the line or follow a space, a semicolon, or a quotation mark. The last character of its alias name must end the line or be followed by a space, a semicolon, or a quotation mark.

**Note**   Any text that you enter into the [Debugger Command window](debugger-command-window.md) that begins with "as", "aS", "ad", or "al" does not receive alias replacement. This restriction prevents the alias commands from being rendered inoperable. However, this restriction also means that commands that follow **ad** or **al** on a line do not have their aliases replaced. If you want aliases to be replaced in a line that begins with one of these strings, add a semicolon before the alias.

 

However, you can use the **${ }** token to expand a user-named alias even when it is next to other text. You can also use this token together with certain switches to prevent an alias from being expanded or to display certain alias-related values. For more information about these situations, see [**${ } (Alias Interpreter)**](-------alias-interpreter-.md).

A fixed-name alias expands correctly from any point within a line, regardless of how it is embedded within the text of the line.

You cannot use commands that are available only in WinDbg ([**.open**](-open--open-source-file-.md), [**.write\_cmd\_hist (Write Command History)**](-write-cmd-hist--write-command-history-.md), [**.lsrcpath**](-srcpath---lsrcpath--set-source-path-.md), and [**.lsrcfix**](-srcfix---lsrcfix--use-source-server-.md)) and a few additional commands ([**.hh**](-hh--open-html-help-file-.md), [**.cls**](-cls--clear-screen-.md), [**.wtitle**](-wtitle--set-window-title-.md), [**.remote**](-remote--create-remote-exe-server-.md), kernel-mode [**.restart**](-restart--restart-kernel-connection-.md), and user-mode [**.restart**](-restart--restart-target-application-.md)) with aliases.

### <span id="using_an_alias_in_a_script_file"></span><span id="USING_AN_ALIAS_IN_A_SCRIPT_FILE"></span>Using an Alias in a Script File

When you use an alias in a script file, you must take special care to make sure that the alias is expanded at the correct time. Consider the following script:

```text
.foreach (value {dd 610000 L4})
{
   as /x ${/v:myAlias} value + 1
   .echo value myAlias
}

ad myAlias
```

The first time through the loop, the [**as, aS (Set Alias)**](as--as--set-alias-.md) command assigns a value to the myAlias. The value assigned to myAlias is 1 plus 610000 (the first output of the dd command). However, when the [**.echo (Echo Comment)**](-echo--echo-comment-.md) command is executed, myAlias has not yet been expanded, so instead of seeing 610001, we see the text "myAlias".

```dbgcmd
0:001> $$>< c:\Script02.txt
00610000 myAlias
00905a4d 0x610001
00000003 0x905a4e
00000004 0x4
0000ffff 0x5
```

The problem is that myAlias is not expanded until a new block of code is entered. The next entry to the loop is a new block, so myAlias gets expanded to 610001. But it is too late: we should have seen 610001 the first time through the loop, not the second time.We can fix this problem by enclosing the [**.echo (Echo Comment)**](-echo--echo-comment-.md) command in a new block as shown in the following script.

```text
.foreach (value {dd 610000 L4}) 
{
   as /x ${/v:myAlias} value + 1
   .block{.echo value myAlias}
}

ad myAlias
```

With the altered script, we get the following correct output.

```dbgcmd
0:001> $$>< c:\Script01.txt
00610000 0x610001
00905a4d 0x905a4e
00000003 0x4
00000004 0x5
0000ffff 0x10000
```

For more information, see [**.block**](-block.md) and [**${ } (Alias Interpreter)**](-------alias-interpreter-.md).

### <span id="Using_a_.foreach_Token_in_an_Alias"></span><span id="using_a_.foreach_token_in_an_alias"></span><span id="USING_A_.FOREACH_TOKEN_IN_AN_ALIAS"></span>Using a .foreach Token in an Alias

When you use a [**.foreach**](-foreach.md) token in the definition of an alias, you must take special care to ensure that the token is expanded. Consider the following sequence of commands.

```dbgcmd
r $t0 = 5
ad myAlias
.foreach /pS 2 /ps 2 (Token {?@$t0}) {as myAlias Token}
al
```

The first command sets the value of the **$t0** pseudo register to 5. The second command deletes any value that might have been previously assigned to myAlias. The third command takes the third token of the **?@$t0** command and attempts to assign the value of that token to myAlias. The fourth command lists all aliases and their values. We would expect the value of myAlias to be 5, but instead the value is the word "Token".

```dbgcmd
   Alias            Value  
 -------          ------- 
 myAlias          Token 
```

The problem is that the [**as**](as--as--set-alias-.md) command is at the beginning of the line in the body of the [**.foreach**](-foreach.md) loop. When a line begins with an **as** command, aliases and tokens in that line are not expanded. If we put a semicolon or blank space before the **as** command, then any alias or token that already has a value is expanded. In this example, myAlias is not expanded because it does not already have a value. Token is expanded because it has a value of 5. Here is the same sequence of commands with the addition of a semicolon before the **as** command.

```dbgcmd
r $t0 = 5
ad myAlias
.foreach /pS 2 /ps 2 (Token {?@$t0}) {;as myAlias Token}
al
```

Now we get the expected output.

```dbgcmd
  Alias            Value  
 -------          ------- 
 myAlias          5 
```

### <span id="recursive_aliases"></span><span id="RECURSIVE_ALIASES"></span>Recursive Aliases

You can use a fixed-name alias in the definition of any alias. You can also use a user-named alias in the definition of a fixed-name alias. However, to use a user-named alias in the definition of another user-named alias, you have to add a semicolon before the **as** or **aS** command, or else the alias replacement does not occur on that line.

When you are using recursive definitions of this type, each alias is translated as soon as it is used. For example, the following example displays **3**, not **7**.

```dbgcmd
0:000> r $.u2=2 
0:000> r $.u1=1+$u2 
0:000> r $.u2=6 
0:000> ? $u1 
Evaluate expression: 3 = 00000003
```

Similarly, the following example displays **3**, not **7**.

```dbgcmd
0:000> as fred 2 
0:000> r $.u1= 1 + fred 
0:000> as fred 6 
0:000> ? $u1 
Evaluate expression: 3 = 00000003
```

The following example is also permitted and displays **9**.

```dbgcmd
0:000> r $.u0=2 
0:000> r $.u0=7+$u0 
0:000> ? $u0
Evaluate expression: 9 = 00000009
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

You can use aliases so that you do not have to type long or complex symbol names, as in the following example.

```dbgcmd
0:000> as Short usersrv!NameTooLongToWantToType
0:000> dw Short +8
```

The following example is similar to the preceding example but it uses a fixed-name alias.

```dbgcmd
0:000> r $.u0=usersrv!NameTooLongToWantToType
0:000> dw $u0+8
```

You can use aliases as macros for commands that you use frequently. The following example increments the **eax** and **ebx** registers two times.

```dbgcmd
0:000> as GoUp r eax=eax+1; r ebx=ebx+1
0:000> GoUp
0:000> GoUp
```

The following example uses an alias to simplify typing of commands.

```dbgcmd
0:000> as Cmd "dd esp 14; g"
0:000> bp MyApi Cmd 
```

The following example is similar to the preceding example but it uses a fixed-name alias.

```dbgcmd
0:000> r $.u5="dd esp 14; g"
0:000> bp MyApi $u5 
```

Both of the preceding examples are equivalent to the following command.

```dbgcmd
0:000> bp MyApi "dd esp 14; g"
```

### <span id="tools_ini_file"></span><span id="TOOLS_INI_FILE"></span> Tools.ini File

In CDB (and NTSD), you can predefine fixed-name aliases in the [tools.ini](configuring-tools-ini.md) file. To predefine a fixed-name alias, add the **$u** fields that you want to your \[NTSD\] entry, as in the following example.

```ini
[NTSD]
$u1:_ntdll!_RtlRaiseException
$u2:"dd esp 14;g"
$u9:$u1 + 42
```

You cannot set user-named aliases in the Tools.ini file.

### <span id="fixed_name_aliases_vs__user_named_aliases"></span><span id="FIXED_NAME_ALIASES_VS__USER_NAMED_ALIASES"></span>Fixed-Name Aliases vs. User-Named Aliases

User-name aliases are easier to use than fixed-named aliases. Their definition syntax is simpler, and you can list them by using the [**al (List Aliases)**](al--list-aliases-.md) command.

Fixed-named aliases are replaced if they are used next to other text. To make a user-named alias be replaced when it is next to other text, enclose it in the [**${ } (Alias Interpreter)**](-------alias-interpreter-.md) token.

Fixed-name alias replacement occurs before user-named alias replacement.

 

 





