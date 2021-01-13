---
title: Percent of machines that installed a driver update and reported a PnP error code within two days of install
description: The measure aggregates telemetry from a 30-day sliding window into a percentage of machines that successfully installed the driver and then Encountered a PNP error within two days of install
ms.topic: article
ms.date: 05/22/2020
ms.localizationpriority: medium
---

# Percent of machines that installed a driver update and reported a PnP error code within two days of install

## Description

After a successful install, machines can experience post-install PnP errors that can result in a negative user experience; from the device not working as expected to an unexpected reboot. A list of PNP error codes is located on [Device Manager Problem Codes](../install/device-manager-error-messages.md) and [Windows Support](https://support.microsoft.com/help/310123/error-codes-in-device-manager-in-windows).

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|30 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|<=5% machines encounter a post-install PNP error|
|**Cohort-enabled**|Yes|
|**Minimum population per cohort**|500 machines|
|**Measure ID**|26387262|

## Calculation

1. The measure aggregates telemetry from a 30-day sliding window into a **Percentage of Machines that Successfully Installed the Driver, then Encountered a PNP error within 2 days of Install**

   a. Any PNP errors associated with an install outside of the 30-day window are not counted

2. *Post Install PNP Errors=Count(machines with a PNP error,within two days of driver installation)*
3. *Total Post Install Errors=Count(all machines that successfully installed the driver)*

### Final calculation

*Post Install PNP Error Rate= Post Install PNP Errors / Total Post Install Errors*
