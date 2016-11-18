---
title: Format of a Text Log Section Header
description: Format of a Text Log Section Header
ms.assetid: ec46a540-e888-426d-85fc-6ad2d756c7b8
keywords: ["section headers WDK SetupAPI logging", "formats WDK SetupAPI logging", "text logs WDK SetupAPI , section header"]
---

# Format of a Text Log Section Header


A *text log section header* consists of two log entries. The format of the first entry includes a "&gt;&gt;&gt; " prefix string, followed by a *section\_title* field and an *instance\_identifier* field. In the following example, the text in italic font style is a placeholder for section-specific text that is supplied by a section creator, and the text in bold font style is supplied by SetupAPI logging.

```
>>>  [section_title - instance_identifier] 
```

The *section\_title* field is always present and provides a title for the operation that is associated with the section.

The *instance\_identifier* provides an identifier that, ideally, uniquely identifies the instance of the operation. If the *instance\_identifier* field is not present, the format of the first entry of a section header is as follows:

```
>>>  [section_title] 
```

The format of the second entry of a section header includes a "&gt;&gt;&gt; " prefix string, followed by a *time\_stamp* field and a "Section start" string, as follows:

```
>>>  time_stamp Section start
```

The format of the *time\_stamp* field is as follows:

```
yyyy/mm/dd hh:mm:ss.sss:
```

where the *time\_stamp* subfields are as follows:

-   *yyyy* is the 4-digit year, *mm* is the 2-digit month, and *dd* is the 2-digit day

-   The local time is based on a 24-hour clock, where *hh* is the 2-digit hour, *mm* is the 2-digit minute, *ss* is the 2-digit number of seconds, and sss is the 3-digit number of milliseconds.

The following is an example of a typical section header that the user-mode Plug and Play (PnP) manager would create to group installation operations for a PCI device. The *section\_title* field is "Device Install," the *instance\_identifier* field is the device instance identifier "PCI\\VEN\_104C&DEV\_8019&SUBSYS\_8010104C&REV\_00\\3&61aaa01&0&38," and the *time\_stamp* field is "2005/02/13 22:06:28.109:."

```
>>>  [Device Install - PCI\VEN_104C&DEV_8019&SUBSYS_8010104C&REV_00\3&61aaa01&0&38]
>>>  2005/02/13 22:06:28.109: Section start
```

 

 





