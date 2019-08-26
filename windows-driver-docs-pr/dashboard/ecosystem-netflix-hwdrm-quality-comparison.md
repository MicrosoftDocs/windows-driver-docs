---
title: Ecosystem Netflix HWDRM Quality Comparison
description: The measure aggregates telemetry from a 28 day sliding window into a binary value (0 or 1), indicating if the driver performance is within 2 standard deviations of the aggregate performance of all drivers from the same IHV in the retail market
ms.topic: article
ms.date: 08/19/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Ecosystem Netflix HWDRM Quality Comparison

## Description

Hardware Digital Rights Management (HWDRM) is a feature that enable secure playback of High Definition and Ultra High Definition content on multiple device platforms. This feature protects digital keys – like private keys and content keys – and compressed & uncompressed video and audio. A HWDRM failure causes the user to be unable to playback videos on certain services, such as Netflix. Drivers whose session failure rate is within 2 standard deviations of the average session failure rates for all drivers in retail from the same IHV, pass.  Those drivers with session failure rates higher, fail.  

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|28-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|1 instance|
|**Passing criteria**|Driver session failure rate is within 2 standard deviations of average session failure rate across all drivers|
|**Measure ID**|19170127|

## Calculation

1.	The measure aggregates telemetry from a 28 day sliding window into a **binary value (0 or 1)**, indicating if the driver performance is within 2 standard deviations of the aggregate performance of all drivers from the same IHV in the retail market
	i.	A measure result of 0 is successful, meaning the driver’s performance is within the 95% of all retail drivers’ performance 
2.	*Evaluated Driver Session Failure Rate = Count(Failed Sessions) / Count(Total Sessions)*
3.	*Retail Driver Session Failure Rates = Count(Failed Sessions) / Count(Total Sessions)*
	i.	Calculated once for all other graphics drivers from the same IHV in the retail market
4.	*Retail Driver Failure Rate Mean = Mean(Retail Driver Session Failure Rates)*
5.	*Retail Driver Failure Rate Standard Deviation = Standard-Deviation(Retail Driver Session Failure Rate)*
6.	*Standard Deviation 2 Upper Bound = Mean + (Retail Driver Failure Rate Standard Deviation * 2)*

### Final Calculation
8.	*Netflix HWDRM Retail Comparison = 
	i.	0, if Evaluated Driver Standard Failure Rate  =< Standard Deviation 2 Upper Bound
	ii.	Else, Netflix HWDRM Retail Comparison = 1* 

