---
title: as, aS (Set Alias)
description: The as and aS commands define a new alias or redefine an existing one.
ms.assetid: 6e42122b-5a18-403b-a19a-1346bea8da12
keywords: ["as, aS (Set Alias) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- as, aS (Set Alias)
api_type:
- NA
ms.localizationpriority: medium
---

# as, aS (Set Alias)


The **as** and **aS** commands define a new alias or redefine an existing one.

```dbgcmd
as Name EquivalentLine 
aS Name EquivalentPhrase 
aS Name "EquivalentPhrase" 
as /e Name EnvironmentVariable 
as /ma Name Address 
as /mu Name Address 
as /msa Name Address 
as /msu Name Address 
as /x Name Expression 
aS /f Name File 
as /c Name CommandString 
```

## <span id="ddk_cmd_set_alias_dbg"></span><span id="DDK_CMD_SET_ALIAS_DBG"></span>Parameters


<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the alias name. This name can be any text string that does not contain a space or the ENTER keystroke and does not begin with "al", "as", "aS", or "ad". *Name* is case sensitive.

<span id="_______EquivalentLine______"></span><span id="_______equivalentline______"></span><span id="_______EQUIVALENTLINE______"></span> *EquivalentLine*   
Specifies the alias equivalent. *EquivalentLine* is case sensitive. You must add at least one space between *Name* and *EquivalentLine*. The number of spaces between these two parameters is not important. The alias equivalent never contains leading spaces. After these spaces, *EquivalentLine* includes the rest of the line. Semicolons, quotation marks, and spaces are treated as literal characters, and trailing spaces are included.

<span id="_______EquivalentPhrase______"></span><span id="_______equivalentphrase______"></span><span id="_______EQUIVALENTPHRASE______"></span> *EquivalentPhrase*   
Specifies the alias equivalent. *EquivalentPhrase* is case sensitive. You must add at least one space between *Name* and *EquivalentPhrase*. The number of spaces between these two parameters is not important. The alias equivalent never contains leading spaces.

You can enclose *EquivalentPhrase* in quotation marks ("). Regardless of whether you use quotation marks, *EquivalentPhrase* can contain spaces, commas, and single quotation marks ('). If you enclose *EquivalentPhrase* in quotation marks, it can include semicolons, but not additional quotation marks. If you do not enclose *EquivalentPhrase* in quotation marks, it can include quotation marks in any location other than the first character, but it cannot include semicolons. Trailing spaces are included regardless of whether you use quotation marks.

<span id="________e______"></span><span id="________E______"></span> **/e**   
Sets the alias equivalent equal to the environment variable that *EnvironmentVariable* specifies.

<span id="_______EnvironmentVariable______"></span><span id="_______environmentvariable______"></span><span id="_______ENVIRONMENTVARIABLE______"></span> *EnvironmentVariable*   
Specifies the environment variable that is used to determine the alias equivalent. The debugger's environment is used, not the target's. If you started the debugger at a Command Prompt window, the environment variables in that window are used.

<span id="________ma______"></span><span id="________MA______"></span> **/ma**   
Sets the alias equivalent equal to the null-terminated ASCII string that begins at *Address*.

<span id="________mu______"></span><span id="________MU______"></span> **/mu**   
Sets the alias equivalent equal to the null-terminated Unicode string that begins at *Address*.

<span id="________msa______"></span><span id="________MSA______"></span> **/msa**   
Sets the alias equivalent equal to the ANSI\_STRING structure that is located at *Address*.

<span id="________msu______"></span><span id="________MSU______"></span> **/msu**   
Sets the alias equivalent equal to the UNICODE\_STRING structure that is located at *Address*.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the location of the virtual memory that is used to determine the alias equivalent.

<span id="________x______"></span><span id="________X______"></span> **/x**   
Sets the alias equivalent equal to the 64-bit value of *Expression*.

<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the expression to evaluate. This value becomes the alias equivalent. For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="________f______"></span><span id="________F______"></span> **/f**   
Sets the alias equivalent equal to the contents of the *File* file. You should always use the **/f** switch together with **aS**, not with **as**.

<span id="_______File______"></span><span id="_______file______"></span><span id="_______FILE______"></span> *File*   
Specifies the file whose contents become the alias equivalent. *File* can contain spaces, but you should never enclose *File* in quotation marks. If you specify an invalid file, you receive an "Out of memory" error message.

<span id="________c______"></span><span id="________C______"></span> **/c**   
Sets the alias equivalent equal to the output of the commands that *CommandString* specifies. The alias equivalent includes carriage returns if they are present within the command display and a carriage return at the end of the display of each command (even if you specify only one command).

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the commands whose outputs become the alias equivalent. This string can include any number of commands that are separated by semicolons.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to use aliases, see [Using Aliases](using-aliases.md).

Remarks
-------

If you do not use any switches, the **as** command uses the rest of the line as the alias equivalent.

You can end the **aS** command by a semicolon. This technique is useful in a script when you have to put all commands on a single line. Note that if the portion of the line after the semicolon requires expansion of the alias, you must enclose that second portion of the line in a new block. The following example produces the expected output, 0x6.

```dbgcmd
0:001> aS /x myAlias 5 + 1; .block{.echo myAlias}
0x6
```

If you omit the new block, you do not get the expected output. That is because the expansion of a newly set alias does not happen until a new code block is entered. In the following example, the new block is omitted, and the output is the text "myAlias" instead of the expected value 0x6.

```dbgcmd
0:001> aS /x myAlias 5 + 1; .echo myAlias
myAlias
```

For more information about using aliases in scripts, see [Using Aliases](using-aliases.md).

If you use a **/e**, **/ma**, **/mu**, **/msa**, **/msu**, or **/x** switch, the **as** and **aS** commands work the same and the command ends if a semicolon is encountered.

If *Name* is already the name of an existing alias, that alias is redefined.

You can use the **as** or **aS** command to create or change any user-named alias. But you cannot use the command to control a fixed-name alias ($u0 to $u9).

You can use the **/ma**, **/mu**, **/msa**, **/msu**, **/f**, and **/c** switches to create an alias that contains carriage returns. However, you cannot use an alias that contains carriage returns to execute multiple commands in sequence. Instead, you must use semicolons.

 

 





