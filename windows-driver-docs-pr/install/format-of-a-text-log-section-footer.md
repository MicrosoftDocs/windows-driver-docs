---
title: Format of a Text Log Section Footer
description: Format of a Text Log Section Footer
ms.assetid: 3b804934-a695-4091-a3ef-03f7598cbe63
keywords: ["section footer WDK SetupAPI", "formats WDK SetupAPI logging", "text logs WDK SetupAPI , section footer"]
---

# Format of a Text Log Section Footer


A *text log section footer* closes a text log section. A section footer consists of two entries. The format of the first entry of a section footer includes a "&lt;&lt;&lt; " prefix, followed by a *time\_stamp* field and the string "Section end".

```
<<<  [time_stamp Section end]
```

The format of the *time\_stamp* field is the same as that described in [Format of a Text Log Section Header](format-of-a-text-log-section-header.md).

The format of the second entry includes a "&lt;&lt;&lt; " prefix, followed by the string "Exit" and a *status* field. In the following example, the text in italic font style is a placeholder for section-specific text that is supplied by a section creator and the text in bold font style is supplied by SetupAPI logging:

```
<<<  [Exit Status(status)]
```

The format of the status field is "0x*hhhhhhhh*", where *hhhhhhhh* is 8-digit hexadecimal number.

If the status field is not present, the format of the first line is as follows:

```
<<<  [Exit]
```

The following is an example of a section footer that specifies an exit status of "0x00000000" and includes a *time\_stamp* field.

```
<<<  [2005/02/13 22:06:28.109: Section end]
<<<  [Exit Status(0x00000000)]
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Format%20of%20a%20Text%20Log%20Section%20Footer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




