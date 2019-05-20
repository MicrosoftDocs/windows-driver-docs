---
title: Driver measure attributes
description: The measures used for driver flighting often share attributes that measure telemetry to the aggregation process to how Microsoft evaluates the measure.
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Driver measure attributes

Microsoft’s set of measures often share attributes in their construction and calculation logic. These attributes are present throughout the measure workflow: from collecting telemetry to the aggregation process to how Microsoft evaluates the measure.
Each measure definition has a section, Measure Attributes, listing the values of its attributes.

## Audience types

There are two types of flighting audiences: the standard audience and the ecosystem audience.

### Standard audience

The HWIDs, CHIDs, OS Floors & Ceilings, and other targeting constraints defined during a driver’s submission determine what machines are eligible to download the driver. Microsoft calls the set of machines in WIP defined by the driver’s targeting the Flighting Audience and calls the set of targeted machines in the retail market the Retail Audience; these audiences are considered **standard audiences**.

### Ecosystem audience

Some measures expand data collection beyond the driver’s submitted HWID, CHID, and OS targets, to reduce sampling noise and increase the measure’s statistical significance. These measures collect additional telemetry from machines that received an identical driver from a different source than the flight. A driver is considered identical to the flighted driver when it has the same Driver INF Version, Driver INF Date, and Architecture. Measures that expand telemetry collection have an **ecosystem audience**.

## Time period

When aggregating telemetry, most measures collect data from a 7-day sliding window; when a driver is in flight for less than 7 days, the sliding window is scoped down to duration of the flight. By scoping data to 7 days, Microsoft can account for differences in a machine’s use between weekdays and the weekend.

Furthermore, when viewing multiple measures, Microsoft knows the failures occurred in the same the period.  

## Machine count and instance count

Measures either determine the percentage of distinct machines experiencing an error or aggregate instances of all errors observed – where a single machine can have multiple instances counted over the flight.

Measures that calculate a percentage of machines are often monitoring for a binary result. For example, the measure *% of Machines where the Driver Install Process completed successfully* is determining whether a driver installed without error and calculates the percentage of machines that successfully installed the driver.

In contrast, measures that evaluate instances can monitor several returned results for a use case. For example, the measure *Camera Preview Failure Rate* is monitoring several camera events related to using the preview feature. The measure is determining how often and at what stage in the preview process machines encounter an error, calculating the average rate of failure for the feature.

## Minimum population and minimum instances

Each measure has an attribute called the **minimum population** or **minimum instances**, defining the minimum count required by the measure’s calculation logic to be statistically significant. If a measure doesn’t have enough data, the driver’s flight status displays **Data Insufficient**.

Measures that evaluate anomalies in expected behavior, like *percentage of Wi-fi sessions that end in an unexpected disconnect*, require larger minimum populations to provide a quality assessment.

## Passing criteria

A measure’s **passing criteria** is the minimum bar of quality a driver must exceed to be approved by Microsoft. This value is assessed with the measure’s Current Value, which is calculated when the measures processes telemetry with its calculation logic.

Microsoft considers a driver to be high-quality if all applied measures exceed their Passing Criteria.

## Measure ID

A measure’s ID is a unique identifier used by Microsoft to simplify communications in evaluation comments when discussing decisions about drivers with external partners.
