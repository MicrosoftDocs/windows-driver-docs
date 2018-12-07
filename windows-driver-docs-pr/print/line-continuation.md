---
title: Line Continuation
description: Line Continuation
ms.assetid: ee4dbb3d-ba9d-45bb-82dd-ecee4682ae63
keywords:
- GPD file entries WDK Unidrv , line continuations
- line continuations WDK GPD files
- continued lines WDK GPD files
- continuation character WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Line Continuation





[GPD file entries](gpd-file-entries.md) that are too long to fit onto a single line can be continued on subsequent lines. To continue an entry, each line after the first must be preceded by a plus sign (+). The plus sign must be the first character on the line, without preceding white space, as illustrated in the following example:

```cpp
*DeviceFonts:
+    LIST(
+        =RC_FONT_Courier_10pt_regular,
+        =RC_FONT_CGTimes_regular,
+        =RC_FONT_Univers_regular,
+        =RC_FONT_Univers_condensed_regular,
+        =RC_FONT_Antique_Olive_regular,
+        =RC_FONT_Albertus_Medium,
+        =RC_FONT_Albertus_Extra_Bold,
+        =RC_FONT_Courier_regular,
+        =RC_FONT_Letter_Gothic_regular,
+        =RC_FONT_Wingdings)
```

You do not need to use a line continuation character at the beginning of the following lines:

-   Lines that start with an asterisk.

-   Lines that start with a left brace.

 

 




