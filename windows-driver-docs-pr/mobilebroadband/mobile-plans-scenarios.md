---
title: Mobile Plans scenarios
description: This topic describes the basic end user facing scenarios that mobile operators can implement.
keywords:
- Windows Mobile Plans scenarios, Mobile Plans implementation mobile operators
ms.date: 05/31/2019
ms.localizationpriority: medium
---

# Mobile Plans scenarios

## Overview

This topic provides guidance about most common scenarios that mobile operators will enable with Mobile Plans. Note that this is not an exhaustive list of supported scenarios. It is probable that your specific use case could be achieved via a combination of solutions. Please speak with your Microsoft contact to discuss your requirements further.

## Install an eSIM profile on a Windows 10 device

This section describes the steps a mobile operator should take to download, install and activate an eSIM profile on a Windows 10 device. Depending upon constrainsts of the mobile operator's eSIM platform and network backend, there are multiple methods used to fulfill the profile and network connectivity at the conclusion of the activation flow.

1. Develop the [mobile operator web portal](mobile-plans-web-portal.md#web-portal-interface-for-esim-enabled-devices) that will take the user through the sign in and activation steps.
2. Implement one of the supported callback methods to return control back to the Mobile Plans app for download of the eSIM profile:
   1. [Inline profile download and connectivity](mobile-plans-callback-notifications.md#inline-profile-download-and-connectivity) - This callback method should be used when the profile is already available to be released by the SM-DP+ server, AND the profile will enable the device to register on the cellular network immediately upon profile activation. This method enables profile delivery and network connection as part of the same end user flow.
   2. [Asynchronous connectivity](mobile-plans-callback-notifications.md#asynchronous-connectivity). This callback method should be used when the eSIM profile is already available for release by the SM-DP+ server, however the device needs to wait some time before attempting to register on the cellular network.
   3. [Delayed profile download](mobile-plans-callback-notifications.md#delayed-esim-profile-download-and-activation). This callback method should be used when the profile is not available to be released by the SM-DP+ server, and can only be downloaded after a period of time. It is expected that the device will be able to register on the cellular network once the profile is downloaded and installed.
3. Ensure proper [handling of profile download errors](mobile-plans-eSIM-error-handling.md).
4. Implement the [basic account management experience](mobile-plans-account-management.md#basic-account-management-experience) for users to manage and maintain their account.

## Activate a warm SIM in a Windows device

This section describes the steps to allow users to activate a warm phsycial SIM in a Windows device. The term 'warm' refers to a SIM which has been preactivated and can connect to the mobile operator network, but has not been associated with an active subscription.

1. Implement the [mobile operator web portal](mobile-plans-web-portal.md#web-portal-interface-for-physical-sims) that will walk the user through the sign in and activation steps.
2. Implement the callback method for [adding balance](mobile-plans-callback-notifications.md#adding-balance).
3. Implement the [enhanced account management experience](mobile-plans-account-management.md#enhanced-account-management-experience).
   1. Implement the [GetBalance method](mobile-plans-account-management.md#getbalance-api) as part of the mobile operator API.
   2. Implement the [Walled Garden](mobile-plans-walled-garden.md) so users can navigate to the mobile operator web portal even if they don't have an active balance.

## Add balance to a current subscription

This section describes the steps invovled in adding balance for an existing customer subscription. This is useful when a mobile operator is selling prepaid data plans that must be topped off when the balance runs out.

1. Develop the [mobile operator web portal](mobile-plans-web-portal.md).
2. Implement the callback method for [adding balance](mobile-plans-callback-notifications.md#adding-balance).
3. Implement the [enhanced account management experience](mobile-plans-account-management.md#enhanced-account-management-experience).
   1. Implement the [GetBalance method](mobile-plans-account-management.md#getbalance-api) as part of the mobile operator API, allowing the user's balance to be shown in the Windows network flyout.
   2. Implement the [Walled Garden](mobile-plans-walled-garden.md) so users can navigate to the mobile operator web portal even if they don't have balance remaining.

## Cancelling a transaction

This section describes the callback method used to notify the Mobile Plans app when a transaction is cancelled while the user is browsing the mobile operator web portal. This applies to all the previous scenarios in this topic.

- Implement the callback method for [canceling purchase flow](mobile-plans-callback-notifications.md#canceling-purchase-flow).
