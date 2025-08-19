---
title: Percent of machines where the driver install process completes successfully
description: The measure aggregates telemetry from a 30-day sliding window into a Percentage of Machines that have Successfully Installed the Driver
ms.date: 07/20/2021
ms.topic: concept-article
---

# Percent of machines where the driver install process completes successfully

## Description

When a driver fails to install correctly, the targeted component can lose functionality and prevent the user from accessing the component's features. The user must troubleshoot the issue to regain functionality. A list of PNP error codes is located on [Device Manager Problem Codes](../install/device-manager-error-messages.md) and on [Windows Support](https://support.microsoft.com/topic/error-codes-in-device-manager-in-windows-524e9e89-4dee-8883-0afa-6bca0456324e).

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|30 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|>= 95% of machines install the driver successfully|
|**Cohort-enabled**|Yes|
|**Minimum population per cohort**|500 machines|
|**High failure rate target**|<= 50%|
|**High failure minimum population**|10 machines|
|**Measure ID**|26387215|

## Calculation

1. The measure aggregates telemetry from a 30-day sliding window into a **Percentage of Machines that have Successfully Installed the Driver**.
2. *Successful Installs= Count(machines with successful PNP events)*
3. *Total Installs= Count(machines that started the driver install process)*

### Final Calculation

*PNP Success Rate= Successful Installs / Total Installs*
