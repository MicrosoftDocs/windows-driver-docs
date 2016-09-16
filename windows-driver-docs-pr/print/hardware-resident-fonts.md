---
title: Hardware-Resident Fonts
author: windows-driver-content
description: Hardware-Resident Fonts
MS-HAID:
- 'nt5gpd\_fc3ca20b-2be4-4112-b735-0d73f2557402.xml'
- 'print.hardware\_resident\_fonts'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 359735c2-bfa3-4c32-82a5-1d455c4eacb1
keywords: ["printer font descriptions WDK Unidrv , hardware-resident fonts", "hardware-resident fonts WDK Unidrv"]
---

# Hardware-Resident Fonts


## <a href="" id="ddk-hardware-resident-fonts-gg"></a>


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

```
*% Assume that RC_FONT_xxx ids are references to 
*% value macros defined by the GPD file creator.
*DeviceFonts: LIST(=RC_FONT_COURIER10, =RC_FONT_ARIALR,
+                  =RC_FONT_ARIALI, =RC_FONT_ARIALB, 
+                  =RC_FONT_ARIALBI, =RC_FONT_TIMESNRR,
+                  =RC_FONT_TIMESNRI, =RC_FONT_TIMESNRB,
+                  =RC_FONT_TIMESNRBI)
```

You can include several \*DeviceFonts entries in [Unidrv minidrivers](unidrv-minidrivers.md). The GPD parser concatenates multiple entries and makes all listed fonts available for all configurations of the printer's features. If you need to specify that some fonts are only available with certain configurations, you can include \*DeviceFonts entries within [conditional statements](conditional-statements.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Hardware-Resident%20Fonts%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


