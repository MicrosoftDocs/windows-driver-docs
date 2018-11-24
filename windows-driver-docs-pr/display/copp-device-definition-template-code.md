---
title: COPP Device Definition Template Code
description: COPP Device Definition Template Code
ms.assetid: 86cafb33-f92a-4c5d-8a54-37aab5e79f37
keywords:
- COPP device WDK DirectX VA
- copy protection WDK COPP , COPP device
- COPP WDK DirectX VA , COPP device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Device Definition Template Code


## <span id="ddk_copp_device_definition_template_code_gg"></span><span id="DDK_COPP_DEVICE_DEFINITION_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to define a COPP DirectX VA device object.

```cpp
#define COPP_OPENED                 0
#define COPP_CERT_LENGTH_RETURNED   1
#define COPP_KEY_EXCHANGED          2
#define COPP_SESSION_ACTIVE         3
typedef struct {
    DWORD   m_LocalLevel[COPP_MAX_TYPES];
    GUID    m_KDI;
    DWORD   m_CmdSeqNumber;
    DWORD   m_StatusSeqNumber;
    DWORD   m_rGraphicsDriver;
    DWORD   m_COPPDevState;
    DWORD   m_DevID;

    AESHelper   m_AesHelper;

} COPP_DeviceData;
```

 

 





