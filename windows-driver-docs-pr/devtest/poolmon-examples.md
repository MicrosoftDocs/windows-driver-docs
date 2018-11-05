---
title: PoolMon Examples
description: PoolMon Examples
ms.assetid: aff0abdd-7d68-49b8-b9a1-71ab866c8487
keywords:
- PoolMon WDK , examples
- Memory Pool Monitor WDK , examples
- examples WDK PoolMon
ms.date: 07/02/2017
ms.localizationpriority: medium
---

# PoolMon Examples


## <span id="ddk_poolmon_examples_tools"></span><span id="DDK_POOLMON_EXAMPLES_TOOLS"></span>


This topic includes the following examples of PoolMon use:

Example 1: Display and Sort PoolMon Output

Example 2: Display Driver Names

Example 3: Detect Memory Leakage

Example 4: Examine a Pool Memory Leak

Example 5: Monitor a Terminal Server Session

### <span id="ddk_example_1_display_and_sort_poolmon_output_tools"></span><span id="DDK_EXAMPLE_1_DISPLAY_AND_SORT_POOLMON_OUTPUT_TOOLS"></span>Example 1: Display and Sort PoolMon Output

This example describes various ways to configure the PoolMon display. By default, PoolMon displays all kernel memory allocations in alphanumeric order by tag value. You can modify the sort order of the display at the command line or while PoolMon is running.

The following command starts PoolMon:

```
poolmon
```

The following command starts PoolMon and sorts the display by number of free operations:

```
poolmon /f
```

While poolmon is running, you can use the run-time commands to change the display. For example, to sort the display by number of bytes used, press **b**. To sort by bytes per allocation, press **m**.

The following command starts PoolMon and displays only allocations from the nonpaged pool:

```
poolmon /p
```

While PoolMon is running, press **p** to toggle through allocations from the paged pool, the nonpaged pool, or both.

To start PoolMon and display data for allocations with a particular tag, use the **/i** parameter. The following command displays allocations with the **AfdB** tag (the tag used by afd.sys for data buffers).

```
poolmon /iAfdB
```

To exclude allocations with a particular tag, use the **/x** parameter. The following command displays all allocations that do not have the **AfdB** tag;

```
poolmon /xAfdB
```

You can use an asterisk (\*) and/or a question mark (?) to specify a set of tags with the same characters. The following command displays allocations that have pool tags beginning with **Afd**, the tag used by afd.sys;

```
poolmon /iAfd*
```

A PoolMon startup command can include multiple **/i** and **/x** parameters. The following command displays allocations that have tags beginning with **Aud** and four-character tags beginning with **Cc**, except for allocations with the **CcBc** tag;

```
poolmon /iAud* /iCc?? /xCcBc
```

You can also sort the PoolMon display by the change in a value between updates. The **/(** parameter places PoolMon in sort-by-change mode.

The following command displays allocations with tags beginning with **Afd**, and sorts by the change in allocations. It uses the **/a** parameter to sort by number of allocations and the **/)** parameter to sort by the change in the number of allocations.

```
poolmon /iAfd* /( /a
```

The **/(** parameter and the parentheses keys are toggle switches. When PoolMon is in sort-by-change mode, it interprets all sort commands as commands to sort by the change in the value. If you press a parenthesis key again, it sorts by the value.

### <span id="ddk_example_2_display_driver_names_tools"></span><span id="DDK_EXAMPLE_2_DISPLAY_DRIVER_NAMES_TOOLS"></span>Example 2: Display Driver Names

You can use the PoolMon **/g** parameter to display the names of Windows components and commonly used drivers that assign each pool tag. If you find a problem in allocations with a particular tag, this feature helps you identify the offending component or driver.

The components and drivers are listed in the Mapped\_Driver column, the right-most column in the display. The data for the Mapped\_Driver column comes from pooltag.txt, a file installed with PoolMon.

The following command displays memory allocated with tags that begin with **NtF**. (It uses the question mark character (**?**) as a wildcard.) The **/g** parameter adds the Mapped\_Driver column.

```
poolmon /iNtF? /g
```

The resulting display lists allocations with tags beginning in **NtF**. The rightmost column in the display, Mapped\_Driver, shows that the memory was allocated by ntfs.sys, the driver for the NTFS file system. In this case, the display is even more specific, because pooltag.txt includes the source files for NTFS allocations.

```
 Memory:  260620K Avail:   65152K  PageFlts:    85   InRam Krnl: 2116K P:19560K
 Commit: 237688K Limit: 640916K Peak: 260632K            Pool N: 8500K P:33024K
 System pool information
 Tag  Type     Allocs            Frees            Diff   Bytes      Per Alloc  Mapped_Driver

 NtFA Nonp       9112 (   0)      9112 (   0)     0       0 (     0)      0 [ntfs.sys  -  AttrSup.c]
 NtFB Paged      3996 (   0)      3986 (   0)    10  252088 (     0)  25208 [ntfs.sys  -  BitmpSup.c]
 NtFC Paged   1579279 (   0)   1579269 (   0)    10     640 (     0)     64 [ntfs.sys  -  Create.c]
 NtFD Nonp         13 (   0)        13 (   0)     0       0 (     0)      0 [ntfs.sys  -  DevioSup.c]
 NtFF Paged      1128 (   0)      1128 (   0)     0       0 (     0)      0 [ntfs.sys  -  FileInfo.c]
 NtFI Nonp        152 (   0)       152 (   0)     0       0 (     0)      0 [ntfs.sys  -  IndexSup.c]
 NtFL Nonp      68398 (   0)     68390 (   0)     8   27280 (     0)   3410 [ntfs.sys  -  LogSup.c]
 NtFS Paged      2915 (   0)      2614 (   0)   301   80192 (     0)    266 [ntfs.sys  -  SecurSup.c]
 NtFa Paged       838 (   0)       829 (   0)     9     288 (     0)     32 [ntfs.sys  -  AllocSup.c]
 NtFd Paged    137696 (   0)    137688 (   0)     8     720 (     0)     90 [ntfs.sys  -  DirCtrl.c]
 NtFf Nonp          2 (   0)         1 (   0)     1      40 (     0)     40 [ntfs.sys  -  FsCtrl.c]
 NtFs Nonp      48825 (   0)     47226 (   0)  1599   64536 (     0)     40 [ntfs.sys  -  StrucSup.c]
 NtFv Paged       551 (   0)       551 (   0)     0       0 (     0)      0 [ntfs.sys  -  ViewSup.c]
```

Pooltag.txt is extensive, but it is not a complete list of all tags used in Windows. When a tag that appears in the display is not included in pooltag.txt, PoolMon displays "Unknown driver" in the Mapped\_Driver column for the tag. When this occurs, you can use the **/c** parameter to search the drivers on the local system and determine whether they assign the tag.

The following examples demonstrate this method.

The following command uses the **/i** parameter to list allocations with tags that end in MEM. The **/g** parameter adds the driver name to the display from the pooltag.txt file.

```
poolmon /i?MEM /g
```

The resulting display lists the allocations with tags ending in MEM. However, because the MEM tags are not included in pooltag.txt, "Unknown Driver" appears in the Mapped\_Driver column in place of the driver name.

```
 Tag  Type        Allocs          Frees      Diff   Bytes      Per Alloc    Mapped_Driver

 1MEM Nonp       1 (   0)         0 (   0)     1    3344 (     0)   3344   Unknown Driver
 2MEM Nonp       1 (   0)         0 (   0)     1    3944 (     0)   3944   Unknown Driver
 3MEM Nonp       3 (   0)         0 (   0)     3     248 (     0)     82   Unknown Driver
```

In this case, you can use the **/c** parameter to compile a list of local drivers and the tags they assign, and then display the names of local drivers in the Mapped\_Driver column.

The following command starts PoolMon. It uses the **/i** parameter to list allocations with tags ending in MEM, and the **/c** parameter to display the local drivers that assign the tags.

```
poolmon /i?MEM /c
```

If you do not specify a local tag file and PoolMon cannot find a localtag.txt file , it creates one, as shown in the following screen messages. (PoolMon cannot generate a local tag file on 64-bit versions of Windows.)

```
d:\tools\poolmon>poolmon /?MEM /c
PoolMon: No localtag.txt in current directory
PoolMon: Creating localtag.txt in current directory......
```

The resulting display, which uses the content from the newly created localtag.txt file, shows the local driver names in the Mapped\_Driver column.

```
 Memory:  260620K Avail:   57840K  PageFlts:   162   InRam Krnl: 2116K P:19448K
 Commit: 244580K Limit: 640916K Peak: 265416K            Pool N: 8496K P:32904K
 System pool information
 Tag  Type     Allocs            Frees            Diff   Bytes      Per Alloc  Mapped_Driver

 1MEM Nonp          1 (   0)         0 (   0)        1    3344 (     0)   3344 [el90xbc5]
 2MEM Nonp          1 (   0)         0 (   0)        1    3944 (     0)   3944 [el90xbc5]
 3MEM Nonp          3 (   0)         0 (   0)        3     248 (     0)     82 [el90xbc5]
```

For a comprehensive driver name display, you can combine the **/c** and **/g** parameters in a command. (The order of parameters does not change the output.) The following command lists allocations for tags beginning with **Ip**. It uses the **/c** parameter, which uses the contents of the localtag.txt file in the Mapped\_Driver column, and the **/g** parameter, which uses the contents of the pooltag.txt file in the Mapped\_Driver column.

```
poolmon /iIp* /c /g
```

In the resulting display, the Mapped\_Driver column contains data from both the localtag.txt and pooltag.txt files.

```
 Memory:  130616K Avail:   23692K  PageFlts:   146   InRam Krnl: 2108K P: 9532K
 Commit: 187940K Limit: 318628K Peak: 192000K            Pool N: 8372K P:13384K
 System pool information
 Tag  Type     Allocs            Frees            Diff   Bytes      Per Alloc  Mapped_Driver

 IpEQ Nonp          1 (   0)         0 (   0)        1    1808 (     0)   1808 [ipsec][ipsec.sys    -  event queue]
 IpFI Nonp         26 (   0)         0 (   0)       26    7408 (     0)    284 [ipsec][ipsec.sys    -  Filter blocks]
 IpHP Nonp          1 (   0)         1 (   0)        0       0 (     0)      0 [ipsec.sys    - IP Security]
 IpIO Nonp          1 (   0)         1 (   0)        0       0 (     0)      0 [ipsec]
 IpLA Nonp          1 (   0)         0 (   0)        1     248 (     0)    248 [ipsec][ipsec.sys    -  lookaside lists]
 IpSH Nonp          1 (   0)         1 (   0)        0       0 (     0)      0 [ipsec.sys    - IP Security]
 IpSI Nonp       1027 (   0)         0 (   0)     1027   53272 (     0)     51 [ipsec][ipsec.sys    - initial allcoations]
 IpTI Nonp          3 (   0)         0 (   0)        3    5400 (     0)   1800 [ipsec][ipsec.sys    -  timers]
```

### <span id="ddk_example_3_detect_memory_leakage_tools"></span><span id="DDK_EXAMPLE_3_DETECT_MEMORY_LEAKAGE_TOOLS"></span>Example 3: Detect Memory Leakage

This example suggests a procedure for using PoolMon to detect a memory leak.

1.  Start PoolMon with the parameters **/p /p** (display only allocations from the paged pool) and **/b** (sort by the number of bytes).
    ```
    poolmon /p /p /b
    ```

2.  Let PoolMon run for a few hours. Because starting PoolMon changes the data, it must regain a steady state before the data is reliable.

3.  Save the information generated by PoolMon, either as a screen shot, or by copying it from the command window and pasting it into Notepad.

4.  Returning to PoolMon, press the **p** key twice to display only allocations from the nonpaged pool.

5.  Repeat steps 3 and 4 approximately every half-hour for at least two hours, switching between the paged and nonpaged pool displays each time.

6.  When data collection is complete, examine the Diff (allocation operations minus free operations) and Bytes (number of bytes allocated minus number of bytes freed) values for each tag, and note any that continually increase.

7.  Next, stop PoolMon, wait for a few hours, and then restart PoolMon.

8.  Examine the allocations that were increasing, and determine whether the bytes are now freed. The likely cause is allocations that have still not been freed or have continued to increase in size.


### <span id="ddk_example_4_examine_a_pool_memory_leak_tools"></span><span id="DDK_EXAMPLE_4_EXAMINE_A_POOL_MEMORY_LEAK_TOOLS"></span>Example 4: Examine a Pool Memory Leak

The following example demonstrates using PoolMon to investigate a pool memory leak from a suspected printer driver. In this example, PoolMon displays data that Windows collects about memory allocations with the Dsrd tag.

Printer drivers assign the Drsd tag when they allocate Graphical Device Interface (GDI) objects and associated memory. If a printer driver has an object leak, the memory allocated with the Drsd tag also will leak.

**Note**   Before running the steps in this example, ensure that the printer you are using will not be interrupted until you are finished. Otherwise, the results may be invalid.

 

At the command line, type the following:

```
poolmon /iDrsd
```

This command directs PoolMon to display information for allocations with the Drsd tag. (Pool tags are case-sensitive, so be sure to type the command exactly as shown.)

Record the values in the Diff and Bytes columns. In the following sample display, the value of Diff is 21 and the number of Bytes is 17472.

```
Memory:  130480K Avail:   91856K  PageFlts:  1220   InRam Krnl: 2484K P: 7988K
Commit:  30104K Limit: 248432K Peak:  34028K            Pool N: 2224K P: 8004K
Tag  Type        Allocs           Frees           Diff  Bytes           Per Alloc

Drsd Paged       560 ( 177)       539 ( 171)       21   17472 (  4992)    832 
```

Send a job to the printer, wait briefly for Windows to return to normal, and then record the values for the Diff and Bytes columns.

```
Memory:  130480K Avail:   91808K  PageFlts:  1240   InRam Krnl: 2488K P: 7996K
Commit:  30152K Limit: 248432K Peak:  34052K            Pool N: 2224K P: 8012K
Tag  Type        Allocs           Frees           Diff  Bytes          Per Alloc

Drsd Paged       737 (   0)       710 (   0)       27   22464 (     0)    832  
```

When the memory management for the printer driver is working properly, the value of Diff should return to its original value of 21 after printing. However, as the preceding output illustrates, the value of Diff rose to 27, and the number of Bytes rose to 22464. The difference between the initial and subsequent output means that six Drsd blocks, with a total of 4992 bytes, leaked during printing.

### <span id="For_More_Information"></span><span id="for_more_information"></span><span id="FOR_MORE_INFORMATION"></span>For More Information

If you believe you have identified a leaking driver, go to the [Microsoft support](http://go.microsoft.com/fwlink/p/?linkid=8713) website and search the Knowledge Base for relevant articles.

### <span id="ddk_example_5_monitor_a_terminal_server_session_tools"></span><span id="DDK_EXAMPLE_5_MONITOR_A_TERMINAL_SERVER_SESSION_TOOLS"></span>Example 5: Monitor a Terminal Server Session

This example shows several ways to display allocations from the Terminal Services session pools. It demonstrates the use of the **/s** command-line parameter, and the **s**, *TSSessionID*, and **i** running parameters.

The following command displays allocations from all of the Terminal Services session pools. In this example, the local computer, which is configured as a Terminal Server, is hosting the sessions, and client computers are using the Remote Desktop feature to connect to the host.

```
poolmon /s
```

In response, PoolMon displays allocations from all session pools. Note the "All sessions pool information" title in the header.

```
Memory:  523572K Avail:  233036K  PageFlts:   344   InRam Krnl: 1828K P:18380K
Commit: 193632K Limit:1279764K Peak: 987356K            Pool N:14332K P:18644K
All sessions pool information
 Tag  Type     Allocs            Frees            Diff   Bytes       Per Alloc

 Bmfd Paged       361 (   0)       336 (   0)       25   57832 (     0)   2313
 DDfb Paged        34 (   0)        22 (   0)       12     720 (     0)     60
 Dddp Paged         8 (   0)         6 (   0)        2     272 (     0)    136
 Dh 1 Paged        24 (   0)        24 (   0)        0       0 (     0)      0
 Dh 2 Paged       344 (   0)       344 (   0)        0       0 (     0)      0
 Dvgr Paged         2 (   0)         2 (   0)        0       0 (     0)      0
 GDev Paged       108 (   0)       102 (   0)        6   20272 (     0)   3378
 GFil Paged        29 (   0)        27 (   0)        2     160 (     0)     80
 GPal Paged        11 (   0)         8 (   0)        3     816 (     0)    272
 GTmp Paged     88876 (   1)     88876 (   1)        0       0 (     0)      0
 GUma Paged         2 (   0)         2 (   0)        0       0 (     0)      0
 Galp Paged      3250 (   0)      3250 (   0)        0       0 (     0)      0
 Gbaf Paged      9829 (   0)      9801 (   0)       28   19712 (     0)    704
 Gcac Paged      3761 (   0)      3706 (   0)       55  288968 (     0)   5253
 Gcsl Paged         1 (   0)         0 (   0)        1     488 (     0)    488
 Gdbr Paged      6277 (   0)      6271 (   0)        6    1872 (     0)    312
 ...
```

To see allocations from a particular session pool, type the session ID immediately after the **/s** parameter, as shown in the following command. This command displays session pool allocations for Terminal Services session 0.

```
poolmon /s0
```

In response, PoolMon displays allocations from the session pool for Terminal Services session 0. Note the "Session 0 pool information" title in the header.

```
Memory:  523572K Avail:  233024K  PageFlts:   525   InRam Krnl: 1828K P:18384K
 Commit: 193760K Limit:1279764K Peak: 987356K            Pool N:14340K P:18644K
 Session 0 pool information
 Tag  Type     Allocs            Frees            Diff   Bytes       Per Alloc

 Bmfd Paged       361 (   0)       336 (   0)       25   57832 (     0)   2313
 DDfb Paged        34 (   0)        22 (   0)       12     720 (     0)     60
 Dddp Paged         8 (   0)         6 (   0)        2     272 (     0)    136
 Dh 1 Paged        24 (   0)        24 (   0)        0       0 (     0)      0
 Dh 2 Paged       344 (   0)       344 (   0)        0       0 (     0)      0
 Dvgr Paged         2 (   0)         2 (   0)        0       0 (     0)      0
 GDev Paged       108 (   0)       102 (   0)        6   20272 (     0)   3378
 GFil Paged        29 (   0)        27 (   0)        2     160 (     0)     80
 GPal Paged        11 (   0)         8 (   0)        3     816 (     0)    272
 GTmp Paged     89079 (  99)     89079 (  99)        0       0 (     0)      0
 GUma Paged         2 (   0)         2 (   0)        0       0 (     0)      0
 Galp Paged      3250 (   0)      3250 (   0)        0       0 (     0)      0
 Gbaf Paged      9830 (   0)      9802 (   0)       28   19712 (     0)    704
 Gcac Paged      3762 (   0)      3707 (   0)       55  283632 (     0)   5156
 Gcsl Paged         1 (   0)         0 (   0)        1     488 (     0)    488
 Gdbr Paged      6280 (   0)      6274 (   0)        6    1872 (     0)    312
 ...
```

To help determine which drivers and components are allocating memory from the session pool, add the **/g** parameter, as shown in the following command. The **/g** parameter adds a Mapped\_Driver column listing the Windows components and drivers that assign each tag.

```
poolmon /s0 /g

Memory:  523572K Avail:  235876K  PageFlts:    43   InRam Krnl: 1900K P:18860K
Commit: 185040K Limit:1279764K Peak: 987356K            Pool N:14684K P:19124K
Session 0 pool information
Tag  Type     Allocs            Frees            Diff   Bytes      Per Alloc  Mapped_Driver

Bmfd Paged       421 (   0)       396 (   0)       25   57832 (     0)   2313 [Font related stuff]
DDfb Paged        34 (   0)        22 (   0)       12     720 (     0)     60 Unknown Driver
Dddp Paged        11 (   0)         6 (   0)        5     392 (     0)     78 Unknown Driver
Dh 1 Paged        37 (   0)        35 (   0)        2     224 (     0)    112 Unknown Driver
Dh 2 Paged       367 (   0)       364 (   0)        3     912 (     0)    304 Unknown Driver
Dvgr Paged         2 (   0)         2 (   0)        0       0 (     0)      0 [vga for risc video driver]
GDev Paged       119 (   0)       113 (   0)        6   20272 (     0)   3378 [Gdi pdev]
GFil Paged        29 (   0)        27 (   0)        2     160 (     0)     80 [Gdi engine descriptor list]
GPal Paged        11 (   0)         8 (   0)        3     816 (     0)    272 [Gdi Objects]
GTmp Paged     98626 (   1)     98626 (   1)        0       0 (     0)      0 [Gdi Objects]
GUma Paged         2 (   0)         2 (   0)        0       0 (     0)      0 [Gdi Objects]
Galp Paged      3250 (   0)      3250 (   0)        0       0 (     0)      0 [Gdi Objects]
Gbaf Paged     10331 (   0)     10305 (   0)       26   18304 (     0)    704 [Gdi Objects]
Gcac Paged      4722 (   0)      4666 (   0)       56  305400 (     0)   5453 [Gdi glyph cache]
Gcsl Paged         1 (   0)         0 (   0)        1     488 (     0)    488 [Gdi string resource script names]
Gdbr Paged      6972 (   0)      6965 (   0)        7    2184 (     0)    312 [Gdi driver brush realization]
```

You can also configure the Terminal Services session pool display while PoolMon is running. The following table shows a series of running commands, in the order in which they are typed, and the resulting PoolMon display.

The series begins with a command to start PoolMon. All other parameters are typed while PoolMon is running.

```
poolmon
```

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Key</th>
<th align="left">Result</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>s</strong></p></td>
<td align="left"><p>Displays all session pools.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>s</strong></p></td>
<td align="left"><p>Displays the system pools.</p></td>
<td align="left"><p>The <strong>s</strong> parameter toggles the display between the system pools and the Terminal Services session pools.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>0</strong></p></td>
<td align="left"><p>Displays session 0 pool.</p></td>
<td align="left"><p>You can type a session ID while displaying the system pools.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>7</strong></p></td>
<td align="left"><p>Displays session 7 pool.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>a</strong></p></td>
<td align="left"><p>Displays pool allocations for session 7, sorted by number of allocations.</p></td>
<td align="left"><p>All standard running parameters are valid for session pool displays.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>0</strong></p></td>
<td align="left"><p>Displays allocations for session 0, sorted by number of allocations.</p></td>
<td align="left"><p>Session and sorting options are retained until changed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>s</strong></p></td>
<td align="left"><p>Displays the system pools.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>s</strong></p></td>
<td align="left"><p>Displays allocations for session 0, sorted by number of allocations.</p></td>
<td align="left"><p>Session option is retained.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>10ENTER</strong></p></td>
<td align="left"><p>Displays Session 1 allocations, and then displays Session 0 allocations.</p></td>
<td align="left"><p>Without <strong>i</strong>, you can enter only session IDs 0 through 9.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>i</strong></p></td>
<td align="left"><p>Prompts for a Terminal Server session ID.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>10</strong></p></td>
<td align="left"><p>Displays Session 10 allocations.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>i</strong></p></td>
<td align="left"><p>Prompts for a Terminal Server session ID.</p></td>
<td align="left"><p>To display all session pools, press <strong>i</strong> and then press ENTER.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ENTER</strong></p></td>
<td align="left"><p>Displays all session pools.</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

Only systems configured as a Terminal Server allocate memory from the session pool. If you use PoolMon to display the session pool on a computer that is not a Terminal Server, or if you type a session ID that does not exist on Windows, PoolMon does not display any allocations. Instead, it displays only the headings with general memory data.

The following command displays allocations from all Terminal Services session pools:

```
poolmon /s
```

The following figure shows the PoolMon display that would result if the **/s** command were submitted to a computer running Windows XP that could not be configured as a Terminal Server:

```
 Memory:  260620K Avail:   44956K  PageFlts:   308   InRam Krnl: 2744K P:20444K
 Commit: 185452K Limit: 640872K Peak: 192472K            Pool N: 8112K P:20648K
 All sessions pool information
 Tag  Type     Allocs            Frees            Diff   Bytes       Per Alloc
```

 

 





