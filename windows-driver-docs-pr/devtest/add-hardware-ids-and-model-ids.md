---
title: Add Hardware and Model IDs in the Device Metadata Authoring Wizard
description: Add Hardware and Model IDs in the Device Metadata Authoring Wizard
ms.assetid: 1BF563AE-B37B-4105-BA76-2D13F88B2BBD
keywords:
- Add Hardware and Model IDs in the Device Metadata Authoring Wizard
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Add Hardware and Model IDs in the Device Metadata Authoring Wizard


Hardware IDs identify a hardware function based on a bus-specific value and can be used to map device drivers to devices. For example, two devices with the same hardware ID share a functional interface that's used by the same driver. Hardware IDs are used to map device metadata packages to device instances on a specific bus or interface.

Model IDs allow the Original Equipment Manufacturer (OEM) or Independent Hardware Vendor (IHV) to uniquely identify the physical device independent of bus or interface technologies. For example, two devices with different model IDs might have the same hardware IDs for their components. Model IDs are used to map device metadata packages to physical devices, regardless of how the device connects to the computer.

To associate the Hardware IDs and Model IDs for your device metadata package, click the **Associations** tab.

### <span id="To_add_a_Hardware_ID_"></span><span id="to_add_a_hardware_id_"></span><span id="TO_ADD_A_HARDWARE_ID_"></span>To add a Hardware ID

1.  Click the **Associations** tab.
2.  Next to **Hardware ID**, click the **Plus Sign (+)**.
3.  In the box that appears, enter the Hardware ID.
    **Note**  If possible, use a value that contains your company's Vendor ID. For example: USB\\VID\_045E&PID\_0047

     

4.  Click **OK**.

### <span id="To_add_a_Model_ID_"></span><span id="to_add_a_model_id_"></span><span id="TO_ADD_A_MODEL_ID_"></span>To add a Model ID

1.  Click the **Associations** tab.
2.  Next to **Model ID**, click the **Plus Sign (+)**.
3.  In the box that appears, enter the GUID value for the Model ID.
4.  Click **OK**.

For detailed information about the Hardware ID for each device style, see the [Device Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226753).

 

 





