---
title: Macro Example to Filter Error Codes
description: Macro Example to Filter Error Codes
ms.date: 04/20/2017
---

# Macro Example to Filter Error Codes

> [!IMPORTANT]  
> WSD Challenger functionality has been deprecated and all WSD Challenger-related documentation will be removed in 2018.

The following macro example filters communication failure error codes.

```cpp
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

 




