---
title: PoolMon Startup Command
description: To start PoolMon, type a command at the command line using the following syntax and parameters.
ms.assetid: 2aa0cf09-f016-46b9-af4e-0f3fbc6fbe5b
keywords:
- PoolMon Startup Command Driver Development Tools
topic_type:
- apiref
api_name:
- PoolMon Startup Command
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PoolMon Startup Command


To start PoolMon, type a command at the command line using the following syntax and parameters.

```
    poolmon [/iTag] [/xTag] [/c [LocalTagFile]] [/g [PoolTagFile]] [/s[TSSessionID]] [ /p | /p /p ] [/e] [/( | /)]  [/t | /a| /f| /d | /b| /m] [/l] [/n [File]] [/? | /h] 
```

## <span id="ddk_poolmon_startup_command_tools"></span><span id="DDK_POOLMON_STARTUP_COMMAND_TOOLS"></span>Parameters


<span id="________i______"></span><span id="________I______"></span> **/i**   
Displays only the allocations with the specified pool tag. You can have multiple **/i** parameters in a PoolMon command. Do not type a space between the **/i** and the *Tag* argument.

<span id="________x______"></span><span id="________X______"></span> **/x**   
Excludes allocations with the specified tag from the display. You can have multiple **/x** parameters in a PoolMon command. Do not type a space between the **/x** and the *Tag* argument.

<span id="_______Tag______"></span><span id="_______tag______"></span><span id="_______TAG______"></span> *Tag*   
Specifies a pool tag or pool tag pattern. Pool tags are case-sensitive. The *Tag* argument can include an asterisk (**\\***) to represent zero or more instances of any character, or a question mark (*<em>?</em>*) to represent one instance of any character. Do not begin a tag with an asterisk.

<span id="________c______"></span><span id="________C______"></span> **/c**   
Adds a column to the display (Mapped\_Driver) listing the drivers on the local computer that use each pool tag. This feature is supported only on 32-bit versions of Windows.

<span id="_______LocalTagFile______"></span><span id="_______localtagfile______"></span><span id="_______LOCALTAGFILE______"></span> *LocalTagFile*   
Specifies the path and file name of a local tag file, a formatted text file that contains a list of the drivers on the local computer, and the tag values that they assign. This file is the data source for the Mapped\_Driver column that appears when you use the **/c** parameter. The default is localtag.txt.

If you use the **/c** parameter, but do not specify a value for *LocalTagFile*, and PoolMon does not find a localtag.txt file in the current directory, PoolMon generates a localtag.txt file by scanning the drivers on the local computer (%SystemRoot%\\System32\\Drivers\\\*.sys) .

<span id="________g______"></span><span id="________G______"></span> **/g**   
Adds a column to the display (Mapped\_Driver) listing Windows components and commonly used drivers that assign each tag.

<span id="_______PoolTagFile______"></span><span id="_______pooltagfile______"></span><span id="_______POOLTAGFILE______"></span> *PoolTagFile*   
Specifies the path and file name of a formatted text file that lists the names of Windows components and commonly used drivers and the tag values they assign. This file is the data source for the Mapped\_Driver column that appears when you use the **/g** parameter.

The default is pooltag.txt, a file provided by Microsoft. *Pooltag.txt* is included in the Tools\\Other subdirectory of the Windows Driver Kit (WDK).

<span id="________s______"></span><span id="________S______"></span> **/s**   
Displays allocations from the Terminal Services session pools.

<span id="_______TSSessionID______"></span><span id="_______tssessionid______"></span><span id="_______TSSESSIONID______"></span> *TSSessionID*   
Displays only allocations from the specified session pool. Do not type a space between the **/s** parameter and the *TSSessionID* argument.

<span id="________p______"></span><span id="________P______"></span> **/p**   
Displays only allocations from the nonpaged pool.

<span id="________p__p_______"></span><span id="________P__P_______"></span> **/p /p**   
Displays only allocations from the paged pool.

<span id="________e_______"></span><span id="________E_______"></span> **/e**   
Displays pool totals. The totals appear at the bottom of the display.

<span id="__________or___"></span><span id="__________OR___"></span> **/(** or **/)**  
Turns on the sort-by-change mode. With **/(** or **/)**, PoolMon sorts by the change in a value (allocation, free operations, and bytes), instead of the value. The change in each value is displayed in a parentheses after the value.

Use with **/a**, **/f**, **/b** or **/m**. For example, **poolmon /a** sorts the display by number of allocations, while **poolmon /( /a** sorts the display by the change in the number of allocations.

The left parenthesis and right parenthesis characters have the same effect and can be used interchangeably.

<span id="________t______"></span><span id="________T______"></span> **/t**   
Sorts alphabetically by tag name. This is the default.

<span id="________a______"></span><span id="________A______"></span> **/a**   
Sorts tags by the number of allocations.

<span id="________f_______"></span><span id="________F_______"></span> **/f**   
Sorts tags by the number of free operations.

<span id="________d______"></span><span id="________D______"></span> **/d**   
Sorts tags by the difference between bytes allocations and bytes freed.

<span id="________b_______"></span><span id="________B_______"></span> **/b**   
Sorts tags by bytes used.

<span id="________m_______"></span><span id="________M_______"></span> **/m**   
Sorts tags by bytes-per-allocation.

<span id="________l______"></span><span id="________L______"></span> **/l**   
Turns highlighting off. By default, PoolMon highlights values that have changed since the last update.

<span id="________n______"></span><span id="________N______"></span> **/n**   
Saves a snapshot of the PoolMon output to a file, instead of displaying it in a command window. You can include other command-line parameters to configure the output.

Because the snapshot data is static, the columns that show the change in values in the PoolMon display do not appear in a snapshot file.

<span id="_______File______"></span><span id="_______file______"></span><span id="_______FILE______"></span> *File*   
Specifies the name and location of the snapshot file. The default is poolsnap.log.

<span id="__________or__h"></span><span id="__________OR__H"></span> **/?** or **/h**  
Displays command-line syntax. The **/?** and **/h** parameters have the same effect and can be used interchangeably.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

PoolMon cannot generate a localtag.txt file on the 64-bit version of Windows Server 2003. As a result, the **/c** parameter and its functionality are available only on 32-bit versions of Windows.

You can use the **/c** and **/g** parameters in the same command. If you do, the Mapped\_Driver column displays data from both the local tag and pool tag files.

You can also use **/c** and **/g** to display data from other files in the Mapped\_Driver column by specifying a file name and location with either parameter -- **poolmon /c** *filename* or **poolcom /g** *filename*. In this case, the **/c** and **/g** parameters behave identically and can be used interchangeably.

Terminal Services session pool monitoring is available only on Windows Server 2003 and later versions of Windows.

The kernel-mode portions of the Win32 subsystem allocate memory from Terminal Services session pools only when the computer is configured as a Terminal Server. Otherwise, Windows allocates pool memory for Terminal Services from the system pool.









