---
title: Format of Log Entries That Are Not Part of a Text Log Section
description: Format of Log Entries That Are Not Part of a Text Log Section
ms.assetid: c2c7567e-dfb4-49d3-acc9-034f6544633e
keywords: ["formats WDK SetupAPI logging", "text logs WDK SetupAPI , entries not part of section"]
---

# Format of Log Entries That Are Not Part of a Text Log Section


A text log can contain log entries that are not part of a text log header or a text log section. Such entries are not associated with any section and, in general, are interspersed between sections. The format of such log entries consists of an *entry*\_*prefix* field, a *time\_stamp* field, an *event\_category* field, and a *formatted\_message* field, as follows:

*entry\_prefix time\_stamp event\_category formatted\_message*

The following list describes the fields of a log entry:

<a href="" id="entry-prefix-field"></a>*entry\_prefix* field  
Indicates the message type. The *entry\_prefix* field is always present and contains one of the strings that are listed in the left-hand column of the following table, where the meaning of the string is indicated in the right-hand column.

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

 

<a href="" id="time-stamp-field"></a>*time\_stamp* field  
Indicates the system time when the logged event occurred. The *time\_stamp* field is optional and will be present only if an installation application requested that a time stamp be included for a log entry. The format of the *time\_stamp* field is the same as that described in [Format of a Text Log Section Header](format-of-a-text-log-section-header.md).

<a href="" id="event-category-field"></a>*event\_category* field  
Indicates the category of the SetupAPI operation that made the log entry. The *event\_category* field is usually present, but is not required. If present, the *event\_category* field contains one of the strings that are listed in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md).

<a href="" id="formatted-message"></a>*formatted\_message*  
Contains the information that is specific to the log entry. The *formatted\_message* field is generally present, but is not required.

**Note**  The maximum length, in characters, of a log entry is 336.

 

The following example of text log entries is taken from a device installation text log. In the example, the first two log entries are not part of a text log section. The user-mode Plug and Play (PnP) manager wrote these log entries in the device installation text log to indicate the start of a server-side installation of a PCI device. The server-side installation, in turn, created the text log section that is indicated by the text log section header that follows the first two log entries in the example.

Be aware that the *event\_category* field for the first two log entries indicates that the user-mode PnP manager wrote these log entries.

```
   . ump: Start service install for: PCI\VEN_104C&amp;DEV_8019&amp;SUBSYS_8010104C&amp;REV_00\3&amp;61aaa01&amp;0&amp;38
   . ump: Creating Install Process: rundll32.exe

>>>  [Device Install - PCI\VEN_104C&amp;DEV_8019&amp;SUBSYS_8010104C&amp;REV_00\3&amp;61aaa01&amp;0&amp;38]
>>>  2005/02/13 22:06:28.109: Section start
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Format%20of%20Log%20Entries%20That%20Are%20Not%20Part%20of%20a%20Text%20Log%20Section%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




