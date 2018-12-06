---
title: Code Example Finish-Install Actions in a Class Installer
description: Code Example Finish-Install Actions in a Class Installer
ms.assetid: 394f321c-2ce4-4773-b5df-e30ce23b7207
keywords:
- finish-install actions WDK device installations
- class installers WDK device installations , finish-install actions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code Example: Finish-Install Actions in a Class Installer


In this example, a class installer performs the following operations to support finish-install actions:

-   When the class installer receives a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request, it calls the installer-supplied function *FinishInstallActionsNeeded* to determine whether there are finish-install actions to perform. (The code for the *FinishInstallActionsNeeded* function is not shown in this example.)

    If *FinishInstallActionsNeeded* returns **TRUE**, the class installer calls [**SetupDiGetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551104) to retrieve the device installation parameters for the device. It then calls [**SetupDiSetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552141) to set the **FlagsEx** member of the [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure for the device with the DI_FLAGSEX_FINISHINSTALL_ACTION flag. Setting this flag causes Windows to send a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request to all class installers, class co-installers, and device co-installers that are involved in the installation of this device. This request is sent after all installation operations except the finish-install actions have completed.

-   When the class installer receives a DIF_FINISHINSTALL_ACTION request, it again calls *FinishInstallActionsNeeded* to determine whether it has finish-install actions to perform and, if so, performs the finish-install actions. The class installer notifies the user that finish-install actions are in progress and waits for the finish-install actions to complete before returning from processing the DIF_FINISHINSTALL_ACTION request.

-   If the finish-install actions succeed, the class installer notifies the user that the finish-install actions succeeded.

-   If the finish-install actions required a restart of the system to complete the finish-install actions, the class installer calls SetupDiGetDeviceInstallParams to retrieve the device installation parameters for the device and then calls SetupDiSetDeviceInstallParams to set the **Flags** member of the SP_DEVINSTALL_PARAMS structure for a device with the DI_NEEDREBOOT flag. The installer also notifies the user that a system restart is required.

-   If the finish-install actions fail, but the finish-install actions should be attempted again the next time the device is enumerated, the class installer notifies the user of this situation.

    **Note**  Starting in Windows 8 a finish-install action is only run once. Windows will not automatically run it again, especially not the next time the device is enumerated because that is not when finish-install actions are run.

     

-   If the finish-install actions fail and the class installer determines that the finish-install actions cannot ever succeed, the class installer notifies the user of this situation.

-   By default, the class installer returns ERROR_DI_DO_DEFAULT in response to a DIF_FINISHINSTALL_ACTION request if the finish-install actions succeeded or if the finish-install actions failed and the installer determines that the finish-install actions should not be attempted again. The installer returns a Win32 error code only if the finish-install actions fail and the finish-install actions should be attempted again the next time the device is enumerated in the context of an administrator.

    **Note**  Starting in Windows 8 a finish-install action is only run once. Windows will not automatically run it again, especially not the next time the device is enumerated because that is not when finish-install actions are run.

     

The following class installer code example shows the basic structure of class installer code that implements finish-install actions:

```cpp
DWORD CALLBACK
SampleClassInstaller(
  IN DI_FUNCTION  InstallFunction,
  IN HDEVINFO  DeviceInfoSet,
  IN PSP_DEVINFO_DATA  DeviceInfoData,
  )
{
  SP_DEVINSTALL_PARAMS DeviceInstallParams;
  DWORD ReturnValue = ERROR_DI_DO_DEFAULT; // The default return value

  switch(InstallFunction)
  {
    case DIF_NEWDEVICEWIZARD_FINISHINSTALL:
      //
      // Processing for finish-install wizard pages
      // If the class installer has wizard pages,
      // set ReturnValue to NO_ERROR
      //
      // Processing for finish-install actions
      if (FinishInstallActionsNeeded())
      {
        // Obtain the device install parameters for the device
        // and set the DI_FLAGSEX_FINISHINSTALL_ACTION flag
        DeviceInstallParams.cbSize = sizeof(DeviceInstallParams);
        if (SetupDiGetDeviceInstallParams(DeviceInfoSet, DeviceInfoData, &DeviceInstallParams))
        {
          DeviceInstallParams.FlagsEx |= DI_FLAGSEX_FINISHINSTALL_ACTION;
          SetupDiSetDeviceInstallParams(DeviceInfoSet, DeviceInfoData, &DeviceInstallParams);
        }
      }
      break;

    case DIF_FINISHINSTALL_ACTION:
      // Processing for finish-install actions
      if (FinishInstallActionsNeeded())
      {
        //
        // Perform the finish-install actions,
        // notify the user that finish install actions
        // are in progress and wait for
        // the finish-install actions to complete
        //
        // If the finish-install actions succeed, notify the user
        //
        // If the finish install actions require a system restart: 
        // notify the user, call SetupDiGetDeviceInstallParams 
        // to obtain the device install parameters for the device in 
        // DeviceInstallParams, and call SetupDiSetInstallParams to set 
        // the DI_NEEDREBOOT flag in DeviceInstallParams.Flags
        // 
        // If the finish install actions failed, but
        // should be attempted again: clean up,
        // notify the user of the failure, and
        // set ReturnValue to an appropriate Win32 error code
        //
        // If the finish install actions failed and 
        // should not be attempted again: clean up and
        // notify the user of the failure
        //
        // Starting with Windows 8, a finish-install action
        // is only run once. Windows will not automatically
        // run it again, especially not the next time
        // the device is enumerated because that is not when
        // finish-install actions are run.
        //
      }
      break;
  }

  return ReturnValue;
}
```

 

 





