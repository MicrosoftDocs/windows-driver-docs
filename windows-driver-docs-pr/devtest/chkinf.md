---
title: ChkINF
description: ChkINF
ms.assetid: fa09cd42-34f0-4a0a-9729-0134057053f1
keywords: ["Perl scripts WDK INF files", "ChkINF", "INF File Syntax Checker WDK", "INF files WDK , syntax checker", "syntax checker WDK INF files", "verifying INF files", "checking INF files", "scripts WDK ChkINF"]
---

# ChkINF


## <span id="ddk_chkinf_tools"></span><span id="DDK_CHKINF_TOOLS"></span>


The *INF File Syntax Checker*, or **ChkINF**, is a set of Perl scripts and support applications that verify the structure and syntax of setup information (INF) files for drivers that are designed for Microsoft Windows 7 and later versions of Windows.

After examining a file, ChkINF displays the errors and possible errors it detected in each INF file. The display is formatted in HTML for viewing in an Internet browser window or for posting on an intranet or the Internet.

ChkINF supports all INF sections and directives for all device classes. In addition, ChkINF can verify INF elements that are used only in INF files for specific device setup classes, including classes of file system drivers. For a complete list of the classes that ChkINF supports, see the chkinf.htm file in the Tools\\chkinf subdirectory of the Windows Driver Kit (WDK).

**Note**   ChkINF has not been tested extensively. Review your results carefully.

 

## <span id="in_this_section"></span>In this section


-   [ChkINF Components](chkinf-components.md)
-   [Requirements and Limitations](requirements-and-limitations.md)
-   [**ChkINF Command Syntax**](chkinf-command-syntax.md)
-   [ChkINF Results](chkinf-results.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20ChkINF%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




