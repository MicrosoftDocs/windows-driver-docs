---
title: Manifest File Placement
description: Manifest File Placement
ms.assetid: ebf10463-3aa1-403a-8508-1462259a5f8a
keywords: ["LogViewer, manifest, file placement"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Manifest File Placement


## <span id="ddk_manifest_file_placement_dtoolq"></span><span id="DDK_MANIFEST_FILE_PLACEMENT_DTOOLQ"></span>


The primary manifest file must be named Main.h.

When Logger is running, Main.h must be located in the Manifest subdirectory of the directory containing Logexts.dll.

LogViewer is more flexible than Logger. It will search for Main.h in the following directories in this order:

1.  The Manifest directory subordinate to the directory containing Logviewer.exe

2.  The WinExt\\Manifest directory subordinate to the directory containing logviewer.exe

3.  The %WinDir%\\System32\\Manifest directory

4.  The %WinDir%\\System\\Manifest directory

All additional manifest files must reside in the same directory as Main.h.

 

 





