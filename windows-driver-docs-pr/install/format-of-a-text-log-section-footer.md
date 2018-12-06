---
title: Format of a Text Log Section Footer
description: Format of a Text Log Section Footer
ms.assetid: 3b804934-a695-4091-a3ef-03f7598cbe63
keywords:
- section footer WDK SetupAPI
- formats WDK SetupAPI logging
- text logs WDK SetupAPI , section footer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format of a Text Log Section Footer


A *text log section footer* closes a text log section. A section footer consists of two entries. The format of the first entry of a section footer includes a "&lt;&lt;&lt; " prefix, followed by a *time_stamp* field and the string "Section end".

```cpp
<<<  [time_stamp Section end]
```

The format of the *time_stamp* field is the same as that described in [Format of a Text Log Section Header](format-of-a-text-log-section-header.md).

The format of the second entry includes a "&lt;&lt;&lt; " prefix, followed by the string "Exit" and a *status* field. In the following example, the text in italic font style is a placeholder for section-specific text that is supplied by a section creator and the text in bold font style is supplied by SetupAPI logging:

```cpp
<<<  [Exit Status(status)]
```

The format of the status field is "0x*hhhhhhhh*", where *hhhhhhhh* is 8-digit hexadecimal number.

If the status field is not present, the format of the first line is as follows:

```cpp
<<<  [Exit]
```

The following is an example of a section footer that specifies an exit status of "0x00000000" and includes a *time_stamp* field.

```cpp
<<<  [2005/02/13 22:06:28.109: Section end]
<<<  [Exit Status(0x00000000)]
```

 

 





