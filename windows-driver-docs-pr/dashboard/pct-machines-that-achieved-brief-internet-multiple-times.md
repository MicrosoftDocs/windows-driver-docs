---
title: Percentage of Machines that achieved brief Internet multiple times within an hour on IPv4
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device disconnects cut short of the lease
ms.date: 10/20/2005
ms.topic: concept-article
---

# Percentage of Machines that achieved brief Internet multiple times within an hour on IPv4

## Description

Once a device successfully establishes a IPv4 and connects to Internet, it must maintain that connection throughout that lease session.  This measure monitors the number of disconnect cut short of the lease.  A user's internet should not (thrash) repeatedly drop and reconnect within a short period of time.

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

1. This measure aggregates telemetry from each device. Once DHCP client recognizes an adapter, an IP address is assigned to a device and the device reaches Internet, it is expected to be connected for the Internet for the duration of the IP address lease.  Each disconnect during an hour period is counted.

2. If there are more than 3 disconnects within an hour, the machine for that hour is considered thrashing and counted as 100.  Otherwise, that hour in which at least a single connection attempt happens is counted as 0.  Hour instances are weighted over the number of instance produced by the device and averages among all devices.
