---
title: Percent of machines with WHEA error after firmware installation
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that have reported a fatal WHEA event over machines successfully installing firmware
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines with Windows Hardware Error Architecture (WHEA) error after firmware installation

## Description

Percent of machines having successful installations that reported a fatal WHEA event (WheaProvider.WheaDriverErrorExternal) after firmware installation.

The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that have reported a fatal WHEA event over machines successfully installing firmware

The WHEA event is only retrieved from 20H1 builds, and will soo be backported to 19H1.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|<= 5%|
|**Measure ID**|23260714|

## Calculation

machines reporting fatal WHEA error /

machines successfully installing firmware (defined by measure 20116729)

