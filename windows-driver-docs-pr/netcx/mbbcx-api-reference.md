---
title: MBBCx API reference
description: This topic contains API reference topics for Mobile Broadband WDF Class Extension (MBBCx) client drivers.
ms.assetid: 7DCC9FE8-200F-4EC6-9DDA-B478B474F887
keywords:
- Mobile Broadband WDF Class Extension API reference, MBBCx API reference
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBBCx API reference

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

This topic contains API reference topics for Mobile Broadband WDF Class Extension (MBBCx) client drivers. These APIs and data structures are found in the Mbbcx.h header.

## Callback functions

- *[EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT](evt-mbb-device-send-mbim-fragment.md)*
- *[EVT_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT](evt-mbb-device-receive-mbim-fragment.md)*
- *[EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA](evt-mbb-device-send-service-session-data.md)*
- *[EVT_MBB_DEVICE_CREATE_ADAPTER](evt-mbb-device-create-adapter.md)*

## Structures
- **[MBB_DEVICE_CONFIG](mbb-device-config.md)**
- **[MBB_DEVICE_MBIM_PARAMETERS](mbb-device-mbim-parameters.md)**

## Methods

- [MBB_DEVICE_CONFIG_INIT](mbb-device-config-init.md)
- [MBB_DEVICE_MBIM_PARAMETERS_INIT](mbb-device-mbim-parameters-init.md)
- [MbbDeviceInitConfig](mbbdeviceinitconfig.md)
- [MbbDeviceInitialize](mbbdeviceinitialize.md)
- [MbbDeviceSetMbimParameters](mbbdevicesetmbimparameters.md)
- [MbbDeviceResponseAvailable](mbbdeviceresponseavailable.md)
- [MbbDeviceArmWake](mbbdevicearmwake.md)
- [MbbDeviceDisarmWake](mbbdevicedisarmwake.md)
- [MbbDeviceSendServiceSessionDataComplete](mbbdevicesendservicesessiondatacomplete.md)
- [MbbDeviceReceiveServiceSessionData](mbbdevicereceiveservicesessiondata.md)
- [MbbAdapterInitialize](mbbadapterinitialize.md)
- [MbbAdapterGetSessionId](mbbadaptergetsessionid.md)
- [MbbRequestGetBuffer](mbbrequestgetbuffer.md)
- [MbbRequestGetActivityId](mbbrequestgetactivityid.md)
- [MbbRequestComplete](mbbrequestcomplete.md)
- [MbbRequestCompleteWithInformation](mbbrequestcompletewithinformation.md)