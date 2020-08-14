---
title:  Percent of Device with WinML Runtime Error (Ecosystem)
description: The measure monitors the overall health and reliability of Windows Machine Learning 
ms.topic: article
ms.date: 4/29/2020
ms.localizationpriority: medium
---

# Percent of Device with WinML Runtime Error (Ecosystem)

## Description

This is a ecosystem measure to monitor the overall health & reliability of the GPU execution path in Windows Machine learning. It tracks the percentage of devices experiencing WinML Runtime Error by using WinML RuntimeError telemetry and WinML SessionCreation telemetry.

This measure will calculate the % of devices that run WinML using GPU sessions and hit WinML Runtime Error. WinML has CPU and GPU execution paths. This measure only considers the results from GPU path. 

This is a Ecosystem counterpart of [Percent of devies with WinML Runtime Errors](https://docs.microsoft.com/windows-hardware/drivers/dashboard/pct-devices-winml-runtime-error), which means it will includes data from multiple driver flights that target the same driver version. The reason to have this Driver Ecosystem measure is we expect the standard WinML Driver Flight measure could have very limited amount of data. Once the Driver Flight measure doesn’t meet minimal data requirement, we’ll use this Ecosystem measure to make the decision.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|30 days|
|**Measurement criteria**|Machine|
|**Minimum population**|30 devices, using confidence intervals|
|**Passing criteria**|Less than 1%|
|**Measure ID**|27057557|

## Calculation

We aggregate the runtime error to device level. And calculate how many % of devices that hit runtime error. The granularity of calculation is daily bases. 

Measure value = COUNT(total devices hit runtime errors) / COUNT(total devices)
