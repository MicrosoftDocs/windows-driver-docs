---
title: Success rate of Fingerprint Enrollment
description: The measure looks at the success of going through the enrollment experience
ms.topic: article
ms.date: 03/30/2020
---
 
# Success rate of Fingerprint Enrollment

## Description 

If a user has a fingerprint sensor attached to their device, they will be offered to enroll their fingerprint to use it as an unlock gesture. The enrollment experience will be launched during the Windows out of box experience or can be launched from settings. This measure monitors success rate of completing that experience.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|10|
|**Passing criteria**|>= 90%|
|**Measure ID**|22162022|

## Calculation

1.	This measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device successfully completes fingerprint enrollment. 
2.	A success is when a user launches the fingerprint enrollment application and is able to commit a template to the biometric database.
3.	A failure is any catastrophic error that causes enrollment to not succeed, including biometric sensor failures.
4.	User initiated cancellations of the enrollment application are filtered from the pool of instances. 

## Final Calculation
Fingerprint enrollment success rate = successful enrollment instances/all instances
