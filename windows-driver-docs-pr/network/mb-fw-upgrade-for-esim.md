---
title: MB Firmware Upgrade for eSIM
description: MB fw upgrade for eSIM
ms.date: 03/01/2021
ms.localizationpriority: medium
---
# Firmware Upgrade for eSIM

## Overview
This document describes the Windows OS changes that support firmware updates for eSIM devices. 

Windows Update (WU) is the model used for the firmware patches. In this model, the eSIM device vendor authors a UMDF driver and adds it to a WU package along with the firmware patch. The package is published to the WU and will be downloaded & installed on Windows devices containing the card vendor’s eSIM device. Once installed the card vendor’s driver writes the firmware patch using the Smart Card WinRT API. Microsoft enables this by providing a UMDF driver for the ISO interface of the eSIM and exposing it as a smart card via the existing Smart Card WinRT API.

The modem ISO interface has a 255-byte limitation as the max Application Protocol Data Unit (APDU) size and is therefore too slow for full firmware OS updates (TRC/PBL image). For full firmware OS updates, Microsoft provides a separate smart card UMDF driver which uses the SPB interface of the eSIM as the transport.

The following acronyms are used in this section:
- **ACPI:** Advanced Configuration and Power Interface
- **APDU:** Application Protocol Data Unit
- **ATR:** Answer to Reset  
- **eUICC:**  Embedded Universal Integrated Circuit Card
- **FW:** Firmware
- **HCP:** Host Controller Protocol
- **HWID:** Hardware ID
- **ISO:** International Organization for Standardization
- **MF:** Master File
- **MSFT:** Microsoft
- **OEM:** Original Equipment Manufacturer
- **PBL:** Primary bootloader
- **RPC:** Remote Procedure Call
- **ScardSvr:** Smart Cards for Windows Service
- **Scard WinRT:** Smart Card Windows Runtime
- **SC DDI:** Smart Card DDI
- **sHDLC:** Simplified High Level Data Link Control
- **SPB:** Simple Peripheral Bus
- **SPI:** Serial Peripheral Interface
- **TRC:** Tamper Resistant Chip
- **WwanSvc:** WWAN Service

### High Level Design for Firmware Patch Update
![High Level Design for Firmware Patch Update.](images\mb-fw-upgrade-esim-high-level-design.png "High Level Design for Firmware Patch Update")

### High Level Design for Firmware OS Update
![High Level Design for Firmware OS Update.](images\mb-fw-upgrade-esim-high-level-os-update.png "High Level Design for Firmware OS Update")

## Firmware Upgrade Architecture

![FW Upgrade for eSIM Block Diagram.](images\mb-fw-upgrade-esim-block-diag.png "FW Upgrade for eSIM Block Diagram")

For Windows 10, version 1703 the card vendor will deliver firmware updates on APDUs over the ISO interface. Updates for full images (PBL HCP) on HCP packets over the SPI interface are planned for the Windows 10, version 1709 time frame. 

The ISO UMDF driver is loaded by the WWAN Service when the WWAN Service detects an eSIM based on the ATR information. The ISO UMDF driver sends APDUs to the eUICC via the modem using the low-level UICC access RPC of the WWAN Service. 

The SPI UMDF driver is loaded by PnP based on the hardware ID in the ACPI entry for the eSIM card. The SPI UMDF driver sends sHDLC frames to the TRC on the card via the SPB IOCTL interface. 

On the upper layer both drivers will implement the Smart Card DDI that provides low-level access for interacting with smart cards. This will expose both the ISO and SPI interfaces of the eSIM as a smart card via the Smart Card WinRT API.

In devices where the SPI interface to eSIM is available, OEMs are expected to add the Microsoft UICC SPI driver HWID to the ACPI table as a hardware compatible ID. The HWID for the Microsoft UICC SPI driver is ACPI\MSFTUICCSPB.

### UMDF drivers

UMDF drivers will implement the following Smart Card IOCTLs:

|Usage|DDI|
|---|---|
|Smart card states|IOCTL_SMARTCARD_GET_STATE<BR>IOCTL_SMARTCARD_IS_ABSENT<BR>IOCTL_SMARTCARD_IS_PRESENT<BR>IOCTL_SMARTCARD_POWER|
|Smart card attributes|IOCTL_SMARTCARD_GET_ATTRIBUTE<BR>IOCTL_SMARTCARD_SET_ATTRIBUTE|
|Smart card communication|IOCTL_SMARTCARD_SET_PROTOCOL<br>IOCTL_SMARTCARD_TRANSMIT|

#### Requirements for smart card devices

Define the following device properties:

|Define|Name|Type|FormatID|Value|
|---|--- |--- |---     |---  |
|Device interface guid|System.Devices.InterfaceClassGuid -- PKEY_Devices_InterfaceClassGuid|Guid -- VT_CLSID|{026E516E-B814-414B-83CD-856D6FEF4822}, 4, DEVPROP_TYPE_GUID|{DEEBE6AD-9E01-47E2-A3B2-A66AA2C036C9}|
|ReaderKind| System.Devices.SmartCards.ReaderKind -- PKEY_Devices_SmartCards_ReaderKind|Byte -- VT_UI1 (should be INT16 Bug 9550228)|{D6B5B883-18BD-4B4D-B2EC-9E38AFFEDA82}, 2, DEVPROP_TYPE_BYTE |SmartCardReaderKind_Uicc|
|ReaderName|DEVPKEY_Device_ReaderName (0xD6B5B883, 0x18BD, 0x4B4D, 0xB2, 0xEC, 0x9E, 0x38, 0xAF, 0xFE, 0xDA, 0x82, 0x03)|String -- VT_LPWSTR  (For variants: VT_BSTR)|{D6B5B883-18BD-4B4D-B2EC-9E38AFFEDA82}, 3, DEVPROP_TYPE_STRING|CustomName|
|AppAccessRestrictionsFlags| System.Devices.SmartCards.ReaderKind -- PKEY_Devices_SmartCards_AppAccessRestrictionsFlags| Byte -- VT_UI1|{D6B5B883-18BD-4B4D-B2EC-9E38AFFEDA82}, 4, DEVPROP_TYPE_BYTE|PrivilegedAppOnly (1)|

The ISO UMDF driver sets additional custom dev properties on the Smart Card reader devnode:

| Define  |Name|Type|FormatID|Value|
|---|--- |--- |---     |---  |
|RadioName|DEVPKEY_MbbDevice_RadioName|: DEVPROP_TYPE_GUID |{41e061f2-9999-4b33-bf42-f950cbfd5f2e}, 1, DEVPROP_TYPE_GUID |RadioInterfaceGuid|
|SlotId|DEVPKEY_MbbDevice_SlotId|DEVPROP_TYPE_UINT32|{c4c66992-3bcc-4f96-9a85-bd807235fbe1}, 2, DEVPROP_TYPE_UINT32|SlotId|
|IsEmbedded|DEVPKEY_MbbDevice_IsEmbedded|DEVPROP_TYPE_BOOLEAN|{7d08a710-b448-4148-8049-0aa12e5fd2dd}, 3, DEVPROP_TYPE_BOOLEAN|IsEmbedded|

These properties are used to uniquely name the smart card readers and identify the reader that is attached to the correct eSIM card. For example: IsEmbedded=True and SlotId=1.

![Additional Custom Properties for UICC ISO SC Driver DevNode.](images\mb-fw-upgrade-esim-Additional-Custom-Properties-for-UICCISOSCDriver-DevNode.png "Additional Custom Properties For UICC ISO SC Driver DevNode")

The TRC Image Update Agent is required to have sharedUserCertificates capability which allows access to the Smart Card WinRT API. The sharedUserCertificates capability is a restricted capability that is only given to enterprises with certain credentials. Once the access is granted, the app can connect to the TRC on the device via the Smart Card API and send commands to the card.

It is expected that the firmware patch is carried over APDUs. Because the Smart Card WinRT API only exposes transmitting APDUs and not channel management functions such as open/close, the UMDF driver will inspect the APDUs and look for a SELECT by AID command. If the driver finds a SELECT by AID command, it will be interpreted as opening a logical channel using the Wwan RPC API. The UMDF driver will always validate that the AID is allowlisted, otherwise it will deny the request. Because there is no close or disconnect IOCTL in the SC DDI, the UMDF driver has no way of knowing when the transmission ends and when to close the logical channel. To prevent leaking of the logical channels, the UMDF driver will set a 5 minute timer when a logical channel is opened and will close the channel when the timer expires. The 5 minutes should be long enough as a firmware update is expected to run up to 2.5 minutes maximum. If the UMDF driver detects a new SELECT by AID command, then it will close the previously opened channel and reset the timer for the new logical channel. Note that 5 minute timeout is measured from the last transmitted APDU. In other words, transmitting an APDU over an existing channel resets the timer.

To prevent from opening channels against random UICC apps, the ISO UMDF driver will permit app IDs that are required for an update and restrict access to only these apps. The card vendor helps identify the app IDs and the OEM adds the IDs as registry entries. It is also expected that the UICC app in the card will perform digital signature checks on the firmware to protect against malicious apps sending data.

##### COSA Setting
`CellCore/PerDevice/eSIM/FwUpdate/AllowedAppIdList`

During a full firmware OS update it is important that the UICC apps that are involved are not accessed by the modem. To achieve this the TRC Image Update Agent will send a special APDU that instructs the eUICC to go in to the TRC/PBL mode. The TRC app will then ask the modem to go into the passthrough mode and reset the card. The card will boot as an empty MF. Once the update is done, the modem will be asked to reset the card again. This time both the modem and the card will get back to normal mode.

## Flow Diagrams
### Connect
![Flow diagram for connecting to SC WinRT.](images\mb-fw-upgrade-esim-connect.png "Connect")
### Transmit (Open Channel)
![Flow diagram for transmit (open channel).](images\mb-fw-upgrade-esim-transmit-open-channel.png "trans open channel")
### Transmit (send APDU and Close Channel)
![Flow diagram for transmit (send APDU and close channel).](images\mb-fw-upgrade-esim-transmit-sendapdu-close-channel.png "Transmit send apdu & close channel")
### Get ATR
![Flow diagram for Get ATR.](images\mb-fw-upgrade-esim-getatr.png "Get ATR")
### Pass-through mode
![Flow diagram for Pass-through Mode.](images\mb-fw-upgrade-esim-passthru.png "pass through")

## Related 
[Preinstall Apps Using DISM Published](/previous-versions/windows/it-pro/windows-8.1-and-8/dn387084(v=win.10)?redirectedfrom=MSDN)

[To add a preinstalled app to a desktop image](/windows-hardware/customize/preinstall/preinstallable-apps-for-windows-10-desktop) 

[Preinstallable apps for mobile devices](/windows-hardware/customize/preinstall/preinstallable-apps-for-window-10-for-phones)

[Preinstall Task](/windows-hardware/customize/preinstall/preinstall-tasks)



