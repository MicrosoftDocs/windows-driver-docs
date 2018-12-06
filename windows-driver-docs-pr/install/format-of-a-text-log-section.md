---
title: Format of a Text Log Section
description: Format of a Text Log Section
ms.assetid: e0f7227c-6cd8-4c66-a38b-104f222847bc
keywords:
- sections WDK SetupAPI logging
- formats WDK SetupAPI logging
- text logs WDK SetupAPI , sections
- SetupAPI logging WDK Windows Vista , text log sections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format of a Text Log Section


A *text log section* includes a section header that opens the section, a section body that includes a sequence of log entries that apply to the section operation, and a section footer that closes the section. Section entries appear in a section in the same order in which they are written to the section.

The following example of a text log section shows the general format of a typical section, where the fields in italic font style are placeholders for section-specific text, and the remaining text in bold font style is generic text supplied by SetupAPI. The first two log entries comprise the section header and the last two log entries comprise the section footer.

```cpp
>>>  [section_title - instance_identifer]
>>> time_stamp Section start
 section body log entry
 section body log entry
 section body log entry
<<<  [time_stamp: Section end]
<<<  [Exit Status(status_value)]
```

The section body entries that are logged depend on the event level that is set for the log and the category levels that are enabled for the log. For more information about these settings, see [SetupAPI Logging Registry Settings](setupapi-logging-registry-settings.md).

The following is a typical example of a text log section that the Plug and Play (PnP) manager created to log entries that pertained to the installation of a PCI device. In the section header, the *section_title* field is "Device Install," the *instance_identifier* field is the device instance identifier "PCI\\VEN_104C&DEV_8019&SUBSYS_8010104C&REV_00\\3&61aaa01&0&38," and the *time_stamp* field is "2005/02/13 22:06:28.109:." In the section footer, the *status_value* field is "0x00000000" and the *time_stamp* field is "2005/02/13 22:06:20.000:." Only the first three section body log entries are included in this example. The event level for this example was set to TXTLOG_DETAILS and all category levels were enabled for this example.

```cpp
>>>  [Device Install - PCI\VEN_104C&DEV_8019&SUBSYS_8010104C&REV_00\3&61aaa01&0&38]
>>>  2005/02/13 22:06:20.000: Section start
     ndv: Retrieving device info...
     ndv: Setting device parameters...
     ndv: Building driver list...
...  
...  additional section body log entries, which are not shown
...  
<<<  [2005/02/13 22:06:28.109: Section end]
<<<  [Exit Status(0x00000000)]
```

For detailed information about the content and format of a text log section, see [Format of a Text Log Section Header](format-of-a-text-log-section-header.md), [Format of a Text Log Section Body](format-of-a-text-log-section-body.md), and [Format of a Text Log Section Footer](format-of-a-text-log-section-footer.md).

 

 





