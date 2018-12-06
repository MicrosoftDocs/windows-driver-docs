---
title: Control GUID File
description: Control GUID File
ms.assetid: cf5dd9bf-c9db-4324-abd3-ee0e1b15e14d
keywords:
- control GUIDs WDK
- .ctl files
- ctl files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control GUID File


## <span id="ddk_control_guid_file_tools"></span><span id="DDK_CONTROL_GUID_FILE_TOOLS"></span>


The *control GUID file* (.ctl extension) is a text file that specifies the [control GUID](control-guid.md) of the trace provider and a friendly name for the GUID in the format:

```
ControlGUID GUIDFriendlyName
```

Developers of trace providers typically supply this file. However, if you have the source code for the trace provider, you can find the GUID and the GUID friendly name, and create a control GUID file.

In the source code, find the definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro. The GUID value and GUID friendly name are shown in bold in the example below.

```
#define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID(GUIDFriendlyName, (ControlGUID),  \
        WPP_DEFINE_BIT(NameOfTraceFlag1)  \
        WPP_DEFINE_BIT(NameOfTraceFlag2)  \
        .............................   \
        .............................   \
        WPP_DEFINE_BIT(NameOfTraceFlag31) )
```

 

 





