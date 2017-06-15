---
title: Managing Device Performance States
author: windows-driver-content
description: Managing Device Performance States
MS-HAID:
- 'PwrMgmt\_30f43251-2eea-42bc-b499-9e89d1110a21.xml'
- 'kernel.managing\_device\_performance\_states'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5a4cc09a-e86e-4e5a-98b2-0351b253b5b6
keywords: ["power management WDK kernel , device performance states", "device performance states WDK power management", "performance states WDK power management", "custom power settings WDK power management"]
---

# Managing Device Performance States


Windows Vista features an enhanced power management infrastructure that makes it possible for driver stacks to better manage the power policy of their devices. Drivers can register to be notified when system-defined power settings change or when system power events occur. A device power policy owner can use these notifications to appropriately adjust the power usage of its devices. In addition, you can create custom power settings that provide access to device-specific power and performance features, which can be tightly-integrated into system power policy. The following are the two primary approaches to integrate device performance states and power-saving behaviors with system power policy.

[Creating Custom Power Settings for a Device](#creating-custom-power-settings-for-a-device)

[Registering to be Notified of a Change to the Active Power Scheme, Power Scheme Personality, or Power Source](#registering-to-be-notified-of-a-change-to-the-active-power-scheme)

### <a href="" id="creating-custom-power-settings-for-a-device"></a> Creating Custom Power Settings for a Device

You can define custom power settings that can be used to configure device performance states or power-saving behaviors. Information about the custom power settings is saved and managed by the power manager. Other components in the system—such as device drivers, services, or applications—can register to be notified when the value of a custom power setting changes. In general, devices that have the capability to tradeoff performance with power consumption should have corresponding custom power settings. Creating custom power settings is the most flexible approach to tightly integrate power consumption with system power policy and provides the following additional benefits:

-   A custom user interface is not required to make custom power settings accessible to a user. All power settings, including custom power settings, are presented to the user on the **Advanced Settings** page of the **Power Options** Control Panel.

-   Users and system administrators can easily script the configuration of custom power settings by using Powercfg.exe, the power management command-line tool.

-   Optionally, a system administrator can create an administrative template (.ADM) file that enables group policy-based configuration of new power settings.

An individual power setting contains all of the information that is required to uniquely identify, name, describe, and provide values for the power setting. Each power setting is defined with a GUID, a setting name, a description, and default settings for AC and DC power schemes. A custom power setting can be created statically for a device, by using an [**INF AddPowerSetting directive**](https://msdn.microsoft.com/library/windows/hardware/ff546313), or dynamically, by calling the Win32 power management functions that are included in the power management reference that is provided with Microsoft Windows SDK documentation.

Drivers call [**PoRegisterPowerSettingCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559727) to register a callback routine that the power manager calls to notify the driver of a change to a power setting. When the setting changes, the power manager calls the callback routine and passes the new setting value. Drivers can then take the action that is appropriate for the power setting. Each setting is identified by the GUID of the power setting. The system-defined GUIDs for power settings are defined in Wdm.h and Ntpoapi.h.

For example, to be notified when monitor power is turned on or off, a driver calls **PoRegisterPowerSettingCallback**, supplying the GUID that identifies the monitor power setting (GUID\_MONITOR\_POWER\_ON) and a pointer to the callback routine that the power manager calls when the value of the monitor power setting changes.

### <a href="" id="registering-to-be-notified-of-a-change-to-the-active-power-scheme"></a>Registering to be Notified of a Change to the Active Power Scheme, Power Scheme Personality, or Power Source

The personality of the active power scheme conveys the user's intent for the overall power saving behavior of the system. Every power scheme, including custom schemes, have a personality that indicates the overall intention of the scheme. This enables additional custom power schemes to be created while still providing all of the benefits of knowing the intent of the scheme. Windows Vista includes the following three system-defined power schemes and their corresponding personalities.

<a href="" id="maximum-power-savings"></a>**Maximum power savings**  
Reduces performance to minimize power consumption.

<a href="" id="automatic--balanced-"></a>**Automatic (balanced)**  
Lets the system choose the best power state level based on overall power consumption.

<a href="" id="maximum-performance-------"></a>**Maximum performance**   
Provides maximum performance regardless of power consumption.

The power source can be either an AC or a DC power source.

A device power policy owner can use information about the active power scheme, power scheme personality, and power source to adjust device power policy. For example, a device power policy owner might aggressively power down a device if the power scheme personality changes to **Maximum Power Savings**. However, if the power scheme personality changes to **Maximum Performance**, the device power policy owner might maintain the performance level of its devices rather than reduce power consumption, and possibly leave the device powered at all times to ensure the highest level of performance.

A driver can register to be notified when a change occurs to the active power scheme, the power scheme personality, or the power source. A driver calls **PoRegisterPowerSettingCallback** to register the callback routine that the power manager calls to notify the driver of such a change, as follows:

-   To register for notification of change to the active power scheme, supply the GUID that represents the setting for the power scheme (GUID\_ACTIVE\_POWERSCHEME). The power manager will then call the callback routine whenever the active power scheme changes, even if the personality of the new power scheme is the same as the previous power scheme.

-   To register for notification of a change to the power scheme personality, supply the GUID that represents the setting for the power scheme personality (GUID\_POWERSCHEME\_PERSONALITY). The power manager will then call the callback routine whenever the active power scheme changes and the personality of the new power scheme is different from the personality of the previous power scheme.

-   To register for notification of a change to the power source, supply the GUID that represents the setting for the power source (GUID\_ACDC\_POWER\_SOURCE). The power manager will then call the callback routine whenever the power source setting changes.

When the active power scheme changes or the power scheme personality changes, the power manager calls the callback routine and passes the GUID that represents the new power scheme or power scheme personality. Drivers can then take the action that is appropriate for the change.

The active power scheme setting and the power scheme personality setting use the following GUIDs to identify their respective values:

-   GUID\_MAX\_POWER\_SAVINGS, which corresponds to the **Maximum Power Savings** power scheme and its corresponding personality.

-   GUID\_MIN\_POWER\_SAVINGS, which corresponds to the **Maximum Performance** power scheme and its corresponding personality.

-   GUID\_TYPICAL\_POWER\_SAVINGS, which corresponds to the **Automatic (Balanced)** power scheme and its corresponding personality.

When the power source changes, the power manager calls the callback routine and passes the GUID that represents the power source setting and the value of the power source setting that indicates whether the computer is being powered by an AC power source, a DC power source, or a short-term DC power source.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Managing%20Device%20Performance%20States%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


