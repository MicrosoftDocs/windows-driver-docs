---
title: Writing Class Installers and Co-Installers
description: Writing Class Installers and Co-Installers
ms.assetid: DA52A2C4-81D7-4e95-97CD-D5A1C625CE02
keywords:
- class installers WDK device installations , writing
- writing class installers WDK device installations
- co-installers WDK device installations , writing
- writing co-installers WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing Class Installers and Co-Installers


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This section contains the guidelines that you should follow when you write a [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer):

[Displaying a user interface](#displaying-a-user-interface)

[Saving device installation state](#saving-device-installation-state)

[Loading executable or DLL files](#loading-executable-or-dll-files)

[Starting other processes or services](#starting-other-processes-or-services)

For more information about how to write a co-installer, see [Writing a Co-installer](writing-a-co-installer.md).

## Displaying a user interface


Device installation mostly runs in a system (noninteractive) service. Therefore, a user cannot see or respond to any user interface that appears in this context. Any dialog box that is provided in [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) during the processing of a [device installation function (DIF) code](https://msdn.microsoft.com/library/windows/hardware/ff541307) causes the device installation to stop responding.

In most cases, co-installers should not interact with the user except during the processing of a [finish-install action](finish-install-actions--windows-vista-and-later-.md). Finish-install actions run in an interactive context.

**Note**  Co-installers should not fail a DIF code with ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION because that causes the device installation to fail. If the device installation requires user interaction, co-installers should support finish-install actions.

 

## Saving device installation state


Do not save device installation state within the [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) dynamic-link library (DLL). Because Windows generally unloads the DLL after a DIF code is handled by the installer, any state information that is saved within the DLL would not persist.

To safely preserve device installer state, class installers or co-installers should save the state information as properties within the device's [*driver key*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-key) in the registry. To do this, follow these steps:

1.  To retrieve a registry handle to the driver key for a [*device instance*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance), use [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) with the *KeyType* parameter set to DIREG_DRV.

2.  Use [**SetupDiGetDevicePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551965) (to retrieve all the property keys for a device instance) or [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) (to retrieve a specified device instance property key).

3.  Use [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) to save the device instance property key.

## Loading executable or DLL files


If your [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) attempts to load an unsigned executable file or DLL on a Windows 64-bit platform, the operating systems prevents it from being loaded in this secure environment.

To safely load an executable file or DLL by a class installer or co-installer, we highly recommended that the executable file or DLL is included in your digitally signed [driver package](driver-packages.md). For more information about how to sign driver packages, see [Driver Signing](driver-signing.md).

**Note**  Class installers and co-installers must not load DLL modules by explicit function calls, such as **LoadLibrary**, or by creating link dependencies.

 

## Starting other processes or services


During device installation, Windows cannot track additional processes and is unable to determine what they are doing or when they are finished. For example, Windows could start or stop the device or initiate a system restart while the process is performing a critical action.

In most cases, [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) should not start other processes or services. However, installers can start other processes safely by calling [CreateProcess](http://go.microsoft.com/fwlink/p/?linkid=194524) from a function or dialog that is displayed through a [finish-install action](finish-install-actions--windows-vista-and-later-.md). The installer must not let the user continue in the dialog or procedure until the created process has exited.

 

 





