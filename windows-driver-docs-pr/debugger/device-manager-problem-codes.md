---
title: Device Manager Problem Codes
description: Device Manager Problem Codes
ms.assetid: d08c3dd1-ab2e-4ce6-8bf7-9634c0a5be1f
keywords: ["Plug and Play (PnP), device manager problem codes", "device manager problem codes", "CM_PROB_XXX"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Manager Problem Codes


The Device Manager marks a device with a yellow exclamation mark (!) when the device has a problem. The problem codes are in the form CM\_PROB\_*XXX* and are defined in the header file cfg.h. The most important are explained here, together with their mapping to the [Device Node Status Flags](device-node-status-flags.md). For a more comprehensive list, please see [Device Manager Error Messages](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/device-manager-error-messages).

<span id="Code_1__CM_PROB_NOT_CONFIGURED_"></span><span id="code_1__cm_prob_not_configured_"></span><span id="CODE_1__CM_PROB_NOT_CONFIGURED_"></span>**Code 1 (CM\_PROB\_NOT\_CONFIGURED)**  
Indicates that the device is not installed and was not installed previously. (Corresponds to DNF\_NOT\_CONFIGURED.)

<span id="Code_10__CM_PROB_FAILED_START_"></span><span id="code_10__cm_prob_failed_start_"></span><span id="CODE_10__CM_PROB_FAILED_START_"></span>**Code 10 (CM\_PROB\_FAILED\_START)**  
Indicates that the device did not start for some reason, but the I/O Manager attempted to start it with a set of resources. (Corresponds to DNF\_START\_FAILED.)

<span id="Code_12__CM_PROB_NORMAL_CONFLICT_"></span><span id="code_12__cm_prob_normal_conflict_"></span><span id="CODE_12__CM_PROB_NORMAL_CONFLICT_"></span>**Code 12 (CM\_PROB\_NORMAL\_CONFLICT)**  
Indicates that there were not sufficient resources to start this device. (Corresponds to DNF\_INSUFFICIENT\_RESOURCES.)

<span id="Code_14__CM_PROB_NEED_RESTART_"></span><span id="code_14__cm_prob_need_restart_"></span><span id="CODE_14__CM_PROB_NEED_RESTART_"></span>**Code 14 (CM\_PROB\_NEED\_RESTART)**  
Indicates that user mode reconfigured the device and a reboot is required for the changes to take effect. (Corresponds to DNF\_NEED\_RESTART.)

<span id="Code_18__CM_PROB_REINSTALL_"></span><span id="code_18__cm_prob_reinstall_"></span><span id="CODE_18__CM_PROB_REINSTALL_"></span>**Code 18 (CM\_PROB\_REINSTALL)**  
Indicates that the device needs to be installed and was installed previously. (Corresponds to DNF\_REINSTALL.)

<span id="Code_21__CM_PROB_WILL_BE_REMOVED_"></span><span id="code_21__cm_prob_will_be_removed_"></span><span id="CODE_21__CM_PROB_WILL_BE_REMOVED_"></span>**Code 21 (CM\_PROB\_WILL\_BE\_REMOVED)**  
Indicates that the user mode uninstalled this device. (Corresponds to DNF\_WILL\_BE\_REMOVED.)

<span id="Code_22__CM_PROB_DISABLED_"></span><span id="code_22__cm_prob_disabled_"></span><span id="CODE_22__CM_PROB_DISABLED_"></span>**Code 22 (CM\_PROB\_DISABLED)**  
Indicates that the device is disabled. (Corresponds to DNF\_DISABLED.)

<span id="Code_28__CM_PROB_FAILED_INSTALL_"></span><span id="code_28__cm_prob_failed_install_"></span><span id="CODE_28__CM_PROB_FAILED_INSTALL_"></span>**Code 28 (CM\_PROB\_FAILED\_INSTALL)**  
Indicates that the installation failed and there is no driver selected for this device, although the kernel did not report a problem (and there is no DNF\_XXX match for this the problem). This problem can be the result of an on-board system device (ISA timer, ISA RTC, RAM Memory, and so forth) that does not yet have an INF file.

<span id="Code_31__CM_FAILED_ADD_"></span><span id="code_31__cm_failed_add_"></span><span id="CODE_31__CM_FAILED_ADD_"></span>**Code 31 (CM\_FAILED\_ADD)**  
Indicates that the device was not added. Reasons for the failure may include: a driver's **AddDevice** routine returned an error, there is no service listed for the device in the registry, there is more than one service listed, or the controlling driver could not be loaded. (Corresponds to DNF\_ADD\_FAILED.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Device%20Manager%20Problem%20Codes%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




