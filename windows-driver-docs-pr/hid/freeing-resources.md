---
title: Freeing Resources
description: User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required.
ms.assetid: 19cbc443-cc25-448f-92dc-d9586c1fd5a7
keywords:
- collections WDK HID , free resources
- HID collections WDK , free resources
- freeing HID resources
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Freeing Resources


User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required.




For example, a user-mode application must call [**SetupDiDestroyDeviceInfoList**](/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist) with the handle to the device list that it obtained from [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) after completing its initialization and connection operations for a HIDClass device. Failure to call **SetupDiDestroyDeviceInfoList** causes a memory leak.

 

