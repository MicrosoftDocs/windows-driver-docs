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
>>>  [Device Install - PCI\VEN_104C&amp;DEV_8019&amp;SUBSYS_8010104C&amp;REV_00\3&amp;61aaa01&amp;0&amp;38]
>>>  2005/02/13 22:06:28.109: Section start
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Format%20of%20a%20Text%20Log%20Section%20Header%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




