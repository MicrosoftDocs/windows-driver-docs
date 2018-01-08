---
title: DYNAMO
description: DYNAMO
ms.assetid: AA432EAE-A89B-4C4C-9539-BC2763091055
keywords:
- Windows DYNAMO mobile operators
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DYNAMO

## Introduction

DYNAMO is the program in Windows 10, version 1803 and later that enables mobile operators (MOs) and other service providers to sell plans to end users. DYNAMO is a new name for the previous Data Marketplace program and is not a separate or competing program.
DYNAMO enables end users to perform the following:

- Install and activate an eSIM profile.
- Activate a device on a mobile operator subscription with either prepaid (PAYG) or postpaid plans.
- Top up prepaid subscriptions when out of data and the only connectivity available is mobile connectivity.

## Definition of terms

| Term | Description |
| --- | --- |
| Contoso Cellular | A fictional mobile operator used for explanatory purposes in these topics. |
| COSA database | Country and Operator Settings Asset. This is a database that contains mobile operator connectivity settings to be used in Windows devices. For more info about COSA, see [COSA Overview](cosa-overview.md). |
| DYNAMO | The name of this project. |   
| Mobile Plans app | The Microsoft app to enable DYNAMO, formerly known as the Paid Wi-Fi and Cellular (PWC) app. |
| PAYG | Pay As You Go |
| RPS | Requests Per Second |

## Project overview

DYNAMO project integration is composed of four stages, each of which has high-level tasks. Some of these high-level tasks are for mobile operators, while others are joint tasks where Microsoft works in coordination with mobile operators. The following diagram illustrates the four stages of the DYNAMO project.

**IMAGE**

## Functional overview

The following diagram shows a high-level view of how a Windows 10 device uses DYNAMO to interact with different services and solutions to successfully activate a subscription and install an eSIM profile.

The following table describes each component of the diagram.

| Component | Description |
| --- | --- |
| Windows 10 device | An eSIM-capable “Always Connected PC” running the latest version of Windows 10. |
| Microsoft DYNAMO Service | A service endpoint responsible for resolving phone number lookup and providing mobile operator information, such as an MO web portal URL and visual assets, to the Windows 10 device. |
| DYNAMO Web API & Web Portal | The endpoint in the mobile operator network that is responsible for hosting the web service API and web portal that allow Windows 10 devices to access the DYNAMO experience. |
| SMDP+ server | Responsible for creating, generating, and managing eSIM profiles that belong to a mobile operator. |

**IMAGE**

A typical functional flow for the preceding diagram is as follows:

1. The Mobile Plans app, running on the Windows 10 device, resolves phone number lookup in the DYNAMO Service.
2. The Mobile Plans app reaches out to the DYNAMO service to retrieve MO-specific information.
3. The Mobile Plans app launches the MO web portal and passes relevant parameters to the MO portal.
4. The mobile operator requests an eSIM profile from the SM-DP+ server. The eSIM activation code is returned to the DYNAMO mobile operator server.
5. Once control is returned to the Mobile Plans app on the Windows 10 device, the eSIM activation code is provided to the Windows device.
6. The Windows 10 device uses the activation code and contacts the SM-DP+ server to retrieve the eSIM profile. The eSIM profile is now installed and activated on the Windows 10 device.
7. The Windows 10 device is connected to the mobile operator network.

Windows uses the Mobile Plans app as a client to consume the overall DYNAMO experience. This application contacts the MO Web portal and handles all interactions with it. Additionally, once the activation code has been returned, the Mobile Plans app is responsible for downloading, installing, and activating the eSIM profile.

## Get started

To get started with the postpaid DYNAMO experience, follow these steps:

1. [Configuration](dynamo-configuration.md)
2. [Implementation](dynamo-implementation.md)
3. [Integration](dynamo-integration.md)
4. [Launch](dynamo-launch.md)

See these topics for additional info about DYNAMO:

- [Prepaid experience](dynamo-prepaid-experience.md)
- [Appendix](dynamo-appendix.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Mobile%20operator%20scenarios%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")