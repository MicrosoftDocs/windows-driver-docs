---
title: AllSigningEqual Group Policy
description: AllSigningEqual Group Policy
keywords:
- driver selections WDK device installations , AllSigningEqual group policy
- locating drivers for device installation WDK device installations , AllSigningEqual group policy
- searching for drivers during device installation WDK device installations , AllSigningEqual group policy
- AllSigningEq
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AllSigningEqual Group Policy

If the **AllSigningEqual** Group Policy is disabled, Windows ranks [driver packages](driver-packages.md) signed by a Windows signing authority (Microsoft signature) better than driver packages that have one of the following:

-   An [Authenticode](authenticode.md) signature.

-   A Microsoft signature for a Windows version earlier than the [LowerLogoVersion](lowerlogoversion.md) value of the driver package's [device setup class](./overview-of-device-setup-classes.md).

If the **AllSigningEqual** Group Policy is disabled, Windows selects a driver package signed by a Windows signing authority over an Authenticode-signed driver package, even if the Authenticode-signed driver package is otherwise a better match to a device.

Signatures from a Windows signing authority are ranked equally and include the following signature types:

-   Premium WHQL signatures and standard WHQL signatures

-   Signatures for inbox driver packages

-   Windows Sustained Engineering (SE) signatures

-   A WHQL signature for a Windows version that is the same or later than the [LowerLogoVersion](lowerlogoversion.md) value of the driver package's [device setup class](./overview-of-device-setup-classes.md).

A network administrator can change this behavior by enabling the **AllSigningEqual** Group Policy. This configures Windows to treat all Microsoft signature types and Authenticode signatures as equal with respect to rank when selecting the driver package that is the best match to a device.

**Note**  Starting with Windows 7, the **AllSigningEqual** Group Policy is enabled by default.

For example, consider the situation where a network administrator has to configure client computers on a network to install driver packages as follows:

-   A client computer should install a new driver package only if the driver package has an Authenticode signature that is issued by an Enterprise Certificate Authority (CA) that is created for the network. An enterprise might want to do this in order to ensure that all driver packages that are installed on client computers are signed and that the only trusted signing authority other than Microsoft is the CA managed by the enterprise.

-   For signed driver packages, the signature score should not be used to determine the driver package that has the best rank. Only the sum of the feature score and identifier score is used to compare driver package ranks. For example, if the sum of the feature score and identifier score of a new driver is lower than the corresponding sum of an inbox driver, Windows installs the new driver package.

To accomplish this, a network administrator:

-   Adds an Enterprise CA certificate to the Trusted Publisher Store of the client computers.

-   Enables the **AllSigningEqual** Group Policy on the client computers.

After the network administrator configures the client computers in this manner, the administrator can sign the driver package that has the Enterprise CA certificate and distribute the driver to the client computers. In this configuration, Windows on client computers will install the new driver package for a device instead of a Microsoft-signed driver package if the sum of the feature score and the identifier score is lower than the corresponding sum for the Microsoft-signed driver package.

Follow these steps to configure the AllSigningEqual Group Policy on Windows Vista and later versions of Windows:

1.  On the Start menu, click **Run.**

2.  Enter **GPEdit.msc** to execute the Group Policy editor, and click **OK**.

3.  In the left pane of the Group Policy editor, click **Computer Configuration**.

4.  On the **Administrative Templates** page, double-click **System**.

5.  On the **System** page, double-click **Device Installation**.

6.  Select **Treat all digitally signed drivers equally in the driver ranking and selection process** and then click **Properties**.

7.  On the **Settings** tab, select **Enabled** (to enable the **AllSigningEqual** Group Policy) or **Disabled** (to disable the **AllSigningEqual** Group Policy).

To ensure that the settings are updated on the target system, do the following:

1.  Create a desktop shortcut to *Cmd.exe*, right-click the *Cmd.exe* shortcut, and select **Run as administrator**.

2.  From the Command Prompt window, run the Group Policy update utility, *GPUpdate.exe*.

This configuration change is made one time and applies to all subsequent driver package installations on the computer until AllSigningEqual is reconfigured.

For more information about driver package ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).
