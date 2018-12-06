---
title: Review the INX file
description: This topics shows you how to revise the INF file for the sample sensor driver, to make it suitable for installing your sensor driver on your target device.
ms.assetid: 1D326C5F-5B69-4C5C-AE52-14153DF964E9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Review the INX file


This topics shows you how to revise the INF file for the sample sensor driver, to make it suitable for installing your sensor driver on your target device.

Windows uses setup information files (also called INF files) as part of the process for installing device drivers. The INF file that was generated for the sample sensor driver is *ADXL345Acc.inf*. This file contains information that the Windows installation on the Sharks Cove will use when it installs the sensor driver for the accelerometer.

When you create a driver project in Microsoft Visual Studio, an INX file is first generated. When you revise this generic INX file and build your driver, the Build process converts the INX file into an INF file that will be used for installing your driver. Work your way through the following steps before you build your driver, to make sure that the Build process generates an INF file that you can use to install your sensor driver.

## Review the ADXL345Acc.inx file


Although you must review the INX file in its entirety, these steps will point out two important sections.

1. Click the *ADXL345Acc.inx* file to open it, and find the \[Version\] section, near the beginning of the file.
   ```cpp
   [Version]
   Class       = Sensor
   ClassGuid   = {5175D334-C371-4806-B3BA-71FD53C9258D}
   ```

Note that the device class is set to “sensor” and the appropriate GUID is provided. For more information about device class GUIDS for Windows, see [System-Defined Device Setup Classes Available to Vendors](https://docs.microsoft.com/windows-hardware/drivers/install/system-defined-device-setup-classes-available-to-vendors).

2. Find the \[ADXL345Acc\_Device.NT$ARCH$\] section.
   ```cpp
   [ADXL345Acc_Device.NT$ARCH$]
   ; DisplayName       Section          DeviceId
   ; -----------       -------          --------
   %ADXL345Acc_DevDesc% = ADXL345Acc_Inst, ACPI\ADXL345Acc
   ```

It is important to note that the value of the DeviceId in the preceding snippet (in this case, "ADXL345Acc") corresponds to the device name that is used to update the ‘hardware information’ file called the secondary system description table (SSDT).

If you're not installing the sample sensor driver on a mobile device, then after updating the relevant generic files, including the INX file, see [Build the sensor driver](build-the-sensor-driver.md), to see how to build the driver in Visual Studio. The build process generates your sensor driver files, including an INF file that Windows will use when you install the driver on the Sharks Cove.

## INF file for a mobile device


If you're using a mobile device, instead of the Sharks Cove, as your target device for testing the sample driver, then perform the following additional tasks to update the INF file.

1. In the *ADXL345Acc.inx* file, find the \[ADXL345Acc\_Inst.NT.HW\] section, and notice that it is empty.

**Important**  If you are not updating your INF file to be used on a mobile, then you must leave the \[ADXL345Acc\_Inst.NT.HW\] section empty. In that case, skip the tasks in this section and move on to the [Build the sensor driver](build-the-sensor-driver.md) topic.

 

2. Add the following code snippet to the empty section.

```cpp
[ADXL345Acc_Inst.NT.HW]
AddReg=Sensor_Inst_SecurityAddReg

[Sensor_Inst_SecurityAddReg]
HKR,,Security,,"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;S-1-5-84-0-0-0-0-0)"    ; Allow all UMDF drivers to access this driver
```

**Important**  Make a note of the value of the AddReg field, because it has to precisely match one of the values that you add to a file that you will update in the next step. From the preceding snippet example, you would make a note of *Sensor\_Inst\_SecurityAddReg*.

 

3. [Create a mobile package](creating-a-mobile-package.md) for installing the sample driver on your mobile device.

## Related topics

[Creating a mobile package](creating-a-mobile-package.md)



