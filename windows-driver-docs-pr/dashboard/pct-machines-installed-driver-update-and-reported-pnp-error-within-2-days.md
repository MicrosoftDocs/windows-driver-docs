---
title: Machines that reported a PnP error code within two days of installing a driver update
description: The measure aggregates data from a 30-day sliding window into a percentage of machines that successfully installed the driver and then encountered a Plug and Play error within two days of install.
ms.date: 07/15/2024
---

# Machines that reported a Plug and Play (PnP) error code within two days of installing a driver update

## Description

Machines can experience post-installation Plug and Play (PnP) errors that result in a negative user experience; from the device not working as expected to an unexpected reboot. A list of PnP error codes is located on [Device Manager Problem Codes](../install/device-manager-error-messages.md) and [Error codes in Device Manager in Windows](https://support.microsoft.com/topic/error-codes-in-device-manager-in-windows-524e9e89-4dee-8883-0afa-6bca0456324e).

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Expanded |
| **Time period** | 30 day sliding window |
| **Measurement criteria** | Aggregation of machines |
| **Minimum population** | 100 machines |
| **Passing criteria** | <=5% machines encounter a post-install PnP error |
| **Cohort-enabled** | Yes |
| **Minimum population per cohort** | 500 machines |
| **High failure rate target** | <= 50% |
| **High failure minimum population** | 10 machines |
| **Measure ID** | 26387262 |

## Calculation

1. The measure aggregates data from a 30-day sliding window into a percentage of machines that successfully installed the driver, then encountered a PnP error within two days of installation
   1. Any PnP errors associated with an install outside of the 30-day window aren't counted

1. Post installation PnP errors = Count(machines with a PnP error,within two days of driver installation)
1. Total post installation errors = Count(all machines that successfully installed the driver)

### Final calculation

Post installation PnP error rate = post installation PnP errors / total post installation errors
