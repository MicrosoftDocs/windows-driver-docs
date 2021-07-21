---
title:  Percent of Devices with WinML Runtime Error
description: The measure monitors the overall health and reliability of Windows Machine Learning 
ms.topic: article
ms.date: 8/26/2020
ms.localizationpriority: medium
---

# Percent of Devices with WinML Runtime Error

## Description

This measure monitors the overall health & reliability of Windows Machine learning feature.

The main intent of this measure is to track the percentage of devices experiencing Winml Runtime Error.

The measure uses only WinML Runtime Error telemetry and WinML SessionCreation telemetry.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|30 days|
|**Measurement criteria**|Machine|
|**Minimum population**|30 devices, using confidence intervals|
|**Passing criteria**|Less than 1%|
|**Measure ID**|25419759|

## Calculation

Using daily distinct devices having winml runtime error divided by daily distinct device count that used winml

Measure value = Daily Distinct DeviceId count that sent Winml Runtime error telemetry / Daily Distinct DeviceId count that sent Winml ProcessInfo telemetry
