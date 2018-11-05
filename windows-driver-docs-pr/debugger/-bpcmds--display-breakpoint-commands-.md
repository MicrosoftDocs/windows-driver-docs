---
title: .bpcmds (Display Breakpoint Commands)
description: The .bpcmds command displays the commands that were used to set each of the current breakpoints.
ms.assetid: 96c13c54-8d85-414c-9775-a0373459dc7a
keywords: [".bpcmds (Display Breakpoint Commands) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .bpcmds (Display Breakpoint Commands)
api_type:
- NA
ms.localizationpriority: medium
---

# .bpcmds (Display Breakpoint Commands)


The **.bpcmds** command displays the commands that were used to set each of the current breakpoints.

```dbgcmd
    .bpcmds
```

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, see [Using Breakpoints](using-breakpoints.md).

Remarks
-------

If it is unclear whether a particular breakpoint is set at an address, at a symbolic reference, or at a symbol, use the **.bpcmds** command to shows which breakpoint command was used to create it. The command that was used to create a breakpoint determines its nature:

-   The [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command sets a breakpoint at an address.

-   The [**bu (Set Unresolved Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command sets a breakpoint on a symbolic reference.

-   The [**bm (Set Symbol Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command sets a breakpoint on symbols that match a specified pattern. If the **/d** switch is included, it creates zero or more breakpoints on addresses (like bp), otherwise it creates zero or more breakpoints on symbolic references (like bu).

-   The [**ba (Break on Access)**](ba--break-on-access-.md) command sets a data breakpoint at an address.

The output of **.bpcmds** reflects the current nature of each breakpoint. Each line of the **.bpcmds** display begins with the command used to create it (**bp**, **bu**, or **ba**) followed by the breakpoint ID, and then the location of the breakpoint.

If the breakpoint was created by **ba**, the access type and size are displayed as well.

If the breakpoint was created by **bm** without the **/d** switch, the display indicates the breakpoint type as **bu**, followed by the evaluated symbol enclosed in the **@!""** token (which indicates it is a literal symbol and not a numeric expression or register). If the breakpoint was created by **bm** with the **/d** switch, the display indicates the breakpoint type as **bp**.

Here is an example:

```dbgcmd
0:000> bp notepad!winmain 

0:000> .bpcmds 
bp0 0x00000001`00003340 ;

0:000> bu myprog!winmain 
breakpoint 0 redefined

0:000> .bpcmds 
bu0 notepad!winmain;

0:000> bu myprog!LoadFile 

0:000> bp myprog!LoadFile+10 

0:000> bm myprog!openf* 
  3: 00421200 @!"myprog!openFile"
  4: 00427800 @!"myprog!openFilter"

0:000> bm /d myprog!closef* 
  5: 00421600 @!"myprog!closeFile"

0:000> ba r2 myprog!LoadFile+2E 

0:000> .bpcmds
bu0 notepad!winmain;
bu1 notepad!LoadFile;
bp2 0x0042cc10 ;
bu3 @!"myprog!openFile";
bu4 @!"myprog!openFilter";
bp5 0x00421600 ;
ba6 r2 0x0042cc2e ;
```

In this example, notice that the output of **.bpcmds** begins with the relevant command ("bu", "bp", or "ba"), followed by the breakpoint number (with no intervening space).

Notice that because breakpoint number 0 was originally set using **bp**, and then was redefined using **bu**, the display shows its type as "bu".

Notice also that breakpoints 3, 4, and 5, which were created by the **bm** commands shown in this example, are displayed as either type "bp" or type "bu", depending on whether the **/d** switch was included when **bm** was used.

 

 





