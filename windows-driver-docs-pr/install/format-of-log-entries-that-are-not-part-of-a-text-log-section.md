---
title: Format of Log Entries That Are Not Part of a Text Log Section
description: Format of Log Entries That Are Not Part of a Text Log Section
ms.assetid: c2c7567e-dfb4-49d3-acc9-034f6544633e
keywords:
- formats WDK SetupAPI logging
- text logs WDK SetupAPI , entries not part of section
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format of Log Entries That Are Not Part of a Text Log Section


A text log can contain log entries that are not part of a text log header or a text log section. Such entries are not associated with any section and, in general, are interspersed between sections. The format of such log entries consists of an *entry*_*prefix* field, a *time_stamp* field, an *event_category* field, and a *formatted_message* field, as follows:

*entry_prefix time_stamp event_category formatted_message*

The following list describes the fields of a log entry:

<a href="" id="entry-prefix-field"></a>*entry_prefix* field  
Indicates the message type. The *entry_prefix* field is always present and contains one of the strings that are listed in the left-hand column of the following table, where the meaning of the string is indicated in the right-hand column.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry_prefix field</th>
<th align="left">Message type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;!!!  &quot;</code></pre></td>
<td align="left"><p>An error message in a text log</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;!    &quot;</code></pre></td>
<td align="left"><p>A warning message in a text log</p></td>
</tr>
<tr class="odd">
<td align="left"><pre space="preserve"><code>&quot;   . &quot;</code></pre></td>
<td align="left"><p>An information message in a text log (other than an error message or a warning message)</p></td>
</tr>
<tr class="even">
<td align="left"><pre space="preserve"><code>&quot;     &quot;</code></pre></td>
<td align="left"><p>An information message in the application installation text log (other than an error message or a warning message)</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="time-stamp-field"></a>*time_stamp* field  
Indicates the system time when the logged event occurred. The *time_stamp* field is optional and will be present only if an installation application requested that a time stamp be included for a log entry. The format of the *time_stamp* field is the same as that described in [Format of a Text Log Section Header](format-of-a-text-log-section-header.md).

<a href="" id="event-category-field"></a>*event_category* field  
Indicates the category of the SetupAPI operation that made the log entry. The *event_category* field is usually present, but is not required. If present, the *event_category* field contains one of the strings that are listed in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md).

<a href="" id="formatted-message"></a>*formatted_message*  
Contains the information that is specific to the log entry. The *formatted_message* field is generally present, but is not required.

**Note**  The maximum length, in characters, of a log entry is 336.

 

The following example of text log entries is taken from a device installation text log. In the example, the first two log entries are not part of a text log section. The user-mode Plug and Play (PnP) manager wrote these log entries in the device installation text log to indicate the start of a server-side installation of a PCI device. The server-side installation, in turn, created the text log section that is indicated by the text log section header that follows the first two log entries in the example.

Be aware that the *event_category* field for the first two log entries indicates that the user-mode PnP manager wrote these log entries.

```cpp
   . ump: Start service install for: PCI\VEN_104C&DEV_8019&SUBSYS_8010104C&REV_00\3&61aaa01&0&38
   . ump: Creating Install Process: rundll32.exe

>>>  [Device Install - PCI\VEN_104C&DEV_8019&SUBSYS_8010104C&REV_00\3&61aaa01&0&38]
>>>  2005/02/13 22:06:28.109: Section start
```

 

 





