---
title: Myriad of drivers that were rolled back or re-installed within 2 days of installation (Ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines that were rolled back or re-installed within 2 days of installation (Ecosystem)
ms.topic: article
ms.date: 05/11/2020
ms.localizationpriority: medium
---

# Myriad of drivers that were rolled back or re-installed within 2 days of installation (Ecosystem)

## Description

This measure is tracking whether a driver is rolled back or succeeded by another driver install (not initiated by WU) within 2 days of the installation. Such actions signal that user is having problems with a driver severe enough that they need to use a different driver.

This is the ecosystem counterpart of [Myriad of drivers that were rolled back or re-installed within 2 days of installation](./myriad-drivers-rolled-back-standard.md) measure.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Machine count|
|**Minimum population**|5,000 Devices|
|**Passing criteria**|<= 10 rollbacks per 10,000 devices that installed the driver|
|**Measure ID**|26124773|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into the Ratio of Driver Rollbacks/​Another Driver Installs per 10,000 devices that installed this driver

Total Devices That Rolled Back Or Installed Another Driver = Count(devices that rolled back or installed another driver within 2 days from the driver installation)

Total Devices = Count(Devices that installed the driver and used it for 2 days)

### Final Calculation

Ratio of Driver Rollbacks/Another Driver Installs = Total Devices That Rolled Back Or Installed Another Driver * 10,000 / Total Devices
