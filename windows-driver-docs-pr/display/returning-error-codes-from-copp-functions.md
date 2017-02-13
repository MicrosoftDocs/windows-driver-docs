---
title: Returning Error Codes from COPP Functions
description: Returning Error Codes from COPP Functions
ms.assetid: a42fba73-59b2-4106-ba2b-9e96cd8524c8
keywords: ["copy protection WDK COPP , error codes", "video copy protection WDK COPP , error codes", "COPP WDK DirectX VA , error codes", "protected video WDK COPP , error codes", "error codes WDK COPP"]
---

# Returning Error Codes from COPP Functions


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

The [COPP DDI](https://msdn.microsoft.com/library/windows/hardware/ff540449) can return the following types of error codes:

-   Error codes that are defined in the *winerror.h* header file and are common to all Windows applications. These Windows error codes start with the E\_ prefix.

-   Error codes that are defined in the *ddraw.h* header file and are unique to DirectDraw. These DirectDraw error codes start with the DDERR\_ prefix.

No error codes are unique to the COPP DDI.

When implementing the COPP DDI, you should restrict your usage of Windows error codes to the following:

-   E\_UNEXPECTED

    The display driver is in an invalid state. For example, the [*COPPSequenceStart*](https://msdn.microsoft.com/library/windows/hardware/ff540421) function was called before the [*COPPKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/ff539646) function.

-   E\_INVALIDARG

    Input parameters passed to the driver are invalid.

-   E\_POINTER

    An output parameter, which should point to a valid address, is **NULL**.

The COPP DDI can return the E\_FAIL and DDERR\_GENERIC error codes; however, because they do not indicate what caused the error, their use is discouraged.

The Remarks section for each COPP function specifies the DDERR\_ error codes that the COPP function can report. The COPP DDI should not be required to return any other DDERR\_ error codes.

When propagating error information from the COPP DDI in the video miniport driver to the display driver, you should not use the return value from the [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) function, because the Windows kernel manipulates the error value that is returned from the IOCTL to **EngDeviceIoControl**. Instead, error information should be passed through the *lpInBuffer* parameter of **EngDeviceIoControl**. For more information, see [Calling the COPP DDI from the Display Driver](calling-the-copp-ddi-from-the-display-driver.md) and the example code in [COPP Video Miniport Driver Template](copp-video-miniport-driver-template.md) and [Performing COPP Operations](performing-copp-operations2.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Returning%20Error%20Codes%20from%20COPP%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




