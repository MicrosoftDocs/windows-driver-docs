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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Defining the COPP Device Class


## <span id="ddk_defining_the_copp_device_class_gg"></span><span id="DDK_DEFINING_THE_COPP_DEVICE_CLASS_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to define the COPP device class:

```
// COPP device class.
struct DXVA_COPPDeviceClass : public DXVA_DeviceBaseClass
{
    VOID*   m_pThis;
};
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Defining%20the%20COPP%20Device%20Class%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




