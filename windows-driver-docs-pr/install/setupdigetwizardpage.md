---
title: SetupDiGetWizardPage
description: SetupDiGetWizardPage
ms.assetid: c43ee948-10aa-4b8f-91d0-0f3baf8ccf16
keywords: ["SetupDiGetWizardPage Device and Driver Installation"]
topic_type:
- apiref
api_name:
- SetupDiGetWizardPage
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SetupDiGetWizardPage


The **SetupDiGetWizardPage** function is reserved for system use. For information about wizard pages, see the DIF_NEWDEVICEWIZARD_*XXX* requests, for example, [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](dif-newdevicewizard-finishinstall.md).

```cpp
HPROPSHEETPAGE
 SetupDiGetWizardPage(
 IN HDEVINFO DeviceInfoSet, 
 IN PSP_DEVINFO_DATA DeviceInfoData..OPTIONAL,
 IN PSP_INSTALLWIZARD_DATA InstallWizardData,
 IN DWORD PageType,
    IN DWORD Flags
 );
```

 

 





