---
title: WDTF Runtime Library
description: Description of the WDTF Runtime Library, the tools it contains, and how to install.
ms.author: eliotgra
keywords:
- WDTF
- Windows Driver Test Framework
- WDTF Runtime
- Installing WDTF
- driver testing
ms.date: 08/14/2018
ms.localizationpriority: medium
---

# The WDTF runtime library

The WDTF runtime library is available as part of the Windows Driver Kit (WDK). When you install the WDK, you also install the Windows Driver Test Framework (WDTF). The templates and sample files for testing and development are installed along with the WDK. The WDTF runtime library needs to be installed on any system that you want to run WDTF-based tests on. This includes the tests provided in the WDK and tests you write using WDK test templates.

The WDK also includes a separate installation package (*.msi) that you can use to install the WDTF runtime on a test computer. The MSI does the following:

- Copies files.

- Adds registry keys.

- Registers WDTF objects.

- Install and uninstalls a log file.

The WDTF runtime library includes tools to help you triage and run tests.

|Name of tool or command script|Description|
|----|----|
|CheckWDTFInstall.cmd|Verifies that WDTF was installed correctly. Running this command creates the file CheckWDTFInstall.log, which contains information on all installed WDTF components.|
|DisplayDeviceClass.vbs|Displays device class information that exist on the current system. Both the Class GUID and Class Friendly name is shown. Useful when trying to create /DQ queries that look for certain class of devices.|
|DisplayDeviceDataFields.cmd|Displays device class information that exist on the current system. Both the Class GUID and Class Friendly name is shown. Useful when trying to create /DQ queries that look for certain class of devices.|
|DisplayDevices.vbs|Displays information about each device expressed by the /DQ parameter, the default is all device in the system. |
|DisplayDevicesWithWDTFilters.vbs|Displays any device that has one of the WDTF filter drivers installed on it. WDTF has three filter drivers: EDT, IOSPY, or the button driver.|
|DisplayDeviceTree.vbs|Displays the device tree of the current system.|
|DisplaySystemDataFields.cmd|Displays all the system namespaces and the fields they have.|

## How to install the WDTF runtime library

When you set up a test computer for deployment, the WDTF runtime library is installed on the test computer. Follow the instructions for the correct version of the WDK:

- [Provision a computer for driver deployment and testing (WDK 10 and WDK 8.1)](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1)

- [Provision a computer for driver deployment and testing (WDK 8)](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8)

You can also install the WDTF runtime library manually.

### Installing WDTF on a test computer (preferred method)

1. Install Visual Studio and then install the WDK.

2. Configure a remote computer for testing. In Visual Studio, click the **Driver** menu, point to **Test**, and then click **Configure Computers**.

### Manually installing WDTF on a test computer (alternative method)

1. Install Visual Studio and the WDK on the computer you use for development.

2. Copy the WDTF installation files from the computer where you installed the WDK to the test computer. The WDTF installation files (*.msi and *.cab files) are located in the %programfiles%\Windows Kits\10\Testing\Runtimes directory on your development system. Copy the all the files in the directory that matches the architecture of the test computer.

3. On the test computer, open a Command Prompt window using elevated permission (**Run as administrator**) and navigate to the directory that contains the WDTF installation files. Run either of the following commands to install WDTF.

    ```cmd
    msiexec /i "Windows Driver Testing Framework (WDTF) Runtime Libraries-x64_en-us.msi"
    ```

    -Or-

    ```cmd
    msiexec /i "Windows Driver Testing Framework (WDTF) Runtime Libraries-x86_en-us.msi"
    ```

The following table describes the options you can use with the **msiexec** command.

|Option|Description|
|----|----|
|**/l*** *filename*|Writes all messages and errors to a file, *filename*.|
|**WDTFDIR=**_CustomInstallationDirectory_|Specifies a destination directory for WDTF Runtimes. Default **WDTFDir** is %programfiles%\Windows Kits\10\Testing\Runtimes\WDTF|
|**WDTF_SKIP_MACHINE_CONFIG=[1 \| 2]**|Specify **1** to skip setting cscript.exe as the default script engine. Specify **2** to skip enabling AC and DC RTC wake.|
|**/?**|Shows help for msiexec.exe options.|

### Example

```cmd
msiexec /i "Windows Driver Testing Framework (WDTF) Runtime Libraries-x64_en-us.msi" /l* WDTFInstall.log WDTFDir=c:\wdtf WDTF_SKIP_MACHINE_CONFIG=1
```

## How to determine if the WDTF runtime library is installed on a compute

You can verify that WDTF was installed correctly by running a command script on the test computer. Running this command creates the file CheckWDTFInstall.log, which contains information on all installed WDTF components.

1. Open a Command Prompt window on the test computer.

2. Run `%WDTFDir%\Tools\CheckWDTFInstall.cmd`.

3. Open the log file CheckWDTFInstall.log and examine the results.

## How to uninstall the WDTF runtime library

When you set up a test computer for deployment, following the instructions [Provision a computer for driver deployment and testing (WDK 10)](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1), the WDTF runtime library is installed on the target computer.

You can remove the WDTF runtime library by removing provisioning from the target computer. For more information, see [Removing provisioning from the target computer](https://docs.microsoft.com/windows-hardware/drivers/develop/what-happens-when-you-provision-a-computer--wdk-8-1-#span-idremovingprovisioningfromthetargetcomputerspanspan-idremovingprovisioningfromthetargetcomputerspanspan-idremovingprovisioningfromthetargetcomputerspanremoving-provisioning-from-the-target-computer).

You can also uninstall the WDTF runtime library manually.

## Manually uninstalling WDTF on a test computer

1. On the test computer, go to **Settings** and then click **Apps**.

2. In **Programs and Features**, locate the Windows Driver Testing Framework (WDTF) Runtime Libraries, right click, and select **Uninstall**.
