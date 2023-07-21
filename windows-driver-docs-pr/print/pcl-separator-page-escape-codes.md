---
title: PCL separator page escape codes
description: PCL separator page escape codes
keywords:
- PCL separator page escape codes WDK PCL XL
- PCL XL vector graphics WDK Unidrv , separator page escape codes
- escape codes WDK PCL XL
ms.date: 07/18/2023
---

# PCL separator page escape codes

[!include[Print Support Apps](../includes/print-support-apps.md)]

The escape codes shown in the following table can be used when you create a PCL separator page.

| Escape code | Meaning |
|--|--|
| \ | The first line of the separator file must contain only this character. The separator file interpreter reads the separator file command as a delimiter. |
| \n | Skips the number of lines specified by *n* (from 0 through 9). Skipping 0 lines moves printing to the next line. |
| \B\M | Prints text in double-width block characters until \U is encountered. |
| \B\S | Prints text in single-width block characters until \U is encountered. |
| \D | Prints the date the job was printed. The time is displayed in the format specified under Regional Options (Windows 2000) or Regional and Language Options (Windows XP and later) in Control Panel. |
| \E | Ejects a page from the printer. Use this code to start a new separator page or to end the separator page file. If you get an extra blank separator page when you print, remove this code from your separator page file. |
| \F*pathname* | Prints the contents of the file specified by *pathname*, starting on an empty line. The contents of this file are copied directly to the printer without processing. |
| \H*nn* | Sets a printer-specific control sequence, where *nn* is a hexadecimal ASCII code sent directly to the printer. See your printer manual to determine the specific numbers. |
| \I | Prints the job number. |
| \L*xxx* | Prints the string of text that appears after the \L escape code. If you enter \LTest, the text "Test" appears in the separator page. |
| \N | Prints the user name of the person who submitted the job. |
| \U | Turns off block character printing. |
| \W*nn* | Sets the width of the separator page. The default width is 80 characters, and the maximum width is 256 characters. Characters beyond this width are deleted. |

After the local print provider passes a job through the print processor and the separator page processor, it sends the job from the spooler to the appropriate port print monitor.
