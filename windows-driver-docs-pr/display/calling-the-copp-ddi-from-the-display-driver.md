---
title: Calling the COPP DDI from the Display Driver
description: Calling the COPP DDI from the Display Driver
ms.assetid: d91d8a62-f212-4ae7-be61-b973d6495880
keywords:
- calling COPP DDI WDK DirectX VA
- COPP WDK DirectX VA , calling from the display driver
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Calling the COPP DDI from the Display Driver


## <span id="ddk_calling_the_copp_ddi_from_the_display_driver_gg"></span><span id="DDK_CALLING_THE_COPP_DDI_FROM_THE_DISPLAY_DRIVER_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The display driver initiates calls to the video miniport driver's [COPP DDI](https://msdn.microsoft.com/library/windows/hardware/ff540449) by using COPP I/O control (IOCTL) requests. The display driver calls the [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) function by using a COPP IOCTL to send a synchronous COPP request to the video miniport driver. Graphics Device Interface (GDI) uses a single buffer for both input and output to pass the request to the I/O subsystem. The I/O subsystem routes the request to the video port, which processes the request by using the video miniport driver.

The following sample data structure and IOCTLs can be used to transfer COPP information between the display driver and the video miniport driver. Your drivers can either use the data structure and IOCTLs or create new ones, as appropriate.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Calling%20the%20COPP%20DDI%20from%20the%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




