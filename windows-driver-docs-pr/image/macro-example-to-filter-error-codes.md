---
title: Macro Example to Filter Error Codes
author: windows-driver-content
description: Macro Example to Filter Error Codes
ms.assetid: 68aa0a75-82c7-4dd9-8f8f-eca5de6ea102
---

# Macro Example to Filter Error Codes


The following macro example filters communication failure error codes.

```
//
// Example of a macro to filter device communication errors
//
#define WSD_COMMUNICATION_ERROR(hr) \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_CANNOT_CONNECT)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_CONNECTION_ERROR)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_TIMEOUT)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_TIMEOUT)) == hr) || \
    ((HRESULT_FROM_WIN32(ERROR_WINHTTP_NAME_NOT_RESOLVED)) == hr))
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Macro%20Example%20to%20Filter%20Error%20Codes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


