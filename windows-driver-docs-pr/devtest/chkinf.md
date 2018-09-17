---
title: ChkINF
description: ChkINF
ms.assetid: fa09cd42-34f0-4a0a-9729-0134057053f1
keywords:
- Perl scripts WDK INF files
- ChkINF
- INF File Syntax Checker WDK
- INF files WDK , syntax checker
- syntax checker WDK INF files
- verifying INF files
- checking INF files
- scripts WDK ChkINF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 





