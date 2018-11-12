---
title: wdfkd.wdflogsave
description: The wdfkd.wdflogsave extension saves the Kernel-Mode Driver Framework (KMDF) error log records for a specified driver to an event trace log (.etl) file that you can view by using TraceView.
ms.assetid: e072d522-a418-4afb-8434-c6355d026770
keywords: ["wdfkd.wdflogsave Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdflogsave
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdflogsave


The **!wdfkd.wdflogsave** extension saves the Kernel-Mode Driver Framework (KMDF) error log records for a specified driver to an event trace log (.etl) file that you can view by using TraceView.

```dbgcmd
!wdfkd.wdflogsave [DriverName [FileName]]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
Optional. The name of a driver. *DriverName* must not include the .sys file name extension.

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Optional. The name of the file to which the KMDF error log records should be saved. *FileName* should not include the .etl file name extension. If you omit *FileName*, the KMDF error log records are saved to the DriverName.etl file.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

If you omit the *DriverName* parameter, the default driver name is used. Use the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension to display the default driver name, and use the [**!wdfkd.wdfsetdriver**](-wdfkd-wdfsetdriver.md) extension to set the default driver name.

 

 





