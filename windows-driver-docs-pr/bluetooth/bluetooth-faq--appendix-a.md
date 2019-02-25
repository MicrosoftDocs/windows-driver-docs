---
title: Installing an in-box Bluetooth driver on new hardware
description: This appendix describes the procedure for installing an in-box Bluetooth driver on new hardware in Windows Vista
ms.assetid: 399514FD-2BD8-4DC2-8446-F5EEB4120876
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





