---
title: Defining the COPP Device Class
description: Defining the COPP Device Class
ms.assetid: eb5e7269-fe4c-44d1-9024-f5b1a180e10b
keywords:
- copy protection WDK COPP , COPP device
- video copy protection WDK COPP , COPP device
- COPP WDK DirectX VA , COPP device
- protected video WDK COPP , COPP device
- COPP device WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining the COPP Device Class


## <span id="ddk_defining_the_copp_device_class_gg"></span><span id="DDK_DEFINING_THE_COPP_DEVICE_CLASS_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to define the COPP device class:

```cpp
// COPP device class.
struct DXVA_COPPDeviceClass : public DXVA_DeviceBaseClass
{
    VOID*   m_pThis;
};
```

 

 





