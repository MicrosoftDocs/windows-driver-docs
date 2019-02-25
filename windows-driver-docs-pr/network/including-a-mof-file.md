---
title: Including a MOF File
description: Including a MOF File
ms.assetid: 87ef7156-d204-4797-b805-a50d9a4c509d
keywords:
- custom GUIDs WDK networking
- WMI WDK networking , GUIDs
- OIDs WDK networking , WMI
- GUIDs WDK networking
- Windows Management Instrumentation WDK networking , GUIDs
- MOF files WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Including a MOF File





You must include a description of all of the custom GUIDs that map to a miniport driver's custom OIDs in a managed object format (MOF) file that must be compiled and included in the miniport driver's resource (\*.rc) file.

The MOF source file must be of type MOFDATA and must have an extension of .mof. You must compile the MOF source file into a binary file with [Mofcomp.exe](https://msdn.microsoft.com/library/windows/hardware/ff542012) and must check this file with [Wmimofck.exe](https://msdn.microsoft.com/library/windows/hardware/ff565588).

You must insert the following line in the miniport driver's resource file (\*.rc) to include the MOF binary:

```Text
NdisMofResource MOFDATA filename.bmf
```

*FileName* represents the file name of the MOF source file.

 

 





