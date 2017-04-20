---
title: Deinterlacing on 64-bit Operating Systems
description: Deinterlacing on 64-bit Operating Systems
ms.assetid: ffac0c1a-2c92-4beb-9622-26d10e1a06aa
keywords:
- deinterlacing WDK DirectX VA , 64-bit
- 64-bit WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Deinterlacing on 64-bit Operating Systems


To ensure that deinterlacing operations initiated by a 32-bit application run successfully on a 64-bit operating system, the display driver code must first detect whether the application is 32 bit or 64 bit. To perform the detection, the driver should check the **Size** member of the [**DXVA\_DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563912) structure that the application passes. The size of the 32-bit version of DXVA\_DeinterlaceBlt is smaller than the size of the 64-bit version because of the pointer size difference between 32 bit and 64 bit. If the driver determines that the initiating application is 32 bit, the driver should handle the deinterlacing operations by thunking. For more information about thunking, see [Supporting 32-Bit I/O in Your 64-Bit Driver](https://msdn.microsoft.com/library/windows/hardware/ff563897).

The following example code demonstrates how the driver should handle the thunk:

```
switch (lpData->dwFunction) {
case DXVA_DeinterlaceBltFnCode:
    {   
        DXVA_DeinterlaceBlt* pBlt = (DXVA_DeinterlaceBlt*)lpData->lpInputData; 
         if (pBlt->Size == sizeof(DXVA_DeinterlaceBlt)) {
            // correctly formed 64-bit or 32-bit structure, so use it
        }
#ifdef _WIN64
        else if (pBlt->Size < sizeof(DXVA_DeinterlaceBlt)) {
            // 32-bit structure, so thunk it!
        }
#endif
        else {
            // unknown structure, so return error;
        }
    }
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deinterlacing%20on%2064-bit%20Operating%20Systems%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




