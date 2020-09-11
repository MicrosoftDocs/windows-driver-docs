---
title: Customize the Component Firmware Update (CFU) inbox HIDCFU driver INF
description: Customize the Component Firmware Update (CFU) inbox HIDCFU driver INF
ms.date: 09/01/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Customize the Component Firmware Update (CFU) inbox HIDCFU driver INF

Component Firmware Update (CFU) allows OEMs and IHVs to seamlessly and securely update firmware for components connected through interconnect buses such as USB, Bluetooth, I<sup>2</sup>C, and so on. As part of the open-source effort, we are sharing a CFU protocol specification, sample CFU driver, and firmware sample code to allow device manufacturers to push firmware updates over Windows Update.

## Contents

- [Before you begin](#before-you-begin)

- [Overview](#overview)

- [Customize the CFU driver sample](#customize-the-cfu-driver-sample)

  - [2 Configure the CFU driver INF](#2-configure-the-cfu-driver-inf)

  - [4 Deploy the package through Windows Update](#4-deploy-the-package-through-windows-update)

- [Firmware file format](#firmware-file-format)

  - [Offer format](#offer-format)

  - [Payload format](#payload-format)

  - [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry)

  - [Firmware update status provided by the driver](#firmware-update-status-provided-by-the-driver)

- [Sample INF file for the HIDCFU inbox driver](#sample-inf-file-for-the-hidcfu-inbox-driver)

- [Troubleshooting tips](#troubleshooting-tips)

- [FAQ](#faq)

- [Additional resources](#additional-resources)

## Before you begin

The following resources will help you learn about the Component Firmware Update (CFU) protocol.

- [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456)

- [WinHEC 2018 video on Component Firmware Update](https://developer.microsoft.com/windows/hardware/events)

- The [Component Firmware Update (CFU) Protocol Specification](cfu-specification.md) describes a generic HID protocol to update firmware for components present on a PC or accessories. The specification allows for a component to accept firmware without interrupting the device operation during a download.

- [CFU resources on GitHub](https://github.com/Microsoft/CFU)

  - [Firmware](https://github.com/Microsoft/CFU/tree/master/Firmware) contains sample firmware source code for implementing the CFU protocol.

  - [Component Firmware Update Driver](https://github.com/microsoft/CFU/tree/master/Host/ComponentFirmwareUpdateDriver) is a sample UMDF driver that talks to the device using the HID protocol. As a firmware developer, you can customize the driver for the purposes of adopting the CFU model to enable firmware updates for your components.
  
  - [Component Firmware Update Standalone Tool Sample](https://github.com/microsoft/CFU/tree/master/Tools/ComponentFirmwareUpdateStandAloneToolSample) contains the standalone tool sample used with CFU.

## Overview

To update the firmware image for your device by using the CFU model, you should expect to meet the following requirements:

- Provide a CFU driver. This driver sends the firmware update to the device. We recommend that you customize the sample CFU driver to support your firmware update scenarios.

- Your device must ship with a firmware image that is compliant with the CFU protocol so that it can accept an update from the CFU driver.

- Your device must expose itself as a HID device to the operating system (running the CFU driver) and expose a HID Top-Level Collection (TLC). The CFU driver loads on the TLC and sends the firmware update to the device.

This allows you to service your in-market devices through Windows Update. To update the firmware for a component, you deploy the CFU driver through the Windows update, and the driver gets installed on a Windows host. When the driver detects the presence of a component, it performs the necessary actions on the host and transmits the firmware image to the primary component on the device.

![CFU firmware update](images/transfer-flowchart.png)

## Customize the CFU driver INF sample

Configure the CFU driver INF to meet your needs.

1. Update the INF with the hardware ID of the HID TLC intended for firmware update.
Windows ensures that the driver is loaded when the component is enumerated on the host.

1. Update the INF with hardware IDs of your devices. Replace the hardware ID in in this section with hardwareID(s) of all your supported devices.
  
        ```inf
        ; Target the Hardware ID for your devices.
        ;
        [Standard.NT$ARCH$]
        %ComponentFirmwareUpdate.DeviceDesc%=ComponentFirmwareUpdate, HID\HID\VID_abc&UP:def_U:ghi ; Your HardwareID- Laptop MCU

        %ComponentFirmwareUpdate.DeviceDesc%=ComponentFirmwareUpdate, HID\HID\VID_jkl&UP:mno_U:pqr ; Your HardwareID- Dock MCU
        ```

1. Update the **SourceDisksFiles** and **CopyFiles** sections to reflect all the firmware files. To see an example, see [DockFirmwareUpdate.inx](https://github.com/Microsoft/CFU/blob/master/Host/ComponentizedPackageExample/DockFWUpdate/DockFirmwareUpdate.inx)

    > [!NOTE]
    > When the package(s) gets installed, the OS replaces the `%13%` with the full path to the files before creating the registry values. Thus, the driver able to enumerate the registry and identify all the firmware image and offer files.

1. Specify device capabilities in the INF.

    The sample driver provides a way to customize the driver behavior to optimize for certain scenarios. Those settings are controlled through registry settings, described [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry).

    For example, the sample driver requires information about the underlying bus protocol to which the device is connected. The protocol can be specified through registry settings.

    Device capabilities are specified in the device specific firmware file.

### 4 Deploy the package through Windows Update

Next, deploy the package through Windows Update.

For information about deployment, see:

[Windows 10 Driver Publishing Workflow](https://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx)

## Firmware update image file format

The firmware update image has two parts: an offer file and a payload file. The offer contains necessary information about the payload to allow the primary component in the device that is receiving the update to decide if the payload is acceptable. The payload is a range of addresses and bytes that the primary component can consume.

### Offer format

The offer file is a 16-byte binary data whose structure must match the format specified in section 5.5.1 of the CFU protocol specification.

### Payload format

The payload file is a binary file which a collection of records that are stored contiguously. Each record is of the following format.

| Offset | Size | Value | Description |
|--|--|--|--|
| Byte 0 | DWORD | Firmware Address | Little Endian (LSB First) Address to write the data. The address is 0-based. Firmware could use this as an offset to determine the address as needed when placing the image in memory. |
| Byte 4 | Byte | Length | Length of payload data. |
| Byte 5-N | Bytes | Data | Byte array of payload data. |

### Configure device capabilities in the registry

You may configure each of these registries per component as needed.

| Registry Value | Description |
|--|--|
| **SupportResumeOnConnect** | Does this component support resume from a previously interrupted update?<p>You can enable this feature if the component can continue to receive payload data starting at a point where it was interrupted earlier. </p><p>When this value is set, during the payload transfer stage, the driver checks to see whether a previous transfer of this payload was interrupted. If it was interrupted, it the driver only sends the payload data from the interrupted point instead of the entire payload. </p><p>Set to 1 to enable and 0 (default) to disable.</p> |
| **SupportProtocolSkipOptimization** | <p>Does this component support skipping the entire protocol transaction for an already known all up to date firmware? </p><p>This is a driver side optimization option. If enabled, the driver checks these conditions during each initialization:<p><ul><li>Were all offers rejected in a previous cycle. </li><li>Does the current offers match the set of offers that the driver offered earlier.</li><ul></p><p>When the preceding conditions are satisfied, the driver skips the whole protocol transaction. <p>Set to 1 to enable and 0 (default) to disable.</p> |
| **Protocol** | Specify these values based on the underlying HID transport for your component.<p>If your component is connected by HID-Over-USB, specify 1. (Default)</p><p>If your component is connected by HID-Over-Bluetooth, specify value 2.</p> |

### Firmware update status provided by the driver

During the protocol transaction, the CFU driver writes registry entries to indicate the status.  This table describes the name, format of values and meaning of values that the driver touches during various stages of the protocol.

- \_ID_ in the table represents the Component ID, that is retrieved from the offer file. As specified in the specification, Component ID uniquely identify each component.

- For information about the DWORD, refer to the specification.

| Stage | Location | Reg Value Name | Value (DWORD) |
|--|--|--|--|
| Start; Pre Offer. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*CurrentFwVersion" | Version from device |
|  | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_NOT_STARTED |
| Offer; About to send offer. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*OfferFwVersion" | Version that is sent (or about to be send) to the device. |
| Offer Response (Rejected) | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatusRejectReason" | Reason for rejection returned by device. |
| Offer Response (Device Busy) | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_BUSY_PROCESSING_UPDATE |
| Offer Response (Accepted); About to send Payload. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_DOWNLOADING_UPDATE |  |
| Payload Accepted. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_PENDING_RESET |
| Error at any stage. | {Device Hardware key}\ComponentFirmwareUpdate | "Component*ID*FirmwareUpdateStatus" | FIRMWARE_UPDATE_STATUS_ERROR |

## Sample INF file for the HIDCFU inbox driver

    ```inf
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; File:               CfuVirtualHidDeviceFwUpdate.inx
    ;
    ; Description:        Driver installation file for Cfu Virtual Hid Device firmware update.
    ;
    ; Copyright (C) Microsoft Corporation.  All Rights Reserved.
    ; Licensed under the MIT license.
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    
    [Version]
    Signature="$Windows NT$"
    Class=Firmware
    ClassGuid={f2e7dd72-6468-4e36-b6f1-6488f42c1b52}
    Provider=%ManufacturerName%
    CatalogFile=CfuVirtualHidDeviceFwUpdate.cat
    DriverVer = 12/16/2019,11.42.16.703
    PnPLockDown=1
    
    [SourceDisksNames]
    1= %DiskName%
    
    [DestinationDirs]
    CfuVirtualHidDeviceFwUpdate.CopyFiles=13
    
    [Manufacturer]
    %ManufacturerName%=Standard,NTamd64
    
    [Standard.NTamd64]
    %CfuVirtualHidDeviceFwUpdate.DeviceDesc%=CfuVirtualHidDeviceFwUpdate, HID\VID_045E&UP:FA00_U:00F5 ; HardwareID for VirtualHidDevice MCU
    
    [CfuVirtualHidDeviceFwUpdate.NT]
    Include            = HidCfu.inf
    Needs              = HidCfu.NT
    CopyFiles          = CfuVirtualHidDeviceFwUpdate.CopyFiles
    
    [CfuVirtualHidDeviceFwUpdate.NT.Wdf]
    Include            = HidCfu.inf
    Needs              = HidCfu.NT.Wdf
    
    [CfuVirtualHidDeviceFwUpdate.NT.HW]
    AddReg = CfuVirtualHidDeviceFwUpdate_HWAddReg
    
    [CfuVirtualHidDeviceFwUpdate_HWAddReg]
    HKR,,FriendlyName,,%FwUpdateFriendlyName%
    HKR,,Alignment,0x00010001, 1                       ; (No Alignment)
    HKR,,OfferInputValueCapabilityUsageRangeMinimum,0x00010001,0x1A
    HKR,,OfferOutputValueCapabilityUsageRangeMinimum,0x00010001, 0x1E
    HKR,,PayloadInputValueCapabilityUsageRangeMinimum,0x00010001,0x26
    HKR,,PayloadOutputValueCapabilityUsageRangeMinimum,0x00010001,0x31
    HKR,,VersionsFeatureValueCapabilityUsageRangeMinimum,0x00010001, 0x42
    
    ; Specify the location of the firmware offer and payload file in the registry.
    ; The files are kept in driver store. When deployed, %13% would be expanded to the actual path
    ; in driver store.
    ;
    ; You can change subkey name under CFU (e.g. "CfuVirtualHidDevice_MCU"), and specify your own offer
    ; (e.g. "CfuVirtualHidDevice_MCU.offer.bin") and payload (e.g "CfuVirtualHidDevice_MCU.payload.bin") file name.
    ;
    HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_MCU,Offer,   0x00000000, %13%\CfuVirtualHidDevice_MCU.offer.bin
    HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_MCU,Payload, 0x00000000, %13%\CfuVirtualHidDevice_MCU.payload.bin
    HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_Audio,Offer,   0x00000000, %13%\CfuVirtualHidDevice_Audio.offer.bin
    HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_Audio,Payload, 0x00000000, %13%\CfuVirtualHidDevice_Audio.payload.bin
    
    [SourceDisksFiles]
    CfuVirtualHidDevice_MCU.offer.bin=1
    CfuVirtualHidDevice_MCU.payload.bin=1
    CfuVirtualHidDevice_Audio.offer.bin=1
    CfuVirtualHidDevice_Audio.payload.bin=1
    
    [CfuVirtualHidDeviceFwUpdate.CopyFiles]
    CfuVirtualHidDevice_MCU.offer.bin
    CfuVirtualHidDevice_MCU.payload.bin
    CfuVirtualHidDevice_Audio.offer.bin
    CfuVirtualHidDevice_Audio.payload.bin
    
    [CfuVirtualHidDeviceFwUpdate.NT.Services]
    Include            = HidCfu.inf
    Needs              = HidCfu.NT.Services
    
    ; =================== Generic ==================================
    
    [Strings]
    ManufacturerName="Surface"
    CfuVirtualHidDeviceFwUpdate.DeviceDesc = "CfuVirtualHidDevice Firmware Update"
    DiskName = "CfuVirtualHidDevice Firmware Update Installation Disk"
    FwUpdateFriendlyName= "CfuVirtualHidDevice Firmware Update"
    ```

## Troubleshooting tips

1. Check WPP logs to see the driver side interaction per component.

1. Check the event logs for any critical errors.

1. Check the book keeping registry entries described in Firmware update status provided by the driver.

## FAQ

**I have a component A that needs an update, how can I make the CFU driver aware of component A?**

You need to [configure the CFU driver INF](#2-configure-the-cfu-driver-inf) by using the hardware ID of the TLC created by component A.

**My company ships several independent components that I want to update by using the CFU model. Do I need separate drivers and package them individually?**

Use the componentized packages approach described in [Create componentized packages](#1-create-componentized-packages) .

**I have two components: component A, and a sub-component B. How should I make the CFU driver aware of component B?**

You don't need to. The driver doesn't need to know about the component hierarchy. It interacts with the primary component.

**How can I make the driver aware about my firmware files (offer, payload) file that I need to send to my component A?**

The firmware file information is set in the INF as registry values. [configure the CFU driver INF](#2-configure-the-cfu-driver-inf) .

**I have many firmware files, multiple offer, payload, for main component A and its subcomponents. How should I make the driver aware of which firmware file is meant for which component?**

The firmware file information is set in the INF as registry values. See Step 3 in [configure the CFU driver INF](#2-configure-the-cfu-driver-inf).

**I have inbuilt component A and peripheral component B that needs an update. How should I make the driver aware of this?**

You do not need to make the driver aware of the component in this case. The driver automatically handles this for you.

**Component A uses HID-Over-USB, component B is uses HID-Over-Bluetooth. How should I pass this information to the driver?**

Specify the correct capability by using the registry **Protocol** value. See [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry) for details.

**I am reusing the same driver for my components, are there any other customizations possible per usage scenarios?**

There are certain optimization settings that the driver allows. Those are configured in the registry. See [Configure device capabilities in the registry](#configure-device-capabilities-in-the-registry) for details.

**I am using the driver for firmware updates.  How do I know an update has succeeded?**

The firmware update status is updated by the driver in the registry as part of book-keeping.

## Additional resources

Learn about developing Windows drivers by using Windows Driver Foundation (WDF):

- [Developing Drivers with Windows Driver Foundation](https://docs.microsoft.com/windows-hardware/drivers/wdf/developing-drivers-with-wdf), written by Penny Orwick and Guy Smith

- [Using WDF to Develop a Driver](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-framework-to-develop-a-driver)

## CFU registry values

| Registry value | Description |
|--|--|
| Alignment | Protocol Attribute: What is the bin record alignment required for this configuration?<p>During payload send phase of the protocol, the driver fills in many Hid buffers with the payload and send to firmware one by one.<p>This option control the alignment requirement when packing the payload.<p>By default 8 byte alignment is used. If no alignment is required, configure this as 1. |
| UseHidSetOutputReport | 0 - Driver will use Write request while sending any output report.<p>1 - Driver will use IOCTL_HID_SET_OUTPUT_REPORT for sending any output report.<p>Default is 0. Set this to 1 if your underlying transport is not USB (for example, HID Over BTH). |
| OfferInputValueCapabilityUsageRangeMinimum | Value Capability Usage Minimum for Offer Input Report Handling. See Notes below. |
| OfferOutputValueCapabilityUsageRangeMinimum | Value Capability Usage Minimum for Offer Output Report Handling. See Notes below. |
| PayloadInputValueCapabilityUsageRangeMinimum | Value Capability Usage Minimum for Payload Input Report Handling. See Notes below. |
| PayloadOutputValueCapabilityUsageRangeMinimum | Value Capability Usage Minimum for Payload Output Report Handling. See Notes below. |
| VersionsFeatureValueCapabilityUsageRangeMinimum | Value Capability Usage Minimum for Version Feature Report Handling. See Notes below. |

## Notes on Value Capability

In order for the inbox driver to communicate with the firmware (real/virtual), the Value capability Usages specified in the INF should match with those in Hid Descriptor configuration in the firmware (real/virtual).

CfuVirtualHidDeviceFwUpdate.INF configures the inbox driver to update the CFU Simulation driver CfuVirtualHid.  

As shown below, the INF values match the values specified in the virtual firmware simulation driver's HID descriptor.

[CfuVirtualHidDeviceFwUpdate_HWAddReg]
...
...
HKR,,OfferInputValueCapabilityUsageRangeMinimum,0x00010001,0x1A
HKR,,OfferOutputValueCapabilityUsageRangeMinimum,0x00010001, 0x1E
HKR,,PayloadInputValueCapabilityUsageRangeMinimum,0x00010001,0x26
HKR,,PayloadOutputValueCapabilityUsageRangeMinimum,0x00010001,0x31
HKR,,VersionsFeatureValueCapabilityUsageRangeMinimum,0x00010001, 0x42

Refer: https://github.com/microsoft/CFU/blob/master/Host/CFUFirmwareSimulation/sys/DmfInterface.c  g_CfuVirtualHid_HidReportDescriptor   (HID Report Descriptor)

    ```cpp
    0x85, REPORT_ID_PAYLOAD_INPUT,      // REPORT_ID(34)
    0x75, INPUT_REPORT_LENGTH,          // REPORT SIZE(32)
    0x95, 0x04,                         // REPORT COUNT(4)
    0x19, PAYLOAD_INPUT_USAGE_MIN,      // USAGE MIN (0x26)
    0x29, PAYLOAD_INPUT_USAGE_MAX,      // USAGE MAX (0x29)
    0x81, 0x02,                         // INPUT(0x02)

    0x85, REPORT_ID_OFFER_INPUT,        // REPORT_ID(37)
    0x75, INPUT_REPORT_LENGTH,          // REPORT SIZE(32)
    0x95, 0x04,                         // REPORT COUNT(4)
    0x19, OFFER_INPUT_USAGE_MIN,        // USAGE MIN (0x1A)
    0x29, OFFER_INPUT_USAGE_MAX,        // USAGE MAX (0x1D)
    0x81, 0x02,                         // INPUT(0x02)

    0x85, REPORT_ID_PAYLOAD_OUTPUT,     // REPORT_ID(32)
    0x75, 0x08,                         // REPORT SIZE(8)
    0x95, OUTPUT_REPORT_LENGTH,         // REPORT COUNT(60)
    0x09, PAYLOAD_OUTPUT_USAGE,         // USAGE(0x31)
    0x92, 0x02, 0x01,                   // OUTPUT(0x02)

    0x85, REPORT_ID_OFFER_OUTPUT,       // REPORT_ID(37)
    0x75, INPUT_REPORT_LENGTH,          // REPORT SIZE(32)
    0x95, 0x04,                         // REPORT COUNT(4)
    0x19, OFFER_OUTPUT_USAGE_MIN,       // USAGE MIN (0x1E)
    0x29, OFFER_OUTPUT_USAGE_MAX,       // USAGE MAX (0x21)
    0x91, 0x02,                         // OUTPUT(0x02)

    0x85, REPORT_ID_VERSIONS_FEATURE,   // REPORT_ID(32)
    0x75, 0x08,                         // REPORT SIZE(8)
    0x95, FEATURE_REPORT_LENGTH,        // REPORT COUNT(60)
    0x09, VERSIONS_FEATURE_USAGE,       // USAGE(0x42)
    0xB2, 0x02, 0x01,                   // FEATURE(0x02)
    ```

## Notes on Hardware ID

In order for the inbox driver to communicate with the firmware (real/virtual), the hardware ID specified in the INF should match with what is specified in the Hid Descriptor configuration in the firmware (real/virtual).

As shown below, the CfuVirtualHidDeviceFwUpdate.inf values match the values specified in the virtual firmware simulation driver's HID descriptor.

[Standard.NTamd64]
%CfuVirtualHidDeviceFwUpdate.DeviceDesc%=CfuVirtualHidDeviceFwUpdate, HID\VID_045E&UP:FA00_U:00F5

Refer: https://github.com/microsoft/CFU/blob/master/Host/CFUFirmwareSimulation/sys/DmfInterface.c  g_CfuVirtualHid_HidReportDescriptor   (HID Report Descriptor)

    ```cpp
    0x06, CFU_DEVICE_USAGE_PAGE,        // USAGE_PAGE(0xFA00) 
    0x09, CFU_DEVICE_USAGE,             // USAGE(0xF5)
