---
title: AllSignersEqual Group Policy
description: AllSignersEqual Group Policy
ms.assetid: b23eed87-76ce-4447-86d2-2be370ee57c5
keywords: ["driver selections WDK device installations , AllSignersEqual group policy", "locating drivers for device installation WDK device installations , AllSignersEqual group policy", "searching for drivers during device installation WDK device installations , AllSignersEqual group policy", "AllSignersEq"]
---

# AllSignersEqual Group Policy


If the **AllSignersEqual** Group Policy is disabled, Windows ranks drivers signed by a Windows signing authority (Microsoft signature) better than drivers that have one of the following:

-   An [Authenticode](authenticode.md) signature.

-   A Microsoft signature for a Windows version earlier than the [LowerLogoVersion](lowerlogoversion.md) value of the driver's [device setup class](device-setup-classes.md).

If the **AllSignersEqual** Group Policy is disabled, Windows selects a driver signed by a Windows signing authority over an Authenticode-signed driver, even if the Authenticode-signed driver is otherwise a better match to a device.

Signatures from a Windows signing authority are ranked equally and include the following signature types:

-   Premium WHQL signatures and standard WHQL signatures

-   Signatures for inbox drivers

-   Windows Sustained Engineering (SE) signatures

-   A WHQL signature for a Windows version that is the same or later than the [LowerLogoVersion](lowerlogoversion.md) value of the driver's [device setup class](device-setup-classes.md).

A network administrator can change this behavior by enabling the **AllSignersEqual** Group Policy. This configures Windows to treat all Microsoft signature types and Authenticode signatures as equal with respect to rank when selecting the driver that is the best match to a device.

**Note**  Starting with Windows 7, the **AllSignersEqual** Group Policy is enabled by default.

 

For example, consider the situation where a network administrator has to configure client computers on a network to install drivers as follows:

-   A client computer should install a new driver only if the driver has an Authenticode signature that is issued by an Enterprise Certificate Authority (CA) that is created for the network. An enterprise might want to do this in order to ensure that all drivers that are installed on client computers are signed and that the only trusted signing authority other than Microsoft is the CA managed by the enterprise.

-   For signed drivers, the signature score should not be used to determine the driver that has the best rank. Only the sum of the feature score and identifier score is used to compare driver ranks. For example, if the sum of the feature score and identifier score of a new driver is lower than the corresponding sum of an inbox driver, Windows installs the new driver.

To accomplish this, a network administrator:

-   Adds an Enterprise CA certificate to the Trusted Publisher Store of the client computers.

-   Enables the **AllSignersEqual** Group Policy on the client computers.

After the network administrator configures the client computers in this manner, the administrator can sign the driver that has the Enterprise CA certificate and distribute the driver to the client computers. In this configuration, Windows on client computers will install the new driver for a device instead of a Microsoft-signed driver if the sum of the feature score and the identifier score is lower than the corresponding sum for the Microsoft-signed driver.

Follow these steps to configure the AllSignersEqual Group Policy on Windows Vista and later versions of Windows:

1.  On the Start menu, click **Run.**

2.  Enter **GPEdit.msc** to execute the Group Policy editor, and click **OK**.

3.  In the left pane of the Group Policy editor, click **Computer Configuration**.

4.  On the **Administrative Templates** page, double-click **System**.

5.  On the **System** page, double-click **Device Installation**.

6.  Select **Treat all digitally signed drivers equally in the driver ranking and selection process** and then click **Properties**.

7.  On the **Settings** tab, select **Enabled** (to enable the **AllSignersEqual** Group Policy) or **Disabled** (to disable the **AllSignersEqual** Group Policy).

To ensure that the settings are updated on the target system, do the following:

1.  Create a desktop shortcut to *Cmd.exe*, right-click the *Cmd.exe* shortcut, and select **Run as administrator**.

2.  From the Command Prompt window, run the Group Policy update utility, *GPUpdate.exe*.

This configuration change is made one time and applies to all subsequent driver installations on the computer until AllSignersEqual is reconfigured.

For more information about driver ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20AllSignersEqual%20Group%20Policy%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




