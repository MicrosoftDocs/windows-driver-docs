---
title: Definitions and Variables Used in the Examples
author: windows-driver-content
description: Definitions and Variables Used in the Examples
ms.assetid: 55dd0618-2171-406b-a22a-437412c77cbc
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Definitions and Variables Used in the Examples


The following code shows constant definitions and common variables that are used in the code examples in this section.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Definitions%20and%20Variables%20Used%20in%20the%20Examples%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


