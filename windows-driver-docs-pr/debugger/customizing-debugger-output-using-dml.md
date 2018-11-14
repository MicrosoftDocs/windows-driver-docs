---
title: Customizing Debugger Output Using DML
description: The debugger markup language (DML) provides a mechanism for enhancing output from the debugger and extensions.
ms.assetid: 04984510-B95F-405F-81DF-E9D0673210B4
ms.author: domars
ms.date: 11/13/2018
ms.localizationpriority: medium
---

# Customizing Debugger Output Using DML


The debugger markup language (DML) provides a mechanism for enhancing output from the debugger and extensions. Similar to HTML, the debugger’s markup support allows output to include display directives and extra non-display information in the form of tags. The debugger user interfaces, such as WinDbg parse out the extra information provided in DML to enhance the display of information and provide new behaviors, such as grid displays and sorting. This topic describes how you can customize your debug output using DML. For general information on enabling and using DML in the debuggers, see [Using Debugger Markup Language](debugger-markup-language-commands.md).

DML is available in Windows 10 and later.

## <span id="DML_Overview"></span><span id="dml_overview"></span><span id="DML_OVERVIEW"></span>DML Overview


On of DML's primary benefits it to provide the ability to link to related information in debugger output. One of the primary DML tags is the &lt;link&gt; tag which lets an output producer indicate that information related to a piece of output can be accessed via the link’s stated action. As with HTML links in a web browser, this allows the user to navigate hyperlinked information.

A benefit of providing hyperlinked content is that it can be used to enhance the discoverability of debugger and debugger extension functionality. The debugger and its extensions contain a large amount of functionality but it can be difficult to determine the appropriate command to use in different scenarios. Users must simply know what commands are available to use in specific scenarios. Differences between user and kernel debugging add further complexity. This often means that many users are unaware of debug commands which could help them. DML links provides the ability for arbitrary debug commands to be wrapped in alternate presentations, such as descriptive text, clickable menu systems or linked help. Using DML, the command output can be enhanced to guide the user to additional related commands relevant for the task at hand.

**Debugger DML Support**

-   The command window in WinDbg supports all DML behavior and will show colors, font styles and links.
-   The console debuggers – ntsd, cdb and kd – only support the color attributes of DML, and the only when running in a true console with color mode enabled.
-   Debuggers with redirected I/O, ntsd –d or remote.exe sessions will not display any colors.

## <span id="DML_Content_Specification"></span><span id="dml_content_specification"></span><span id="DML_CONTENT_SPECIFICATION"></span>DML Content Specification


DML is not intended to be a full presentation language such as HTML. DML is deliberately very simple and has only a handful of tags.

Because not all debugger tools support rich text, DML is designed to allow simple translation between DML and plain text. This allows DML to function in all existing debugger tools. Effects such as colors can easily be supported since removing them does not remove the text carrying the actual information.

DML is not XML. DML does not attempt to carry semantic nor structured information. As mentioned above, there must be a simple mapping between DML and plain text, for this reason, DML tags are all discardable.

DML is not extensible; all tags are pre-defined and validated to work across all of the existing debugger tools.

**Tag Structure**

Similar to XML, DML tags are given as a starting &lt;tagname \[args\]&gt; and a following &lt;/tagname&gt;.

**Special Characters**

DML content roughly follows the XML/HTML rules for special characters. The characters &, &lt;, &gt; and “ are special and cannot be used in plain text. The equivalent escaped versions are &, &lt;, &gt; and &quot;. For example this text:

"Alice & Bob think 3 &lt; 4"

would be converted to the following DML.

```text
&quot;Alice & Bob think 3 &lt 4&quot;
```

**C programming language formatting characters**

A significant departure from XML/HTML rules is that DML text can include C programming language stream-style formatting characters such as \\b, \\t, \\r and \\n. This is to support compatibility with existing debugger text production and consumption.

## <span id="Example_DML"></span><span id="example_dml"></span><span id="EXAMPLE_DML"></span>Example DML


Suppose the file C:\\Dml\_Experiment.txt contains the following lines.

```text
My DML Experiment
<link cmd="lmD musb*">List modules that begin with usb.</link>
```

The following command displays the text and link in the Command Browser window.

```dbgcmd
.browse .dml_start c:\Dml_Experiment.txt
```

![screen shot of dml file output](images/dmlcommands03.png)

If you click the **List modules that begin with usb** link, you see output similar to the following image.

![screen shot of module list](images/dmlcommands04.png)

## <span id="Right-Click_Behavior_in_DML"></span><span id="right-click_behavior_in_dml"></span><span id="RIGHT-CLICK_BEHAVIOR_IN_DML"></span>Right-Click Behavior in DML


Right-click behavior is available in DML. This sample shows how to define right click behavior using &lt;altlink&gt; to send a breakpoint [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command and send the [**u (Unassemble)**](u--unassemble-.md) with a regular click.

```text
<link cmd="u MyProgram!memcpy">
<altlink name="Set Breakpoint (bp)" cmd="bp MyProgram!memcpy" />
u MyProgram!memcpy
</link>
```

## <span id="DML_Tag_Reference"></span><span id="dml_tag_reference"></span><span id="DML_TAG_REFERENCE"></span>DML Tag Reference


### <span id="_link_"></span><span id="_LINK_"></span>&lt;link&gt;

*&lt;link \[name=”text”\] \[cmd=”debugger\_command”\]\[alt="Hover text to display"\] \[section=”name”\]&gt;link text&lt;/link&gt;*

The link tag is the basic hyper linking mechanism in DML. It directs user interfaces which support DML presentation to display the link text as a clickable link. When a link with a cmd specification is clicked the debugger command is executed and its output should replace the current output.

The name and section arguments allow for navigation between named links, similar to HTML’s &lt;a name&gt; and \#name support. When a link that has a section argument is clicked on the UI will scan for a link named with a matching name and will scroll that into view. This allows links to point to different sections of the same page (or a particular section of a new page). DML’s section name is separate to avoid having to define a new syntax which would allow a section name at the end of the command string.

Conversion to plain text drops the tags.

**Example**

```text
<b> Handy Links </b>
<link cmd="!dml_proc">Display process information with DML rendering.</link>
<link cmd="kM">Display stack information with DML rendering.</link>
```

**Example**

This example shows the use of the alt attribute to create text that will appear when you hover over the DML link.

```text
<b>Hover Example</b>
<link cmd="lmD" alt="This link will run the list modules command and display the output in DML format">LmD</link>
```

### <span id="_altlink_"></span><span id="_ALTLINK_"></span>&lt;altlink&gt;

*&lt;altlink \[name=”text”\] \[cmd=”debugger\_command”\] \[section=”name”\]&gt;alt link text&lt;/altlink&gt;*

The &lt;altlink&gt; tag provides right-click behavior is available in DML. When a link with a cmd specification is clicked the debugger command is executed and its output should replace the current output. The &lt;altlink&gt; tab is normally paired with the &lt;link&gt; tag to support regular and right click behavior.

Conversion to plain text drops the tags.

**Example**

This example shows how to define right click behavior using &lt;altlink&gt; to send a breakpoint [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command and send the [**u (Unassemble)**](u--unassemble-.md) with a regular click.

```text
<link cmd="u MyProgram!memcpy">
<altlink name="Set Breakpoint (bp)" cmd="bp MyProgram!memcpy" />
u MyProgram!memcpy
</link>
```

### <span id="_exec_"></span><span id="_EXEC_"></span>&lt;exec&gt;

*&lt;exec cmd=”debugger\_command”&gt;descriptive text&lt;/exec&gt;*

An exec tag is similar to a link tag in that the descriptive text should be presented as a clickable item. However, when the exec tag is used in a command browser window, the given command is executed without replacing the current output, this tag provides a way to have commands executed with a click, from a menu.

Conversion to plain text drops the tags.

**Example**

This example shows how to define two commands with a regular click.

```text
<b>Exec Sample</b>
<exec cmd="!dml_proc">Display process information with DML rendering.</exec>
<exec cmd="kM">Display stack information with DML rendering.</exec>
```

### <span id="_b_"></span><span id="_B_"></span>&lt;b&gt;

*&lt;b&gt;bold text&lt;/b&gt;*

This tag requests bold. The &lt;b&gt;, &lt;i&gt; and &lt;u&gt; can be nested to have a mix of the properties.

Conversion to plain text drops the tags.

**Example**

This example shows how to bold text.

```text
<b>This is bold Text</b>
```

### <span id="_i_"></span><span id="_I_"></span>&lt;i&gt;

*&lt;i&gt;italicized text&lt;/i&gt;*

This tag requests italics. The &lt;b&gt;, &lt;i&gt; and &lt;u&gt; can be nested to have a mix of the properties.

Conversion to plain text drops the tags.

**Example**

This example shows how to italicize text.

```text
<i>This is italicized Text</i>
```

### <span id="_u_"></span><span id="_U_"></span>&lt;u&gt;

*&lt;u&gt;underlined text&lt;/u&gt;*

This tag requests underlined text. The &lt;b&gt;, &lt;i&gt; and &lt;u&gt; can be nested to have a mix of the properties.

Conversion to plain text drops the tags.

**Example**

This example shows how to underlined text.

```text
<u>This is underlined Text</u>
```

**Example**

This example shows how to combine tags to bold, underline and italicize text.

```text
<b><u><i>This is bold, underlined and italizized text. </i></u></b> 
```

### <span id="_col_"></span><span id="_COL_"></span>&lt;col&gt;

&lt;col fg="name" bg="name"&gt;text&lt;/col&gt;

Request foreground and background colors for the text. The colors are given as names of known colors instead of absolute values as that allows customers to control what kind of color they see. Current color names (defaults only apply to WinDbg).

**Foreground and Background Element Tags**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><strong>Setting</strong></td>
<td align="left"><strong>Description / Example</strong></td>
</tr>
<tr class="even">
<td align="left"><p>wbg - Windows background</p>
<p>wfg - Windows foreground</p></td>
<td align="left">Default window background and foreground colors. Default to system colors for window and window text.
<p>&lt;col fg=&quot;wfg&quot; bg=&quot;wbg&quot;&gt; This is standard foreground / background text &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>clbg - Current line foreground</p>
<p>clfg - Current line background</p></td>
<td align="left">Current line background and foreground colors. Default to system colors for highlight and highlight text.
<p>&lt;col fg=&quot;clfg&quot; bg=&quot;clbg&quot;&gt; Test Text - Current Line&lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>empbg - Emphasized background</p>
<p>emphfg - Emphasized foreground</p></td>
<td align="left">Emphasized text. Defaults to light blue.
<p>&lt;col fg=&quot;empfg&quot; bg=&quot;empbg&quot;&gt; This is emphasis foreground / background text &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>subbg - Subdued background</p>
<p>subfg- Subdued foreground</p></td>
<td align="left">Subdued text. Default to system color for inactive caption text and inactive captions.
<p>&lt;col fg=&quot;subfg&quot; bg=&quot;subbg&quot;&gt; This is subdued foreground / background text &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>normbg - Normal background</p>
<p>normfg - Normal foreground</p></td>
<td align="left">Normal
<p>&lt;col fg=&quot;normfg&quot; bg=&quot;normbg&quot;&gt; Test Text - Normal (normfg / normbg) &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>warnbg - Warning background</p>
<p>warnfg - Warning foreground</p></td>
<td align="left">Warning
<p>&lt;col fg=&quot;warnfg&quot; bg=&quot;warnbg&quot;&gt; Test Text - Warning (warnfg / warnbg) &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>errbg - Error background</p>
<p>errfg - Error foreground</p></td>
<td align="left">Error
<p>&lt;col fg=&quot;errfg&quot; bg=&quot;errbg&quot;&gt; Test Text - Error (errfg / errbg) &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>verbbg - Verbose background</p>
<p>verbfg - Verbose foreground</p></td>
<td align="left">Verbose
<p>&lt;col fg=&quot;verbfg&quot; bg=&quot;verbbg&quot;&gt; Test Text - Verbose (verbfg / verbbg) &lt;/col&gt;</p></td>
</tr>
</tbody>
</table>



**Source Code Single Element Tags**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>srcnum - Source numeric constant</p></td>
<td align="left">Source element colors.
<p>&lt;col fg=&quot;srcnum&quot; bg=&quot;wbg&quot;&gt; Test Text - srcnum &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>srcchar - Source character constant</p></td>
<td align="left"><p>&lt;col fg=&quot;srcchar&quot; bg=&quot;wbg&quot;&gt; Test Text - srcchar &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>srcstr - Source string constant</p></td>
<td align="left"><p>&lt;col fg=&quot;srcstr&quot; bg=&quot;wbg&quot;&gt; Test Text - srcstr &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>srcid -Source identifier</p></td>
<td align="left"><p>&lt;col fg=&quot;srcid &quot; bg=&quot;wbg&quot;&gt; Test Text - srcid &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>srckw- Keyword</p></td>
<td align="left"><p>&lt;col fg=&quot;srckw&quot; bg=&quot;wbg&quot;&gt; Test Text - srckw &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>srcpair - Source brace or matching symbol pair</p></td>
<td align="left"><p>&lt;col fg=&quot;srcpair&quot; bg=&quot;empbbg&quot;&gt; Test Text - srcpair &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>srccmnt - Source comment</p></td>
<td align="left"><p>&lt;col fg=&quot;srccmnt&quot; bg=&quot;wbg&quot;&gt; Test Text - srccmnt &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>srcdrct - Source directive</p></td>
<td align="left"><p>&lt;col fg=&quot;srcdrct&quot; bg=&quot;wbg&quot;&gt; Test Text - srcdrct &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>srcspid - Source special identifier</p></td>
<td align="left"><p>&lt;col fg=&quot;srcspid&quot; bg=&quot;wbg&quot;&gt; Test Text - srcspid &lt;/col&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>srcannot - Source annotation</p></td>
<td align="left"><p>&lt;col fg=&quot;srcannot&quot; bg=&quot;wbg&quot;&gt; Test Text - srcannot &lt;/col&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>changed - Changed data</p></td>
<td align="left">Used for data that has changed since a previous stop point, such as changed registers in WinDbg. Defaults to red.
<p>&lt;col fg=&quot;changed&quot; bg=&quot;wbg&quot;&gt; Test Text - Changed&lt;/col&gt;</p></td>
</tr>
</tbody>
</table>



## <span id="DML_Example_Code"></span><span id="dml_example_code"></span><span id="DML_EXAMPLE_CODE"></span>DML Example Code


This example code illustrates the following.

-   Calling debug commands
-   Implementing right click commands
-   Implementing hover over text
-   Using color and rich text

```XML
<col fg="srckw" bg="wbg"> <b>
*******************************************************
*** Example debug commands for crash dump analysis ****
*******************************************************
</b></col>
<col fg="srcchar" bg="wbg"><i>
**** Hover over commands for additional information ****
        **** Right-click for command help ****
</i></col>

<col fg="srccmnt" bg="wbg"><b>*** Common First Steps for Crash Dump Analysis ***</b> </col>
<link cmd=".symfix" alt="Set standard symbol path using .symfix">.symfix<altlink name="Help about .symfix" cmd=".hh .symfix" /> </link> - Set standard symbol path
<link cmd=".sympath+ C:\Symbols" alt="This link adds addtional symbol directories">.sympath+ C:\Symbols<altlink name="Help for .sympath" cmd=".hh .sympath" /> </link> - Add any additional symbol directories, for example C:\Symbols
<link cmd=".reload /f" alt="This link reloads symbols">.reload /f<altlink name="Help for .reload" cmd=".hh .reload" /> </link> - Reloads symbols to make sure they are in good shape
<link cmd="!analyze -v" alt="This link runs !analyze with the verbose option">!analyze -v<altlink name="Help for !analyze" cmd=".hh !analyze" /> </link> - Run !analyze with the verbose option
<link cmd="vertarget" alt="This link runs checks the target version">vertarget<altlink name="Help for vertarget" cmd=".hh vertarget" /></link> - Check the target version
<link cmd="version" alt="This link displays the versions in use">version<altlink name="Help for version" cmd=".hh version" /></link> - Display the versions in use
<link cmd=".chain /D" alt="This link runs .chain">.chain /D<altlink name="Help for .chain" cmd=".hh .chain" /></link> - Use the .chain /D command to list debugger extensions
<link cmd="kM" alt="This link displays the stack backtrace using DML">kD<altlink name="Help for k" cmd=".hh k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)" /> </link> - Display the stack backtrace using DML rendering
<link cmd="lmD" alt="This link will run the list modules command and display the output in DML format">LmD<altlink name="Help for lmD" cmd=".hh lm" /> </link> - List modules command and display the output in DML format
<link cmd=".help /D" alt="Display help for commands">.help /D <altlink name="Help for .dot commands" cmd=".hh commands" /></link> - Display help for commands in WinDbg
<link cmd=".hh" alt="Start help">.hh<altlink name="Debugger Reference Help".hh Contents" cmd=".hh Debugger Reference" /></link> - Start help

<col fg="srccmnt" bg="wbg"><b>*** Registers and Context ***</b></col>
<link cmd="r" alt="This link displays registers">r<altlink name="Help about r command" cmd=".hh r" /></link>  - Display registers
<link cmd="dt nt!_CONTEXT" alt="This link displays information about nt_CONTEXT">dt nt!_CONTEXT<altlink name="Help about the dt command" cmd=".hh dt" /></link> - Display information about nt_CONTEXT
<link cmd="dt nt!_PEB" alt="This link calls the dt command to display nt!_PEB">dt nt!_PEB<altlink name="Help about dt command" cmd=".hh dt" /></link> - Display information about the nt!_PEB
<link cmd="ub" alt="This link unassembles backwards">ub<altlink name="Help about ub command" cmd=".hh u, ub, uu (Unassemble)" /></link> - Unassemble Backwards

<col fg="srcchar" bg="wbg"><i>
**** Note: Not all of the following commands will work with all crash dump data ****
</i></col>
<col fg="srccmnt" bg="wbg"><b>*** Device Drivers ***</b></col>
<link cmd="!devnode 0 1" alt="This link displays the devnodes">!devnode 0 1<altlink name="Help about !devnode command" cmd=".hh !devnode" /></link> - Display devnodes
<link cmd=".load wdfkd.dll;!wdfkd.help" alt="Load wdfkd extensions and display help">.load wdfkd.dll;!wdfkd.help<altlink name="Help about the wdfkd extensions" cmd=".hh !wdfkd" /></link> - Load wdfkd extensions and display help
<link cmd="!wdfkd.wdfldr" alt="This link displays !wdfkd.wdfldr">!wdfkd.wdfldr<altlink name="Help about !wdfkd.wdfldr" cmd=".hh !wdfkd.wdfldr" /></link>  - Display WDF framework driver loader information
<link cmd="!wdfkd.wdfumtriage" alt="This link displays !wdfkd.umtriage">!wdfkd.umtriage<altlink name="Help about !wdfkd.umtriage" cmd=".hh !wdfkd_wdfumtriage" /></link> - Display WDF umtriage driver information

<col fg="srccmnt" bg="wbg"><b>*** IRPs and IRQL ***</b></col>
<link cmd="!processirps" alt="This link displays process IRPs">!processirps<altlink name="Help about !processirps command" cmd=".hh !processirps" /></link> - Display process IRPs
<link cmd="!irql" alt="This link displays !irql">!irql<altlink name="Help about !irql command" cmd=".hh !irql" /></link> - Run !irql

<col fg="srccmnt" bg="wbg"><b>*** Variables and Symbols ***</b></col>
<link cmd="dv" alt="This link calls the dv command">dv<altlink name="Help about dv command" cmd=".hh dv" /></link> - Display the names and values of all local variables in the current scope

<col fg="srccmnt" bg="wbg"><b>*** Threads, Processes, and Stacks ***</b></col>
<link cmd="!threads" alt="This link displays threads">!threads<altlink name="Help about the !threads command" cmd=".hh !threads" /></link> - Display threads
<link cmd="!ready 0xF" alt="This link runs !ready 0xF">!ready 0xF<altlink name="Help about the !ready command" cmd=".hh !ready" /></link> - Display threads in the ready state
<link cmd="!process 0 F" alt="This link runs !process 0 F ">!process 0 F<altlink name="Help about the !process command" cmd=".hh !process" /></link> - Run !process 0 F
<link cmd="!stacks 2" alt="This link displays stack information using !stacks 2 ">!stacks 2<altlink name="Help about the !stacks command" cmd=".hh !stacks" /></link> - Display stack information using !stacks 2
<link cmd=".tlist" alt="This link displays a process list using TList ">tlist<altlink name="Help about the TList command" cmd=".hh .tlist" /></link> - Display a process list using tlist
<link cmd="!process" alt="This link displays process ">!process<altlink name="Help about the !process command" cmd=".hh !process" /></link> - Display process information
<link cmd="!dml_proc" alt="This link displays process information with DML rendering.">!dml_proc<altlink name="Help about the !dml_proc command" cmd=".hh !dml_proc" /></link> - Display process information with DML rendering
```

This example code illustrates the use of color and formatting tags.

```XML
*** Text Tag Examples ****

<b>This is bold text</b>
<u>This is underlined text</u>
<i>This is italizized text</i>
<b><u><i>This is bold, underlined and italizized text</i></u></b>

<b>Color Tag Examples</b>
<col fg="wfg" bg="wbg"> This is standard foreground / background text </col>
<col fg="empfg" bg="empbg"> This is emphasis foreground / background text </col>
<col fg="subfg" bg="subbg"> This is subdued foreground / background text </col>
<col fg="clfg" bg="clbg"> Test Text - Current Line</col>

<b>Other Tags Sets</b>
<col fg="normfg" bg="normbg"> Test Text - Normal (normfg / normbg) </col>
<col fg="warnfg" bg="warnbg"> Test Text - Warning (warnfg / warnbg) </col>
<col fg="errfg" bg="errbg"> Test Text - Error (errfg / errbg) </col>
<col fg="verbfg" bg="verbbg"> Test Text - Verbose (verbfg / verbbg) </col>

<b>Changed Text Tag Examples</b>
<col fg="changed" bg="wbg"> Test Text - Changed</col>

<b>Source Tags - using wbg background</b>
<col fg="srcnum" bg="wbg"> Test Text - srcnum  </col>
<col fg="srcchar" bg="wbg"> Test Text - srcchar  </col>
<col fg="srcstr" bg="wbg"> Test Text - srcstr  </col>
<col fg="srcid " bg="wbg"> Test Text - srcid   </col>
<col fg="srckw" bg="wbg"> Test Text - srckw </col>
<col fg="srcpair" bg="empbbg"> Test Text - srcpair </col>
<col fg="srccmnt" bg="wbg"> Test Text - srccmnt  </col>
<col fg="srcdrct" bg="wbg"> Test Text - srcdrct </col>
<col fg="srcspid" bg="wbg"> Test Text - srcspid </col>
<col fg="srcannot" bg="wbg"> Test Text - srcannot </col>

<b>Source Tags - using empbg background</b>
<col fg="srcnum" bg="empbg"> Test Text - srcnum  </col>
<col fg="srcchar" bg="empbg"> Test Text - srcchar  </col>
<col fg="srcstr" bg="empbg"> Test Text - srcstr  </col>
<col fg="srcid " bg="empbg"> Test Text - srcid   </col>
<col fg="srckw" bg="empbg"> Test Text - srckw </col>
<col fg="srcpair" bg="empbbg"> Test Text - srcpair </col>
<col fg="srccmnt" bg="empbg"> Test Text - srccmnt  </col>
<col fg="srcdrct" bg="empbg"> Test Text - srcdrct </col>
<col fg="srcspid" bg="empbg"> Test Text - srcspid </col>
<col fg="srcannot" bg="empbg"> Test Text - srcannot </col>

<b>Source Tags - using subbg background</b>
<col fg="srcnum" bg="subbg"> Test Text - srcnum  </col>
<col fg="srcchar" bg="subbg"> Test Text - srcchar  </col>
<col fg="srcstr" bg="subbg"> Test Text - srcstr  </col>
<col fg="srcid " bg="subbg"> Test Text - srcid   </col>
<col fg="srckw" bg="subbg"> Test Text - srckw </col>
<col fg="srcpair" bg="subbg"> Test Text - srcpair </col>
<col fg="srccmnt" bg="subbg"> Test Text - srccmnt  </col>
<col fg="srcdrct" bg="subbg"> Test Text - srcdrct </col>
<col fg="srcspid" bg="subbg"> Test Text - srcspid </col>
<col fg="srcannot" bg="subbg"> Test Text - srcannot </col>
```

## <span id="DML_Additions_to_the_dbgeng_Interface"></span><span id="dml_additions_to_the_dbgeng_interface"></span><span id="DML_ADDITIONS_TO_THE_DBGENG_INTERFACE"></span>DML Additions to the dbgeng Interface


The [Debugger Engine and Extension APIs](debugger-engine-and-extension-apis.md) provide an interface to use the debugger engine to create custom applications. You can also write custom extensions that will run in WinDbg, KD, CDB, and NTSD. For more information see [Writing DbgEng Extensions](writing-dbgeng-extensions.md). This section describes the available DML enhancements to the debugger engine interfaces.

The dbgeng already has a set of text handling input methods and output interfaces, the use of DML only requires specification of the type of content carried in input and output text.

**Providing DML Content to dbgeng**

The output control flag DEBUG\_OUTCTL\_DML indicates that the text generated by a dbgeng method should be handled as DML content. If this flag is not given the text is treated as plain text context. DEBUG\_OUTCTL\_DML can be used with the following methods.

-   [**IDebugControl4::ControlledOutput**](https://msdn.microsoft.com/library/windows/hardware/ff539248)
-   [**IDebugControl4::ControlledOutputVaList**](https://msdn.microsoft.com/library/windows/hardware/ff539252)
-   [**IDebugControl4::ControlledOutputWide**](https://msdn.microsoft.com/library/windows/hardware/ff539266)
-   [**IDebugControl4::ControlledOutputVaListWide**](https://msdn.microsoft.com/library/windows/hardware/ff539259)

Text given must follow the DML rules for valid characters.

All output routines have been enhanced to allow a new format specifier %\[h|w\]Y{t}. This format specifier has a string pointer as an argument and indicates that the given text is plain text and should be converted to DML format during output processing. This gives callers a simple way of including plain text in DML content without having to pre-convert to DML format themselves. The h and w qualifiers indicate ANSI or Unicode text, as with %s.

The following table summarizes the use of the %Y format specifier.

|        |                                                                                                                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| %Y{t}  | Quoted string. Will convert text to DML if the output format (first arg) is DML.                                                                                                                                                   |
| %Y{T}  | Quoted string. Will always convert text to DML regardless of the output format.                                                                                                                                                    |
| %Y{s}  | Unquoted string. Will convert text to DML if the output format (first arg) is DML.                                                                                                                                                 |
| %Y{S}  | Unquoted string. Will always convert text to DML regardless of the output format.                                                                                                                                                  |
| %Y{as} | ULONG64. Adds either an empty string or 9 characters of spacing for padding the high 32-bit portion of debugger formatted pointer fields. The extra space outputs 9 spaces which includes the upper 8 zeros plus the \` character. |
| %Y{ps} | ULONG64. Extra space for padding debugger formatted pointer fields (includes the upper 8 zeros plus the \` character).                                                                                                             |
| %Y{l}  | ULONG64. Address as source line information.                                                                                                                                                                                       |



This code snippet illustrates the use of the %Y format specifier.

```cpp
HRESULT CALLBACK testout(_In_ PDEBUG_CLIENT pClient, _In_ PCWSTR /*pwszArgs*/)
{
    HRESULT hr = S_OK;

    ComPtr<IDebugControl4> spControl;
    IfFailedReturn(pClient->QueryInterface(IID_PPV_ARGS(&spControl)));

    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{t}: %Y{t}\n", L"Hello <World>");
    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{T}: %Y{T}\n", L"Hello <World>");
    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{s}: %Y{s}\n", L"Hello <World>");
    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{S}: %Y{S}\n", L"Hello <World>");

    spControl->ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{t}: %Y{t}\n", L"Hello <World>");
    spControl->ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{T}: %Y{T}\n", L"Hello <World>");
    spControl->ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{s}: %Y{s}\n", L"Hello <World>");
    spControl->ControlledOutputWide(0, DEBUG_OUTPUT_NORMAL, L"TEXT/NORMAL Y{S}: %Y{S}\n", L"Hello <World>");

    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{a}: %Y{a}\n", (ULONG64)0x00007ffa7da163c0);
    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{as} 64bit   : '%Y{as}'\n", (ULONG64)0x00007ffa7da163c0);
    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{as} 32value : '%Y{as}'\n", (ULONG64)0x1);

    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{ps} 64bit   : '%Y{ps}'\n", (ULONG64)0x00007ffa7da163c0);
    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{ps} 32value : '%Y{ps}'\n", (ULONG64)0x1);

    spControl->ControlledOutputWide(DEBUG_OUTCTL_DML, DEBUG_OUTPUT_NORMAL, L"DML/NORMAL Y{l}: %Y{l}\n", (ULONG64)0x00007ffa7da163c0);

    return hr;

}
```

This sample code would generate the following output.

```dbgcmd
0:004> !testout
DML/NORMAL Y{t}: "Hello <World>"
DML/NORMAL Y{T}: "Hello <World>"
DML/NORMAL Y{s}: Hello <World>
DML/NORMAL Y{S}: Hello <World>
TEXT/NORMAL Y{t}: "Hello <World>"
TEXT/NORMAL Y{T}: &quot;Hello &lt;World&gt;&quot;
TEXT/NORMAL Y{s}: Hello <World>
TEXT/NORMAL Y{S}: Hello &lt;World&gt;
DML/NORMAL Y{a}: 00007ffa`7da163c0
DML/NORMAL Y{as} 64bit   : '         '
DML/NORMAL Y{as} 32value : '         '
DML/NORMAL Y{ps} 64bit   : '        '
DML/NORMAL Y{ps} 32value : '        '
DML/NORMAL Y{l}: [d:\th\minkernel\kernelbase\debug.c @ 443]
```

An additional control flag, DEBUG\_OUTCTL\_AMBIENT\_DML, allows specification of DML context text without modifying any out output control attributes. DEBUG\_OUTCTL\_AMBIENT\_TEXT has been added also as a more-descriptive alias for the previously-existing DEBUG\_OUTCTL\_AMBIENT. The output control flags are defined in dbgeng.h.

```cpp
#define DEBUG_OUTCTL_DML               0x00000020

// Special values which mean leave the output settings
// unchanged.
#define DEBUG_OUTCTL_AMBIENT_DML       0xfffffffe
#define DEBUG_OUTCTL_AMBIENT_TEXT      0xffffffff

// Old ambient flag which maps to text.
#define DEBUG_OUTCTL_AMBIENT           DEBUG_OUTCTL_AMBIENT_TEXT
```

**Providing DML Content From a Debuggee**

The dbgeng has been enhanced to scan debuggee output for a special marker – – that indicates the remaining text in a piece of debuggee output should be treated as DML. The mode change only applies to a single piece of debuggee output, such as a single OutputDebugString string, and is not a global mode switch.

This example shows a mix of plain and DML output.

```text
OutputDebugString(“This is plain text\n<?dml?>This is <col fg=\”emphfg\”>DML</col> text\n”);
```

The output produced, will have a line of plain text followed by a line of DML where the acronym DML is displayed in a different color.

**IDebugOutputCallbacks2**

IDebugOutputCallbacks2 allows dbgeng interface clients to receive full DML content for presentation. IDebugOutputCallbacks2 is an extension of IDebugOutputCallbacks (not IDebugOutputCallbacksWide) so that it can be passed in to the existing SetOutputCallbacks method. The engine will do a QueryInterface for IDebugOutputCallbacks2 to see which interface the incoming output callback object supports. If the object supports IDebugOutputCallbacks2 all output will be sent through the extended IDebugOutputCallbacks2 methods; the basic IDebugOutputCallbacks::Output method will not be used.

The new methods are:

-   IDebugOutputCallbacks2::GetInterestMask – Allows the callback object to describe which kinds of output notifications it wants to receive. The basic choice is between plain text content (DEBUG\_OUTCBI\_TEXT) and DML content (DEBUG\_OUTCBI\_DML). In addition, the callback object can also request notification of explicit flushes (DEBUG\_OUTCBI\_EXPLICIT\_FLUSH).
-   IDebugOutputCallbacks2::Output2 – All IDebugOutputCallbacks2 notifications come through Output2. The Which parameter indicates what kind of notification is coming in while the Flags, Arg and Text parameters carry the notification payload. Notifications include:

    -   DEBUG\_OUTCB\_TEXT – Plain text output. Flags are from DEBUG\_OUTCBF\_\*, Arg is the output mask and Text is the plain text. This will only be received if DEBUG\_OUTCBI\_TEXT was given in the interest mask.

    -   DEBUG\_OUTCB\_DML – DML content output. Flags are from DEBUG\_OUTCBF\_\*, Arg is the output mask and Text is the DML content. This will only be received if DEBUG\_OUTCBI\_DML was given in the interest mask.
    
    -   DEBUG\_OUTCB\_EXPLICIT\_FLUSH – A caller has called FlushCallbacks with no buffered text. Normally when buffered text is flushed the DEBUG\_OUTCBF\_COMBINED\_EXPLICIT\_FLUSH flag will be set, folding the two notifications into one. If no text is buffered a flush-only notification is sent.

 The interest mask flags are defined in dbgeng.h as shown here.

 ```cpp
 // IDebugOutputCallbacks2 interest mask flags.
 //
 // Indicates that the callback wants notifications
// of all explicit flushes.
#define DEBUG_OUTCBI_EXPLICIT_FLUSH 0x00000001
// Indicates that the callback wants
// content in text form.
#define DEBUG_OUTCBI_TEXT           0x00000002
// Indicates that the callback wants
// content in markup form.
#define DEBUG_OUTCBI_DML            0x00000004

#define DEBUG_OUTCBI_ANY_FORMAT     0x00000006
 ```

Note that an output object can register for both text and DML content if it can handle them both. During output processing of the callback the engine will pick the format that reduces conversions, thus supporting both may reduce conversions in the engine. It is not necessary, though, and supporting only one format is the expected mode of operation.

**Automatic Conversions**

The dbgeng will automatically convert between plain text and DML as necessary. For example, if a caller sends DML content to the engine the engine will convert it to plain text for all output clients which only accept plain text. Alternately, the engine will convert plain text to DML for all output callbacks which only accept DML.

## <span id="related_topics"></span>Related topics


[Using Debugger Markup Language](debugger-markup-language-commands.md)










