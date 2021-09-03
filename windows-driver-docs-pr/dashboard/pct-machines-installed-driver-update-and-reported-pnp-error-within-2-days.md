---
title: Percent of machines that reported a PnP error code within two days of installing a driver update
description: The measure aggregates telemetry from a 30-day sliding window into a percentage of machines that successfully installed the driver and then Encountered a PNP error within two days of install
ms.topic: article
ms.date: 09/02/2021
ms.localizationpriority: medium
---

# Percent of machines that reported a PnP error code within two days of installing a driver update

## Description

Machines can experience post-installation PnP errors that result in a negative user experience; from the device not working as expected to an unexpected reboot. A list of PNP error codes is located on [Device Manager Problem Codes](../install/device-manager-error-messages.md) and [Windows Support](https://support.microsoft.com/help/310123/error-codes-in-device-manager-in-windows).

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Expanded |
| **Time period** | 30 day sliding window |
| **Measurement criteria** | Aggregation of machines |
| **Minimum population** | 100 machines |
| **Passing criteria** | <=5% machines encounter a post-install PNP error |
| **Cohort-enabled** | Yes |
| **Minimum population per cohort** | 500 machines |
| **High failure rate target** | <= 50% |
| **High failure minimum population** | 10 machines |
| **Measure ID** | 26387262 |

## Calculation

1. The measure aggregates telemetry from a 30-day sliding window into a percentage of machines that successfully installed the driver, then encountered a PNP error within 2 days of installation
   1. Any PNP errors associated with an install outside of the 30-day window are not counted

1. Post installation PNP errors = Count(machines with a PNP error,within two days of driver installation)
1. Total post installation errors = Count(all machines that successfully installed the driver)

### Final calculation

Post installation PNP error rate = post installation PNP errors / total post installation errors
