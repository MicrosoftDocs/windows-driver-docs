---
title: Format of a Text Log Section Body
description: Format of a Text Log Section Body
ms.assetid: 37995fc8-9822-4c2f-ba6a-154a86e1eadf
keywords:
- section body WDK SetupAPI
- formats WDK SetupAPI logging
- text logs WDK SetupAPI , section body
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format of a Text Log Section Body


A *text log section body* contains zero or more log entries that apply to the operation that is associated with a text log section. The format of a section body log entry includes an *entry_prefix* field, a *time_stamp* field, an *event_category* field, an *indentation* field, and a *formatted_message* field, as follows:

*entry_prefix time_stamp event_category indentation formatted_message*

The maximum length, in characters, of a section body log entry is 336.

<a href="" id="entry-prefix-field"></a>*entry_prefix* field  
Indicates whether the log entry is an error message, a warning message, or an information message. The *entry_prefix* field is always present and contains one of the strings that are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>Entry_prefix</em> field</th>
<th align="left">Type of message</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;!!!  &quot;</code></pre></td>
<td align="left"><p>An error message</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;!    &quot;</code></pre></td>
<td align="left"><p>A warning message</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;     &quot;</code></pre></td>
<td align="left"><p>Information message other than an error message or a warning message</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="time-stamp-field"></a>*time_stamp* field  
Indicates the system time when the logged event occurred. The *time_stamp* field is optional and SetupAPI does not include a time stamp by default. However, [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) supports including a time stamp in a log entry. The format of the *time_stamp* field is the same as the format of the *time_stamp* field that is described in [Format of a Text Log Section Header](format-of-a-text-log-section-header.md).

<a href="" id="event-category-field"></a>*event_category* field  
Indicates the category of SetupAPI operation that made the log entry. The *event_category* field is usually present, but is not required. If the *event_category* field is present, it will contain one of the strings that are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>Event_category</em> field strings</th>
<th align="left">SetupAPI operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;...: &quot;</code></pre></td>
<td align="left"><p>Vendor-supplied operation</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;bak: &quot;</code></pre></td>
<td align="left"><p>Backup data</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;cci: &quot;</code></pre></td>
<td align="left"><p>Class installer or co-installer operation</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;cpy: &quot;</code></pre></td>
<td align="left"><p>Copy files</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;dvi: &quot;</code></pre></td>
<td align="left"><p>Device installation</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;flq: &quot;</code></pre></td>
<td align="left"><p>Manage file queues</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;inf: &quot;</code></pre></td>
<td align="left"><p>Manage INF files</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;ndv: &quot;</code></pre></td>
<td align="left"><p>New device wizard</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;prp: &quot;</code></pre></td>
<td align="left"><p>Manage device and driver properties</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;reg: &quot;</code></pre></td>
<td align="left"><p>Manage registry settings</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;set: &quot;</code></pre></td>
<td align="left"><p>General setup</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;sig: &quot;</code></pre></td>
<td align="left"><p>Verify digital signatures</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;sto: &quot;</code></pre></td>
<td align="left"><p>Manage the driver store</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;ui : &quot;</code></pre></td>
<td align="left"><p>Manage user interface dialog boxes</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;ump: &quot;</code></pre></td>
<td align="left"><p>User-mode PnP manager</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="indentation-field"></a>*indentation* field  
Consists of a sequence of zero or more *indentation units*, where an indentation unit is a monospace string that contains five spaces. The *indentation* field is optional and SetupAPI does not include indentation by default. **SetupWriteTextLog** supports changing the number of indentation units that are included in a log entry.

<a href="" id="formatted-message-field"></a>*formatted_message* field  
Contains the specific information that applies to the log entry.

The section body entries that are logged depend on the event level that is set for the log and the category levels that are enabled for the log. For more information about these settings, see [SetupAPI Logging Registry Settings](setupapi-logging-registry-settings.md).

When SetupAPI creates a section that groups operations that apply to a device installation, it also recursively groups section body log entries in subsections. SetupAPI distinguishes subsections by the way it annotates and indents log entries. One such subsection appears in the following excerpt from a typical device installation section. The subsection begins with the log entry "dvi: {Build Driver List}" and ends with the log entry "dvi: {Build Driver List - exit(0x00000000)}". This subsection shows a typical sequence of log entries that include the *entry_prefix*, *event_category*, *indentation*, and *formatted_message* fields. The SetupAPI operations that wrote the log entries also created the indentation and supplied the content of the formatted messages. The event level for this example was set to TXTLOG_DETAILS and all category levels were enabled for this example.

```cpp
>>>  [Device Install - PCI\VEN_104C&DEV_8019&SUBSYS_8010104C&REV_00\3&61aaa01&0&38]
>>>  2005/02/13 22:06:28.109: Section start
...
 Deleted section body log entries
...
     dvi: {Build Driver List}
     dvi:      Enumerating all INFs...
     dvi:      Found driver match:
     dvi:           HardwareID - PCI\VEN_104C&DEV_8019
     dvi:           InfName    - C:\WINDOWS\inf\1394.inf
     dvi:           DevDesc    - Texas Instruments OHCI Compliant IEEE 1394 Host Controller
     dvi:           DrvDesc    - Texas Instruments OHCI Compliant IEEE 1394 Host Controller
     dvi:           Provider   - Microsoft
     dvi:           Mfg        - Texas Instruments
     dvi:           InstallSec - TIOHCI_Install
     dvi:           ActualSec  - TIOHCI_Install.NT
 dvi:           Rank       - 0x00002001
     dvi:           DrvDate    - 10/01/2002
 dvi:           Version    - 6.0.5033.0 
!!!  inf:      InfCache: Error flagging 1394.inf for match string pci\ven_104c&dev_8019
     dvi: {Build Driver List - exit(0x00000000)}
...
 Deleted section body log entries 
...
<<<  [2005/02/13 22:06:29.000: Section end]
<<<  [Exit Status(0x00000000)]
```

 

 





