---
title: Manifest File Placement
description: Manifest File Placement
ms.assetid: ebf10463-3aa1-403a-8508-1462259a5f8a
keywords: ["LogViewer, manifest, file placement"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Manifest%20File%20Placement%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




