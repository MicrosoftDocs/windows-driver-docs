---
title: Creating a Single Driver Package for Windows XP and Windows Vista
description: Creating a Single Driver Package for Windows XP and Windows Vista
ms.assetid: 5e350152-edd7-4afb-bcba-dd0217d0d17a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Single Driver Package for Windows XP and Windows Vista


The Microsoft [Connect](http://go.microsoft.com/fwlink/p/?linkid=133880) Web site provides two groups of core driver updates:

-   For Windows operating systems earlier than Windows Vista (including Windows Server 2003, Windows XP, and Windows 2000), a set of redistributable updates allows hardware manufacturers to incorporate the specific files they need to support these operating systems.

-   For Windows Vista and later, a separate package allows hardware manufacturers to ship the latest core driver package.

To support both Windows XP (and other Windows operating systems earlier than Windows Vista) and Windows Vista and later operating systems in the same driver package, hardware manufacturers must use the appropriate redistributable package, and construct their INF accordingly.

### No Redistributable Package

If your driver works with both the Windows XP and Windows Vista versions of the core driver components (that is, if no redistribution of core drivers is required), follow these steps:

1.  Continue to use your Windows XP driver on Windows Vista. No changes are required.

2.  For Windows Vista Premium logo certification, provide separate INF install sections for Windows XP (and other Windows operating systems earlier than Windows Vista) and Windows Vista and later operating systems, and make the INF install section for Windows Vista package aware.

### <a href="" id="redistributable-package-for-windows-operating-systems-earlier-than-win"></a> Redistributable Package for Windows Operating Systems earlier than Windows Vista

If your driver works with the initial Windows Vista release, but you need the Windows Vista version of the core driver components to work on Windows XP and earlier operating systems (that is, if redistribution for Windows operating systems earlier than Windows Vista is required), follow these steps:

1.  Create separate INF install sections for Windows XP (and other Windows operating systems earlier than Windows Vista) and for Windows Vista (and later).

2.  Use the INF **CoreDriverDependencies** and **CoreDriverSections** directives to force the Windows Vista section of the INF file to use the inbox core driver package.

3.  Determine the files from the redistribution packages for Windows operating systems earlier than Windows Vista that are needed to support those operating system versions.

4.  Include the required binaries for downlevel support in your driver package, and only copy them for installation on Windows operating systems earlier than Windows Vista.

### Windows Vista Redistributable Package

If your driver requires updated versions of the core driver package to work properly on the initial Windows Vista release and on Windows XP (that is, if redistribution to Windows Vista is required), follow these steps:

1.  Create separate INF install sections for Windows XP (and other Windows operating systems earlier than Windows Vista) and for Windows Vista and later.

2.  Include the entire Windows Vista core driver package in a subdirectory of your driver package.

3.  Use the [**INF CopyINF directive**](https://msdn.microsoft.com/library/windows/hardware/ff547317) to preload the updated core driver into the driver store.

4.  Use the INF **InboxVersionRequired**=*&lt;version of the updated core driver&gt;* directive to ensure only the newer version of the core driver package is used.

5.  Use the INF **CoreDriverDependencies** and **CoreDriverSections** directives to indicate that your Windows Vista driver requires the updated core driver.

6.  In your install section for Windows operating systems earlier than Windows Vista, copy the required files directly out of the included core driver package as if they were part of your driver.

 

 




