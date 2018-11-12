---
title: Video Miniport Driver Initialization (Windows 2000 Model)
description: Video Miniport Driver Initialization (Windows 2000 Model)
ms.assetid: b18b5483-f11f-4533-9434-a3a4a30fb4b2
keywords:
- video miniport drivers WDK Windows 2000 , initializing
- initializing video miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Miniport Driver Initialization (Windows 2000 Model)


## <span id="ddk_video_miniport_driver_initialization_windows_2000_model__gg"></span><span id="DDK_VIDEO_MINIPORT_DRIVER_INITIALIZATION_WINDOWS_2000_MODEL__GG"></span>


Video miniport driver initialization occurs after the NT kernel, [*HAL*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hal), and core drivers, such as the PCI bus driver, are loaded and initialized. The basic system initialization sequence occurs as follows:

1.  The NT kernel and HAL are loaded and initialized.

2.  Core drivers such as the PCI bus driver are loaded and initialized.

3.  The PCI bus driver obtains PCI resource information and the device ID and vendor ID from each of its children's PCI configuration spaces and reports this information back to the system.

4.  If the PnP manager recognizes the device and vendor IDs, the I/O manager loads the corresponding video miniport driver and the video port driver from a known location. If the PnP manager does not recognize the IDs, it prompts the user for the location of the miniport driver and loads it from this location.

5.  The I/O manager calls the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556159) routine with two system-supplied input pointers. **DriverEntry** allocates and initializes a [**VIDEO\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff570505) structure with driver-specific and adapter-specific values, including pointers to the miniport driver's other entry points. **DriverEntry** must also claim any legacy resources, which are those resources not listed in the device's PCI configuration space but that are decoded by the device. See [Claiming Legacy Resources](claiming-legacy-resources.md) for details.

6.  The miniport driver's **DriverEntry** function calls [**VideoPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff570320). **VideoPortInitialize** performs those aspects of miniport driver initialization that are common to all miniport drivers. For example, for non-PnP drivers, **VideoPortInitialize** verifies portions of the miniport driver-initialized VIDEO\_HW\_INITIALIZATION\_DATA structure, initializes some of the public members of the system-created device object, allocates memory for the device extension of the device object, and collects and stores pertinent information in the device extension. See [Video Miniport Driver's Device Extension (Windows 2000 Model)](video-miniport-driver-s-device-extension--windows-2000-model-.md) for more details about device extensions. For PnP drivers, the device object-related actions occur at a later time.

7.  When **VideoPortInitialize** returns, **DriverEntry** propagates the return value of **VideoPortInitialize** back to the caller. Miniport driver writers should make no assumptions about the value returned by **VideoPortInitialize**.

At this point, the system has loaded and initialized the video miniport driver. The next step is for the PnP manager to start the device. See [Starting the Device of the Video Miniport Driver](starting-the-device-of-the-video-miniport-driver.md) for details.

 

 





