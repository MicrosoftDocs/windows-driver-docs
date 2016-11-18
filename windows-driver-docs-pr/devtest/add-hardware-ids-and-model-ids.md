---
title: Add Hardware and Model IDs in the Device Metadata Authoring Wizard
description: Add Hardware and Model IDs in the Device Metadata Authoring Wizard
ms.assetid: 1BF563AE-B37B-4105-BA76-2D13F88B2BBD
keywords: ["Add Hardware and Model IDs in the Device Metadata Authoring Wizard"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\dma]:%20Add%20Hardware%20and%20Model%20IDs%20in%20the%20Device%20Metadata%20Authoring%20Wizard%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




