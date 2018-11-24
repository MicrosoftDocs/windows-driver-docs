---
title: Calling the COPP DDI from the Display Driver
description: Calling the COPP DDI from the Display Driver
ms.assetid: d91d8a62-f212-4ae7-be61-b973d6495880
keywords:
- calling COPP DDI WDK DirectX VA
- COPP WDK DirectX VA , calling from the display driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling the COPP DDI from the Display Driver


## <span id="ddk_calling_the_copp_ddi_from_the_display_driver_gg"></span><span id="DDK_CALLING_THE_COPP_DDI_FROM_THE_DISPLAY_DRIVER_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The display driver initiates calls to the video miniport driver's [COPP DDI](https://msdn.microsoft.com/library/windows/hardware/ff540449) by using COPP I/O control (IOCTL) requests. The display driver calls the [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) function by using a COPP IOCTL to send a synchronous COPP request to the video miniport driver. Graphics Device Interface (GDI) uses a single buffer for both input and output to pass the request to the I/O subsystem. The I/O subsystem routes the request to the video port, which processes the request by using the video miniport driver.

The following sample data structure and IOCTLs can be used to transfer COPP information between the display driver and the video miniport driver. Your drivers can either use the data structure and IOCTLs or create new ones, as appropriate.

```cpp
typedef struct {
    PVOID* ppThis;
    PVOID InputBuffer;
    HRESULT phr;
} COPP_IO_InputBuffer;

#define IOCTL_COPP_OpenDevice \
        CTL_CODE(FILE_DEVICE_VIDEO, 2190, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_COPP_CloseDevice \
        CTL_CODE(FILE_DEVICE_VIDEO, 2191, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_COPP_GetCertificateLength \
        CTL_CODE(FILE_DEVICE_VIDEO, 2192, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_COPP_KeyExchange \
        CTL_CODE(FILE_DEVICE_VIDEO, 2193, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_COPP_StartSequence \
        CTL_CODE(FILE_DEVICE_VIDEO, 2194, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_COPP_Command \
        CTL_CODE(FILE_DEVICE_VIDEO, 2195, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_COPP_Status \
        CTL_CODE(FILE_DEVICE_VIDEO, 2196, METHOD_BUFFERED, FILE_ANY_ACCESS)
```

If you do not use the preceding IOCTLs, then you can define your own private IOCTLs, which must be formatted as described in [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023).

 

 





