---
title: Specifying Module and Function Owners
description: Specifying Module and Function Owners
ms.assetid: be227712-7f70-4e74-b090-ca8b3ecd1e13
keywords: ["executable files and paths, specifying module owner", "function owners", "owners of modules and functions", "triage.ini file", "triage.ini file, syntax", "analyze extension, triage.ini file"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Specifying Module and Function Owners


## <span id="ddk_specifying_module_and_function_owners_dbg"></span><span id="DDK_SPECIFYING_MODULE_AND_FUNCTION_OWNERS_DBG"></span>


The **!analyze** and **!owner** extensions use a file that is named Triage.ini to determine the owner of the symbols that the debugger encounters.

When you use these extensions, the identities of the function or module owner are displayed after the word "Followup".

The Triage.ini file is a text file that resides in the \\triage subdirectory of your Debugging Tools for Windows installation. A sample Triage.ini file is included as part of the Debugging Tools for Windows package.

**Warning**   If you install an updated version of Debugging Tools for Windows in the same directory as the current version, it overwrites all of the files in that directory, including Triage.ini. After you modify or replace the sample Triage.ini file, save a copy of it to a different directory. After you reinstall the debuggers, you can copy the saved Triage.ini over the default version.

 

### <span id="format_of_the_triage_ini_file"></span><span id="FORMAT_OF_THE_TRIAGE_INI_FILE"></span>Format of the Triage.ini File

Although the Triage.ini file is intended to help you determine the owner of a function that has broken into the debugger, the "owner" strings in this file can be anything that might help you with debugging. The strings can be names of people who wrote or maintain the code. Or, the strings can be short instructions about what you can do when an error occurs in a module or function.

Each line in this file has the following syntax.

```dbgcmd
Module[!Function]=Owner 
```

You can add an asterisk (\*) only at the end of a module or function name. If it appears elsewhere, it is interpreted as a literal character.

You cannot add spaces in the owner string. If spaces do exist in the owner string, they are ignored.

For more information about syntax options, see Special Triage.ini Syntax.

The following examples shows a sample Triage.ini file.

```ini
module1=Person1
module2!functionA=Person2
module2!functionB=Person3
module2!funct*=Person4
module2!*=Person5
module3!singleFunction=Person6
mod*!functionC=Person7
```

### <span id="triage_ini_and__owner"></span><span id="TRIAGE_INI_AND__OWNER"></span> Triage.ini and !owner

When you pass a module or function name to the [**!owner**](-owner.md) extension, the debugger displays the word "Followup" followed by the name of the module or function's owner.

The following example uses the previous sample Triage.ini file.

```dbgcmd
0:000> !owner module2!functionB
Followup:  Person3
```

According to the file, "Person3" owns **module2!functionB**, and "Person4" owns **module2!funct\\**<em>. Both of these strings match the argument that is passed to **!owner</em>*, so the more complete match is used.

### <span id="triage_ini_and__analyze"></span><span id="TRIAGE_INI_AND__ANALYZE"></span> Triage.ini and !analyze

When you use the [**!analyze**](-analyze.md) extension, the debugger looks at the top faulting frame in the stack and tries to determine the owner of the module and function in this frame. If the debugger can determine the owner, the owner information is displayed.

If the debugger cannot determine the owner, the debugger passes to the next stack frame, and so on, until the debugger determines the owner or the stack is completely examined.

If the debugger can determine the owner, the owner name is displayed after the word "Followup". If the debugger searches the whole stack without finding any information, no name is displayed.

The following example uses the sample Triage.ini file that is given earlier in this topic.

Suppose the first frame on the stack is **MyModule!someFunction**. The debugger does not find **MyModule** in the Triage.ini file. Next, it continues to the second frame on the stack.

Suppose the second frame is **module3!anotherFunction**. The debugger does see an entry for **module3**, but there is no match for **anotherFunction** in this module. Next, the debugger continues to the third frame.

Suppose the third frame is **module2!functionC**. The debugger first looks for an exact match, but such a match does not exist. The debugger then trims the function name and discovers **module2!funct\\*** in Triage.ini. This match ends the search, because the debugger determines that the owner is "Person4".

The debugger then displays output that is similar to the following example.

```dbgcmd
0:000> !analyze
*******************************************************************************
*                                                                             *
*                        Exception Analysis                                   *
*                                                                             *
*******************************************************************************

Use !analyze -v to get detailed debugging information.

Probably caused by : module2 ( module2!functionC+15a )

Followup: Person4
---------
```

A more complete match takes precedence over a shorter match. However, a module name match is always preferred to a function name match. If **module2!funct\\*** had not been in this Triage.ini file, the debugger would have selected **module2!\\*** as the match. And if both **module2!funct\\*** and **module2!\\*** were removed, **mod\*!functionC** would have been selected.

### <span id="special_triage_ini_syntax"></span><span id="SPECIAL_TRIAGE_INI_SYNTAX"></span>Special Triage.ini Syntax

If you omit the exclamation point and function name or add **!\\*** after a module name, all functions in that module are indicated. If a function within this module is also specified separately, the more precise specification takes precedence.

If you use "default" as a module name or a function name, it is equivalent to a wildcard character. For example, **nt!\\*** is the same as **nt!default**, and **default** is the same as **\*!\\***.

If a match is made, but the word **ignore** appears to the right of the equal sign (=), the debugger continues to the next frame in the stack.

You can add **last\_** or **maybe\_** before an owner's name. This prefix gives the owner less priority when you run **!analyze**. The debugger chooses a definite match that is lower on the stack over a **maybe\_** match that is higher on the stack. The debugger also chooses a **maybe\_** match that is lower on the stack over a **last\_** match that is higher on the stack.

### <span id="sample_triage_ini"></span><span id="SAMPLE_TRIAGE_INI"></span>Sample Triage.ini

A sample Triage.ini template is included in the Debugging Tools for Windows package. You can add the owners of any modules and functions that you want to this file. If you want to have no global default, delete the **default=MachineOwner** line at the beginning of this file.

 

 





