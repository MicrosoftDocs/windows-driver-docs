---
title:  Percent of Devices with WinML Runtime Error (Ecosystem)
description: The measure monitors the overall health and reliability of Windows Machine Learning (Ecosystem)
ms.topic: article
ms.date: 4/29/2020
---

# Percent of Devices with WinML Runtime Error (Ecosystem)

## Description

This is an Ecosystem measure to monitor the overall health & reliability of the GPU execution path in Windows Machine Learning. It tracks the percentage of devices experiencing WinML RuntimeError by using WinML RuntimeError telemetry and WinML SessionCreation telemetry.

This measure will calculate the % of devices that run WinML using GPU sessions and hit WinML RuntimeError. WinML has CPU and GPU execution paths. This measure only considers the results from GPU path.

This is the Ecosystem counterpart of [Percent of devices with WinML Runtime Errors](./pct-devices-winml-runtime-error.md), which means it will include data from multiple driver flights that target the same driver version. The reason to have this Driver Ecosystem measure is because we expect the standard WinML Driver Flight measure could have very limited amount of data. Once the Driver Flight measure doesn’t meet the minimal data requirement, we’ll use this Ecosystem measure to make the decision.

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

We aggregate the runtime error to device level then calculate the % of devices that hit runtime error. The granularity of calculation is  daily basis.

Measure value = COUNT(total devices hit runtime errors) / COUNT(total devices)
