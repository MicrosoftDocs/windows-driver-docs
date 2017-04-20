---
title: Installing an In-Box Bluetooth Driver on New Hardware
description: This appendix describes the procedure for forcing the Bluetooth driver that is included with Windows Vista to install on a new Bluetooth radio. Windows XP SP2 uses a similar procedure, although some of the details are different.
ms.assetid: 399514FD-2BD8-4DC2-8446-F5EEB4120876
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Appendix A: How to Install an In-Box Bluetooth Driver on New Hardware in Windows Vista


This appendix describes the procedure for forcing the Bluetooth driver that is included with Windows Vista to install on a new Bluetooth radio. Windows XP SP2 uses a similar procedure, although some of the details are different.

## <span id="Step_1__Start_Device_Manager_and_Select_the_Bluetooth_Radio"></span><span id="step_1__start_device_manager_and_select_the_bluetooth_radio"></span><span id="STEP_1__START_DEVICE_MANAGER_AND_SELECT_THE_BLUETOOTH_RADIO"></span>Step 1: Start Device Manager and Select the Bluetooth Radio


To start Device Manager:

1.  Click **Start**, navigate to **All Programs &gt; Accessories &gt; Command Prompt**, right-click **Command Prompt**, and then click **Run as administrator** to open a command window with elevated privileges.
2.  Type the following: **Devmgmt.msc**

Under **Other Devices**, find the entry for the Bluetooth radio on the Device Manager list of devices. In the following figure, the radio’s name is ”UGT”. On some portable computers, you might be required to first turn on the Bluetooth radio by using a key combination such as Fn+F5.

![bluetooth update driver software vista](images/bthnewhwstep1.jpg)

To verify that the selected device is a Bluetooth radio, right-click the device name and then click **Properties** to display the **Properties** dialog box. On the **Details** tab, verify that the device has the compatible ID for a Bluetooth radio:

USB\\Class\_e0&SubClass\_01&Prot\_01
### <span id="Step_2__Start_the_Update_Driver_Software_Wizard"></span><span id="step_2__start_the_update_driver_software_wizard"></span><span id="STEP_2__START_THE_UPDATE_DRIVER_SOFTWARE_WIZARD"></span>Step 2: Start the Update Driver Software Wizard

Right-click the Bluetooth radio node and then click **Update Driver Software**. To go to the page in the following figure, click **Browse my computer for driver software**. To manually select a driver, click **Let me pick from a list of device drivers on my computer**.

![bluetooth update driver software vista](images/bthnewhwstep2.jpg)

### <span id="Step_3__Select_the_Generic_Bluetooth_Driver"></span><span id="step_3__select_the_generic_bluetooth_driver"></span><span id="STEP_3__SELECT_THE_GENERIC_BLUETOOTH_DRIVER"></span>Step 3: Select the Generic Bluetooth Driver

The Update Driver Software Wizard next displays a list of available drivers. Select **Bluetooth Radios** and then select a Bluetooth radio that matches your system, as shown in the following figure. If you are not sure which driver to use, you can use the generic driver for testing. To do this, select **Generic Adapter** as manufacturer and **Generic Bluetooth Adapter** as the model.

![bluetooth update driver software vista](images/bthnewhwstep3.jpg)

After you select a driver, the wizard asks you to confirm that you want to install the specified driver on the new Bluetooth radio. If you try to install a Bluetooth driver on a device that is not a Bluetooth radio, the driver will probably not start.

If the driver loads correctly, Device Manager should have a Generic Bluetooth Adapter entry under the Bluetooth Radios node, as shown in the following figure.

![bluetooth update driver software vista](images/bthnewhwstep4.jpg)

If the driver failed to start, for example, if Windows returned a start error code, examine the event log to help determine the cause.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Appendix%20A:%20How%20to%20Install%20an%20In-Box%20Bluetooth%20Driver%20on%20New%20Hardware%20in%20Windows%20Vista%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




