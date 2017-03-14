---
title: Deinterlacing and Compositing on 64-bit Operating Systems
description: Deinterlacing and Compositing on 64-bit Operating Systems
ms.assetid: af95b9f8-1329-4cba-a70f-4f1884f6a0f9
keywords: ["deinterlacing WDK DirectX VA , 64-bit", "64-bit WDK DirectX VA", "DXVA_DeinterlaceBltEx"]
---

# Deinterlacing and Compositing on 64-bit Operating Systems


This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

To ensure that [deinterlacing with substream-compositing operations](performing-deinterlacing-with-substream-compositing-operations.md) initiated by a 32-bit application run successfully on a 64-bit operating system, the display driver code must first detect whether the application is 32 bit or 64 bit. To perform the detection, the driver should check the size of the [**DXVA\_DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563915) structure that the application passes. If the driver determines that the initiating application is 32 bit, the driver should handle the deinterlacing operations by thunking. The driver should use the [**DXVA\_VideoSample32**](https://msdn.microsoft.com/library/windows/hardware/ff564102) and [**DXVA\_DeinterlaceBltEx32**](https://msdn.microsoft.com/library/windows/hardware/ff563920) structures to perform the deinterlace thunk. For more information about thunking, see [Supporting 32-Bit I/O in Your 64-Bit Driver](https://msdn.microsoft.com/library/windows/hardware/ff563897).

**Note**   When the driver code is compiled for 64-bit, the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure contains two extra DWORD members to make the size of the 32-bit version of DXVA\_VideoSample2 different from the 64-bit version. Because of an 8-byte alignment, the 32-bit compiler adds 4 bytes of padding to the end of the 32-bit version, which--without these two extra DWORD members--makes the 32-bit version the same size as the 64-bit version, even accounting for the pointer-size difference between 32 bit and 64 bit.
With two extra DWORD members included in DXVA\_VideoSample2 for 64-bit compile, the driver can differentiate between the 32-bit and 64-bit versions based on the **Size** member of the [**DXVA\_DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563915) structure.

 

The following example code demonstrates how the driver should handle the thunk:

```
switch (lpData->dwFunction) {
case DXVA_DeinterlaceBltExFnCode:
    {   DXVA_DeinterlaceBltEx* pBlt = (DXVA_DeinterlaceBltEx*)lpData->lpInputData; 
        switch (pBlt->Size) {
             case sizeof(DXVA_DeinterlaceBltEx): // should be 4400 bytes on Win64
                                                // should be 4144 bytes on Win32
                  break;
#ifdef _WIN64
             case sizeof(DXVA_DeinterlaceBltEx32): // should be 4144 bytes
                  // 32-bit structure, so thunk it!
                  break;
#endif
            default:
                  // unknown structure, so return error;
                  break;
            }
      }
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deinterlacing%20and%20Compositing%20on%2064-bit%20Operating%20Systems%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




