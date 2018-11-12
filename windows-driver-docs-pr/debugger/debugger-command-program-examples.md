---
title: Debugger Command Program Examples
description: Debugger Command Program Examples
ms.assetid: da756906-6243-4cb9-b4e5-5b0b4540533d
keywords: ["debugger command program, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugger Command Program Examples


## <span id="ddk_debugger_command_program_examples_dbg"></span><span id="DDK_DEBUGGER_COMMAND_PROGRAM_EXAMPLES_DBG"></span>


The following sections describe debugger command programs.

### <span id="using_the__foreach_token"></span><span id="USING_THE__FOREACH_TOKEN"></span>Using the .foreach Token

The following example uses the [**.foreach**](-foreach.md) token to search for WORD values of 5a4d. For each 5a4d value that is found, the debugger displays 8 DWORD values, starting at the address of where the 5a4d DWORD was found.

```dbgcmd
0:000> .foreach (place { s-[1]w 77000000 L?4000000 5a4d }) { dc place L8 } 
```

The following example uses the [**.foreach**](-foreach.md) token to search for WORD values of 5a4d. For each 5a4d value that is found, the debugger displays 8 DWORD values, starting 4 bytes prior to the address where the 5a4d DWORD was found.

```dbgcmd
0:000> .foreach (place { s-[1]w 77000000 L?4000000 5a4d }) { dc place -0x4 L8 } 
```

The following example displays the same values.

```dbgcmd
0:000> .foreach (place { s-[1]w 77000000 L?4000000 5a4d }) { dc ( place -0x4 ) L8 } 
```

**Note**  If you want to operate on the variable name in the *OutCommands* portion of the command, you must add a space after the variable name. For example, in the preceeding example, there is a space between the variable *place* and the subtraction operator.

 

The **-\[1\]** option together with the [**s (Search Memory)**](s--search-memory-.md) command causes its output to include only the addresses it finds, not the values that are found at those addresses.

The following command displays verbose module information for all modules that are located in the memory range from 0x77000000 through 0x7F000000.

```dbgcmd
0:000> .foreach (place { lm1m }) { .if ((${place} >= 0x77000000) & (${place} <= 0x7f000000)) { lmva place } } 
```

The **1m** option together with the [**lm (List Loaded Modules)**](lm--list-loaded-modules-.md) command causes its output to include only the addresses of the modules, not the full description of the modules.

The preceding example uses the [**${ } (Alias Interpreter)**](-------alias-interpreter-.md) token to make sure aliases are replaced even if they are next to other text. If the command did not include this token, the opening parenthesis that is next to **place** prevents alias replacement. Note that the **${}** token works on the variables that are used in **.foreach** and on true aliases.

### <span id="walking_the_process_list"></span><span id="WALKING_THE_PROCESS_LIST"></span>Walking the Process List

The following example walks through the kernel-mode process list and displays the executable name for each entry in the list.

This example should be stored as a text file and executed with the [**$$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) command. This command loads the whole file, replaces all carriage returns with semicolons, and executes the resulting block. This command enables you to write readable programs by using multiple lines and indentation, instead of having to squeeze the whole program onto a single line.

This example illustrates the following features:

-   The **$t0**, **$t1**, and **$t2** pseudo-registers are used as variables in this program. The program also uses aliases named **Procc** and **$ImageName**.

-   This program uses the MASM expression evaluator. However, the **@@c++( )** token appears one time. This token causes the program to use the C++ expression evaluator to parse the expression within the parentheses. This usage enables the program to use the C++ structure tokens directly.

-   The **?** flag is used with the [**r (Registers)**](r--registers-.md) command. This flag assigns typed values to the pseudo-register **$t2**.

```dbgcmd
$$  Get process list LIST_ENTRY in $t0.
r $t0 = nt!PsActiveProcessHead

$$  Iterate over all processes in list.
.for (r $t1 = poi(@$t0);
      (@$t1 != 0) & (@$t1 != @$t0);
      r $t1 = poi(@$t1))
{
    r? $t2 = #CONTAINING_RECORD(@$t1, nt!_EPROCESS, ActiveProcessLinks);
    as /x Procc @$t2

 $$  Get image name into $ImageName.
 as /ma $ImageName @@c++(&@$t2->ImageFileName[0])

 .block
    {
        .echo ${$ImageName} at ${Procc}
    }

    ad $ImageName
    ad Procc
}
```

### <span id="walking_the_ldr_data_table_entry_list"></span><span id="WALKING_THE_LDR_DATA_TABLE_ENTRY_LIST"></span>Walking the LDR\_DATA\_TABLE\_ENTRY List

The following example walks through the user-mode LDR\_DATA\_TABLE\_ENTRY list and displays the base address and full path of each list entry.

Like the preceding example, this program should be saved in a file and executed with the [**$$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) command.

This example illustrates the following features:

- This program uses the MASM expression evaluator. However, in two places, the **@@c++( )** token appears. This token causes the program to use the C++ expression evaluator to parse the expression within the parentheses. This usage enables the program to use C++ structure tokens directly.

- The **?** flag is used with the [**r (Registers)**](r--registers-.md) command. This flag assigns typed values to the pseudo-registers **$t0** and **$t1**. In the body of the loop, **$t1** has the type **ntdll!\_LDR\_DATA\_TABLE\_ENTRY\\***, so the program can make direct member references.

- The user-named aliases **$Base** and **$Mod** are used in this program. The dollar signs reduce the possibility that these aliases have been used previously in the current debugger session. The dollar signs are not necessary. The [**${/v: }**](-------alias-interpreter-.md) token interprets the alias literally, preventing it from being replaced if it was defined before the script is run. You can also use this token together with any block to prevent alias definitions before the block from being used.

- The [**.block**](-block.md) token is used to add an extra alias replacement step. Alias replacement occurs one time for the whole script when it is loaded and one time when each block is entered. Without the **.block** token and its braces, the **.echo** command does not receive the values of the **$Mod** and **$Base** aliases that are assigned in the previous lines.

```dbgcmd
$$ Get module list LIST_ENTRY in $t0.
r? $t0 = &@$peb->Ldr->InLoadOrderModuleList
 
$$ Iterate over all modules in list.
.for (r? $t1 = *(ntdll!_LDR_DATA_TABLE_ENTRY**)@$t0;
 (@$t1 != 0) & (@$t1 != @$t0);
      r? $t1 = (ntdll!_LDR_DATA_TABLE_ENTRY*)@$t1->InLoadOrderLinks.Flink)
{
    $$ Get base address in $Base.
 as /x ${/v:$Base} @@c++(@$t1->DllBase)
 
 $$ Get full name into $Mod.
 as /msu ${/v:$Mod} @@c++(&@$t1->FullDllName)
 
 .block
    {
        .echo ${$Mod} at ${$Base}
    }
 
    ad ${/v:$Base}
    ad ${/v:$Mod}
}
```

 

 





