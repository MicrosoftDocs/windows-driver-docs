---
title: Mobile Plans use cases
description: This topic describes the basic user cases that Mobile Operators could implement.
ms.assetid: 24050B13-4A1A-466F-974B-40B34EDB16DC
keywords:
- Windows Mobile Plans User cases, Mobile Plans implementation mobile operators
ms.date: 05/31/2019
ms.localizationpriority: medium
---

# Mobile Plans use cases

## Overview

This topic provides insights about most common use cases that mobile operators can enable with Mobile Plans. Note that this is not an exhaustive list of supported cases. It is probable that your specific use case could be achieved via a combination of solutions. Please reach out to your Microsoft contact to discuss your scenario further.

## Install an eSIM profile on a Windows device

This section describes what a mobile operator should implement to activate, download, and install an eSIM profile on a Windows device. Depending on the particular conditions of your network backend and how long the activation process takes, you can implement more than one way to return control to Mobile Plans app.

Follow these steps:

1. Implement the [Mobile Plans web portal](mobile-plans-web-portal.md#web-service-api-used-for-esim).
2. Implement a way to give control back to the Mobile Plans app.
   1. [Immediate eSIM profile download](mobile-plans-callback-notifications.md#immediate-esim-profile-download-and-activation). Implement this callback if the eSIM profile is immediately available in the SM-DP+ server and the device can attach to the cellular network immediately.
   2. [Asynchronous Connectivity](mobile-plans-callback-notifications.md#asynchronous-connectivity). Implement this callback if the eSIM profile is immediately available in the SM-DP+ server, but the device needs to wait some time before attaching to the cellular network.
   3. [Deferred eSIM profile download](mobile-plans-callback-notifications.md#deferred-esim-profile-download-and-activation). Implement this callback if the eSIM profile is available in your SM-DP+ server after a period of time and the device is able to attach to the cellular network immediately.
3. [Handle eSIM download errors](mobile-plans-eSIM-error-handling.md). (Optional)
4. Define the [basic device experience](mobile-plans-device-experience.md#basic-device-experience).
5. Provide [Mobile Plans service configuration](mobile-plans-service-configuration.md) information.
6. [Validate](mobile-plans-integration.md) the implementation.
7. Commercial [launch](mobile-plans-launch.md).

## Add balance to a current subscription

This section describes the work needed to add balance to your current subscription. This is useful if you are selling prepaid plans or if you sell data packages once a postpaid subscription runs out of Internet data.

1. Implement the [Mobile Operator web portal](mobile-plans-web-portal.md).
2. Implement the [adding balance](mobile-plans-callback-notifications.md#adding-balance) to hand control back to Mobile Plans.
3. Implement the [enhanced device experience](mobile-plans-device-experience.md#enhanced-device-experience).
   1. Implement the [Get Balance API](mobile-plans-device-experience.md#getbalance-api).
   2. Implement the [Walled Garden](mobile-plans-device-experience.md#walled-garden).
4. Provide [Mobile Plans service configuration](mobile-plans-service-configuration.md) information.
5. [Validate](mobile-plans-integration.md) the implementation.
6. Commercial [launch](mobile-plans-launch.md).

## Cancelling a transaction

This section describes the control callback to use for notifying the Mobile Plans app when a transaction is canceled while the user is in the mobile operator web portal. This applies to all the previous scenarios in this topic.

- Implement the [Canceling purchase flow](mobile-plans-callback-notifications.md#canceling-purchase-flow) control.

## Activate a warm SIM in a Windows device

This section describes what a mobile operator should implement to activate a warm SIM profile in a Windows device.

Follow these steps:

1. Implement the [Mobile Operator web portal](mobile-plans-web-portal.md#web-service-api-used-for-a-physical-sim).
2. Implement the [adding balance](mobile-plans-callback-notifications.md#adding-balance) to hand control back to Mobile Plans.
3. Implement the [enhanced device experience](mobile-plans-device-experience.md#enhanced-device-experience).
   1. Implement the [Get Balance API](mobile-plans-device-experience.md#getbalance-api).
   2. Implement the [Walled Garden](mobile-plans-device-experience.md#walled-garden).
4. Provide [Mobile Plans service configuration](mobile-plans-service-configuration.md) information.
5. [Validate](mobile-plans-integration.md) the implementation.
6. Commercial [launch](mobile-plans-launch.md).