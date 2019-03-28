---
title: Mobile Plans Use Cases
description: This topic describes the basic user cases that Mobile Operators could implement.
ms.assetid: 24050B13-4A1A-466F-974B-40B34EDB16DC
keywords:
- Windows Mobile Plans User cases, Mobile Plans implementation mobile operators
ms.date: 03/25/2019
ms.localizationpriority: medium
---

# Mobile Plans Use Cases

## Overview

This topic provides insights about most common use cases that mobile operators are planning to enable, this is not an exhaustive list of supported cases. It is probable that your specific user case could be achieved via a combination of solutions. Please reach your Microsoft contact to discuss further your scenario.

## Install an eSIM profile in a Windows device

This section describes what a mobile operator should implement to activate, download and install an eSIM profile in a Windows device. Depending on which are the particular conditions of your network backend and how long the activation process will take you could choose to implement more than one way to return control to Mobile Plans app.
Please follow these steps:

1. Implement the [Mobile Operator web portal](mobile-plans-web-portal.md#web-service-api-used-for-esim)
2. Implement the adequate control back to Mobile Plans
   1. [Inline profile Delivery](mobile-plans-callbacks.md#inline-profile-delivery), implement this callback if the eSIM profile is immediately available in the SMDP+ server and the device will be able to attach to the cellular network immediately.
   2. [Asynchronous Connectivity](mobile-plans-callbacks.md#asynchronous-connectivity), implement this callback if the eSIM profile is immediately available in the SMDP+ server but the device will need to wait some time before attach to the cellular network.
   3. **Asynchronous Profile Download**, implement this callback if the eSIM profile will be available in your SMDP+ server after a period of time and the device will be able to attach to the cellular network immediately.
3. [Handling eSIM download errors](mobile-plans-eSIM-error-handling.md) (Optional)
4. Define the [basic device experience](mobile-plans-device-experience.md#basic-device-experience).
5. Provide [Mobile Plans configuration](mobile-plans-configuration.md) information
6. [Validate](mobile-plans-integration.md) the implementation.
7. Commercial [launch](mobile-plans-launch.md)

## Add balance to a current subscription

This section describes which work is needed to add balance to your current subscription, this is useful if you are selling prepaid plans or if you sell data packages once a postpaid subscription runs out of Internet data.

1. Implement the [Mobile Operator web portal](mobile-plans-web-portal.md)
2. Implement the [adding balance](mobile-plans-callbacks.md#adding-balance) control back to Mobile Plans.
3. Implement the [enhanced device experience](mobile-plans-device-experience.md#enhanced-device-experience)
   1. Implement the [Get Balance API](mobile-plans-device-experience.md#getbalance-api)
   2. Implement the [Walled Garden](mobile-plans-device-experience.md#walled-garden)
4. Provide [Mobile Plans configuration](mobile-plans-configuration.md) information
5. [Validate](mobile-plans-integration.md) the implementation.
6. Commercial [launch](mobile-plans-launch.md)

## Cancelling a transaction

This section describes which control back should be used to notify the Mobile Plans app, when a transaction is cancelled while the user is in the mobile operator web portal. This applies to all the above scenarios.

- Implement the [Cancelling purchase flow](mobile-plans-callbacks.md#cancelling-purchase-flow) control

## Activate a warm SIM in a Windows device

This section describes what a mobile operator should implement to activate a warm SIM profile in a Windows device.
Please follow these steps:

1. Implement the [Mobile Operator web portal](mobile-plans-web-portal.md#web-service-api-used-for-physical-sim)
2. Implement the [adding balance](mobile-plans-callbacks.md#adding-balance) control back to Mobile Plans.
3. Implement the [enhanced device experience](mobile-plans-device-experience.md#enhanced-device-experience)
   1. Implement the [Get Balance API](mobile-plans-device-experience.md#getbalance-api)
   2. Implement the [Walled Garden](mobile-plans-device-experience.md#walled-garden)
4. Provide [Mobile Plans configuration](mobile-plans-configuration.md) information
5. [Validate](mobile-plans-integration.md) the implementation.
6. Commercial [launch](mobile-plans-launch.md)
