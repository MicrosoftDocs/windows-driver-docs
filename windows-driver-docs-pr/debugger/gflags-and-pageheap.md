---
title: GFlags and PageHeap
description: GFlags and PageHeap
ms.assetid: 9ced92d9-b37c-4db5-b3f9-fa2fe5325e57
keywords: ["GFlags, GFlags and PageHeap", "PageHeap (pageheap.exe)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# GFlags and PageHeap


## <span id="ddk_gflags_and_pageheap_dtools"></span><span id="DDK_GFLAGS_AND_PAGEHEAP_DTOOLS"></span>


This version of GFlags includes the functionality of PageHeap (pageheap.exe), a tool that enables heap allocation monitoring in Windows. PageHeap enables Windows features that reserve memory at the boundary of each allocation to detect attempts to access memory beyond the allocation.

The page heap options in GFlags let you select *standard heap verification*, which writes fill patterns at the end of each heap allocation and examines the patterns when the allocations are freed, or *full-page heap verification*, which places an inaccessible page at the end of each allocation so that the program stops immediately if it accesses memory beyond the allocation. Because full heap verification uses a full page of memory for each allocation, its widespread use can cause system memory shortages.

-   To enable standard page heap verification for all processes, use **gflags /r +hpa** or **gflags /k +hpa**.

-   To enable standard page heap verification for one process, use **gflags /p /enable** *ImageFileName*.

-   To enable full page heap verification for one process, use **gflags /i** *ImageFileName* **+hpa** or **gflags /p /enable** *ImageFileName* **/full**.

All page heap settings, except for **/k**, are stored in the registry and remain effective until you change them.

Use care in interpreting the **Enable page heap** check box for an image file in the GFlags dialog box. It indicates that page heap verification is enabled for an image file, but it does not indicate whether it is full or standard page heap verification. If the check results from selecting the check box, then full page heap verification is enabled for the image file. However, if the check results from use of the command-line interface, then the check can represent the enabling of either full or standard page heap verification for the image file.

To determine whether full or standard page heap verification is enabled for a program, at the command line, type **gflags /p**. In the resulting display, **traces** indicates that standard page heap verification is enabled for the program and **full traces** indicates that full page heap verification is enabled for the program.

 

 





