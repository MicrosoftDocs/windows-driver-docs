---
title: GetSupportedVersions
description: The IPrintTicketProvider GetSupportedVersions method returns the major version numbers of the Print Schemas that print driver supports. For now, version 1 is the only version that exists so this method must return only one supported version.
ms.assetid: 0b648cc3-4d61-401c-b626-34db2b026b2a
keywords:
- GetSupportedVersions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GetSupportedVersions


The [**IPrintTicketProvider::GetSupportedVersions**](https://msdn.microsoft.com/library/windows/hardware/ff554371) method returns the major version numbers of the Print Schemas that print driver supports. For now, version 1 is the only version that exists so this method must return only one supported version.

The implementation shown in the following sample code will work for the initial version of Windows Vista and until a new version is added. When a new version is supported, this value will change.

```cpp
STDMETHODIMP 
CPrintTicketProvider::
GetSupportedVersions(THIS_ HANDLE hPrinter,
                           INT *ppVersions[],
                           INT *pcVersions)
{
    if ( (*ppVersions = (INT*)CoTaskMemAlloc(sizeof(INT))) != NULL)
    {
         (*ppVersions)[0] = 1;  // Version 1
        *pcVersions = 1; // 1 supported version
        return S_OK;
    }
    else
        return E_OUTOFMEMORY;
}
```

 

 




