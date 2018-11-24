---
title: Deinterlacing on 64-bit Operating Systems
description: Deinterlacing on 64-bit Operating Systems
ms.assetid: ffac0c1a-2c92-4beb-9622-26d10e1a06aa
keywords:
- deinterlacing WDK DirectX VA , 64-bit
- 64-bit WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deinterlacing on 64-bit Operating Systems


To ensure that deinterlacing operations initiated by a 32-bit application run successfully on a 64-bit operating system, the display driver code must first detect whether the application is 32 bit or 64 bit. To perform the detection, the driver should check the **Size** member of the [**DXVA\_DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563912) structure that the application passes. The size of the 32-bit version of DXVA\_DeinterlaceBlt is smaller than the size of the 64-bit version because of the pointer size difference between 32 bit and 64 bit. If the driver determines that the initiating application is 32 bit, the driver should handle the deinterlacing operations by thunking. For more information about thunking, see [Supporting 32-Bit I/O in Your 64-Bit Driver](https://msdn.microsoft.com/library/windows/hardware/ff563897).

The following example code demonstrates how the driver should handle the thunk:

```cpp
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

 

 





