---
title: Parsing Extension Arguments
description: Parsing Extension Arguments
ms.assetid: 3c75fb75-50d0-48e4-abf4-e4dba9a080f9
keywords: ["EngExtCpp extensions, parsing arguments"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Parsing Extension Arguments


The EngExtCpp extension framework provides methods to aid in parsing the command-line arguments passed to an extension. To take advantage of these methods, the extension must first declare the format of the command-line arguments in the [**EXT\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff544514) macro.

To bypass the command-line argument parsing done by the framework and let the extension itself parse the arguments, set the command-line description to `"{{custom}}"` and use the method [**GetRawArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff548226) to get the command-line arguments for parsing.

Command-line description strings will automatically be wrapped when printed, to fit the column width of the display. However, newline characters can be embedded in the description strings - using '`\n`' - to start new lines.

The command-line description can be **NULL** or the empty string. If either occurs, it indicates that the extension command does not take any arguments.

### <span id="command_line_description"></span><span id="COMMAND_LINE_DESCRIPTION"></span>Command-Line Description

The description of the command-line arguments is a sequence that contains two types of components: directives and arguments. The description can optionally contain one of each directive and can contain up to 64 arguments.

### <span id="directives"></span><span id="DIRECTIVES"></span>Directives

Directives specify how the arguments are parsed. They are enclosed by double braces (`'{{'` and `'}}'`). Each directive can optionally appear zero or one times in the string that describes the arguments.

The following directives are available:

<span id="custom"></span><span id="CUSTOM"></span>`custom`  
Turns off the parsing done by the extension framework and lets the extension perform its own parsing.

<span id="l_str"></span><span id="L_STR"></span>`l:str`  
Overrides the default long description of the command-line arguments. The extension framework will use *str* for the full description of all the arguments.

<span id="opt_str"></span><span id="OPT_STR"></span>`opt:str`  
Overrides the default prefix characters for named commands. The default value is `"/-"`, allowing '`/`' or '`-`' to be used as the prefix that identifies named arguments.

<span id="s_str"></span><span id="S_STR"></span>`s:str`  
Overrides the default short description of the command-line arguments. The extension framework will use *str* for the short description of all the arguments.

Here are some examples of directives. The following string is used by an extension command that parses its own arguments. It also provides short and long descriptions for use with the automatic **!help** extension command:

```dbgcmd
{{custom}}{{s:<arg1> <arg2>}}{{l:arg1 - Argument 1\narg2 - Argument 2}}
```

The following string changes the argument option prefix characters to '`/`' or '`-`'. With this directive, the arguments will be specified using '`+arg`' and '`:arg`' instead of '`/arg`' and '`-arg`':

```dbgcmd
{{opt:+:}}
```

### <span id="arguments"></span><span id="ARGUMENTS"></span>Arguments

Arguments can be of two types: named and unnamed. Unnamed arguments are read positionally. Both types of argument also have a display name, used by the help command.

Argument descriptions are enclosed by single braces (`'{'` and `'}'`).

Each argument description has the following syntax:

```dbgcmd
{[optname];[type[,flags]];[argname];[argdesc]}
```

where:

<span id="optname"></span><span id="OPTNAME"></span>*optname*  
The name of the argument. This is the name used in commands and in methods that fetch arguments by name. This name is optional. If it is present, the argument becomes a "named argument"; it can appear anywhere on the command-line and is referenced by name. If it is not present, the argument becomes an "unnamed argument"; its position on the command-line is important and it is referenced by its position relative to the other unnamed arguments.

<span id="type"></span><span id="TYPE"></span>*type*  
The type of the argument. This affects how the argument is parsed and how it is retrieved. The *type* parameter can have one of the following values:

<span id="b"></span><span id="B"></span>b  
Boolean type. The argument is either present or not present. Named Boolean arguments can be retrieved using [**HasArg**](https://msdn.microsoft.com/library/windows/hardware/ff549721).

<span id="e_d__s__bits_"></span><span id="E_D__S__BITS_"></span>e\[d\]\[s\]\[bits\]  
Expression type. The argument has a numeric value. Named expression arguments can be retrieved using [**GetArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff545596) and unnamed expression arguments can be retrieved using [**GetUnnamedArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff549465).

<span id="d"></span><span id="D"></span>d  
The expression is limited to the next space character in the argument string. If this is not present, the expression evaluator will consume characters from the command line until it determines that it reached the end of the expression.

<span id="s"></span><span id="S"></span>s  
The value of the expression is signed. Otherwise, the value of the expression is unsigned.

<span id="bits"></span><span id="BITS"></span>bits  
The number of bits in the value of the argument. The maximum value for *bits* is 64.

<span id="s"></span><span id="S"></span>s  
String type. The string is limited to the next space character. Named string arguments can be retrieved using [**GetArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff545586) and unnamed string arguments can be retrieved using [**GetUnnamedArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff549464).

<span id="x"></span><span id="X"></span>x  
String type. The argument is the rest of the command line. The argument is retrieved using **GetArgStr** or **GetUnnamedArgStr**, as with the s string type.

<span id="flags"></span><span id="FLAGS"></span>*flags*  
The argument flags. These determine how the argument will be treated by the parser. The *flags* parameter can have one of the following values:

<span id="d_expr"></span><span id="D_EXPR"></span>d=expr  
The default value of the argument. If the argument is not present on the command line, then the argument is set to *expr*. The default value is a string that is parsed according to the type of the argument.

<span id="ds"></span><span id="DS"></span>ds  
The default value will not be displayed in the argument description provided by the help.

<span id="o"></span><span id="O"></span>o  
The argument is optional. This is the default for named arguments.

<span id="r"></span><span id="R"></span>r  
The argument is required. This is the default for unnamed arguments.

<span id="argname"></span><span id="ARGNAME"></span>*argname*  
The display name of the argument. This is the name used by the automatic **!help** extension command and by the automatic **/?** or **-?** command-line arguments. Used when printing a summary of the command-line options.

<span id="argdesc"></span><span id="ARGDESC"></span>*argdesc*  
A description of the argument. This is the description printed by the automatic **!help** extension and by the automatic "**/?**" or "**-?**" command-line arguments.

Here are some examples of argument descriptions. The following expression defines a command which takes a single optional expression argument. The argument must fit in 32 bits. If the argument isn't present on the command line, the default value of 0x100 will be used.

```dbgcmd
{;e32,o,d=0x100;flags;Flags to control command}
```

The following expression defines a command with an optional Boolean "**/v**" argument and a required unnamed string argument.

```dbgcmd
{v;b;;Verbose mode}{;s;name;Name of object}
```

The following expression defines a command that has an optional named expression argument **/oname** *expr* and an optional named string argument **/eol** *str*. If **/eol** is present, its value will be set to the remainder of the command line and no further arguments will be parsed.

```dbgcmd
{oname;e;expr;Address of object}{eol;x;str;Commands to use}
```

### <span id="command_line"></span><span id="COMMAND_LINE"></span>Command Line

The following is a list of some ways that arguments are parsed on the command line:

-   The values of named expression and string arguments follow the name on the command line. For example, **/name** *expr* or **/name** *str*.

-   For named Boolean arguments, the value is true if the name appears on the command line; false otherwise.

-   Multiple single-character-named Boolean options can be grouped together on the command line. For example, "/a /b /c" can be written using the shorthand notation "/abc" (unless there is already an argument named "abc").

-   If the command line contains the named argument "?" - for example, "/?" and "-?" - the argument parsing ends, and the help text for the extension is displayed.

### <span id="parsing_internals"></span><span id="PARSING_INTERNALS"></span>Parsing Internals

Several methods are used by the argument parser to set arguments.

The method [**SetUnnamedArg**](https://msdn.microsoft.com/library/windows/hardware/ff556876) will change the value of an unnamed argument. And, for convenience, the methods [**SetUnnamedArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff556878) and [**SetUnnamedArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff556879) will set unnamed string and expression arguments respectively.

Similar methods exist for named arguments. [**SetArg**](https://msdn.microsoft.com/library/windows/hardware/ff556614) is used to change the value of any named argument and [**SetArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff556618) and [**SetArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff556622) are used for named string and expression arguments respectively.

 

 





