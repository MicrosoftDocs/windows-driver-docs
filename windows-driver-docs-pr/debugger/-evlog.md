---
title: evlog
description: The evlog extension displays, changes, or backs up the event log.
ms.assetid: 72038e3e-ff12-4df1-8f55-c02258d764aa
keywords: ["event log", "evlog Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- evlog
api_type:
- NA
ms.localizationpriority: medium
---

# !evlog


The **!evlog** extension displays, changes, or backs up the event log.

```dbgcmd
!evlog addsource [-d] [-s Source] [-t Type] [-f MsgFile] 
!evlog backup [-d] [-l EventLog] [-f BackupFile] 
!evlog clear [-!] [-d] [-l EventLog] [-f BackupFile] 
!evlog info 
!evlog option [-d] [-!] [-n Count] [ -l EventLog [ -+ | -r RecordBound ]] [-o Order] [-w Width] 
!evlog read [-d] [-l EventLog] [-s Source] [-e ID] [-c Category] [-t Type] [-n Count] [-r Record] 
!evlog report [-s Source] [-e ID] [-c Category] [-t Type] Message 
!evlog [Option] -?
```

## <span id="ddk__evlog_dbg"></span><span id="DDK__EVLOG_DBG"></span>Parameters


<span id="_______addsource______"></span><span id="_______ADDSOURCE______"></span> **addsource**   
Adds an event source to the registry. By default, this only adds events from the DebuggerExtensions source (to support **!evlog report**).

<span id="_______backup______"></span><span id="_______BACKUP______"></span> **backup**   
Makes a backup of the specified event log and writes it to a file.

<span id="_______clear______"></span><span id="_______CLEAR______"></span> **clear**   
Erases the specified event log, and optionally creates a file recording its old contents.

<span id="_______info______"></span><span id="_______INFO______"></span> **info**   
Displays summary information about the event log.

<span id="_______option______"></span><span id="_______OPTION______"></span> **option**   
Sets the default search options. These options will be used in future **!evlog read** commands.

<span id="_______read______"></span><span id="_______READ______"></span> **read**   
Displays a list of events logged to the specified event log. Details of this display -- such as the number of records displayed and the chronological order of the display -- can be controlled by the **!evlog read** parameters or by a previous use of **!evlog option**.

<span id="_______report______"></span><span id="_______REPORT______"></span> **report**   
Writes an event record to the application event log.

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
Specifies that all default values should be used. The **-d** option is only required if you are omitting all other parameters. However, with the **!evlog option** command this option displays the existing default settings.

<span id="_______-_______"></span> **-!**   
With **!evlog option**, this resets all defaults. With **!evlog clear**, this prevents a backup file from being written.

<span id="_______Source______"></span><span id="_______source______"></span><span id="_______SOURCE______"></span> *Source*   
Specifies the event source. The default value is **DebuggerExtensions**.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the success type. Possible *Type* values are 1 (Error), 2 (Warning), 4 (Information), 8 (Audit\_Success), or 16 (Audit\_Failure). A value of 0 represents Success. For **!evlog read** and **!evlog report**, the default is Success (0). For **!evlog addsource**, these bits can be combined, and the default is all bits (31).

<span id="_______MsgFile______"></span><span id="_______msgfile______"></span><span id="_______MSGFILE______"></span> *MsgFile*   
Specifies the path and file name of the message file. If the path is omitted, the directory of the current Uext.dll is used.

<span id="_______EventLog______"></span><span id="_______eventlog______"></span><span id="_______EVENTLOG______"></span> *EventLog*   
For **!evlog read**, **!evlog backup**, and **!evlog clear**, *EventLog* specifies the event log from which to read. The possible values are **Application**, **System**, and **Security**. The default is **Application**.

For **!evlog option**, *EventLog* specifies the event log whose maximum count is to be set. The possible values are **All**, **Application**, **System**, and **Security**. The default is **All**.

<span id="_______BackupFile______"></span><span id="_______backupfile______"></span><span id="_______BACKUPFILE______"></span> *BackupFile*   
Specifies the path and file name of the backup file. The default location is the current directory. The default file name is *EventLog*\_backup.evt, where *EventLog* is the event log used in this command. If this file already exists, the command will be terminated.

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the maximum number of records to retrieve. The default is 20.

<span id="_______-_______"></span> **-+**   
Specifies that the current maximum record number should be the highest record number retrieved in future **!evlog read** commands. (In other words, no records will be shown as long as the search is performed forward.)

<span id="_______RecordBound______"></span><span id="_______recordbound______"></span><span id="_______RECORDBOUND______"></span> *RecordBound*   
Specifies the highest record number to retrieve in future **!evlog read** commands. If zero is specified, no bound is set -- this is the default.

<span id="_______Record______"></span><span id="_______record______"></span><span id="_______RECORD______"></span> *Record*   
If **-n** **** *Count* is not included, **-r** **** *Record* specifies the record number to retrieve. If **-n** **** *Count* is included, *Record* specifies the record number at which the display should begin.

<span id="_______Order______"></span><span id="_______order______"></span><span id="_______ORDER______"></span> *Order*   
Specifies the search order, either **Forwards** or **Backwards**. The default is **Forwards**. A backward search order causes searches to start from the most recent record logged to the event log, and continue in reverse-chronological order as matching records are found.

<span id="_______Width______"></span><span id="_______width______"></span><span id="_______WIDTH______"></span> *Width*   
Specifies the data display width, in characters. This is the width displayed in the Data section. The default is 8 characters.

<span id="_______ID______"></span><span id="_______id______"></span> *ID*   
Specifies the prefix to display before the event. Possible values are 0 (no prefix), 1000 (Information), 2000 (Success), 3000 (Warning), and 4000 (Error).

The default is 0.

<span id="_______Category______"></span><span id="_______category______"></span><span id="_______CATEGORY______"></span> *Category*   
Specifies the event category.

Possible values are 0 (no category), 1 (Devices), 2 (Disk), 3 (Printers), 4 (Services), 5 (Shell), 6 (System\_Event), and 7 (Network). The default is 0.

<span id="_______Message______"></span><span id="_______message______"></span><span id="_______MESSAGE______"></span> *Message*   
Specifies a text message to add to the event description.

<span id="_______Option______"></span><span id="_______option______"></span><span id="_______OPTION______"></span> *Option*   
Specifies the **!evlog** option whose help text is to be displayed.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension or one of its options in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
</tbody>
</table>

 

The **!evlog** extension can only be used during live debugging.

Remarks
-------

After you have added an event source to the registry with **!evlog addsource**, you can view the values with [**!dreg**](-dreg.md). For example:

```dbgcmd
0:000> !dreg hklm\system\currentcontrolset\services\eventlog\Application\<source>!* 
```

The **!evlog option** command is used to set new defaults for the **!evlog read** command. This lets you avoid retyping all the parameters every time you use **!evlog read**. Setting a maximum record bound with the **-+** parameter or the **-r** **** *Records* parameter allows you to terminate all searches after a known record number is encountered. This can be useful if you are only interested in all records logged after a certain event.

Before using **!evlog report**, you should use **!evlog addsource** to configure an event source in the registry. After this has been configured, the event viewer will recognize the various event IDs.

Here is an example of the **!evlog info** extension:

```dbgcmd
## 0:000> !evlog info -?

Application Event Log:
# Records       : 4362
  Oldest Record # : 1
  Newest Record # : 4362
##   Event Log Full  : false

System Event Log:
# Records       : 2296
  Oldest Record # : 1
  Newest Record # : 2296
##   Event Log Full  : false

Security Event Log:
# Records       : 54544
  Oldest Record # : 1
  Newest Record # : 54544
##   Event Log Full  : false


0:000> !evlog option -n 4
## Default EvLog Option Settings:

Max Records Returned: 4
Search Order:         Backwards
## Data Display Width:   8

Bounding Record Numbers:
  Application Event Log: 0
  System Event Log:      0
##   Security Event Log:    0


0:000> !evlog read -l application
-------------- 01 --------------
Record #: 4364

Event Type:      Error (1)
Event Source:    Userenv
Event Category:  None (0)
Event ID:        1000 (0xC00003E8)
Date:            06/06/2002
Time:            18:03:17
Description:     (1 strings)
The Group Policy client-side extension Security was passed flags (17) and returned a failure status code of (87).

-------------- 02 --------------
Record #: 4363

Event Type:      Warning (2)
Event Source:    SceCli
Event Category:  None (0)
Event ID:        1202 (0x800004B2)
Date:            06/06/2002
Time:            18:03:17
Description:     (1 strings)
0x57 : The parameter is incorrect.
Please look for more details in TroubleShooting section in Security Help.

-------------- 03 --------------
Record #: 4362

Event Type:      Error (1)
Event Source:    Userenv
Event Category:  None (0)
Event ID:        1000 (0xC00003E8)
Date:            06/06/2002
Time:            16:04:08
Description:     (1 strings)
The Group Policy client-side extension Security was passed flags (17) and returned a failure status code of (87).

-------------- 04 --------------
Record #: 4361

Event Type:      Warning (2)
Event Source:    SceCli
Event Category:  None (0)
Event ID:        1202 (0x800004B2)
Date:            06/06/2002
Time:            16:04:08
Description:     (1 strings)
0x57 : The parameter is incorrect.
Please look for more details in TroubleShooting section in Security Help.
WARNING: Max record count (4) exceeded, increase record count to view more
```

 

 





