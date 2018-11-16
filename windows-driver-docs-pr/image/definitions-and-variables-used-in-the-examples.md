---
title: Definitions and Variables Used in the Examples
description: Definitions and Variables Used in the Examples
ms.assetid: 55dd0618-2171-406b-a22a-437412c77cbc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Definitions and Variables Used in the Examples

> [!IMPORTANT]  
> WSD Challenger functionality has been deprecated and all WSD Challenger-related documentation will be removed in 2018.

The following code shows constant definitions and common variables that are used in the code examples in this section.

```cpp
//
// WSD Challenge DLL name (including a forward path separator) and public API names
 
//
#define WSDCHNGR_DLL_NAME                    L"\\WSDCHNGR.DLL"
#define WSDCHNR_INITIALIZE                   "WSDCHNGRInitialize" 
#define WSDCHNR_SHUTDOWN                     "WSDCHNGRShutdown" 
#define WSDCHNR_REGISTER_DEVICE_TO_CHALLENGE "WSDCHNGRRegisterDeviceToChallenge" 

//
// Function pointer types for public WSD Challenge APIs
//
typedef HRESULT (*PFN_WSDCHNR_INITIALIZE)();
typedef HRESULT (*PFN_WSDCHNR_SHUTDOWN)();
typedef HRESULT (*PFN_WSDCHNR_REGISTER_DEVICE_TO_CHALLENGE)(__in IFunctionInstance *pFunctionInstance);

//
// The instance module of the WSD Challenge DLL (WSDCHNGR.DLL)
//
HMODULE m_hChallengeDll;

//
// Function pointer for public WSD Challenge APIs that are used by this driver
//
PFN_WSDCHNR_REGISTER_DEVICE_TO_CHALLENGE m_pfnRegisterDeviceToChallenge;
PFN_WSDCHNR_INITIALIZE m_pfnInitializeChallenge;
PFN_WSDCHNR_SHUTDOWN m_pfnShutdownChallenge;
```

 

 




