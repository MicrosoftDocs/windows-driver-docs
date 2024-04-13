---
title: Percent of Camera initialization failures
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a camera device failed to initialize
ms.topic: article
ms.date: 05/20/2019
---

# Percent of Camera initialization failures

## Description

When a someone tries to use an application that accesses the machine’s camera device, the camera feature must first be initialized. If this initialization fails, the user cannot use the machine’s camera to capture content and must restart initialization process.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|10 instances|
|**Passing criteria**|<= 5% of Instances result in an initialization failure|
|**Measure ID**|16998810|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of instances where a camera device failed to initialize**.

   a. A unique device can have one initialization Instance counted per hour.

2. Types of Instances:

   a. *Successful inialization event = 0% failure*

```cpp
MF_CAPTURE_ENGINE_INITIALIZED with an HRESULT == 0
```

   b. *Failed initialization event = 100% failure*

```cpp
i. MF_E_NO_CAPTURE_DEVICES_AVAILABLE

ii. E_ACCESSDENIED

iii. ERROR_BAD_UNIT
```

### Final calculation

*Camera initialization failure rate = average (all instances)*
