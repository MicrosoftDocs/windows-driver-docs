---
title: .foreach
description: The .foreach token parses the output of one or more debugger commands and uses each value in this output as the input to one or more additional commands.
ms.assetid: 646c86c2-a436-43d6-b0d8-32dbd423120e
keywords: [".foreach Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .foreach
api_type:
- NA
ms.localizationpriority: medium
---

# .foreach


The **.foreach** token parses the output of one or more debugger commands and uses each value in this output as the input to one or more additional commands.

```dbgcmd
.foreach [Options] ( Variable  { InCommands } ) { OutCommands } 

.foreach [Options] /s ( Variable  "InString" ) { OutCommands } 

.foreach [Options] /f ( Variable  "InFile" ) { OutCommands } 
```

## <span id="ddk_token_foreach_dbg"></span><span id="DDK_TOKEN_FOREACH_DBG"></span>Syntax Elements


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any combination of the following options:

<span id="_pS_InitialSkipNumber"></span><span id="_ps_initialskipnumber"></span><span id="_PS_INITIALSKIPNUMBER"></span>**/pS** *InitialSkipNumber*  
Causes some initial tokens to be skipped. *InitialSkipNumber* specifies the number of output tokens that will not be passed to the specified *OutCommands*.

<span id="_ps_SkipNumber"></span><span id="_ps_skipnumber"></span><span id="_PS_SKIPNUMBER"></span>**/ps** *SkipNumber*  
Causes tokens to be skipped repeatedly each time a command is processed. After each time a token is passed to the specified *OutCommands*, a number of tokens equal to the value of *SkipNumber* will be ignored.

<span id="_______Variable______"></span><span id="_______variable______"></span><span id="_______VARIABLE______"></span> *Variable*   
Specifies a variable name. This variable will be used to hold the output from each command in the *InCommands* string; you can reference *Variable* by name in the parameters passed to the *OutCommands*. Any alphanumeric string can be used, although using a string that can also pass for a valid hexadecimal number or debugger command is not recommended. If the name used for *Variable* happens to match an existing global variable, local variable, or alias, their values will not be affected by the **.foreach** command.

<span id="_______InCommands______"></span><span id="_______incommands______"></span><span id="_______INCOMMANDS______"></span> *InCommands*   
Specifies one or more commands whose output will be parsed; the resulting tokens will be passed to *OutCommands*. The output from *InCommands* is not displayed.

<span id="_______InString______"></span><span id="_______instring______"></span><span id="_______INSTRING______"></span> *InString*   
Used with **/s**. Specifies a string that will be parsed; the resulting tokens will be passed to *OutCommands*.

<span id="_______InFile______"></span><span id="_______infile______"></span><span id="_______INFILE______"></span> *InFile*   
Used with **/f**. Specifies a text file that will be parsed; the resulting tokens will be passed to *OutCommands*. The file name *InFile* must be enclosed in quotation marks.

<span id="_______OutCommands______"></span><span id="_______outcommands______"></span><span id="_______OUTCOMMANDS______"></span> *OutCommands*   
Specifies one or more commands which will be executed for each token. Whenever the *Variable* string occurs it will be replaced by the current token.

**Note**   When the string *Variable* appears within *OutCommands*, it must be surrounded by spaces. If it is adjacent to any other text -- even a parenthesis -- it will not be replaced by the current token value, unless you use the [**${ } (Alias Interpreter)**](-------alias-interpreter-.md) token.

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

Remarks
-------

When the output from *InCommands*, the *InString* string, or the *InFile* file is parsed, any number of spaces, tabs, or carriage returns is treated as a single delimiter. Each of the resulting pieces of text is used to replace *Variable* when it appears within *OutCommands*.

Here is an example of a **.foreach** statement that uses the [**dds**](dds--dps--dqs--display-words-and-symbols-.md) command on each token found in the file *myfile.txt*:

```dbgcmd
0:000> .foreach /f ( place "g:\myfile.txt") { dds place } 
```

The **/pS** and **/ps** flags can be used to pass only certain tokens to the specified *OutCommands*. For example, the following statement will skip the first two tokens in the *myfile.txt* file and then pass the third to [**dds**](dds--dps--dqs--display-words-and-symbols-.md). After each token that is passed, it will skip four tokens. The result is that **dds** will be used with the 3rd, 8th, 13th, 18th, and 23rd tokens, and so on:

```dbgcmd
0:000> .foreach /pS 2 /ps 4 /f ( place "g:\myfile.txt") { dds place } 
```

For more examples that use the **.foreach** token, see [Debugger Command Program Examples](debugger-command-program-examples.md).

 

 





