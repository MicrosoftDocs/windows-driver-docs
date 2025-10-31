---
title: Percentage of Machines That Achieved Brief Internet Multiple Times Within An Hour Over IPv4
description: The measure aggregates telemetry from a seven-day sliding window into a percentage of machines where there are unexpected repeated drops and connects
ms.date: 10/31/2005
ms.topic: concept-article
---

# Percentage of machines that achieved brief Internet multiple times within an hour over IPv4

Frequent and brief Internet connectivity interruptions can degrade user experience, disrupt application performance, and signal underlying network instability. This measure identifies machines that exhibit repeated short-lived connections within a one-hour window, a behavior commonly referred to as "thrashing." By quantifying the percentage of affected machines over a seven-day period, this metric helps network administrators and service providers detect and address reliability issues in IPv4 environments.

## Description

Once a device successfully establishes a IPv4 connection and connects to the Internet, it must maintain that connection throughout that lease session.
This measure monitors the number of disconnects that were cut short before the lease expiry. A user's internet shouldn't repeatedly drop and reconnect ("thrash") within a short
period of time.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Machine vs. Instance** | Instance |
| **Minimum instances** | 100 instances |
| **Passing criteria** | <= 5% of instances end up with unexpected disconnects |
| **Measure ID** | 55883634 |

## Calculation

1. This measure aggregates telemetry from each device. When the Dynamic Host Configuration Protocol (DHCP) client detects an adapter, it assigns an IP address to the device. After the device connects to the Internet, it's expected to stay connected for the duration of the IP address lease. Each disconnect during an hour period is counted.

2. If there are more than 3 disconnects within an hour, the machine for that hour is considered "thrashing" and counted as 100. Otherwise, that hour in which at least a single
connection attempt happens is counted as 0. Hour instances are weighted over the number of instances produced by the device, and averages among all devices.
