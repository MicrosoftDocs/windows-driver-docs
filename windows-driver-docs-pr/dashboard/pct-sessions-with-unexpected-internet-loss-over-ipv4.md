---
title: Percentage of Sessions with unexpected Internet loss over IPv4
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a there are unexpected disconnects
ms.date: 10/20/2005
ms.topic: concept-article
---

# Percentage of Sessions with unexpected Internet loss over IPv4

## Description

Once a device successfully establishes a IPv4 and connects to Internet, the user should expect a stable connection with little to no Internet loss.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Machine vs. Instance** | Instance |
| **Minimum instances** | 100 instances |
| **Passing criteria** | <= 3% of instances end up with unexpected disconnects |
| **Measure ID** | 55883614 |

## Calculation

1. This measure calculates the percentage of instances aggregated per device that have at least one unexpected Internet loss.  After gaining Internet above, Internet loss occurs when NCSI CapabilityChange event is fired during a DHCP connectivity session with the old capability being Internet.
