---
title: Co-installer Interface
description: Co-installer Interface
ms.assetid: affcf2a5-5dbb-49bd-916c-bc99302b5bd8
keywords:
- co-installers WDK device installations , interface
- interface WDK co-installer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Co-installer Interface


A co-installer's interface consists of an exported entry point function and an associated data structure.

### <a href="" id="co-installer-entry-point"></a> Co-installer Entry Point

A co-installer must export an entry point function that has the following prototype:

```cpp
typedef DWORD 
  (CALLBACK* COINSTALLER_PROC) (
    IN DI_FUNCTION  InstallFunction,
    IN HDEVINFO  DeviceInfoSet,
    IN PSP_DEVINFO_DATA  DeviceInfoData  OPTIONAL,
    IN OUT PCOINSTALLER_CONTEXT_DATA  Context
    );
```

<a href="" id="installfunction"></a>*InstallFunction*  
Specifies the device installation request being processed, in which the co-installer has the option of participating. These requests are specified using DIF codes, such as DIF_INSTALLDEVICE. For more information, see [Device Installation Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff541307).

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to a [device information set](device-information-sets.md).

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Optionally identifies a device that is the target of the device installation request. If this parameter is non-**NULL**, it identifies a device information element in the device information set. *DeviceInfoData* is non-**NULL** when [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) calls a device-specific co-installer. A class-specific co-installer can be called with a DIF request that has a **NULL***DeviceInfoData*, such as DIF_DETECT or DIF_FIRSTTIMESETUP.

<a href="" id="context"></a>*Context*  
Points to a [**COINSTALLER_CONTEXT_DATA**](#coinstaller-context-data) structure.

A device co-installer returns one of the following values:

<a href="" id="no-error"></a>NO_ERROR  
The co-installer performed the appropriate actions for the specified *InstallFunction*, or the co-installer determined that it didn't need to perform any actions for the request.

The co-installer must also return NO_ERROR if it receives an unrecognized DIF code. (Note that class installers return ERROR_DI_DO_DEFAULT for unrecognized DIF codes.)

<a href="" id="error-di-postprocessing-required"></a>ERROR_DI_POSTPROCESSING_REQUIRED  
The co-installer performed any appropriate actions for the specified *InstallFunction* and is requesting to be called again after the Class Installer has processed the request.

<a href="" id="a-win32-error"></a>*A Win32 error*  
The co-installer encountered an error.

A co-installer does not set a return status of ERROR_DI_DO_DEFAULT. This status can be used only by a Class Installer. If a co-installer returns this status, **SetupDiCallClassInstaller** will not process the DIF_*Xxx* request properly. A co-installer might *propagate* a return status of ERROR_DI_DO_DEFAULT in its postprocessing pass, but it never *sets* this value.

### <a href="" id="coinstaller-context-data"></a> COINSTALLER_CONTEXT_DATA

COINSTALLER_CONTEXT_DATA is a co-installer-specific context structure that describes an installation request. The format of the structure is:

```cpp
typedef struct 
  _COINSTALLER_CONTEXT_DATA {
      BOOLEAN  PostProcessing;
      DWORD    InstallResult;
      PVOID    PrivateData;
  } COINSTALLER_CONTEXT_DATA, *PCOINSTALLER_CONTEXT_DATA;
```

The following list describes the members of this structure:

-   **PostProcessing** is **TRUE** when a co-installer is called after the appropriate class installer, if any, has processed the DIF code specified by *InstallFunction*. **PostProcessing** is read-only to the co-installer.

-   If **PostProcessing** is **FALSE**, **InstallResult** is not relevant. If **PostProcessing** is **TRUE**, **InstallResult** is the current status of the install request. This value is NO_ERROR or an error status returned by the previous component called for this install request. A co-installer can propagate the status by returning this value for its function return, or it can return another status. **InstallResult** is read-only to the co-installer.

-   **PrivateData** points to a co-installer-allocated buffer. If a co-installer sets this pointer and requests postprocessing, **SetupDiCallClassInstaller** passes the pointer to the co-installer when it calls the co-installer for postprocessing.

 

 





