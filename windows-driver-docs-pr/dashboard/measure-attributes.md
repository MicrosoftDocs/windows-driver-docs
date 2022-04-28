---
title: Driver measure attributes
description: The measures used for driver flighting often share attributes that measure telemetry to the aggregation process to how Microsoft evaluates the measure.
ms.topic: article
ms.date: 05/20/2019
---

# Driver measure attributes

Microsoft’s set of measures often share attributes in their construction and calculation logic. These attributes are present throughout the measure workflow: from collecting telemetry to the aggregation process to how Microsoft evaluates the measure.
Each measure definition has a section, *Measure attributes*, listing the values of its attributes.

## Audience types

Microsoft defines an audience as the set of machines that can download a flighted, gradually rolled-out, or released driver. These drivers can be delivered to machines by Windows Update (WU) or a 3rd party downloader. There are 3 types of audiences: **standard audiences**, **expanded audiences**, and **ecosystem audiences**.

### Standard audience

Measures with standard audiences only collect telemetry from machines that received the driver directly from WU and align with the driver’s targeting constraints set during submission, like HWID, CHID, OS Floors and Ceilings. 

### Expanded audience

Measures with expanded audiences collect telemetry from machines that align with a driver’s targeting constraints and received the driver from any source, including 3rd party downloaders.

### Ecosystem audience

Measures with ecosystem audiences expand data collection beyond a driver’s targeting constraints to reduce sampling noise and increase the measures’ statistical significance. These measures collect telemetry from any machine that downloaded the driver from any source, including untargeted machines that downloaded an identical version of the driver. 

A driver is considered identical to another driver when they share the same Driver INF Version, Driver INF Date, and Architecture. 

## Time period

When aggregating telemetry, most measures collect data from a 7-day sliding window; when a driver is in flight for less than 7 days, the sliding window is scoped down to duration of the flight. By scoping data to 7 days, Microsoft can account for differences in a machine’s use between weekdays and the weekend.

Furthermore, when viewing multiple measures, Microsoft knows the failures occurred in the same the period.  

## Measurement Criteria - Machine count and instance count

Measures either determine the percentage of distinct machines experiencing an error or aggregate instances of all errors observed – where a single machine can have multiple instances counted over the flight.

Measures that calculate a percentage of machines are often monitoring for a binary result. For example, the measure *% of Machines where the Driver Install Process completed successfully* determines whether a driver installed without error and calculates the percentage of machines that successfully installed the driver.

In contrast, measures that evaluate instances can monitor several returned results for a use case. For example, the measure *Camera Preview Failure Rate* monitors several camera events related to using the preview feature. The measure determines how often and at what stage in the preview process machines encounter an error, calculating the average rate of failure for the feature.

## Minimum population and minimum instances

Each measure has an attribute called the **minimum population** or **minimum instances**, defining the minimum count required by the measure’s calculation logic to be statistically significant. If a measure doesn’t have enough data, the driver’s flight status displays **Data Insufficient**.

Measures that evaluate anomalies in expected behavior, like *percentage of Wi-fi sessions that end in an unexpected disconnect*, require larger minimum populations to provide a quality assessment.

## Passing criteria

A measure’s **passing criteria** is the minimum bar of quality a driver must exceed to be approved by Microsoft. This value is assessed with the measure’s Current Value, which is calculated when the measures processes telemetry with its calculation logic.

Microsoft considers a driver to be high-quality if all applied measures exceed their Passing Criteria.

## Measure ID

A measure’s ID is a unique identifier used by Microsoft to simplify communications in evaluation comments when discussing decisions about drivers with external partners.
