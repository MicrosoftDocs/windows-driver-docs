---
title: Line Continuation
author: windows-driver-content
description: Line Continuation
ms.assetid: ee4dbb3d-ba9d-45bb-82dd-ecee4682ae63
keywords:
- GPD file entries WDK Unidrv , line continuations
- line continuations WDK GPD files
- continued lines WDK GPD files
- continuation character WDK GPD files
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Line Continuation


## <a href="" id="ddk-line-continuation-gg"></a>


[GPD file entries](gpd-file-entries.md) that are too long to fit onto a single line can be continued on subsequent lines. To continue an entry, each line after the first must be preceded by a plus sign (+). The plus sign must be the first character on the line, without preceding white space, as illustrated in the following example:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Line%20Continuation%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


