---
title: Writing Indented Log Entries
description: Writing Indented Log Entries
ms.assetid: 8ce6b433-a004-43f6-9481-9c23c5e7e8da
keywords:
- indented log entries WDK SetupAPI
- formats WDK SetupAPI logging
- text logs WDK SetupAPI , indented log entries
- SetupWriteTextLog
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing Indented Log Entries


As described in [Format of a Text Log Section Body](format-of-a-text-log-section-body.md), the format of a section body log entry in a [SetupAPI text log](setupapi-text-logs.md) consists of the following fields:

```cpp
entry_prefix time_stamp event_category indentation formatted_message
```

You can use the *indentation* field in log entries to indent the *formatted_message* fields in order to make the log entries easier to read and understand. The amount of indentation in an indentation field depends on the indentation depth that is set for the section. The indentation depth is the number of indentation units, where an indentation unit is five monospace text spaces. For example, an indentation depth of 1 results in an indentation of 5 spaces, an indentation depth of 2 results in an indentation of 10 spaces, and so on. The minimum indentation depth is zero and the maximum indentation depth is 16.

By default, the indentation depth of a section is zero. If the indentation depth is zero, the *formatted_message* field will not be indented. If an application increases the indentation depth to write a sequence of indented section entries, the application must also write a corresponding set of section entries to reset the indentation depth to zero before the application can subsequently write additional section entries that are not indented.

To change the indentation depth for a section, call a SetupAPI logging function and use a bitwise OR between one of following system-defined manifest constants and the flags parameter that is supplied to the SetupAPI logging function.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Manifest constant</th>
<th align="left">Change in indentation depth</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>TXTLOG_DEPTH_INCR</p></td>
<td align="left"><p>The indentation depth is increased by 1 for the current log entry and all subsequent log entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>TXTLOG_DEPTH_DECR</p></td>
<td align="left"><p>The indentation depth is decreased by 1 for the current log entry and all subsequent log entries.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TXTLOG_TAB_1</p></td>
<td align="left"><p>The indentation depth is increased by 1 only for the current log entry.</p></td>
</tr>
</tbody>
</table>

 

For example, the following sequence of calls to [**SetupWriteTextLog**](https://msdn.microsoft.com/library/windows/hardware/ff552218) writes a sequence of indented log entries after the section header whose *section_title* field is "Indentation Example" and whose *instance_identifier* field is "Instance 0".

```cpp
// The LogToken value was previously returned by a call to 
// SetupGetThreadLogToken.
// The LogToken value specifies a section in one of the text logs.

DWORD Category = TXTLOG_VENDOR; 
DWORD Flags = TXTLOG_DETAILS;

SetupWriteTextLog(LogToken, Category, Flags, TEXT("Subsection A"));

// Additional SetupWriteTextLog calls that write entries at Subsection A indentation level

SetupWriteTextLog(LogToken, Category, Flags | TXTLOG_DEPTH_INCR, TEXT("Subsection A.1"));

// Additional SetupWriteTextLog calls that write entries at Subsection A.1 indentation level

SetupWriteTextLog(LogToken, Category, Flags | TXTLOG_DEPTH_INCR, TEXT("Subsection A.1.1"));

// Additional SetupWriteTextLog calls that write entries at Subsection A.1.1 indentation level

SetupWriteTextLog(LogToken, Category, Flags, TEXT("End of Subsection A.1.1"));

// Additional SetupWriteTextLog calls that write entries at Subsection A.1 indentation level

SetupWriteTextLog(LogToken, Category, Flags | TXTLOG_DEPTH_DECR, TEXT("End of Subsection A.1"));

// Additional SetupWriteTextLog calls that write entries at Subsection A indentation level
SetupWriteTextLog(LogToken, Category, Flags | TXTLOG_DEPTH_DECR, TEXT("End of Subsection A"));
```

If the event level for the text log is greater than or equal to TXTLOG_DETAILS and the event category TXTLOG_VENDOR is enabled for the text log, the previous code would write the following log entries after the section header.

In the following example, ellipsis (...) represents zero or more additional log entries at the same level of indentation as the previous log entry. The time stamp would be replaced by an actual time stamp.

```cpp
>>>  [Indentation Example - Instance 0]
>>>  2005/02/13 22:06:28.109: Section start
        : Subsection A
...
        :      Subsection A.1
...
        :           Subsection A.1.1
...
        :           End Subsection A.1.1
...
        :      End of Subsection A.1
...
        : End of Subsection A
```

For another example of indented section entries that was taken from an actual text log, see [Format of a Text Log Section Body](format-of-a-text-log-section-body.md).

 

 





