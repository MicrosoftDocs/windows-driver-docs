---
title: wdfkd.wdfsetdriver
description: The wdfkd.wdfsetdriver extension sets the name of the default Kernel-Mode Driver Framework (KMDF) driver to which debugger extension commands apply.
ms.assetid: 90fc99a0-1e78-44bb-ba91-191f116160e7
keywords: ["wdfkd.wdfsetdriver Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfsetdriver
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfsetdriver


The **!wdfkd.wdfsetdriver** extension sets the name of the default Kernel-Mode Driver Framework (KMDF) driver to which debugger extension commands apply.

```dbgcmd
!wdfkd.wdfsetdriver DriverName
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of a driver. *DriverName* must not include the .sys file name extension.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The **!wdfkd.wdfsetdriver** extension sets the default driver name. You can use this name with other **wdfkd** extensions that would otherwise require you to specify a driver name.

To obtain the name of the current default KMDF driver, use the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension.

 

 





