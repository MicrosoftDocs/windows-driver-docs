---
title: Returning Error Codes from COPP Functions
description: Returning Error Codes from COPP Functions
ms.assetid: a42fba73-59b2-4106-ba2b-9e96cd8524c8
keywords:
- copy protection WDK COPP , error codes
- video copy protection WDK COPP , error codes
- COPP WDK DirectX VA , error codes
- protected video WDK COPP , error codes
- error codes WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
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

When propagating error information from the COPP DDI in the video miniport driver to the display driver, you should not use the return value from the [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) function, because the Windows kernel manipulates the error value that is returned from the IOCTL to **EngDeviceIoControl**. Instead, error information should be passed through the *lpInBuffer* parameter of **EngDeviceIoControl**. For more information, see [Calling the COPP DDI from the Display Driver](calling-the-copp-ddi-from-the-display-driver.md) and the example code in [COPP Video Miniport Driver Template](copp-video-miniport-driver-template.md) and [Performing COPP Operations](performing-copp-operations-example.md).

 

 





