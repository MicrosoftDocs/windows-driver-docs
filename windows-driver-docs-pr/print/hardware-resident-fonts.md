---
title: Hardware-Resident Fonts
description: Hardware-Resident Fonts
ms.assetid: 359735c2-bfa3-4c32-82a5-1d455c4eacb1
keywords:
- printer font descriptions WDK Unidrv , hardware-resident fonts
- hardware-resident fonts WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware-Resident Fonts





If your printer contains hardware-resident fonts, you must provide specifications of font metrics for these fonts within .ufm or .ifi files.

Each hardware resident font is described in a separate .ufm or .ifi file. To make the these files available to Unidrv, do the following:

-   In the printer's resource DLL, specify .ufm files by using the RC\_UFM resource type, and specify .ifi files by using the RC\_FONT resource type.

-   In the printer's GPD file, use the \*ResourceDLL attribute to specify the resource DLL's name.

-   In the printer's GPD file, use a \*DeviceFonts entry to specify the resource identifiers associated with the RC\_UFM or RC\_FONT entries in the resource DLL.

The format of the \*DeviceFonts entry is as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>*DeviceFonts: LIST (</strong><em>FontResourceID</em><strong>,</strong> <em>FontResourceID</em><strong>,</strong> ...<strong>)</strong></p></td>
</tr>
</tbody>
</table>

 

where *FontResourceID* is the RC\_UFM resource identifier associated with a .ufm file, or the RC\_FONT resource identifier associated with an .ifi file.

Following is an example:

```cpp
*% Assume that RC_FONT_xxx ids are references to 
*% value macros defined by the GPD file creator.
*DeviceFonts: LIST(=RC_FONT_COURIER10, =RC_FONT_ARIALR,
+                  =RC_FONT_ARIALI, =RC_FONT_ARIALB, 
+                  =RC_FONT_ARIALBI, =RC_FONT_TIMESNRR,
+                  =RC_FONT_TIMESNRI, =RC_FONT_TIMESNRB,
+                  =RC_FONT_TIMESNRBI)
```

You can include several \*DeviceFonts entries in [Unidrv minidrivers](unidrv-minidrivers.md). The GPD parser concatenates multiple entries and makes all listed fonts available for all configurations of the printer's features. If you need to specify that some fonts are only available with certain configurations, you can include \*DeviceFonts entries within [conditional statements](conditional-statements.md).

 

 




